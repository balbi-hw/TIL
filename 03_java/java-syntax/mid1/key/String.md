# ***STRING***

## String 클래스
자바에서 문자를 다루는 타임은 대표적으로 `char`, `String` 두가지가 있다.  
기본형인 `char`은 문자 하나를 다룰 때 사용하고 `char`로 여러 문자를 나열하려면 `char[]` 배열을 사용해야한다.  
`char` 은 사용이 불편해서 자바에서는 `String` 클래스를 제공하는데, 문자열 생성 방법이 두 가지가 있다.
1. 쌍따옴표: "hello"
2. 객체 생성: new String("hello")
이렇게 `String`은 클래스이고 참조형이다. `str1` 변수에는 `String` 인스턴스의 참조값이 들어간다.
```java
String str1 = "hello";
String str1 = new String("hello");
```
객체를 만드는 방식도 가능하지만 자바에서는 생성자를 생략해도 자동으로 문자열 객체를 생성해준다.
  
## String 클래스 구조
`String` 클래스는 대략 다음과 같이 생겼다.
```java
public final class String {
    private final char[] value; // 자바 9 이전
    private final byte[] value; // 자바 9 이후
    // char은 메모리 2byte를 차지하는데 영어와 숫자는 보통 1byte 로 표현이 가능하기에
    // 영어와 숫자만 표현된 경우 1byte를 사용하고 그렇지 않은 경우 2byte인 UTF-16 인코딩을 한다.
    // 효율적인 메모리 사용이 가능하다.
    
    public String concat(String str) {}
    public int length() {}
    // 등등
}
```
클래스이기에 필드와 메서드를 가진다.
  
`Stirng` 클래스는 메서드가 매우 많기에 필요한 기능이 있으면 검색하거나 DOCs 를 찾아보자.
- lenth()
- charAt(int index): 특정 인덱스의 값을 반환
- substring(int beginIndex, int endIndex): 문자열의 부분을 반환
- indexOf(String str): 특정 문자열이 시작되는 인덱스를 반환
- toLowerCase(), toUpperCase()
- trim(): 양 옆 공백 제거
- concat(String str): 문자열을 더한다. 

## String 클래스와 참조형
`String`은 클래스라 기본형이 아니라 참조형이다. 그래서 계산할 수 없는 참조값이 들어가는데,  
이 때문에 원칙적으로 `+` 같은 연산을 할 수 없다.  
원래는 `String`이 제공하는 `concat()` 메서드를 사용해야하는데  
문자열은 너무 자주 사용되기 때문에 자바에서 특별히 `+` 연산을 제공한다.
```java
String result1 = a.concat(b);
String result2 = a + b;
// 두 계산의 결과는 같다.
```

## String 클래스의 비교
`String` 클래스 간의 비교를 할 때는 항상 `equals()` 비교를 해야한다.  
- 쌍따옴표를 이용해 만든 문자열은 `String Pool` 이라고 하는 곳에 저장되고 같은 문자열은 두 번 생성하지 않는다.
  - 이 때 풀 안의 문자열은 참조값을 가지며 만들어진 객체는 해당 참조값을 갖는다. ( `==` 실패 )
- 생성자를 이용하면 두 개의 객체가 만들어지고 각 객체에 문자열을 갖는다.
  
이런 특징 때문에 리터럴을 사용하는 경우 같은 참조값을 가지므로 `==` 비교에 성공한다.  
그럼 리터럴을 사용해 만들면 `==` 비교, 생성자를 이용하면 `equals` 비교를 하면 안될까?
  
가능하지만 기능을 만든 개발자랑 사용하는 개발자가 항상 같을 수 없다.  
두 경우를 구분하면 착오가 생기기 쉽기 때문에 항상 성공하는 `equals()`를 사용한 비교를 하는게 바람직하다.


