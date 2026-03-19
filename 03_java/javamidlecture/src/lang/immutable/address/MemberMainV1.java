package lang.immutable.address;

public class MemberMainV1 {

    public static void main(String[] args) {
        Address address = new Address("서울");

        MemberV1 memberVA = new MemberV1("회원A", address);
        MemberV1 memberVB = new MemberV1("회원B", address);

        // 둘 다 처음 서울
        System.out.println("memberVA = " + memberVA);
        System.out.println("memberVB = " + memberVB);

        // B 주소 변경
//        memberVB.getAddress().setValue("부산");
        System.out.println("부산 -> memberB.address");
        System.out.println("memberVA = " + memberVA);
        System.out.println("memberVB = " + memberVB);


    }
}
