import java.util.Scanner;

public class Sequence {

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		String line = in.nextLine();
		int k = 0;
		for (int i = 0; i < line.length(); i++) {
			if (line.substring(i, i + 1).equals("?")) {
				k++;
			}
		}
		int res = (int) (Math.pow(2,  k) - 1) % 1000000007;
		System.out.print(res);
		in.close();
		System.exit(0);
	}

}
