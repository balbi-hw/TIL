package poly.basic;

public class CastingMain6 {

    public static void main(String[] args) {
        Parent parent1 = new Parent();
        System.out.println("1");
        call(parent1);

        Parent parent2 = new Child();
        System.out.println("2");
        call(parent2);



    }

    private static void call(Parent parent) {
        parent.parentMethod();
        if (parent instanceof Child child) {
            System.out.println("Child");
            child.childMethod();
        }
    }
}
