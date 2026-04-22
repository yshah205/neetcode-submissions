class Solution {
    public int longestConsecutive(int[] nums) {

    Arrays.sort(nums);
    int count = 1;
   int j = 1;

    int maxCount = 0;
    if (nums.length == 0) {
        return 0;
    }

    for (int i = 0; i < nums.length && j < nums.length; i++, j++) {

        if (nums[i] == nums[j]) {
            continue;
        }
        if (nums[i] + 1 == nums[j] ) {
            count++;
        } else {
            maxCount = Math.max(maxCount, count);
            count = 1; 
        }
    }
    maxCount = Math.max(maxCount, count);

    return maxCount;
    }
}
