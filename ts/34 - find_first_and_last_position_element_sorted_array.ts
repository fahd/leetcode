function searchRange(nums: number[], target: number): number[] {
	function search(nums: number[], target:number, side: string) {
		let s = 0
		let e = nums.length - 1
		
		while (s <= e){
			const m = Math.floor((s + e) / 2);
			const mV = nums[m];
			if (side === 'left' && mV < target) s = m + 1
			else if (side === 'right' && mV <= target) s = m + 1
			else e = m - 1
		}
		return side === 'left' ? s : e
	}

	const left = search(nums, target, 'left')
	const right = search(nums, target, 'right')

	if (!(left <= right)) {
		return [-1,-1]
	}
	return [left, right]
};
