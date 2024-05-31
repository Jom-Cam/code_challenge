let input = [2,95,5,7,11,15]
let target = 9

function sortDecending(arr) {
  arr.sort((a,b)=>a-b);
  arr.reverse();
  return arr;
}

function twoSum(nums, target) {
  original_arr = nums
  sortDecending(nums)

  let my_indexes =  []
  let comparitive_num = 0

  for (let i = 0; i < nums.length; i++) {
      let comparitive_num = target
      if (target - nums[i] >= 0) {
        my_indexes.push(parseInt(nums[i]))
        console.log(nums[i])
        target -= nums[i]
        console.log(target)
          if (my_indexes.length >= 2) { 
            console.log(`[ ${original_arr.indexOf(my_indexes[0])} , ${original_arr.indexOf(my_indexes[1])} ]`) 
          }
      }

  }
};

twoSum(input, target)