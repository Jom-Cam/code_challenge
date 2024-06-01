let input = [2,95,5,7,11,15,8]
let target = 9

function sortDecending(arr) {
  arr.sort((a,b)=>a-b); 
  // read into sort method for better explenation
  // Read about anon function and callback
  arr.reverse();
  return arr;
}

function twoSum(nums, target) {
  original_arr = nums

  sortDecending(nums)

  let my_indexes =  []
  let comparitive_num = 0

  // Array has now been reversed in decending order from [ 2, 95, 5, 7, 11, 15 ] => [ 95, 15, 11, 7, 5, 2 ] 
  // Now we need to find the largest number the target will fit into 

  for (let i = 0; i < nums.length; i++) {
      let comparitive_num = target

      // is compatitive num needed? when is it being used?
      // Needs error handling when a larger number fits into the target without its matching smaller number 

      if (target - nums[i] >= 0) {
        if (nums.includes(target-nums[i]) == true || target-nums[i] == 0) {
            target -= nums[i]
            my_indexes.push(nums[i])
            console.log(`this is the number that fits in the target ${nums[i]}`)
            console.log(`This is the new target ${target}`)
        }
          if (my_indexes.length >= 2) { 
            console.log(`[ ${original_arr.indexOf(my_indexes[0])} , ${original_arr.indexOf(my_indexes[1])} ]`) 
          }
      }

  }
};

twoSum(input, target)