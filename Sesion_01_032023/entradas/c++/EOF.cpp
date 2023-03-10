#include <bits/stdc++.h>
using namespace std;

int main() {
    int k;
    // leer enteros hasta que se alcance el final de archivo (EOF)
    // se utiliza el operador != para comparar el resultado de scanf con EOF
    while (scanf("%d", &k) != EOF) {
        int ans = 0, v;

        while (k--) {
            scanf("%d", &v);
            ans += v;
        }

        printf("%d\n", ans);
    }

    return 0;
}
