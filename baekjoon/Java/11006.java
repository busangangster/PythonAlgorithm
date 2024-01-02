package baekjoon.Java;
import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    for (int i=0;i<n;i++) {
      int num1 = sc.nextInt();
      int num2 = sc.nextInt();
      int k = 2*num2;
      int result = k-num1;
      System.out.println(result+" "+(num2-result));
    }
    sc.close();
  }
}