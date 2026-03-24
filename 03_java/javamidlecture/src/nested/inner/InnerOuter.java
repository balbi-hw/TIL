package nested.inner;

public class InnerOuter {

    private static int outClassValue = 3;
    private int outInstanceValue = 2;

    class Inner {
        private int innerInstanceValue = 1;

        public void print() {
            //세 변수 모두 접근 가능
            //클래스에 static 이 붙지 않으면 내부 클래스, 즉 인스턴스 클래스이다.
            System.out.println(innerInstanceValue);
            System.out.println(outInstanceValue);
            System.out.println(outClassValue);
        }
    }
}
