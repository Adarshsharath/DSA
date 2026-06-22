int addDigits(int num) {
    int sum = 0;
    int a = 0;
    while (num!=0){
        a = num%10;
        sum +=a;
        num = num/10;
    }
    if (sum/10!=0){
        return addDigits(sum);
    }
    return sum;
}