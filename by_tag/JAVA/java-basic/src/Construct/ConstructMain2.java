package Construct;

public class ConstructMain2 {
    public static void main(String[] args) {
        MemberConstruct member1 = new MemberConstruct("user1", 16, 90);
        MemberConstruct member2 = new MemberConstruct("user2", 18);

        MemberConstruct[] member = {member1, member2};

        for (MemberConstruct s : member) {
            System.out.println("이름: " + s.name + " 나이 :" + s.age + " 성적: " + s.grade);
        }
    }
}
