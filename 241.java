public class Solution {
    /**
     * @param str: A string
     * @return: An integer
     */
    public int stringToInteger(String str) {
        
        // return Integer.valueOf(str);

        if (str == null || str.isEmpty() ){
            return 0;
        }
        
        int negative = 0; 
        if (str.charAt(0) == '-'){
            negative = 1;
        }
        
    
        
        int ans = 0;
        for (int i = negative; i < str.length(); i ++) {
            ans = ans * 10 + str.charAt(i) - '0';
        }
        
        if (negative == 1){
            ans = ans * -1;
        }
        return ans;
    }
}