package com.ats.technicalscreen.arraycontainsduplicates;

import java.util.HashSet;
import java.util.Set;

public class ArrayContainsDuplicates {

	/**
	 * This method determines whether the input array contains any duplicate integers.
	 *
	 * TODO: The algorithmic complexity of my solution is O(n).
	 *
	 * @param input the input array
	 * @return Whether the array contains duplicates
	 *  
	 */
	public boolean containsDuplicates(int[] input) {
		Set<Integer> valueSet = new HashSet<Integer>();
		for(int value : input){
			
			if(!valueSet.add(value))
				return true;
		}
		return false;
	}
	
	public static void main(String args[]){
		
		ArrayContainsDuplicates dup = new ArrayContainsDuplicates();
		System.out.println(dup.containsDuplicates(new int[]{1,2,3,4,5,6,7}));
		System.out.println(dup.containsDuplicates(new int[]{1,2,3,1,5,6,7}));
	}
}
