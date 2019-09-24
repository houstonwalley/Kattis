import java.util.Scanner;

public class Carrots {

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		String line = in.nextLine();
		String[] yeet = line.split(" ");
		int n = Integer.parseInt(yeet[0]);
		int p = Integer.parseInt(yeet[1]);
		String[] lit = new String[n];
		for (int i = 1; i < n + 1; i++) {
			lit[i - 1] = in.nextLine();
		}
		System.out.print(p);
		in.close();
		System.exit(0);;
	}

}
