# ***객체지향 원리의 적용***

```java
public class OrderServiceImpl implements OrderService {
    private final DiscountPolicy discountPolicy = new FixDiscountPolicy();
}

/*
        이 코드에서 FixDiscountPolicy를 Rate로 바꾸려면 어떻게 해야할까?
        새 코드를 작성해야한다.
 */
public class OrderServiceImpl implements OrderService {
    private final DiscountPolicy discountPolicy = new RateDiscountPolicy();
}
```
이렇게 코드를 변경하게 되면 이 코드는 **SOLID** 중 OCP 와 DIP 를 위반하고 있다.  
discountPolicy 변수는 지금 타입은 DiscountPolicy 이고 객체는 RateDiscountPolicy 의 객체이다. -> DIP 위반  
코드를 확장하기 위해 변경이 수반됐다. -> OCP 위반
  
그럼 어떻게 해야할까?
  
문제점을 분석하자면 다음과 같다.
1. 클라이언트 코드인 OrderServiceImpl 은 DiscountPolicy의 인터페이스 뿐만 아니라 구체 클래스도 함께 의존한다.
2. 그래서 구체 클래스를 변경할 때 클라이언트 코드도 함께 변경해야 한다.
3. DIP 위반 -> 추상에만 의존하도록 변경해야한다.
4. DIP를 위반하지 않도록 인터페이스에만 의존하도록 의존관계를 변경하면 된다.
  
**인터페이스 의존 코드**  
```java
public class OrderServiceImpl implements OrderService {
    private DiscountPolicy discountPolicy;
}
```
인터페이스에만 의존하도록 코드를 변경했는데 이러면 구현이 없다. 구현 없이 코드를 어떻게 실행할까?
  
**어디에선가 클라이언트인 OrderServiceImpl 에 DIscountPolicy 의 구현 객체를 대신 생성하고 주입해주어야한다**
  
## 관심사의 분리
**AppConfig 의 등장**  
- 애플리케이션의 전체 동작 방식을 구성하기 위해 구현 객체를 생성하고 연결하는 책임을 갖는 별도의 설정 클래스를 만든다.

```java
public class AppConfig {
    
    public MemberService memberService() {
        return new MemberServiceImpl(new MemoryMemberRepository());
    }
    
    public OrderService orderService() {
        return new OrderServiceImpl(new MemoryMemberRepository(), new FixDiscountPolicy());
    }
}
```
이 클래스는 애플리케이션 실제 동작에 필요한 구현 객체를 생성한다.
- MemberServiceImpl
- MemoryMemberRepository
- OrderServiceImpl
- FixDiscountPolicy
  
AppConfig 는 생성한 객체 인스턴스의 참조를 생성자를 통해 주입해준다.
- MemberServiceImpl -> MemoryMemberRepository
- OrderServiceImpl -> MemoryMemberRepository, FixDiscountPolicy
  
객체의 생성과 연결은 이제 AppConfig가 담당한다.  
- DIP 가 완성됐다. 객체의 생성과 주입을 담당하는 클래스가 생겼으니 서비스 클래스는 실행에만 집중하면 된다.
- 관심사의 분리는 이렇게 객체의 생성, 연결하는 역할과 실행하는 역할이 명확히 분리하는 것을 의미한다.
- 이렇게 AppConfig 가 실행 클래스에 의존관계를 주입해주는 것 같은 것을 **DI, Dependency Injection**, 우리말로 **의존관계 주입** 또는 **의존성 주입**이라 한다.

## AppConfig 리팩터링
위의 AppConfig 를 보면 DI 는 잘 수행하지만 가독성이 조금 떨어진다. 이를 고쳐보자.
```java
public class AppConfig {
    public MemberService memberService() {
        return new MemberServiceImpl(memberRepository());
    }

    public OrderService orderService() {
        return new OrderServiceImpl(new MemoryMemberRepository(), new FixDiscountPolicy());
    }
    
    public MemberRepository memberRepository() {
        return new MemoryMemberRepository();
    }
    
    public DiscountPolicy discountPolicy() {
        return new FixDiscountPolicy();
    }
}
```
이렇게 가독성도 높일 수 있었다. 이제 혹시라도 DiscountPolicy 가 Fix 에서 Rate 로 바뀌게 되면 discountPolicy 메서드의 리턴 객체만 RateDiscountPolicy 로 바꿔주면 된다.
  
이렇게 전체 프로그램의 흐름이 **사용 영역**과 **구성 영역** 두 가지로 분리되었다. 

## OOP, SOLID 의 적용
여기서 SOLID, 다섯 가지 중 세 가지를 적용해보았다.
  
### SRP 단일 책임 원칙
한 클래스는 하나의 책임만 가져야한다.
  
- 클라이언트 객체는 직접 구현 객체를 생성하고 연결하고 실행하는 다양한 책임을 지고 있었음
- SRP 단일 책임 원칙을 따르면서 관심사를 분리함
- 구현 객체를 생성하고 연결하는 책임은 AppConfig가 담당
- 클라이언트 객체는 프로그램의 실행만 담당

### DIP 의존관계 역전 원칙
프로그래머는 추상화에 의존해야하고 구체화에 의존하면 안된다.
  
