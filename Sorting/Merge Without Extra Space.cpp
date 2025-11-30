class Solution {
  public:
    void mergeArrays(vector<int>& a, vector<int>& b) {
        int n = a.size(), m = b.size();
        int gap = (n + m + 1) / 2;

        while (gap > 0) {
            int i = 0, j = gap;

            while (j < n + m) {
                int val_i, val_j;

                if (i < n) val_i = a[i];
                else val_i = b[i - n];

                if (j < n) val_j = a[j];
                else val_j = b[j - n];

                if (val_i > val_j) {
                    if (i < n && j < n)
                        swap(a[i], a[j]);
                    else if (i < n && j >= n)
                        swap(a[i], b[j - n]);
                    else
                        swap(b[i - n], b[j - n]);
                }

                i++;
                j++;
            }

            gap = (gap == 1) ? 0 : (gap + 1) / 2;
        }
    }
};
