import java.util.Scanner;

public class BabyBites {

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		boolean makesSense = true;
		String y = in.nextLine();
		int x = Integer.parseInt(y);
		String line = in.nextLine();
		String[] yeet = line.split(" ");
		
		for (int i = 0; i < yeet.length; i++) {
			if (yeet[i].contentEquals("mumble") || Integer.parseInt(yeet[i]) == i + 1) {
				
			}
			else {
				makesSense = false;
				break;
			}
		}
		
		if (makesSense) {
			System.out.print("makes sense");;
		}
		else {
			System.out.print("something is fishy");
		}
		in.close();
		System.exit(0);

	}

}
