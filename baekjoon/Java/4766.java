package baekjoon.Java;
import java.util.Scanner;
import java.util.ArrayList;

class P4766 {
  public static void main(String[] args) {
    Scanner sc =  new Scanner(System.in);
    ArrayList<Double> arr = new ArrayList<Double>();
    while (true) {
      double n = sc.nextDouble();
      if (n==999){
        break;
      }else {
        arr.add(n);
      }
    }
    for(int i=1;i<arr.size();i++) {
      String ans = String.format("%.2f",(arr.get(i)-arr.get(i-1)));
      System.out.println(ans);
    }
    sc.close();
  } 
}
