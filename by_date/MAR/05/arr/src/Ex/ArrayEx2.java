package Ex;

import java.util.Scanner;

public class ArrayEx2 {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int[] nums = new int[5];

        System.out.println("5개의 정수를 입력하세요:");
        for (int i = 0; i < 5; i++) {
            nums[i] = scanner.nextInt();
        }

        for (int num : nums) {
            if (num == nums[4]) {
                System.out.println(num);
            } else {
                System.out.print(num + ", ");

            }
        }
    }
}
