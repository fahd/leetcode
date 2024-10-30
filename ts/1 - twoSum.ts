function twoSum(nums: number[], target:number): number[] {
  const map:{
    [key:number]: number
  } = {}

  for (let i = 0; i < nums.length; i++){
    let diff = target - nums[i];
    if (map.hasOwnProperty(diff)){
      return [map[diff], i]
    }
    map[nums[i]]  = i
  }
  return []
}