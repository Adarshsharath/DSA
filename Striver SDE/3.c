// I used the sliding window technique with two pointers: left and right,
// both initially at 0.

// I used an array (visited[256]) as a hashmap to track whether a character
// is already present in the current window.

// Since characters in C are stored as ASCII values, s[right] gives the ASCII
// value of the character (e.g., 'a' → 97), which is used as an index in visited[].

// As I iterate with the right pointer:
// - If the character is not visited, I mark it as visited and expand the window.
// - If a duplicate character is found (visited[s[right]] == 1),
//   I shrink the window from the left by unmarking visited[s[left]]
//   and incrementing left until the duplicate is removed.

// After adjusting the window, I calculate the current window length:
//     length = right - left + 1

// I update maxLen if the current length is greater.

// This ensures that at any time, the window contains only unique characters.
int lengthOfLongestSubstring(char *s)
{
    int visited[256] = {0}; // ASCII
    int left = 0, maxLen = 0;

    for (int right = 0; s[right] != '\0'; right++)
    {

        // If character already exists, shrink window
        while (visited[s[right]] == 1)
        {
            visited[s[left]] = 0;
            left++;
        }

        // Mark current character
        visited[s[right]] = 1;

        // Update max length
        int len = right - left + 1;
        if (len > maxLen)
            maxLen = len;
    }

    return maxLen;
}