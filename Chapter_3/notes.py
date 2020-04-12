7 Functions for Big O: From fastest to slowest

Constant Time:      O(1)
Log Time:           O(log(N))
Linear Time:        O(N)
NLogN Time:         O(NLog(N))
Quadratic Time:     O(N^2)




# O(N^2)
def prefix average1(S):
    ”””Return list such that, for all j, A[j] equals average of S[0], ..., S[j].”””
    n = len(S)
    A = [0] n # create new list of n zeros
    for j in range(n):
        total = 0 # begin computing S[0] + ... + S[j]
        for i in range(j + 1):
            total += S[i]
        A[j] = total / (j+1) # record the average
    return A


# O(N^2)
def prefix average2(S):
    ”””Return list such that, for all j, A[j] equals average of S[0], ..., S[j].”””
    n = len(S)
    A = [0] n # create new list of n zeros
    for j in range(n):
        A[j] = sum(S[0:j+1]) / (j+1) # record the average
    return A

# O(N)
def prefix average3(S):
    ”””Return list such that, for all j, A[j] equals average of S[0], ..., S[j].”””
    n = len(S)
    A = [0] n # create new list of n zeros
    total = 0 # compute prefix sum as S[0] + S[1] + ...
    for j in range(n):
        total += S[j] # update prefix sum to include S[j]
        A[j] = total / (j+1) # compute average based on current sum
    return A