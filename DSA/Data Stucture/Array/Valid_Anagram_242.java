class Solution {
    public boolean isAnagram(String s, String t) {
            // char[] arr1= s.toCharArray();
            // char[] arr2= t.toCharArray();

            // Arrays.sort(arr1);
            // Arrays.sort(arr2);

            // return Arrays.equals(arr1,arr2);
     


        int m=s.length();
        int n=t.length();
        if(m!=n){
            return false;//Checking both strings are equal or not
        }
        else{
        int count[]=new int[26];
        for(int i=0;i<m;i++){
            count[s.charAt(i)-'a']++;       // Count the frequency of characters in string s
        }
        for(int i=0;i<n;i++){
            count[t.charAt(i)-'a']--;     // Count the frequency of characters in string t
        }
        for(int i=0;i<count.length;i++){    // Check if any character has non-zero frequency
            if(count[i]!=0){
                return false;
            }
        }
            return true;
        }
        
    }
}
 