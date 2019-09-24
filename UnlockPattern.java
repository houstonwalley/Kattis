import java.util.Scanner;


public class UnlockPattern {
	
	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		Integer[] board = new Integer[9];
		int i = 0;
		int index1 = 0;
		int next;
		while (i < 9) {
			next = in.nextInt();
			board[i] = next;
			if (next == 1) {
				index1 = i;
			}
			i++;
		}
		double sum = 0;
		int index2 = 10;
		for (int j = 2; j < 10; j++) {
			boolean found = false;
			int k = 0;
			while (!found) {
				if (board[k] == j) {
					index2 = k;
					found = true;
				}
				k++;
			}
			int x1 = index1 % 3;
			int y1 = index1 / 3;
			int x2 = index2 % 3;
			int y2 = index2 / 3;
			sum += Math.sqrt(Math.pow(Math.abs(x1 - x2), 2) + Math.pow(Math.abs(y1 - y2), 2));
			index1 = index2;
		}
		System.out.print(sum);
		in.close();
		System.exit(0);;
	}

}
