# implementing two sum problem on sorted array using two pointers technique 

import random
import unittest

def twoSumSortedArray_twoPointers(arr,target):
    n = len(arr)
    left = 0
    right = n-1
    while left<right:
        total = arr[left]+arr[right]
        if total==target:
            return [left,right]
        elif total<target:
            left += 1
        else:
            right -= 1
    return []

# test cases 

class TestTwoSumSortedArrayTwoPointers(unittest.TestCase):

    ## 1. empty array 
    def test_empty_array(self):
        self.assertEqual(twoSumSortedArray_twoPointers([],5),[])

    ## 2. array with only one element
    def test_single_element(self):
        self.assertEqual(twoSumSortedArray_twoPointers([3],3),[])

    ## 3. array with two elements - target match 
    def test_two_elements_with_match(self):
        self.assertEqual(twoSumSortedArray_twoPointers([3,6],9),[0,1])

    ## 4. array with two elements - no target match 
    def test_two_elements_with_no_match(self):
        self.assertEqual(twoSumSortedArray_twoPointers([2,5],9),[])
    
    ## 5. array with two elements - both are same with match 
    def test_two_same_elements_with_match(self):
        self.assertEqual(twoSumSortedArray_twoPointers([3,3],6),[0,1])

    ## 6. array with two elements - both are same with no match 
    def test_two_same_elements_with_no_match(self):
        self.assertEqual(twoSumSortedArray_twoPointers([3,3],7),[])
    
    ## 7. array with no target match
    def test_no_match(self):
        self.assertEqual(twoSumSortedArray_twoPointers([1,2,3,4,5,6],2),[]) 

    ## 8. target is zero 
    def test_target_zero(self):
        self.assertEqual(twoSumSortedArray_twoPointers([-3, -1, 0, 2, 3], 0), [0, 4])
    
    ## 9. array with negative numbers 
    def test_all_negatives(self):
        self.assertEqual(twoSumSortedArray_twoPointers([-5, -4, -3, -2], -7), [0, 3])
    
    ## 10. array with positive and negative numbers
    def test_mixed_negative_positive(self):
        self.assertEqual(twoSumSortedArray_twoPointers([-3, 1, 2, 4], 1), [0, 3])

    ## 11. array with all same elements - match 
    def test_all_same_match(self):
        self.assertEqual(twoSumSortedArray_twoPointers([2, 2, 2, 2], 4), [0, 3])


    ## 12. array with all same elements - no match 
    def test_all_same_no_match(self):
        self.assertEqual(twoSumSortedArray_twoPointers([2, 2, 2, 2], 5), [])


    ## 13. answer is first and last element
    def test_first_and_last(self):
        self.assertEqual(twoSumSortedArray_twoPointers([1, 3, 5, 7], 8), [0, 3])


    ## 14. answer is two adjacent elements
    def test_adjacent_elements(self):
        self.assertEqual(twoSumSortedArray_twoPointers([1, 3, 5, 7], 12), [2, 3])

    ## 15. array with large numbers
    def test_large_numbers(self):
        result = twoSumSortedArray_twoPointers([10**9 - 1, 10**9], 2 * 10**9 - 1)
        self.assertEqual(result, [0, 1])


    ## 16. target smaller than smallest possible sum
    def test_target_too_small(self):
        self.assertEqual(twoSumSortedArray_twoPointers([3, 5, 7, 9], 4), [])


    ## 17. target larger than largest possible sum 
    def test_target_too_large(self):
        self.assertEqual(twoSumSortedArray_twoPointers([1, 2, 3, 4], 10), [])

    ## 18. array with duplicate elements - with match
    def test_duplicates_multiple_pairs(self):
        result = twoSumSortedArray_twoPointers([1, 2, 2, 3], 4)
        nums = [1, 2, 2, 3]
        self.assertEqual(nums[result[0]] + nums[result[1]], 4)


if __name__== "__main__":
    unittest.main(verbosity=2)






