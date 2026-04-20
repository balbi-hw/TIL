내장 라이브러리 os, requests
외부 라이브러리 python-dotenv

```python
import requests
import pprint
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = "http://www.aladin.co.kr/ttb/api/ItemList.aspx"
params = {
    'TTBKey': API_KEY,
    'QueryType': "ItemNewSpecial",
    'MaxResults': 50,
    "start": 1,
    'SearchTarget': 'Book',
    'Output': 'js',
    'Version': 20131101,
}

response = requests.get(API_URL, params=params, timeout=5)
# pprint.pprint(response.json())

result = []
for item in response.json()['item']:
    parsed_date = {
        '책 제목': item.get('title'),
        '저자': item.get('author'),
        '출간일': item.get('pubDate'),
        '국제 표준 도서 번호 (ISBN)': item.get('isbn'),
    }

    result.append(parsed_date)

pprint.pprint(result)
```

API 불러오는 코드  
하단부 데이터 파싱을 할 때 찾는 key 값이 없을 때를 대비해 저렇게 .get 메서드를 사용해주자. 두번째 매개변수로 default 값을 받는다.