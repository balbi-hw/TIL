package poly.ex.sender;

public class SmsSender implements Sender {

    @Override
    public void sendMessage(String greet) {
        System.out.println("SMS를 발송합니다: " + greet);
    }
}
