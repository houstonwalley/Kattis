#include <stdio.h>

int main() {

	int n = 0;
	scanf("%d", &n);
	while (1) {
		int temp = n;
		int i = 0;
		while (temp > 0) {
			i += temp % 10;
			temp /= 10;
		}
		if (n % i == 0) {
			printf("%d", n);
			return 0;
		}
		n += 1;
	}
	return 0;

}
