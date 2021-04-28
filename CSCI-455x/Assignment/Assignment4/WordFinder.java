// Name: Yao Fu
// USC NetID: yaof
// CS 455 PA4
// Spring 2021

import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Map;
import java.util.TreeMap;
import java.util.Scanner;
import java.util.Comparator;

/**
 * When given letters that could comprise a Scrabblerack, creates a list of all legal words
 * that can be formed from the letters on that rack.
 *
 * The format of input:
 * java WordFinder [dictionaryFile]
 * eg:
 * java WordFinder < testFiles/test1.in > test1.out
 * java WordFinder testFiles/tinyDictionary.txt < testFiles/tiny.in > tiny.out
 */
public class WordFinder {
   public static void main(String[] args) throws IOException {
      Scanner input = new Scanner(System.in);
      DataReader reader = new DataReader();
      try {
         String dictName;
         if (args.length == 0){
            dictName = "";
         }
         else{
            dictName = args[0];  // Get the dictionary file name if exists
         }
         ArrayList<String> anagramDict = reader.readFile(dictName);
         System.out.println("Type . to quit.");
         while (true) {
            System.out.print("Rack? ");
            String rackString = input.nextLine();
            if (rackString.equals(".")){
               break;
            }
            playScrabble(rackString, anagramDict); // Play the Scrabble game
         }
      } catch (FileNotFoundException exception) {
         System.out.println("ERROR: Dictionary file " + exception.getMessage() + " does not exist.");
         System.out.println("Exiting program.");
         System.exit(1);
      } catch (IllegalDictionaryException exception) {
         System.out.println("ERROR: Illegal dictionary: " + exception.getMessage());
         System.out.println("Exiting program.");
         System.exit(1);
      }
   }

   /**
    * Plays the Scrabble game and prints the required information.
    *
    * @param rackString the string of the rack.
    * @param anagramDict the list containing words od the dictionary.
    */
   private static void playScrabble(String rackString, ArrayList<String> anagramDict)
         throws FileNotFoundException, IllegalDictionaryException {
      Rack myRack = new Rack(rackString, 0);
      ArrayList<String> allSubsetOfRack = myRack.getAllSubsetList(); // Get all subsets

      AnagramDictionary myDict = new AnagramDictionary(anagramDict);
      Map<String, String> myDictMap = myDict.getAnagramDictMap(); // Get the map of the dictionary

      ArrayList<String> anagramListOfRack;
      Map<String, Integer> resultMap = new TreeMap<String, Integer>();
      for (String subsetRack : allSubsetOfRack) {
         anagramListOfRack = new ArrayList<String>(myDict.getAnagramsOf(subsetRack));
         ScoreTable currScoreTable;
         for (String currAnagram : anagramListOfRack) {
            if (myDictMap.containsKey(currAnagram)) {
               currScoreTable = new ScoreTable(currAnagram);
               int currScore = currScoreTable.getScore();
               resultMap.put(currAnagram, currScore);
            }
         }
      }
      System.out.println("We can make " + resultMap.size() + " words from "
            + '\u0022' + rackString +'\u0022');
      if (resultMap.size() != 0){
         System.out.println("All of the words with their scores (sorted by score):");
      }
      // Print the final results
      ArrayList<Map.Entry<String, Integer>> resultList = new ArrayList<>(resultMap.entrySet());
      MapComparator mapComparator = new MapComparator();
      resultList.sort(mapComparator);
      for (Map.Entry<String, Integer> resultEntry : resultList) {
         System.out.println(resultEntry.getValue() + ": " + resultEntry.getKey());
      }
   }

}

/**
 * This class implements the Comparator in order to help sort the map.
 */
class MapComparator implements Comparator<Map.Entry<String, Integer>> {
   public int compare(Map.Entry<String, Integer> e1, Map.Entry<String, Integer> e2) {
      if (e1.getValue() > e2.getValue()){
         return -1;
      }
      else if (e1.getValue().equals(e2.getValue())){
         return 0;
      }
      else{
         return 1;
      }
   }
}