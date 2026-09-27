class Solution {
public:
    void reverseString(vector<char>& s) {
        int left_ptr = 0;
        int right_ptr = s.size()-1;

        printf("%d", right_ptr);

        while(left_ptr < right_ptr){
            char temp = s[left_ptr];
            s[left_ptr] = s[right_ptr];
            s[right_ptr] = temp;

            left_ptr += 1;
            right_ptr -= 1;
        };
    };
};