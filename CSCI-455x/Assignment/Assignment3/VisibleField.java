// Name: Yao Fu
// USC NetID: yaof
// CS 455 PA3
// Spring 2021

import java.awt.Point;
import java.util.Stack;

/**
 * VisibleField class
 *
 * This is the data that's being displayed at any one point in the game (i.e., visible field,
 * because it's what the user can see about the minefield).
 *
 * Client can call getStatus(row, col) for any square to find out the current display status.
 *
 * It actually has data about the whole current state of the game, including the underlying mine
 * field (getMineField()). Other accessors related to game status: numMinesLeft(), isGameOver().
 *
 * It also has mutators related to actions the player could do (resetGameDisplay(), cycleGuess(), uncover()),
 * and changes the game state accordingly.
 *
 * It, along with the MineField (accessible in mineField instance variable), forms the Model for the game
 * application, whereas GameBoardPanel is the View and Controller, in the MVC design pattern.
 *
 * It contains the MineField that it's partially displaying. That MineField can be accessed (or modified) from
 * outside this class via the getMineField accessor.
 */
public class VisibleField {
   // ----------------------------------------------------------   
   // The following public constants (plus numbers mentioned in comments below) are the possible states of one
   // location (a "square") in the visible field (all are values that can be returned by public method 
   // getStatus(row, col)).
   
   // The following are the covered states (all negative values):
   public static final int COVERED = -1;   // initial value of all squares
   public static final int MINE_GUESS = -2;
   public static final int QUESTION = -3;

   // The following are the uncovered states (all non-negative values):
   // values in the range [0,8] corresponds to number of mines adjacent to this square
   public static final int MINE = 9;      // this loc is a mine that hasn't been guessed already (end of losing game)
   public static final int INCORRECT_GUESS = 10;  // is displayed a specific way at the end of losing game
   public static final int EXPLODED_MINE = 11;   // the one you uncovered d by mistake (that caused you to lose)
   // ----------------------------------------------------------   

   private MineField mineField;
   private int [][] visibleField;
   private Stack<Point> positions;

   /**
    * Create a visible field that has the given underlying mineField.
    *
    * The initial state will have all the mines covered up, no mines guessed, and the game
    * not over.
    *
    * Representation invariants:
    * 1: visible 2d array has dimensions the same as its mineField.
    * 2.: for each valid location (i,j), visible[i][j] can take on any of the values described by the
    * constants in the range [QUESTION,EXPLODED_MINE].
    * 3: 0 <= numMinesGuessed <= mineField.numRows()*mineField.numCols()
    * 4: If we define numNonMines = (mineField.numRows() * mineField.numCols() - mineField.numMines()), then:
    * 0 <= numUncovered <= numNonMines.
    * 5: gameOver is true iff numUncovered = numNonMines
    *
    * @param mineField  the minefield to use for for this VisibleField
    */
   public VisibleField(MineField mineField) {
      this.mineField = mineField;  // Shouldn't make a defensive copy.
      this.visibleField = new int[mineField.numRows()][mineField.numCols()];
      resetGameDisplay();          // Make the object get its initial state
   }
   
   
   /**
    * Reset the object to its initial state (see constructor comments), using the same underlying
    * MineField.
   */     
   public void resetGameDisplay() {
      for (int i = 0; i < this.mineField.numRows(); i++) {
         for (int j = 0; j < this.mineField.numCols(); j++) {
            this.visibleField[i][j] = COVERED;
         }
      }
   }
  
   
   /**
    * That MineField can be accessed (or modified) from outside this class via the getMineField accessor.
    *
    * Returns a reference to the mineField that this VisibleField "covers".
    *
    * @return the minefield
    */
   public MineField getMineField() {
      return this.mineField;
   }
   
   
   /**
    * Returns the visible status of the square indicated.
    *
    * @param row  row of the square.
    * @param col  col of the square.
    *
    * @return the status of the square at location (row, col). See the public constants
    *         at the beginning of the class for the possible values that may be returned,
    *         and their meanings.
    *
    * PRE: getMineField().inRange(row, col)
    */
   public int getStatus(int row, int col) {
      return this.visibleField[row][col];
   }

   
   /**
    * Returns the the number of mines left to guess. This has nothing to do with whether
    * the mines guessed are correct or not. Just gives the user an indication of how
    * many more mines the user might want to guess. This value can be negative, if they
    * have guessed more than the number of mines in the minefield.
    *
    * @return the number of mines left to guess.
    */
   public int numMinesLeft() {
      int mineGuessNum = 0;
      for (int i = 0; i < this.mineField.numRows(); i++) {
         for (int j = 0; j < this.mineField.numCols(); j++) {
            if (this.visibleField[i][j] == MINE_GUESS){
               mineGuessNum++;
            }
         }
      }
      return this.mineField.numMines() - mineGuessNum;
   }
 
   
   /**
    * Cycles through covered states for a square, updating number of guesses as necessary.
    * Call on a COVERED square changes its status to MINE_GUESS; call on a MINE_GUESS
    * square changes it to QUESTION; call on a QUESTION square changes it to COVERED again;
    * call on an uncovered square has no effect.
    *
    * @param row  row of the square
    * @param col  col of the square
    *
    * PRE: getMineField().inRange(row, col)
    */
   public void cycleGuess(int row, int col) {
      if (getStatus(row, col) == COVERED){
         this.visibleField[row][col] = MINE_GUESS;
         return;
      }
      if (getStatus(row, col) == MINE_GUESS){
         this.visibleField[row][col] = QUESTION;
         return;
      }
      if (getStatus(row, col) == QUESTION){
         this.visibleField[row][col] = COVERED;
      }
   }

   
   /**
    * Uncovers this square and returns false iff you uncover a mine here.
    *
    * If the square wasn't a mine or adjacent to a mine, it also uncovers all the squares in
    * the neighboring area that are also not next to any mines, possibly uncovering a large region.
    *
    * Any mine-adjacent squares you reach will also be uncovered, and form
    * (possibly along with parts of the edge of the whole field) the boundary of this region.
    *
    * Does not uncover, or keep searching through, squares that have the status MINE_GUESS.
    *
    * Note: this action may cause the game to end: either in a win (opened all the non-mine squares)
    * or a loss (opened a mine).
    *
    * @param row  row of the square
    * @param col  column of the square
    * @return false   iff you uncover a mine at (row, col)
    *
    * PRE: getMineField().inRange(row, col)
    */
   public boolean uncover(int row, int col) {
      if (this.mineField.hasMine(row, col)){
         this.visibleField[row][col] = EXPLODED_MINE;
         return false;
      }
      else{
         this.positions = new Stack<Point>();
         searchSquares(row, col);  // Searches the region to uncover a large region
         return true;
      }
   }


