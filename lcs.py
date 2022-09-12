#given two strings, find the length of longest common sequence among them
#logic driven function
# def lcd_sequence(seq1, seq2, idx1=0, idx2=0):
#     if idx1==len(seq1) or idx2==len(seq2):
#         return 0
#     elif seq1[idx1]==seq2[idx2]:
#         return 1+lcd_sequence(seq1,seq2,idx1+1,idx2+1)
#     else:
#         case1=lcd_sequence(seq1,seq2,idx1+1,idx2)
#         case2=lcd_sequence(seq1,seq2,idx1,idx2+1)
#         return max(case1,case2)

#memorization to solve execution of same pattern of recurssion method

# def lcs_memo(seq1, seq2):
#     memo={}
#     def recurse(idx1=0, idx2=0):
#         key=(idx1,idx2)
#         if key in memo:
#             return memo[key]
#         elif idx1==len(seq1) or idx2==len(seq2):
#             memo[key]=0
#         elif seq1[idx1]==seq2[idx2]:
#             memo[key]=1+ recurse(idx1+1,idx2+1
#         else:
#             memo[key]=max(recurse(idx1+1,idx2),recurse(idx1,idx2+1))
#         return memo[key]
#     return recurse(0,0)

# dynamic programming method to solve space complexity of recursive method

def lcs_dp(seq1, seq2):
    l1, l2=len(seq1), len(seq2)
    table=[[0 for x in range (l2+1)] for x in range(l1+1)]
    for i in range(l1):
        for j in range(l2):
            if seq1[i]==seq2[j]:
                table[i+1][j+1]=table[i][j]
            else:
                table[i+1][j+1]=max(table[i][j+1], table[i+1][j])
    return table[-1][-1]
print(lcs_dp('','condense'))