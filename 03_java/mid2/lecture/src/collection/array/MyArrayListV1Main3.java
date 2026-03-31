package collection.array;

public class MyArrayListV1Main3 {

    public static void main(String[] args) {
        MyArrayListV3 list = new MyArrayListV3(2);
        System.out.println("==데이터 추가==");
        list.add("a");
        list.add("b");
        list.add("c");
        System.out.println(list);

        System.out.println("addLast");
        list.add(3, "addList");
        System.out.println(list);

        System.out.println("addFirst");
        list.add(0, "addFirst");
        System.out.println(list);

        Object delete = list.delete(4);
        System.out.println("delete(4) = " + delete);
        System.out.println(list);

    }
}
