package extends1.ex;

public class Item {
    private String name;
    private int price;

    protected Item(String name, int price) {
        this.name = name;
        this.price = price;
    }

    protected void print() {
        System.out.println("이름:" + name + ", 가격:" + price);
    }

    protected int getPrice() {
        return price;
    }
}
