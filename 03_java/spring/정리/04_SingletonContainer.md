# ***Singleton Container***

보통 웹 애플리케이션은 여러 고객이 동시에 요청을 한다. 그럼 스프링 없는 순수한 DI 컨테이너는 고객의 요청이 발생할 때마다 객체를 새로 생성해서 반환한다. 트래픽이 초당 100 나오면 객체도 초당 100개가 생성되고 소멸된다. 이는 심한 메모리의 낭비가 될 수 있는데 싱글톤 패턴은 이를 해결한다. 바로 객체가 단 하나만 생성되고 공유되도록 설계하는 것인데 이러한 방식을 싱글톤 패턴이라고 한다.
  
즉, 싱글톤 패턴은 클래스의 인스턴스를 딱 1개만 생성되는 것을 보장하는 디자인 패턴으로 인스턴스가 2개 이상 생성되는 것을 막는다.
```java
public class SingletonService {
    
    // static 영역에 객체를 한 개 생성해둔다.
    private static final SingletonService instance = new SingletonService();

    // get 메서드로 객체를 조회한다.
    public static SingletonService getInstance() {
        return instance;
    }
    
    // 생성자를 private 으로 설정해 생성을 막는다.
    private SingletonService() {
    }
}
```
싱글톤을 구현하는 방법이 이 방법만 있는 것은 아니지만 이 방법이 가장 단순하고 안전하다.
  
이렇게 싱글톤 패턴을 적용하면 객체를 하나만 만들고 공유해서 효율적으로 사용할 수 있지만 다음과 같은 단점이 있다.
- 초기 비용이 크다. ( 코드 )
- 의존관계상 클라이언트가 구현에 의존한다. -> DIP 위반
- 클라이언트가 구현에 의존해 OCP 원칙을 위반할 가능성이 높다
- 테스트가 까다롭다.
- 내부 속성의 변경 및 초기화가 어렵다
- 생성자로 자식 클래스를 만들기 어렵다.
- 유연성이 떨어진다.

## Singleton Container
스프링 컨테이너는 위의 문제점들을 해결하면서 싱글톤 패턴을 유지할 수 있다.
  
**싱글톤 컨테이너**
- 스프링 컨테이너는 싱글턴 패턴을 적용하지 않아도 객체 인스턴스를 싱글톤으로 관리한다.
  - 컨테이너는 객체를 하나만 생성한다.
- 스프링 컨테이너는 싱글톤 컨테이너 역할을 한다. 이렇게 싱클톤 객체를 생성하고 관리하는 기능을 싱글톤 레지스트리라 한다.
- 스프링 컨테이너 덕분에 위 문제점을 해결하며 패턴을 유지할 수 있다.
![SingletonContainer](/key/properties/AdoptSingleton.png)
  
## 주의점
- 싱글톤 패턴이든 스프링 같은 컨테이너를 사용하든 객체 인스턴스를 하나만 생성하는 방식은 모두가 같은 인스턴스를 공유하기 때문에 상태를 유지하도록 설계하면 안된다.
- 즉, `무상태(stateless)`로 설계해야한다.
  - 특정 클라이언트에 의존적인 필드가 있으면 안된다.
  - 특정 클라이언트가 값을 변경할 수 있는 필드가 있으면 안된다.
  - 가급적 읽기만 가능해야한다.
  - 필드 대신 자바에서 공유되지 않는 지역변수, 파라미터, ThreadLocal 등을 사용해야한다.

```java
public class StatefulService {
    private int price;

    public void order(String name, int price) {
        System.out.println("name = " + name + " price = " + price);
        this.price = price;
    }

    public int getPrice() {
        return price;
    }
}
```
너무나 당연하게도 위 order 메서드에서 필드를 변경하면 같은 객체를 공유하는 모든 클라이언트에 이 값을 공유하게 된다.  
A고객의 물품 구매와 결제 사이에 B고객의 물품 구매가 끼게 되면 A고객의 결제 대금은 B고객의 가격이 되는 것이다.

  
## @Configuration 과 싱글톤
```java
@Configuration
public class Appconfig {

    @Bean
    public MemberService memberService() {
        return new MemberServiceImpl(memberRepository());
    }

    @Bean
    public OrderService orderService() {
        return new OrderServiceImpl(
                memberRepository(),
                discountPolicy()
        );
    }

    @Bean
    public MemberRepository memberRepository() {
        returj new MemoryMemberRepository();
    }
}
```
위 코드를 보면 `memberRepository()` 를 메서드 두 곳에서 호출하고 있다. 그럼 `new MemoryMemberRepository` 또한 두 번 생성되고 같은 클래스의 인스턴스가 두 개가 된다.
  
하지만 실제 검증을 해보면 메서드가 한 번밖에 호출되지 않는 것을 볼 수 있다.
  
이는 스프링의 기능인데 `@Configuration`을 적용하게 되면 스프링 빈에 등록될 때 우리가 만든 컨텍스트가 등록되는 것이 아니다. 스프링이 클래스의 바이트코드를 조작하는 라이브러리를 사용하기 때문인데 이것의 효과는 우리가 만든 클래스를 모두 상속받는 새로운 클래스를 만들어서 컨테이너에 등록하고 클래스가 호출될 때 유무를 확인해서 있다면 있는 객체를 반환하고 없다면 새로 만들어서 반환하는 것이다.

```java
@Bean
public MemberRepository memberRepository() {
    
    if ( memoryMemberRepository 가 이미 컨테이너에 있다면 ) {
        return 컨테이너에서 찾아서 반환
  } else { // 컨테이너에 없다면
        기존 로직을 호출해 MemoryMemberRepository를 생성하고 컨테이너에 등록
        return 반환    
}
```
Config 클래스에 @Configuration 어노테이션을 달지 않으면 이는 기능하고 싱글톤 기능을 잃는다. 반드시 달아둘 수 있도록 하자.
  
- @Bean 만 사용해도 스프링 빈으로 등록되지만 싱글톤이 보장되지 않는다.
- 스프링 설정 정보는 항상 `@Configuration`을 사용하자.