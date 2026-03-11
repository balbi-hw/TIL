package Class.Ex1;

public class MovieReviewMain1 {

    public static void main(String[] args) {
        MovieReview inception = new MovieReview();

        inception.title = "인셉션";
        inception.review = "it was good";

        MovieReview abouttime = new MovieReview();

        abouttime.title = "어바웃타임";
        abouttime.review = "good too";

        System.out.println(inception.review + " " +  inception.title);
        System.out.println(abouttime.review + " " +  abouttime.title);
    }
}
