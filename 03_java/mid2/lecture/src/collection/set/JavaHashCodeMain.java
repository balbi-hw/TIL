package collection.set;

import collection.set.member.Member;

public class JavaHashCodeMain {

    public static void main(String[] args) {
        Object obj1 = new Object();
        Object obj2 = new Object();
        System.out.println("obj1 = " + obj1);
        System.out.println("obj2 = " + obj2);

        Integer i = 10;
        String strA = "A";
        String strAB = "AB";

        System.out.println("i.hashCode() = " + i.hashCode());
        System.out.println("strA.hashCode() = " + strA.hashCode());
        System.out.println("strAB.hashCode() = " + strAB.hashCode());

        System.out.println("Integer.valueOf(-1) = " + Integer.valueOf(-1));

        Member member1 = new Member("idA");
        Member member2 = new Member("idA");

        System.out.println("member1 == member2 = " + (member1 == member2));
        System.out.println("member1 equals member2 = " + (member1.equals(member2)));
        System.out.println("member1.hashCode() = " + member1.hashCode());
        System.out.println("member2.hashCode() = " + member2.hashCode());


    }
}
