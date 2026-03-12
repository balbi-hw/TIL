package access.ex;

public class MaxCounter {
    private int count;
    private int max;

    public MaxCounter(int max) {
        this.max = max;
    }

    void increment() {
        if (count + 1 <= max) {
            count ++;
        } else {
            System.out.println("최대값을 초과할 수 없습니다.");
        }
    }

    int getCount() {
        return count;
    }
}
