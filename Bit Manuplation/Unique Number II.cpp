class Solution {
  public:
    vector<int> singleNum(vector<int>& arr) {
        // Code here.
        int xorAll=0;
        for(int num : arr)
        {
            xorAll ^=num;
        }
        int diffBit=xorAll & -xorAll;
        int x=0,y=0;
        for(int num : arr)
        {
            if (num & diffBit)
            x ^= num;
            else
            y ^= num;
        }
        if(x<y)
        return {x,y};
        else
        return {y,x};
    }
};