import java.util.Scanner;

public class SpeedLimit {

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		String line = "";
		String result = "";
		while (true) {
			line = in.nextLine();
			if (line.equals("-1")) {
				break;
			}
			int sum = 0;
			int elap = 0;
			for (int x = 0; x < Integer.parseInt(line); x++) {
				String lit = in.nextLine();
				String[] yeet = lit.split(" ");
				int speed = Integer.parseInt(yeet[0]);
				int time = Integer.parseInt(yeet[1]);
				sum += (speed * (time - elap));
				elap = time;
			}
			if (result.equals("")) {
				result += sum + " miles";
			}
			else {
				result += "\n" + sum + " miles";
			}
		}
		System.out.print(result);
		in.close();
		System.exit(0);
	}

}
