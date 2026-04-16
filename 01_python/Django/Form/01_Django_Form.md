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