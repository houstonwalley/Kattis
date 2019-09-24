import java.util.Scanner;

public class Sibice {

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		String line = in.nextLine();
		String[] yeet = line.split(" ");
		int n = Integer.parseInt(yeet[0]);
		int w = Integer.parseInt(yeet[1]);
		int h = Integer.parseInt(yeet[2]);
		String result = "";
		for (int i = 0; i < n; i++) {
			int x = in.nextInt();
			if (x <= Math.sqrt(Math.pow(w,  2) + Math.pow(h,  2))) {
				if (result.equals("")) {
					result += "DA";
				}
				else {
					result += "\nDA";
				}
			}
			else {
				if (result.equals("")) {
					result += "NE";
				}
				else {
					result += "\nNE";
				}
			}
		}
		System.out.print(result);
		in.close();
		System.exit(0);
	}

}
