package baekjoon.Java;

import java.io.*;
import java.util.*;

class P15873 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    StringTokenizer st = new StringTokenizer(br.readLine()," ");

    String s = st.nextToken();
    int ans = 0;

    if (s.charAt(1) == '0') {
      ans = 10 + Integer.parseInt(s.substring(2)); 
    } else {
      ans = Integer.parseInt(s.substring(0,1)) + Integer.parseInt(s.substring(1));
    }
    System.out.println(ans);
  }
}
