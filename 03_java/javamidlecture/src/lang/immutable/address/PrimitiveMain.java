package lang.immutable.address;

public class PrimitiveMain {

    public static void main(String[] args) {
        //기본형은 값 공유  x
        int a = 10;
        int b = a;
        System.out.println("a = " + a);
        System.out.println("b = " + b);

        b = 20;
        System.out.println("20 -> b");
        System.out.println("a = " + a);
        System.out.println("b = " + b);

    }
}
