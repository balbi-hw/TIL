package nested.nested;

public class NestedOuterMain {

    public static void main(String[] args) {
        // 제거 가능
        // NestedOuter outer = new NestedOuter();
        NestedOuter.Nested nested = new NestedOuter.Nested();
        nested.print();

        System.out.println("nestedClass = " + nested.getClass());
    }
}
