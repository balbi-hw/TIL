package nested.anonymous.ex;

import java.util.Random;

public class Ex1RefMainV5 {

    public static void hello(Process clazz) {
        System.out.println("프로그램 시작");

        clazz.run();

        System.out.println("프로그램 시작");
    }

    public static void main(String[] args) {

        new Process() {
            @Override
            public void run() {
                for (int i = 0; i < 3; i++) {
                    System.out.println("i = " + i);
                }
            }
        };

        hello(() -> {
            int randomValue = new Random().nextInt(6) + 1;
            System.out.println("주사위 = " + randomValue);
        });
        hello(() -> {
            for (int i = 0; i < 3; i++) {
                System.out.println("i = " + i);
            }
        });
        hello(() -> {
            for (int i = 0; i < 5; i++) {
                System.out.println("i = " + i);
            }
        });
    }
}
