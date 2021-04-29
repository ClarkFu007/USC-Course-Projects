import java.util.Scanner;

public class LongestWordLen {
   public static void main(String[] args) {
      String string1 = "What is the longest word";
      int num1 = longestWordLen(string1);
      System.out.println("The longest word in string1 is " + num1 + ".");

      String string2 = "some words";
      int num2 = longestWordLen(string2);
      System.out.println("The longest word in string2 is " + num2 + ".");

      String string3 = "one";
      int num3 = longestWordLen(string3);
      System.out.println("The longest word in string3 is " + num3 + ".");
   }

   private static int longestWordLen(String words) {
      Scanner wordsScanner = new Scanner(words);
      int initialLength = 0;
      return iterateWords(wordsScanner, initialLength);
   }

   private static int iterateWords(Scanner scanner, int length) {
      if (!scanner.hasNext()){
         return length;
      }
      else{
         int currentLength = scanner.next().length();
         if (length < currentLength){
            length = currentLength;
         }
         return iterateWords(scanner, length);
      }
   }
}
