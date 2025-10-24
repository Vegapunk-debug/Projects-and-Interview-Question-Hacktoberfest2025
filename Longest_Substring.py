Python Intermediate Problem: Find the Longest Substring Without Repeating Characters
📝 Problem Statement

Given a string s, find the length of the longest substring without repeating characters.

Example:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Intuition

We need to find a contiguous substring with all unique characters.
A sliding window approach helps here — we move a window along the string and adjust its start whenever we find a duplicate character.

This ensures we never re-check characters unnecessarily.

Approach
Use a set to store unique characters in the current window.
Use two pointers — left and right — to represent the window boundaries.
Move right to expand the window, and if a duplicate appears, move left until the duplicate is removed.
Keep track of the maximum window size seen so far.

Python Solution:
def length_of_longest_substring(s):
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        # If a duplicate is found, shrink the window from the left
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        
        # Add current character and update max length
        seen.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

Example:
Input:
s = "pwwkew"
Output: 3 (substring = "kew")

Complexity Analysis:
Type	Complexity
Time Complexity	O(n) — each character visited at most twice
Space Complexity	O(k) — where k is the number of unique characters
