package collection.map;

import java.util.HashMap;

public class MapMain3 {

    public static void main(String[] args) {
        HashMap<Object, Object> studentMap = new HashMap<>();

        studentMap.put("studentA", 50);
        System.out.println(studentMap);

        if (!studentMap.containsKey("studentA")) {
            studentMap.put("studentA", 100);
        }
        System.out.println("studentMap = " + studentMap);

        studentMap.putIfAbsent("studentA", 100);
        studentMap.putIfAbsent("studentB", 100);
        System.out.println("studentMap = " + studentMap);
    }
}
