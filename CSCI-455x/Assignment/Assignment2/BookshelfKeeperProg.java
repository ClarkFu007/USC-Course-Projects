// Name: Yao Fu
// USC NetID: yaof
// CSCI455 PA2
// Spring 2021

import java.util.Scanner;
import java.util.ArrayList;

/**
 * This class tests the BookshelfKeeperProg class and the Bookshelf class, which
 * will read user input and print results.
 *
 * Instruction:
 * Just run the code and input commands according to the requirement of PA2
 * and see the statements in the console to check whether the implementation
 * of two implemented classes are correct or not.
 */

public class BookshelfKeeperProg {
   public static void main(String[] args) {
      System.out.println("Please enter initial arrangement of books followed by newline:");
      Scanner in = new Scanner(System.in);
      String line = in.nextLine();
      Scanner lineScanner = new Scanner(line);
      ArrayList<Integer> inBooksSequence = inputArrayList(lineScanner); // For a sequence of books
      seqErrorCheck(inBooksSequence);                // Error check the valid state of input books
      System.out.println(inBooksSequence + " " + 0 + " " + 0);
      Bookshelf bookShelf = new Bookshelf(inBooksSequence);
      BookshelfKeeper keeper = new BookshelfKeeper(bookShelf);

      System.out.println("Type pick <index> or put <height> followed by newline. Type end to exit.");
      line = in.nextLine();
      lineScanner = new Scanner(line);
      String operation = lineScanner.next(); // Read the operation instruction
      operationErrorCheck(operation);        // Error check the valid state of the operation

      while (!operation.equals("end")) {
         int integerPart = inputInteger(lineScanner);
         doOperation(operation, integerPart, keeper); // Implement the operation of "put" pr "pick"
         line = in.nextLine();
         lineScanner = new Scanner(line);
         operation = lineScanner.next(); // Read the operation instruction
         operationErrorCheck(operation); // Error check the valid state of the operation iteratively
      }
   }

   /**
    * Gets the ArrayList of books input by users.
    *
    * Returns the the sequence of books.
    *
    * @param lineScanner  input from users
    */
   private static ArrayList<Integer> inputArrayList(Scanner lineScanner) {
      ArrayList<Integer> inBooksSequence = new ArrayList<Integer>();
      while (lineScanner.hasNextLine()) {
         int height = Integer.parseInt(lineScanner.next());
         inBooksSequence.add(height);
         if (!lineScanner.hasNextInt()){
            break;
         }
      }
         return inBooksSequence;
   }

   /**
    * Gets the integer part by users.
    *
    * Returns the the integer part.
    *
    * @param lineScanner  input from users
    */
   private static int inputInteger(Scanner lineScanner) {
      int integerPart = 0;
      while (lineScanner.hasNextLine()) {
         integerPart = Integer.parseInt(lineScanner.next());
         if (!lineScanner.hasNextInt()){
            break;
         }
      }
      return integerPart;
   }

   /**
    * Implements the operation of "put" pr "pick".
    *
    * @param operation  put or pick
    * @param integerPart  height or position
    * @param keeper  instance of BookshelfKeeper to be handled
    */
   private static void doOperation(String operation, int integerPart, BookshelfKeeper keeper) {
      if (operation.equals("pick")){
         positionCheck(integerPart, keeper);  // Check the validity of the position
         int minCallNum = keeper.pickPos(integerPart);
         int totalCallNum = keeper.getTotalOperations();
         System.out.println(keeper.toString() + " " + minCallNum + " " + totalCallNum);
      }
      else if ((operation.equals("put"))){
         heightCheck(integerPart);            // Check the validity of the height
         int minCallNum = keeper.putHeight(integerPart);
         int totalCallNum = keeper.getTotalOperations();
         System.out.println(keeper.toString() + " " + minCallNum + " " + totalCallNum);
      }
      else {
            System.out.println("Input operation must be either pick or put!");
            System.exit(0);
         }
   }

   /**
    * Checks whether books are in non-decreasing order and having positive height.
    *
    * @param bookShelf  input books
    */
   private static void seqErrorCheck(ArrayList<Integer> bookShelf) {
      for (int i = 0; i < bookShelf.size() - 1; i++) {
         if (bookShelf.get(i) > bookShelf.get(i + 1)) {
            System.out.println("ERROR: Heights must be specified in non-decreasing order.");
            System.out.println("Exiting Program.");
            System.exit(0);

         }
         if (bookShelf.get(i) <= 0) {
            System.out.println("ERROR: Height of a book must be positive.");
            System.out.println("Exiting Program.");
            System.exit(0);
         }
      }
   }

   /**
    * Checks whether the operation is valid or not.
    *
    * @param operation  input operation
    */
   private static void operationErrorCheck(String operation) {
      if (!(operation.equals("put") || operation.equals("pick"))) {
         if (!operation.equals("end")){
            System.out.println("ERROR: Operation should be either pick or put.");
         }
         System.out.println("Exiting Program.");
         System.exit(0);
      }
   }

   /**
    * Checks the validity of the position.
    *
    * @param height  input height
    */
   private static void heightCheck(int height) {
      if (height <= 0) {
         System.out.println("ERROR: Height of a book must be positive.");
         System.out.println("Exiting Program.");
         System.exit(0);
      }
   }

   /**
    * Checks the validity of the height.
    *
    * @param position  input position
    * @param keeper  instance of BookshelfKeeper to be checked
    */
   private static void positionCheck(int position, BookshelfKeeper keeper) {
      int booksNum = keeper.getNumBooks();
      if (!(position >= 0 && position < booksNum)) {
         System.out.println("ERROR: Entered pick operation is invalid on this shelf.");
         System.out.println("Exiting Program.");
         System.exit(0);
      }
   }
}

