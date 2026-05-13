우선 http 파일의 구조를 파악해야 한다는 게 절망적이다.

1. 선택메서드
```javascript
const variable = document.querySelector('.className')
const variable = document.querySelector('#attributeValue')
const variable = document.querySelector('httpTag')
const variable = document.querySelectorAll('http tag')
```
변수의 타입이 크게 두 가지 ( let, const ) 가 있다.
- let: 재할당이 허용되는 일반 변수이지만 재정의는 안된다.
- const: let 에 java 의 final keyword 가 붙었다고 생각하자.

querySelector 의 인자는 지금까지 세 가지 확인했다. http 의 class, 태그의 attribute, 그리고 Tag 이다.  
class 와 attribute 는 각각 `.`, `#` 를 앞에 붙여야 인식한다.

2. 속성 조작
   1. classList
    `element.classList.add()`, `element.classList.remove()`, `element.classList.toggle()`  
    세 가지 중 toggle 이 인상적이었는데 클래스가 존재하면 제거하고 false 를, 없다면 추가하고 true 를 반환한다.
   2. attribute
    `Element.getAttribute()`, `Element.setAttribute()`, `Element.removeAttribute()`  
    get, set, remove 메서드이다.

3. DOM 요소 조작
   `document.createElement(tag)`, `Node.appendChild()`, `Node.removeChild()`  
   Node 는 객체를 의미한다.


4. 예시
실습으로 진행한 내용이다.
```html
<body>
  <h1>안녕하세요, 제 이름은 <b id="name">홍길동</b>입니다.</h1>
  
  <img src="" alt="" width="200">
  
  <h2>소개</h2>
  <p>저는 <b id="job">[직업/전공]</b>으로 일하고 있습니다. <b id="experience">[간단한 경력/학력]</b>을 가지고 있으며, <b>[특기 또는 관심 분야]</b>에 대해 꾸준히 공부하고 있습니다.</p>
  
  <h2>프로젝트</h2>
  <ul id="list-group">
    <li><b>프로젝트 1:</b> <span class="project-1">[프로젝트 1 제목]</span></li>
    <li><b>프로젝트 2:</b> <span class="project-2">[프로젝트 2 제목]</span></li>
    <li><b>프로젝트 3:</b> <span class="project-3">[프로젝트 3 제목]</span></li>
  </ul>
  
  <h2>연락처</h2>
  <p>이메일: <b id="email">[이메일 주소]</b></p>
  <p>전화번호: <b id="phone">[전화번호]</b></p>
  
  <script>
    const name = document.querySelector('#name')
    const job = document.querySelector('#job')
    const experience = document.querySelector('#experience')
    const email = document.querySelector('#email')
    const phone = document.querySelector('#phone')

    name.textContent = '홍길동'
    job.textContent = '의적'
    experience.textContent = '서당'
    email.textContent = 'hgd@korea'
    phone.textContent = '010-1234-1234'
  
    const img = document.querySelector('img')
    // img.setAttribute('src', 'profile.jpg') 
    // img.setAttribute('alt', '프로필 사진') 
    imageTag.src = './profile.jpg'
    imageTag.alt = '프로필 사진'

    
    const bodyTag = document.querySelector('body')
    bodyTag.classList.add('container')

    const h1Tag = document.querySelector('h1')
    h1Tag.classList.add('title')

    img.classList.add('img')

    name.classList.add('highlight')
    job.classList.add('highlight')
    experience.classList.add('highlight')
    email.classList.add('highlight')
    phone.classList.add('highlight')

    const pTagSns = document.createElement('p')
    pTagSns.textContent = 'SNS: '

    const bTagSns = document.createElement('b')
    bTagSns.textContent = 'asd@sns.com'
    bTagSns.classList.add('highlight')

    pTagSns.appendChild(bTagSns)

    bodyTag.appendChild(pTagSns)
  
  </script>
```