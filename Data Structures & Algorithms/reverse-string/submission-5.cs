public class Solution {
    public void ReverseString(char[] s) {
        char[] tmp = new char[s.Length];
        int n = s.Length;

        for (int i=0; i<n; i++) {
            tmp[i] = s[n-1-i];
        }

        for (int i=0; i<n; i++) {
            s[i] = tmp[i];
        }

    }
}