# ***Nested Class***

## 중첩클래스와 내부클래스 ?
이중 `for`문 처럼 클래스도 중첩할 수 있는데 이를 `중첩 클래스` 라고 한다.
```java
class Outer {
    class Nested {
    }
}
```
이 중첩 클래스는 클래스의 위치에 따라 다음과 같이 구분한다.  
![중첩클래스](/properties/NestedClass.png)
**중첩 클래스는 총 4가지가 있고 크게 2가지로 분류할 수 있다**
- 정적 중첩 클래스, static nested class
- 내부 클래스, non-static
  - 내부 클래스, inner class
  - 지역 클래스, local class
  - 익명 클래스, anonymous class
  
중첩 클래스의 위치 개념은 변수의 위치 개념과 같다.
- 변수
  - 정적 변수 ( 클래스 변수 )
  - 인스턴스 변수
  - 지역 변수
- 중첩 클래스
  - 정적 중첩 클래스 > 정적 변수
  - 내부 클래스 > 인스턴스 변수
  - 지역 클래스 > 지역 변수

```java
class Outer {
    // 정적 중첩
    static class StaticNested {
        
    }
    
    // 내부
    class Inner {
        
    }
}
```
- 정적 중첩 클래스는 정적 변수와 같이 `static`을 붙인다
- 내부 클래스는 붙이지 않는다.

```java
class Outer {

    public void process() {
        int localVar = 0;

        class Local {
        }

        Local local = new Local();
    }
}
```
- 지역 클래스는 지역 변수같이 코드 블럭 안에서 클래스를 정의한다.
  
" 익명 클래스는 아래에서 설명한다. "
  
**중첩과 내부는 무슨 차이가 있을까?**  
정적 중첩 클래스는 바깥 클래스의 안에 있지만 바깥 클래스와 전혀 관계가 없는 클래스이다.  
내부 클래스는 바깥 클래스의 안에 있으면서 바깥 클래스를 구성하는 요소를 말한다.  
- 정적 중첩 클래스는 바깥 클래스와 전혀 다른 클래스이고 바깥 클래스의 인스턴스에 소속되지 않는다.
- 내부 클래스는 바깥 클래스를 구성하는 요소이므로 바깥 클래스의 인스턴스에 소속된다.
  
**내부 클래스는 바깥 클래스의 인스턴스에 소속되지만 정적 중첩은 그렇지 않다.**
  
**중첩 클래스를 사용하는 경우**
- 모든 중첩 클래스는 특정 클래스가 다른 하나의 클래스 안에서만 사용되거나 둘이 깊은 연관이 있을 때만 사용해야한다.
외부에서 사용하는 경우가 있다면 중첩해선 안된다.
  
**사용하는 이유**
- 논리적 그룹화: 특정 클래스가 다른 하나의 클래스 안에서만 사용되는 경우 해당 클래스 안에 포함하는 것이
논리 적으로 더 그룹화 된다. 패키지 안에서 다른 곳에서 사용될 필요가 없는 중첩 클래스가 외부에 노출되지 않는 장점도 있다.
- 캡슐화: 중첩 클래스는 바깥 클래스의 `private` 멤버에 접근 할 수 있다. 이렇게 해서 둘을 연결하고 불필요한
`public` 메서드를 제거할 수 있다.

## 정적 중첩 클래스, Static Nested Class

```java
public class NestedOuter {
    private static int outClassValue = 3;
    private int outInstanceValue = 2;
    
    static class Nested {
        private int nestedInstanceVale = 1;
        
        public void print() {
            
            // 자신 멤버
            System.out.println(nestedInstanceVale);
            
//            Outer의 인스턴스 멤버는 접근 불가 / Outer 인스턴스 소속이 아님
//            System.out.println(outInstanceValue);

            // Outer 의 클래스 멤버는 접근 가능, private 도 가능하다.
            System.out.println(NestedOuter.outClassValue);
        }
    }
}
```
- 정적 중첩 클래스는 앞에 static 이 붙는다.
- 정적 중첩 클래스는
  - 자신의 멤버 접근 가능
  - Outer 인스턴스는 접근 불가
  - Outer 클래스 필드는 접근 가능

