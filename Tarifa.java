import java.util.Scanner;

public class Tarifa {

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		int x = in.nextInt();
		int y;
		int i = 0;
		int n = in.nextInt();
		int sum = x;
		while (i < n) {
			y = in.nextInt();
			sum += (x - y);
			i++;
		}

		System.out.print(sum);
		in.close();
		System.exit(0);
	}

}
