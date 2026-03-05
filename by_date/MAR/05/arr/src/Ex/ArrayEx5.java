package Ex;

import java.util.Scanner;

public class ArrayEx5 {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.print("입력받을 숫자의 개수를 입력하세여: ");
        int number = scanner.nextInt();

        System.out.println(number+ "개의 정수를 입력하세요:");

        int[] numbers = new int[number];

        int total = 0;

        for (int i = 0; i < number; i++) {
            int num = scanner.nextInt();
            total += num;
        }
        double average;
        average = (double) total / numbers.length;

        System.out.println("입력한 정수의 합계: " +total);
        System.out.println("입력한 정수의 평균: " +average);

    }
}