> `static` 이 붙어있으니까 static 변수는 접근 가능하구나. static 변수와 같은 위치에 있다는게 무슨 말인지 알겠다.
> 메서드, 스택, 힙 중 메서드 영역에 존재한다는 뜻이구나. 그러니까 힙에 들어있는 인스턴스는 접근이 안되는거고
> 메서드 영역의 Outer 클래스 안에 있으니까 Outer 의 private 도 접근이 가능하다.

```java
public class NestedOuterMain {
    
    public static void main(String[] args) {
        NestedOuter outer = new NestedOuter();
        NestedOuter.Nested nested = new NestedOuter.Nested();
        nested.print();

        System.out.println("nestedClass = " + nested.getClass());
    }
}
//실행 결과
//1
//3
//nestedClass = class NestedOuter$Nested
```
- 정적 중첩 클래스는 `new Outer.Nested()` 로 생성 가능하다.
  - Outer 클래스의 안에 있으니까 Outer의 참조값이 필요하다.
- 중첩 클래스는 NestedOuter.Nested 같이  Outer.Nested 로 접근 가능하다.
  - 이것도 참조값이 필요하기 때문
- 이 때 Outer 의 인스턴스와 Nested 의 인스턴스는 아무 연관이 없다. 클래스 구조상 중첩되어있을 뿐
  - 정적 중첩 클래스의 인스턴스만 따로 생성할 수 있다.
  
## 정적 중첩 활용
리팩토링 전

```java
public class NetworkMessage {
    private String content;

    public NetworkMessage(String content) {
        tihs.content = content;
    }

    public void print() {
        System.out.println(content);
    }
}

public class Network {

    public void sendMessage(String text) {
        NetworkMessage networkMessage = new NetworkMessage();
        networkMessage.print();
    }
}

public class NetworkMain {

    public static void main(String[] args) {
        Network network = new Network();
        network.sendMessage("hello java");
    }
}
```
- `NetworkMessage` 는 `Network` 객체 안에서만 사용되는 객체이다.
- Network 의 `sendMessage`는 text를 입력 받아 `NetworkMessage` 객체를 생성하고 출력하는 기능을 제공한다.
  
이렇게 `NetworkMessage` 클래스는 `Network` 클래스 안에서만 사용된다.  
클래스가 두 개이니 이 코드를 처음 보는 사람은 이걸 이해하는 데 시간이 걸릴 것이다.  
그래서 가독성을 높이기 위해 하나로 합친다.  
**리팩토링 후**

```java
public class Network {

    public void sendMessage(String text) {
        NetworkMessage networkMessage = new NetworkMessage();
        networkMessage.print();
    }

    private static class NetworkMessage {
        private String content;

        public NetworkMessage(String content) {
            this.content = content;
        }

        public void print() {
            System.out.println(content);
        }
    }
}

//메인
public class NetworkMain {

    public static void main(String[] args) {
        Network network = new Network();
        network.sendMessage("hello java");
    }
}
```
`NetworkMessage` 클래스를 `Network` 클래스 안에 중첩해서 만들었다.  
또한 private 을 붙였기 때문에 외부에서 접근이 불가능하다.  ( 외부에서 접근하는 경우가 있다면 따로 빼는 게 더 좋다. )
그럼 이 `NetworkMessage` 클래스는 `Network` 클래스만 사용할 수 있는 클래스이고 이게 명확해진다.
  
## 내부 클래스, Inner Class

