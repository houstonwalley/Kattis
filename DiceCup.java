/**
 *Houston Walley
 *09/05/2019
 *1.2
 *
 *Dice Cup
 */

import java.util.Scanner;
import java.util.HashMap;

public class DiceCup {

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		String diceIn = in.nextLine();
		String[] x = diceIn.split(" ");
		int left = Integer.parseInt(x[0]);
		int right = Integer.parseInt(x[1]);
		int yyy = right;
		int ttt = left;
		
		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
		int high = 0;
		int r = 1;
		while (r <= ttt) {
			int f = 1;
			while (f <= yyy) {
				if (map.containsKey(r + f)) {
					map.put(r + f, map.get(r + f) + 1);
					if (map.get(r + f) > high) {
						high = map.get(r + f);
					}
				}
				else {
					map.put(r + f, 1);
				}
				f++;
			}
			r++;
		}
		Integer[] yeet = new Integer[ttt + yyy - 2];
		int index = 0;
		for (int i = 2; i <= yyy + ttt; i++) {
			if (map.get(i) == high) {
				yeet[index] = i;
				index++;
			}
		}
		String result = "";
		for (int i = 0; i < index; i++) {
			if (result.contentEquals("")) {
				result += yeet[i];
			}
			else {
				result += "\n" + yeet[i];
			}
		}
		System.out.print(result);
		in.close();
		System.exit(0);;
	}

}
