// Name: Yao Fu
// USC NetID: yaof
// CS 455 PA1
// Spring 2021

import javax.swing.JFrame;
import java.util.Scanner;
/**
 * This class is to view the result of the coin toss experiment. 
 * 
 * Instruction:
 * Just run the code and you have to enter the number of trials.
 * 
 * NOTE:
 * You have to input an integer which is >= 1.
 * 
 */
public class CoinSimViewer 
{
   public static void main(String[] args)
   {
	   
      Scanner input = new Scanner(System.in);
      System.out.print("Enter number of trials: ");
      int trialNum = input.nextInt();
      while (trialNum <= 0)
      {
    	  System.out.println("ERROR: Number entered must be greater than 0.");
    	  System.out.print("Enter number of trials: ");
          trialNum = input.nextInt();
      }
	   
	  JFrame frame = new JFrame();

	  int framwWidth = 800;   // Width of the frame
      int framwHeight = 500;  // Height of the frame
      frame.setSize(framwWidth, framwHeight);
	  frame.setTitle("CoinSim");
	  frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      
	  CoinSimComponent component = new CoinSimComponent (trialNum);
	  frame.add(component);

	  frame.setVisible(true);
   }
}
