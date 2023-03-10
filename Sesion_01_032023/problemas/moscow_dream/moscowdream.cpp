#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b, c, n; scanf("%d %d %d %d", &a, &b, &c, &n);
  string  _answer = (
    (a >= 1) && (b >= 1) && (c >= 1) &&
    (a+b+c >= n) &&
    (n >= 3)) ? "YES\n" : "NO\n";

  printf("%s", _answer.c_str());                      // operador ternario
  return 0;
}
