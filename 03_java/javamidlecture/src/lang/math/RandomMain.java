package lang.math;

import java.util.Random;

public class RandomMain {

    public static void main(String[] args) {
        Random random = new Random(1);

        int i = random.nextInt();
        System.out.println("i = " + i);

        double v = random.nextDouble();
        System.out.println("v = " + v);

        boolean b = random.nextBoolean();
        System.out.println("b = " + b);

        int i1 = random.nextInt(10);
        System.out.println("i1 = " + i1);

        int i2 = random.nextInt(10) + 1;
        System.out.println("i2 = " + i2);
    }
}
