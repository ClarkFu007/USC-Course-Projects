import java.util.ArrayList;

/**
   Stores a sequence of integer data values and supports some computations
   with it.

   CS 455 Lab 4.
*/
public class Nums 
{

   private ArrayList<Integer> myNums;

   /**
      Create an empty sequence of nums.
   */
   public Nums () 
   {
      this.myNums = new ArrayList<Integer>();
   }
   
   /**
      Create a nonempty sequence of nums.
   */
   public Nums (ArrayList<Integer> nums) 
   {
      this.myNums = new ArrayList<Integer>(nums);
   }

   /**
      Add a value to the end of the sequence.
   */
   public void add(int value) 
   {
      this.myNums.add(value);
   }

   /**
      Return the minimum value in the sequence.
      If the sequence is empty, returns Integer.MAX_VALUE
   */
   public int minVal() 
   {
      if(myNums.size() == 0)
      {
         return Integer.MAX_VALUE;
      }
      else
      {
         int minValue = this.myNums.get(0);
      //Iterate through ArrayList
      for(int i = 1; i < this.myNums.size(); i++ )
      {
         if(this.myNums.get(i) < minValue)
         {
            minValue = this.myNums.get(i);
         }
      }
      return minValue;
    }
   }

   /**
      Prints out the sequence of values as a space-separated list 
      on one line surrounded by parentheses.
      Does not print a newline.
      E.g., "(3 7 4 10 2 7)", for empty sequence: "()"
   */
   public void printVals() 
   {
	   String str = "(";
       for(int i = 0; i < myNums.size(); i++)
       {
          str += (myNums.get(i) + " ");
       }
       str = str.trim();
       str += ")";
       System.out.println(str);
   }

   /**
      Returns a new Nums object with all the values from this Nums
      object that are above the given threshold.  The values in the
      new object are in the same order as in this one.
      E.g.: call to myNums.valuesGT(10) where myNums = (3 7 19 4 21 19 10)
      returns      (19 21 19)
      myNums after call:  (3 7 19 4 21 19 10)
      The method does not modify the object the method is called on.
   */
   public Nums valuesGT(int threshold) 
   {
      Nums gtList = new Nums();
	      
	  for (int i = 0; i < myNums.size(); i++)
	  {
	     if(myNums.get(i) > threshold)
	     {
	        gtList.add(myNums.get(i));
	     }
	  }
	  return gtList;
   }    
}
