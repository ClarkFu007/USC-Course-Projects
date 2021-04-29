import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Scanner;


/**
   Reads a data set from a file. The file must have the format
   numberOfValues
   value1
   value2
   . . .
*/
public class DataSetReader {
   private double[] data;

   /**
      Reads a data set.
      @param filename the name of the file holding the data
      @return the data in the file

      The method throws an IOException, the common superclass of
      FileNotFoundException(thrown by the Scanner constructor) and
      BadDataException (thrown by the readData method).
   */
   public double[] readFile(String filename) throws IOException {
      File inFile = new File(filename);
      try (Scanner in = new Scanner(inFile)) {
         readData(in);
         return data;
      }  // Will close the file automatically
      catch (FileNotFoundException exception) {
         throw new FileNotFoundException(filename);
      }
   }

   /**
      Reads all data.
      @param in the scanner that scans the data

      It reads the number of values, constructs an array,
      and calls readValue for each data value.This method
      checks for two potential errors. The file might not
      start with an integer, or it might have additional
      data after reading all values.

   */
   private void readData(Scanner in) throws BadDataException {
      if (!in.hasNextInt()) {
         throw new BadDataException("Length expected");
      }
      int numberOfValues = in.nextInt();
      data = new double[numberOfValues];

      for (int i = 0; i < numberOfValues; i++) {
         readValue(in, i);
      }

      if (in.hasNext()) {
         throw new BadDataException("Too many data values given");
      }
   }

   /**
      Reads one data value.
      @param in the scanner that scans the data
      @param i the position of the value to read
   */
   private void readValue(Scanner in, int i) throws BadDataException {
      if (!in.hasNextDouble()) {
         if (in.hasNext()) {
            throw new BadDataException("Non-floating point value given: " + in.next());
         }
         throw new BadDataException("Too few data values given");
      }
      data[i] = in.nextDouble();      
   }
}
