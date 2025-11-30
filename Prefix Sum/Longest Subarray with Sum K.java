import java.util.*;

class Solution {
    public int longestSubarray(int[] arr, int k) {
        Map<Integer, Integer> prefixMap = new HashMap<>();
        int sum = 0, maxLen = 0;

        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];
            // Case 1: entire subarray from 0 to i has sum = k
            if (sum == k)
                maxLen = i + 1;

            // Case 2: subarray (prefix) exists with sum-k
            if (prefixMap.containsKey(sum - k)) {
                maxLen = Math.max(maxLen, i - prefixMap.get(sum - k));
            }

            // store first occurrence of prefix sum
            prefixMap.putIfAbsent(sum, i);
        }
        return maxLen;
    }
}
