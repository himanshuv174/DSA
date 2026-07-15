class Solution {
    public int gcdOfOddEvenSums(int n) {
        int sumOdd = n*n;
        int sumEven = n*(n+1);
        // Everything divides 0
        if(sumOdd ==0 || sumEven ==0) 
            return 0;

        int result = 0;
        // Find Minimum of sumOdd sumOddnd sumEven
        if (sumOdd <= sumEven){
            result = sumOdd;
        }
        else {
           result = sumEven; 
        }

        while (result > 0) {
            if (sumOdd % result == 0 && sumEven % result == 0) {
                break;
            }
        result--;}
    // Return gcd of sumOdd sumOddnd sumEven
    return result;
    }
}