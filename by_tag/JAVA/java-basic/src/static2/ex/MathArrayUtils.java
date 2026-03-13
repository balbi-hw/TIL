package static2.ex;

public class MathArrayUtils {

    private MathArrayUtils() {

    }

    public static int sum(int[] values) {
        int total = 0;

        for (int value : values) {
            total += value;
        }

        return total;
    }

    public static double average(int[] values) {

        return (double) sum(values) / values.length;
    }

    public static int min(int[] values) {
        int minimum = 100;
        for (int value : values) {
            if (value < minimum) {
                minimum = value;
            }
        }

        return minimum;
    }

    public static int max(int[] values) {
        int maximum = 0;
        for (int value : values) {
            if (value > maximum) {
                maximum = value;
            }
        }

        return maximum;
    }


}
