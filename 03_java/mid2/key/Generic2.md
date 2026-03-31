# ***GENERIC***

동물 병원을 만들어보자  

```java
public class DogHospital {
    
    private Dog animal;
    
    public void set(Dog animal) {
        this.animal = animal;
    }

    public void checkup() {
        System.out.println("동물 이름: " + animal.getName());
        System.out.println("동물 크기: " + animal.getSize());
        animal.sound();
    }

    public Dog bigger(Dog target) {
        return animal.getSize() > target.getSize() ? animal : target;
    }
}
```

```java
public class AnimalHospitalV2<T> {
    
    private T animal;

    public void set(T animal) {
        this.animal = animal;
    }

    public void checkup() {
        animal.toString();
        animal.equals(null);

        // 컴파일 오류
        //System.out.println("동물 이름: " + animal.getName());
        //animal.sound();
    }

    public T getBigger(T target) {
        // 컴파일 에러
//        return animal.getSize() > target.getSize() ? animal : target;
        return null;
    }
}
```
아래 코드는 제네럴로 `T`를 설정하고 우리는 `Animal`을 상속받은 `Dog`와 `Cat` 을 넣는다.  
그런데 왜 컴파일이 안될까!  
  
바로 타입 매개변수 T 에는 어떤 타입이든지 올 수 있기 때문이다.  
제네릭을 컴파일 할 때 컴파일러는 Object 로 바꿔서 컴파일을 하게 되는데 이 때 Object 는 Animal 의 메서드를 가지고 있지 않다.
  
따라서 그냥 T 만 띡 하고 쓴다고 만사형통이 아니다.  
그럼 어떡해야할까 ?  
  
`T` 의 상한값을 정해주면 된다.

```java
public class AnimalHospitalV3<T extends Animal> {
    
    private T animal;
}
```
이렇게 클래스를 선언하면 `T` 는 컴파일 시 `Object` 가 아니라 `Animal` 이 된다.  
그러면 T 의 최대값이 Animal 이니까 `T.AnimalMethod()` 가 가능해진다 !
  
**이렇게 제네릭을 사용해 타입 안전성 문제를 해결했고 제네릭에 타입 상한을 걸어줌으로서 더 편리하게 사용할 수 있게 하였다.**
  
## 제네릭 메서드
제네릭 메서드는 타입과 비슷하지만 서로 다른 기능을 제공한다.
  
```java
public class GenericMethod {

    public static Object objMethod(Object object) {
        System.out.println("object print = " + object);
        return object;
    }
    
    public static <T> T genericMethod(T t) {
        System.out.println("generic print = " + t);
        return t;
    }

    public static <T extends Number> T numberMethod(T t) {
        System.out.println("bound print = " + t);
        return t;
    }
}
```
이렇게 메서드를 선언하면 타입인자가 **메서드를 호출하는 시점**에 전달이 된다.  
- 제네릭 메서드는 클래스 전체가 아니라 특정 메서드 단위로 제네릭을 도입할 때 사용한다.
- 제네릭 메서드를 정의할 때는 메서드의 반환 타입 왼쪽에 다이아몬드를 사용한다.
- 제네릭 메서드는 메서드를 실제 호출하는 시점에 다이아몬드를 사용해서 <Integer> 와 같이 타입을 정하고 호출한다.
  
**참고**  
제네릭 타입은 static 메서드에 타입 매개변수를 사용할 수 없다. 제네릭 타입은 객체를 생성하는 시점에 타입이 정해지는데 static 메서드는
인스턴스 단위가 아니라 클래스 단위이기 때문에 객체 생성보다 순서가 먼저이다.
  
**따라서 static 메서드에 제네릭을 도입하려면 제네릭 메서드를 사용해야 한다.**
  
### 타입 매개변수 제한
제네릭 메서드도 타입과 마찬가지로 제한이 가능하다. 위의 세 번째 메서드가 바로 그것이다.  
`numberMethod()` 는 Number 가 최상위 타입이기 때문에 Number 밖의 타입은 사용하지 못한다.
  
## 제네릭 타입과 메서드 사이의 우선순위
제네릭 타입보다 제네릭 메서드가 높은 우선순위를 가진다.  
변수 또는 메서드의 이름이 같다면 제네릭 메서드가 적용된다.
  
## 와일드카드
프로그래밍에서 와일드카드는 *, ? 와 같이 하나 이상의 문자들을 상징하는 특수 문자를 뜻한다.  
간단히 여러 타입이 들어갈 수 있다는 의미이다.
```java
public class WildcardEx {

    static <T> void printGenericV1(Box<T> box) {
        System.out.println("T = " + box.get());
    }

    static void printWildcardV1(Box<?> box) {
        System.out.println("? = " + box.get());
    }
}
```
위는 제네릭, 아래는 와일드카드이다.  
우선 와일드 카드는 제네릭이 아니라는 점을 기억하자. 와일드카드는 이미 만들어진 제네릭 타입을 활용할 때 사용한다.  
Box 클래스가 제네릭이기 때문에 사용할 수 있다는 이야기이다.
  
이번에는 위 두 메서드를 비교해보자.  
제네릭은 우선 타입 매개변수가 명시되어 있는 반면에 와일드카드는 그냥 ? 하나가 적혀있을 뿐이다.  
제네릭 타입이나 제네릭 메서드를 정의하는게 꼭 필요한 상황이 아니라면 그냥 더 단순한 와일드 카드 사용을 권장한다.
  
그런데 와일드 카드는 반환값이 존재할 때 반환값의 타입을 항상 상한 타입으로만 반환한다. 위 코드로 치면 항상 Animal 객체를 반환한다.  
이는 Dog 또는 Cat 객체가 필요할 때도 Animal 객체가 나온다는 것이다.  
그래서 이런 경우는 제네릭을 사용하는 것이 바람직하다.

## 상한 와일드카드
```java
static void printWildcardV2(Box<? extends Animal> box) {
    Animal animal = box.get();
    System.out.println("이름 = " + animal.getName());
}
```
와일드 카드 또한 이렇게 상한을 지정할 수 있다.  

## 하한 와일드카드
```java
static void writeBox(Box<? super Animal> box) {
    box.set(new Dog("dog", 100));
}
```
이렇게 extends 대신 super 를 사용하면 ? 가 Animal 을 포함한 Animal 타입의 상위 타입만 입력 받을 수 있다는 뜻이 된다.
  
Box<Object> objBox: 허용
Box<Animal> animalBox: 허용
Box<Dog> dogBox: 불가
Box<Cat> catBox: 불가


## 타입 이레이저
위에서 설명한 컴파일 시점에 제네릭과 와일드 카드가 최상위 타입으로 변화하고 필요한 코드에서는 자동으로 다운캐스팅 코드가 작성되는 것을
타입 이레이저라고 이야기한다. 이 설명이 100% 정확한 것은 아니지만 대략적으로 비슷하다.
  
그리고 이 타입 이레이저 때문에 다음과 같은 코드를 작성하지 못한다.
```java
class EraserBox<T> {

    public boolean instanceCheck(Object param) {
        return param instanceof  T; // 불가
    }

    public T create() {
        return new T(); // 불가
    }
}
```
이 코드는 컴파일 시점이 아닌 런타임 시점에 타입을 비교하고 객체를 생성하는데, 제네릭은 일단 컴파일이 진행되면 최상위 타입으로 컴파일 되기 때문에
의도대로 작동하지 않는 코드가 되어버린다. 그래서 자바가 이를 막기 위해 컴파일 에러가 발생시킨다.