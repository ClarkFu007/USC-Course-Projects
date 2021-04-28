// Name: Yao Fu
// USC NetID: yaof
// CSCI455 PA2
// Spring 2021

import java.util.ArrayList;
import java.lang.Math;

/**
 * Class BookshelfKeeper 
 *
 * Enables users to perform efficient putPos or pickHeight operation on a bookshelf of books kept in 
 * non-decreasing order by height, with the restriction that single books can only be added 
 * or removed from one of the two "ends" of the bookshelf to complete a higher level pick or put
 * operation. Pick or put operations are performed with minimum number of such adds or removes.
 */
public class BookshelfKeeper {
    /**
     * Representation invariant:
     * The books of the bookshelf should be in non-decreasing order;
     * The number of calling mutators should be minimized.
     */
    private Bookshelf myBookshelf;
    private int totalCallNums = 0;
    private final static double MID_POS_FACTOR = 2.0;

   /**
    * Creates a BookShelfKeeper object with an empty bookshelf
    */
   public BookshelfKeeper() {
      this.myBookshelf = new Bookshelf();
      assert isValidBookshelfKeeper();
   }

   /**
    * Creates a BookshelfKeeper object initialized with the given sorted bookshelf.
    * Note: method does not make a defensive copy of the bookshelf.
    *
    * @param sortedBookshelf  a sorted books according to their height
    *
    * PRE: sortedBookshelf.isSorted() is true.
    */
   public BookshelfKeeper(Bookshelf sortedBookshelf) {
      assert sortedBookshelf.isSorted();
      int bookNums = sortedBookshelf.size();
      ArrayList<Integer> sortedPileOfBooks = new ArrayList<Integer>(bookNums);
      for (int i = 0; i < bookNums; i++){
         sortedPileOfBooks.add(sortedBookshelf.getHeight(i));
      }
      this.myBookshelf = new Bookshelf(sortedPileOfBooks);
      assert isValidBookshelfKeeper();
   }

   /**
    * Removes a book from the specified position in the bookshelf and keeps bookshelf sorted 
    * after picking up the book.
    * 
    * Returns the number of calls to mutators on the contained bookshelf used to complete this
    * operation. This must be the minimum number to complete the operation.
    *
    * @param position  input position
    *
    * PRE: position must be in the range [0, getNumBooks()).
    */
   public int pickPos(int position) {
      assert isValidBookshelfKeeper();
      Bookshelf tempBookshelf = new Bookshelf();
      int callNums = 0;
      int bookNums = this.myBookshelf.size();
      double middlePos = bookNums / MID_POS_FACTOR;  // Get the middle position
      if (position < middlePos) {
         // From the left part
         for (int i = 0; i <= position; i++) {
            tempBookshelf.addLast(this.myBookshelf.removeFront());
            callNums++;
         }
         tempBookshelf.removeLast();
         while (tempBookshelf.size() != 0) {
            int tempBook = tempBookshelf.removeLast();
            this.myBookshelf.addFront(tempBook);
            callNums++;
         }
      }
      else{
         // From the right part
         int lastPos = bookNums - 1; // The index starts from 0 instead of 1
         for (int i = lastPos; i >= position; i--) {
            tempBookshelf.addFront(this.myBookshelf.removeLast());
            callNums++;
         }
         tempBookshelf.removeFront();
         while (tempBookshelf.size() != 0) {
            int tempBook = tempBookshelf.removeFront();
            this.myBookshelf.addLast(tempBook);
            callNums++;
         }
      }

      this.totalCallNums += callNums;
      assert isValidBookshelfKeeper();
      return callNums;
   }

