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

- **장점**
`action()` 메서드는 Object 타입의 매개변수를 사용한다. 모든 객체는 Object의 자식이기 때문에 어떤 객체든지 action 메서드를 사용할 수 있다.

- **한계**
`action()` 메서드 안에서 obj.sound()를 호출하면 오류가 발생한다. 매개변수인 Oject 타입은 sound() 메서드가 없기 때문이다.
  
그래서 action() 메서드의 인자로 넣은 dog 의 sound() 메서드를 사용하기 위해서는 `다운캐스팅`이 필요하다.
```java
if (obj instanceof Dog dog) {
    dog.sound()
}
```
- Object 는 모든 객체를 대상으로 다형적 참조를 할 수 있다.
- Object 를 통해 전달 받은 객체를 호출하려면 각 객체에 맞는 다운캐스팅 과정이 필요하다.
  - Object 본인이 보유한 toString() 같은 메서드는 당연히 자식 클래스에서 오버라이딩 할 수 있지만 Object에 정의되어 있지 않은 메서드는
  오버라이딩이 불가능하다. 결국 각 객체의 기능을 호출하려면 다운캐스팅을 해야한다.

## Object 배열
Object 는 모든 타입의 객체를 담을 수 있다. 따라서 Object[] 을 만들면 세상의 모든 객체를 담을 수 있는 배열을 만들 수 있다.

```java
public class ObjectPolyExample2 {

    public static void main(String[] args) {
        Dog dog = new Dog();
        Car car = new Car();
        Object object = new Object();
        
        Object[] objects = {dog, car, object};
        
        size(objects);
    }
    
    private static void size(Object[] objects) {
        System.out.println("전달된 객체의 수는: " + objects.length);
    }
}

// 실행 결과
// 전달된 객체의 수는: 3
```
Object 배열은 자바 내 모든 객체를 담을 수 있기 때문에 위의 size() 메서드는 전 세계 어디서든지 사용할 수 있다.

## toString()
Object.toString() 메서드는 객체의 정보를 문자열 형태로 제공한다. 그래서 디버깅과 로깅에 유용하게 사용된다.

```java
public class ToStringMain1 {

    static void main() {
        Object object = new Object();
        String string = object.toString();

        System.out.println(string);

        System.out.println(object);
    }
}
```
**Object.toString()**
```java
public String toString() {
    return getClass().getName() + "@" + Integer.toHexString(hashCode());
}
```
- Object 가 제공하는 toString() 메서드는 기본적으로 패키지를 포함한 객체의 이름과 객체의 참조값(해쉬 코드)를 16진수로 제공한다.
> 참고: 해시코드 (hashCode())에 대한 내용은 이후에 별도로 다룬다.

**println() 과 toString()**
toString() 과 object 를 println() 에 직접 출력한 코드의 결과가 같다.
  
System.out.println() 메서드는 사실 내부에서 toString() 을 호출한다.
  
- toString() 오버라이딩
Object.toString() 메서드가 클래스 정보와 참조값을 제공하지만 이 정보만으로는 (해시값) 객체의 필드를 나타내지 못한다. 그래서 보통 toString을
오버라이딩해서 보다 유용한 정보를 제공한다.

```java
public class Dog {
    private String dogName;
    private int age;

    public Dog(String dogName, int age) {
        this.dogName = dogName;
        this.age = age;
    }

    @Override
    public String toString() {
        return "Dog{" +
                "dogName='" + dogName + '\'' +
                ", age=" + age +
                '}';
    }
}

```
Dog 클래스틑 toString 메서드를 재정의했다. ( toString() 메서드는 IDE의 generate 기능을 이용하는게 좋다. )
  
그런데 이렇게 하면 객체의 정보는 나타내지만 나중에 해시값이 궁금할 때 곤란해질 수 있다.  
해시값을 얻기 위한 코드는 다음과 같다.
```java
String refValue = Integer.toHexString(System.identityHashCode(dog));
System.out.println("refValue = " + refValue);
```

## Object와 OCP
> 추상적: 상속관계에서 위로 올라가게 될 수록 개념이 추상적이라고 이야기한다. 예를들어 Animal과 Dog, Cat 의 관계가 있을 때 Animal 클래스는 Dog 와 Cat 보다
> 추상적이고 하위 두 클래스는 Animal 클래스보다 구체적이라고 한다.

