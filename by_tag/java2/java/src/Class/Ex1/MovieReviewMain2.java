package Class.Ex1;

public class MovieReviewMain2 {

    public static void main(String[] args) {
        MovieReview inception = new MovieReview();

        inception.title = "인셉션";
        inception.review = "it was good";

        MovieReview abouttime = new MovieReview();

        abouttime.title = "어바웃타임";
        abouttime.review = "good too";

        MovieReview[] movies = new MovieReview[2];
        movies[0] = inception;
        movies[1] = abouttime;

        for (MovieReview movie : movies) {
            MovieReview m = movie;
            System.out.println(m.review + " " +  m.title);
        }

    }
}
