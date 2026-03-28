package nested.test;

public class OuterClass3 {
    public void myMethod() {
        OuterClass3 outerClass3 = new OuterClass3();

        class LocalClass {
            public void hello() {
                System.out.println("LocalClass.hello");
            }
        }

        LocalClass localClass = new LocalClass();
        localClass.hello();
    }
}
