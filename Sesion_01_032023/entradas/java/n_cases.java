import java.util.*;
import java.io.*;

class Cases {
    public static void main(String[] args) {

    // Scanner sc = new Scanner(new File("IO_in1.txt")); // lee el archivo especificado
    Scanner sc = new Scanner(System.in);

    int test_cases = Integer.parseInt(sc.nextLine());
    while (test_cases-- > 0) { // seguir leyendo líneas mientras se acaban los casos
        String[] token = sc.nextLine().split(" ");
        int ans = 0;

        for (int i = 0; i < token.length; ++i)
            ans += Integer.parseInt(token[i]);

        System.out.println(ans);
        }
    }
}
