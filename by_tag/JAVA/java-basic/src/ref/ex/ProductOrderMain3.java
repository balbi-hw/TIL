package ref.ex;

import java.util.Scanner;

public class ProductOrderMain3 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("입력할 주문의 개수를 입력하세요: ");
        int num = scanner.nextInt();
        scanner.nextLine();

        ProductOrder[] products = new ProductOrder[num];

        for (int i = 0; i < products.length; i++) {
            products[i] = new ProductOrder();

            System.out.println((i + 1) + "번째 주문 정보를 입력하세요.");
            System.out.print("상품명: ");
            products[i].productName = scanner.nextLine();

            System.out.print("가격: ");
            products[i].price = scanner.nextInt();

            System.out.print("수량: ");
            products[i].quantity = scanner.nextInt();
            scanner.nextLine();
        }

        int total = 0;
        for (ProductOrder product : products) {
            printOrder(product);
            total += getTotalAmount(product, total);
        }
        System.out.println("총 결제 금액: " + total);

    }

    static ProductOrder createOrder(String productName, int price, int quantity) {
        ProductOrder product = new ProductOrder();
        product.productName = productName;
        product.price = price;
        product.quantity = quantity;
        return product;
    }

    static void printOrder(ProductOrder product) {
        System.out.println("상품명: " + product.productName + ", 가격: " + product.price + ", 수량: " + product.quantity);
    }

    static int getTotalAmount(ProductOrder product, int total) {
        return product.price * product.quantity;
    }

}
