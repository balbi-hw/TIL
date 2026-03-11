package oop1.ex;

public class AcountMain {

    public static void main(String[] args) {

        Account account = new Account();

        account.balance = account.deposit(10000);
        account.balance = account.withdraw(9000);
        account.balance = account.withdraw(2000);

        System.out.println("잔고: " + account.balance);
    }
}
