function search(nums: number[], target: number): number {
    let start = 0;
    let end = nums.length - 1;

    while (start <= end){
        const m = Math.floor((start + end) / 2);
        const mid = nums[m];
        
        if (mid === target){
            return m
        }
        else if (mid < target){
            start = m + 1
        }
        else {
            end = m - 1
        }
    }

    return -1
};