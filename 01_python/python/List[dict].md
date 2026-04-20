Dict 타입을 받는 List 의 .sort() 메서드를 사용할 때는 key 값에 람다를 넣어준다.

```python
data = requests.get(API_URL, params=params, timeout=5).json()
pprint.pprint(data)

result = []
for parsed_data in data['item']:
    info = {
        'title': parsed_data['title'],
        'author': parsed_data['author'],
        'pubDate': parsed_data['pubDate'],
        'isbn': parsed_data['isbn'],
        'salesPoint': parsed_data['salesPoint'],
        'bestDuration': parsed_data.get('bestDuration', ''),
    }
    result.append(info)

result.sort(key=lambda x: x['salesPoint'])
```
result 내부 Dict 의 'salesPoint' 값을 기준으로 정렬