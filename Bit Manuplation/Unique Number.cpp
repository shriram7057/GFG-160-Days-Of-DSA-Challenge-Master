class Solution {
  public:
    int findUnique(vector<int> &arr) {
        // code here
        int result = 0;
        for (int num : arr)
        {
            result ^= num ;
            
        }
        return result;
    }
};