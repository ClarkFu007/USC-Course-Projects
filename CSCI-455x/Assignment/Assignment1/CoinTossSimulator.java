// Name: Yao Fu
// USC NetID: yaof
// CS 455 PA1
// Spring 2021

import java.util.Random;

/**
 * class CoinTossSimulator:It has no graphical output or I/O to the console. 
 * 
 * Simulates trials of repeatedly tossing two coins and allows the user to access the
 * cumulative results.
 * 
 * Invariant: getNumTrials() = getTwoHeads() + getTwoTails() + getHeadTails()
 * 
 * Instruction:
 * 1. The run method to run a simulation of tossing a pair of coins for some number of trials.
 * 2. The accessors to get results of the simulation: getNumTrials, getTwoHeads, 
 * getTwoTails, and getHeadTails. 
 * 3. Subsequent calls to run add trials to the current simulation. 
 * 4. Call the reset method to reset the CoinTossSimulator to start a new simulation.
 * 
 * NOTE: The course staff have provided the public interface for this class. I didn't 
 * change the public interface and just added private instance variables, constants, 
 * and private methods to the class. I have also completed the implementation of
 * the methods given. 
 * 
 */
public class CoinTossSimulator 
{
	// Instance variables for the CoinTossSimulator class
	private Random coinToss;           // A coin toss simulator 
	private int twoHeadsNum = 0;       // The frequency of two heads
	private int oneHeadOneTailNum = 0; // The frequency of one head and one tail
	private int twoTailsNum = 0;       // The frequency of two tails
	private int trialNum = 0;          // The total number of trials
	
   /**
      Creates a coin toss simulator with no trials done yet.
   */ 
   public CoinTossSimulator() 
   {
      this.coinToss = new Random();
   }

   /**
      Runs the simulation for numTrials more trials. Multiple calls to this method
      without a reset() between them *add* these trials to the current simulation.
      
      @param numTrials  number of trials for simulation; must be an integer and >= 1
   */
   public void run(int numTrials) 
   {
      for (int trialCounter = 1; trialCounter <= numTrials; trialCounter++ )
      {
         // Get 0 or 1 with equal probability
         int case1 = this.coinToss.nextInt(2); 
         int case2 = this.coinToss.nextInt(2);
         int head = 1;
         int tail = 0;
          
         if ((case1 == head) && (case2== head)) 
         {
            this.twoHeadsNum ++;         // For the reault "two heads"
            this.trialNum ++;
         }
         else if ((case1 == tail) && (case2== tail)) 
         {
            this.twoTailsNum ++;         // For the reault "two tails"
            this.trialNum ++;
         }
         else 
         {
            this.oneHeadOneTailNum ++;   // For the reault "one head one tail"
            this.trialNum++;
         } 
      }
   }

   /**
      Get number of trials performed since last reset.
   */
   public int getNumTrials() 
   {
       return this.trialNum; 
   }

   /**
      Get number of trials that came up two heads since last reset.
   */
   public int getTwoHeads() 
   {
       return this.twoHeadsNum; 
   }

   /**
      Get number of trials that came up two tails since last reset.
   */  
   public int getTwoTails() 
   {
       return this.twoTailsNum; 
   }

   /**
      Get number of trials that came up one head and one tail since last reset.
   */
   public int getHeadTails() 
   {
       return this.oneHeadOneTailNum; 
   }

   /**
      Resets the simulation, so that subsequent runs start from 0 trials done.
    */
   public void reset() 
   {
		this.twoHeadsNum = 0;
		this.oneHeadOneTailNum = 0;
		this.twoTailsNum = 0;
		this.trialNum = 0;
   }
}
