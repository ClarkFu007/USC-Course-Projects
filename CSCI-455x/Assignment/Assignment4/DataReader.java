// Name: Yao Fu
// USC NetID: yaof
// CS 455 PA4
// Spring 2021

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * Reads a data set from a file. The file must have a certain number of
 * English words.
 */
public class DataReader {
   private ArrayList<String> anagramDict;

   /**
    * Reads a data set.
    * @param fileName the name of the file holding words of the dictionary.
    * @return the data in the file.

    * The method throws an IOException, the common superclass of
    * FileNotFoundException(thrown by the Scanner constructor).
    */
   public ArrayList<String> readFile(String fileName) throws IOException {
      if (fileName.equals("")){
         fileName = "sowpods.txt";
      }
      File myFile = new File(fileName);
      try(Scanner myReader = new Scanner(myFile)){
         this.anagramDict = new ArrayList<String>();
         System.out.println("Here");
         while (myReader.hasNextLine()) {
            readData(myReader);
         }

         String duplicateWord = duplicateWord(this.anagramDict);
         if (!duplicateWord.equals("")){
            throw new IllegalDictionaryException("dictionary file has a duplicate word: " + duplicateWord);
         }
      }
      catch (FileNotFoundException exception) {
         throw new FileNotFoundException('\u0022' + fileName +'\u0022');
      }

      return new ArrayList<String>(this.anagramDict);
   }

   /**
    * Reads data in each step in the while loop.
    * @param in the scanner that scans the data.
    */
   private void readData(Scanner in){
      String data = in.nextLine();
      if (!data.equals("")){
         this.anagramDict.add(data);
      }
   }

   /**
    * Finds the first duplicate wrod.
    *
    * @param list the list containing words of the dictionary.
    * @return the first duplicate word in the dictionary.
    */
   private String duplicateWord(ArrayList<String> list) {
      String word = "";
      for (int i = 0; i < list.size(); i++){
         if (list.indexOf(list.get(i)) != i){
            word = list.get(i);
            break;
         }
      }
      return word;
   }
}
