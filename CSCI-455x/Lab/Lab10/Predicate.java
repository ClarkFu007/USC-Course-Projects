import java.util.Map;
import java.util.TreeMap;

/* Describes any class whose objects can test something about a Map Entry
 *    containing a String and Integer.
 */
interface Predicate {

   /**
      Tests whether item satisfies some condition.
      @param item the entry to be tested
      @return whether this predicate is true about the entry
   */
   public boolean predicate(Map.Entry<String, Integer> item);
}

