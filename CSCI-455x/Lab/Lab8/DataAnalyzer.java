import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Scanner;

/**
   This program reads a file containing numbers and analyzes its contents.
   If the file doesn't exist or contains strings that are not numbers, an
   error message is displayed.

   The Scanner constructor will throw an exception when the file does not exist.
   The methods that process the input values need to throw an exception when
   they find an error in the data format.

   The catch clauses in the main method give a human-readable error report
   if the file was not found or bad data was encountered.

*/
public class DataAnalyzer {
   public static void main(String[] args) {
      Scanner in = new Scanner(System.in);
      DataSetReader reader = new DataSetReader();
      
      boolean done = false;
      while (!done) {
         try {
            System.out.println("Please enter the file name: ");
            String filename = in.next();
            
            double[] data = reader.readFile(filename);
            double sum = 0;
            for (double d : data) {
               sum = sum + d; }
            System.out.println("The sum is " + sum);
            done = true;
         }
         catch (FileNotFoundException exception) {
            System.out.println("File not found: " + exception.getMessage());
         }
         catch (BadDataException exception) {
            System.out.println("Bad data: " + exception.getMessage());
            done = true;
         }
         catch (IOException exception) {
            exception.printStackTrace();
            System.exit(0);
         }
      }
   }
}
