#weight, profit, capacity problem
#recursive method
def max_profit(weights, profits, capacity, idx=0):
    if idx==len(weights):
        return 0
    elif weights[idx]>capacity:
        return max_profit(weights,profits,capacity,idx+1)
    else:
        case1=max_profit(weights, profits, capacity, idx+1)
        case2=profits[idx] + max_profit(weights, profits, 
            capacity-weights[idx], idx+1)
        return max(case1,case2)

#memorization method --- 
# def maxprofit_memo(weights, profits, capacity):
#     memo={}
#     def recurse(idx, remain):
#         key=(idx, remain)
#         if key in memo:
#             return memo[key]
#         elif idx==len(weights):
#             memo[key]=0
#         elif weights[idx]>remain:
#             memo[key]=recurse(idx+1, remain)
#         else:
#             memo[key]=max(recurse(idx+1, remain),
#                 (profits[idx]+recurse(idx+1, remain-weights[idx])))
#         return memo[key]
#     return recurse(0,capacity)

#dynamic programming method-------------------------
def maxprofit_dp(capacity, weights, profits):
    n = len(weights)
    results = [[0 for x in range(capacity+1)] for x in range(n+1)]
    
    for idx in range(n):
        for c in range(1,capacity+1):
            if weights[idx] > c:
                results[idx+1][c] = results[idx][c]
            else:
                results[idx+1][c] = max(results[idx][c], profits[idx] + results[idx][c-weights[idx]])
            
    return results[-1][-1]
capacity= 15
weights=[4,5,6]
profits= [1,2,3]

maxprofit_dp(weights, profits, capacity)