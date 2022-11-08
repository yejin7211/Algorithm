#include <stdio.h>
int N, K;
int A[10];

int main() {
    scanf("%d %d", &N, &K);
    for (int i = 0; i < N; i++)
        scanf("%d", &A[i]);

    int cnt = 0;
    for (int i = N - 1; i >= 0; i--){
        if (K / A[i] != 0) {
            cnt += K / A[i];
            K %= A[i];
            if (K == 0)
                break;
        }
    }
    printf("%d\n", cnt);
    return 0;
}