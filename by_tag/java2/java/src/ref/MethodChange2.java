package ref;

public class MethodChange2 {

    public static void main(String[] args) {
        Data dataA = new Data();
        dataA.value = 10;
        System.out.println("메서드 호출 전: a = " + dataA.value);
        changePrimitive(dataA);
        System.out.println("메서드 호출 후: a = " + dataA.value);

    }

    public static void changePrimitive(Data dataX) {
         dataX.value = 20;
    }
}
