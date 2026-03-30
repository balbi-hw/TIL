# ***EXCEPTION HANDLING***

## 예외처리가 왜 필요해?
사용자의 입력을 받고 입력 받은 문자를 외부 서버에 전송하는 프로그램을 만들어보자.

```java
import java.util.Scanner;

public class NetworkClientV0 {
    private final String address;

    public NeteworkClientV0(String address) {
        this.address = address;
    }

    public String connect() {
        System.out.println(address + " 서버 연결 성공");
        return "success";
    }

    public String send(String data) {
        System.out.println(address + " 서버 데이터 전송: " + data);
        return success;
    }

    public void disconnect() {
        System.out.println(address + " 서버 연결 해제");
    }
}

// Service 클래스는 Client 사용 로직을 처리한다.
public class NetworkServiceV0 {

    public void sendMessage(String data) {
        String address = "http://example.com";
        NetworkClientV0 client = new NetworkClientV0(address);

        client.connect();
        client.send(data);
        client.disconnect();
    }
}

// 메인
import java.util.Scanner;

public class MainV0 {

    public static void main(String[] args) {
        NetworkServiceV0 networkService = new NetworkServiceV0();

        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.print("전송할 문자");
            String input = scanner.nextLine();
            if (input.equals("exit")) {
                break;
            }
            networkService.sendMessage(input);
            System.out.println();
        }
        System.out.println("프로그램을 정상 종료합니다.");
    }
}
```
이렇게 의도대로 진행되는 코드를 만들었다.  
그런데 이대로 서비스를 런칭하면 어떻게될까..  
아마 말도 안되는 예외, 오류들로 범벅되어 제대로 기능하지 못할 가능성이 높다.
- 외부 서버 문제
- 클라이언트 문제
- 인터넷 연결 문제
- 그 외 등등
  
물론 지금은 실제 통신이 아니기에 발생하지 않는다. 대신 오류 상황을 시뮬레이션 해보자.

1. 네트워크 연결에 실패한 상황
2. 데이터 전송에 실패한 상황

```java
// NetworkClientV1

public class NetworkClientV1 {
    private final String address;
    public boolean connectError;
    public boolean sendError;

    public NetworkClientV1(String address) {
        this.address = address;
    }

    public String connect() {
        if (connectError) {
            System.out.println(address + " 서버 연결 실패");
            return "connectError"
        }

        System.out.println(address + " 서버 연결 성공");
        return "success";
    }

    public String send(String data) {
        if (sendError) {
            System.out.println(address + " 서버에 데이터 전송 실패: " + data);
            return "sendError";
        }

        System.out.println(address + " 서버에 데이터 전송: " + data);
        return "success";
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
- ClientV1 에는 `connectError`, `sendError` 가 추가되었다.
- initError(String data) 메서드를 통해 connectError, sendError 의 값을 컨트롤 할 수 있다.

```java
public class NetworkServiceV1_1 {
    
    public void sendMessage(String data) {
        String address = "http://example.com";
        NetworkClientV1 client = new NetworkClientV1(address);
        client.initError(data);

        client.connect();
        client.send(data);
        client.disconnect();
    }
}

public class MainV1 {

    public static void main(String[] args) {
        NetworkServiceV1_1 networkService = new NetworkServiceV1_1();

        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.print("전송할 문자: ");
            String input = scaaner.nextline();
            if (input.equals("exit")) {
                break;
            }
            networkService.sendMessage(input);
            System.out.println();
        }
        System.out.println("프로그램을 정상 종료합니다.");
    }
}
//전송할 문자: hello
//http://example.com 서버 연결 성공
//http://example.com 서버에 데이터 전송: hello
//http://example.com 서버 연결 해제

//전송할 문자: error1
//http://example.com 서버 연결 실패
//http://example.com 서버에 데이터 전송: error1
//http://example.com 서버 연결 해제

//전송할 문자: error2
//http://example.com 서버 연결 성공
//http://example.com 서버에 데이터 전송 실패: error2
//http://example.com 서버 연결 해제

