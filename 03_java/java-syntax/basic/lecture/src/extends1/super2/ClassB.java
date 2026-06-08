package extends1.super2;

public class ClassB extends ClassA {

    public ClassB(int a) {
        super(); // 기본 생성자는 생략 가능하다.
        System.out.println("ClassB 생성자 a= "+ a);
    }

    public ClassB(int a, int b) {
        super();
        System.out.println("ClassB 생성자 a= " + a + "b= " + b);
    }

}
