package lang.string.test;

public class TestString2 {

    public static void main(String[] args) {
        String[] arr = {"hello", "Java", "jvm", "spring", "jpa"};
    
        int total = 0;
        for (String s : arr) {
            int len = s.length();
            total = total + len;
            System.out.println(s + ":" + s.length());
        }
        System.out.println(total);

    }
}
