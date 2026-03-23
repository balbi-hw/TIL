package time.test;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;

public class TestLoopPlus {

    public static void main(String[] args) {
        LocalDate ldt = LocalDate.of(2024, 1, 1);
        for (int i = 0; i < 5; i++) {
            LocalDate plus = ldt.plus(2 * i, ChronoUnit.WEEKS);
            System.out.println("날짜 " + (i+1) + ": " + plus);
        }
    }
}
