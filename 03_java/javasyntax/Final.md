# ***Final***

---

## Final 변수와 상수

`final` 키워드는 단어 그대로 `끝` 이라는 뜻이다.  
변수에 `final` 키워드가 붙으면 더는 값을 변경할 수 없다.

`final`은 `class`, `method`를 포함한 여러 곳에 붙을 수 있다.

```java
final int data1;
//data1 = 10; // 이렇게 변수를 한 번 초기화 하면
//data1 = 20; // 두번째 초기화부터는 컴파일 오류가 발생한다.

static void method(final int parameter) {
    parameter = 20; // 이 메서드 또한 컴파일 에러가 발생한다. 인자로 받은 값을 사용해야한다.
}
```
  
```java
public class ConstructInit {
    final int value;
    static final int CONST_VALUE = 10;
}
```
final 을 필드에 사용할 경우 해당 필드는 생성자를 통해서 한번만 초기화 될 수 있다.  
static 변수에도 final 을 선언할 수 있다. (상수)

### **상수**
상수(Constant) 는 변하지 않고 항상 일정한 값을 갖는 수를 말한다. 자바에서는 보통 단 하나만 존재하는 변하지 않는 고정된 값을 상수라 한다.  
-> `static final` | 대문자를 사용하고 구분은 언더바로 한다.

```java
public class Constant {
    public static final double PI = 3.14;
    
    public static final int HOURS_IN_DAY = 24;
    public static final int MINUTES_IN_HOUR = 60;
    public static final int SECONTDS_IN_MINUTE = 60;
    
    public static final int MAX_USERS = 1000;
}
```

## final 변수와 참조
```java
public class Data {
    public int value;
}
```
```java
public class FinalRefMain {

    static void main() {
        final Data data = new Data();
        // data = new Data(); // final 변수 참조값 변경 불가
        
        data.value = 10;
        data.value = 20;
        // 참조 대상의 필드를 변견하는 건 가능
    }
}
```

## **마치며**
`final`은 매우 유용한 제약이다. 만약 고객의 id 같은 할당 이후 변경해선 안되는 값은 final을 사용하자.

---

### 추가
  
- 클래스와 메서드에 사용되는 final
  - 클래스에 사용된 final
    - 상속이 끝났음을 알리는 상태
    - final 로 선언된 클래스는 더 이상 상속될 수 없다. (확장될 수 없다.)
  - 메서드에 사용된 final
    - final 이 선언된 메서드는 더 이상 오버라이드 될 수 없다.