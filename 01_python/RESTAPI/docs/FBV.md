# Function Based Views

어노테이션을 이용해 API endpoint 를 구분한다.

```python
@api_view(['POST'])
def article_create(request):
  serializer = ArticleSerializer(request.data)
  if serializer.is_valid(raise_404):
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
```

이렇게 엔드포인트를 함수로 구현한다. 함수를 보면 로직을 알 수 있어 직관적이고 로직을 수정하기도 편리하다. 확장에 용이하다.