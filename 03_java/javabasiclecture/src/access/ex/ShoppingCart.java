package access.ex;

public class ShoppingCart {

    private Item[] items = new Item[10];
    private int itemCount = 0;
    private int totalPrice = 0;

    void addItem(Item item) {
        if (itemCount <= 10) {
            items[itemCount] = item;
            itemCount ++;
        } else {
            System.out.println("장바구니가 가득 찼습니다.");
        }
    }

    void displayItems() {

        for (Item item : items) {
            if (item != null) {
                totalPrice += item.price * item.quantity;
                System.out.println("상품명:"+ item.name + ", 합계:" + totalPrice);
            } else {
                break;
            }
        }

        System.out.println("전체 가격 합:" + totalPrice);
    }

}
