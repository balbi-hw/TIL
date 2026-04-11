# Project
장고의 프로젝트는 애플리케이션의 집합이다.  
DB의 설정, URL 연결, 전체 앱 설정등을 처리한다.

## Project's Structure
- settings.py
    - 프로젝트의 모든 설정을 관리한다.
- urls.py
    - 요청이 들어오는 URL 에 따라 이에 대응하는 적절한 views 를 연결한다.
- __init__.py
    - 해당 폴더를 패키지로 인식하도록 설정하는 파일
- asgi.py
    - 비동기식 웹 서버와의 연결 관련 설정
- wsig.py
    - 웹 서버와의 연결 관련 설정
- manage.py
    - Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티

# Django Application
앱은 프로젝트에서 독립적으로 작동하는 기능 단위 모듈이다.  
각자 특정한 기능을 담당하며 다른 앱들과 함께 하나의 프로젝트를 구성한다.

## App's Structure
- admin.py
    - 관리자용 페이지 설정
- models.py
    - DB와 관련된 Model 을 정의
    - MTV 패턴의 M
- views.py
    - HTTP 요청을 처리하고 해당 요청에 대한 응답을 반환 (url, model, template 과 연동)
    - MTV 패턴의 V
- apps.py
    - 앱의 정보가 작성된 곳
- tests.py
    - 프로젝트 테스트 코드를 작성하는 곳
  
수업을 들으며 생각한 걸로는 일반 웹 어플리케이션 처럼 각 앱은 도메인이고 다수의 도메인을 합쳐서 프로젝트를 만드는 느낌이다.  
그래서 장고 프로젝트 파일 구조를 살펴보면 프로젝트 폴더와 앱 폴더가 분리되어 있는 것을 볼 수 있고 프로젝트 폴더 안에서 각 앱의 연결을 담당한다.
  
스프링의 Container 역할을 프로젝트가 하는 느낌이다! AppConfig 의 정보를 받아서 DI를 진행하듯이 각 앱들의 정보를 받아서 필요한 절차를 진행한다.
  
AppConfig 는 프로젝트 폴더 안의 setting.py 에서 설정을 한다.  반드시 앱을 생성한 후에 `setting.py` 의 `INSTALLED_APPS` 리스트 내부에 등록해줘야한다고 한다.