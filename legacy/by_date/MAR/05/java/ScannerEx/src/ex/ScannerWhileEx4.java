package ex;

import java.util.Scanner;

public class ScannerWhileEx4 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int order = 0;
        int sum = 0;


        while (order != 3) {
            System.out.println("1: 상품 입력, 2: 결제, 3: 프로그램 종료");
            order = scanner.nextInt();
            scanner.nextLine();

            if (order == 1) {
                System.out.print("상품명을 입력하세요: ");
                String name = scanner.nextLine();

                System.out.print("상품의 가격을 입력하세요: ");
                int price = scanner.nextInt();
                scanner.nextLine();

                System.out.print("구매 수량을 입력하세요: ");
                int qauntity = scanner.nextInt();
                scanner.nextLine();

                sum += price * qauntity;

                System.out.println("상품명: " + name + " 가격: " + price + " 수량: " + qauntity + " 합계: " + sum);
            } else if (order == 2) {
                System.out.println("총 비용 " + sum);
            } else if (order == 3) {
                sum = 0;
                System.out.println("프로그램을 종료합니다.");
            } else {
                System.out.println("올바른 입력을 입력해주세요.");
                continue;
            }
        }
    }
}
