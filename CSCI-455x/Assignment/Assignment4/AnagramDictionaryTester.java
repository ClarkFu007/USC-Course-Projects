// Name: Yao Fu
// USC NetID: yaof
// CS 455 PA4
// Spring 2021


import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Map;

/**
 * A test file to test the Anagram Dictionary.
 */

public class AnagramDictionaryTester {
   public static void main(String[] args) throws IOException {
      String dictName = "testFiles/tinyDictionary.txt";
      DataReader reader = new DataReader();
      ArrayList<String> anagramDict = reader.readFile(dictName);

      AnagramDictionary tinyDictionary = new AnagramDictionary(anagramDict);
      ArrayList<String> myDict = tinyDictionary.getAnagramDict();
      for (String s : myDict) {
         System.out.println(s);
      }
      System.out.println();

      Map<String, String> myDictMap = tinyDictionary.getAnagramDictMap();
      for (Map.Entry<String, String> stringStringEntry : myDictMap.entrySet()){
         System.out.println(stringStringEntry);
      }
      System.out.println();

      String inString = "bldgooo";
      ArrayList<String> anagramList = tinyDictionary.getAnagramsOf(inString);
      for (String s : anagramList) {
         System.out.println(s);
      }
   }

}
