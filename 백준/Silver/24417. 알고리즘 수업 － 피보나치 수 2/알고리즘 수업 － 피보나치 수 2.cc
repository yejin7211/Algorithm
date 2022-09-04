#include <iostream>
using namespace std;
static const int MOD = 1000000007;

int main()
{
    int n, z;
    int x = 1;
    int y = 1;
    cin >> n;
    for (int i = 3; i <= n; i++){
        z = y;
        y = (x + y) % MOD;
        x = z;
    }
    cout << y << ' ' << n-2;
    return 0;
}