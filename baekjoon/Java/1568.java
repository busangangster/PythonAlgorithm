package baekjoon.Java;
import java.io.*;

class P1568 {
  public static void main(String[] args) throws IOException{

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int n = Integer.parseInt(br.readLine());
    int k = 1;
    int ans = 0;

    while (n != 0) {
      if (k > n) {
        k = 1;
      } else {
        n -= k;
        k += 1;
        ans += 1;
      }
    }
    System.out.println(ans);
  }
}