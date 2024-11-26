

def can_fit(n, a, b, w, h, d):
    # Размеры модуля с защитой
    mw1, mw2 = a + 2 * d, b + 2 * d
    mh1, mh2 = b + 2 * d, a + 2 * d

    # Количество модулей по ширине и высоте
    cw1, cw2 = w // mw1, w // mw2
    ch1, ch2 = h // mh1, h // mh2

    # Общее количество модулей
    return max(cw1 * ch1, cw2 * ch2) >= n


def max_layer(n, a, b, w, h):
    l, r = 0, min(w // 2, h // 2)  # Максимально возможное значение d

    while l < r:
        m = (l + r + 1) // 2  # Проверяем верхнюю половину
        if can_fit(n, a, b, w, h, m):
            l = m  # Если подходит, ищем большее значение
        else:
            r = m - 1  # Иначе ищем меньшее значение

    return l



N, A, B, W, H = map(int, input().split())
res = max_layer(N, A, B, W, H)
print(res)