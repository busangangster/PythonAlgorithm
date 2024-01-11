package baekjoon.Java;
import java.io.*;

class P23037 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    String s = br.readLine();
    int ans = 0;

    for (int i=0;i<s.length();i++) {
      ans += Math.pow(Character.getNumericValue(s.charAt(i)),5);
    }

    System.out.println(ans);
  }
  
}
