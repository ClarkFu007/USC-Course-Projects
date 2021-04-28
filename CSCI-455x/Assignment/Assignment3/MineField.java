// Name: Yao Fu
// USC NetID: yaof
// CS 455 PA3
// Spring 2021

import java.util.Arrays;
import java.util.Random;

/**
 * MineField
 * class with locations of mines for a game.
 * This class is mutable, because we sometimes need to change it once it's created.
 * mutators: populateMineField, resetEmpty
 * includes convenience method to tell the number of mines adjacent to a location.
 */
public class MineField {

   private int numMines = 0;         // number of mines
   private int numRows = 0;          // number of rows
   private int numCols = 0;          // number of columns
   private boolean[][] mineField;    // A 2d array to indicate mines
   private Random placeMines;        // A random generator to place mines

   private static final int PUT_Mine = 1;
   public static boolean HAS_MINE = true;
   public static boolean HAS_NO_MINE = false;


   /**
    * Create a minefield with same dimensions as the given array, and populate it with the mines in the array
    * such that if mineData[row][col] is true, then hasMine(row,col) will be true and vice versa. numMines() for
    * this minefield will corresponds to the number of 'true' values in mineData.
    *
    * Representation invariant:
    * The object can be in two different states: either hasMine (the boolean array) is completely false OR
    * numMines == (the number of true locations in hasMine).
    *
    * @param mineData  the data for the mines; must have at least one row and one col,
    *                  and must be rectangular (i.e., every row is the same length)
    */
   public MineField(boolean[][] mineData) {
      this.numRows = mineData.length;
      this.numCols = mineData[0].length;
      this.mineField = new boolean[this.numRows][this.numCols];
      defensiveCopy(mineData);
      countMineNumbers(numRows(), numCols());;
      this.placeMines = new Random();
   }
   
   
   /**
    * Create an empty minefield (i.e. no mines anywhere), that may later have numMines mines (once
    * populateMineField is called on this object). Until populateMineField is called on such a MineField,
    * numMines() will not correspond to the number of mines currently in the MineField.
    *
    * @param numRows  number of rows this minefield will have, must be positive.
    * @param numCols  number of columns this minefield will have, must be positive.
    * @param numMines   number of mines this minefield will have, once we populate it.
    *
    * PRE: numRows > 0 and numCols > 0 and 0 <= numMines < (1/3 of total number of field locations).
    */
   public MineField(int numRows, int numCols, int numMines) {
      this.numRows = numRows;
      this.numCols = numCols;
      this.mineField = new boolean[numRows][numCols];
      this.numMines = numMines;
      this.placeMines = new Random();
   }
   

