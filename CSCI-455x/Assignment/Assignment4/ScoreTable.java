// Name: Yao Fu
// USC NetID: yaof
// CS 455 PA4
// Spring 2021

/**
 * This class has information about Scrabble scores for scrabble letters and words. In scrabble not
 * every letter has the same value. Letters that occur more often in the English language are worth
 * less (e.g., 'e' and 's' are each worth 1 point), and letters that occur less often are worth more
 * (e.g., 'q' and 'z' are worth 10points each). Here are all the letter values:
 * (1 point) - A, E, I, O, U, L, N, S, T, R
 * (2 points) - D, G
 * (3 points) - B, C, M, P
 * (4 points) - F, H, V, W, Y
 * (5 points) - K
 * (8 points) - J, X
 * (10 points) - Q, Z
 * This class should work for both upper and lower case versions of the letters, e.g., 'a' and 'A' will
 * have the same score.
 */

public class ScoreTable {
   private String targetString;
   private static final int POINTS_0 = 0;
   private static final int POINTS_1 = 1;
   private static final int POINTS_2 = 2;
   private static final int POINTS_3 = 3;
   private static final int POINTS_4 = 4;
   private static final int POINTS_5 = 5;
   private static final int POINTS_8 = 8;
   private static final int POINTS_10 = 10;

   /**
    * Creates a ScoreTable to calculate the score of the given string in terms of
    * the criterion above.
    *
    * Representation invariant:
    * The given string should only contain English letters no matter whether they
    * are upper or lower case versions.
    *
    * @param inString  the given string whose score is to be calculated.
    */
   public ScoreTable(String inString){
      this.targetString = inString;
   }

   /**
    * Gets the score value of the given string.
    *
    * @return the score value.
    */
   public int getScore(){
      int finalScore = 0;
      char[] tempArray = this.targetString.toCharArray();
      for (char c : tempArray) {
         if (c == 'A' || c == 'a' || c == 'E' || c == 'e'
               || c == 'I' || c == 'i' || c == 'O' || c == 'o'
               || c == 'U' || c == 'u' || c == 'L' || c == 'l'
               || c == 'N' || c == 'n' || c == 'S' || c == 's'
               || c == 'T' || c == 't' || c == 'R' || c == 'r') {
            finalScore += POINTS_1;
         } else if (c == 'D' || c == 'd' || c == 'G' || c == 'g') {
            finalScore += POINTS_2;
         } else if (c == 'B' || c == 'b' || c == 'C' || c == 'c'
               || c == 'M' || c == 'm' || c == 'P' || c == 'p') {
            finalScore += POINTS_3;
         } else if (c == 'F' || c == 'f' || c == 'H' || c == 'h'
               || c == 'V' || c == 'v' || c == 'W' || c == 'w'
               || c == 'Y' || c == 'y') {
            finalScore += POINTS_4;
         } else if (c == 'K' || c == 'k') {
            finalScore += POINTS_5;
         } else if (c == 'J' || c == 'j' || c == 'X' || c == 'x') {
            finalScore += POINTS_8;
         } else if (c == 'Q' || c == 'q' || c == 'Z' || c == 'z') {
            finalScore += POINTS_10;
         } else {
            System.out.println("ERROR: This isn't a letter!");
            finalScore += POINTS_0;
         }
      }

      return finalScore;
   }
}
