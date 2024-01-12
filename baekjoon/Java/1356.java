package baekjoon.Java;
import java.util.*;
import java.io.*;

class P1356 {
  	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Boolean flag = false;
		
		String s = br.readLine();
		if (s.equals("1")) {
			flag = false;
		} else {
			for (int i=0;i<s.length();i++) {
				String first = s.substring(0,i);
				String second = s.substring(i,s.length());
				int front = 1;
				int back = 1;
				for (int j=0;j<first.length();j++) {
					front *= Character.getNumericValue(first.charAt(j));
				}
				for (int t=0;t<second.length();t++) {
					back *= Character.getNumericValue(second.charAt(t));
				}
				
				if (front == back) {
					flag = true;
					break;
				} 		
			}	
		}

		if (flag == true) {
			System.out.println("YES");
		} else {
			System.out.println("NO");
		}
		
	}
  
}
