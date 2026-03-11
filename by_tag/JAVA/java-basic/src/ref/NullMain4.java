package ref;

public class NullMain4 {

    public static void main(String[] args) {
        BigData bigData = new BigData();
        bigData.data = new Data();
        System.out.println("bigData.count= " + bigData.count);
        System.out.println("bigData.data= " + bigData.data);

        System.out.println("bigData.data.value=  " + bigData.data.value);

        // nullpointerexception 이 발생하면 null 값에 .(dot) 을 찍었다고 생각하자.
        // dot 은 참조형에 사용하는 메서드 표시인데 참조값이 아닌 곳에 dot 을 찍으면 에러가 발생한다.
        // 그러면 기본형에 dot을 찍으면?

        int a = 10;
//        a.data = new Data();
        // ** java: int cannot be dereferenced ** 에러 발생
        // int 는 참조 불가능하다는 에러 표시
    }
}
