# ***EXCEPTION HANDLING***

앞에서 만든 예외처리 코드는 정상 흐름과 예외 흐름이 섞여있어 코드를 이해하기가 어려웠다.  
심지어 예외흐름이 더 많은 분량을 차지했고 실무에서는 이 처리가 훨씬 더 복잡해진다.  
  
```java
public class NetworkClientExceptionV2 extends Exception {
    private String errorCode;

    public NetworkClientExceptionV2(String errorCode, String message) {
        super(message);
        this.errorCode = errorCode;
    }

    public String getErrorCode() {
        return errorCode;
    }
}
```
- 예외 또한 객체이기 때문에 필드와 메서드를 가질 수 있다.
- 오류 코드
  - 이전에는 오류 코드를 **반환값**으로 리턴해서 어떤 오류가 있는지 구분했다.
  - 여기서는 오류 코드를 예외 내부에 필드로 보관한다.
- 오류 메시지
  - 오류 메시지는 어떤 오류가 발생했는지 개발자가 보고 이해할 수 있도록 설명을 담아둔다.
  
```java
public class NetworkClientV2 {
    
    private final String address;
    public boolean connectError;
    public boolean sendError;

    public NetworkClientV2(String address) {
        this.address = address;
    }
    
    public void connect() throws NetworkClientExceptionV2 {
        if (connectError) {
            throw new NetworkClientExceptionV2("connectError", address + " 서버 연결 실패");
        }

        System.out.println(address + " 서버 연결 성공");
    }
    
    public void send(String data) throws NetworkClientExceptionV2 {
        if (sendError) {
            throw new NetworkClientExceptionV2("sendError", address + " 서버에 데이터 전송 실패: " + data);
        }

        System.out.println(address + " 서버에 데이터 전송: " + data);
    }

    public void disconnect() {
        System.out.println(address + " 서버 연결 해제");
    }

    public void initError(String data) {
        if (data.contains("error1")) {
            connectError = true;
        }
        if (data.contains("error2")) {
            sendError = true;
        }
    }
}
```
- 기존 코드와 대부분 같지만 오류가 발생했을 때 코드를 반환하는 게 아니라 예외를 던진다.
- 반환값이 필요 없고 반환 값을 void로 처리한다.
- 메서드가 정상 종료되면 성공이고 예외가 던져지면 실패임을 알 수 있다.
  
## 예외 복구
이번에는 던지는 것 말고 예외를 잡아서 처리해보자

```java
public class NetworkServiceV2_2 { 
    public void sendMessage(String data) {
        String address = "hyperlink";
        
        NetworkClientV2 client = new NetworkClientV2(address);
        client.initError(data);
        
        try {
            client.connect();
        } catch (NetworkClientExceptionV2 e) {
            System.out.println("[오류] 코드: " + e.getErrorCode() + ", 메시지: " + e.getMessage());
            return;
        }
        
        try {
            client.send(data);
        } catch (NetworkClientExceptionV2 e) {
            System.out.println("[오류] 코드: " + e.getErrorCode() + ", 메시지: " + e.getMessage());
            return;
        }
        
        client.disconnect();
    }
}
```
- connect, send 와 같이 예외가 발생할 수 있는 곳을 try, catch 문을 사용해서 예외를 잡는다.
- 이 코드에서는 예외를 잡으면 코드와 메시지를 출력한다.
- 이렇게 예외를 처리하면 이후에는 정상흐름으로 돌아온다.
  
하지만 지금 두 try 문이 사실상 중복이다. 다음에는 이걸 없애보자.

## 예외처리 - 정상, 예외 흐름의 분리

```java
public class NetworkServiceV2_3 {
    public void sendMessage(String data) {
      String address = "log";

      NetworkClientV2 client = new NetworkClientV2(address);
      client.initError(data);

      try {
        client.connect();
        client.send(data);
        client.disconnect();
      } catch (NetworkClientExceptionV2 exceptionV2) {
        System.out.println("[오류] 코드: " + e.getErrorCode() + ", 메시지: " + e.getMessage());
      }
    }
}
```
- 하나의 try 안에 정상 흐름을 모두 담는다.
- 예외는 catch 블럭에서 해결한다.
  
이렇게 하나의 흐름으로 묶으면 코드 중복을 없앨 수 있다. 하지만 이러면 예외 발생 시 disconnect 가 호출되지 않는 문제가 남는다.

## 예외처리 - finally
자바에서는 어떤 경우라도 반드시 호출되는 finally 기능을 제공한다.
- try ~ catch ~ finally 구조는 정상 흐름, 예외 흐름, 마무리 흐름을 제공한다.
- try 를 시작하기만 하면 finally 블럭은 어떤 경우라도 반드시 호출 된다.
- 그래서 주로 try 에서 사용한 자원을 해제할 때 주로 사용한다.

