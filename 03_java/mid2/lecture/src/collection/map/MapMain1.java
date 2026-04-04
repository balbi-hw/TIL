package collection.map;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class MapMain1 {

    public static void main(String[] args) {
        Map<String, Integer> studentMap = new HashMap<>();

        studentMap.put("studentA", 90);
        studentMap.put("studentB", 80);
        studentMap.put("studentC", 70);
        studentMap.put("studentD", 100);
        System.out.println("studentMap = " + studentMap);

        Integer result = studentMap.get("studentD");
        System.out.println("result = " + result);

        Set<String> keySet = studentMap.keySet();
        System.out.println("keySet = " + keySet);
        for (String key : keySet) {
            Integer value = studentMap.get(key);
            System.out.println(key + " : " + value);
        }

        Set<Map.Entry<String, Integer>> entries = studentMap.entrySet();
        for (Map.Entry<String, Integer> entry : entries) {
            String key = entry.getKey();
            Integer value = entry.getValue();
            System.out.println("key = " + key + ", value = " + value);
        }


        Collection<Integer> values = studentMap.values();
        System.out.println("values = " + values);
        for (Integer value : values) {
            System.out.println("value = " + value);
        }

    }
}
