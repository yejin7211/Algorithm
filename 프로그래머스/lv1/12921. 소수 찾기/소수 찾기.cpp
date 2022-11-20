#include <vector>

using namespace std;

int isPrime(int n) {
    for (int i = 2; i * i <= n; i++)
        if (n % i == 0)
            return 0;
    return 1;
}

int solution(int n) {
    int answer = 0;
    for (int i = 2; i <= n; i++)
        if (isPrime(i))
            answer++;
    return answer;
}