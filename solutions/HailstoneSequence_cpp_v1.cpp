#include <bits/stdc++.h>
using namespace std;

int HailstoneNumbers(int N){
    static int c;
    cout << N << " ";
    if (N == 1 && c == 0) {
        return c;
    }
    else if (N == 1 && c != 0) {
        c++;
        return c;
    }
    else if (N % 2 == 0) {
        c++;
        HailstoneNumbers(N / 2);
    }
    else if (N % 2 != 0) {
        c++;
        HailstoneNumbers(3 * N + 1);
    }
}

int main(){
    int N = 7;
    int x;
    x = HailstoneNumbers(N);
    cout << endl;
    cout << "Number of Steps: " << x;
    return 0;
}
