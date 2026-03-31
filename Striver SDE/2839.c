//this checks if |j-i|=2 and compares both strings at i and j respectively also it checked ith and jth position of itself
#include <stdbool.h>

bool canBeEqual(char* s1, char* s2) {

    // check even indices (0 and 2)
    if (!((s1[0] == s2[0] && s1[2] == s2[2]) ||
          (s1[0] == s2[2] && s1[2] == s2[0]))) {
        return false;
    }

    // check odd indices (1 and 3)
    if (!((s1[1] == s2[1] && s1[3] == s2[3]) ||
          (s1[1] == s2[3] && s1[3] == s2[1]))) {
        return false;
    }

    return true;
}