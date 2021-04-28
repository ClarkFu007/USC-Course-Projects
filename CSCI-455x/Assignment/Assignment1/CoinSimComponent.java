// Name: Yao Fu
// USC NetID: yaof
// CS 455 PA1
// Spring 2021

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.JComponent;
/**
 * This component extends JComponent. Constructor initializes any necessary 
 * data and runs the simulation. Overrides paintComponent to draw the bar graph, 
 * using Bar objects for each bar in the graph. This class only uses the 
 * CoinTossSimulator and Bar class.
 * 
 */
public class CoinSimComponent extends JComponent
{
   // Instance variables for the CoinSimComponent class
   private int trialNum;   // The total number of trials
   private int callCount;  // the total number of calling the class.
   private double weightBar;         // the weight for bar width.
   private double weightMaxHeight;   // the weight for maximum height.
   private double weightTotalHeight; // the weight for total height.
   private double scaleValue;        // To scale the picture accordingly.
   private int midLocate;    // To locate the middle bar
   private int leftLocate;   // To locate the left bar
   private int rightLocate;  // To locate the right bar
	   
   /**
      Creates a CoinSimComponentr with no calling and required trials.
   */ 
   public CoinSimComponent(int trialNum) 
   {
      this.callCount = 0;
      this.trialNum = trialNum;
      this.weightBar = 0.1;
      this.weightMaxHeight = 0.9;
      this.weightTotalHeight = 0.8;
      this.scaleValue = 1.0; 
      this.midLocate = 2;
      this.leftLocate = 3;
      this.rightLocate = 3;
   }
   
   /**
      Multiple calls to resize the graph.
      
      @param g  the illustrated picture. 
   */
   public void paintComponent(Graphics g)
   {  
      // Recover Graphics2D
	  Graphics2D g2 = (Graphics2D) g;
	            
      // the following two lines are for instrumentation
      callCount++;
	  System.out.println("Called paintComponent(" + callCount + ")");
	  
      // Experiment results
	  CoinTossSimulator coinTrial = new CoinTossSimulator();
	  coinTrial.run(this.trialNum);
	  int twoHeadsNum = coinTrial.getTwoHeads();
      int twoTailsNum = coinTrial.getTwoTails();
      int oneHeadOneTailNum = coinTrial.getHeadTails();
	  
      // Multiplying 100 means getting a two-digit integer
	  int twoHeadsPercent = twoHeadsNum * 100 / this.trialNum;
	  int twoTailsPercent = twoTailsNum * 100 / this.trialNum;
	  int oneHeadOneTailPercent = oneHeadOneTailNum * 100 / this.trialNum;

	  
	  int currentWidth = getWidth();
	  int currentHeight = getHeight();
	  
	  int barWidth = (int) (this.weightBar * currentWidth);         // Set the bar width
	  int maxHeight = (int) (this.weightMaxHeight * currentHeight);     // To set the y value for the middle bar 
	  int totalHeight = (int) (this.weightTotalHeight * currentHeight); // To control every bar's height
	  
	  int oneHeadOneTailHeight = (int) (oneHeadOneTailPercent / 100.0 * totalHeight);
	  int twoHeadsHeight = (int) (twoHeadsPercent / 100.0 * totalHeight);
	  int twoTailsHeight = (int) (twoTailsPercent / 100.0 * totalHeight);
	  
	  
	  int x2 = (int) (currentWidth - barWidth) / this.midLocate;  // x coordinate for the middle bar
	  int y2 = (int)(maxHeight - oneHeadOneTailHeight);           // y coordinate for the middle bar
	  String label2 = "A Head and a Tail: " + oneHeadOneTailNum + "(" + oneHeadOneTailPercent +"%)";
	  Bar bar2 = new Bar(y2, x2, barWidth, oneHeadOneTailHeight, scaleValue, Color.GREEN, label2);
	  
	  int x1 = x2 - barWidth * this.leftLocate;                   // x coordinate for the left bar
	  int y1 = y2 + oneHeadOneTailHeight - twoHeadsHeight;        // y coordinate for the left bar
	  String label1 = "Two Heads: " + twoHeadsNum + "(" + twoHeadsPercent +"%)";
	  Bar bar1 = new Bar(y1, x1, barWidth, twoHeadsHeight, scaleValue, Color.RED, label1);
	  
	  int x3 = x2 + barWidth * this.rightLocate;                  // x coordinate for the right bar
	  int y3 = y2 + oneHeadOneTailHeight - twoTailsHeight;        // y coordinate for the right bar
	  String label3 = "Two Tails: " + twoTailsNum + "(" + twoTailsPercent +"%)";
	  Bar bar3 = new Bar(y3, x3, barWidth, twoTailsHeight, scaleValue, Color.BLUE, label3);

	  bar1.draw(g2);
	  bar2.draw(g2);
	  bar3.draw(g2);
   }
}
