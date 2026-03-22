# ***CLASS***

자바에서 `Class` 클래스는 클래스의 정보 ( 메타데이터 ) 를 다루는데 사용된다. `Class` 클래스를 통해
개발자는 실행 중인 자바 앱 내에서 필요한 클래스 속성과 메서드에 대한 정보를 조회하고 조작할 수 있다.
  
`Class` 클래스의 주요 기능은 다음과 같다.
- 타입 정보 얻기: 클래스의 이름, 슈퍼클래스, 인터페이스, 접근 제한자 등과 같은 정보를 조회할 수 있다.
- 리플렉션: 클래스에 정의된 메서드, 필드, 생성자 등을 조회하고 이들을 통해 객체 인스턴스를 생성하거나 메서드를 호출하는 등의 작업이 가능하다.
- 동적 로딩과 생성: `Class.forName()` 메서드를 사용해 클래스를 동적으로 로드하고 `newInstance()` 메서드를 통해 새로운 인스턴스를 만들 수 있다.
- 애노테이션: 클래스에 적용된 애노테이션을 조회하고 처리하는 기능을 제공한다.

예를 들어 `String.class`는 `String` 클래스에 대한 `Class` 객체를 나타내며,
이를 통해 `String` 클래스에 대한 메타데이터를 조회하거나 조작할 수 있다.

```java
public class ClassMetaMain {
    public static void main(String[] args) throws Exception {
        Class clazz = String.class; // 1. 클래스에서 조회
        //Class clazz = new String().getClass(); // 2. 인스턴스에서 조회
        //Class clazz = Class.forName("java.lang.String"); // 3. 문자열로 조회
        
        Field[] fields = clazz.getDeclaredField();
        for (Field field : fields) {
            System.out.println("Field: " + field.getType() + " " + geild.getName());
        }
        
        Method[] methods = clazz.getDeclaredMethods();
        for (Method method : methods) {
            System.out.println("Method: " + method);
        }

        System.out.println("Superclass: " + clazz.getSuperclass().getName());
        
        Class[] interfaces = clazz.getInterfaces();
        for (Class i : interfaces) {
            System.out.println("Interface: " + i.getName());
        }
    }
}
```
**class vs clazz - class 는 자바의 예약어이기 때문에 패키지, 변수명으로 사용할 수 없다.**
**`main()` 옆에 `throws Exception`이 추가된 부분이 없으면 컴파일에러가 나니 주의**
  
**Class 클래스의 주요 기능**
- getDeclaredFields(): 클래스의 모든 필드를 조회한다.
- getDeclaredMethods(): 클래스의 모든 메서드를 조회한다.
- getSuperclass(): 클래스의 부모 클래스를 조회한다.
- getInterfaces(): 클래스의 인터페이스들을 조회한다.

## Class 생성하기
`Class` 클래스에는 클래스의 모든 정보가 들어있다.
```java
public class Hello {
    public String hello() {
        return "hello!";
    }
}

public class ClassCreateMain {
    public static void main(String[] args) throws Exception {
        Class helloClass = Class.forName("lang.clazz.Hello");
        Hello hello = (Hello);
HelloClass.getDeclaredConstructor().newInstance();
        String result = hello.hello();
        System.out.println("result = " + result);
    }
}
```
**getDeclaredConstructor().newInstance()**
- `getDeclaredConstructor()`: 생성자를 선택한다.
- `newInstance()`: 생성된 생성자를 기반으로 인스턴스를 생성한다.

**리플렉션 - reflection**
`Class`를 사용하면 클래스의 메타 정보를 기반으로 클래스에 정의된 메서드, 필드, 생성자 등을 조회하고, 이들을 통해
객체 인스턴스를 생성하거나 메서드를 호출하는 작업을 할 수 있다. 이런 작업을 리플렉션이라고 한다.  
추가로 애노테이션 정보를 읽어 특별한 기능을 수행할 수도 있다. 최신 프레임워크들은 이런 기능을 적극 활용한다.  
이 시점에는 `Class`가 뭔지, 그리고 대략 어떤 기능을 제공하는지만 학습하자. 지금은 리플렉션보다 더 중요한 기본기를 배워야한다.
  
## System 클래스
`System` 클래스는 시스템과 관련된 기본 기능들을 제공한다.
```java
public class SystemMain {
    public static void main(String[] args) {
        //현재 시간(밀리초)을 가져온다.
        long currentTimeMillies = System.currentTimeMillis();
        System.out.println("currentTimeMillies = " + currentTimeMillies);
        
        //현재 시간(나노초)을 가져온다.
        long currentTimeNano = System.nanoTime();
        System.out.println("currentTimeNano = " + currentTimeNano);
        
        //환경 변수를 읽는다.
        System.out.println("getenv = " + System.getenv());
        
        //시스템 속성을 읽는다.
        System.out.println("properties = " + System.getProperties());
        System.out.println("Java version: " + System.getProperty("java.version"));
        
        //배열을 고속으로 복사한다.
        char[] originalArray = new char[]{'h', 'e', 'l', 'l', 'o'};
        char[] copiedArray = new char[5];
        System.arraycopy((originalArray, 0, copiedArray, 0, originalArray.length));
        
        //배열 출력
        System.out.println("copiedArray = " + copiedArray);
        System.out.println("Arrays.toString = " + Arrays.toString(copiedArray));
        
        //프로그램 종료
        System.exit(0);
    }
}
```
- 표준 입력, 출력, 오류 스트림: `System.in`, `System.out`, `System.err`은 각각 표준 입력, 표준 출력, 표준 오류 스트림을 나타낸다.
- 시간 측정: `System.currentTimeMillis()` 는 현재 시간을 밀리초 또는 나노초 단위로 제공한다.
  - 참고 `System.nanoTime()`은 정확한 현재 시간이 아닌 JVM이나 운영체제에 의해 정해진 임의의 시작점을 기준으로 한다.
  따라서 두 시간 지점의 경과 시간을 측정할 때만 사용해야 한다.
- 환경변수: System.getenv() 메서드를 사용하여 OS 에서 설정한 환경변수의 값을 얻을 수 있다.
- 시스템 속성: `System.getProperties()`를 사용해 현재 시스템 속성을 얻거나 `System.getProperty(String key)`로
특정 속성을 얻을 수 있다. 시스템 속성은 자바에서 사용하는 설정 값이다.
- 시스템 종료: `System.exit(int status)` 메서드는 프로그램을 종료하고, OS에 프로그램 종료의 상태 코드를 전달한다.
  - 상태코드 0: 정상종료
  - 상태코드 != 0: 오류나 예외적 종료
- 배열 고속 복사: `System.arraycopy`는 시스템 레벨에서 최적화된 메모리 복사 연산을 사용한다.
반복문을 통한 복사보다 수 배 이상 빠른 성능을 제공한다.

## **Math, Random 클래스**
**Math 클래스**
1. 기본 연산
   - abs(x): 절대값
   - max(a, b): 최대값
   - min(a, b): 최소값
2. 지수 및 로그 연산 메서드
   - exp(x): e^x 연산
   - log(x): 자연 로그
   - log10(x): 로그 10
   - pow(a, b): a의 b 제곱
3. 반올림 및 정밀도
    - ceil(x): 올림
    - floor(x): 내림
    - rint(x): 가장 가까운 정수로 반올림
    - round(x): 반올림
4. 기타 유용한 메서드
   - sqrt(x): 제곱근
   - cbrt(x): 세제곱근
   - random(): 0.0과 1.0 사이의 무작위 값 생성
> 추후 아주 정밀한 숫자와 반올림 계산이 필요하다면 `BigDecimal`을 검색해보자.