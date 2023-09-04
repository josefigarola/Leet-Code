class Solution {
public:
    int lengthOfLastWord(string s) {
        int p1 = 0;
        int n = 0;

        while(p1 < s.length()){
            if(s[p1] != ' '){
                n++;
            }
            else if(p1+1 < s.length() && s[p1+1] != ' '){
                n = 0;
            }
            p1++;
        }
        return n;
        
    }
};