```java
public class NetworkServiceV2_5 {

  public void sendMessage(String data) {
    String address = "link";

    NetworkClientV2 client = new NetworkClientV2(address);
    client.initError(data);
    
    try {
        client.connect();
        client.send(data);
    } catch (NetworkClientExceptionV2 e) {
      System.out.println("[오류] 코드: " + e.getErrorCode() + ", 메시지: " + e.getMessage());
    } finally {
        client.disconnect();
    }
  }
}
```
- finally 는 무슨 일이 있어도 실행되기 때문에 catch 에서 정의하지 않은 예외가 발생해도 자원을 반환할 수 있다.
- catch 없이도 사용할 수 있다.

## 예외 계층
이전에 언급했던것 같이 예외도 객체이고 필연적으로 상속관계가 존재한다. 이는 계층이 존재한다는 것을 의미한다.  
이를 이용하면 주의해야하는 예외만 따로 처리하고 크게 중요치 않은 예외들은 상위 클래스로 한 번에 묶어서 처리할 수 있을 것이다.

```java
    try {
        client.connect();
        client.send(data);
    } catch (NetworkClientExceptionV2 e) {
        System.out.println("[오류] 코드: " + e.getErrorCode() + ", 메시지: " + e.getMessage());
    } catch (Object o) {
        "Error 처리"
    }
```
조금 극단적이지만 위 처럼 하면 NetworkClientExceptonV2 예외만 주의해서 따로 처리하고 다른 예외들은 Object로 싸잡혀서 처리된다.

## 실무 예외 처리 방안
**처리 불가능한 예외**
예를 들어 상대 네트워크 서버에 문제가 발생해서 통신이 불가능하거나 데이터베이스 서버에 문제가 발생해 접속이 안되면 예외가 발생한다.  
그런데 이런 예외들은 우리쪽에서 처리할 수 있는게 없다. 잡아도 해결할 수가 없다.
  
이런 경우는 고객에게 안내 메시지를 보내고 오류에 대한 로그를 남겨둬야한다.
  
**체크 예외의 부담**
체크 예외는 개발자의 실수를 커버할 수 있기 때문에 많이 사용되었지만 기술이 발전하여 프로그램이 점점 복잡해지면서
체크 예외를 사용하는 것이 점점 더 부담스러워졌다. 수 없이 많이 발생하는 예외들을 하나하나 처리할 수가 없기 때문이다.

## try-with-resources
어플에서 외부 자원을 사용하는 경우 반드시 외부 자원을 해제해야한다. 따라서 finally 구문을 반드시 사용해야한다.
  
그런데 try-with-resources 기능을 사용하면 finally 를 선언하지 않아도 된다.  
이 기능을 사용하기 위해서는 AutoCloseable 인터페이스를 구현해야한다.

```java
public interface AutoCloseable {
    void close() throws Exception;
}

@Override
public void close() {
  System.out.println("NetworkClientV5.close");
  disconnect();
}
```
위 AutoCloseable 을 구현해서 close() 메서드를 오버라이딩하면 try 종료 시 반드시 호출된다.
  
**장점**
- 리소스 누수 방지: 모든 리소스가 제대로 닫히도록 보장한다. 실수로 finally 를 적지 않거나 자원 해제 코드를 누락하는 문제를 예방할 수 있다.
- 코드 간결성 및 가독성 향상: 명시적인 close 호출이 필요 없어 코드가 더 간결해지고 이해하기 쉬워진다.
- 스코프 범위 한정: resource 의 스코프가 try 안의 블럭으로 한정된다. 코드 유지보수가 더 쉬워진다.
- 더 빠른 자원 반납: 기존에는 catch 이후 finally 로 자원을 반납했지만 이젠 try 가 끝나면 바로 자원을 반납한다.
  
## 정리
처음 자바가 설계될 때에는 체크 예외가 더 나은 선택이었다. 예외가 그렇게 많지 않았기 때문이다. 그래서 자바가 기본으로 제공하는 기능에는
체크 예외가 많다. 하지만 프로그램이 복잡해지며 점점 예외가 늘어났고 이젠 체크 예외를 사용하기에는 부담스러워졌다.
  
이런 문제 때문에 최근 라이브러리들은 대부분 런타임 예외를 기본으로 제공한다. 가장 유명한 스프링이나 JPA 같은 기술들도 대부분 언타임 예외를 사용한다.
  
런타임 예외도 필요 시 잡을 수 있기 때문에 필요한 경우만 잡아서 처리하고 그렇지 않으면 자연스럽게 던지도록 둔다.
