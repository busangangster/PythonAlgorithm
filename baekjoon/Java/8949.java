package baekjoon.Java;
import java.util.*;
import java.io.*;

class P8949 {
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    StringTokenizer st = new StringTokenizer(br.readLine());

    StringBuilder sb = new StringBuilder();
    String a = st.nextToken();
    String b = st.nextToken();

    if (a.length() == b.length()) {
      for (int i=0;i<a.length();i++) {
        sb.append(a.charAt(i)-'0'+b.charAt(i)-'0');
      }
    } else if (a.length() > b.length()) {
      int t = a.length()-b.length();
      for (int i=0;i<t;i++) {
        sb.append(a.charAt(i)-'0');
      }
      for (int i=0;i<b.length();i++) {
        sb.append(b.charAt(i)-'0'+a.charAt(i+t)-'0');
      }
    } else if (b.length() > a.length()) {
      int p = b.length()-a.length();
      for (int i=0;i<p;i++) {
        sb.append(b.charAt(i)-'0');
      }
      for (int i=0;i<a.length();i++) {
        sb.append(a.charAt(i)-'0'+b.charAt(i+p)-'0');
      }
    }
    System.out.println(sb);
    sb.setLength(0);

  }
  
}


