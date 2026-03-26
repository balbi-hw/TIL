package nested.test.ex1;


import java.awt.print.Book;

public class Library {

    private Book[] books;
    private int bookCount;

    public Library(int num) {
        books = new Book[num];
        bookCount = 0;
    }

    public void addBook(String book, String author) {
        if (bookCount < books.length) {
            books[bookCount++] = new Book(book, author);
        } else {
            System.out.println("도서관 저장 공간이 부족합니다.");
        }
    }

    public void showBooks() {
        for (Book book : books) {
            System.out.println("도서 제목: " + book.title + ", 저자: " +
                    book.author);
        }
    }

    private static class Book {
        private String title;
        private String author;

        public Book(String title, String author) {
            this.title = title;
            this.author = author;
        }
    }
}
