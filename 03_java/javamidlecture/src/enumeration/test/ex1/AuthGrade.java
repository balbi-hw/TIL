package enumeration.test.ex1;

public enum AuthGrade {
    GUEST(1, "손님"), LOGIN(2, "로그인 회원"), ADMIN(3, "관리자");

    private final int level;
    private final String grade;

    AuthGrade(int level, String grade) {
        this.level = level;
        this.grade = grade;
    }

    public int getLevel() {
        return level;
    }

    public String getGrade() {
        return grade;
    }
}
