package collection.map;

import java.util.HashMap;

public class MapMain2 {

    public static void main(String[] args) {
        HashMap<Object, Object> studentMap = new HashMap<>();

        studentMap.put("studentA", 80);
        System.out.println(studentMap);

        studentMap.put("studentA", 100);
        System.out.println(studentMap);

        boolean studentA = studentMap.containsKey("studentA");
        System.out.println("studentA = " + studentA);

        studentMap.remove("studentA");
        System.out.println("studentMap = " + studentMap);
    }
}
