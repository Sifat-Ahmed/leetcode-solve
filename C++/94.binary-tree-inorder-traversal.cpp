/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:

    vector<int> result;

    void inorder_traverse(TreeNode* root){
        if (root == NULL) {
            return;
        }

        inorder_traverse(root->left);
        result.push_back(root->val);
        inorder_traverse(root->right);

    }

    vector<int> inorderTraversal(TreeNode* root) {

        inorder_traverse(root);
        return result;

    }
};