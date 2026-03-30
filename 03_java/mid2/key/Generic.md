# ***Generic***

## 제네릭은 왜 필요한가 !
대부분의 최신 프로그래밍 언어는 제네릭을 제공한다.  
제네릭은 간단하게 말하면 클래스에 타입에 대한 매개변수를 추가하는 것이다.  
객체를 생성할 때 타입 인수를 전달하면 해당 타입에 대한 객체가 만들어진다. 코드로 알아보자.
  
```java
public class IntegerBox {
    private Integer value;
    
    public void set(Integer value) {
        this.value = value;
    }
    
    public Integer get() {
        return value;
    }
}

public class StringBox {
    private String value;
    
    public void set(String value) {
        this.value = value;
    }
    
    public String get() {
        return value;
    }
}

public class BoxMain1 {
    
    public static void main(String[] args) {
        IntegerBox integerBox = new IntegerBox();
        integerBox.set(10);
        Integer integer = integerBox.get();
        System.out.println("integer = " + integer);
        
        StringBox stringBox = new StringBox();
        stringBox.set("hello");
        String str = stringBox.get();
        System.out.println("str = " + str);
    }
}
```
위 두 클래스는 완벽히 동일하지만 타입만 다르다. 그래서 메인에서는 완벽히 같은 코드를 타입만 다르게 두 번 작성해야한다.  
이걸 어떻게 할 수 없을까?  
Object를 사용하면 한 번에 할 수 있지 않을까?
  
그렇다. Object 를 사용하면 해결할 수 있다 !

```java
public class BoxMain2 {

    public static void main(String[] args) {
        ObjectBox integerBox = new ObjectBox();
        integerBox.sert(10);
        Integer integer = (Integer) integerBox.get();
        System.out.println("integer = " + integer);

        ObjectBox stringBox = new ObjectBox();
        stringBox.set("hello");
        String str = (String) stringBox.get();
        System.out.println("str = " + str);
        
        //잘못된 타입
        integerBox.set("문자1000");
        Integer result = (Integer) integerBox.get(); //String -> Integer 캐스팅 예외 발생
    }
}
```
클래스 코드는 하나로 합쳐졌지만 메인에서는 그대로 두 개로 나눠야한다. 심지어 다운캐스팅을 해야한다는 리스크도 생겼다.  
다운 캐스팅을 잘못하면 위 세 번째 경우처럼 예외가 발생하고 프로그램이 터진다. 타입 안전성이 깨지는 것이다.
  
이런 문제를 해결하는 게 제네릭이다!

## 제네릭 적용
제네릭을 사용하면 코드 재사용과 타임 안전성을 둘 다 챙길 수 있다.

```java
public class GenericBox<T> {
    private T value;
    
    public void set(T value) {
        this.value = value;
    }
    
    public T get() {
        return value;
    }
}
```
- <> 를 사용한 클래스를 제네릭 클래스라고 하고 이 기호를 보통 다이아몬드라고 이야기한다.
- 제네릭 클래스를 사용할 때는 Integer, String 같은 타입을 미리 정하지 않고 타입 매개변수를 정한다.
- 타입 매개변수 명은 뭐가 되어도 상관 없다.

```java
public class BoxMain3 {
    
    public static void main(String[] args) {
        GenericBox<Integer> integerBox = new GenericBox<Integer>();
        integerBox.set(10);
        //integerBox.set("string"); // 타입에러
        Integer integer = integerBox.get();
        System.out.println("integer = " + integer);
        
        GenericBox<String> stringBox = new GenericBox<String>();
        stringBox.set("hello");
        String str = stringBox.get();
        System.out.println("str = " + str);
        
        // 모든 타입 사용 가능
        GenericBox<Double> doubleBox = new GenericBox<Double>();
        duobleBox.set(10,5);
        Double doubleValue = doubleBox.get();
        System.out.println("doubleValue = " + doubleValue);
    
        //타입추론: 생성자는 제네릭 타입 생략 가능
        GenericBox<Integer> integerBox2 = new GenericBox<>();
    }
}
```
이렇게 제네릭을 사용하면 생성 시점에 타입을 지정할 수 있다.

## 제네릭 용어와 관례
제네릭의 핵심은 **사용할 타입을 미리 결정하지 않는다는 점**이다.  
  
제네릭 명명 관례는 다음과 같다.
- E - Element
- K - Key
- N - Number
- T - Type
- V - Value
- S,U,V etc. - 2nd, 3rd, 4th types
  
또한 다음과 같이 여러 타입 매개변수를 선언할 수 있다.
`class Data<K, V> {}`  
  
타입 인자로 기본형은 넣을 수 없다. 래퍼 클래스를 사용해야한다.  
(int, double) (x), (Integer, Double) (o)
  
## 로 타입 - Raw Type

```java
public class RawTypeMain {
    public static void main(Stringp[] args) {
        GenericBox integerBox = new GenericBox();
        //GenericBox<Object> integerBox = new GenericBox<>();
    }
}
```
위처럼 객체를 생성하면 주석처리 된 부분처럼 Object 클래스로 자동 생성이 되고 이를 Raw type 이라고 한다.
