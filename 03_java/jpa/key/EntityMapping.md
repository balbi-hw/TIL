# 엔티티 맵핑

1. 객체와 테이블 매핑: **Entity, @Table**
2. 필드와 컬럼 매핑: **@Column**
3. 기본 키 매핑: **@Id**
4. 연관관계 매핑: **@ManyToOne, @JoinColumn**
  
## 1. 객체와 테이블 매핑

### @Entity

- @Entity 가 붙은 **클래스**는 JPA가 관리하며 엔티티라고 이야기한다.
- JPA를 사용해서 테이블과 매핑할 클래스는 어노테이션을 꼭 붙이자.
- 주의사항
  - **기본생성자 필수**
  - final 클래스, enum, interface, inner 클래스는 사용 X
  - 저장할 필드에 final 을 사용하지 않는다.
- 파라미터
  - name:  
  JPA에서 사용할 이름을 지정한다. 기본값은 클래스 이름이며 같은 클래스 이름이 없다면 기본값을 사용하도록 권장된다.

### @Table

- @Table은 엔티티와 매핑할 테이블을 지정한다. 
- 파라미터
  - name: 매핑할 테이블 이름 ( 기본값: 엔티티 이름 )
  - catalog: 데이터베이스 catalog 매핑
  - schema: 데이터베이스 schema 매핑
  - uniqueConstraints( DDL ): DDL 생성 시에 유니크 제약 조건 생성

> DDL:  
> SQL 의 한 종류로 흔히 이야기하는 CRUD 는 데이터를 다루는 SQL ( DML )이고 DDL 은 테이블을 다루는 SQL 이다. 테이블 생성, 컬럼 추가, 제약조건 설정 등이 있다.

> 참고:  
> catalog 와 schema 는 DB 내부의 directory 라고 이해하면 될 것 같다. table 은 entity 정보를 DB에서 담아두는 파일이고 이 비슷한 파일들을 넣어둔 폴더를 스키마, 이 스키마를 넣어둔 폴더를 카탈로그라고 이해했다.
> DB > catalog > schema > table (entity)


## 2. 필드와 컬럼 매핑

다음 요구사항이 추가되었다고 가정하자.
1. 회원은 일반 회원과 관리자로 구분해야 한다.
2. 회원 가입일과 수정일이 있어야 한다.
3. 회원을 섦여할 수 있는 필드가 있어야 한다. 이 필드는 길이 제한이 없다.

```java
@Entity
public class Member {
    @Id
    private Long id;
    
    @Column(name = "name")
    private String username;
  
    private Integer age;
    
    @Enumerated(EnumType.String)
    private RoleType roleType;
    
    @Temporal(TemporalType.TIMESTAMP)
    private Date createdDate;
    
    @Temporal(TemporalType.TIMESTAMP)
    private Date lastModifiedDate;
  
    @Lob
    private String description;
}
```
다음과 같이 정리된다.


## 3. 기본키 매핑

기본 키 매핑 어노테이션은 **@Id** 와 **@GeneratedValue** 두 가지가 있다.
```java
@Id @GeneratedValue(strategy = GenerationType.AUTO)
private Long id;
```
