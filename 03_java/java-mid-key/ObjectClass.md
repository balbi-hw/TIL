# ***Object Class***

## Java.lang 패키지
자바에서 기본적으로 제공하는 라이브러리 중 가장 기본이 되는 것이 java.lang 패키지이다.  
여기서 lang 은 Language 의 줄임말로 간단히 자바 언어를 이루는 가장 기본이 되는 클래스를 보관하는 패키지를 말한다.
  
*java.lang 패키지의 대표적인 클래스들*
- Object: 모든 자바 객체의 부모 클래스
- String: 문자열
- Integer, Long, Double: 래퍼 타입, 기본형 데이터 타입을 객체로 만든 것
- Class: 클래스 메타 정보
- System: 시스템과 관련된 기본 기능을 제공  
여기 나열한 클래스들은 자바 언어의 기본을 이루는 클래스들이다.
  
*import 생략 가능*
java.lang 패키지는 모든 자바 애플리케이션에 자동으로 `import` 된다. 따로 임포트 하지 않아도 된다.

## Object Class
자바에서 모든 클래스의 최상의 부모 클래스는 항상 Object 클래스이다.
```java
public class Parent {
    
    public void parentMethod() {
        System.out.println("Parent.parentMethod");
    }
}

public class Parent extends Object {
    
    public void parentMethod() {
        System.out.println("Parent.parentMethod");
    }
}
```
위 두 클래스는 같은 클래스로 상속받을 부모 클래스가 없으면 묵시적으로 Object 클래스를 상속받는다.
- 간단히 이야기해서 부모 클래스가 명시되지 않은 모든 클래스는 `extends Object` 코드를 넣어준다.

> 묵시적: 개발자가 코드에 기술하지 앙ㄶ아도 시스템 또는 컴파일러에 의해 자동으로 수행되는 것을 의미
> 명시적: 개발자가 코드에 직접 기술해서 작동하는 것을 의미
  
- 자바에서 모든 객체의 최종 부모는 Object 이다.  
최상위 클래스가 Object 클래스를 상속받기 때문에 모든 객체의 메모리에는 항상 Object 클래스의 정보가 있다.

## 자바에서 Object 클래스가 최상위 부모 클래스가 되는 이유
모든 클래스가 Object 클래스를 상속 받는 이유는 다음과 같다.
- 공통 기능 제공
- 다형성의 기본 구현
  
*공통 기능 제공*
객체의 정보를 제공하고 ( .toString() ), 이 객체가 다른 객체와 같은지 비교하고 ( .equals() ), 객체가 어떤 클래스롷 만들어졌는지 확인하는 기능 ( getClass() )
은 모든 객체에게 필요한 기본 기능인데 이런 기능을 객체를 만들 때마다 항상 새로운 메서드를 정의해서 만들어야 한다면 상당히 번거로울 것이다.  
그런데 힘들게 만들어 놨더니 개발자마다 다른 이름의 `Object` 클래스를 사용한다면 일관성이 없을 것이다.  
그래서 자바에서 모든 객체에 필요한 공통 기능을 `Object` 클래스를 통해 제공한다. 최상위 부모 클래스이기 때문에 모든 객체는 이 기능들을 편리하게 상속 받을 수 있다.
  
*Object 가 제공하는 기능*  
- 객체의 정보를 제공하는 toString()
- 객체의 같음을 비교하는 equals()
- 객체의 클래스 정보를 제공하는 getClass()
- 기타 여러가지 기능
  

## Object 다형성
Object는 모든 클래스의 부모 클래스이기 때문에 Object 는 모든 객체를 참조할 수 있다.

```java
class Car {
    public void move() {
        System.out.println("자동차 이름");
    }
}

class Dog {
    public void sound() {
        System.out.println("멍멍");
    }
}

public class ObjectPolyExample1 {

    static void main() {
        Dog dog = new Dog();
        Car car = new Car();

        
    }
    
    private static void action(Object obj) {
//        obj.sound(); //컴파일 오류, Object는 sound() 가 없다.
        //onj.move(); // 컴파일 오류, Object는 move() 도 없다.
        
        // 다운 캐스팅 필요
        if (onj instanceof Dog dog) {
            dog.sound();
        } else if (obj instanceof Car car){
            car.move();
        }
    }
}
```
Object는 모든 타입의 부모이기 때문에 다운캐스팅이 가능하고 또 앞의 다운 캐스팅 코드를 다음과 같이 쓸 수도 있다.
```java
Object dog = new Dog(); // Dog -> Object
Object car = new Car(); // Dog -> Object
```

