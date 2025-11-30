class Solution {
  public:
    int findMin(vector<int>& arr) {
        int low = 0, high = arr.size() - 1;

        while (low < high) {
            int mid = low + (high - low) / 2;

            // If mid element is greater than the rightmost, min is in right half
            if (arr[mid] > arr[high]) {
                low = mid + 1;
            }
            // Else, min is in left half including mid
            else {
                high = mid;
            }
        }

        return arr[low];
    }
};
