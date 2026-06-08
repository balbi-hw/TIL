package poly.ex.pay0;

import java.util.Scanner;

public class PayMain1 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        PayService payService = new PayService();

        while (true) {
            System.out.print("결제 수단을 입력해주세요('종료' 입력 시 프로그램 종료): ");
            String payOption = scanner.nextLine();
            if (payOption.equals("종료")) {
                System.out.println("프로그램을 종료합니다.");
                break;
            }
            System.out.print("금액을 입력해주세요: ");
            int amount = scanner.nextInt();
            scanner.nextLine();
            payService.processPay(payOption, amount);
        }
    }
}
