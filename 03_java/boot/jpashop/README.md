

## 목차
  - [도메인 분석](#도메인-분석)
  - [애플리케이션 구현 준비](#애플리케이션-구현-준비)
  - [회원 도메인](#회원-도메인)
  - [상품 도메인](#상품-도메인)
  - [주문 도메인](#주문-도메인)
  - [웹]()


## 도메인 분석

### 기능 목록
- 회원 기능
  - 회원 등록
  - 회원 조회
- 상품 기능
  - 상품 등록
  - 상품 수정
  - 상품 조회
- 주문 기능
  - 상품 주문
  - 주문 내역 조회
  - 주문 취소
- 기타 요구사항
  - 재고 관리 필요
  - 상품 종류는 도서, 음반, 영화 ( 도서만 구현 )
  - 상품을 카테고리로 구분
  - 상품 주문 시 배송 정보 입력 가능

### 도메인 모델과 테이블 설계
![Relations](/properties/Relation.png)  
**회원, 주문, 상품의 관계**: 회원은 주문을 여러개 할 수 있고 한 주문 안에 여러 상품을 담을 수 있다. 따라서 상품과 주문은 다대다 관계가 된다. 하지만 다대다 관계는 사용하지 않도록 권장하기에 주문 상품이라는 엔티티를 추가해 다대다 관계를 일대다, 다대일 관계로 풀어냈다.
  
![Entity](/properties/Entity.png)  
- **Member**: 이름과 임베디드 타입인 주소(Address), 주문 리스트를 가진다.
- **Order**: 한 주문에 여러 상품이 들어갈 수 있으니 주문과 주문 상품(OrderItem)은 일대다 관계이다. 주문은 상품을 주문한 회원과 배송 정보, 주문 날짜, 주문 상태를 갖는다.
- **OrderItem**: 주무한 상품 정보와 주문 금액, 주문 수량 정보를 갖는다.
- **Item**: 이름, 가격, 재고 수량을 갖는다. 상품인 음반, 도서, 영화가 상속 받는다.
- **Delivery**: 주문시 하나의 배송 정보를 생성한다. 주문과 배송은 일대일 관계이다.
- **Category**: 상품과 다대다 관계를 갖는다. parent, child 로 부모, 자식 카테고리를 연결한다.
- **Address**: 값 타입( 임베디드 타입 )이다. 회원과 배송에서 사용한다.
  
![Table](/properties/Table.png)  
테이블 분석도. 연관관계를 분석하면 다음과 같다.
- **회원과 주문**: 일대다, 다대일의 양방향. 외래 키가 있는 주문을 연관관계의 주인으로 정했다. ( Order.member 를 ORDERS.MEMBER_ID 와 매핑 )
- **주문상품과 주문**: 다대일 양방향 관계. 외래 키가 주문상품에 있으니 연관관계의 주인. ( OrderItem.order 를 ORDER_ITEM.ORDER_ID 에 매핑 )
- **주문상품과 상품**: 다대일 단방향 관계. OrderItem.item 을 ORDERS_ITEM.ITEM_ID 외래 키와 매핑
- **주문과 배송**: 일대일 양방향 관계. Order.delivery 를 ORDERS.DELIVERY_ID 외래 키와 매핑
- **카테고리와 상품**: @ManyToMany 사용 ( 실무에서는 사용하지 않는다. 예시를 위해 추가 )

### 엔티티 설계시 주의점
- 엔티티에는 가급적 Setter를 사용하지 말자
유지보수가 힘들어진다.
- 모든 연관관계는 지연로딩
엔티티 코드를 보면 알겠지만 모든 연관관계는 LAZY 로 설정해야한다. EAGER ( 즉시 로딩 )은 예측이 어렵고 어떤 SQL 이 실행될지 추적이 어렵다 특히 N + 1 문제가 자주 발생한다.
- 컬렉션은 필드에서 초기화
엔티티는 영속화될 때 다른 하이버네이트 내장 래퍼 클래스로 감싸지는데 ( 비유 ) 이 엔티티를 이후 다른 클래스로 초기화하게 되면 하이버네이트 내부 매커니즘에 문제가 발생할 수 있다. 필드 레벨에서 초기화한 뒤 변경하지 말자


## 애플리케이션 구현 준비

예제를 단순화하기 위해 다음 기능은 구현하지 않는다.
- 로그인과 권한 관리
- 파라미터 검증과 예외처리
- 카테고리
- 배송 정보
- 상품은 도서만 사용한다.
  
![Architecture](/properties/Archi.png)
- controller, web: 웹 계층
- service: 비즈니스 로직, 트랜잭션 처리
- repository: JPA를 직접 사용하는 계층, EntityManager 사용
- domain: 엔티티가 모여 있는 계층, 모든 계층에서 접근한다.
  
**패키지 구조**
- jpabook.jpashop
  - domain
  - exception
  - repository
  - service
  - web
  

## 회원 도메인

- [MemberRepository](/src/main/java/jpabook/jpashop/repository/MemberRepository.java)
- [MemberService](/src/main/java/jpabook/jpashop/service/MemberService.java)
- [MemberEntity](/src/main/java/jpabook/jpashop/domain/Member.java)


## 상품 도메인




## 주문 도메인