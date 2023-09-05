class Solution {
public:
    int strStr(string haystack, string needle) {
        int lengthhay = haystack.size();
        int lengthneedle = needle.size();
        int p1 = 0;

        while(p1 < lengthhay){
            // get a substring from position p1 to p1+lenghtneedle
            if(haystack.substr(p1,lengthneedle) == needle){
                // return position
                return p1;
            }
            p1++;
        }

        return -1;

    }
};