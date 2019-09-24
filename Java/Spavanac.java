import java.util.Scanner;

public class Spavanac {

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		String nums = in.nextLine();
		String[] yeet = nums.split(" ");
		int hour = Integer.parseInt(yeet[0]);
		int min = Integer.parseInt(yeet[1]);
		if (min >= 45) {
			System.out.print(hour + " " + (min - 45));
		}
		else {
			if (hour == 0) {
				System.out.print("23 " + ((min - 45) + 60));
			}
			else {
				System.out.print((hour - 1) + " " + ((min - 45) + 60));
			}
		}
		in.close();
		System.exit(0);
	}

}
