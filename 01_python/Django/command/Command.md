1. 가상환경 생성
`python -m venv venv`
- `python -m venv`: 가상환경 생성
- `~ venv`: 가상환경 명
  
2. 가상환경 활성화
`source venv/Scripts/activate`

3. 가상환경 종료
`deactivate`
- 터미널 끄면 자동 종료된다.

4. Django 프로젝트 생성
`django-admin startproject firstpjt .`
- `django-admin startproject`: 머였드라
- `firstpjt`: 프로젝트 명
- `.`: Directory

5. 서버 실행
`python manage.py runserver`
- `manage.py`: 파일명
- `runserver`: 명령어

6. 앱 생성
`python manage.py startapp articles`
- articles 폴더 생성