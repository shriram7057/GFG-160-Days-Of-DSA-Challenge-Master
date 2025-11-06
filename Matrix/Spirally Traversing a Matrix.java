import java.util.*;

class Solution {
    public ArrayList<Integer> spirallyTraverse(int[][] mat) {
        ArrayList<Integer> result = new ArrayList<>();
        int top = 0, bottom = mat.length - 1;
        int left = 0, right = mat[0].length - 1;

        while (top <= bottom && left <= right) {
            // Traverse top row
            for (int i = left; i <= right; i++)
                result.add(mat[top][i]);
            top++;

            // Traverse right column
            for (int i = top; i <= bottom; i++)
                result.add(mat[i][right]);
            right--;

            // Traverse bottom row
            if (top <= bottom) {
                for (int i = right; i >= left; i--)
                    result.add(mat[bottom][i]);
                bottom--;
            }

            // Traverse left column
            if (left <= right) {
                for (int i = bottom; i >= top; i--)
                    result.add(mat[i][left]);
                left++;
            }
        }

        return result;
    }
}
