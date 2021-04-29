public class String1UpToN {
   public static void main(String[] args) {
      System.out.println(string1UpToN(3));
      System.out.println(string1UpToN(1));
      System.out.println(string1UpToN(5));
   }

   private static String string1UpToN(int number) {
      return RAppendUpTo("", 1, number);
   }

   private static String RAppendUpTo(String strSoFar, int i, int n) {
      if (i == n){
         if (n == 1){
            return strSoFar + i;
         }
         else{
            return strSoFar + " " + i;
         }
      }
      else{
         if (i == 1){
            strSoFar = strSoFar + i;
         }
         else {
            strSoFar = strSoFar + " " + i;
         }
         return RAppendUpTo(strSoFar, i + 1, n);
      }
   }
}
