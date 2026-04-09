package collection.list.test.ex2;

import java.util.ArrayList;
import java.util.List;

public class ShoppingCart {

    private List<Item> cart = new ArrayList<>();


    public void addItem(Item item) {
        this.cart.add(item);
    }

    public void displayItems() {
        int total = 0;
        System.out.println("장바구니 상품 출력");
        for (Item item : cart) {
            int price = item.getTotalPrice();
            System.out.println("상품명: " + item.getName() + ", 합계: " + price);

            total += price;
        }
        System.out.println("전체 가격 합: " + total);
    }
}
