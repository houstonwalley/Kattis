#include <stdio.h>

int main() {

	int n = 0;
	scanf("%d", &n);
	int arr[n];
	int first;
	if (n == 0) {
		printf("0");
		return 0;
	}
	scanf("%d", &first);
	int min = first;
	int day = 0;
	int i = 1;
	int temp;
	while (i < n) {
		scanf("%d", &temp);
		if (temp < min) {
			day = i;
			min = temp;
		}
		i += 1;
	}
	printf("%d", day);
	return 0;

}
