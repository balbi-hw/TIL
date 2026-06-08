package lang.immutable.address;

public class MemberMainV2 {

    public static void main(String[] args) {
        ImmutableAddress address = new ImmutableAddress("서울");

        MemberV2 memberVA = new MemberV2("회원A", address);
        MemberV2 memberVB = new MemberV2("회원B", address);

        // 둘 다 처음 서울
        System.out.println("memberVA = " + memberVA);
        System.out.println("memberVB = " + memberVB);

        // B 주소 변경
//        memberVB.getAddress().setvalue(); // 컴파일 오류
        memberVB.setAddress(new ImmutableAddress("부산"));
        System.out.println("memberVA = " + memberVA);
        System.out.println("memberVB = " + memberVB);

    }
}
