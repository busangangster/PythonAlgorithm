package baekjoon.Java;
import java.util.Scanner;

class P25191 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int coke = sc.nextInt();
        int beer = sc.nextInt();
        int cnt = 0;
        while (true) {
            if(coke == 1) {
                break;
            } else if (coke == 0) {
                break;
            } else{
                cnt += 1;
                coke -= 2;
            }
        }
        while (beer != 0) {
            cnt += 1;
            beer -= 1;
        }
        if (cnt <= n) {
            System.out.println(cnt);
        } else {
            System.out.println(n);
        }
        sc.close();
    }
}