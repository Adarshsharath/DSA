

char* intToRoman(int num) {
    int val[] = {1000, 900, 500, 400, 100, 90, 50,
                 40, 10, 9, 5, 4, 1};

    char *rom[] = {"M", "CM", "D", "CD", "C", "XC", "L",
                   "XL", "X", "IX", "V", "IV", "I"};

    char *ans = malloc(20);
    ans[0] = '\0';

    for (int i = 0; i < 13; i++) {
        while (num >= val[i]) {
            strcat(ans, rom[i]);
            num -= val[i];
        }
    }

    return ans;
}