//전송할 문자: exit
//프로그램을 정상 종료합니다.
```
네트워크 연결이 실패하면 데이터 전송을 하지 말아야하는데 데이터 전송을 시도한다.  
또한 오류가 발생했을 때 어떤 오류가 발생했는지 자세한 내역을 남기면 이후 디버깅에 도움이 된다. 로그를 남기자.


```java
public class NetworkServiceV1_2 {

    public void sendMessage(String data) {
        NetworkClientV1 client = new NetworkClientV1("http://example.com");
        clinet.initError(data);

        String connectResult = client.connect();
        if (isError(connectResult)) {
            System.out.println("[네트워크 오류 발생] 오루 코드: " + connectResult);
            return;
        }

        String sendResult = client.send(data);
        if (isError(sendResult)) {
            System.out.println("[네트워크 오류 발생] 오류 코드: " + sendResult);
            return;
        }

        client.disconnect();
    }

    private static boolean isError(String resultCode) {
        return !resultCode.equals("success");
    }
}
//Main 실행 결과

//전송할 문자: hello
//http://example.com 서버 연결 성공
//http://example.com 서버에 데이터 전송: hello
//http://example.com 서버 연결 해제

//전송할 문자: error1
//http://example.com 서버 연결 실패
//[네트워크 오류 발생] 오류 코드: connectError

//전송할 문자: error2
//http://example.com 서버 연결 성공
//http://example.com 서버에 데이터 전송 실패: error2
//[네트워크 오류 발생] 오류 코드: sendError

//전송할 문자: exit
//프로그램을 정상 종료합니다.
```
연결이 실패하면 전송을 호출하지 않는다. 하지만 연결에 성공하면 전송에 실패해도 연결을 해제하지 않는다는 문제가 남았다.  
계속 이렇게 두면 네트워크 연결 자원이 고갈될 수 있다.

```java
public class NetworkServiceV1_3 {

    public void sendMessage(String data) {
        NetworkClientV1 client = new NetworkClientV1("http://example.com");
        clinet.initError(data);

        String conncetResult = client.connect();
        if (isError(connectResult)) {
            System.out.println("[네트워크 오류 발생] 오류 코드: " + connectResult);
        } else {
            String sendResult = client.send(data);
            if (isError(sendResult)) {
                System.out.println("[네트워크 오류 발생] 오류 코드: " + sendResult);
            }
        }
        
        client.disconnect();
    }
}
//Main 실행 결과

//전송할 문자: hello
//http://example.com 서버 연결 성공
//http://example.com 서버에 데이터 전송: hello
//http://example.com 서버 연결 해제

//전송할 문자: error1
//http://example.com 서버 연결 실패
//[네트워크 오류 발생] 오류 코드: connectError
//http://example.com 서버 연결 해제

//전송할 문자: error2
//http://example.com 서버 연결 성공
//http://example.com 서버에 데이터 전송 실패: error2
//[네트워크 오류 발생] 오류 코드: sendError
//http://example.com 서버 연결 해제

