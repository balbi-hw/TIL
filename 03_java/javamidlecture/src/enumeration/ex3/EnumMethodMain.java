package enumeration.ex3;

import java.util.Arrays;

public class EnumMethodMain {

    public static void main(String[] args) {

        Grade[] values = Grade.values();
        System.out.println("values = " + Arrays.toString(values));
    }
}
