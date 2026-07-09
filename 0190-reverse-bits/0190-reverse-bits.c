

char* toBinary(int n) {
    char *binary = malloc(33 * sizeof(char));

    for (int i = 31; i >= 0; i--) {
        binary[i] = (n % 2) + '0';
        n = n / 2;
    }

    binary[32] = '\0';

    return binary;
}

void reverseBinary(char *binary) {
    int i = 0;
    int j = 31;

    while (i < j) {
        char temp = binary[i];
        binary[i] = binary[j];
        binary[j] = temp;

        i++;
        j--;
    }
}

int reverseBits(int n) {
    char *binary = toBinary(n);

    reverseBinary(binary);

    unsigned int ans = 0;

    for (int i = 0; i < 32; i++) {
        ans = ans * 2 + (binary[i] - '0');
    }

    free(binary);

    return ans;
}