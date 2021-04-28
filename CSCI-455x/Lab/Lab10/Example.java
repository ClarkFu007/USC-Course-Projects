import java.util.ArrayList;
import java.util.Map;
import java.util.TreeMap;
import java.util.Comparator;

public class Example {
   public static void main(String[] args) {
      TreeMap<String, Integer> initTree = new TreeMap<String, Integer>();
      initTree.put("D", 0);
      initTree.put("C", -3);
      initTree.put("A", 43);
      initTree.put("B", 32);
      System.out.println("Sorted by keys:");
      System.out.println(initTree);
      ArrayList<Map.Entry<String, Integer>> list = new ArrayList<>(initTree.entrySet());
      list.sort(new Comparator<Map.Entry<String, Integer>>() {
         public int compare(Map.Entry<String, Integer> e1, Map.Entry<String, Integer> e2) {
            return e1.getValue().compareTo(e2.getValue());
         }
      });
      ArrayList<Map.Entry<String, Integer>> revList = new ArrayList<Map.Entry<String, Integer>>();
      for (int i = list.size() - 1; i >= 0; i--) {
         // Append the elements in reverse order
         revList.add(list.get(i));
      }
      System.out.println("Sorted by values:");
      System.out.println(revList.get(1));
   }

}
