class Solution {
  public:
    int kthElement(vector<int> &a, vector<int> &b, int k) {
        int n = a.size(), m = b.size();

        // Ensure a is the smaller array
        if (n > m) return kthElement(b, a, k);

        int low = max(0, k - m), high = min(k, n);

        while (low <= high) {
            int cutA = (low + high) / 2;
            int cutB = k - cutA;

            int l1 = (cutA == 0) ? INT_MIN : a[cutA - 1];
            int l2 = (cutB == 0) ? INT_MIN : b[cutB - 1];
            int r1 = (cutA == n) ? INT_MAX : a[cutA];
            int r2 = (cutB == m) ? INT_MAX : b[cutB];

            if (l1 <= r2 && l2 <= r1)
                return max(l1, l2);
            else if (l1 > r2)
                high = cutA - 1;
            else
                low = cutA + 1;
        }

        return -1; // Should never reach here
    }
};
