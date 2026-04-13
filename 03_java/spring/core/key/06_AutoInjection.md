# ***Auto Injection***

## 의존관계 주입 방법
의존관계 주입의 방식은 크게 네 가지 방법이 있다.
1. 생성자 주입
2. 수정자 주입 (Setter)
3. 필드 주입
4. 일반 메서드 주입
  
**생성자 주입**  
지금까지 했던 방싣으로 이름 그대로 생성자를 이용해 주입하는 방법이다.
- 생성자 호출 시점에 단 한 번만 호출되는 것이 보장된다.
- 불변, 필수 의존관계에 사용한다.
```java
@Component
public class OrderServiceImpl implements OrderService {
    
    private final MemberRepository memberRepository;
    private final DiscountPolicy discountPolicy;

    @Autowired
    public OrderServiceImpl(MemberRepository memberRepository, DiscountPolicy discountPolicy) {
        this.memberRepository = memberRepository;
        this.discountPolicy = discountPolicy;
    }
}
```
위 코드에서 `@Autowired`를 사용했지만 생성자가 한 개만 있다면 생략해도 자동 주입된다.
  
**수정자 주입**  
setter 라 불리는 필드의 값을 변경하는 수정자 메서드를 통해 의존관계를 주입한다.
- 선택, 변경 가능성이 있는 의존관계에 사용한다.
```java
@Component
public class OrderServiceImpl implements OrderService {
    
    private MemberRepository memberRepository;
    private DiscountPolicy discountPolicy;

    @Autowired
    public void setMemberRepository(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }
    
    @Autowired
    public void setDiscountPolicy(DiscountPolicy discountPolicy) {
        this.discountPolicy = discountPolicy;
    }
}
```
> 참고: `@Autowired`의 기본 동작은 주입할 대상이 없으면 오류가 발생한다. ( 생성자의 인자가 빈에 존재하지 않으면 에러가 발생한다. ) 주입 대상이 없어도 동작하게 하려면 `@Autowired(required = false)`로 지정하면 된다.
  
**필드 주입**  
필드에 바로 주입하는 방식이다.
- 코드가 간결하지만 외부에서 변경이 불가능해 테스트가 까다롭다.
- DI 프레임워크가 없으면 아무것도 할 수 없다.
- 안티패턴으로 사용하지 말자.
  - 애플리케이션의 실제 코드와 무관한 테스트 코드이거나
  - 스프링 설정을 목적으로 하는 `@Configuration` 같은 곳에서만 특별한 용도로 사용한다.
```java
@Component
public class OrderServiceImpl implements OrderSerivce {
    
    @Autowired
    private MemberRepository memberRepository;
    
    @Autowired
    private DiscountPolicy discountPolicy;
}
```
  
**일반 메서드 주입**  
일반 메서드를 통해서도 DI 가 가능하다.
- 한 번에 여러 필드를 주입 받을 수 있다.
- 일반적으로 잘 사용하지는 않는다.
```java
@Component
public class OrderServiceImpl implements OrderSercice {
    
    private MemberRepository memberRepository;
    private DiscountPolicy discountPolicy;

  @Autowired
  public void init(MemberRepository memberRepository, DiscountPolicy discountPolicy) {
      this.memberRepository = memberRepository;
      this.discountPolicy = discountPolicy;
  }
}
```
위처럼 public 으로 메스드를 정의해야해서 수정이 가능하기 때문에 잘 사용하지 않는다.

## 옵션 처리
주입할 스프링 빈이 없어도 작동해야할 떄가 있다.
그런데 `@Autowired`만 사용하면 `required` 옵션의 기본 값이 `true`이기 때문에 자동 주입 대상이 없으면 오류가 발생한다.
  
자동 주입 대상을 옵션으로 처리하는 방법은 다음과 같다.
- `@Autowired(required = false)`: 주입 대상이 없으면 수정자 메서드가 호출되지 않음
- `org.springframwork.lang.@Nullable`: 자동 주입 대상이 없으면 null이 입력된다.
- `Optional<>`: 자동 주입 대상이 없으면 `Optional.empty`가 입력된다.
```java
// 호출 안됨
@Autowired(required = false)
public void setNoBean(Member member) {
  System.out.println("setNoBean1 = " + member);
}

// null 호출
@Autowired
public void setNoBean2(@Nullable Member member2) {
  System.out.println("setNoBean2 = " + member2);
}

// Optinal.empty 호출
@Autowired(required = false)
public void setNoBean3(Optional<Member> member) {
  System.out.println("setNoBean3 = " + member);
}
```
위 코드 `Optional`안의 Member 는 스프링 빈이 아니다.

## 생성자 주입이 권장된다.
과거에는 다른 방식들도 많이 사용했다고 하는데 현재는 생성자 주입을 권장한다고 한다.

1. 불변성
  - 대부분의 의존관계 주입은 한 번 발생하면 의존관계를 변경할 일이 없다. 오히려 변하면 안되는 경우가 많다.
  - 수정자 주입을 사용하면 수정자 메서드를 public 으로 열어둬야한다.
  - 생성자 주입은 객체 생성 시 단 한 번만 호출되기에 불변 설정이 가능하다.
2. 누락
  - 프레임워크 없이 순수한 자바 코드를 단위 테스트 하는 경우에는 수정자의 인수가 누락되어도 컴파일 에러가 발생하지 않는다. 하지만 실행하게 되면 NPE 에러가 발생한다.
  - 생성자를 사용하면 필수 인자가 누락되었기 때문에 컴파일 에러가 발생한다.
