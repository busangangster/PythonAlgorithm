package  baekjoon.Java;
import java.util.*;
import java.io.*;

class P5363 {
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    int n = Integer.parseInt(br.readLine());

    StringBuilder sb = new StringBuilder();

    for (int i=0;i<n;i++) {
      String[] arr = br.readLine().split(" ");
      for(int j=2;j<arr.length;j++) {
        sb.append(arr[j]).append(" ");
      }
      sb.append(arr[0]).append(" ").append(arr[1]);
      sb.append("\n");
    }
   
    System.out.print(sb);
  }
}
