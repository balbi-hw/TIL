# ***Enumerate, 열거형***

## 문자열과 타입 안전성1
열거형 설명 이전에 먼저 다음 예제를 살펴보자.

**비즈니스 요구사항**
고객은 3등급으로 나누고, 상품 구매시 등급별로 할인을 적용한다. 할인시 소수점 이하는 버린다.
- BASIC > 10% 할인
- GOLD > 20% 할인
- DIAMOND > 30% 할인

```java
public class DiscountService {
    public int discount(String grade, int price) {
        int discountPercent = 0;

        if (grade.equals("BASIC")) {
            discountPercent = 10;
        } else if (grade.equals("GOLD")) {
            discountPercent = 20;
        } else if (grade.equals("DIAMOND")) {
            discountPercent = 30;
        } else {
            System.out.println(grade + ": 할인X");
        }
        return price * discountPercent / 100;
    }
}

public class StringGradeEx0_1 {
    public static void main(String[] args) {
        int price = 10000;

        DiscountService discountService = new DiscountService();
        int basic = discountService.discount("BASIC", price);
        int gold = discountService.discount("GOLD", price);
        int diamond = discountService.discount("DIAMOND", price);

        System.out.println("BASIC 등급의 할인 금액: " + basic);
        System.out.println("GOLD 등급의 할인 금액: " + gold);
        System.out.println("DIAMOND 등급의 할인 금액: " + diamond);
    }
}
```
이렇게 코드를 구성할 수 있다.  
그런데 지금과 같이 단순히 문자열을 입력하는 방식은 오타가 발생하기 쉽고 유효하지 않는 값이 입력될 수 있다.

```java
public class StringGradeEx0_2 {
    public static void main(String[] args) {
        int price = 10000;

        DiscountService discountService = new DiscountService();
        
        // 존재하지 않는 등급
        int vip = discountService.discount("VIP", price);
        System.out.println("VIP 등급의 할인 금액: " + vip);
        
        // 오타
        int diamondd = discountService.discount("DIAMONDD", price);
        System.out.println("DIAMONDD 등급의 할인 금액: " + diamondd);
        
        // 소문자 입력
        int gold = discountService.discount("gold", price);
        System.out.println("gold 등급의 할인 금액: " + gold);
    }
}
```
이렇게 미리 정해지지 않은 값이 입력되면 장애가 발생한다.  
지금의 방식은 다음과 같은 문제가 있다.
- **타입 안정성 부족**: 문자열은 오타가 발생하기 쉽고, 유효하지 않은 값이 입력될 수 있다.
- **데이터 일관성**: GOLD, gold, Gold 등 다양한 형식으로 입력이 가능해 일관성이 떨어진다.

**String 사용 시 타입 안정성 부족 문제**
- 값의 제한 부족: `String`으로 상태나 카테고리를 표현하면 잘못된 문자열이 들어올 가능성이 있다.
- 컴파일 시 오류 감지 불가: 이러한 오기는 컴파일 시 감지가 되지 않고 런타임에서만 문제가 발견되어 디버깅이 어렵다.
  
이런 문제를 해결하기 위해는 입력값을 제한해야하는데 `String` 타입으로는 이 제한이 불가능하다.
  
## 문자열과 타입 안전성2
이번에는 상수를 사용해보자

```java
public class StringGrade {
    public static final String BASIC = "BAISC";
    public static final String GOLD = "GOLD";
    public static final String DIAMOND = "DIAMOND";
}

public class DiscountService {
    public int discount(String grade, int price) {
        int discountPercent = 0;

        if (grade.equals(StringGrade.BASIC)) {
            discountPercent = 10;
        } else if (grade.equals(StringGrade.GOLD)) {
            discountPercent = 20;
        } else if (grade.equals(StringGrade.DIAMOND)) {
            discountPercent = 30;
        } else {
            System.out.println(grade + ": 할인X");
        }

        return price * discountPercent / 100;
    }
}

public class StringGradeEx1_1 {
    public static void main(String[] args) {
        int price 10000;

        DiscountService discountService = new DiscountService;
        int basic = discountService.discount(StringGrade.BASIC, price);
        int gold = discountService.discount(StringGrade.GOLD, price);
        int diamond = discountService.discount(StringGrade.DIAMOND, price);

        System.out.println("BASIC 등급의 할인 금액 = " + basic);
        System.out.println("GOLD 등급의 할인 금액 = " + gold);
        System.out.println("DIAMOND 등급의 할인 금액: " + diamond);
    }
}
```
상수 덕분에 조금 더 명확해진..? 느낌이다. 그리고 discount() 에 인자를 전달할 때도
StringGrade 가 제공하는 상수를 사용하면 된다. 입력값이 잘못되면 컴파일 에러가 발생하여
문제 중 하나가 해결되었다.
  