   /**
    * Returns whether the game is over.
    * (Note: This is not a mutator.)
    *
    * @return whether game is over or not
    */
   public boolean isGameOver() {
      int unCoveredNum = 0;
      int targetNum = this.mineField.numRows() * this.mineField.numCols() - this.mineField.numMines();
      for (int i = 0; i < this.mineField.numRows(); i++) {
         for (int j = 0; j < this.mineField.numCols(); j++) {
            if (this.visibleField[i][j] == EXPLODED_MINE){
               for (int m = 0; m < this.mineField.numRows(); m++) {
                  for (int n = 0; n < this.mineField.numCols(); n++) {
                     if (this.visibleField[m][n] == MINE_GUESS && !this.mineField.hasMine(m ,n)){
                        this.visibleField[m][n] = INCORRECT_GUESS;
                     }
                     if ((this.visibleField[m][n] == COVERED || this.visibleField[m][n] == QUESTION)
                           && this.mineField.hasMine(m ,n)){
                        this.visibleField[m][n] = MINE;}
                  }
               }
               return true;
            }
            else if (isUncovered(i, j)){
               unCoveredNum++;
            }
         }
      }
      if (unCoveredNum == targetNum){
         for (int i = 0; i < this.mineField.numRows(); i++) {
            for (int j = 0; j < this.mineField.numCols(); j++) {
               if (!isUncovered(i, j)) {
                  this.visibleField[i][j] = MINE_GUESS;
               }
            }
         }
         return true;
      }
      else{
         return false;
      }
   }
 
   
   /**
    * Returns whether this square has been uncovered. (i.e., is in
    * any one of the uncovered states, vs. any one of the covered states).
    *
    * @param row of the square
    * @param col of the square
    *
    * @return whether the square is uncovered
    *
    * PRE: getMineField().inRange(row, col)
    */
   public boolean isUncovered(int row, int col) {
      return this.visibleField[row][col] != COVERED &&
            this.visibleField[row][col] != MINE_GUESS &&
            this.visibleField[row][col] != QUESTION;
   }


   /**
    * For the square that wasn't a mine or adjacent to a mine, use recursion to uncover all
    * the squares in the neighboring area that are also not next to any mines, possibly
    * uncovering a large region.
    *
    * Does not uncover, or keep searching through, squares that have the status MINE_GUESS.
    *
    * @param row  row of the square
    * @param col  column of the square
    *
    * PRE: getMineField().inRange(row, col)
    */
   private void searchSquares(int row, int col) {
      if (this.mineField.inRange(row, col)){
         Point newPos = new Point(col, row);
         this.positions.push(newPos);
      }

      if (!this.positions.isEmpty()){
         Point tempPos = this.positions.pop();
         int tempRow = tempPos.y;
         int tempCol = tempPos.x;
         if (this.visibleField[tempRow][tempCol] == COVERED){
            int tempNum = this.mineField.numAdjacentMines(tempRow, tempCol);
            this.visibleField[tempRow][tempCol] = tempNum;
            if (tempNum == 0){
               searchSquares(tempRow - 1, tempCol - 1);  // northwest
               searchSquares(tempRow - 1, tempCol);          // north
               searchSquares(tempRow - 1, tempCol + 1);  // northeast
               searchSquares(tempRow , tempCol - 1);          // west
               searchSquares(tempRow, tempCol + 1);           // east
               searchSquares(tempRow + 1, tempCol - 1);  // southwest
               searchSquares(tempRow + 1, tempCol);          // south
               searchSquares(tempRow + 1, tempCol + 1);  // southeast
            }
         }
      }
   }

}
