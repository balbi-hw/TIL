package Array;

public class ArrayDi3 {

    public static void main(String[] args) {
        int[][] arr = new int[4][4];

        int i = 1;
        for (int row = 0; row < arr.length; row++) {
            for (int column = 0; column < arr[row].length; column++) {
                arr[row][column] = i++;
            }
        }

        for (int row = 0; row < arr.length; row++) {
            for (int colum = 0; colum < arr[row].length; colum++) {
                System.out.print(arr[row][colum] + " ");
            }
            System.out.println();
        }
    }
}