3. final
  - 생성자를 사용하면 필드에 `final` 키워드를 사용할 수 있다. 그래서 값 설정이 필수적인 경우에 누락된 상황을 막을 수 있다.
  
기본적으로 생성자 주입을 사용하고 필수 값이 아닌 경우에는 수정자 주입 방식을 옵션으로 부여하면 된다. 생성자와 수정자를 둘 다 사용할 수 있다.  
항상 생성자를 선택하되 가끔 필요할 때 수정자 주입을 선택하는 것이다. 필드 주입은 되도록 지양하자.
  
## 롬복, lombok
생성자를 생략할 수 있는 방법이 있다. 클래스에 필드가 생성되거나 제거될 때 생성자 또한 수정해야 하는 번거로움이 있는데 이를 해결하는 방법이다.
  
롬복 라이브러리의 `@RequiredArgsConstructor` 기능을 이용하는 것인데 이를 사용하면 final 필드를 모아서 생성자를 자동으로 만들어준다. (코드에 보이지는 않는다.)
  
최근에는 생성자를 한 개만 만들고 `@Autowired`를 생략하는 방법을 사용하는데 여기에 Lombok 라이브러리의 해당 기능을 사용하면 코드를 더 간결하게 만들 수 있다.
  
라이브러리 추가 방법은 필요할 때 찾아보자.

## 빈이 두 개 이상일 때
`@Autowired`는 기본적으로 빈을 타입으로 조회한다. 타입으로 조회하게 되면 선택된 빈이 두 개 이상일 때 문제가 발생한다. `DiscountPolicy`의 하위 타입인 `FixDiscountPolicy`, `RateDiscountPolicy` 둘 다 스프링 빈으로 선언하면 `DiscountPolicy`를 `@Autowired`할 때 에러가 발생한다. 이 때 애초에 하위 타입을 지정할 수도 있지만 하위 타입으로 지정하는 것은 DIP를 위배하고 유연성이 떨어진다. 또한 이름만 다르고 같은 타입의 빈이 두 개 이상 있을 경우는 해결이 안된다.
  
### @Autowired 필드명, @Qualifire, @Primary
위 세가지 방법으로 해결이 가능하다.

1. @Autowired 필드 명 매칭
`@Autowired`는 타입 매칭을 시도하고, 이때 여러 빈이 있으면 필드 이름, 파라미터 이름으로 빈 이름을 추가 매칭한다. 타입은 그대로 두고 필드 명을 바꾸는 것이다.  
`타입 검색 -> 중복 -> 필드명 빈 검색 -> 중복 x -> DI`  
필드 명 매칭은 먼저 타입 매칭을 시도하고 그 결과에 여러 빈이 있을 때 추가 동작 하는 것이다.

2. @Qualifire
`@Qualifier`는 추가 구분자를 붙여주는 것이다. 조금 다르지만 쉽게 이야기하면 key 를 하나 추가하는 것이다.
```java
@Component
@Qualifier("mainDiscountPolicy")
public class RateDiscountPolicy implements DiscountPolicy {}

@Component
@Qualifier("fixDiscountPolicy")
public class FixDiscountPolicy implements DiscountPolicy {}

@Autowired
public OrderServiceImpl(MemberRepository memberRepository, @Qualifier("mainDiscountPolicy") DiscountPolicy discountPolicy) {
    this.memberRepository = memberRepository;
    this.discountPolicy = discountPolicy;
}
```
`@Qualifier`의 키값을 못찾으면 해당 문자열과 같은 이름의 빈을 추가로 찾는다. 하지만 이런 용도로 사용하는건 좋지 못하다.  
빈을 수동으로 등록할 때도 사용이 가능하다.

3. @Primary
`@Primary` 는 우선순위를 정하는 방법이다. `@Autowired` 사용 시 빈이 여러개 매칭되면 `@Primary` 가 우선권을 가진다.
```java
@Component
@Primary
public class RateDiscountPolicy implements DiscountPolciy {}

@Component
public class FixDiscountPolicy implements DiscountPolicy {}
```
`@Autowired` 호출 시 `RateDiscountPolicy`가 우선권을 갖는다.

## 조회한 빈이 모두 필요할 때, List, Map
빈이 여러개 있는데 그 여러개의 빈이 모두 다 필요한 경우도 있다.  
예를 들어 할인 서비스를 제공하는데 클라이언트가 Fix 와 Rate 를 선택할 수 있다면 모두 다 필요할 것이다. 스프링은 소위 말하는 이 전략 패턴을 매우 간단히 구현 가능하다.
```java
public class AllBeanTest {

  @Test
  void findAllBean() {
    ApplicationContext ac = new AnnotationConfigApplicationContext(AutoAppConfig.class, DiscountService.class);
    DiscountService discountService = ac.getBean(DiscountService.class);
    Member member = new Member(1L, "userA", Grade.VIP);
    int discountPrice = discountService.discount(member, 10000, "fixDiscountPolciy");
  }
  
  static class DIscountService {
      private final Map<String, DiscountPolicy> policyMap;
      private final List<DiscountPolicy> policies;
      
      public DiscountService(Map<String, DiscountPolicy> policyMap, List<DiscountPolicy> policies) {
          this.policyMap = policyMap;
          this.policies = policies;
      }
  }
  
}
```