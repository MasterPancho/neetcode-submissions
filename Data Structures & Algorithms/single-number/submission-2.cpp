class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res = 0;
        for(int i =0; i < nums.size(); i++){
            res = (res ^ nums[i]);
        };

        return res;
    };
};


// 1. Go trhough the array
// 2. check if the number is repeated
// 3. if so, stop and go to the next number.




// We could have a hash set, and do a loop. Now:

// dic = {
//     7: 2
//     6: 2
//     8: 1
// }

// Output is the one number that has only "1".