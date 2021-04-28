

public class MineFieldTester {
   public static void main(String[] var0) {
      boolean[][] almostEmptyMineField =
            {{false, false, false, false},
                  {false, false, false, false},
                  {false, false, false, false},
                  {false, true, false, false},
                  {false, true, false, false}};

      MineField mineField1 = new MineField(almostEmptyMineField);

      mineField1.populateMineField(3, 1);
      System.out.println("The initial mines are: ");

      System.out.println(mineField1.numRows());
      System.out.println(mineField1.numCols());
      System.out.println(mineField1.numMines());
      mineField1.resetEmpty();
      System.out.println(mineField1.numRows());
      System.out.println(mineField1.numCols());
      System.out.println(mineField1.numMines());
      System.out.println();

   }

}
