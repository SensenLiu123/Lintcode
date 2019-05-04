public class Solution {
    /**
     * @param str: A string
     * @return: A string
     */
    public String lowercaseToUppercase2(String str) {
        // write your code here
        char [] charList =  str.toCharArray();
        
        for (int i = 0; i < charList.length; i ++ ) {
            if (!Character.isLetter (charList[i]) ){
                continue;
            }
            
            charList[i] = Character.toUpperCase(charList[i]);
        }
        
        String ans = new String (charList);
       
        return ans;
    }
}