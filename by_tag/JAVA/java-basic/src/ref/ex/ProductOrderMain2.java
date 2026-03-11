package ref.ex;

public class ProductOrderMain2 {

    public static void main(String[] args) {
        ProductOrder[] products = new ProductOrder[3];

        products[0] = createOrder("두부", 2000, 2);
        products[1] = createOrder("김치", 5000, 1);
        products[2] = createOrder("콜라", 1500, 2);

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
