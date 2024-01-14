from matplotlib import pyplot as plt
import numpy as np


x = list(range(-10, 11))
y = np.exp(x) / np.sum(np.exp(x))

plt.plot(x, y)
plt.title('Многопеременная функция')
plt.xlabel('Ввод')
plt.ylabel('вывод')
plt.savefig('softmax.png')
plt.show()
