package generic.ex1;

public class BoxMain3 {

    public static void main(String[] args) {
        GenericBox<Integer> integerBox = new GenericBox<Integer>();
        integerBox.set(10);
        //integerBox.set("23"); // Integer 만 허용, 컴파일 오류
        Integer integer = integerBox.get();
        System.out.println("integer = " + integer);

        GenericBox<String> stringBox = new GenericBox<String>();
        stringBox.set("hello");
//        stringBox.set(10);
        String s = stringBox.get();
        System.out.println("s = " + s);

        GenericBox<Double> doubleBox = new GenericBox<>();
        doubleBox.set(10.5);
        Double v = doubleBox.get();
        System.out.println("v = " + v);

        //타입 추론 :: 생성하는 제너릭 타입 생략 가능
        GenericBox<Integer> integerBox2 = new GenericBox<>();
    }
}
