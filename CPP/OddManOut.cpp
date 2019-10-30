#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n;
	cin >> n;
	string result = "";
	for (int i = 0; i < n; i++) {
		int g;
		cin >> g;
		vector<int> vec;
		for (int j = 0; j < g; j++) {
			int c;
			cin >> c;
			vec.push_back(c);
			for (int k = 0; k < vec.size() - 1; k++) {
				if (vec[k] == c) {
					vec.erase(vec.begin() + k);
					vec.pop_back();
					break;
				}
			}
		}
	result += "Case #";
	result += to_string(i + 1);
	result +=  ": ";
	result += to_string(vec[0]);
	result += "\n";
	}
	cout << result;
}
