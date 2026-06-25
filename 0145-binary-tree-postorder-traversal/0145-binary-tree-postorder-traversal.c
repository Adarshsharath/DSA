int *arr;
int k;

void postorder(struct TreeNode *root)
{
    if (root == NULL)
        return;
    postorder(root->left);
    postorder(root->right);
    arr[k++] = root->val;
}

int* postorderTraversal(struct TreeNode* root, int* returnSize)
{
    arr = (int *)malloc(1000 * sizeof(int));
    k = 0;

    postorder(root);

    *returnSize = k;

    return arr;
}