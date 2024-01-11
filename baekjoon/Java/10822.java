package baekjoon.Java;
import java.io.*;
import java.util.*;

class P10822 {
  public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine(),",");
		int ans = 0;
		while (st.hasMoreTokens()) {
			ans += Integer.parseInt(st.nextToken());
		}
		System.out.println(ans);
	}
  
}
