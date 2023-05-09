class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }

        int[] charcount = new int[26];
        for (int i = 0; i < s.length(); i++){
             int idx = (int) s.charAt(i);
             charcount[idx-97] += 1;

             idx = (int) t.charAt(i);
             charcount[idx-97] -= 1;
        }

        for (int i: charcount){
            if (i!=0)
            return false;
        }
        return true;
    }
}