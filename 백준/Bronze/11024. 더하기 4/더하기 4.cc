#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char s[1000000];

int main() {
    int T;
    scanf("%d", &T);
    getchar();

    int sum = 0;
    for (int i = 0; i < T; i++) {
        sum = 0;
        scanf("%[^\n]s", s);
        getchar();
        int len = strlen(s);
 
        int j = 0;
        while (j < len) {
            if (s[j] == ' ') j++;

            if ('0' <= s[j] && s[j] <= '9')
                sum += atoi(&s[j]);
            while ('0' <= s[j] && s[j] <= '9')
                j++;
        }
 
        printf("%d\n", sum);
    }
    return 0;
}