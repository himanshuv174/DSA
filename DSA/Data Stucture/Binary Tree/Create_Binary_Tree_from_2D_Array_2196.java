/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode createBinaryTree(int[][] descriptions) {
        HashMap<Integer ,TreeNode > d  = new HashMap<>();
        HashMap<Integer, Integer> root = new HashMap<>();

        for(int[] i: descriptions){
            
            int parent = i[0];
            int child = i[1];
            int isLeft = i[2];

            if(!d.containsKey(parent)){
                d.put(parent, new TreeNode(parent));
            }

            if(!d.containsKey(child)){
                d.put(child, new TreeNode(child));
            }


            if(isLeft == 1){
                d.get(parent).left = d.get(child);
            }
            if(isLeft == 0){
                d.get(parent).right = d.get(child);
            }

            if(root.getOrDefault(parent,0)!= -1){
                root.put(parent,1);
            }

            root.put(child,-1);

        }

        int rootVal = 0;

        for (var entry : root.entrySet()){
            if(entry.getValue()==1){
                rootVal = entry.getKey();
                break;
            }
        }

        return d.get(rootVal);

    }
}