package exception.ex1;

import java.util.Scanner;

public class NetworkMainV1 {

    public static void main(String[] args) {
        //NetworkServciceV1_1 networkService = new NetworkServciceV1_1();
        //NetworkServciceV1_2 networkService = new NetworkServciceV1_2();
        NetworkServciceV1_3 networkService = new NetworkServciceV1_3();

        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("전송할 문자: ");
            String input = scanner.nextLine();
            if (input.equals("exit")) {
                break;
            }
            networkService.sendMessage(input);
            System.out.println();
        }
        System.out.println("프로그램을 정상 종료합니다.");
    }
}
