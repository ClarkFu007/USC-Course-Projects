import java.util.ArrayList;

/**
   This class tests the BookShelf class.
   CS 455  Lab 5.
*/
public class BookshelfTester 
{
	public static void main(String[] args)   
	{
		// create an ArrayList Integer type
		ArrayList<Integer> pilesOfBooks = new ArrayList<Integer>();
	
		// Initialize an ArrayList with add()
		int[] booksArray = {1, 3, 4, 8, 11, 14, 15, 18};
		for (int j : booksArray) {
			pilesOfBooks.add(j);
		}

		System.out.print("The pile of books are: ");
		System.out.println(pilesOfBooks);
		System.out.println();

		// Test empty Bookshelf object
		Bookshelf bookShelf1 = new Bookshelf();
		String bookShelf1String = bookShelf1.toString();
		System.out.print("For the empty object, the read-in books (exp:[]) are ");
		System.out.println(bookShelf1String + ".");
		System.out.println();

	   
		// Test nonempty Bookshelf object
		Bookshelf bookShelf2 = new Bookshelf(pilesOfBooks);
		String bookShelf2String = new String();
		bookShelf2String = bookShelf2.toString();
		System.out.print("For the nonempty object, the read-in books (exp:[1, 3, 4, 8, 11, 14, 15, 18]) are ");
		System.out.println(bookShelf2String + ".");
	   
		// Inserts a book with height 12 at the start of the Bookshelf.
		int fontHeight = 12;
		bookShelf2.addFront(fontHeight);
		bookShelf2String = bookShelf2.toString();
		System.out.print("  After addFont 12, the books (exp:[12, 1, 3, 4, 8, 11, 14, 15, 18]) are ");
		System.out.println(bookShelf2String + ".");
		// Check whether books are sorted or not.
		boolean sortedSituation = bookShelf2.isSorted();
		System.out.println("  The statement that books are sorted is " + sortedSituation + " (exp:false).");
		System.out.println();
	   
		// Inserts a book with height 20 at the end of the Bookshelf.
		int lastHeight = 20;
		bookShelf2.addLast(lastHeight);
		bookShelf2String = bookShelf2.toString();
		System.out.print("  After addLast 20, the books (exp:[12, 1, 3, 4, 8, 11, 14, 15, 18, 20]) are ");
		System.out.println(bookShelf2String + ".");
		// Check whether books are sorted or not.
		sortedSituation = bookShelf2.isSorted();
		System.out.println("  The statement that books are sorted is " + sortedSituation + " (exp:false).");
		System.out.println();
	   
		// Remove the book at the start of the Bookshelf and returns the removed height.
		fontHeight = bookShelf2.removeFront();
		bookShelf2String = bookShelf2.toString();
		System.out.print("  Aftering removeFront, the books (exp:[1, 3, 4, 8, 11, 14, 15, 18, 20]) are ");
		System.out.println(bookShelf2String + ".");
		System.out.println("And the removed book is " + fontHeight + " (exp:12).");
		// Check whether books are sorted or not.
		sortedSituation = bookShelf2.isSorted();
		System.out.println("  The statement that books are sorted is " + sortedSituation + " (exp:true).");
		System.out.println();
	   
		// Remove the book at the end of the Bookshelf and returns the removed height.
		lastHeight = bookShelf2.removeLast();
		bookShelf2String = bookShelf2.toString();
		System.out.print("  After removeLast, the books (exp:[1, 3, 4, 8, 11, 14, 15, 18]) are ");
		System.out.println(bookShelf2String + ".");
		System.out.println("And the removed book is " + lastHeight + " (exp:20).");
		// Check whether books are sorted or not.
		sortedSituation = bookShelf2.isSorted();
		System.out.println("  The statement that books are sorted is " + sortedSituation + " (exp:true).");
		System.out.println();
	   
		// Get the height of the book at the position 3.
		int position = 3;
		int heightPos3 = bookShelf2.getHeight(position);
		System.out.println("  The book at the position" + position + " is " + heightPos3 + " (exp:8).");

	   
		// Get the number of books on the this Bookshelf.
		int booksNumber = bookShelf2.size();
		System.out.println("  The number of books on the this Bookshelf is " + booksNumber + " (exp:8).");
	}
}
	


	

