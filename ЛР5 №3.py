import numpy as np
import matplotlib.pyplot as plt

# Функция f(x)
def f(x, c):
    return (np.abs(2*x-c)**3)**(1/5) + 0.567

# Заданный интервал для x
x = np.linspace(-10, 10, 100)

# Значения функции для x=12.1 и различных c
c_values = np.arange(-10, 1, 0.35)
f_values = f(12.1, c_values)

# Вывод значений аргумента и значения функции
for i in range(len(c_values)):
    print(f"c={c_values[i]}, f(x)= {f_values[i]}")

# Наибольшее, наименьшее, среднее значение и количество элементов массива
max_f = np.max(f_values)
min_f = np.min(f_values)
mean_f = np.mean(f_values)
num_elements = len(f_values)

print(f"Наибольшее значение: {max_f}")
print(f"Наименьшее значение: {min_f}")
print(f"Среднее значение: {mean_f}")
print(f"Количество элементов: {num_elements}")

# Сортировка массива по убыванию
sorted_indices = np.argsort(f_values)[::-1]
sorted_c_values = c_values[sorted_indices]
sorted_f_values = f_values[sorted_indices]

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(c_values, f_values, marker='o', label='f(x)')
plt.axhline(mean_f, color='r', linestyle='--', label='Среднее значение f(x)')
plt.xlabel('c')
plt.ylabel('f(x)')
plt.title('График функции f(x)')
plt.legend()
plt.grid(True)
plt.show()