## String 클래스 - 불변 객체
기본적으로 `String`은 불변객체이다.  
이는 문자열의 특징인 `String Pool` 때문인데, 같은 문자열 참조값을 갖는 객체들은  
문자열에 변동이 생기면 사이드이펙트가 생기기 쉽다.  
이런 이유로 `String`은 불변객체이고 값을 변화시키는 메서드는 모두 새로운 문자열을 반환한다.


## 알아야하는 문자열 메서드
강의에도 정말 많은 메서드가 나와있어서 개인적으로 정말 필요할 것 같은 것만 추렸다.
**정보 조회**
- length()
- isEmpty()
- isBlank()
- charAt()
  
**문자열 비교**
- eqauls(Object anObject)
- equalsIgnoreCase(String anotherString): 두 문자를 대소문자 구분 없이 비교한다.
- compareTo(String anotherString): 두 문자를 사전 순으로 비교한다.
- compareToIgnoreCase(String str): 두 문자를 대소문자 구분 없이 사전순으로 비교한다.
  
**문자열 검색**
- contains(CharSequence s): 문자열이 특정 문자열을 포함하는지 확인한다.
- indexOf(String ch) / indexOf(String ch, int fromIndex): 문자열이 처음 등장하는 위치를 반환한다.
- lastIndexOf(String ch): 문자열이 마지막으로 등장하는 위치를 반환한다.
- substring(int beginIndex) / substring(int beginIndex, int endIndex): 문자열의 부분을 반환한다.
- concat(String str): 문자열의 끝에 다른 문자열을 붙인다.
- replace(CharSequence target, CharSequence replacement): 특정 문자열을 새 문자열로 대체한다.
- replaceAll(String regex, String replacement): 문자열에서 정규식과 일치하는 부분을 대체한다.
- toLowerCase() / toUpperCase(): 문자열을 소문자나 대문자로 변환한다.
- trim(): 문자열 양쪽 끝의 공백을 제거한다.
  
**문자열 분할 및 조합**
- split(String regex): 문자열을 정규 표현식을 기준으로 분할한다.
- join(CharSequence delimiter, CharSequence.. elements): 주어진 구분자로 여러 문자열을 결합한다.
  
**기타 유틸**
- valueOf(Object obj): 다양한 타입을 문자열로 변환한다.


## StringBuilder - 가변 String
불변인 `String` 클래스에도 단점이 있다.
```java
String str = "A" + "B" + "C" + "D";
String str = String("A") + String("B") + String("C") + String("D");
String str = new String("AB") + String("C") + String("D");
String str = new String("ABC") + String("D");
String str = new String("ABCD");
```
바로 문자를 더하거나 변경할 때 마다 새로운 객체를 만들어야 한다는 점이다. 결과적으로 컴퓨터의
리소스를 더 많이 사용하게 된다.
  
**StringBuilder**
이 문제를 해결하는 방법으로 불변이 아닌 `가변 String`을 만드는 개념이다. 가변 객체는 내부의 값을 바로
변경하면 되기 때문에 새로운 객체를 생성할 필요가 없다.  
물론 가변 객체의 사용은 사이드 이펙트에 주의해서 사용해야 한다.
  
**StringBuilder 사용 예**
```java
public class StringBuilderMain1_1 {
    static void main() {
        StringBuilder sb = new StringBuilder();
        sb.append("A");
        sb.append("B");
        sb.append("C");
        sb.append("D");
        System.out.println("sb = " + sb);
        
        sb.insert(4, "Java");
        System.out.println("insert = " + sb);
        
        sb.delete(4, 8);
        System.out.println("delete = " + sb);

        sb.reverse();
        System.out.println("reverse = " + sb);
        
        String string = sb.toString();
        System.out.println("string = " + string);
    }
}
```
```java
// 실행 결과
sb = ABCD
insert = ABCDJava
delete = ABCD
reverse = DCBA
string = DCBA
```
위와 같이 `StringBuilder` 는 보통 문자열 변경이 완료되면 안전한 불변 객체 `String`으로 변환하는 것이 좋다.

