package lang.wrapper;

public class AutoboxingMain1 {

    public static void main(String[] args) {
        //primitive -> wrapper
        int value = 7;
//        Integer voxedValuew = Integer.valueOf(value);
        Integer boxedValue = value;

//        int unboxedValue = voxedValuew.intValue();
        int unboxedValue = boxedValue;

        System.out.println("unboxedValue = " + unboxedValue);
        System.out.println("boxedValue = " + boxedValue);;
    }
}
