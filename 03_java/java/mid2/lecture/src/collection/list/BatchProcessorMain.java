package collection.list;

public class BatchProcessorMain {

    public static void main(String[] args) {
        MyArrayList<Integer> list = new MyArrayList<>(); // O(N)
//        MyLinkedList<Integer> list = new MyLinkedList<>(); // O(1)

        BatchProcessor processor = new BatchProcessor(list);
        processor.logic(100_000);

    }
}
