package generic.test.ex2;

public class Pair<T, T1> {

    private T first;
    private T1 second;

    public void setFirst(T i) {
        this.first = i;
    }

    public void setSecond(T1 data) {
        this.second = data;
    }

    public T getFirst() {
        return first;
    }

    public T1 getSecond() {
        return second;
    }

    @Override
    public String toString() {
        return "Pair{" +
                "first=" + first +
                ", second=" + second +
                '}';
    }
}

