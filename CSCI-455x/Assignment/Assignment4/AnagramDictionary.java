// Name: Yao Fu
// USC NetID: yaof
// CS 455 PA4
// Spring 2021

import java.util.Arrays;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

/**
 * A dictionary of all anagram sets.
 * Note: the processing is case-sensitive; so if the dictionary has all lower
 * case words, you will likely want any string you test to have all lower case
 * letters too, and likewise if the dictionary words are all upper case.
 */
public class AnagramDictionary {
   private ArrayList<String> anagramDict;
   private Map<String, String> anagramDictMap;


   /**
    * Creates an anagram dictionary from the list of words given in the file
    * indicated by fileName. Then key is the original word and the value is
    * the sorted version of that original word.
    *
    * Representation invariants:
    * 1: The anagramDict should contain English words.
    * 2: The anagramDictMap's keys should always be string with letters and values
    * are relevant sorted versions.
    *
    * @param anagramDict  the list containing words of the dictionary.
    */
   public AnagramDictionary(ArrayList<String> anagramDict) {
      this.anagramDict = new ArrayList<String>(anagramDict);
      this.anagramDictMap = convertAnagramDictToMap();
   }

   /**
    * Gets all anagrams of the given string. This method is case-sensitive.
    * E.g. "CARE" and "race" would not be recognized as anagrams.
    *
    * @param inString  string to process.
    * @return a list of the anagrams of s.
    */
   public ArrayList<String> getAnagramsOf(String inString) {
      String sortedInString = sortWord(inString);
      ArrayList<String> anagramList = new ArrayList<String>();

      for (Map.Entry<String, String> dictMapEntry : this.anagramDictMap.entrySet()){
         if (dictMapEntry.getValue().equals(sortedInString)){
            anagramList.add(dictMapEntry.getKey());
         }
      }

      return anagramList;
   }

   /**
    * Gets the current anagram dictionary.
    *
    * @return the anagram dictionary.
    */
   public ArrayList<String> getAnagramDict() {
      return this.anagramDict;
   }

   /**
    * Gets the current anagram dictionary map.
    *
    * @return the anagram dictionary map.
    */
   public Map<String, String> getAnagramDictMap() {
      return this.anagramDictMap;
   }

   /**
    * Converts the anagram dictionary into the anagram dictionary map. The value
    * of the map is the sorted key, where they are both strings.
    *
    * @return the anagram dictionary map.
    */
   private Map<String, String> convertAnagramDictToMap(){
      Map<String, String> tempAnagramDictMap = new HashMap<String, String>();
      for (String word : this.anagramDict) {

         String sortedWord = sortWord(word);       // get the sorted word

         tempAnagramDictMap.put(word, sortedWord); // put the (word, sorted word) into the map
      }
      return new HashMap<String, String>(tempAnagramDictMap);
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
}
