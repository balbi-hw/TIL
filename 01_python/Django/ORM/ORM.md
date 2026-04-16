# ***ORM, Object Relational Mapping***

객체 지향 프로그래밍 언어의 객체와 데이터베이스의 데이터를 매핑하는 기술 ( 여기서는 Django ORM 을 다룸 )

## QuerySet API

데이터베이스의 복잡한 SQL 쿼리문을 직관적인 Python 코드로 다룰 수 있게 해주는 번역기로 개발자가 직접 SQL 을 작성하지 않고 .filter(), .exclude(), .order_by() 등 파이썬다운 메서드를 사용해 손쉽게 CRUD 가 가능하도록 해준다. 메서드의 종류는 Docs의 **QuerySet API reference** 문서를 참고하자
![ORM](./properties/ORM.png)
  
### QuerySet API 기본 구조

**Article.objects.all()**  
- Article (모델 클래스)
  - 역할: 데이터베이스 테이블에 대한 Python 클래스 표현
  - articles_article 테이블의 스키마(필드, 데이터 타입 등)를 정의하며 Django ORM 이 데이터베이스와 상호작용할 때 사용하는 기본적인 구조체
- .objects (매니저, like manager.py)
  - 역할: 데이터베이스 조회 작업을 위한 기본 인터페이스 ( SQL 메서드가 거의 다 모여있는 듯 하다. maybe Model 클래스에 소속되어 있지 않을까? )
  - 모델 클래스가 데이터베이스 쿼리 작업을 수행할 수 있도록 한다.
  - Django는 모든 모델에 onjects 라는 이름의 매니저를 자동으로 추가하며 이 매니저를 통해 .all(), .filter() 등의 쿼리 메서드 호출
- .all() (SQL 메서드)
  - 역할: 특정 데이터베이스 작업을 수행하는 명령
  - 매니저를 통해 호출되는 메서드로 해당 모델과 연결된 테이블의 모드느 레코드를 조회하라는 쿼리를 생성 및 실행

## CRUD

장고에서의 CRUD 는 QuerySet API 를 통해 SQL 없이 작업이 가능하다.
- Create: 저장
- Read: 조회
- Update: 수정
- Delete: 삭제
  
Shell 필요: [Shell](../command/Shell.md)

### Create:

Create의 방법에는 총 세 가지가 있다.
1. 빈 객체 생성 후 값 초기화 및 저장
```shell
article = Article()  # Article 인스턴스 생성
>>> article == <Article:Article object (None)>  # 저장 안되어있음

article.title = 'title'
article.content = 'content'

# 꼭 save를 진행해줘야한다.
article.save()
article == <Article: Article object (1)>  # Article 테이블의 1번 데이터

article.id == 1
article.pk == 1

Article.objects.all() == <QuerySet [Article: Article object (1)]>
```
  
2. 초기 값과 함께 객체 생성 및 저장
```shell
article = Article(title='title', content='content')  # 반드시 save 해야한다.
article.save()

article == <Article: Article object (2)>
```
  
3. create() 메서드로 한 번에 생성 및 저장
```shell
Article.objects.create(title='title', content='content')
== <Article: Article object (3)>  #  DB를 직점 건드리기 때문에 save 가 필요 없음 (객체를 만들지 않음)
# DB를 건드리지 않는다. 위에서 잘못 이해하고 있었다. DB를 건드리는건 SQL 쿼리를 직접 작성하는 것이고 메서드도 결국 변역을 해준다. 객체를 생성하고 DB에 넣고 그 객체를 반환까지 해준다. (위 코드에서는 반환하지 않는다.) 추가로 쿼리를 통해 데이터를 추가하면 이는 DB 용어인 '레코드'를 추가, 생성했다고 표현하고 이 데이터를 파이썬 또는 다른 프로그래밍 언어는 이해하지 못하기 때문에 읽어오는 과정에서 DB가 객체로 표현을 해준다고 생각하자.
```

### READ:

QuerySet API 의 조회 메서드는 두 종류로 나뉘는데 QuerySet 타입을 반환하는 메서드와 그렇지 않은 메서드가 그것이다.
1. <QuerySet> 반환 메서드
   1. .all(): 해당 테이블의 전체 데이터를 조회한다.
   2. .filter(): 키워드 인자로 들어간 조건에 부합하는 데이터만 조회한다. ( 종류가 매우 많다. Docs의 **Field looups**를 찾아보자)
2. 아닌 메서드
   1. .get(): 키워드 인자와 일치하는 데이터만 조회한다. 다음과 같은 특징을 가진다.
    - 데이터를 찾을 수 없으면 `DoesNotExist` 예외를 발생시키고 둘 이상의 값이 있다면 `MultipleObjectsReturned` 예외를 발생시킨다.
    - 사실상 `pk, primary key` 조회 전용 메서드라고 생각하자.

### Update:

수정은 생성과 과정이 비슷하지만 이미 존재하는 데이터를 다루기 때문에 조회를 먼저 해야한다는 차이가 있다.
```shell
article = Article.objects.get(pk=1)
article.title = 'updated title'
article.save()
```
`조회 -> 수정 -> 저장` 의 과정을 거친다.

### Delete:

삭제 또한 수정과 같이 데이터를 조회한 후 삭제해야한다. 하지만 조회와는 달리 저장을 할 필요는 없다.
```shell
article = Article.objects.get(pk=1)
article.delete()  # 이 때 list의 .pop() 메서드 같이 삭제된 객체가 반환된다.
Article.objects.get(pk=1)  # 삭제한 데이터는 더이상 조회가 불가능하다. 'DoesNotExist` 에외 발생
```
delete 는 메서드 내부에서 DB를 조작하는 코드가 들어있어서 객체를 삭제하면 해당 데이터 또한 삭제된다.

## ORM, QuerySet API 를 사용하는 이유

1. 데이터베이스 추상화
  - 개발자는 특정 데이터베이스 시스템에 종속되지 않는다.
2. 생산성 향상
  - 복잡한 SQL 쿼리를 직접 작성하는 대신 간단한 Python 코드로 SQL 작업 수행이 가능하다.
3. 객체 지향
  - 데이터베이스 내 데이터를 Python 객체로 다룰 수 있어 OOP의 이점을 활용할 수 있다.