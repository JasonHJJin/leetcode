import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/*******************************************************************************
 * Name : BinaryTreeRightSideView.java
 * Author : Brian S. Borowski
 * Version : 1.0
 * Date : July 22, 2021
 * Last modified : July 21, 2022
 * Description : Solution to LeetCode 199
 * Binary Tree Right Side View
 ******************************************************************************/

public class TreeNode{
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }

    public static void main(String[] args) {
        TreeNode tn = new TreeNode();
        Solution s = new Solution();
        s.rightSideView(tn);

        System.out.println("asdf");
    }

}

class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> rightSideValues = new ArrayList<>();

        // If the root is null, we must return the empty List.
        if (root == null) {
            return rightSideValues;
        }

        // Create Queue object and insert root to start.
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);

        // Loop while TreeNodes remain in Queue
        while (!q.isEmpty()) {
            // The size of the queue at this stage is how many elements to
            // consume before we reach the rightmost TreeNode.
            // Store the size.
            int queueSize = q.size();

            while (queueSize > 0) {
                // Every loop, decrement queueSize and remove one TreeNode from
                // the queue. Store removed TreeNode in temporary variable node.
                queueSize--;
                TreeNode node = q.poll();

                // If queueSize is 0, we have reached the end of this level.
                // Add the value of the TreeNode that was just polled.
                if (queueSize == 0) {
                    rightSideValues.add(node.val);
                }

                // Offer left and right nodes to the queue, in that order,
                // as long as they exist.
                if (node.left != null) {
                    q.offer(node.left);
                }
                if (node.right != null) {
                    q.offer(node.right);
                }
            }
        }
        // Algorithm is finished, return accumulated values.
        return rightSideValues;
    }
}
