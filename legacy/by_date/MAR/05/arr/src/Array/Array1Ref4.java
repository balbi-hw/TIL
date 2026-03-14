package Array;

public class Array1Ref4 {

    public static void main(String[] args) {
        int[] students = {90, 80, 70, 60, 50};

//        students[0] = 90;
//        students[1] = 80;
//        students[2] = 70;
//        students[3] = 60;
//        students[4] = 50;

        for (int i = 0; i < students.length; i++) {
            System.out.println("학생" + (i+1) + " 점수: " + students[i]);
        }

//        System.out.println("학생1 점수: " + students[0]);
//        System.out.println("학생2 점수: " + students[1]);
//        System.out.println("학생3 점수: " + students[2]);
//        System.out.println("학생4 점수: " + students[3]);
//        System.out.println("학생5 점수: " + students[4]);
//        System.out.println([I@5b6f7412[1]);
    }
}
