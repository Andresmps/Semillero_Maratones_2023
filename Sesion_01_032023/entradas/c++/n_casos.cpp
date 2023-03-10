#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b;
    int num_test_cases;

  // leer el número de casos de prueba desde la entrada estándar
    scanf("%d", &num_test_cases);

    // ejecutar cada caso de prueba uno por uno
    while (num_test_cases--) {
        scanf("%d %d", &a, &b);
        printf("%d\n", a + b);
    }

    return 0;
}
