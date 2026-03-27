# ***NESTED CLASS2***

## 지역 클래스, Local Class
- 지역 클래스는 내부 클래스의 특별한 종류의 하나이다. 따라서 내부 클래스의 특징을 그대로 가진다.  
- 지역 클래스는 지역 변수와 같이 코드 블럭 안에서 정의된다.

```java
class Outer {
    public void process() {
        int localVar = 0;

        class Local {
        }

        Local local = new Local();
    }
}
```
이렇게 지역 클래스는 지역 변수처럼 블럭 안에 클래스를 선언한다.

```java
public class LocalOuterV1 {
    private int outInstanceVar = 3;

    public void process(int paramVar) {

        int localVar = 1;

        class LocalPrinter {
            int value = 0;

            public void printData() {
                System.out.println("value = " + value);
                System.out.println("localVar = " + localVar);
                System.out.println("paramVar = " + paramVar);
                System.out.println("outInstanceVar = " + outInstanceVar);
            }
        }

        LocalPrinter printer = new LocalPrinter();
        printer.printData();
    }

    public static void main(String[] args) {
        LocalOuterV1 localOuter = new LocalOuterV1();
        localOuter.process(2);
    }
}
```
- 자신의 인스턴스 변수 접근 가능
- 자신이 속한 코드 블럭의 로컬 변수 접근 가능
- 속한 블럭의 매개변수 접근 가능 (매개변수도 로컬)
- Outer 의 인스턴스 밸류 접근 가능
  
지역 클래스도 인터페이스를 구현하거나 상속을 받을 수 있다.

```java
public interface Printer {
    void print();
}

public class LocalOuterV2 {
    private int outInstanceVar = 3;

    public void process(int paramVar) {
        int localVar = 1;

        class LocalPrinter implements Printer {
            int value = 0;

            @Override
            public void print() {
                System.out.println("value = " + value);
                System.out.println("localVar = " + localVar);
                System.out.println("paramVar = " + paramVar);
                System.out.println("outInstanceVar = " + outInstanceVar);
            }
        }

        LocalPrinter printer = new LocalPrinter();
        printer.print();
    }

    public static void main(String[] args) {
        LocalOuterV2 localOuter = new LocalOuterV2();
        localOuter.process(2);
    }
}
```

## 지역 변수 캡처1

```java
public class LocalOuterV3 {
    private int outInstanceVar = 3;

    public Printer process(int paramVar) {

        int localVal = 1;

        class LocalPrinter implements Printer {
            int value = 0;

            @Override
            public void print() {
                System.out.println("value = " + value);

                System.out.println("localVal = " + localVal);
                System.out.println("paramVar = " + paramVar);

                System.out.println("outInstanceVar = " + outInstanceVar);
            }
        }

        Printer printer = new LocalPrinter();
        return printer;
    }

    public static void main(String[] args) {
        LocalOuterV3 localOuter = new LocalOuterV3();
        Printer printer = localOuter.process(2);
        
        printer.print();
    }
}
```
로컬을 떠났는데 localVar 이 살아있다.  
로컬밸류를 들고 있는 객체를 반환함으로서 로컬 밖에서 로컬 필드를 들고있는 객체가 탄생했다.  
이런 경우를 객체가 로컬밸류를 **캡처** 했다고 한다.
    
지역 클래스가 접근하는 지역 변수는 절대 중간에 값이 변하면 안된다.  
따라서 `final`로 선언하거나 사실상 `final`이어야 한다.
  
**사실상 final**
영어로는 `effectivelt final`이라고 한다. final 키워드를 넣지 않았지만 실제 final 키워드를
붙인 것 처럼 기능하는 경우를 사실상 final 이라고 한다.
  

## 익명 클래스, Anonymous Class
익명 클래스 또한 지역 클래스의 특별한 한 종류이다. 클래스의 이름이 없다는 특징이 있다.

```java
public class LocalOuterV2 {

    private int outInstanceVar = 3;

    public void process(int paramVar) {

        int localVar = 1;

        class LOcalPrinter implements Printer {

            int value = 0;

            @Override
            public void print() {
                System.out.println("value = " + value);
                System.out.println("localVar = " + localVar);
                System.out.println("paramVar = " + paramVar);
                System.out.println("outInstanceVar = " + outInstanceVar);
            }
        }

        Printer printer = new LocalPrinter();
        printer.print();
    }

    public static void main(String[] args) {
        LocalOuterV2 localOuter = new LocalOuterV2();
        localOuter.process(2);
    }
}
```
위 코드는 지역 클래스를 사용하기 위해 선언과 생성이라는 두 가지 단계를 거친다.
1. 선언: 지역 클래스를 LocalPrinter 라는 이름으로 선언한다. 이 때 인터페이스도 함께 구현한다.
2. 생성: new LocalPrinter() 를 사용해서 앞서 선언한 지역 클래스의 인스턴스를 생성한다.