   /**
    * Inserts book with specified height into the shelf. Keeps the contained bookshelf sorted
    * after the insertion.
    * 
    * Returns the number of calls to mutators on the contained bookshelf used to complete this
    * operation. This must be the minimum number to complete the operation.
    *
    * @param height  input height
    *
    * PRE: height > 0
    */
   public int putHeight(int height) {
      int bookNums = this.myBookshelf.size();

      // Count how many books from left or right of this input height
      // Number of books from left
      int leftNum = bookNumFrom2Sides(height, this.myBookshelf, "left");
      // Number of books from right
      int rightNum = bookNumFrom2Sides(height, this.myBookshelf, "right");

      int callNums = 0;
      if (leftNum == bookNums && rightNum == bookNums) {
         if (bookNums == 0){ // No books in this shelf
            this.myBookshelf.addFront(height);
            callNums++;
         }
         else{ // No book in the shelf has the same height with input height
            callNums = putUniqueHeight(height, bookNums);
         }
      }
      else if(leftNum <= rightNum){ // Some books in the shelf has the same height with input height
         // From the left part
         callNums = putNonuniqueHeight(height, leftNum, "left");
      }
      else{ // Some books in the shelf has the same height with input height
         // From the right part
         callNums = putNonuniqueHeight(height, rightNum, "right");
      }

      this.totalCallNums += callNums;
      assert isValidBookshelfKeeper();
      return callNums;
   }


   /**
    * Returns the total number of calls made to mutators on the contained bookshelf
    * so far, i.e., all the ones done to perform all of the pick and put operations
    * that have been requested up to now.
    */
   public int getTotalOperations() {
      assert isValidBookshelfKeeper();
      return this.totalCallNums;
   }

   /**
    * Returns the number of books on the contained bookshelf.
    */
   public int getNumBooks() {
      assert isValidBookshelfKeeper();
      return this.myBookshelf.size();
   }

   /**
    * Returns string representation of this BookshelfKeeper. Returns a String containing height
    * of all books present in the bookshelf in the order they are on the bookshelf, followed 
    * by the number of bookshelf mutator calls made to perform the last pick or put operation, 
    * followed by the total number of such calls made since we created this BookshelfKeeper.
    * 
    * Example return string showing required format: "[1, 3, 5, 7, 33] 4 10"
    */
   public String toString() {
      assert isValidBookshelfKeeper();
      return this.myBookshelf.toString();
   }

   /**
    * Returns true iff the BookshelfKeeper data is in a valid state.
    *
    * The valid state of the BookshelfKeeper data means height of books should be in
    * non-decreasing order.
    */
   private boolean isValidBookshelfKeeper() {
      return this.myBookshelf.isSorted();
   }

   /**
    * Returns how many books from left or right of this input height.
    *
    * @param height  input height
    * @param bookshelf  bookshelf to be handled
    * @param direction  the handled direction
    *
    * PRE: height > 0
    *      direction should be either "left" or "right"
    */
   private int bookNumFrom2Sides(int height, Bookshelf bookshelf, String direction) {
      int num = 0;
      if (direction.equals("left")){ // Start from left
         for (int i = 0; i < bookshelf.size(); i++){
            if (height == bookshelf.getHeight(i)){
               break;
            }
            else{
               num ++;
            }
         }
      }
      else if (direction.equals("right")){ // Start from right
         for (int i = bookshelf.size() - 1; i >= 0; i--){
            if (height == bookshelf.getHeight(i)){
               break;
            }
            else{
               num ++;
            }
         }
      }
      else{
         System.out.println("Input direction must be either left or right!");
         System.exit(0);
      }
      return num;
   }

   /**
    * No existing books have the same height as the input height.
    *
    * Returns the number of calling mutators.
    *
    * @param height  input height
    * @param bookNums  number of books
    *
    * PRE: height > 0
    *      bookNums >= 0
    */
   private int putUniqueHeight(int height, int bookNums) {
      int callNums = 0;
      int middlePos = (int) Math.floor(bookNums / MID_POS_FACTOR);
      int midBookHeight = this.myBookshelf.getHeight(middlePos);
      if (height < midBookHeight) {
         // From the left part to add height
         callNums = leftPutUniqueHeight(height);
      }
      else {
         // From the right part to add height
         callNums = rightPutUniqueHeight(height, bookNums);
      }
      return callNums;
   }


