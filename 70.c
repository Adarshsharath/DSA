int arr[1000];

int climb(int n){

    if(arr[n] != -1)
        return arr[n];

    if(n == 1)
        return 1;

    if(n == 2)
        return 2;

    arr[n] = climb(n-1) + climb(n-2);

    return arr[n];
}

int climbStairs(int n) {

    for(int i = 0; i < 1000; i++) {
        arr[i] = -1;
    }

    return climb(n);
}