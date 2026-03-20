package enumeration.ref1;

import static enumeration.ex3.Grade.*;

public class DiscountService {

    public int discount(ClassGrade classGrade, int price) {
        return price * classGrade.getDiscountPercent() / 100;
    }
}
