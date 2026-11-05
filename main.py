def newton_backward(x_n: list, y_n: list, x_target: list) -> list:
    n = len(x_n)

    #переворачиваем узлы
    xr = x_n[::-1]
    yr = y_n[::-1]

    #вычисление таблицы разделенных разностей
    coef = [[0.0] * n for _ in range(n)]
    for i in range(n):
        coef[i][0] = yr[i]

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (xr[i + j] - xr[i])

    #сборка значения по формуле интерполирования назад
    val = []
    for x_i in x_target:
        result = coef[0][0]  # f(xn)
        product_term = 1.0
        for k in range(1, n):
            product_term *= x_i - xr[k - 1]
            result += product_term * coef[0][k]

        val.append(round(result,5))
    return val

with open('input.txt', 'r', encoding='utf-8') as file:
    xn = [float(i.replace(',', '.')) for i in file.readline().split()]
    yn = [float(i.replace(',', '.')) for i in file.readline().split()]
    x = [float(i.replace(',', '.')) for i in file.readline().split()]

res = newton_backward(xn, yn, x)
with open('output.txt', 'w', encoding='utf-8') as file:
    for xi, yi in zip(x, res):
        file.write(f"Результат интерполяции для х = {xi}: {yi}\n")
