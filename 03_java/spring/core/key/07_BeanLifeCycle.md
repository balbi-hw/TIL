# ***빈 생명주기 콜백***

## 생명주기 콜백

데이터 베이스 커넥션 풀이나 네트워크 소켓처럼 애플리케이션 시작 시점에 필요한 연결으 미리 해두고 종료 시점에 연결을 모두 종료하는 작업을 진행하려면 객체의 초기화와 종료 작업이 필요하다.  
  
간단하게 외부 네트워크에 미리 연결하는 객체를 하나 생성한다고 생각하고 코드를 보자. `NetworkClient`는 애플리케이션 시작 시점에 `connect()`를 호출해셔 연결하고 종료되면 `disConnect()`를 호출해서 연결을 끊어야 한다.

```java
import java.beans.BeanProperty;
import java.nio.channels.NetworkChannel;

public class NetworkClient {

    private String url;

    public NetworkClient() {
        System.out.println("생성자 호출, url = " + url);
        connect();
        call("초기화 연결 메시지");
    }

    public void setUrl(String url) {
        this.url = url;
    }

    // 서비스 시작시 호출
    public void connect() {
        System.out.println("connect: " + url);
    }

    public void call(String message) {
        System.out.println("call: " + url + " message = " + message);
    }

    // 서비스 종료시 호출

    public void disconnect() {
        System.out.println("close: " + url);
    }
}

// 테스트
public class BeanLifeCycleTest {

    @Test
    public void lifeCycleTest() {
        ConfigurableApplcationContext ac = new AnnotationConfigApplicationContext(LifeCycleConfig.class);
        NetworkClient client = ac.getBean(NetworkClient.class);
        ac.close(); //스프링 컨테이너를 종료, ConfigurableApplicationContext 타입이 필요하다.
    }

    @Configuration
    static class LifeCycleConfig {

        @Bean
        public NetworkClient networkClient() {
            NetworkClient networkClient = new NetworkClent();
            networkClient.setUrl("http://hello-spring.dev");
            return networkClient;
        }
    }
}
//실행 결과
생성자 호출, url = null
connect: null
call: null message = 초기화 연결 메시지
```
생성자를 보면 url 정보 없이 connect가 호출되고 있다. 생성자를 보면 url 을 초기화하지 않는데 connect를 호출하기 떄문에 그렇다.  
객체를 생성하고 url 이 초기화가 된 후에 connect 를 호출해야 정상적인 결과가 나온다.
  
스프링 빈은 간략하게하면 다음과 같은 라이프사이클을 가진다.
**객체 생성 -> DI**  
  
빈은 객체를 생성하고 DI가 다 끝난 다음에야 필요한 데이터를 사용할 준비가 완료된다. 따라서 초기화는 DI가 모두 완료되고 난 다음에 호출해야한다. 하지만 이걸 어떻게 파악할 수 있을까?  
**스프링은 DI가 완료되면 빈에게 콜백 메서드를 통해서 초기화 시점을 알려주는 다양한 기능을 제공한다.** 또한 스프링은 스프링 컨테이너가 종료되기 직전에 소멸 콜백을 해준다.
  
**스프링 빈의 이벤트 라이프 사이클**  
컨테이너 생성 -> 빈 생성 -> DI -> 초기화 콜백 -> 사용 -> 소멸전 콜백 -> 스프링 종료  
- 초기화 콜백: 빈이 생성되고 DI가 끝난 후 호출
- 소멸전 콜백: 빈이 소멸되기 직전에 호출
  
> **참고**:  
> 그럼 생성자에서 객체를 만들 때 필드에 값을 부여하면 되는거 아닐까? 결론은 '자제하는게 좋다.'이다. 생성자는 필수 정보를 받고 메모리를 할당해서 객체를 생성하는데 초기화는 이렇게 생성된 값을 활용해서 외부 커넥션을 연결하는 등 무거운 동작을 수행한다.  
> 따라서 생성자 안에서 무거운 초기화 작업을 함께 하는 것보다는 객체를 생성하는 부분과 초기화하는 부분을 나누는 것이 **유지보수** 관점에서 좋다.

