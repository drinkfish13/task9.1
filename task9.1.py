# Создайте numpy array с элементами от числа N до 0 (например, для N = 10 это будет array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])).
import numpy as np
n = int(input())
# version 1 так сказать индийская
lst = []
for i in range(n):
    lst.append(i)
lst.reverse()
lst = np.array(lst)
print(lst, type(lst))

# version 2 так сказать гугловская
x = np.flip(np.arange(n))
print(x, type(x))