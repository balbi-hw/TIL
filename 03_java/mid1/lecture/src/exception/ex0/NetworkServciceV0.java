package exception.ex0;

public class NetworkServciceV0 {

    public void sendMessage(String data) {
        String address = "http://exmaple.com";
        NetworkClientV0 client = new NetworkClientV0(address);

        client.connect();
        client.send(data);
        client.disconnect();
    }
}
