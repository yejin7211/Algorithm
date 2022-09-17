#include <iostream>
int s[50001];

int main() {
	int n, k;
	std::cin >> n >> k;

	for (int i = 1; i <= n; i++) 
		std::cin >> s[i];

	int max_even_cnt = 0;
	for (int i = 1; i <= n; i++) {
		if (s[i] % 2 == 0) {
			int even_cnt = 0;
			int jump_able = 0;
			for (int j = i; j <= n; j++) {
				if (s[j] % 2 == 0) 
					even_cnt++;
				else {
					if (jump_able < k)
						jump_able++;
					else break;
				}
			}
			max_even_cnt = max_even_cnt > even_cnt ?
				max_even_cnt : even_cnt;
		}
	}

	std::cout << max_even_cnt;

	return 0;
}