정적 중첩 클래스는 Outer 와 관계가 없다. 하지만 Inner 는 Outer 의 인스턴스 필드 중 하나가 된다.
```java
public class InnerOuter {
    private static int outClassValue = 3;
    private int outInstanceValue = 2;
    
    class Inner {
        private int innerInstanceValue = 1;
        
        public void print() {
            System.out.println(innerInstanceValue);

            // 외부 클래스 인스턴스, 클래스 멤버 접근 가능, private 도 가능
            System.out.println(outInstanceValue);
            System.out.println(InnerOuter.outClassValue);
        }
    }
}

public class InnerOuterMain {
    
    public static void main(String[] args) {
        InnerOuter outer = new InnerOuter();
        InnerOuter.Inner inner = outer.new Inner();
        inner.print();

        System.out.println("innerClass = " + inner.getClass());
    }
}
```
- Inner 는 앞에 static 이 붙지 않는다.
- Inner 는
  - 자신의 멤버 접근 가능
  - Outer 의 인스턴스 멤버 접근 가능
  - Outer 의 클래스 멤버 접근 가능
  
내부 클래스는 바깥 클래스의 인스턴스에 소속된다. 따라서 바깥 클래스의 인스턴스 참조값이 있어야 만들 수 있다.
- `OuterHash.new Inner()` 로 생성 가능하다.
개념 상 Inner의 객체는 Outer 의 객체 내부에 생성된다.
- 따라서 Outer 의 인스턴스를 먼저 만들어야 Inner 의 인스턴스를 만들 수 있다.
  
## 내부 클래스 활용
리팩토링 전
```java
//Car 에서만 사용하는 클래스
public class Engine {

    private Car car;

    public Engine(Car car) {
        this.car = car;
    }

    public void start() {
        System.out.println("충전 레벨 확인: " + car.getChargeLevel());
        System.out.println(car.getModel() + "의 엔진을 구동합니다.");
    }
}

public class Car {
    private String model;
    private int chargeLevel;
    private Engine engine;
    
    public Car(String model, int chargeLevel) {
        this.model = model;
        this.chargeLevel = chargeLevel;
        this.engine = new Engine(this);
    }
    
    //Engine 에서만 사용하는 메서드
    public String getModel() {
        return model;
    }

    //Engine 에서만 사용하는 메서드
    public int getChargeLevel() {
        return chargeLevel;
    }

    public void start() {
        engine.start();
        System.out.println(model + " 시작 완료");
    }
}

public class CarMain {
    
    public static void main(String[] args) {
        Car myCar = new Car("Model Y", 100);
        myCar.start();
    }
}
```
- 엔진은 Car 클래스에서만 사용된다.
- 엔진을 시작하기 위해서는 차의 충전 레벨과 차량의 이름이 필요하다.
  - Car 인스턴스의 참조를 생성자에서 보관한다.
  - 엔진은 충전 레벨을 확인하기 위해 Car.getChargeLevel 이 필요하다.
  - 엔진은 차량의 이름을 알기 위해 Car.getModel() 이 필요하다.
  
- Car 클래스는 엔진에 필요한 메서드를 제공해야해서 get 메서드를 만들었다.
  - Car 클래스는 자신이 사용할 클래스에 정보를 제공하기 위해 메서드를 만들어 필드를 외부에 노출한다.

리팩토링 후  
```java
public class Car {
    private String model;
    private int chargeLevel;
    private Engine engine;

    public Car(String model, int chargeLevel) {
        this.model = model;
        this.chargeLevel = chargeLevel;
        this.engine = new Engine();
    }

    public void start() {
        engine.start();
        System.out.println(model + " 시작 완료");
    }
    
    private class Engine {
        public void start() {
            System.out.println("충전 레벨 확인: " + chargeLevel);
            System.out.println(model + "의 엔진을 구동합니다.");
        }
    }
}
```
- 엔진을 내부 클래스로 만들었다.
- 엔진은 이제 Car 의 인스턴스 변수에 접근이 가능하고 덕분에 Car 는 추가 public 메서드를 만들지 않았다.