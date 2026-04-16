# ***ADMIN***

## 관리자 인터페이스, Automatic admin interface

장고는 추가 설치 및 설정 없이 자동으로 제공하는 관리자 인터페이스가 있다. 데이터 베이스 모델의 **CRUD(생성, 읽기, 업데이트, 삭제)** 작업을 간편하게 수행할 수 있다. 덕분에 빠른 프로토 타이핑, 비개발자 데이터 관리, 내부 시스템 구축에 이상적이다.

## 과정

1. manage.py 파일이 있는 위치에서 터미널을 연다
2. `python manage.py createsuperuser` 명령어 입력
3. 정보 입력
  - username: 아이디
  - email: 선택 사항
  - password: 비밀번호 ( 입력해도 콘솔창에 보이지 않으니 주의 )
  - password check: 비밀번호 확인
  
생성이 완료되면 DB 파일에서 확인이 가능하다.