   /**
    * No existing books have the same height as the input height.
    * Put the target height from left
    *
    * Returns the number of calling mutators.
    *
    * @param height  input height
    *
    * PRE: height > 0
    */
   private int leftPutUniqueHeight(int height) {
      Bookshelf tempBookshelf = new Bookshelf();
      int callNums = 0;
      if (height < this.myBookshelf.getHeight(0)) {
         this.myBookshelf.addFront(height);
         callNums++;
      }
      else {
         while (this.myBookshelf.size() != 1){
            int leftHeight = this.myBookshelf.getHeight(0);
            int rightHeight = this.myBookshelf.getHeight(1);
            if (leftHeight < height && rightHeight > height) {
               tempBookshelf.addLast(this.myBookshelf.removeFront());
               this.myBookshelf.addFront(height);
               callNums += 2;
               break;
            }
            else {
               tempBookshelf.addLast(this.myBookshelf.removeFront());
               callNums++;
            }
         }

         while (tempBookshelf.size() != 0) {
            int tempBook = tempBookshelf.removeLast();
            this.myBookshelf.addFront(tempBook);
            callNums++;
         }
      }
      return callNums;
   }

   /**
    * No existing books have the same height as the input height.
    * Put the target height from right
    *
    * Returns the number of calling mutators.
    *
    * @param height  input height
    * @param bookNums  number of books
    *
    * PRE: height > 0
    */
   private int rightPutUniqueHeight(int height, int bookNums) {
      Bookshelf tempBookshelf = new Bookshelf();
      int lastPos = bookNums - 1; // The index starts from 0
      int callNums = 0;
      if (height > this.myBookshelf.getHeight(lastPos)) {
         this.myBookshelf.addLast(height);
         callNums++;
      }
      else {
         while (this.myBookshelf.size() != 1){
            int lastIndex = this.myBookshelf.size() - 1;
            int leftHeight = this.myBookshelf.getHeight(lastIndex - 1);
            int rightHeight = this.myBookshelf.getHeight(lastIndex);
            if (leftHeight < height && rightHeight > height) {
               tempBookshelf.addFront(this.myBookshelf.removeLast());
               this.myBookshelf.addLast(height);
               callNums += 2;
               break;
            }
            else {
               tempBookshelf.addFront(this.myBookshelf.removeLast());
               callNums++;
            }
         }
         while (tempBookshelf.size() != 0) {
            int tempBook = tempBookshelf.removeFront();
            this.myBookshelf.addLast(tempBook);
            callNums++;
         }
      }
      return callNums;
   }

   /**
    * Some of the existing books have the same height as the input height.
    *
    * Returns the number of calling mutators.
    *
    * @param height  input height
    * @param directionNum  number of books in this direction
    * @param direction  "left" or "right"
    *
    * PRE: height > 0
    *      bookNums >= 0
    */
   private int putNonuniqueHeight(int height, int directionNum, String direction) {
      Bookshelf tempBookshelf = new Bookshelf();
      int callNums = 0;
      if (direction.equals("left")){
         for (int i = 0; i <= directionNum - 1; i++) {
            tempBookshelf.addLast(this.myBookshelf.removeFront());
            callNums++;
         }
         this.myBookshelf.addFront(height);
         callNums++;
         while (tempBookshelf.size() != 0) {
            int tempBook = tempBookshelf.removeLast();
            this.myBookshelf.addFront(tempBook);
            callNums++;
         }
      }
      else if (direction.equals("right")){
         for (int i = 0; i <= directionNum - 1; i++) {
            tempBookshelf.addFront(this.myBookshelf.removeLast());
            callNums++;
         }
         this.myBookshelf.addLast(height);
         callNums++;
         while (tempBookshelf.size() != 0) {
            int tempBook = tempBookshelf.removeFront();
            this.myBookshelf.addLast(tempBook);
            callNums++;
         }
      }
      else{
         System.out.println("Input direction must be either left or right!");
         System.exit(0);
      }
      return callNums;
   }
}