하지만 이는 근본적 해결책이 아니다. 여전히 String에는 어떤 문자열이든 입력할 수 있고
어떤 개발자가 실수로 StringGrade 의 상수를 사용하지 않고 다음과 같이 사용해도 막지 못한다.
```java
public class StringGradeEx1_2 {
    public static void main(String[] args) {
        int price = 10000;
        
        DiscountService discountService = new DiscountService();

        // 존재하지 않는 등급
        int vip = discountService.discount("VIP", price);
        System.out.println("VIP 등급의 할인 금액: " + vip);

        // 오타
        int diamondd = discountService.discount("DIAMONDD", price);
        System.out.println("DIAMONDD 등급의 할인 금액: " + diamondd);

        // 소문자 입력
        int gold = discountService.discount("gold", price);
        System.out.println("gold 등급의 할인 금액: " + gold);
    }
}
```
또한 코드를 사용하는 사용자 입장에서 상수가 어디에 있는지 어떻게 알 수 있을까?
```java
public int discount(String grade, int price) {}
```
이 코드에는 분명 String을 인자로 받는다고 되어 있다.  
결국 누군가 주석을 잘 남겨 StringGrade 의 상수를 사용해달라고 해야하고 이렇게 한다해도
문제가 해결되는 것은 아니다.

## 타입 안전 열거형 패턴
**타입 안전 열거형 패턴 - Type-Safe Enum Pattern**
이런 문제를 해결하기 위해 나온 것이 타입 안전 열거형 패턴이다.  
`enum` 은 `enumeration`의 줄임말인데 이는 열거라는 뜻이다.  
이 enum 의 핵심은 이걸 사용하면 열거한 항목만 사용할 수 있다는 점이다.  
쉽게 String 같이 모든 문자열을 사용할 수 있는게 아니라 우리가 지정한 문자만 사용할 수 있다.

```java
public class ClassGrade {
    public static final ClassGrade Basic = new ClassGrade();
    public static final ClassGrade GOLD = new ClassGrade();
    public static final ClassGrade DIAMOND = new ClassGrade();
}
```
- 등급을 다루는 클래스를 만들고 등급 별 상수를 선언한다.
- 각 상수마다 별도의 인스턴스를 만들고 인스턴스 참조값을 초기화한다.

```java
public class ClassRefMain {
    public static void main(String[] args) {
        System.out.println("class BASIC = " + ClassGrade.BASIC.getClass());
        System.out.println("class GOLD = " + ClassGrade.GOLD.getClass());
        System.out.println("class DIAMOND = " + ClassGrade.DIAMOND.getClass());

        System.out.println("ref BASIC = " + ClassGrade.BASIC);
        System.out.println("ref GOLD = " + ClassGrade.GOLD);
        System.out.println("ref DIAMOND = " + ClassGrade.DIAMOND);
    }
}
```
- 각 상수는 모두 ClassGrade 타입을 기반으로 인스턴스를 만들었기에 클래스가 모두 같다
- 각 상수는 모두 다른 인스턴스를 참조해 참조값은 다르다.
  
이렇게 BASIC, GOLD, DIAMOND 를 상수로 열거했으니 이제 ClassGrade 타입을 사용할 때는 상수를 사용하면 된다.
```java
public class DiscountService {
    public int discount(ClassGrade classGrade, int price) {
        int discountPercent = 0;
        
        if (classGrade == ClassGrade.BASIC) {
            discountPercent = 10;
        } else if (classGrade == ClasssGrade.GOLD) {
            discountPercent = 20;
        } else if (classGrade == ClassGrade.DIAMOND) {
            discountPercent = 30;
        } else {
            System.out.println("할인 X");
        }
        
        return price * discountPercent / 100;
    }
}
```
- discount() 메서드는 매개변수로 ClassGrade 클래스를 사용헀다.
- 값을 비교할 때 `==` 참조값 비교를 사용했다.
  - 매개변수에 넘어오는 인수도 ClassGrade가 가진 상수 중 하나를 사용하기에 참조값 비교로 충분하다.

