package baekjoon.Java;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

class P1284 {
  public static void main(String[] args) throws IOException {
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    while (true){
      String n = bf.readLine();
      int ans = 2;
      if (n.equals("0")) {
        break;
      }else {
        ans += n.length()-1;
        for (int i=0;i<n.length();i++) {
          if (n.charAt(i) == '1') {
            ans += 2;
          } else if (n.charAt(i) == '0') {
            ans += 4;
          } else {
            ans += 3;
          }
        }
      }
      bw.write(ans+"\n");
    }
    bw.flush();
    bw.close();
  }
}
