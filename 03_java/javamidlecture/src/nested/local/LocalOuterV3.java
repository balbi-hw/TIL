package nested.local;

import java.lang.reflect.Field;

public class LocalOuterV3 {

    private int outInstanceVar = 3;


    public Printer process(int paramVar) {

        int localVar = 1;

        class LocalPrinter implements Printer {
            int value = 0;

            @Override
            public void print() {
                System.out.println("value = " + value);
                System.out.println("localVar = " + localVar);
                System.out.println("paramVar=" + paramVar);
                System.out.println("outInstanceVar = " + outInstanceVar);
            }

        }

        LocalPrinter localPrinter = new LocalPrinter();
//        localPrinter.print();
        return localPrinter;
    }

    public static void main(String[] args) {
        LocalOuterV3 localOuterV1 = new LocalOuterV3();
        Printer process = localOuterV1.process(2);
        process.print();

        System.out.println("필드 확인?");
        Field[] declaredFields = process.getClass().getDeclaredFields();
        for (Field declaredField : declaredFields) {
            System.out.println("declaredField = " + declaredField);
        }
    }
}