**익명 클래스**
```java
public class AnonymousOuter {
    
    private int outInstanceVar =3 ;

    public void process(int paramVar) {
        
        int localVar = 1;

        Printer printer = new Printer() {
            int value = 0;

            @Override
            public void print() {
                System.out.println("value = " + value);
                System.out.println("localVar = " + localVar);
                System.out.println("paramVar = " + paramVar);
                System.out.println("outInstanceVar = " + outInstanceVar);
            }
        };
        printer.print();
        System.out.println("printer.Class = " + printer.getClass());
        
    }

    public static void main(String[] args) {
        AnonymousOuter main = new AnonymousOuter();
        main.process(2);
    }
} 
```
위 코드는 익명 클래스를 사용한 클래스로 익명 클래스는 body 를 정의하면서 동시에 생성한다.
**new Printer() {body}**  
`new` 다음에 바로 상속 받으면서 구현 할 부모 타입을 입력하면 된다.  
이 코드는 마치 인터페이스 객체를 생성하는 것 같지만 그건 불가능하다. 인터페이스를 구현한 익명 클래스를
만든 것이다. `Printer`를 상속하면서 즉시 생성하는 것이다.
  
**특징**
- 익명 클래스는 이름 없는 지역 클래스를 선언하면서 동시에 생성한다.
- 익명 클래스는 부모 클래스를 상속 받거나, 인터페이를 구현해야한다. 익명 클래스를 사용하기 위해서는
상위 클래스나 인터페이스가 필요하다.
- 익명 클래스는 말 그대로 이름이 없다. 생성자를 기질 수 없다.

**장점**  
익명 클래스를 사용하면 클래스를 별도로 정의하지 않고도 인터페이스나 추상 클래스를 즉석에서
구현할 수 있어 코드가 더 간결해진다. 하지만 복잡하거나 재사용이 필요한 경우에는 별도의 클래스를 정의하는 게 좋다.
  
**익명클래스를 사용할 수 없는 경우**  
재사용이 불가능하다. 인스턴스가 두 개 이상 필요하면 별도의 클래스를 선언하고 사용해야한다.

## 활용
리팩토링 전
```java
public class Ex0Main {
    public static void helloJava() {
        System.out.println("프로그램 시작");
        System.out.println("Hello Java");
        System.out.println("프로그램 종료");
    }
    
    public static void helloSpring() {
        System.out.println("프로그램 시작");
        System.out.println("Hello Spring");
        System.out.println("프로그램 종료");
    }

    public static void main(String[] args) {
        helloJava();
        helloSpring();
    }
}
```
리팩토링 후

```java
public interface Hello {
    void print();
}

public class Ex1Main {

    public static void hello(Hello hello) {
        System.out.println("프로그램 시작");
        hello.print();
        System.out.println("프로그램 종료");
    }

    static class Java implements Hello {
        @Override
        public void print() {
            System.out.println("Hello java");
        }
    }

    static class Sprint implements Hello {
        @Override
        public void print() {
            System.out.println("Hello spring");
        }
    }

    public static void main(String[] args) {
        Hello java = new Java();
        Hello spring = new Spring();
        
        hello(java);
        hello(spring);
    }
}
```
- 프로그램 시작, 프로그램 종료를 출력하는 부분은 변하지 않는 부분이다.
- 코드 조각을 시작하고 종료하는 부분은 변하는 부분이다.
- 결국 변하는 부분을 외부에서 받아야하는데 이건 문자열 같은 필드를 전달 받는 것과는 다르다.

**어떻게 외부에서 코드를?**
코드는 보통 메서드에 정의하기 떄문에 코드를 넘기려면 메서드를 넘겨야한다. 하지만
메서드를 넘길 방법을 배우지 못했다.  
지금 가능한 건 객체를 생성하고 객체를 넘겨서 메서드를 사용하는 것이다.
  
이번에는 익명 클래스를 사용해보자

```java
public class Ex1RefMainV3 {

    public static void hello(Process process) {
        System.out.println("프로그램 시작");
        process.run();
        System.out.println("프로그램 종료");
    }

    public static void main(String[] args) {
        Process dice = new Process() {
            @Override
            public void run() {
                int randomValue = new Random().nextInt(6) + 1;
                System.out.println("주사위 = " + randomValue);
            }
        };
        
        Process sum = new Process() {
            @Override
            public void run() {
                for (int i = 0; i < 3; i++) {
                    System.out.println("i = " + i);
                }
            }
        };
        
        hello(dice);
        hello(sum);
    }
}
```
이렇게 익명 클래스를 활용하면 코드를 조금 더 짧게 할 수 있다.
  
또는 객체의 참조값을 변수에 담아두지 않고도 가능하다.

```java
public static void main(String[] args) {
    hello(new Process() {
        @Override
        public void run() {
            int randomValue = new Random().nextInt(6) + 1;
            System.out.println("주사위 = " + randomValue);
        }
    });
}
```
또는 람다를 사용해도 된다.

```java
public class Ex1RefMain5 {

    public static void hello(Process process) {
        System.out.println("프로그램 시작");
        process.run();
        System.out.println("프로그램 종료");
    }

    public static void main(String[] args) {
        hello(() -> {
            int randomValue = new Random().nextInt(6) + 1;
            System.out.println("주사위 = " + randomValue);
        });
    }
}
```
이렇게 람다를 활용하면 익명 클래스 같은 클래스 없이 코드 자체만 넘길 수가 있다 !