> **참고: StringBuilder vs StringBuffer**
> `StringBuilder` 와 같은 기능을 수행하는 `StringBuffer`도 있다.
> `Buffer` 는 내부에 동기화가 되어 있어 멀티스레드 환경에 안전하지만 동기화 오버헤드로 인해 성능이 느리다.
> `Builder` 는 멀티스레드에 안전하지 않지만 오버헤드가 없어 속도가 빠르다.
> 아직은 그냥 그런게 있구나 하고 넘겨도 된다고 한다.

## 메서드 체이닝 - Method Chaining
```java
public class ValueAdder {
    private int value;
    
    public ValueAdder add(int addValue) {
        value += addValue;
        return this;
    }
    
    public int getValue() {
        return value;
    }
}
```
- 단순히 값을 누적해 더하는 기능을 제공하는 클래스
- `add()` 메서드를 호출하면 내부의 `value`에 값을 누적한다.
- `add()` 메서드는 자기 자신의 참조값을 반환한다.
  
```java
public class MethodChainingMain1 {
    static void main() {
        ValueAdder adder = new ValueAdder();
        adder.add(1);
        adder.add(2);
        adder.add(3);
        int result = adder.getValue();
        System.out.println("result = " + result);
    }
}
// result = 6
```
- `add()` 메서드를 여러번 호출해서 값을 누적해 더하고 출력한다.
- 그런데 여기서 add()의 반환값을 사용하지 않았다.

```java
public class MethodChainingMain2 {
    static void main() {
        ValueAdder adder = new ValueAdder();
        ValueAdder adder1 = adder.add(1);
        ValueAdder adder2 = adder1.add(2);
        ValueAdder adder3 = adder2.add(3);
        int result = adder3.getValue();
        System.out.println("result = " + result);
    }
}
// result = 6
```
위 두 코드는 같은 기능을 수행한다. 그런데 후자가 전자보다 훨씬 복잡해보이는데 왜 후자의 방식을 사용할까?
  
이번에는 방금 사용헀던 방식에서 반환된 참조값을 새로 변수에 담지 말고 바로 사용해보자.

```java
public class MethodChainingMain3 {
    static void main() {
        ValueAdder adder = new ValueAdder();
        int result = adder.add(1).add(2).add(3).getValue();
        System.out.println("result = " + result);
    }
}
// result = 6
```
이렇게 간단하게 표현할 수 있다.
  
메서드 호출의 결과로 자기 자신의 참조값을 반환하면 그 참조값을 사용해 다시 메서드를 호출할 수 있다.  
이런 기법을 메서드 체이닝이라 한다.  
메서드 체이닝은 코드를 간결하고 읽기 쉽게 만들어준다.
  
**StringBuilder 와 메서드 체인**
`StringBuilder`의 `append()` 메서드를 보면 자기 자신의 참조값을 반환한다.
```java
public StringBuilder append(String str) {
    super.append(str);
    return this;
}
```
그래서 앞서 `StringBuilder`를 사용해 만든 코드는 다음과 같이 개선할 수 있다.
```java
public class StringBuilderMain1_2 {
    static void main() {
        StringBuilder sb = new StringBuilder();
        String string = sb.append("A").append("B").append("C").append("D")
                .insert(4, "Java")
                .delete(4, 8)
                .reverse()
                .toString();

        System.out.println("string = " + string);
    }
}
// string = DCBA
```
  
### 정리
**"만드는 사람이 수고로우면 쓰는 사람이 편하고, 만드는 사람이 편하면 쓰는 사람이 수고롭다"** 라는 말이 있다고 합니다.  
메서드 체이닝은 구현하는 입장에서는 번거롭지만 사용하는 개발자는 편리해진다.  
자바의 라이브러리와 오픈 소스들은 메서드 체이닝을 종종 사용한다.
