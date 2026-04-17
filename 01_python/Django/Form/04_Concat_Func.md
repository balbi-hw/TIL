# ***Concat_Func***

지금까지의 내용을 통해 몇몇 view 함수를 결합할 수가 있다.

## new & create

두 함수는 데이터 생성을 구현한다는 공통점이 있다. 하지만 HTTP Request method 의 차이가 존재한다. (GET, POST) 이를 잘 구분하면 함수를 결합할 수가 있다.
  
우선 원본 함수를 확인해보자.
```python
# new
def new(request):
  form = ArticleForm()
  context = {
    'form': form,
  }
  return render(request, 'articles/new.html', context)

# create
def create(request):
  form = ArticleForm(request.POST)
  if form.is_valid():
    article = form.save()
    return redirect('articles:detail', article.pk)
  context = {
    'form': form,
  }
  return render(request, 'articles/new.html', context)
```
잘 보면 겹치는 부분이 있음을 알 수 있다. 중복을 제거하자!
  
```python
def create(request):
  if request.method == 'POST' :
    form = ArticleForm(request.POST)
    if form.is_valid():
      article = form.save()
      return redirect('articles:detail', article.pk)
  else:
    form = ArticleForm()
  context = {
    'form': form,
  }
  return render(request, 'articles/new.html', context)
```
두 함수의 차이점이었던 메서드를 기준으로 분기처리를 했다. 기준이 `POST`가 된 이유는 POST는 DB에 영향을 미치는 코드들이 있기 때문이다. 추후 `GET`과 `POST` 외에도 다른 메서드가 있지만 `POST`만 주의해서 다루면 충분하다.
  
이렇게 `new` 함수를 지우게 되면 다른 코드에서도 new 의 흔적을 다 지워야한다!

## edit & update

똑같이 `edit` 함수와 `update` 함수 또한 겹치는 부분이 있다.
```python
def update(request, pk):
  article = Article.objects.get(pk=pk)
  if request.method == 'POST':
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
      form.save()
      return redirect('articles:detail', article.pk)

  else:
    form = ArticleForm(instance=article)

  context = {
    'article': article,
    'form': form,
  }
  return render(request, 'articles/update.html', context)
```
아래 `else` 부분이 `edit` 이고 윗 부분이 `update` 로직이다. 코드는 위에서부터 아래로 흐르지만 사실 아래부터 작성하는게 흐름에 맞다는 점을 기억하자. `edit` 을 통해 수정할 내용을 작성해야 `update`가 가능하다.