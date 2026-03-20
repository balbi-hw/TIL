package lang.clazz;

public class ClassCreateMain {

    public static void main(String[] args) throws Exception {
//        Class helloClass = Hello.class;
        Class helloClass = Class.forName("lang.clazz.Hello");

        Hello object = (Hello) helloClass.getDeclaredConstructor().newInstance();
        String hello = object.hello();
        System.out.println("hello = " + hello);

    }
}
