// Name: Yao Fu
// USC NetID: yaof
// CS 455 PA1
// Spring 2021

/**
 * This class tests the CoinTossSimulator class. 
 * 
 * Instruction:
 * Just run the code and see the statements in the console to check
 * whether the implementation of the CoinTossSimulator class is
 * correct or not.
 * 
 */
public class CoinTossSimulatorTester 
{
   public static void main(String[] args)
   {
   	CoinTossSimulator coinTrial = new CoinTossSimulator();
	      
	   System.out.println("After constructor: ");
	   System.out.print("Number of trials [exp:0]: ");
	   System.out.println(coinTrial.getNumTrials());
	   System.out.print("Two-head tosses: ");
	   System.out.println(coinTrial.getTwoHeads());
	   System.out.print("Two-tail tosses: ");
	   System.out.println(coinTrial.getTwoTails());
	   System.out.print("One-head one-tail tosses: ");
	   System.out.println(coinTrial.getHeadTails());
	   System.out.print("Tosses add up correctly? ");
	   System.out.println(coinTrial.getNumTrials() == 0);
	   System.out.println();

	   coinTrial.run(1);
	   System.out.println("For the edge case, after run(1): ");
	   System.out.print("Number of trials [exp:1]: ");
	   System.out.println(coinTrial.getNumTrials());
	   System.out.print("Two-head tosses: ");
	   System.out.println(coinTrial.getTwoHeads());
	   System.out.print("Two-tail tosses: ");
	   System.out.println(coinTrial.getTwoTails());
	   System.out.print("One-head one-tail tosses: ");
	   System.out.println(coinTrial.getHeadTails());
	   System.out.print("Tosses add up correctly? ");
	   System.out.println(coinTrial.getNumTrials() == 1);
	   System.out.println();
	      
	   coinTrial.run(10);
	   System.out.println("After run(10): ");
	   System.out.print("Number of trials [exp:11]: ");
	   System.out.println(coinTrial.getNumTrials());
	   System.out.print("Two-head tosses: ");
	   System.out.println(coinTrial.getTwoHeads());
	   System.out.print("Two-tail tosses: ");
	   System.out.println(coinTrial.getTwoTails());
	   System.out.print("One-head one-tail tosses: ");
	   System.out.println(coinTrial.getHeadTails());
	   System.out.print("Tosses add up correctly? ");
	   System.out.println(coinTrial.getNumTrials() == 11);
	   System.out.println();
	      
	   coinTrial.run(100);
	   System.out.println("After run(100): ");
	   System.out.print("Number of trials [exp:111]: ");
	   System.out.println(coinTrial.getNumTrials());
	   System.out.print("Two-head tosses: ");
	   System.out.println(coinTrial.getTwoHeads());
	   System.out.print("Two-tail tosses: ");
	   System.out.println(coinTrial.getTwoTails());
	   System.out.print("One-head one-tail tosses: ");
	   System.out.println(coinTrial.getHeadTails());
	   System.out.print("Tosses add up correctly? ");
	   System.out.println(coinTrial.getNumTrials() == 111);
	   System.out.println();
	     
	   coinTrial.reset();
	   System.out.println("After reset: ");
	   System.out.print("Number of trials [exp:0]: ");
	   System.out.println(coinTrial.getNumTrials());
	   System.out.print("Two-head tosses: ");
	   System.out.println(coinTrial.getTwoHeads());
	   System.out.print("Two-tail tosses: ");
	   System.out.println(coinTrial.getTwoTails());
	   System.out.print("One-head one-tail tosses: ");
	   System.out.println(coinTrial.getHeadTails());
	   System.out.print("Tosses add up correctly? ");
	   System.out.println(coinTrial.getNumTrials() == 0);
	   System.out.println();
	      
	   coinTrial.run(1000);
	   System.out.println("After run(1000): ");
	   System.out.print("Number of trials [exp:1000]: ");
	   System.out.println(coinTrial.getNumTrials());
	   System.out.print("Two-head tosses: ");
	   System.out.println(coinTrial.getTwoHeads());
	   System.out.print("Two-tail tosses: ");
	   System.out.println(coinTrial.getTwoTails());
	   System.out.print("One-head one-tail tosses: ");
	   System.out.println(coinTrial.getHeadTails());
	   System.out.print("Tosses add up correctly? ");
	   System.out.println(coinTrial.getNumTrials() == 1000);
	   System.out.println();
	  
	   coinTrial.run(1000);
	   System.out.println("After run(1000): ");
	   System.out.print("Number of trials [exp:2000]: ");
	   System.out.println(coinTrial.getNumTrials());
	   System.out.print("Two-head tosses: ");
	   System.out.println(coinTrial.getTwoHeads());
	   System.out.print("Two-tail tosses: ");
	   System.out.println(coinTrial.getTwoTails());
	   System.out.print("One-head one-tail tosses: ");
	   System.out.println(coinTrial.getHeadTails());
	   System.out.print("Tosses add up correctly? ");
	   System.out.println(coinTrial.getNumTrials() == 2000);
	   System.out.println();
	  
	   CoinTossSimulator newCoinTrial = new CoinTossSimulator();
	   newCoinTrial.run(1000);
	   System.out.println("For a new instance, after run(1000): ");
	   System.out.print("Number of trials [exp:1000]: ");
	   System.out.println(newCoinTrial.getNumTrials());
	   System.out.print("Two-head tosses: ");
	   System.out.println(newCoinTrial.getTwoHeads());
	   System.out.print("Two-tail tosses: ");
	   System.out.println(newCoinTrial.getTwoTails());
	   System.out.print("One-head one-tail tosses: ");
	   System.out.println(newCoinTrial.getHeadTails());
	   System.out.print("Tosses add up correctly? ");
	   System.out.println(newCoinTrial.getNumTrials() == 1000);
	   System.out.println();
   }
}
