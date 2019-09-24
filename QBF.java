import java.util.Scanner;

public class QBF {

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		String[] alf = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"};
		String rep = in.nextLine();
		int i = 0;
		String fin = "";
		while (i < Integer.parseInt(rep)) {
			String result = "";
			String line = in.nextLine();
			line = line.toLowerCase();
			for (String s: alf) {
				if (line.contains(s)) {
					
				}
				else {
					result += s;
				}
			}
			if (result.contentEquals("")) {
				fin += "pangram\n";
			}
			else {
				fin += "missing " + result + "\n";
			}
			i++;
		}
		System.out.print(fin);
		in.close();
		System.exit(0);;
	}

}
