class Solution {
    public String processStr(String s) {
        StringBuilder result = new StringBuilder();
        int n = s.length();

        for(int i=0; i<n; i++){
            if(s.charAt(i) == '*'){
                if(result.length() != 0){
                    result.deleteCharAt(result.length() - 1);
                }
            }
            else if (s.charAt(i) == '#'){
                result.append(result);
            }
            else if (s.charAt(i) == '%'){
                result.reverse();
            }
            else if (s.charAt(i) >= 'a' && s.charAt(i) <= 'z'){
                result.append(s.charAt(i));
            }
        }
        return result.toString();
    }

}
