# ***Wrapper***

## 기본형의 한계
자바는 객체 지향 언어이다. 그런데 자바 안에 `int`, `double` 같은 기본형이 있다.
기본형은 객체가 아니기 때문에 다음과 같은 한계가 있다.
- 객체가 아니다.: 기본형 데이터는 객체가 아니라 객체지향 프로그래밍의 장점을 살릴 수 없다.
예를 들어 객체는 유용한 메서드를 제공할 수 있는데, 기본형은 메서드를 제공하지 않는다.
  - 객체 참조가 필요한 컬렉션 프레임워크를 사용할 수 없고 제네릭도 사용할 수 없다.
- null 값을 가질 수 없다.: 기본형은 `null` 값을 가질 수 없다. 때로는 데이터가 `없음`이라는
상태를 나타내야 할 필요가 있는데, 기본형은 이런 표현이 불가능하다.

```java
void main() {
    int value = 10;
    int i1 = compareTo(value, 5);
    int i2 = compareTo(value, 10);
    int i3 = compareTo(value, 20);
    System.out.println("i1 = " + i1);
    System.out.println("i2 = " + i2);
    System.out.println("i3 = " + i3);
}

public static int compareTo(int value, int target) {
    if (value < target) {
        return -1;
    } else if (value > target) {
        return 1;
    } else {
        return 0;
    }
}
```
`int` 가 클래스이고 그 클래스가 비교 메서드를 제공했다면 더 편하고 간결한 코드를
작성할 수 있었을 것이다.
  
그래서 래퍼 클래스가 등장했다.

**직접 만든 래퍼 클래스**
```java
public class MyInteger {
    private final int value;

    public MyInteger(int value) {
        this.value = value;
    }

    public int getValue() {
        return value;
    }

    public int compareTo(int target) {
        if (value < target) {
            return -1;
        } else if (value > target) {
            return 1;
        } else {
            return 0;
        }
    }
    
    @Override
    public String toString() {
        return String.valueOf(value);
    }
}
```
- `MyInteger`는 `int value`라는 단순한 기본형 변수를 하나 가지고 있다.
- 이 변수를 편리하게 사용하도록 메서드를 제공한다.
- compareTo() 메서드를 클래스 내부로 캡슐화 헀고, 불변으로 설계했다.
  
이 래퍼 클래스 덕분에 다음과 같은 코드 작성이 가능해졌다.
```java
public class MyIntegerMethodMain1 {
    static void main() {
        Myinteger myinteger = new Myinteger(10);
        int i1 = myinteger.compareTO(5);
        int i2 = myinteger.compareTO(10);
        int i3 = myinteger.compareTO(20);
        System.out.println("i1 = " + i1);
        System.out.println("i2 = " + i2);
        System.out.println("i3 = " + i3);
    }
}
```
이렇게 기본형 데이터를 감싸는 클래스를 래퍼클래스라고 한다.

## 기본형의 한계2
**기본형과 null**
기본형은 항상 값을 가져야하기 때문에 null 값을 가질 수가 없다.
```java
public class MyIntegerNullMain0 {
    static void main() {
        int[] intArr = {-1, 0, 1, 2, 3};
        System.out.println(findValue(intArr, -1));
        System.out.println(findValue(intArr, 0));
        System.out.println(findValue(intArr, 1));
        System.out.println(findValue(intArr, 100));
    }
    
    private static int findValue(int[] intArr, int target) {
        for (int value :intArr){
            if (value == target) {
                return value;
            }
        }
        return -1;
    }
}
// 실행 결과
// -1
// 0
// 1
// -1
```
`findValue()` 메서드는 배열에 찾는 값이 있으면 해당 값을 반환하고 없으면 `-1`을 반환한다.  
실행 결과를 보면 `-1`이 두개인데 이게 -1이 배열에 있어서 나온건지 없어서 -1이 나온건지 알 수가 없다.  
  