- 새로운 할인 정책을 만들면 클라이언트 코드를 변경해야했는데 의존성 주입을 통해 이를 해결했다.
- AppConfig, 구성 역역을 만들고 여기서 객체의 생성과 주입을 담당해 사용 영역의 코드는 변경을 막을 수 있었다.

### OCP
소프트웨어 요소는 확장에는 열려 있으나 변경에는 닫혀 있어야 한다.

- 다형성을 사용하고 클라이언트가 DIP 를 지킴
- 애플리케이션을 사용과 구성 영역 두가지로 나눔
- FIX 를 RATE 로 바꾼 것 처럼 소프트웨어 요소를 새롭게 확장해도 사용 영역의 변경은 닫혀 있다.


## IoC, Di, 그리고 컨테이너
### IoC, Inversion of Control, 제어의 역전
기존의 프로그램은 클라이언트 구현 객체가 스스로 서버 구현 객체를 생성하고 연결하고 실행했다. 구현 객체가 프로그램의 제어 흐름을 스스로 조종했다.  
반면에 AppConfig가 등장한 이후 구현 객체는 자신의 로직을 **실행**하는 역할만 담당한다. 프로그램의 제어 흐름은 `AppConfig`에서 담당한다.  
이제 사용 영역의 코드들은 그저 전원을 누르면 작동하는 기계가 되었다. 그리고 그 기계의 컨트롤은 구성 영역의 코드가 담당한다.  
이렇게 프로그램의 제어 흐름을 직접 제어하는 것이 아니라 외부에서 관리하는 것을 **제어의 역전**이라고 한다.
  
**프레임워크 vs 라이브러리**  
- 프레임워크가 내가 작성한 코드를 제어하고 대신 실행하면 그것은 프레임워크이다. (JUnit)
- 반면 내가 작성한 코드가 제어의 흐름을 담당한다면 그것은 프레임워크가 아니라 라이브러리이다.

### DI, Dependency Injection, 의존관계 주입
의존관계는 **정적인 클래스 의존 관계**와 **동적인 객체(인스턴스) 의존 관계** 둘을 분리해서 생각해야한다.  
**정적인 클래스 의존 관계**  
클래스가 사용하는 import 코드만 보고 의존관계를 쉽게 판단할 수 있다. 즉 코드를 보면 관계를 알 수 있는 의존을 정적인 클래스 의존관계라고 한다.
  
**동적인 객체 인스턴스 의존 관계**  
애플리케이션 실행 시점에 실제 생성된 객체 인스턴스의 참조가 연결된 의존 관계이다.  
- 애플리케이션 실행 시점에 외부에서 실제 구현 객체를 생성하고 클라이언트에 전달해서 클라이언트와 서버의 실제 의존관계가 연결되는 것을 의존관계 주입이라 한다.
- 이를 이용하면 정적인 클래스 의존관계를 변경하지 않고 동적인 객체 인스턴스 의존관계를 쉽게 변경할 수 있다.

### IoC 컨테이너 DI 컨테이너
`AppConfig` 처럼 객체를 생성하고 관리하면서 의존관계를 연결해주는 것을 IoC 컨테이너 또는 DI 컨테이너라 한다. 또는 어셈블러, 오브젝트 팩토리 등으로 불리기도 한다.

## 스프링으로의 변경
Spring 으로 전환하기 위해 해야하는 몇 가지 작업이 있다.
1. `AppConfig`에 설정을 구성한다는 뜻의 어노테이션 `@Configuration` 을 붙여준다.
2. 각 메서드에 `@Bean`을 붙여준다. 이러면 스프링 컨테이너에 스프링 빈으로 등록한다.
```java
@Configuration
public class AppConfig {
    
    @Bean
    public MemberService memberService() {
        return new MemberServiceImpl(memberRepository());
    }
}
```
그리고 각 개체가 필요한, 메서드를 사용하는 코드에서 객체를 받아오는 방식이 달라진다.
  
```java
// 기존
AppConfig appConfig = new AppConfig();
MemberService memberService = appConfig.memberService();

// 변경 후
ApplicationContext applicationContext = new AnnotationConfigApplicationContext(AppConfig.class);
MemberService memberService = applicationContext.getBean("memberService", MemberService.class);
```
객체 생성부가 조금 길어졌지만 이는 이후 엄청난 효과를 불러온다고 한다.  
.getBean() 메서드는 매개변수로 메서드 명과 클래스를 받는데 이 때 메서드 명은 위와 같이 String 으로 넣어줘야한다.
  
### 스프링 컨테이너
`ApplicationContext`를 스프링 컨테이너라 한다. 기존에는 개발자가 AppConfig를 사용해서 직접 객체를 생성하고 DI 했지만 이제부터는 스프링 컨테이너를 사용한다.  
스프링 컨테이너는 `@Configuration`이 붙은 `AppConfig`를 설정(구성) 정보로 사용한다. 이 때 `@Bean` 이 적힌 메서드를 모두 호출해서 반환된 객체를 스프링 컨테이너에 등록한다.
이렇게 등록된 객체를 스프링 빈이라 한다. 스프링 빈은 @Bean 이 붙은 메서드 명을 스프링 빈의 이름으로 사용한다.  
기존에는 개발자가 직접 자바코드로 모든 것을 헀다면 이제부터는 스프링 컨테이너에 객체를 스프링 빈으로 등록하고 스프링 컨테이너에서 스프링 빈을 찾아서 사용하도록 변경되었다.