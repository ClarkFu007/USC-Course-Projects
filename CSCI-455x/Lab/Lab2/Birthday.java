

import java.time.LocalDate;
import java.util.Scanner;

public class Birthday 
{
	@SuppressWarnings("resource")
	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);
		
		int month;
		System.out.println("Enter your birth month [1..12]:");
		month = input.nextInt();
		int day;
		System.out.println("Enter your birth day of month:");
		day = input.nextInt();
		int year;
		System.out.println("Enter your birth year [4-digit year]:");
		year = input.nextInt();
		
		LocalDate currentDate = LocalDate.now(); 
		//LocalDate birthday = LocalDate.of(year, month, day); // Year, month, day
		LocalDate birthdayOfYear = LocalDate.of(currentDate.getYear(), month, day); // Year, month, day
		
		if (birthdayOfYear.isAfter(currentDate))
		{
			System.out.println("Your birthday has not yet happened this year.");
		}
		else 
		{
			System.out.println("Your birthday has already happened this year.");
		}
		
		if (birthdayOfYear.isEqual(currentDate))
		{
			System.out.println("Happy Birthday!");
		}
	}
}
