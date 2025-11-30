class Solution {
  public:
    int peakElement(vector<int> &arr) {
        int n = arr.size();
        int low = 0, high = n - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            bool leftOK = (mid == 0 || arr[mid] >= arr[mid - 1]);
            bool rightOK = (mid == n - 1 || arr[mid] >= arr[mid + 1]);

            if (leftOK && rightOK)
                return mid;

            // Move to the side with a bigger neighbor
            if (mid > 0 && arr[mid - 1] > arr[mid])
                high = mid - 1;
            else
                low = mid + 1;
        }

        return -1; // Should never reach here if array has at least one element
    }
};
