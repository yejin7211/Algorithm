#include <stdio.h>
int fac(int n) {
    int num = 1;
    while (n >= 1) {
        num *= n;
        n--;
    }
    return num;
}

int main() {
    int test; int N;
    int total = 0; int x; int n;
    scanf("%d", &test);
    for (int i = 0; i < test; i++) {
        scanf("%d", &N);
        total = 0;
        for (int j = N; j >= 0; j--) { //1 의 개수
            x = N - j;
            for (int m = 0; m <= x / 2; m++) {
                for (n = 0; n <= x / 2; n++) {
                    if (m * 2 + n * 3 == x)
                        total += fac(j+m+n) / (fac(j) * fac(m) * fac(n));
                }
            }
        }
        printf("%d\n", total);
    }
    return 0;
}