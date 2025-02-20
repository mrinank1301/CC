#include<stdio.h>
#include<stdlib.h>

struct Node{
    int data;
    struct Node *left;
    struct Node *right;
};
int height(struct Node *root){
    if(root==NULL){
        return 0;
    }
    int leftHeight=height(root->left);
    int rightHeight=height(root->right);

    if(leftHeight>rightHeight){
        return leftHeight+1;
    }
    else{
        return rightHeight+1;
    }
}

struct Node* newNode(int data){
    struct Node *node=(struct Node*)malloc(sizeof(struct Node));
    node->data=data;
    node->left=NULL;
    node->right=NULL;
    return node;
}

int main(){
    struct Node *root=newNode(1);
    root->left=newNode(2);
    root->right=newNode(3);
    root->left->left=newNode(4);
    root->left->right=newNode(5);
    root->right->left=newNode(6);
    root->right->right=newNode(7);
    root->left->left->left=newNode(8);
    printf("%d",height(root));
    return 0;
}
