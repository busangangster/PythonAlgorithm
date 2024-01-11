package baekjoon.Java;
import java.util.*;
import java.io.*;

class P5032 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    StringTokenizer st = new StringTokenizer(br.readLine()," ");

    int e = Integer.parseInt(st.nextToken());
    int f = Integer.parseInt(st.nextToken());
    int c = Integer.parseInt(st.nextToken());
    int cnt = 0;
    int glass = e+f;

    while (glass != 0) {
      if (glass == c) {
        cnt += 1;
        break;
      } else if (glass < c) {
        break;
      } else {
        glass -= (c-1);
        cnt += 1;
      }
    }
    System.out.println(cnt);
  }
}
