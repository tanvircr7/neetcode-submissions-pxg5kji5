public class Solution {
    public void ReverseString(char[] s) {
        char[] tmp = new char[s.Length];
        int n = s.Length;
        int mid = n/2;

        for (int i=0; i<mid; i++) {
            char tmpX = s[i];
            s[i] = s[n-1-i];
            s[n-1-i] = tmpX;
        }

    }
}