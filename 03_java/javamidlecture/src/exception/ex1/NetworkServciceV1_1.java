package exception.ex1;


public class NetworkServciceV1_1 {

    public void sendMessage(String data) {
        String address = "http://exmaple.com";
        NetworkClientV1 client = new NetworkClientV1(address);
        client.initError(data);

        client.connect();
        client.send(data);
        client.disconnect();
    }
}
