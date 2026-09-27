class Solution {
public:
    bool isPowerOfTwo(int n) {
        long long ans = 1;

        while (ans <= n) {
            if (ans == n) {
                return true;
            }

            ans <<= 1;
        }

        return false;
    }
};