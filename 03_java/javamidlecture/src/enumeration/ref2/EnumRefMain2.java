package enumeration.ref2;

public class EnumRefMain2 {

    public static void main(String[] args) {
        int price = 10000;

        Grade[] values = Grade.values();
        for (Grade value : values) {
            printDiscount(value, price);
        }
    }

    private static void printDiscount(Grade grade, int price) {
        System.out.println(grade.name() + " 등급의 할인 금액: " + grade.discount(price));
    }
}
