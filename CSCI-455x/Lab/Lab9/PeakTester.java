/* 
 * Contains hasOnePeak method and
 * tests it on a bunch of hardcoded test cases, printing out test
 * data, actual results, and a FAILED message if actual results don't
 * match expected results.
 */

import java.util.LinkedList;
import java.util.ListIterator;
import java.util.Scanner;

public class PeakTester {


   /*
    * see lab assignment for specification of hasOnePeak method.
    */
   public static boolean hasOnePeak(LinkedList<Integer> list) {
      if (list.size() == 0 || list.size() == 1 || list.size() ==2){
         return false;
      }
      int pastValue = 0;
      int peakNum = 0;
      boolean isFirst = true;
      boolean isSecond = true;
      boolean increaseMode = true;
      boolean decreaseMode = false;

      ListIterator<Integer> listIter = list.listIterator();
      while (listIter.hasNext()){
         if (isFirst){
            pastValue = listIter.next();
            isFirst = false;
         }
         else
         {
            int currentValue = listIter.next();
            if (increaseMode && currentValue < pastValue){
               if (isSecond){  // There is no increasing part.
                  return false;
               }
               peakNum++; // We have found one peak.
            }
            isSecond = false;
            if (decreaseMode && currentValue > pastValue){ // There might be another peak.
               return false;
            }
            if (currentValue > pastValue){
               increaseMode = true;
               decreaseMode = false;
            }
            else{
               increaseMode = false;
               decreaseMode = true;
            }
            pastValue = currentValue;
         }
      }
      return peakNum == 1;
   }


   public static void main(String[] args) {

      testPeak("", false);
      testPeak("3", false);
      testPeak("3 4", false);
      testPeak("4 2", false);
      testPeak("3 4 5", false);
      testPeak("5 4 3", false);
      testPeak("3 4 5 3", true);
      testPeak("3 4 5 3 2", true);
      testPeak("3 7 9 11 8 4 3 1", true);
      testPeak("3 5 4", true);
      testPeak("4 3 5", false);
      testPeak("2 4 3 5", false);
      testPeak("5 2 4 3 5", false);
      testPeak("5 2 4 3", false);
      testPeak("2 4 3 5 2", false);  // 2 peaks
   }

    
    
   /*  Assumes the following format for listString parameter, shown by example
    * (first one is empty list):
    *   "", "3", "3 4", "3 4 5", etc.
    */
   private static LinkedList<Integer> makeList(String listString) {
      Scanner strscan = new Scanner(listString);

      LinkedList<Integer> list = new LinkedList<Integer>();

      while (strscan.hasNextInt()) {
         list.add(strscan.nextInt());
      }

      return list;
   }


   /* Test hasOnePeak method on a list form of input given in listString
    * Prints test data, result, and whether result matched expectedResult
    *
    * listString is a string form of a list given as a space separated
    * sequence of ints.  E.g.,
    *  "" (empty string), "3" (1-element string), "2 4" (2-element string), etc.
    *
    */
   private static void testPeak(String listString, boolean expectedResult) {

      LinkedList<Integer> list = makeList(listString);

      boolean result = hasOnePeak(list);
      System.out.print("List: " + list
                       + " hasOnePeak? " + result);
      if (result != expectedResult) {
         System.out.print("...hasOnePeak FAILED");
      }
      System.out.println();
   }
}
