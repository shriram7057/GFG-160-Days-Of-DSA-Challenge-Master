// User function Template for Java
class Solution {
    public int findDuplicate(int[] arr) {
        // code here
        int slow = arr[0];
        int fast=arr[0];
        
        do
        {
            slow=arr[slow];
            fast=arr[arr[fast]];
        }while (slow!=fast);
        
        slow =arr[0];
        while(slow!=fast)
        {
            slow=arr[slow];
            fast=arr[fast];
        }
        return slow;
    }
}