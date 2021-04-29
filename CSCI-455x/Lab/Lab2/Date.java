package cs_455_lab2;
import java.time.LocalDate; // Question 1.1

public class Date 
{
	public static void main(String[] args)
	{
		// Question 1.2
		LocalDate myDate = LocalDate.of(1995, 1, 20); // Year, month, day
		// Question 1.3
		System.out.println("DEBUG:" + myDate);
		System.out.println(myDate.getMonthValue() + "/" 
				   + myDate.getDayOfMonth() + "/" 
				   + myDate.getYear());
		// Question 1.4
		LocalDate later = myDate.plusDays(20);
		System.out.println(later.getMonthValue() + "/" 
		           + later.getDayOfMonth() + "/" 
		           + later.getYear());
		// Question 1.5
		myDate = myDate.plusDays(20);
		System.out.println(myDate.getMonthValue() + "/" 
		           + myDate.getDayOfMonth() + "/" 
		           + myDate.getYear());
	}

}