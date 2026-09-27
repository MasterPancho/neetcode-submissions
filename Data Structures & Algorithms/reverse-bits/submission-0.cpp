class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        int i = 0;
        uint32_t res = 0;
        while(i < 32){
            if(((n >> i) & 1u) == 1){
                res |= (1u << (31-i));
            };
            i++;
        };
        return res;
    };

};


// We could have a loop where we change last bit with first bit, then second last with second first and so on...
