1. Migrations 생성
`python manage.py makemigrations`

2. DB 반영
`python manage.py migrate`

3. migrate 진행 여부 확인
`python manage.py showmigrations`

4. 해당 migrations 파일이 SQL언어로 어떻게 번역되는지 확인하는 명령어
`python manage.py sqlmigrate articles 0001` - sqlmigrate <앱 이름> <migration 이름>