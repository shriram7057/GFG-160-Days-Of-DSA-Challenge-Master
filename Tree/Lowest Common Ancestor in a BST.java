/*
class Node {
    int data;
    Node left;
    Node right;

    Node(int data) {
        this.data = data;
        left = null;
        right = null;
    }
}
*/

class Solution {
    public Node LCA(Node root, Node n1, Node n2) {
        // code here
        int a=n1.data;
        int b=n2.data;
        
        while(root != null)
        {
            if (a < root.data && b < root.data)
            {
                root=root.left;
            }else if (a > root.data && b > root.data)
            {
                root=root.right;
            }else{
                return root;
            }
        }
        return null;
    }
}

