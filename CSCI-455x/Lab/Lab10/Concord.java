import javax.swing.text.Keymap;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Map;
import java.util.TreeMap;
import java.util.Scanner;
import java.util.Set;
import java.util.Iterator;
import java.util.Comparator;


/**
 * Computes the number of occurrences of all words from a Scanner.
 * Strips a word of surrounding punctuation and converts to all lower
 * case before counting it.
 * Allows for output in map-order (print) or sorted in decreasing order
 * by number of occurrences (printSorted)
 * or output of only entries satisfying some condition (printSatisfying)
 *
 * Version for lab.
 */
public class Concord {
	
   private Map<String, Integer> concord;
	
   /**
    * Creates empty concordance
    */
   public Concord() {
      concord = new TreeMap<String, Integer>();
   }
	
   /**
    * Add data from Scanner to concordance.
    * @param in data to scan.  "in" will be at the end of its data after this
    * operation.
    */
   public void addData(Scanner in) {
      while (in.hasNext()) {
			
         String word = in.next();
         word = filter(word);  // remove punctuation, convert upper case
         Integer oldValue = concord.get(word);

         if (oldValue == null) {
            concord.put(word, 1);
         }
         else {
            concord.put(word, oldValue + 1);
         }


      }
		
   }
	
   public String toString() {
      return concord.toString();
   }
	
   /**
    * Write concordance data to out.
    * Format is one entry per line: word number
    * where "number" is the number of occurrrences of that word.
    * @param out where to write the results.
    */
   public void print(PrintStream out) {
		
      // version with for each loop

      for (Map.Entry<String, Integer> curr : concord.entrySet()) {
         out.println(curr.getKey() + " " + curr.getValue());
      }

   }
	

   /**
    * Write concordance data to "out" in decreasing order by 
    * number of occurrences.
    * Format is one entry per line: word number
    * where "number" is the number of occurrences of that word.
    * @param out where to write the results.
    */
   public void printSorted(PrintStream out) {
      ArrayList<Map.Entry<String, Integer>> concoedList = new ArrayList<>(this.concord.entrySet());
      /**
      concoedList.sort(new Comparator<Map.Entry<String, Integer>>() {
         public int compare(Map.Entry<String, Integer> e1, Map.Entry<String, Integer> e2) {
            return e1.getValue().compareTo(e2.getValue());
         }
      });
      for (int i =  concoedList.size() - 1; i >= 0; i--) {
         // Append the elements in reverse order
         out.println(concoedList.get(i));
      }
       */
      MapComparator mapComparator = new MapComparator();
      concoedList.sort(mapComparator);
      for (int i = 0; i < concoedList.size(); i++) {
         // Append the elements in reverse order
         out.println(concoedList.get(i));
      }

   }
	
   // NOTE: printSatisfying only used in Ex. 3
   /**
    * Writes some entries to out, using same format as Concord print method
    * The entries it writes are the the ones that satisfying pred.
    * @param out the outstream to write to
    * @param pred the predicate that each entry is tested on.
    */
   public void printSatisfying(PrintStream out, Predicate pred) {
      for (Map.Entry<String,Integer> entry : concord.entrySet()) {

         if (pred.predicate(entry)) {
            out.println(entry.getKey() 
                        + " " + entry.getValue());
         }

      }
   }

   /**
    * Returns a version of the word that's all lower case
    * with leading and trailing punctuation removed.
    * (Keeps internal punctuation, such as "won't")
    * @param word the word to filter
    * @return the filtered word
    */
   public static String filter(String word) {
      // match beginning of string followed one or more non-word chars OR
      // match one or more non-word chars followed by end of string
      // replaces such sequences with the empty string
      String newWord = word.replaceAll("(\\A[^\\w]+)|([^\\w]+\\z)", "");
      newWord = newWord.toLowerCase();
      return newWord;
   }

}

class MapComparator implements Comparator<Map.Entry<String, Integer>> {
   /**
    * Creates empty concordance
    */
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