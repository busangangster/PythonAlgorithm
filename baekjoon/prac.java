package baekjoon;
import java.util.Scanner;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    for (int tc=0;tc<t;tc++) {
      int n = sc.nextInt();
      int[] score = new int[101];
      for (int i=0;i<1000;i++) {
        int k = sc.nextInt();
        score[k]++;
      }
      int max_v = 0;
      int ans = 0;
      for (int i=0;i<score.length;i++) {
        if (score[i] >= max_v) {
          max_v = score[i];
          ans = i;
        }
      }
      System.out.println("#"+(tc+1)+" "+ans);
    }
    sc.close();
  }
}