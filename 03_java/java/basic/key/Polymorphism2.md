# 다형성의 활용

## 활용1
우선 다형성을 사용하지 않고 개발한 프로그램을 보자.
```java
public class Dog {
    public void sound() {
        System.out.println("멍멍");
    }
}

public class Cat {
    public void sound() {
        System.out.println("야옹");
    }
}

public class Cow () {
    public void sound() {
        System.out.println("음메");
    }
}
```

```java
import javax.xml.catalog.Catalog;
import java.awt.datatransfer.ClipboardOwner;

public class AnimalSoundMain {
    public static void main() {
        Dog dog = new Dog();
        Cat cat = new Cat();
        Cow cow = new Cow();

        System.out.println("동물 소리 테스트 시작");
        dog.sound();
        System.out.println("동물 소리 테스트 종료");

        System.out.println("동물 소리 테스트 시작");
        cat.sound();
        System.out.println("동물 소리 테스트 종료");

        System.out.println("동물 소리 테스트 시작");
        cow.sound();
        System.out.println("동물 소리 테스트 종료");
    }
}
```
동물 소리를 내는 코드인데 한 눈에 보기에도 중복이 많다. 게다가 새로운 동물을 추가하려면 클래스를 만들고 메인 파일도 수정해야한다.
  
그럼 다른 방법을 사용해서 중복을 제거할 수는 없을까?
  
1. 메서드
```java
private static void soundCow(Cow cow) {
    System.out.println("동물 소리 테스트 시작");
    cow.sound();
    System.out.println("동물 소리 테스트 종료");
}
```
그런데 dog 와 cat 을 사용하려고 보니까 매개변수의 타입이 Cow이다. 메서드는 불가능하다.

2. 배열과 for 문
```java
Cow[] cowArr = {dog, cat, cow}; // 컴파일 에러
```
벼열 또한 Cow 타입의 배열을 생성하는 거라 다른 타입의 변수를 담지 못한다. 배열도 불가능하다.
  
방법이 없다. 동물이 추가될 때마다 중복 코드를 작성해야한다.
  
그럼 타입을 통일하면 어떨까?

---

## 활용2
```java
public class Animal {
    public void sound() {
        System.out.println("동물 울음 소리");
    }
}

public class Dog extends Animal {
    @Override
    public void sound() {
        System.out.println("멍멍");
    }
}
```
이렇게 상위 클래스 하나로 묶어버린다. 그럼 상위 클래스의 메서드를 오버리이딩 하면 각자 다 다른 메서드를 사용할 수 있다.
 타입이 같으니까 배열에도 넣을 수 있다.
  
다형성과 오버라이딩 덕분에 엄청난 중복 코드를 없앨 수 있었다.

```java
// 배열을 사용한 방법
public class AnimalPilyMain2 {

    static void main() {
        Dog dog = new Dog();
        Cat cat = new Cat();
        Cow cow = new Cow();
        Animal[] animalArr = {dog, cat, cow};

        for (Animal animal : animalArr) {
            System.out.println("동물 소리 테스트 시작");
            cow.sound();
            System.out.println("동물 소리 테스트 종료");
        }
    }
}
```
성공 !

```java
// 배열과 메서드 모두 활용해 조금 더 개선

public class AnimalPolyMain2 {
    static void main() {
        Animal[] animalArr = {new Dog(), new Cat(), new Cow()};
        for (Animal animal : animalArr) {
            soundAnimal(animal);
        }
    }
    
    private static void soundAnimal(Animal aniamal) {
        System.out.println("동물 소리 테스트 시작");
        animal.sound();
        System.out.println("동물 소리 테스트 종료");
    }
}
```
완성 !
  
지금까지 다형성과 오버라이딩을 이용해 코드를 개선했는데 아직 남은 문제가 있다.
1. Animal 클래스의 인스턴스가 생성 가능하다.
2. Animal 클래스를 상속받는 클래스가 sound() 메서드를 오버라이딩 하지 않을 수 있다.
  
해당 프로그램을 개발한 사람 말고 다른 사람이 보면 Animal 클래스의 인스턴스를 생성할 수도 있다.  
제대로된 기능 없는 객체가 되는 것이고 이는 착오를 일으킬 수 있다.
  
자식 클래스가 sound() 메서드를 오버라이딩 하지 않으면?  
개발자가 동물을 추가하고 오버라이딩을 잊을 수도 있다. 이러면 하위 클래스의 메서드가 아닌 상위 클래스의 메서드가
호출 될 것이고 이는 서비스 장애로 이어질 수 있다.
  
**좋은 프로그램은 적당한 제약이 있는 프로그램이다.**  
추상 클래스와 추상 메서드를 사용하면 이 문제를 해결할 수 있다.

