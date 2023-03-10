import java.util.*;
import java.io.*;

class EOF {
  public static void main(String[] args) throws Exception {

    // Scanner sc = new Scanner(new File("IO_in3.txt")); // lee el archivo especificado
    Scanner sc = new Scanner(System.in);

    int c = 0;
    while (sc.hasNext()) { // seguir leyendo líneas mientras haya más
        String[] token = sc.nextLine().split(" ");
        int a = Integer.valueOf(token[0]), b = Integer.valueOf(token[1]);
        if (c > 0) System.out.println();
        System.out.printf("Case %d: %d\n", ++c, a+b);
    }
    }
}
