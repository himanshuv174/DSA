class Solution {
    public int[] leftRightDifference(int[] nums) {
        int n = nums.length;
        
        int[] leftSum = new int[n];
        int[] rightSum = new int[n];
        int[] answer = new int[n];
        
        if (n == 0)
        return answer;

        int sum1 = 0;
        int sum2 = 0;
        for(int i=0;i<n;i++){
            leftSum[i] = sum1;
            sum1 += nums[i];
            rightSum[n-1-i] = sum2;
            sum2 += nums[n-1-i];
        }
        for(int i=0;i<n;i++){
            answer[i] = Math.abs(leftSum[i] - rightSum[i]);
        }
        return answer;
    }
}