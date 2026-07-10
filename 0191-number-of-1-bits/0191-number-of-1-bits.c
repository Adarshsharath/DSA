int int_to_bin(int n){
    char* bin = malloc(33*sizeof(char));
    bin[32] = '\0';
    int count = 0;
    for(int i = 31;i>=0;i--){
        if(n%2 == 1){
            count++;

        }
        bin[i]= (n%2) + '0';
        n = n/2;
    }
    return count;

}
int hammingWeight(int n) {
    int val = int_to_bin(n);
    return val;
    
}