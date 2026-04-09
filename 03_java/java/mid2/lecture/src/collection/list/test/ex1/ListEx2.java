package collection.list.test.ex1;

import java.util.ArrayList;
import java.util.Scanner;

public class ListEx2 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        ArrayList<Integer> numbers = new ArrayList<>();

        System.out.println("n개의 정수를 입력하세요 (종료 0)");
        while (true) {
            int num = sc.nextInt();
            if (num != 0) {
                numbers.add(num);
                sc.nextLine();
            } else {
                for (int i = 0; i < (numbers.size() - 1); i++) {
                    System.out.print(numbers.get(i) + ", ");
                }
                System.out.println(numbers.getLast());
                break;
            }
        }
    }
}
