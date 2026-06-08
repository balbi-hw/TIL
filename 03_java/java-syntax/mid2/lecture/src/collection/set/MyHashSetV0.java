package collection.set;

import java.security.PublicKey;
import java.util.Arrays;

public class MyHashSetV0 {

    private int[] elementData = new int[10];
    public int size = 0;

    public boolean add(int value) {
        if (contains(value)) {
            return false;
        }

        elementData[size] = value;
        size++;
        return true;

    }

    public boolean contains(int value) {
        for (int elementDatum : elementData) {
            if (elementDatum == value){
                return true;
            }
        }

        return false;
    }

    public int size() {
        return size;
    }

    @Override
    public String toString() {
        return "MyHashSetV0{" +
                "elementData=" + Arrays.toString(Arrays.copyOf(elementData, size)) +
                ", size=" + size +
                '}';
    }
}