   /**
    * Removes any current mines on the minefield, and puts numMines() mines
    * in random locations on the minefield,
    * ensuring that no mine is placed at (row, col).
    *
    * @param row the row of the location to avoid placing a mine
    * @param col the column of the location to avoid placing a mine
    *
    * PRE: inRange(row, col) and numMines() < (1/3 * numRows() * numCols())
    */
   public void populateMineField(int row, int col) {
      resetEmpty();  // Resets the minefield to all empty squares
      int currentMineNums = 0;
      int randomNumber = numRows() * numCols() / this.numMines;
      while(currentMineNums != this.numMines){
         for(int i = 0; i < numRows(); i++){
            for(int j = 0; j < numCols(); j++){
               if (!(i == row && j == col)){
                  if (currentMineNums < this.numMines){
                     int putMineDirection = this.placeMines.nextInt(randomNumber);
                     if (putMineDirection == PUT_Mine && !this.mineField[i][j]){
                        this.mineField[i][j] = true;
                        currentMineNums++;
                     }
                  }
               }
            }
         }
      }
   }

   
   /**
    * Resets the minefield to all empty squares. This does not affect numMines(), numRows() or numCols().
    * Thus, after this call, the actual number of mines in the minefield does not match numMines().
    * Note: This is the state a minefield created with the three-arg constructor is in
    *       at the beginning of a game.
    */
   public void resetEmpty() {
      for (int i = 0; i < numRows(); i++){
         for (int j = 0; j < numCols(); j++){
            this.mineField[i][j] = HAS_NO_MINE;
         }
      }
   }

   
  /**
   * Returns the number of mines adjacent to the specified mine location (not counting a possible
   * mine at (row, col) itself).
   * Diagonals are also considered adjacent, so the return value will be in the range [0,8]
   *
   * @param row  row of the location to check
   * @param col  column of the location to check
   *
   * @return  the number of mines adjacent to the square at (row, col)
   *
   * PRE: inRange(row, col)
   */
   public int numAdjacentMines(int row, int col) {
      int adjMinesNum = 0;
      for (int i = -1; i <= 1; i++){
         for (int j = -1; j <= 1; j++){
            if (i != 0 || j != 0){
               int adjRow = row + i;
               int adjCol = col + j;
               if (inRange(adjRow, adjCol)){
                  if (hasMine(adjRow, adjCol)){
                     adjMinesNum++;
                  }
               }
            }
         }
      }
      return adjMinesNum;
   }
   
   
   /**
    * Returns true iff (row,col) is a valid field location. Row numbers and column numbers
    * start from 0.
    *
    * @param row  row of the location to consider.
    * @param col  column of the location to consider.
    *
    * @return whether (row, col) is a valid field location.
   */
   public boolean inRange(int row, int col) {
      if (row >= 0 && row < numRows()){
         return col >= 0 && col < numCols();
      }
      else{
         return false;
      }
   }
   
   
   /**
    * Returns the number of rows in the field.
    *
    * @return number of rows in the field
   */  
   public int numRows() {
      return this.numRows;
   }
   
   
   /**
    * Returns the number of columns in the field.
    *
    * @return number of columns in the field
   */    
   public int numCols() {
      return this.numCols;
   }
   
   
   /**
    * Returns whether there is a mine in this square.
    *
    * @param row  row of the location to check.
    * @param col  column of the location to check.
    *
    * @return whether there is a mine in this square.
    *
    * PRE: inRange(row, col)
   */    
   public boolean hasMine(int row, int col) {
      return this.mineField[row][col];
   }
   
   
   /**
    * Returns the number of mines you can have in this minefield. For mines created with the 3-arg constructor,
    * some of the time this value does not match the actual number of mines currently on the field. See doc for
    * that constructor, resetEmpty, and populateMineField for more details.
    *
    * @return number of mines
    */
   public int numMines() {
      return this.numMines;
   }


   /**
    * Prints the mine field for the purpose of testing.
    */
   public void printMineField() {
      // Loop through all rows
      for (boolean[] row : this.mineField)
         // converting each row as string
         // and then printing in a separate line
         System.out.println(Arrays.toString(row));
   }


   /**
    * Count the number of mines for the 1-arg constructor input case.
    *
    * @param row number of rows for the 2d matrix
    * @param col number of rows for the 2d matrix
    */
   private void countMineNumbers(int row, int col){
      for(int i = 0; i < row; i++){
         for(int j = 0; j < col; j++){
            if(mineField[i][j] == HAS_MINE){
               this.numMines ++;
            }
         }
      }
   }


   /**
    * Make a defensive copy of the 2d matrix, which is used only in the
    * 1-arg constructor input case.
    *
    * @param mineData the input 2d matrix.
    */
   private void defensiveCopy(boolean[][] mineData){
      for(int i =0; i < this.numRows; i++){
         for(int j = 0; j < this.numCols; j++){
            if(mineData[i][j] == HAS_MINE){
               this.mineField[i][j] = HAS_MINE;
            }
            else if(mineData[i][j] == HAS_NO_MINE){
               mineField[i][j] = HAS_NO_MINE;
            }
         }
      }
   }

}

