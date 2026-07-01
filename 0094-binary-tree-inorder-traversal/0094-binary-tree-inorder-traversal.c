int *arr;
int k;

void inorder(struct TreeNode *root)
{
    if (root == NULL)
        return;

    

    inorder(root->left);
    arr[k++] = root->val;
    inorder(root->right);
}

int* inorderTraversal(struct TreeNode* root, int* returnSize)
{
    arr = (int *)malloc(1000 * sizeof(int));
    k = 0;

    inorder(root);

    *returnSize = k;

    return arr;
}