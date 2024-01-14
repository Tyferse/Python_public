from datetime import datetime
import itertools
import io

import tensorflow as tf
from keras.datasets import mnist
from keras import utils
from keras import layers
from keras import models
from keras import callbacks
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt


def plot_confusion_matrix(cm, class_names):
    figure = plt.figure(figsize=(8, 8))
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Accent)
    plt.title("Матрица неточностей")
    plt.colorbar()
    tick_marks = np.arange(len(class_names))
    plt.xticks(tick_marks, class_names, rotation=45)
    plt.yticks(tick_marks, class_names)

    cm = np.around(cm.astype('float') / cm.sum(axis=1)[:, np.newaxis],
                   decimals=2)
    threshold = cm.max() / 2.

    for i, j in itertools.product(range(cm.shape[0]),
                                  range(cm.shape[1])):
        color = "white" if cm[i, j] > threshold else "black"
        plt.text(j, i, cm[i, j], horizontalalignment="center",
                 color=color)

    plt.tight_layout()
    plt.ylabel('Правильный ответ')
    plt.xlabel('Предсказанный ответ')

    return figure


def plot_to_image(figure):
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(figure)
    buf.seek(0)

    digit = tf.image.decode_png(buf.getvalue(), channels=4)
    digit = tf.expand_dims(digit, 0)

    return digit


def log_confusion_matrix(epoch, logs):
    predictions = model.predict(x_test)
    predictions = np.argmax(predictions, axis=1)

    y_test_arg = np.argmax(y_test, axis=1)
    cm = metrics.confusion_matrix(y_test_arg, predictions)
    figure = plot_confusion_matrix(cm, class_names=class_names)
    cm_image = plot_to_image(figure)

    with file_writer_cm.as_default():
        tf.summary.image("Confusion Matrix", cm_image, step=epoch)


class_names = ['Ноль', 'Один', 'Два', 'Три', 'Четыре',
               'Пять', 'Шесть', 'Семь', 'Восемь', 'Девять']

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape((60000, 28, 28, 1))
x_train = x_train.astype('float32') / 255

x_test = x_test.reshape((10000, 28, 28, 1))
x_test = x_test.astype('float32') / 255

y_train = utils.to_categorical(y_train)
y_test = utils.to_categorical(y_test)
print(y_test, y_train)

model = models.Sequential([
    layers.Conv2D(50, (3, 3), activation='relu',
                  input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(100, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(100, 'relu'),
    layers.Dense(10, 'softmax')
])

model.summary()

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

log_dir = "logs/fit/" + datetime.now().strftime("%Y-%m-%d-%H%M%S")
tensorboard_callback1 = callbacks.TensorBoard(log_dir=log_dir,
                                              histogram_freq=1,
                                              write_graph=True,
                                              write_images=True)

logdir = "logs/image/"
tensorboard_callback2 = tf.keras.callbacks.TensorBoard(log_dir=logdir,
                                                       histogram_freq=1)
file_writer_cm = tf.summary.create_file_writer(logdir + '/cm')

cm_callback = tf.keras.callbacks.LambdaCallback(
    on_epoch_end=log_confusion_matrix)

model.fit(x_train, y_train, epochs=5, batch_size=60,
          validation_data=(x_test, y_test),
          callbacks=[tensorboard_callback1, tensorboard_callback2,
                     cm_callback])

test_loss, test_acc = model.evaluate(x_test, y_test)
print('Loss:', test_loss, '\nAccuracy:', test_acc)

model.save('trained_model.h5')
