import java.lang.Math;

public class FastExpon {
   public static void main(String[] args) {
      System.out.println(fastExpon(3, 4));
      System.out.println(fastExpon(2, 3));
      System.out.println(fastExpon(2, 12));
      System.out.println(fastExpon(3, 0));
   }

   private static int fastExpon(int x, int n) {
      if (n == 0){
         return 1;
      }
      else if (n == 1){
         return x;
      }
      else if (n % 2 == 0){
         int temp = fastExpon(x, n/2);
         return temp * temp;
      }
      else{
         int temp = fastExpon(x, (n-1)/2);
         return x*temp*temp;
      }
   }
}
