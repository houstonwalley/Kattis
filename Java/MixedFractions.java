import java.util.Scanner;

public class MixedFractions {

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		String numer;
		String denom;
		String line = in.nextLine();
		String result = "";
		String[] lit = line.split(" ");
		
		while (!line.contentEquals("0 0"))
		{
			numer = lit[0];
			denom = lit[1];
			int numerI = Integer.parseInt(numer);
			int denomI = Integer.parseInt(denom);
			if (result.equals("")) {
				result += (numerI / denomI) + " " + (numerI % denomI) + " / " + denomI;
			}
			else {
				result += "\n" + (numerI / denomI) + " " + (numerI % denomI) + " / " + denomI;
			}
			line = in.nextLine();
			lit = line.split(" ");
		}
		
		System.out.print(result);
		in.close();
		System.exit(0);
	}

}