```java
public class ClassGradeEx2_1 {
    public static void main(String[] args) {
        int price = 10000;
        
        DiscountService discountService = new DiscountService();
        
        int basic = discountService.discount(ClassGrade.BASIC, price);
        int gold = discountService.discount(ClassGrade.GOLD, price);
        int diamond = discountService.discount(ClassGrade.DIAMOND, price);
        
        System.out.println("BASIC 등급의 할인 금액: " + basic);
        System.out.println("GOLD 등급의 할인 금액: " + gold);
        System.out.println("DIAMOND 등급의 할인 금액: " + diamond);
    }
}
```

**private 생성자**
위 방식은 많이 개선헀지만 그래도 아직 문제가 있다.  
외부에서 임의로 ClassGrade 의 인스턴스를 생성할 수 있다는 점이다.
```java
public class ClassGradeEx2_2 {
     public static void main(String[] args) {
         int price = 10000;
         
         DiscountService discountService = new DiscountService();
         
         ClassGrade newClassGrade = new ClassGrade(); //생성자 private으로 막아야 함
         int result = discountService.discount(newClassGrade, price);
         System.out.println("newClassGrade 등급의 할인 금액: " + result);
     }
}
```
이렇게 newClassGrade 를 만들 수 있다.  
이 문제는 생성자를 `private`으로 막으면 된다.
```java
public class ClassGrade {
    
    public static final ClassGrade BASIC = new ClassGrade();
    public static final ClassGrade DIAMOND = new ClassGrade();
    public static final ClassGrade DIAMOND = new ClassGrade();

    private ClassGrade() {}
}
```
- private 생성자를 통해 외부 인스턴스 생성을 막았다.
- 이제 ClassGrade 인스턴스를 사용할 때는 ClassGrade 내부에 정의한 상수를 사용해야하고
그렇지 않으면 컴파일 오류가 발생한다.

### 타입 안전 열거형 패턴의 장점
- 타입 안전성 향상: 정해진 객체만 사용할 수 있어 잘못된 값을 입력할 수 없다.
- 데이터 일관성: 정해진 객체만 사용하므로 데이터의 일관성이 보장된다.

- 제한된 인스턴스 생성: 클래스는 사전에 정의된 몇 개의 인스턴스만 생성하고 외부에서는 이것들만
사용할 수 있도록 한다.
- 타입 안전성: 이 패턴을 사용하면 잘못된 값이 할당되거나 사용되는 것을 컴파일 시점에 방지할 수 있다.

### 단점
- 코드가 길고 private 생성자를 만드는 등 유의해야하는 부분도 있다.

## 열거형 - Enum Type
자바에서는 위의 타입 안전 열거형 패턴을 편리하게 사용할 수 있는 열거형을 제공한다.
  
```java
public enum Grade {
    BASIC, GOLD, DIAMOND
}
```
- 열거형을 정의할 때는 `class` 대신에 `enum`을 사용한다.
- 그냥 원하는 상수를 나열하면 끝이다.
- 매우매우 편리하다.
- 열거형도 클래스이다.
- 열거형은 자동으로 `java.lang.Enum` 을 상속받는다
- 외부에서 임의로 생성할 수 없다.

```java
public class EnumRefMain {
     public static void main(String[] args) {
         System.out.println("class BASIC = " + Grade.BASIC.getClass());
         System.out.println("class GOLD = " + Grade.GOLD.getClass());
         System.out.println("class DIAMOND = " + Grade.DIAMOND.getClass());
         
         System.out.println("ref BASIC = " + refValue(Grade.BASIC));
         System.out.println("ref GOLD = " + refValue(Grade.GOLD));
         System.out.println("ref DIAMOND = " + refValue(Grade.DIAMOND));
         }
         
         private static String refValue(Object grade) {
            return Integer.toHexString(System.identityHashCode(grade));
     }
}
```
- 위의 코드는 지금까지 작성했던 코드들과 같은 결과를 얻을 수 있다.
- 열거형은 toString()을 오버라이딩 하기 때문에 참조값을 구하기 위해 refValue 메서드를 만들었다.
- 열거형도 클래스이다. 열거형 제공을 위해 제약이 추가된 클래스이다.

