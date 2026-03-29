package generic.ex1;

public class RowTypeMain {

    public static void main(String[] args) {
        GenericBox integerBox = new GenericBox();
        //GenericBox<Object> integerBox = new GenericBox<>();
        integerBox.set(10);
        Integer integer = (Integer) integerBox.get();
        System.out.println("integer = " + integer);
    }
}