객체라면 null 이라는 값이 있어서 명확하게 할 수 있다.
```java
public class MyIntegerNullMain1 {
  static void main() {
    MyInteger[] intArr = {new Myinteger(-1), new Myinteger(0), new Myinteger(1)};
    System.out.println(findValue(intArr, -1));
    System.out.println(findValue(intArr, 0));
    System.out.println(findValue(intArr, 1));
    System.out.println(findValue(intArr, 100));
  }
  
  private static MyInteger findValue(MyInteger[] intArr, int target) {
    for (MyInteger myInteger : intArr) {
      if (myInteger.getValue() == target) {
          retrun myInteger;
      }
    }
    return null;
  }
}
// 실행 결과
// -1
// 0
// 1
// null
```
기본형은 항상 값이 존재해야한다. 숫자의 경우 0, -1 같은 값이라도 항상 있어야한다.  
반면 객체인 참조형은 값이 없다는 `null` 을 사용할 수 있다.  
물론 `null` 값을 반환하는 경우 잘못하면 `NullPointerException` 이 발생할 수 있으니 주의해야 한다.

## 래퍼 클래스
래퍼 클래스는 기본형을 객체로 감싸 더 편리하게 사용하도록 도아줘서 매우 유용하다.  
쉽게 기본형의 객체 버전이 래퍼 클래스이다.
  
유용한 만큼 자바에서 기본적으로 제공하는 래퍼클래스가 있다.
- `byte` > `Byte`
- `short` > `Short`
- `int` > `Integer`
- `long` > `Long`
- `float` > `Float`
- `double` > `Double`
- `char` > `Character`
- `boolean` > `Boolean`
  
이 기본 제공 클래스들은 다음과 같은 특징이 있다.
- 불변이다
- `equals()`를 통해 비교해야 한다.

대략적 사용법은 다음과 같다.
```java
public class WrapperClassMain {
  public static void main(String[] args) {
    Integer newInteger = new Integer(10);
    Integer integerObj = Integer.valueOf(10);
    Long longObj = Long.valueOf(100);
    Double doubleObj = Double.valueOf(10.5);

    System.out.println("newInteger = " + newInteger);
    System.out.println("integerObj = " + integerObj);
    System.out.println("longObj = " + longObj);
    System.out.println("doubleObj = " + doubleObj);

    System.out.println("내부 값 읽기");
    int intValue = integerObj.intValue();
    System.out.println("intValue = " + intValue);
    long longValue = longObj.longValue();
    System.out.println("longValue = " + longValue);

    System.out.println("비교");
    System.out.println("==: " + (newInteger == integerObj));
    System.out.println("eqauls: " + newInteger.equals(integerObj));
  }
}
```
```java
// 실행 결과
newInteger = 10
integerObj = 10
longObj = 100
doubleObj = 10.5
내부 값 읽기
        intValue = 10
longObj = 100
비교
==: false
equals: true
```

래퍼 클래스 생성 - 박싱( Boxing )
- 기본형을 래퍼 클래스로 변경하는 것을 박싱이라고 한다.
- 위 코드의 `new Integer(10)`은 향후 자바에서 제거될 예정이다.
  - 대신 `Integer.valueOf(10)` 을 사용하자.
  
xxxValue() - 언박싱 ( Unboxing )
- 기본형 값을 다시 꺼내는 메서드이다.
  
비교는 equals()를 사용한다.
- 래퍼 클래스는 객체이기 때문에 `==` 비교를 하면 인스턴스의 참조값을 비교한다.
- 래퍼 클래스는 `equals()`를 오버라이딩 해두었으니 사용하면 된다.
  
래퍼클래스는 `toString()`도 오버라이딩 되어있다.
  
## AutoBoxing, 오토박싱
`int`를 `Integer`로 변환하거나 반대의 경우를 정리해보자  
`valueOf()`, `intValue()` 메서드를 사용하면 된다.
```java
public class AutoboxingMain1 {
    public static void main(String[] args) {
        int value = 7;
        Integer boxedValue = Integer.valueOf(value);
        
        int unboxedValue = boxedValue.intValue();

        System.out.println("boxedValue = " + boxedValue);
        System.out.println("unboxedValue = " + unboxedValue);
    }
}
// 실행 결과
// boxedValue = 7
// unboxedValue = 7
```
- 박싱: `valueOf()`
- 언박싱: `xxxValue()`
  
