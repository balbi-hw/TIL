package hello.item_service.domain.item;

import lombok.Getter;
import lombok.Setter;

@Getter @Setter
public class Item {

    private Long id;
    private String itemName;

    // 아래 두 값이 Null 이 될 수 있어서 Integer 로 받는다.
    // int 는 기본형이기 때문에 값이 반드시 필요함
    private Integer price;
    private Integer quantity;

    public Item() {
    }

    public Item(String itemName, Integer price, Integer quantity) {
        this.itemName = itemName;
        this.price = price;
        this.quantity = quantity;
    }

}
