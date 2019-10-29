#include <iostream>
using namespace std;

int main() {
	int n, h, v;
	cin >> n >> h >> v;
	int top_l = (h * v);
	int top_r = (h * (n - v));
	int bot_l = ((n - h) * v);
	int bot_r = ((n - h) * (n - v));
	if (top_l >= top_r && top_l >= bot_r && top_l >= bot_l) {
		cout << top_l * 4;
	}
	else if (top_r >= top_l && top_r >= bot_r && top_r >= bot_l) {
		cout << top_r * 4;
	}
	else if (bot_r >= top_r && top_l <= bot_r && bot_r >= bot_l) {
		cout << bot_r * 4;
	}
	else {
		cout << bot_l * 4;
	}
	return 0;
}