## 추상 클래스 1
**추상 클래스**  
Animal 클래스와 같이 하위 클래스를 묶는 기능은 하지만 실제 인스턴스를 생성할 수는 없는 클래스를 추상 클래스라고 한다.
  
오직 상속을 목적으로만 생성되는 클래스이다.
```java
abstract class AbstractAnimal {}
```
앞에 `abstract` 키워드를 입력하면 된다.
  
**추상 메서드**  
클래스를 받는 자식 클래스가 반드시 오버리이딩 해야하는 메서드를 부모 클래스에 정의할 수 있따. 이를 추상 메서드라고 하며
만드는 방법은 클래스와 똑같이 메서드 앞에 abstract 키워드를 붙여주면 된다.
  
- **추상 메서드가 하나라도 있는 클래스는 추상 클래스로 선언해야 한다.**
  - 그렇지 않으면 컴파일 오류가 발생한다,
  - 추상 메서드는 메서드 바디가 없다. 오버라이딩 하지 않으면 불완전한 메서드를 갖는 불완전한 클래스로 볼 수 있다.
- **추상 메서드는 상속 받는 자식 클래스가 반드시 오버라이딩 해야 한다.**
  - 똑같이 컴파일 오류가 발생한다.
  - 추상 메서드는 바디가 없기 때문에 반드시 오버라이딩을 해야한다.
  - 오버라이딩 하지 않으면 자식 클래스도 추상 클래스가 되어야한다.
  
- 추가로 추상 메서드밖에 갖고 있지 않은 추상 클래스는 `순수 추상 클래스` 라고한다.

---

## 인터페이스
자바는 순수 추상 클래스를 더 편리하게 사용할 수 있는 인터페이스 기능을 제공한다.
```java
// 순수 추상
public abstract class AbstractAnimal {
    public abstract void sound();
    public abstract void move();
}

public interface InterfaceAnimal {
    public abstract void sound();
    public abstract void move();
}

public interface InterfaceAnimal {
    void sound();
    void move();
}
```
위 세 클래스는 모두 다 같은 클래스이다. 순수 추상클래스는 interface 키워드로 바꿀 수 있고
`public abstract` 또한 생략 가능하다. ( 생략 권장 )
  
인터페이스가 갖는 큰 특징 중 하나가 **다중상속 지원**이다.  
인터페이스는 이름이 같은 메서드가 있더라도 메서드 자체의 기능이 없기 떄문에 에러 발생의 위험이 없다.
그래서 다중 상속이 지원된다.
  
또한 인터페이스에서 멤버 변수는 상수이다.  
`public`, `static`, `final` 이 모두 포함 되었다고 간주된다. ( 생략 권장 )

---

## 클래스, 추상 클래스, 인터페이스 는 모두 같다.
- 이 세가지는 프로그램 코드, 메모리 구조상 모두 같다. 파일명도 자바에서는 모두 `.class` 로 다룬다.
- 각각 조금씩의 제약이 추가된 것이라고 보면 된다.
  
**상속 vs 구현**
클래스는 부모 클래스의 자식 클래스를 상속 받는다고 표현하지만 인터페이스의 기능이 상속될 때는
자식 클래스가 인터페이스를 구현한다고 표현한다. ( 자연어만 다르고 다 똑같다. )

---

## 다중 상속, 추상 클래스 | 인터페이스 동시 사용 예제

```java
public abstract class Animal {
    public abstract void sound();

    public void move() {
        System.out.println("동물이 이동합니다.");
    }
}

public interface Fly {
    void fly();
}

public class Dog extends Animal {
    @Override
    public void sound() {
        System.out.println("멍멍");
    }
}

public class Bird extends Animal implements Fly {
    @Override
    public void sound() {
        System.out.println("쨱쨱");
    }

    @Override
    public void fly() {
        System.out.println("새 날기");
    }
}


// 메인
public class SOundFlyMain {
    static void main() {
        Dog dog = new Dog();
        Bird bird = new Bird();
        
        soundAnimal(dog);
        soundAnimal(bord);
        
        flyAnimal(bird);
    }

    private static void soundAnimal(Animal animal) {
        System.out.println("동물 소리 테스트 시작");
        animal.sound();
        System.out.println("동물 소리 테스트 종료");
    }
    
    private static void flyAnimal(Fly fly) {
        System.out.println("날기 테스트 시작");
        fly.fly();
        System.out.println("날기 테스트 종료");
    }
}
```
추가로 `Bird` 클래스와 같이 상속과 구현을 동시에 할 경우 `extends`가 앞, `implements`가 뒤에 온다.