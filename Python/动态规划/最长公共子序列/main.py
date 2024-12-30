import torch


def print_LCS(rec,X,i,j):
    if i == 0 or j == 0:
        return
    if rec[i][j] == "LU":
        print_LCS(rec, X, i-1, j-1)
        print(X[i-1], end="")
    elif rec[i][j] == " L":
        print_LCS(rec, X, i-1, j)
    else:
        print_LCS(rec, X, i, j-1)

if __name__ == '__main__':
    X = "ABCBDAB"
    Y = "BDCABA"

    n = len(X)
    m = len(Y)
    print(f"X: {n}")
    print(f"Y: {m}")
    
    C = torch.zeros((n+1, m+1), dtype=torch.int32)
    rec = [["" for _ in range(m+1)] for _ in range(n+1)]

    print(f"C 初始化 {C.shape}")
    print(f"rec 初始化 {len(rec)} x {len(rec[0])}")
    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                C[i][j] = C[i-1][j-1] + 1
                rec[i][j] = "LU"
            elif C[i-1][j] >= C[i][j-1]:
                C[i][j] = C[i-1][j]
                rec[i][j] = " L"
            else:
                C[i][j] = C[i][j-1]
                rec[i][j] = " U"
    print(C)
    for row in rec:
        print(row)
    print(f"长度 {C[n][m]}")
    print_LCS(rec, X, n, m)