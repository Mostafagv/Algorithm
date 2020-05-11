"""
https://leetcode.com/problems/longest-palindromic-substring/


mat[i][j] = 1 if i==j
if j = i+1:
    mat[i][j] = 1*(s[i]==s[j])

if j=i+2:
    s[i] == s[j] and mat[i+1][j-1] == 1

if j= i+3:
    s[i] == s[j] and mat[i+1][j-1] == 1

for gap in range(0,len(s)):
    for i in range(0,len(s)-gap)):
        mat[i][i+gap] = 1*(s[i] == s[j] and mat[i+1][j-1] == 1)
"""


def longestPalindrome(s: str) -> str:
    mat = [[0 for i in range(len(s))] for i in range(len(s))]
    mx_ = -1
    s_ = ''

    for i in range(len(s)):
        mat[i][i] = 1
        if mx_ < 1:
            mx_ = 1
            s_ = s[i]

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            mat[i][i + 1] = 1
            if mx_ < 2:
                mx_ = 2
                s_ = s[i] + s[i + 1]

    for j in range(len(s)):
        for i in range(j - 1):
            if mat[i + 1][j - 1] == 1 and s[i] == s[j]:
                mat[i][j] = 1
                if j - i >= mx_:
                    mx_ = j - i
                    s_ = s[i:j + 1]

    # print(mat)
    return s_


if __name__ == '__main__':
    print(longestPalindrome('babad') in ['bab', 'aba'])
    print(longestPalindrome('cbbd') in ['bb'])
    print(longestPalindrome('cccc') in ['cccc'])
    print(longestPalindrome('ccc') in ['ccc'])
