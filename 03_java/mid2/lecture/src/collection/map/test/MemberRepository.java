package collection.map.test;

import java.util.HashMap;
import java.util.Map;

public class MemberRepository {

    private Map<String, Member> memberMap = new HashMap<>();
    public void save(Member member) {
// 코드 작성
        memberMap.put(member.getId(), member);
    }
    public void remove(String id) {
// 코드 작성
        memberMap.remove(id);
    }
    public Member findById(String id) {
// 코드 작성
        for (String key : memberMap.keySet()) {
            if (key.equals(id)) {
                return memberMap.get(key);
            }
        }
        return null;
    }
    public Member findByName(String name) {
// 코드 작성
        for (String key : memberMap.keySet()) {
            if (memberMap.get(key).getName().equals(name)) {
                return memberMap.get(key);
            }
        }
        return null;
    }
}