//전송할 문자: exit
//프로그램을 정상 종료합니다.
```
return 을 없애고 if문으로 분기를 만들었다.  
connect 에 실패하면 send 를 호출하지 않고 사용 후에는 반드시 disconnect를 호출해야한다. 의 두 조건 모두 충족했다.  
하지만 코드가 너무 직관적이지 않다.  

**정상흐름과 예외흐름**  
위 코드를 보면 정상흐름과 예외흐름이 전혀 분리되어 있지 않다. 코드를 이해하기가 너무 어렵다.  
예외 처리를 활용하면 이 문제를 해결할 수 있다.

## 예외처리1 - 예외 계층
자바는 프로그램 실행 중 발생할 수 있는 예외를 처리하기 위한 메커니즘을 제공한다.  
예외처리 키워드는 다음과 같은 것들이 있다.  
`try`, `catch`, `finally`, `throw`, `throws`
  
![Exception](/properties/Exception.png)
그리고 자바에서는 예외 또한 객체이다. 따라서 예외의 최상위 클래스 또한 Object가 된다.  
Object 바로 밑에는 Throwable 이 있다. 그리고 그 밑에 Exception 과 Error 가 있다.
- Error: 메모리 부족이나 심각한 시스템 오류와 같이 복구가 불가능한 시스템 예외이다. 이 예외는 잡으려 하면 안된다.
- Exception: 체크 예외
  - 애플리케이션 로직에서 사용할 수 있는 실질적인 최상위 예외이다.
  - Exception 과 그 하위 예외는 모두 컴파일러가 체크하는 예외이다. 하지만 그 중 RuntimeException 은 예외이다.
- RuntimeException: 언체크 예외, 런타임 예외
  - 컴파일러가 체크하지 않는 **언체크** 예외이다.
  
**체크 예외 vs 언체크 예외(런타임 예외)**
체크 예외는 발생한 예외를 개발자가 명시적으로 처리해야한다. 하지 않으면 컴파일이 되지 않는다. 하지만 언체크 에러는 컴파일이 된다.

## 예외처리2 - 예외 기본 규칙
예외는 폭탄 돌리기와 같다. 발생하면 처리하거나 불가하다면 밖으로 던져야한다.
- 예외는 잡아서 처리하거나 밖으로 던져야한다.
- 예외를 잡거나 던질 때 지정한 예외 뿐만 아니라 그 예외의 하위 예외들도 모두 함께 처리된다.
- Main 메서드에서 밖으로 던지면 예외 로그를 출력하며 시스템이 다운된다.

## 예외처리3 - 체크 예외
- Exception 과 그 하위 예외는 모두 컴파일러가 체크하는 예외이다. (Runtime 제외)

```java
public class MyCheckedException extends Exception {
    public MyCheckedException(String message) {
        super(message);
    }
}
```
- 예외 클래스를 만들기 위해서는 상속 받으면 된다.

```java
public class Client {
    public void call() throws MyCheckedException {
        throw new MyCheckedException("ex");
    }
}
```
- throw 키워드를 사용하면 새로운 예외를 발생시킬 수 있다. 예외또한 객체이기 때문에 객체를 먼저 생성하고 발생시켜야한다.
- throws 는 예외를 밖으로 던질 때 사용하는 키워드이다.
- `throw` 와 `throws` 차이 주의

```java
public class Service {
    Client client = new Client();

    public void callCatch() {
        try {
            client.call();
        } catch (MyCheckedException e) {
            System.out.println("예외 처리, message= " + e.getMessage());
        }
        System.out.println("정상 흐름");
    }
    
    public void callThrow() throws MyCheckedException {
        client.call();
    }
}
```
이렇게 예외 처리를 할 수 있다. 잡거나 던지거나.  
MyCheckedException 은 Exception 을 상속받아서 체크 예외가 되었다.  
참고로 RuntimeException 을 상속받으면 언체크 예외가 된다.

## 체크 예외의 장단점
체크 예외는 예외를 잡아서 처리할 수 없을 때, 예외를 밖으로 던지는 throws 예외를 필수로 선언해야한다. 그렇지 않으면 컴파일 오류가 발생한다.
- 장점: 개발자가 실수로 예외를 누락하지 않도록 컴파일러를 통해 문제를 잡아주는 훌륭한 안전 장치이다.
- 단점: 실제로는 개발자가 모든 체크예외를 반드시 잡거나 던지도록 처리해야하기 때문에 너무 번거로운 일이 된다.

**정리**  
체크 예외는 잡아서 직접 처리하거나 또는 밖으로 던지거나 둘중 하나를 개발자가 명시적으로 처리해야한다.

## 에최처리4 - 언체크 예외
- RuntimeException 과 그 하위 예외는 언체크 예외로 분류된다.
- 언체크 예외는 말 그대로 컴파일러가 예외를 체크하지 않는다는 뜻이다.
- 체크 예외와 기본적으로 동일하지만 언체크 예외는 throws 를 선언하지 않아도 밖으로 던질 수 있다.
- throws 를 선언해도 되고 안해도 된다. 안하면 컴파일러가 자동으로 처리한다.
  
**장단점**
- 장점: 신경쓰고 싶지 않은 언체크 예외를 무시할 수 있다.
- 단점: 언체크 예외는 개발자가 실수로 누락할 위험이 있다.
  
**정리**  
체크 예외와 언체크 예외의 차이는 예외를 처리할 수 없을 때 예외를 밖으로 던지는 부분에 있다. 이걸 선언해야하는지 생략할수있는지의 차이이다.