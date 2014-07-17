package com.ats.technicalscreen.ishappyprime;

import com.ats.technicalscreen.arraycontainsduplicates.ArrayContainsDuplicates;

/**
 * ===== Happy Primes ======
 * Background:
 * In the 2007 Doctor Who episode "42", a sequence of happy primes (313, 331, 367, 379) is used as a code for unlocking a sealed door on a spaceship 
 * about to collide with a star. When the Doctor learns that nobody on the spaceship besides himself has heard of happy numbers, he asks, 
 * "Don't they teach recreational mathematics anymore?"
 *  
 * Happy Prime Definition:
 *    A happy prime is a number that is both 'prime' and 'happy'
 *  
 * Happy Number Definition:  
 *    A 'happy' number is defined by the following process - starting with any positive integer, replace the number by the sum of the squares of its digits, 
 *    and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
 * 
 * Happy Number Examples: 
 * a) 19 is happy
 *    19    
 *    1^2 + 9^2 = 82
 *    8^2 + 2^2 = 68
 *    6^2 + 8^2 = 100
 *    1^2 + 0^2 + 0^2 = 1 ===> Happy!!!! :-)
 *    
 * b) 4 is not happy (and results in a cycle)
 *    4
 *    4^2 = 16
 *    1^2 + 6^2 = 37
 *    3^2 + 7^2 = 58 
 *    5^2 + 8^2 = 89
 *    8^2 + 9^2 = 145
 *    1^2 + 4^2 + 5^2 = 42
 *    4^2 + 2^2 = 20
 *    2^2 + 0^2 = 4 ===> Cycle!!! Not Happy :-(
 * 
 */
public class IsHappyPrime {

	/**
	 * Determines whether the input value is a "happy prime" 
	 * e.g., a prime number that is also a happy number
	 * 
	 * @param input The input value
	 * @return Whether the input value is a happy prime
	 */
	boolean isHappyPrime(int input) {
		int j = 0;
		while((j=getHappy(input))/10!=0)       //   You have to check the sum of all digits until a single digit is achieved i.e. sum=1,2,3,..9
		{
			input=j;                // If sum of digits= 19 it then again goes to 1+9 =10 and again 1+0= '1' a single digit to check if 1 or not
		}
		if ( j==1)
		System.out.println("It is a happy number ");
		else
		System.out.println("Not a happy number");
				
		return false;
	}
	
	int getHappy(int number){
		
		// reached the exit condition
//		if(number == 1)
//			return 1;
		
		if(number/10 == 0)
			return number * number;
		
		int lastPart = number%10;
		int firstPart = number/10;
		
//		System.out.println(lastPart);
//		System.out.println(firstPart);
		return lastPart*lastPart + getHappy(firstPart);
	}
	
	public static void main(String args[]){
		
		IsHappyPrime dup = new IsHappyPrime();
		System.out.println(dup.isHappyPrime(19));
	}
}
