# Class Based Views

Views 내부를 Class 로 구성한다.

```python
class SnippetList(APIView):
  
  def get(self, request, format=None):
    snippets = Snippet.objects.all()
    serializer = SnippetSerializer(snippets, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = SnippetSerializer(data=request.data)
    if serializer.is_valid(raise_404):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
```

```python
urlpatterns = [
  path('', views.SnippetList.as_view()),
]
```

views 와 urls 의 코드 일부이다. 다른 방법으로 클래스를 구현하는 방법도 있지만 사용하면 할 수록 불편하다. 구현은 정말 빠르지만 커스텀이 힘들고 그래서 추가 로직을 부여하기가 힘들다. 단순한 기능을 만드는 데에는 정말 빠르게 할 수 있다.
  
하지만 확장성의 문제로 실무에서는 거의 사용되지 않는 방법이라고 한다. FBV 를 열심히 보자.


---
예시

```python
class SnippetList(generics.ListCreateAPIView):
  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
```

위 코드만 보면 솔직히 직관적이라고 할 수는 없다. 추후 숙달되면 이를 잘 활용할 수 있을 것 같지만 학습하는 단계에서는 FBV 로 하나하나 구현하는 게 좋아보인다.