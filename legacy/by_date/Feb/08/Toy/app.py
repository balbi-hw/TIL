# app.py
import streamlit as st

# ===== your imports (필요한 것만) =====
import json
import os
from datetime import datetime

DATA_PATH = "data/notes.json"

# ===== storage (이미 만든 버전이 있으면 그대로 쓰세요) =====

# load_notes func
# notes.json 파일, 즉 기록이 로컬에 존재하는지를 판단한 뒤 존재하면 데이터를 불러오고 아니라면 새 기록을 만들 준비를 한다.

# save_notes func
# 데이터가 없다면 기입한 데이터를 저장하고 이미 있다면 그 데이터에 업데이트 한다.

def load_notes():
    if not os.path.exists(DATA_PATH):
        return {}
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_notes(notes: dict):
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)

# ===== your functions (여기에 현우님 함수 붙여넣기) =====

# 추가한 기능
# match | parse_input | add | search

# match func
# 입력 받은 텍스트가 데이터 안에 존재하는지 판단한다.

def match(text, kw):
    return kw in str(text).lower()

# parse_input func
# 입력을 데이터화 하는 함수

def parse_input(text: str):
    parts = [p.strip() for p in text.split('|') if p.strip()]
    cmd = parts[0].lower() if parts else ""
    tokens = parts[1:]

    fields = {}
    free = []

    for t in tokens:
        if '=' in t:
            k, v = t.split('=', 1)
            fields[k.strip().lower()] = v.strip()
        else:
            free.append(t.strip())

    # 정규화
    if "platform" in fields:
        fields["platform"] = fields["platform"].upper()

    # tags 리스트화
    if "tags" in fields and isinstance(fields["tags"], str):
        fields["tags"] = [x.strip() for x in fields["tags"].split(",") if x.strip()]

    return cmd, fields, free

# handle_add func
# parse_input 에서 뽑아낸 커맨드가 add 일 경우 불러오는 함수
# 필수값의 존재여부를 판단하고 데이터에 추가한다.

def handle_add(fields, notes):
    required = ["platform", "id", "cause"]
    for r in required:
        if r not in fields:
            return False, "필수 필드가 부족합니다: platform, id, cause", notes

    key = f"{fields['platform']}-{fields['id']}"

    if key not in notes:
        notes[key] = {
            "platform": fields["platform"],
            "problem_id": fields["id"],
            "tags": fields.get("tags", []),
            "logs": []
        }
    else:
        # tags가 새로 들어오면 합치고 싶으면 여기서 합칠 수 있음(선택)
        pass

    log = {
        "cause": fields["cause"],
        "counterexample": fields.get("counterexample", ""),
        "fix": fields.get("fix", ""),
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    notes[key]["logs"].append(log)
    return True, f"추가 완료: {key} (logs={len(notes[key]['logs'])})", notes

# search_notes func
# search cmd를 처리하는 함수

def search_notes(notes, keyword):
    kw = keyword.strip().lower()
    if not kw:
        return []

    hits = []
    for key, item in notes.items():
        hit = False

        # meta
        if match(key, kw) or match(item.get("platform", ""), kw) or match(item.get("problem_id", ""), kw):
            hit = True

        # tags
        for tag in item.get("tags", []):
            if match(tag, kw):
                hit = True
                break

        # logs (정밀 검색: log 단위로)
        if not hit:
            for log in item.get("logs", []):
                if (
                    match(log.get("cause", ""), kw)
                    or match(log.get("fix", ""), kw)
                    or match(log.get("counterexample", ""), kw)
                ):
                    hit = True
                    break

        if hit:
            hits.append((key, item))

    return hits

# ===== Streamlit UI =====

# 외부 라이브러리
# 이해 우선순위 낮음

st.set_page_config(page_title="Algo Lab Notebook", layout="wide")
st.title("Algo Lab Notebook")

with st.expander("명령 예시", expanded=False):
    st.markdown("""
- 추가:
  - `add | platform=boj | id=2557 | cause=출력 형식 실수 | tags=입출력,문자열 | fix=... | counterexample=...`
- 검색:
  - `search | keyword=구간분할`
  - `search | 구간분할`
- 최근:
  - `recent | 10`
""")

# 세션 상태 초기화: 앱이 rerun돼도 notes 유지
if "notes" not in st.session_state:
    st.session_state.notes = load_notes()

if "last_result" not in st.session_state:
    st.session_state.last_result = None

cmd_text = st.text_input("명령을 입력하세요", placeholder="add | platform=swea | id=4613 | cause=... | tags=...")

col1, col2 = st.columns([1, 1])
run = col1.button("실행")
save_btn = col2.button("저장(강제)")

if save_btn:
    save_notes(st.session_state.notes)
    st.success("저장 완료")

if run and cmd_text.strip():
    cmd, fields, free = parse_input(cmd_text)

    if cmd == "add":
        ok, msg, new_notes = handle_add(fields, st.session_state.notes)
        st.session_state.notes = new_notes
        if ok:
            save_notes(st.session_state.notes)
            st.success(msg)
        else:
            st.error(msg)

    elif cmd == "search":
        # search | keyword=... 우선, 없으면 free[0] 사용
        keyword = fields.get("keyword", "") or (free[0] if free else "")
        results = search_notes(st.session_state.notes, keyword)
        st.session_state.last_result = ("search", keyword, results)
        st.info(f"검색어: {keyword} / 결과: {len(results)}개")

    elif cmd == "recent":
        n_str = free[0] if free else "10"
        try:
            n = int(n_str)
        except:
            n = 10

        # 최근 기록은 created_at 기준으로 logs를 펼쳐서 정렬(간단 버전)
        flat = []
        for key, item in st.session_state.notes.items():
            for log in item.get("logs", []):
                flat.append((log.get("created_at", ""), key, log))
        flat.sort(reverse=True)

        st.session_state.last_result = ("recent", n, flat[:n])
        st.info(f"최근 {n}개 표시")

    else:
        st.warning("알 수 없는 명령입니다. add/search/recent 중 하나를 사용하세요.")

# ===== 결과 출력 =====
st.divider()
st.subheader("결과")

lr = st.session_state.last_result
if lr is None:
    st.write("아직 실행 결과가 없어요.")
else:
    kind = lr[0]

    if kind == "search":
        _, keyword, results = lr
        for key, item in results:
            st.markdown(f"### {key}")
            st.caption(f"tags: {', '.join(item.get('tags', []))}")
            for i, log in enumerate(item.get("logs", []), start=1):
                st.markdown(f"- [{i}] {log.get('created_at','')} / 원인: {log.get('cause','')}")
                if log.get("fix"):
                    st.markdown(f"  - 수정: {log.get('fix')}")
                if log.get("counterexample"):
                    st.markdown(f"  - 반례: {log.get('counterexample')}")

    elif kind == "recent":
        _, n, rows = lr
        for created_at, key, log in rows:
            st.markdown(f"- **{created_at}** | {key} | 원인: {log.get('cause','')}")
            if log.get("fix"):
                st.markdown(f"  - 수정: {log.get('fix')}")
            if log.get("counterexample"):
                st.markdown(f"  - 반례: {log.get('counterexample')}")
