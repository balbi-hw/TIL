# ***Django_Form***

## HTML Form 의 한계

사용자로부터의 데이터를 받기 위해 활용한 방법인데 이 HTML Form 만으로는 비정상적인, 또는 악의적인 요청을 필터링할 수가 없다. 즉 유효한 데이터에 대한 확인이 불가능했다.  
유효성 검사를 위해 추가적인 코드를 작성해야하는데 이를 구현하기 위해서는 고려할 사항이 매우 많고 복잡한데 이 과정을 Django Form 에서는 제공을하고 있다.
  
## Django Form

동일하게 사용자의 입력 데이터를 수집하지만 처리 및 유효성 검사의 기능이 추가되었다고 생각하자.
  
코드는 다음과 같다.
```python
# articles/forms.py 
## Templates 를 생성하듯 forms.py 파일을 생성해야한다.
from django import forms

class ArticleForm(forms.Form):
  title = forms.CharField(max_length=10)
  content = forms.CharField()
```
```python
# articles/views.py
from .forms import ArticleForm

def new(requeset):
  form = articleForm()  # Form 인스턴스 생성
  context = {
    'form' = form,
  }
  return render(request, 'articles/new.html', context)
```
```html
<!-- new.html -->
<h1>NEW</h1>
<form action = " {%url 'articles:create' %} " method="POST">
  {% csrf token %}
  {{ form }}  <!-- 인스턴스 조회 -->
  <input type="submit">
</form>
```
이렇게 하면 기존 HTML form 코드를 생략하고 같은 기능을 구현할 수 있다. HTML에 있던 ( 클라이언트 ) 코드를 view와 forms로 ( 서버 ) 옮겼다. 코드를 뒤로 숨긴다고 생각하자.


> 참고:  
추가로 HTML 의 <a> 태그와 Django HTML 의 <form> 태그 내의 `action` 은 둘 다 요청을 보내는 수단이지만 <form> 태그는 값을 묶어 보낼 수 있다는 점이 <a> 와 다르다.  
```html
{% block content %}
<h1>이 곳에서 할 일을 생성합니다.</h1>
<p>추후 기능 추가 예정</p>

<form action="{% url 'index' %}" method="GET">
  <input type="text" name='work'>
  <input type="submit" value="제출">
</form>
{% endblock content %}
```
위는 값 'work' 를 'index' url 로 보내는데 저 부분을 <a> 태그로 바꾸게 되면 값을 보내지 않고 '이동'만 진행한다.