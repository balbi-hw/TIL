package lang.string.test;

public class TestString10 {

    public static void main(String[] args) {
        String fruits = "apple,banana,mango";

        String[] lst = fruits.split(",");
        for (String s : lst) {
            System.out.println(s);
        }
        String result = String.join("->", lst);
        System.out.println(result);

        }
    }

