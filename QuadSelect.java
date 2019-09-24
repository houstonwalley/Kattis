import java.util.Scanner;

public class QuadSelect {

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		int x = in.nextInt();
		int y = in.nextInt();
		if (x > 0 && y > 0) {
			System.out.print(1);
		}
		if (x < 0 && y > 0) {
			System.out.print(2);
		}
		if (x < 0 && y < 0) {
			System.out.print(3);
		}
		if (x > 0 && y < 0) {
			System.out.print(4);
		}
		in.close();
		System.exit(0);;
	}

}
