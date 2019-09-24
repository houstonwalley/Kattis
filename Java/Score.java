import java.util.Scanner;
import java.util.HashMap;

public class Score {

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		String line = "";
		HashMap<String, Integer> tot = new HashMap<String, Integer>();
		HashMap<String, Boolean> tf = new HashMap<String, Boolean>();
		String[] lit = new String[9];
		int i = 0;
		int timeSum = 0;
		int correct = 0;
		while (true) {
			line = in.nextLine();
			if (line.equals("-1")) {
				break;
			}
			String[] yeet = line.split(" ");
			int time = Integer.parseInt(yeet[0]);
			String prob = yeet[1];
			String cor = yeet[2];
			if (tot.containsKey(prob)) {
				if (cor.equals("right")) {
					tf.put(prob, true);
					tot.put(prob, tot.get(prob) + time);
					lit[i] = prob;
					i++;
				}
				else {
					tot.put(prob, tot.get(prob) + 20);
				}
			}
			else {
				if (cor.equals("right")) {
					tf.put(prob, true);
					tot.put(prob, time);
					lit[i] = prob;
					i++;
				}
				else {
					tf.put(prob, false);
					tot.put(prob, 20);
				}
			}
		}
		for (int y = 0; y < i; y++) {
			if (tf.get(lit[y]).equals(true)) {
				correct++;
				timeSum += tot.get(lit[y]);
			}
		}
		System.out.print(correct + " " + timeSum);
		in.close();
		System.exit(0);
	}

}
