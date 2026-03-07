package Ex;

import java.util.Scanner;

public class ArrayEx2 {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int times = 0;

        int[] catalogue = new int[10];
        String[] names = new String[10];

        while (times < 11) {

            System.out.println("1. 상품 등록 | 2. 상품 목록 | 3. 종료");
            System.out.print("메뉴를 선택하세요:");
            int numMenu = scanner.nextInt();
            scanner.nextLine();

            if (times == 0) {
                if (numMenu == 2) {
                    System.out.println("등록된 상품이 없습니다.");
                    continue;
                }
            } else if (times == 10) {
                if (numMenu == 1) {
                    System.out.println("더 이상 상품을 등록할 수 없습니다.");
                    continue;
                }
            }

            if (numMenu == 1) {
                System.out.print("상품 이름을 입력하세요:");
                names[times] = scanner.nextLine();
                System.out.print("상품 가격을 입력하세요:");
                catalogue[times] = scanner.nextInt();
                scanner.nextLine();
                times ++;
            } else if (numMenu == 2) {
                for (int i = 0; (names[i] != null); i++) {
                    System.out.println(names[i] + ": " + catalogue[i] + "원");
                }
            } else {
                System.out.println("프로그램을 종료합니다.");
                break;
            }


        }
    }
}
