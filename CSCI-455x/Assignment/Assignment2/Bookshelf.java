// Name: Yao Fu
// USC NetID: yaof
// CSCI455 PA2
// Spring 2021

import java.util.ArrayList;

/**
 * Class Bookshelf
 *
 * Implements idea of arranging books into a bookshelf.
 * Books on a bookshelf can only be accessed in a specific way so books don’t fall down;
 * You can add or remove a book only when it’s on one of the ends of the shelf.   
 * However, you can look at any book on a shelf by giving its location (starting at 0).
 * Books are identified only by their height; two books of the same height can be
 * thought of as two copies of the same book.
*/
public class Bookshelf {
   /**
    * Representation invariant:
    * The height of each book should be positive;
    * The instance variable cannot be null.
    */
	private ArrayList<Integer> myPileOfBooks;

   /**
    * Creates an empty Bookshelf object i.e. with no books
    */
   public Bookshelf() {
      this.myPileOfBooks = new ArrayList<Integer>();
      assert isValidBookshelf();  
   }

   /**
    * Creates a Bookshelf with the arrangement specified in pileOfBooks. Example
    * values: [20, 1, 9].
    *
    * @param pileOfBooks  input pile of books
    *
    * PRE: pileOfBooks contains an array list of 0 or more positive numbers
    * representing the height of each book.
    */
   public Bookshelf(ArrayList<Integer> pileOfBooks) {
	  this.myPileOfBooks = new ArrayList<Integer>(pileOfBooks);
	  assert isValidBookshelf();  
   }

   /**
    * Inserts book with specified height at the start of the Bookshelf, i.e., it
    * will end up at position 0.
    *
    * @param height  input height
    *
    * PRE: height > 0 (height of book is always positive)
    */
   public void addFront(int height) {
      this.myPileOfBooks.add(0, height);
      assert isValidBookshelf();
   }

   /**
    * Inserts book with specified height at the end of the Bookshelf.
    *
    * @param height  input height
    *
    * PRE: height > 0 (height of book is always positive)
    */
   public void addLast(int height) {
	   this.myPileOfBooks.add(height);
	   assert isValidBookshelf();
   }

   /**
    * Removes book at the start of the Bookshelf and returns the height of the
    * removed book.
    * 
    * PRE: this.size() > 0 i.e. can be called only on non-empty BookShelf
    */
   public int removeFront() {
      int firstBook = this.myPileOfBooks.get(0);
      this.myPileOfBooks.remove(0);
      assert isValidBookshelf();
      return firstBook;   
   }

   /**
    * Removes book at the end of the Bookshelf and returns the height of the
    * removed book.
    * 
    * PRE: this.size() > 0 i.e. can be called only on non-empty BookShelf
    */
   public int removeLast() {
      int pileSize = this.myPileOfBooks.size();
	   int lastBook = this.myPileOfBooks.get(pileSize - 1);
	   this.myPileOfBooks.remove(pileSize - 1);
	   assert isValidBookshelf();
	   return lastBook;
   }

   /**
    * Gets the height of the book at the given position.
    *
    * @param position  input position
    *
    * PRE: 0 <= position < this.size()
    */
   public int getHeight(int position) {
      int theHeight = this.myPileOfBooks.get(position);
      assert isValidBookshelf();
      return theHeight;   
   }

   /**
    * Returns number of books on the this Bookshelf.
    */
   public int size() {
	  int theSize = this.myPileOfBooks.size();
	  assert isValidBookshelf();
	  return theSize;
   }

   /**
    * Returns string representation of this Bookshelf. Returns a string with the height of all
    * books on the bookshelf, in the order they are in on the bookshelf, using the format shown
    * by example here:  "[7, 33, 5, 4, 3]"
    */
   public String toString() {
	  assert isValidBookshelf();
	  StringBuilder bookString = new StringBuilder("[");
      int bookSize = size();
      if (bookSize == 0) {
         bookString.append("]");
      }
      else {
         for(int i = 0; i < bookSize; i++) {
            if (i == bookSize - 1) {
               bookString.append(this.myPileOfBooks.get(i)).append("]");
            }
            else {
               bookString.append(this.myPileOfBooks.get(i)).append(", ");
            }
         }
      }
      
      return bookString.toString();
   }

   /**
    * Returns true iff the books on this Bookshelf are in non-decreasing order.
    * (Note: this is an accessor; it does not change the bookshelf.)
    */
   public boolean isSorted() {
	  assert isValidBookshelf();
	  for (int i = 0; i < this.myPileOfBooks.size() - 1; i++) {
         if (this.myPileOfBooks.get(i) > this.myPileOfBooks.get(i + 1)) {
            return false;
         }
      }
	  return true;
   }

   /**
    * Returns true iff the Bookshelf data is in a valid state.
    * (See representation invariant comment for more details.)
    */
   private boolean isValidBookshelf() {
      if (this.myPileOfBooks == null) {
	     return false;
      }
	  
	  if (this.myPileOfBooks.size() == 0) {
         return true; 
      }
      else {
        for (Integer myPileOfBook : this.myPileOfBooks) {
           if (myPileOfBook < 0) {
              return false;
           }
        }
      }
	  return true;
   }
}
