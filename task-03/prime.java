import java.util.Scanner;

public class prime{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter the limit n: ");
        int n = scan.nextInt();
	System.out.println();

        for (int i = 2; i <= n; i++) {
            int c = 0;
            for (int j = 1; j <= i; j++) {
                if (i % j == 0) {
                    c++;
                }
            }

            if (c == 2) {
                System.out.println(i + " ");
            }
        }
    }
}