> **참고**:  
> 싱글톤 빈들은 스프링 컨테이너가 종료될 때 싱글톤 빈도 함꼐 종료되기 떄문에 스프링 컨테이너가 종료되기 직전에 소멸전 콜백이 일어난다. 뒤에서 다루지만 싱글톤 처럼 컨테이너의 시작과 끝까지 생존하는 빈도 있는 반면 생명주기가 더 짧은 빈들도 있는데 이러한 빈들은 컨테이너와 무관하게 해당 빈이 종료되기 직전에 소멸전 콜백이 일어난다.

  
**스프링은 크게 3가지 방법으로 빈 생명주기 콜백을 지원한다,**  
- 인터페이스 ( InitializingBean, DisposableBean )
- 설정 정보에 초기화 메서드, 종료 메서드 지정
- @PostConstruc, @PreDestroy 애노테이션 지원

## 1. 인터페이스, InitializingBean, DisposableBean

```java
public class NetworkClient implements InitializingBean, DisposableBean {
    
    private String url;
    
    // 등등
    
    @Overide
    public void afterPropertiesSet() throws Exception {
        cnnect();
        call("초기화 연결 메시지");
    }
    
    @Overide
    public void destroy() throws Exception {
        disConnect();
    }
}
```
- `InitailizingBean`은 `afterPropertiesSet()` 메서드로 초기화를 지원한다.
- `DisposibaleBean`은 `destroy()` 메서드로 소멸을 지원한다.

**단점**  
- 이 인터페이스는 스프링 전용 인터페이스로 해당 코드가 스프링 전용 인터페이스에 의존한다.
- 초기화, 소멸 메서드의 이름을 변경할 수 없다.
- 내가 코드를 고칠 수 없는 외부 라이브러리에 적용할 수 없다.
- 스프링 초창기의 방법이고 거의 사용되지 않는다.

## 2. 빈등록 초기화, 소멸 메서드 지정

설정 정보에 `@Bean(initMethod = "init", destroyMethod = "close")` 처럼 초기화, 소멸 메서드를 지정할 수 있다.

```java

@Configuration
static class LifeCycleConfig {

    @Bean(initMethod = "init", destroyMethod = "close")
    public NetworkClient networkClient() {
        NetworkClient networkClient = new NetworkClient();
        networkClient.setUrl("http://hello-spring.dev");
        return networkClient;
    }
}
```
- 메서드 이름을 자유롭게 설정 가능하다.
- 스프링 빈이 스프링 코드에 의존하지 않는다.
- 코드가 아니라 설정 정보를 사용하기 떄문에 코드를 고칠 수 없는 외부 라이브러리에서도 초기화, 종료 메서드를 적용할 수 있다.

**종료 메서드 추론**
- `@Bean의 destroyMethod`속성에는 아주 특별한 기능이 있다.
- 라이브러리는 대부분 `close`, `shutdonw`이라는 이름의 종료 메서드를 사용한다.
- `@Bean`의 `destroyMethod`는 기본값이 `(inferred)`(추론)으로 되어있다.
- 이 추론 기능은 위의 close 와 shutdown 같은 이름의 메서드를 자동으로 호출해준다.
- 따라서 스프링 빈으로 등록하면 종료 메서드는 따로 적어주지 않아도 동작한다.
- 추론 기능을 사용하기 싫으면 `destroyMethod=""`처럼 공백을 설정하면 된다.

## 3. 애노테이션 @PostConstruct, @PreDestroy

```java
public class NetworkClient {
    private String url;

    public NetworkClient() {
        System.out.println("생성자 호출, url = " + url);
    }

    public void setUrl(String url) {
        this.url = url;
    }

    // 서비스 시작시 호출
    public void connect() {
        System.out.println("connect: " + url);
    }

    // 종료시 호출
    public void disConnect() {
        System.out.println("close: " + url);
    }

    @PostConstruct
    public void init() {
        System.out.println("NetworkClient.init");
        connect();
        call("초기화 연결 메시지");
    }

    @PreDestroy
    public void close() {
        System.out.println("NetworkClient.close");
        disConnect();
    }
}
```
- 최신 스프링에서 가장 권장하는 방법이고 애노테이션 하나만 붙이면 되므로 매우 편리하다.
- 스프링에 종속적인 기술이 아니라 자바 표준이다. 따라서 스프링이 아닌 다른 컨테이너에서도 사용 가능하다.
- 컴포넌트 스캔과 잘 어울린다.
- 유일한 단점으로 외부 라이브러리에는 적용이 불가능하다는 점이 있다. 외부 라이브러리를 초기화, 종료해야한다면 @Bean 의 기능을 사용하자.

**정리**  
**@PostConstruct, @PreDestroy 를 사용하자.**