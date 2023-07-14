def count_even_numbers(A, B):
    counts = []
    for i in range(len(B)):
        start = B[i][0]
        end = B[i][1]
        count = 0
        for j in range(start, end+1):
            if A[j] % 2 == 0:
                count += 1
        counts.append(count)
    return counts
