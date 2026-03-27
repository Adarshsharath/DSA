//Learning here we were returning double so we should divide by 2.0 not just 2
//Here i created a helper function merge which merges two sorted arrays and retrun array
//Then using simple logic i returned median :))

int* merge(int* nums1,int nums1Size,int* nums2,int nums2Size){
    int i = 0,j=0,k=0;
    int total = nums1Size+nums2Size;
    int* arr = malloc(total*sizeof(int));
    while(i<nums1Size && j<nums2Size){
        if (nums1[i]<=nums2[j]){
            arr[k]=nums1[i];
            i++;
        }
        else if (nums1[i]>nums2[j]){
            arr[k]=nums2[j];
            j++;
        }
        k++;
    }
    while (i < nums1Size) {
        arr[k++] = nums1[i++];
    }

    while (j < nums2Size) {
        arr[k++] = nums2[j++];
    }
    return arr;
}
double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int* result = merge(nums1,nums1Size,nums2,nums2Size);
    int total = nums1Size + nums2Size;
    if (total%2==0){
        return ((result[total/2]+result[(total/2)-1])/2.0);
    }
    else{
        return (result[total/2]);
    }   
}