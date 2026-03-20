package lang.wrapper;

public class MyInteger {

    private final int value;

    public MyInteger(int value) {
        this.value = value;
    }

    public int getValue() {
        return value;
    }

//    public int compareTo(int target) {
//        if (value < target) {
//            return -1;
//        } else if (value > target) {
//            return 1;
//        } else {
//            return 0;
//        }
//    }

    public void compareTo(int target) {
        if (value < target) {
            System.out.println(target + "=" + 1);
        } else if (value > target) {
            System.out.println(target + "=" + -1);
        } else {
            System.out.println(target + "=" + 0);
        }
    }

    @Override
    public String toString() {
        return String.valueOf(value);
    }
}
