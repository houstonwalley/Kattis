import java.util.Scanner;

public class TimeLoop {

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		int time = in.nextInt();
		String result = "";
		for (int i = 1; i <= time; i++) {
			if (i == 1) {
				result += i + " Abracadabra";
			}
			else {
				result += "\n" + i + " Abracadabra";
			}
		}
		System.out.print(result);
		in.close();
		System.exit(0);;
	}

}
