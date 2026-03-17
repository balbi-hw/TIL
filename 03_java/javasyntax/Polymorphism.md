# ***Polymorphism***

OOP의 대표적 특징은 ( 캡슐화, 상속, 다형성 ) 이 있는데 그 중 다형성은 OOP의 꽃이라고 불리는 특징이다.  
  
### 들어가기 전에..  
다형성을 이해하기 위해 필요한 개념은 다음과 같다.
1. 다형적 참조
2. 메서드 오버라이딩

---

### 다형적 참조

1. 다형적 참조
코드를 먼저 보자
```java
public class Parent {
    
    public void parentMethod() {
        System.out.println("Parent.parentMethod");
    }
}
```
```java
public class Child extends Parent {
    
    public void childMethod() {
        System.out.println("Child.childMethod");
    }
}
```
```java
public class PolyMain {
    static void main() {
        // 부모 변수가 부모 인스턴스 참조
        System.out.println("Parent -> Parent");
        Parent parent = new Parent();
        parent.parentMethod();
    
        //자식 변수가 자식 인스턴스
        System.out.println("Child -> Child");
        Child child = new Child();
        child.childMethod();
    
        //부모 변수가 자식 인스턴스 참조 ( 다형적 참조 )
        System.out.println("Parent -> Child");
        Parent poly = new Child();
        poly.parentMethod();
        
        //Child child1 = new Parent(); 자식은 부모를 담을 수 없다.
        // 부모 > 자식 만 가능하고 자식 > 부모는 안된다.
//        poly.childMethod(); 불가능
    }
}
```
    1. 부모 타입 변수는 부모 인스턴스를 참조할 수 있다.
    2. 자식 타입 변수도 자식 인스턴스를 참조할 수 있다.
    3. 부모 타입의 변수가 자식 인스턴스를 참조할 수 있다.
        - 변수의 자식 인스턴스 참조값이 있어야한다.  
            ( Parent parent = new Child(); )
    4. 자식 타입의 변수는 부모 인스턴스를 참조할 수 없다.
            ( Child child = new Parent(); ) 불가능  

상속이 되어있는 자식 인스턴스를 생성하면 그 참조 메모리 안에는 부모 객체도 같이 생성된다.  

오버라이딩이 되어 있을 수 있으니 그냥 다 같이 생성하는 것으로 이해헀다. ( 아니어도 그냥 같이 생성된다. )  

부모 타입의 변수는 직계 자식은 물론이고 자식의 자식 타입까지 참조할 수 있다.  

하지만 부모 타입의 변수도 자식 타임의 메서드를 호출하지는 못한다.

```java
Parent poly = new Child();
//poly.childMethod(); 불가능
```
---
2. 다형성과 캐스팅

바로 위의 코드에서는 `Parent` 타입인 `poly`에 `Child` 객체 주소를 초기화했다.
그래서 Child의 메서드는 사용하지 못한다. 그럼 사용하려면 어떻게 해야할까?  

강제로 형변환 ( 다운캐스팅 ) 을 해주어야한다.  

`Child child = (Child) poly // Parent poly` 이후 `child.childMethod()` 를 실행하면
정상적으로 자식 메서드를 실행할 수 있다.
  
---

3. 캐스팅의 종류  

자식 타임의 기능을 사용하려면 아래와 같이 다운캐스팅 결과를 담아두고 이후 사용하면 된다.
```java
Child child = (Child) poly;
child.childMethod();
```
조금 번거롭지만 할 수는 있다. 그런데 이 번거로움 없이 바로 할 수도 있다.
```java
((Child) poly).childMethod();
```

- 업캐스팅  
다운 캐스팅과 반대로 현재 타입을 부모 타입으로 변경하는 것을 업캐스팅이라고 한다.  
`Parent parent2 = child // Parent parent2 = new Child()`  
그런데 이 업캐스팅은 생력이 가능하다. 매우 사용하는 기능이기 때문에 오히려 생략을 권장한다.  
하지만 다운캐스팅이 생략이 불가하다.
  

- 다운캐스팅과 주의점  
다운캐스팅은 잘못하면 런타임 에러가 발생할 수 있다.
```java
public class CastingMain4 {
    static void main() {
        Parent parent1 = new Child();
        Child child1 = (Child) parent1;
        child.childMethod();
        
        Parent parent2 = new Parent();
        Child child2 = (Child) parent2; // 오류 발생 - ClassCastExeption
        child2.childMethod();
    }
}
```
위의 블럭에서는 Child 인스턴스를 받아왔기 때문에 Child와 Parent 객체 둘 다 메모리에 들어있지만
아래 블럭에서는 Parent 인스턴스를 받아와서 메모리에 Parent 객체만 존재한다.
  
이렇게 업캐스팅은 절대 오류가 발생하지 않는데 비해 다운캐스팅은 조금 잘못하면 바로 런타임 에러가 발생하기 때문에
심각한 문제가 될 수 있어 주의해야한다.
  
컴파일 오류는 실행이 안되기에 사고를 방지할 수 있지만 런타임 오류는 실행이 되다가 해당 부분에 접근을 시도하면
에러가 발생하기 때문에 시스템 운영 중 클라이언트가 서비스를 사용할 때 에러가 난다면 큰 문제가 될 가능성이 있는 것이다.
  
---

4. instanceof
  
이 문제를 해결하려면 해당 변수가 어떤 인스턴스를 참조하고 있는지 확인해야하는데 이를 위한 문법이
instanceof 문법이다.
```java
parent instanceof Child; // parent 는 Parent의 인스턴스
new Parent() instanceof Child; // Child의 인스턴스 ?? -> false
```
오른쪽 대상의 자식 타입을 왼쪽에서 참조하는 경우에도 true를 반환한다.
```java
parent instanceof Parent // parent 는 Child의 인스턴스

new Parent() instanceof Parent; // parent가 Parent의 인스턴스를 참조 ?? == true
new Child() instanceof Parent;  // parent가 Child의 인스턴스를 참조 ?? == true
```

---

### 메서드 오버라이딩

오버라이딩 설명에 앞서 꼭 기억해야할 점은 **오버라이딩 된 메서드가 항상 우선권을 가진다**는 점이다.

- `Parent`, `Child` 모두 `value` 라는 같은 멤버 변수를 가지고 있다.
  - 멤버 변수는 오버라이딩 되지 않는다.
- `Parent`, `Child` 모두 `method()` 라는 같은 메서드를 가지고 있다. `Child`에서 메서드를 오버라이딩 했다.
  - 메서드는 오버라이딩 가능하다.

![메서드 오버라이딩](/properties/OverridingCapture.png)

- 위에서 `poly` 변수는 `Parent`타입이다. 따라서 `poly.value`, `poly.method()`를 호출하면 인스턴스의
`Parent` 타입에서 기능을 찾아 실행한다.
  - `poly.value`: `Parent` 타입의 value 값을 읽는다.
  - `poly.method()`가 오버라이딩 되어있다. **오버라이딩 된 메서드는 항상 우선권을 갖는다.**
    따라서 `Parent.method`가 아닌 `Child.method` 가 실행된다.

