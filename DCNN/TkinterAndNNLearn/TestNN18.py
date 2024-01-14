import numpy as np
import matplotlib.pyplot as plt
import gzip
from typing import List
from sklearn.preprocessing import OneHotEncoder
import tensorflow.keras as keras
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import itertools
"""
%matplotlib inline

№ Чтение меток из файла
%%bash

rm -Rf train-images-idx3-ubyte.gz
rm -Rf train-labels-idx1-ubyte.gz
wget -q http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
wget -q http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz


with gzip.open('train-labels-idx1-ubyte.gz') as train_labels:
    data_from_train_file = train_labels.read()

# Пропускаем первые 8 байт
label_data = data_from_train_file[8:]
assert len(label_data) == 60000

# Конвертируем каждый байт в целое число. 
# Это будет число от 0 до 9
labels = [int(label_byte) for label_byte in label_data]
assert min(labels) == 0 and max(labels) == 9
assert len(labels) == 60000

№ Чтение изображений
SIZE_OF_ONE_IMAGE = 28 ** 2
images = []

# Перебор тренировочного файла и читение одного изображения за раз
with gzip.open('train-images-idx3-ubyte.gz') as train_images:
    train_images.read(4 * 4)
    ctr = 0
    for _ in range(60000):
        image = train_images.read(size=SIZE_OF_ONE_IMAGE)
        assert len(image) == SIZE_OF_ONE_IMAGE
        
        # Конвертировать в NumPy
        image_np = np.frombuffer(image, dtype='uint8') / 255
        images.append(image_np)

images = np.array(images)
images.shape

# Создание изображений
def plot_image(pixels: np.array):
    plt.imshow(pixels.reshape((28, 28)), cmap='gray')
    plt.show()

plot_image(images[25])

# Превращение целевых меток в вектор
labels_np = np.array(labels).reshape((-1, 1))

encoder = OneHotEncoder(categories='auto')
labels_np_onehot = encoder.fit_transform(labels_np).toarray()

print(labels_np_onehot)

# Разбиение изображений на обучающую и тестовую выборку
X_train, X_test, y_train, y_test = train_test_split(images, 
                                                    labels_np_onehot)
print(y_train.shape)
print(y_test.shape)

# Обучение нейронной сети
model = keras.Sequential()
model.add(keras.layers.Dense(input_shape=(SIZE_OF_ONE_IMAGE,), 
                             units=128, activation='relu'))
model.add(keras.layers.Dense(10, activation='softmax'))
model.summary()
model.compile(optimizer='sgd',                
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Результаты обучения
print(model.fit(X_train, y_train, epochs=20, batch_size=128))

# Проверка точности
print(model.evaluate(X_test, y_test))

predicted_results = model.predict(X_test[1010].reshape((1, -1)))
 Вывод слоя softmax — это распределение вероятностей для каждого вывода. 
В этом случае их может быть 10 (цифры от 0 до 9). Но ожидается, 
что каждое изображение будет соответствовать лишь одному.

 Поскольку это распределение вероятностей, 
их сумма приблизительно равна 1 (единице).
print(predicted_results.sum(), predicted_results, sep= '/n')

# Просмотр матрицы ошибок
predicted_outputs = np.argmax(model.predict(X_test), axis=1)
expected_outputs = np.argmax(y_test, axis=1)

predicted_confusion_matrix = confusion_matrix(expected_outputs, 
                                              predicted_outputs)
print(predicted_confusion_matrix)

# Визуализация данных
def plot_confusion_matrix(cm, classes,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.


    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), 
                                        range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()


# Compute confusion matrix
class_names = [str(idx) for idx in range(10)]
cnf_matrix = confusion_matrix(expected_outputs, predicted_outputs)
np.set_printoptions(precision=2)

# Plot non-normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names,
                      title='Confusion matrix, without normalization')

plt.show()
"""
