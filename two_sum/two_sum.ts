// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// You can return the answer in any order.

// Example 1:

// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
// Example 2:

// Input: nums = [3,2,4], target = 6
// Output: [1,2]
// Example 3:

// Input: nums = [3,3], target = 6
// Output: [0,1]
 

// Constraints:

// 2 <= nums.length <= 104
// -109 <= nums[i] <= 109
// -109 <= target <= 109
// Only one valid answer exists.
 
// Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


// Thought process 
// order the initial inputs given 
// store the second input 
// iterate through the array of numbers decending (highest number to lowest)
// find one that does not give back a decimal and note its location
// use the remaining number to loop throug the array of numbers again
// return with the 2 number locations. 
   

  const input = [2,7,11,15]
  const target = 9

function twoSum(nums, target) {
    
    let my_indexes =  []
    let comparitive_num = 0

    for (let i = 0; i < nums.length; i++) {
        let comparitive_num = target
        if (target - nums[i] > 0) {
          my_indexes.push(parseInt(nums[i]))
          console.log(`this is the current itteration ${i} `)
          console.log(nums[i])
          console.log(comparitive_num)
        }

    }
};

twoSum(input, target)