### 열거형의 장점
- 타입 안전성 향상
- 간결성 및 일관성: 직접 구현한 것보다 코드가 매우 간결하고 일관성이 보장된다.
- 확장성: 새로운 회원 등급을 추가할 때, ENUM에 새로운 상수를 추가하기만 하면 된다.

## 주요 메서드
모든 열거형은 `java.lang.Enum` 클래스를 자동으로 상속 받는다. 따라서 해당 클래스의 기능을 사용할 수 있다.
```java
import java.util.Arrays;

public class EnumMethodMain {
    public static void main(String[] args) {
        
        //모든 ENUM 반환
        Grade[] values = Grade.values();
        System.out.println("valeus = " + Arrays.toString(values));
        for (Grade value : values) {
            System.out.println("name= " + value.name() + ", ordinal= " + value.ordinal());
        }
        
        //String -> ENUM 변환, 잘못된 문자면 에러 발생
        String input = "GOLD";
        Grade gold = Grade.valueOf(input);
      System.out.println("gold = " + gold);
    }
}
```
- values(): 모든 ENUM 상수를 포함하는 배열을 반환한다.
- valueOf(String name): 주어진 이름과 일치하는 ENUM 상수를 반환한다.
- neme(): ENUM 상수의 이름을 문자열로 반환한다.
- ordinal(): ENUM 상수의 선언 순서(0부터 시작) 을 반환한다.
- toString(): ENUM 상수의 이름을 문자열로 반환한다. name() 메서드와 유사하지만 toString() 은 직접 오버라이드 할 수 있다.

**주의! ordinal()은 가급적 지양하자**
- ordinal 은 새 상수를 선언하면 인덱스가 밀리기 쉽기 때문이다.
  - python list에서 pop 을 잘 안쓰는 것과 같은 이유
- BASIC 과 GOLD 사이에 SILVER 가 추가되면 인덱스 값이 밀린다 !

**열거형 정리**
- 열거형은 `java.lang.Enum` 을 자동(강제)으로 상속 받는다.
- 열거형은 이미 상속을 받았기 때문에 추가로 다중상속 ㅂ다을 수 없다.
- 열거형은 인터페이스 구현이 가능하다.
- 열거형에 추상 메서드를 선언하고, 구현할 수 있다.
  - 이 경우 익명 클래스와 같은 방식을 사용한다.

## 리팩토링1
지금까지 구현한 코드들을 더 읽기 쉽게 리팩토링 해보자 !
```java
// DiscountService.discount() 를 살펴보자
if (classGrade == ClassGrade.BASIC) {
    discountPercent = 10;
} else if (classGrade == ClassGrade.GOLD) {
    discountPercent = 20;
} else if (classGrade == ClassGrade.DIAMOND) {
    discountPercent = 30;
} else {
    System.out.println("할인X")
}
```
- 불필요한 if 문을 제거하자
- 할인율은 각각의 회원 등급별로 판단된다. 그러니 할인율을 클래스 필드로 선언하자.

```java
public class ClassGrade {
    public static final ClassGrade BASIC = new ClassGrade(10);
    public static final ClassGrade GOLD = new ClassGrade(20);
    public static final ClassGrade DIAMOND = new ClassGrade(30);

    private final int discountPercent;
    
    private ClassGrade(int discountPercent) {
        this.discountPercent = discountPercent;
    }
    
    public int getDiscountPercent() {
        return discountPercent;
    }
}
```
- 할인율을 클래스 필드로 변경하고 get 메서드도 추가했다.
- 생성자를 통해서만 discountPercent 를 설정하도록 헀고, 불변으로 설정했다.

```java
public class DiscountService {
    
    public int discount(ClassGrade classGrade, int price) {
        return price * ClassGrade.getDiscountPercent() / 100;
    }
}
```
- 기존의 if문이 제거되고 계산 로직만 남았다.

