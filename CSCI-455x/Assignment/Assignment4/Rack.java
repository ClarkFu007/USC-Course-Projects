// Name: Yao Fu
// USC NetID: yaof
// CS 455 PA4
// Spring 2021

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;

/**
 * A Rack of Scrabble tiles
 */
public class Rack {
   private ArrayList<String> allSubsetList;

   /**
    * Creates an Rack that can help get all of its subsets.
    *
    * Representation invariants:
    * 1: the information of the rack string should only contain English words.
    * 2: 0 <= starPos < uniqueLetters.length().
    *
    * @param inString  the string containing letters of the rack in the game.
    * @param starPos  the starting position to get subsets in the "AllSubset" function.
    */
   public Rack(String inString, int starPos){
      RackInfor rackInfor = new RackInfor(inString);          // Creat a RackInfor object
      String uniqueLetters = rackInfor.getUniqueLetters();    // Get all unique letters of the rack
      int[] letterMultiArray = rackInfor.getMultiOfLetters(); // Get multiplicity od each unique letter

      this.allSubsetList = new ArrayList<String>(
            Rack.allSubsets(uniqueLetters, letterMultiArray, starPos));
   }

   /**
    * Gets all subsets of the multiset.
    *
    * @return the allSubsetList.
    */
   public ArrayList<String> getAllSubsetList(){
      return new ArrayList<String>(this.allSubsetList);
   }

   /**
    * Finds all subsets of the multiset starting at position k in unique and mult.
    * unique and mult describe a multiset such that mult[i] is the multiplicity of the char
    *      unique.charAt(i).
    *
    * PRE: mult.length must be at least as big as unique.length() 0 <= k <= unique.length()
    * @param unique a string of unique letters
    * @param mult the multiplicity of each letter from unique.
    * @param k the smallest index of unique and mult to consider.
    * @return all subsets of the indicated multiset. Unlike the multiset in the parameters,
    * each subset is represented as a String that can have repeated characters in it.
    * @author Claire Bono
    */
   private static ArrayList<String> allSubsets(String unique, int[] mult, int k) {
      ArrayList<String> allCombos = new ArrayList<>();
      
      if (k == unique.length()) {  // multiset is empty
         allCombos.add("");
         return allCombos;
      }
      
      // get all subsets of the multiset without the first unique char
      ArrayList<String> restCombos = allSubsets(unique, mult, k+1);
      
      // prepend all possible numbers of the first char (i.e., the one at position k) 
      // to the front of each string in restCombos.  Suppose that char is 'a'...
      
      String firstPart = "";          // in outer loop firstPart takes on the values: "", "a", "aa", ...
      for (int n = 0; n <= mult[k]; n++) {   
         for (int i = 0; i < restCombos.size(); i++) {  // for each of the subsets 
                                                        // we found in the recursive call
            // create and add a new string with n 'a's in front of that subset
            allCombos.add(firstPart + restCombos.get(i));  
         }
         firstPart += unique.charAt(k);  // append another instance of 'a' to the first part
      }
      
      return allCombos;
   }
}

/**
 * The class to collect the information of rack (unique letters of rack and
 * multiplicity of every unique letter).
 */
class RackInfor {
   private String rackString;
   private String uniqueLetters;
   private int uniqueNum = 0;
   private int[] letterMultiArray;

   /**
    * Creates an RackInFor that can store the information of
    * the rack string in order to help get all of its subset..
    *
    * Representation invariants:
    * the information of the rack string should only contain English words.
    *
    * @param rackString  the string containing letters of the rack in the game.
    */
   public RackInfor(String rackString){
      this.rackString = rackString;
      this.uniqueLetters = getUniqueLettersHelper(this.rackString);
      this.uniqueNum = getNumOfUniqueLetters();
      this.letterMultiArray = getMultiOfLettersHelper();
   }


   /**
    * Gets the string of unique letters of a given rack.
    *
    * @return the string of unique letters of a given rack.
    */
   public String getUniqueLetters(){
      return this.uniqueLetters;
   }


   /**
    * Gets the number of unique letters of a given rack.
    *
    * @return the number of unique letters of a given rack.
    */
   public int getNumOfUniqueLetters(){
      return this.uniqueLetters.length();
   }

   /**
    * Gets the multiplicity of every unique letter of a given rack.
    *
    * @return an array to store multiplicity of every unique letter of a given rack.
    */
   public int[] getMultiOfLetters() {
      return Arrays.copyOf(this.letterMultiArray, this.uniqueNum);
   }

   /**
    * Gets the string of unique letters of a given rack.
    *
    * @param inString a string of the given rack.
    * @return the string of unique letters of a given rack.
    */
   private String getUniqueLettersHelper(String inString){
      String tempString = "";
      String sortedInString = sortWord(inString);
      for (int i = 0; i < sortedInString.length(); i++){
         if (tempString.indexOf(sortedInString.charAt(i)) == - 1){
            tempString = tempString + sortedInString.charAt(i);
         }
      }
      return tempString;
   }

   /**
    * Sorts a word to have its sorted version in alphabetical order.
    *
    * @param word  the word of String type to be sorted.
    * @return the sorted word of String type.
    */
   private String sortWord(String word){
      char[] tempArray = word.toCharArray();     // convert input string to char array
      Arrays.sort(tempArray);                    // sort tempArray
      return new String(tempArray);              // get the sorted string
   }

   /**
    * Gets the multiplicity of every unique letter of a given rack.
    *
    * @return tempArray an array to store multiplicity of every unique letter of a given rack..
    */
   private int[] getMultiOfLettersHelper(){
      Map<Character, Integer> letterMap = new HashMap<Character, Integer>();
      for (int i = 0; i < this.uniqueNum; i++){
         letterMap.put(this.uniqueLetters.charAt(i), i);
      }

      int[] tempArray = new int[this.uniqueNum];
      for (int i = 0; i < this.rackString.length(); i++){
         int letterIndex = letterMap.get(rackString.charAt(i));
         tempArray[letterIndex] ++;
      }
      return Arrays.copyOf(tempArray, this.uniqueNum);
   }



}



