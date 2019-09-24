import java.util.Scanner;

public class Qaly {

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		String n = in.nextLine();
		int i = Integer.parseInt(n);
		String line;
		double sum = 0;
		int x = 0;
		while (x < i ) {
			line = in.nextLine();
			String[] yeet = line.split(" ");
			double left = Double.parseDouble(yeet[0]);
			double right = Double.parseDouble(yeet[1]);
			sum += (left * right);
			x++;
		}
		
		System.out.print(sum);
		in.close();
		System.exit(0);
	}

}
