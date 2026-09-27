class Solution {
public:
    bool isPowerOfTwo(int n) {
        return n > 0 && (n & (n-1)) == 0;       //Works when only a single bit is "1", meaning that it is a power of 2
    };
};