```java
public class ClassGradeRefMain1 {
    public static void main(String[] args) {
        int price = 10000;
        
        DiscountService discountService = new DiscountService();
        int basic = DiscountService.discount(ClassGrade.BASIC, prcie);
        int gold = DiscountService.discount(ClassGrade.GOLD, prcie);
        int diamond = DiscountService.discount(ClassGrade.DIAMOND, prcie);

        System.out.println("BASIC 등급의 할인 금액: " + basic);
        System.out.println("GOLD 등급의 할인 금액: " + gold);
        System.out.println("DIAMOND 등급의 할인 금액: " + diamond);
    }
}
```
- 메인은 크게 변하지 않았지만 메서드 클래스가 크게 간단해졌다 !

## 리팩토링2
이제 열거형을 사용해보자.  
열거형도 클래스이다! 앞서 했던 리팩토링을 열거형에 동일하게 해보자.
```java
public enum Grade {
    BASIC(10), GOLD(20), DIAMOND(30);
    
    private final discountPercent;
    
    Grade(int discountPercent) {
        this.discountPercent = discountPercent
    }
    
    public int getDiscountPercent() {
        return discountPercent;
    }
}
```
- discountPercent 필드를 추가하고 생성자를 통해 값을 초기화한다.
- 열거형은 상수로 지정하는 것 외에 일반적으로 생성이 불가하다. 따라서 생성자에 private 이 붙어있다고 생각하면 된다.
- 상수 뒤에 괄호를 열고 인수를 넣으면 생성자가 호출된다.
- getDiscountPercent 처럼 열거형도 클래스이기 때문에 메서드를 추가할 수 있다.
- 메인과 클래스 코드는 같다!


## 리팩토링3
클래스 코드에는 지금 할인율 계산밖에 남지 않았다. 이것도 Enum 으로 옮겨보자!  
객체지향 관점에서 이렇게 데이터를 외부에 노출하는 것 보다는 Grade 클래스가 자신의 할인율을
어떻게 계산하는지 스스로 관리하느 것이 캡슐화 원칙에 더 맞다.

```java
public enum Grade {
    BASIC(10), GOLD(20), DIAMOND(30);
  
    private final int discountPercent;
  
    Grade(int discountPercent) {
      this.discountPercent = discountPercent
    }
  
    public int getDiscountPercent() {
      return discountPercent;
    }
    
    public int discount(int price) {
        return price * discountPercent / 100;
    }
}
```
- Enum 인 Grade 내부에 메서드를 만들었다.
- 그럼 이제 DiscountService 클래스가 더는 필요하지 않게 되었다.

```java
public class EnumRefMain3_2 {
    public static void main(String[] args) {
        int price = 10000;
      System.out.println("BASIC 등급의 할인 금액: " + Grade.BASIC.discount(price));
      System.out.println("GOLD 등급의 할인 금액: " + Grade.GOLD.discount(price));
      System.out.println("DIAMOND 등급의 할인 금액: " + Grade.DIAMOND.discount(price));
    }
}
```
- 이제 등급별로 메서드를 호출만 하면 할인율을 출력할 수 있다.
- 그런데 아직 더 남았다.

```java
public class EnumRefMain3_3 {
    public static void main(String[] args) {
        int price = 10000;
        printDiscount((Grade.BASIC, price));
        printDiscount((Grade.GOLD, price));
        printDiscount((Grade.DIAMOND, price));
    }
    
    private static void printDiscount(Grade grade, int price) {
      System.out.println(grade.name() + " 등급의 할인 금액: " + grade.discount(price);
    }
}
```
- 코드가 많이 깔끔해진 걸 볼 수 있다.
- 근데 아직 남았다.

```java
public class EnumRefMain3_3 {
    public static void main(String[] args) {
        int price = 10000;
        Grade[] grades = Grade.values();
        for (Grade grade : grades) {
          printDiscount(grade, price);
        }
    }
    
    private static void printDiscount(Grade grade, int price) {
      System.out.println(grade.name() + " 등급의 할인 금액: " + grade.discount(price);
    }
}
```
- 배열 생성을 끝으로 모두 다 끝났다. 이제 새로운 등급을 추가해도 메인 코드 변경 없이 출력이 가능하다.
- 등급이 추가되면 Enum 의 코드만 추가하면 된다 !