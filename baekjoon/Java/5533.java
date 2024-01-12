package baekjoon.Java;
import java.util.*;
import java.io.*;

class P5533 {
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int n = Integer.parseInt(br.readLine());
    int [][] arr = new int[n][3];
    int [] score = new int[n];

    for (int i=0;i<n;i++) {
      StringTokenizer st = new StringTokenizer(br.readLine()," ");
      for (int j=0;j<3;j++) {
        arr[i][j]= Integer.parseInt(st.nextToken());
      }
    }
    int sum = 0;
      for (int j=0;j<3;j++) {
        for (int i=0;i<n;i++){
          for (int z=0;z<n;z++) {
            if (i == z) {
              continue;
            }
            if (arr[i][j] != arr[z][j]) {
              sum = arr[i][j];
            } else {
              sum = 0;
              break;
            }
          }
          score[i] += sum;
          sum = 0;
          
        }
      }
      for (int i=0;i<n;i++) {
        System.out.println(score[i]);
      }
  }
  
}
