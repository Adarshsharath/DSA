int *arr;
int k;

void preorder(struct TreeNode *root)
{
    if (root == NULL)
        return;

    arr[k++] = root->val;

    preorder(root->left);
    preorder(root->right);
}

int* preorderTraversal(struct TreeNode* root, int* returnSize)
{
    arr = (int *)malloc(1000 * sizeof(int));
    k = 0;

    preorder(root);

    *returnSize = k;

    return arr;
}