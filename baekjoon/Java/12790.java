package baekjoon.Java;
import java.io.IOException;
import java.util.Scanner;

class P12790 {
	public static void main(String[] args) throws IOException{
	    Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();
		for (int i=0;i<t;i++) {
		    int ans = 0;
		    int[] arr = new int[8];
		    for (int j=0;j<8;j++) {
		        arr[j] = sc.nextInt();
		    }
		  int HP = arr[0]+arr[4];
		  int MP = arr[1]+arr[5];
		  int attack = arr[2]+arr[6];
		  int defense = arr[3]+arr[7];
		  if (HP < 1) {
		      HP = 1;
		  }
		  if (MP < 1) {
		      MP = 1;
		  }
		  if (attack <0) {
		      attack = 0;
		  }
		  ans = ((1*HP)+(5*MP)+(2*attack)+(2*defense));
		  System.out.println(ans);
		}
    sc.close();
	}
}