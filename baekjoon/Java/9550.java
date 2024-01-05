package baekjoon.Java;
import java.util.Scanner;

class P9550 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int t  = sc.nextInt();
    for(int i=0;i<t;i++) {
      int n = sc.nextInt();
      int k = sc.nextInt();
      int[] arr = new int[n];
      int ans = 0;
      for(int j=0;j<n;j++) {
        arr[j] = sc.nextInt();
        ans += arr[j]/k;
      }
      System.out.println(ans);
    }
    sc.close();
  }
}
