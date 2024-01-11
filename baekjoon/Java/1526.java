package baekjoon.Java;
import java.io.*;

class P1526 {
  	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String s = br.readLine();
		
		while (true) {
			boolean flag = true;
			for (int i=0;i<s.length();i++) {
				if (s.charAt(i) != '4' && s.charAt(i) != '7') {
					flag = false;
					break;
				}
			}
			if (flag == true) {
				break;
			} else { 
				s = String.valueOf(Integer.parseInt(s)-1);
			}

	}
		System.out.println(s);
 }
}
