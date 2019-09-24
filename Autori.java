/**
 *Houston Walley
 *09/04/2019
 *1.2
 *
 *Autori
 */

import java.util.Scanner;

public class Autori {

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		String line = in.nextLine();
		String[] x = line.split("-");
		String result = "";
		for (int i = 0; i < x.length; i++) {
			result += x[i].substring(0,1);
		}
		System.out.print(result);
		in.close();
		System.exit(0);;
	}

}
