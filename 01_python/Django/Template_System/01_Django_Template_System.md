# ***Django Template System***

파이썬 데이터 ( Context ) 를 HTML 문서 ( Template ) 와 결합하여 로직과 표현을 분리한 채 동적인 웹페이즈를 생성하는 도구이다.
  
```html
<body>
  <h1>Hello, Django!</h1>
</body>
```
위 코드에서 `Django!` 부분을 변수처럼 바꿔보자!

```html
<!--index.html-->
<body>
  <h1>Hello, {{ name }}!</h1>
</body>
```
위 코드에서 `{{ name }}`이 변수가 되었다. 그럼 이 변수에 값을 주입해보자.

```python
#view.py
def index(request):
    context = {
        'name': 'Jane',
    }
    return render(request, 'articles/index.html', context)
```
이렇게 `view`함수를 작성하면 된다. 위 함수는 index 페이지로 접근을 할 때 호출되고 함수 내의 context가 render 함수의 3번째 인자로 들어가게 된다. 그럼 html 내의 변수명과 같은 키값을 context에서 찾아 밸류값을 넣어준다. **키값과 변수명이 같아야한다!** 아마 Spring Container의 Bean처럼 내부적으로 맵핑을 더 하기 때문인 것 같다.
  
**Django Template system의 목적**
'페이지 틀'에 '데이터'를 동적으로 결합하여 수많은 페이지를 효율적으로 나타내기 위함
