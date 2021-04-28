// Name: Yao Fu
// USC NetID: yaof
// CS 455 PA1
// Spring 2021

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.font.FontRenderContext;
import java.awt.geom.Rectangle2D;

/**
 * Bar class
 * A labeled bar that can serve as a single bar in a bar graph.
 * The text for the label is centered under the bar.
 * 
 * NOTE: The course staff have provided the public interface for this class. I didn't 
 * change the public interface and just added private instance variables, constants, 
 * and private methods to the class. I have also completed the implementation of
 * the methods given. 
 * 
 */
public class Bar 
{
   private final int barWidth;  // Width of the bar
   private final int barHeight; // Height of the bar
   private final int bottom;    // y coordinate
   private final int left;      // x coordinate
   private final double scale;  // scale value
   private final Color color;   // color for the bar
   private static final Color STRING_COLOR = Color.BLACK; // color for the string variable
   private final String label;  // label to indicate the bar
   
   /**
      Creates a labeled bar.
  
      @param bottom  y coordinate of the bottom bar
      @param left  x coordinate of the left side of the bar
      @param width  width of the bar (in pixels)
      @param barHeight  height of the bar in application units
      @param scale  how many pixels per application unit
      @param color  the color of the bar
      @param label  the label under the bar
   */
   public Bar(int bottom, int left, int width, int barHeight, 
              double scale, Color color, String label) 
   {
	   this.bottom = bottom;
	   this.left = left;
	   this.barWidth = width;
	   this.barHeight = barHeight;
	   this.scale = scale;
	   this.color = color;
	   this.label = label;
   }
   
   /**
      Draw the labeled bar.
      
      @param g2  the graphics context
   */
   public void draw(Graphics2D g2) 
   {
      g2.setColor(this.color);
	  int x = (int) (this.left / this.scale);
	  int y = (int) (this.bottom / this.scale);
	  int width = (int) (this.barWidth / this.scale);
	  int height = (int)(this.barHeight / this.scale);
	   
	  Rectangle bar = new Rectangle(x, y, width, height); // x, y, width, height
	  g2.fill(bar);
	  g2.setColor(this.STRING_COLOR);
	  
	  double adjustX = 0.25;  // Weights to adjust x coordinate
      double adjustY = 0.30;  // Weights to adjust y coordinate
	  g2.drawString(this.label, (int)(x - adjustX * width),(int)( y + height + adjustY * width));
   }
}
