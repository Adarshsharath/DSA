#include <stdlib.h>
#include <string.h>

// Struct to store result
typedef struct {
    int length;
    int isPalindrome;
} Result;

// Function to check palindrome using indices
Result checkPalindrome(char* s, int start, int end) {
    Result res;
    res.length = end - start + 1;
    res.isPalindrome = 1;

    while (start < end) {
        if (s[start] != s[end]) {
            res.isPalindrome = 0;
            break;
        }
        start++;
        end--;
    }

    return res;
}

// Main function (LeetCode required)
char* longestPalindrome(char* s) {
    int n = strlen(s);

    // Edge case
    if (n == 0) return "";

    int maxLen = 0;
    int startIndex = 0;

    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {

            Result r = checkPalindrome(s, i, j);

            if (r.isPalindrome && r.length > maxLen) {
                maxLen = r.length;
                startIndex = i;
            }
        }
    }

    // Allocate memory for result
    char* result = (char*)malloc((maxLen + 1) * sizeof(char));

    for (int i = 0; i < maxLen; i++) {
        result[i] = s[startIndex + i];
    }

    result[maxLen] = '\0';

    return result;
}