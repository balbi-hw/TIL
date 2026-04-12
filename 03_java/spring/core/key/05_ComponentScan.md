# ***Component Scan***

## 컴포넌트 스캔과 의존관계 자동 주입
컴포넌트 스캔은 쉽게 말하면 **의존관계 자동 주입** 이다!  
지금까지 스프링 빈을 등록할 때는 `@Bean` 어노테이션을 이용해 직접 설정 정보에 빈을 등록했다. 지금까지는 그 수가 얼마 되지 않아서 가능했지만 이 수가 많아지면 실수가 생기기 쉽다!  
그래서 스프링은 설정 정보가 없어도 자동으로 스프링 빈을 등록하는 컴포넌트 스캔이라는 기능을 제공한다. 또한 의존관계도 자동으로 주입하는 `@Autowired`라는 기능도 제공한다.
```java
@Configuration
@ComponentScan(
        excludeFilters = @Filter(type = FilterType.ANNOTATION, classes = Configuration.class))
public class AutoAppConfig {
}
```
컴포넌트 스캔을 사용하기 위해서는 이렇게 `@ComponentScan`을 설정 정보에 붙여주면 된다. 지금까지 작성한 AppConfig와는 다르게 @Bean 이 하나도 없다!
  
> 참고로 컴포넌트 스캔을 사용하면 `@Configuration`이 붙은 설정 정보도 자동으로 등록된다. 등록하고 싶지 않은 설정 정보가 있다면 위 코드와 같이 excludeFilters 를 설정하자. 이는 컴포넌트 대상에서 제외한다는 의미이다.

  
컴포넌트 스캔은 `@Component`가 붙은 클래스를 스캔해서 스프링 빈으로 자동 등록한다. ( @Configuration 또한 소스코드에 @Component 가 붙어있다. )
  
```java
@Component
public class MemoryMemberRepository implements MemberRepository {}

@Component
public class RateDiscountPolicy implements DiscountPolicy {}

@Component
public class MemberServiceImpl implements MemberService {
    
    private final MemberRepository memberRepository;

    @Autowired
    public MemberServiceImpl(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }
}
```
이렇게 `@Component`가 붙은 클래스들을 자동으로 컨테이너에 등록하고 `@Autowired`를 통해 DI도 자동으로 진행된다.
  
```java
public class AutoAppConfigTest {

    @Test
    void basicScan() {
        ApplicationContext ac = new AnnotationConfigApplicationContext(AutoAppConfig.class);
        MemberService memberService = ac.getBean(MemberService.class);
        assertThat(memberService).isInstanceOf(MemberService.class);
    }
}
```
`AnnotationConfigApplicationContext()` 를 사용하는 것은 기존과 동일하지만 인자로 AutoAppConfig 클래스를 넘겨준다는 점이 다르다. 실행해보면 기존과 같이 동작한다는 걸 확인할 수 있다.

## 탐색 위치와 기본 스캔 대상
모든 자바 클래스를 다 탐색해서 빈에 등록하면 시간이 오래 걸린다. 그래서 탐색 시작 위치를 지정하는 기능을 제공한다.
```java
@ComponentScan(
        basePackages = "hello.core",
)
```
- `basePackages`: 탐색을 시작할 위치를 지정한다. 이 패키지를 포함해서 하위 패키지를 모두 탐색한다. 두 개 이상의 위치를 지정 할 수도 있다.
- `basePackageClasses`: 지정한 클래스의 패키지를 탐색 시작 위치로 지정한다.
- 만약 지정하지 않으면 `@ComponentScan`이 붙은 설정 정보 클래스의 패키지가 시작 위치가 된다.

**권장**  
패키지 위치를 지정하지 않고 설정 정보 클래스의 위치를 프로젝트 최상단에 두는 것이다. ( 지금까지 해왔던 방식 )  
최근의 스프링 부트도 이 방법을 기본으로 제공한다.  
  
참고로 스프링 부트를 사용하면 스프링 부트의 대표 시작 정보인 `@SpringBootApplication`을 이 프로젝트 시작 루트 위치에 두는 것이 관례이다. ( 이 어노테이션 안에도 `@ComponentScan`이 들어있다. )
  
### 기본 스캔 대상
컴포넌트 스캔은 `@Component`뿐만 아니라 다음의 내용들도 추가로 대상에 포함한다.
- `@Controller`: 스프링 MVC 컨트롤러에서 사용
- `@Service`: 스프링 비즈니스 로직에서 사용
- `@Repository`: 스프링 데이터 접근 계층에서 사용
- `@Configuration`: 스프링 설정 정보에서 사용

위 어노테이션들도 소스코드를 보면 `@Component`를 포함하고 있는 것을 알 수 있다.

> 참고: 어노테이션에는 상속관계라는 것이 없지만 이렇게 인식할 수 있는 것은 자바가 아니라 스프링에서 제공하는 기능이다.
  
위 어노테이션은 컴포넌트 스캔의 용도 뿐만이 아니라 다음과 같은 부가기능이 달려있다.
- `@Controller`: 스프링 MVC 컨트롤러로 인식
- `@Repository`: 스프링 데이터 접근 계층으로 인식하고 데이터 계층의 예외를 스프링 예외로 변환
- `@Configuration`: 스프링 설정 정보로 인식하고 빈이 싱글톤을 유지하도록 추가 처리
- `@Service`: 스프링에서 특별한 처리를 하지는 않지만 가독성을 높여 동료 개발자들에게 도움을 줌

## 필터
- `includeFilters`: 컴포넌트 스캔 대상을 추가로 지정한다.
- `excludeFilters`: 컴포넌트 스캔에서 제외할 대상을 지정한다.  
사용법은 필요할 때 찾아보자. 자주 사용하지 않는다고 한다.

## 중복 등록과 충돌
컴포넌트 스캔에서 같은 빈 이름을 등록하면 어떻게 될까?
  
1. 자동 vs 자동
2. 수동 vs 자동

### 자동 vs 자동
자동으로 스프링 빈이 등록될 때 이름이 같은 클래스가 있을 경우 스프링은 오류를 발생시킨다.
- `ConflictingBeanDefinitionException` 에외 발생

### 수동 vs 자동
이 경우 수동으로 등록한 빈이 우선권을 가진다. ( 수동이 자동을 오버라이딩 한다. )  
이렇게 되기는 하지만 이를 의도하고 사용해선 안될 것이다 ! 명확성 !
  
스프링 부트에서는 기본값으로 해당 기능을 막아두고 있다.