```java
public class ObjectPrinter {
    public class void print(Object obj) {
        String string = "객체 정보 출력: " + obj.toString();
        System.out.println(string);
    }
}
```
이 ObjectPrinter 메서드는 구체적인 것이 아니라 추상적인 것에 의존한다.
  
이 메서드는 다형성을 매우 잘 활용하고 있다.
  
- 다형적 참조:
  print(Object obj), Object 타입을 매개변수로 사용해서 다형적 참조를 사용한다.
- 메서드 오버라이딩:
  Object 는 모든 클래스의 부모이기에 Object 클래스의 toString() 메서드를 하위 객체들이 오버라이딩 할 수 있다. 따라서 print(Object obj) 메서드는
Dog, Car 와 같은 구체적인 타입에 의존하지 않고 추상적인 Object 타입에 의존하면서 런타임에 각 인스턴스의 toString()을 호출할 수 있다.
  
**OCP 원칙**
- Open: 새로운 클래스를 추가하고 toString()을 오버라이딩해서 기능을 확장할 수 있다.
- Closed: 새로운 클래스를 추가해도 Object 와 toString() 을 사용하는 클라이언트 코드인 ObjectPrinter 는 변경하지 않아도 된다.
  
다형적 참조, 메서드 오버라이딩, 클라이언트 코드가 구체적인 Car, Dog 에 의존하는 것이 아니라 추상적인 Object에 의존하면서 OCP 원칙을 지킬 수 있었다.
덕분에 새로운 클래스를 추가하고 toString() 메서드를 새롭게 오버라이딩해서 기능을 확장할 수 있다. 그럼에도 ObjectPrinter 코드는 변경할 필요가 없다.
  
이 toString() 메서드는 상술했듯이 System.out.println() 안에서 호출되기 때문에 println() 또한 객체지향의 특징을 매우 잘 활용한다고 할 수 있다.
  
**자바는 객체지향 언어 답게 언어 스스로도 객체지향의 특징을 매우 잘 활용한다.**
  
### 참고 - 정적 의존관계 vs 동적 의존관계
- 정적 의존관계는 컴파일 시간을 결정하며 주로 클래스간의 관계를 의미한다. 앞서 보여준 클래스 의존관계 그림이 바로 정적 의존관계이다.
- 동적 의존관계는 프로그램을 실행하는 런타임을 결정하는 의존관계이다. 매개변수가 Object 클래스인 메서드는 어떤 객체가 인자로 들어갈 지는
프로그램을 실행해봐야 알 수 있다. 이렇게 런타임에 어떤 인스턴스를 사용하는지를 나타내는 것이 동적 의존관계이다.
- 단순히 의존관계 또는 어디에 의존한다고 하면 주로 정적 의존관계를 뜻한다.

## equals() - 1. 동일성과 동등성
Object 는 동등성 비교를 위한 equals() 메서드를 제공한다.
  
자바는 두 객체가 같다는 표현을 두 가지로 나눈다.
- 동일성 (Identity): == 연산자를 이용해 두 객체의 `참조값`이 동일한지 확인
- 동등성 (Equality): equals() 메서드를 사용해 두 객체가 논리적으로 동등한지 확인
  
동일성은 자바 기준이고 메모리의 참조가 기준이라 물리적이다. 반면에 동등성은 보통 사람이 생각하는 논리적인 기준에 맞추어 비교한다.
  
```java
User a = new User("id-100")
User b = new User("id-100")
```
이 경우 두 객체는 물리적으로 다른 객체지만 id 가 같으니 논리적으로 같은 회원으로 볼 수 있다.  
-> 동일성은 다르지만 동등성은 같다.
  
하지만 `a.equals(b)` 이렇게 동등성을 확인하면 `false` 가 출력된다.
  
이는 사실 equals() 메서드가 내부에서 `==` 연산자를 사용하기 때문이다. 그래서 동등성을 비교하고 싶다면 equals 메서드를 재정의해야한다.  
그런데 이 메서드를 오버라이딩 하는 건 매우 복잡한데 다행히 InellJ 에서 toString 과 같이 generate 기능을 제공한다.
  
