import java.util.Scanner;

public class TakeTwoStones {

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		int numStones = in.nextInt();
		int rem = numStones % 2;
		if (rem == 1) {
			System.out.print("Alice");
		}
		else {
			System.out.print("Bob");
		}
		in.close();
		System.exit(0);;
	}

}