그런데 박싱 언박싱은 개발자들이 워낙 많이 사용하는 개념이기 때문에 자바에서 기본 제공을 하게 되었다.
```java
// 오토 박싱, 오토 언박싱
public class AutoboxingMain2 {
    public static void main(String[] args) {
        int value = 7;
        Integer boxedValue = value;
        
        int unboxedValue = boxedValue;

      System.out.println("boxedValue = " + boxedValue);
      System.out.println("unboxedValue = " + unboxedValue);
    }
}
```
오토 박싱과 오토 언박싱은 컴파일러가 개발자 대신 `valueOf`, `xxxValue()` 등의 코드를 추가해주는 기능이다.  
덕분에 기본형과 래퍼형을 서로 편리하게 변환할 수 있다.  
아래 두 코드는 동일한 기능을 수행한다.
```java
Integer boxedValue = value;
Integer boxedValue = Integer.valueOf(value);

int unboxedValue = boxedValue;
int unboxedValue = boxedValue.intValue();
```

## 래퍼 클래스의 주요 메서드와 성능
```java
public class WrapperUtilsMain {
    public static void main(String[] args) {
        Integer i1 = Integer.valueOf(10);
        Integer i2 = Integer.valueOf("10");
        int intValue = Inter.parseInt("10");
        
        int compareResult = i1.compareTo(20);
        System.out.println("compareResult = " + compareResult);

        System.out.println("sum: " + Integer.sum(10, 20));
        System.out.println("min: " + Integer.min(10, 20));
        System.out.println("max: " + Integer.max(10, 20));
    }
}
```
- valueOf(): 래퍼 타입을 반환한다.
- parseInt(): 문자열을 기본형으로 변환한다.
- compareTo(): 내 값과 인수로 넘어온 값을 비교한다. 내 값이 크면 `1`, 같으면 `0`, 내 값이 작으면 `-1`을 반환한다.
- `Integer.sum()`, `Integer.min()`, `Integer.max()`: `static` 메서드이다. 간단한 덧셈, 작은 값, 큰 값 연산을 수행한다.

***parseInt() vs valueOf()***
원하는 타입에 맞는 메서드를 사용하자.
- valueOf("10")은 래퍼 타입을 반환한다.
- parseInt("10")은 기본형을 반환한다.
  - Long.parseLong() 처럼 각 타입에 parseXxx() 가 존재한다.


## 래퍼 클래스와 성능
래퍼 클래스는 객체이기 때문에 기본형보다 다양한 기능이 있다. 그럼 래퍼만 제공하지 기본형은 왜 유지할까?  
다음과 같은 이유가 있다.
- 기본형 연산이 래퍼 클래스보다 빠르다.
- 기본형이 메모리를 더 적게 사용한다.
  
그럼 뭘 사용해야할까?
  
**유지보수 vs 최적화**
양자택일의 상황이라면 **유지보수**가 우선된다. 최신 컴퓨터는 사양이 매우 좋기 때문에 이 정도 최적화는 고려하지 않아도 괜찮은 경우가 많다.
- 코드 변경 없이 성능 최적화를 하면 가장 좋지만 보통 최적화는 복잡함을 요구하는 경우가 많다.
그런데 최적화를 한다고 해도 전체 애플리케이션의 성능 관점에서 보면 불필요한 최적화를 할 가능성이 있다.
- 웹 애플리케이션의 경우 메모리 안에서 발생하는 연산 하나보다 네트워크 호출 한 번이 많게는 수십만배 더 오래 걸린다.
자바 내부 연산보다 네트워크 호출 한 번을 더 줄이는 것이 더 효과적인 경우가 많다.
- 권장하는 방법은 개발 이후에 성능 테스트를 해보고 정말 문제가 되는 부분을 찾아서 최적화 하는 것이다.
