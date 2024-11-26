def int_sqrt(A):
    low, high = 0, A

    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid

        if mid_squared == A:
            return mid  # Если нашли точный корень
        elif mid_squared < A:
            low = mid + 1  # Ищем в правой половине
        else:
            high = mid - 1  # Ищем в левой половине

    return high

a = int(input())
print(int_sqrt(a))
