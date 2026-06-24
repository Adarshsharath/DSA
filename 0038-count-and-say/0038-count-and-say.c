char* countAndSay(int n) {
    static char curr[5000];
    static char next[5000];

    strcpy(curr, "1");

    for (int i = 2; i <= n; i++) {
        int k = 0;

        for (int j = 0; curr[j] != '\0'; ) {
            int count = 1;

            while (curr[j] == curr[j + 1]) {
                count++;
                j++;
            }

            next[k++] = count + '0';  // store count
            next[k++] = curr[j];      // store digit

            j++;
        }

        next[k] = '\0';
        strcpy(curr, next);
    }

    return curr;
}