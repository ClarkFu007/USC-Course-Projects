// Name: Yao Fu
// USC NetID: yaof
// CS 455 PA4
// Spring 2021


import java.util.ArrayList;


/**
 * A test file to test the Rack class.
 */

public class RackTester {
   public static void main(String[] args) {
      String rackString = "abc";
      Rack myRack = new Rack(rackString, 0);
      ArrayList<String> allSubsetList = myRack.getAllSubsetList();
      for (String s : allSubsetList) {
         System.out.println(s);
      }
      System.out.println();

   }
}
