import glob
from collections import defaultdict
from PIL import Image

import numpy as np
import tensorflow.python.keras as keras
from tensorflow.python.keras import layers
from tensorflow.python.keras.optimizer_v1 import Adam


shape_counts = defaultdict(int)

IMG_SIZE = (94, 125)


def pixels_from_path(file_path):
    im = Image.open(file_path)
    im = im.resize(IMG_SIZE)
    np_im = np.array(im)
    # matrix of pixel RGB values
    return np_im


for i, cat in enumerate(glob.glob('cats/*')[:1000]):
    if i % 100 == 0:
        print(i)
    img_shape = pixels_from_path(cat).shape
    # loads image as np matrix and checks shape.
    shape_counts[str(img_shape)] = shape_counts[str(img_shape)] + 1

shape_items = list(shape_counts.items())
shape_items.sort(key=lambda x: x[1])
shape_items.reverse()

SAMPLE_SIZE = 2048
print("loading training cat images...")
cat_train_set = np.asarray([pixels_from_path(cat)
                            for cat in glob.glob('cats/*')
                            [:SAMPLE_SIZE]])
print("loading training dog images...")
dog_train_set = np.asarray([pixels_from_path(dog)
                            for dog in glob.glob('dogs/*')
                            [:SAMPLE_SIZE]])

valid_size = 512
print("loading validation cat images...")
cat_valid_set = np.asarray([pixels_from_path(cat)
                            for cat in glob.glob('cats/*')
                            [-valid_size:]])
print("loading validation dog images...")
dog_valid_set = np.asarray([pixels_from_path(dog)
                            for dog in glob.glob('dogs/*')
                            [-valid_size:]])

# generate X and Y (inputs and labels).
x_train = np.concatenate([cat_train_set, dog_train_set])
labels_train = np.asarray([1 for _ in range(SAMPLE_SIZE)] +
                          [0 for _ in range(SAMPLE_SIZE)])

x_valid = np.concatenate([cat_valid_set, dog_valid_set])
labels_valid = np.asarray([1 for _ in range(valid_size)] +
                          [0 for _ in range(valid_size)])

total_pixels = IMG_SIZE[0] * IMG_SIZE[1] * 3
fc_size = 512

inputs = keras.Input(shape=(IMG_SIZE[1], IMG_SIZE[0], 3),
                     name='ani_image')
x = layers.Flatten(name='flattened_img')(inputs)
# turn image to vector.

x = layers.Dense(fc_size, activation='relu', name='first_layer')(x)
outputs = layers.Dense(1, activation='sigmoid', name='class')(x)

model = keras.Model(inputs=inputs, outputs=outputs)

customAdam = Adam(lr=0.001, decay=0.1)
model.compile(optimizer=customAdam,  # Optimizer
              # Loss function to minimize
              loss="mean_squared_error",
              # List of metrics to monitor
              metrics=["binary_crossentropy", "mean_squared_error"])

print('# Fit model on training data')

history = model.fit(x_train,
                    labels_train,
                    batch_size=32,
                    shuffle=True,
                    # important since we loaded cats first, dogs second.
                    epochs=3,
                    validation_data=(x_valid, labels_valid))

# Train on 4096 samples, validate on 2048 samples
# loss: 0.5000 - binary_crossentropy: 8.0590 -
# mean_squared_error: 0.5000 - val_loss: 0.5000 -
# val_binary_crossentropy: 8.0591 - val_mean_squared_error: 0.5000

fc_layer_size = 128
img_size = IMG_SIZE

conv_inputs = keras.Input(shape=(img_size[1], img_size[0], 3),
                          name='ani_image')
conv_layer = layers.Conv2D(24, kernel_size=3,
                           activation='relu')(conv_inputs)
conv_layer = layers.MaxPool2D(pool_size=(2, 2))(conv_layer)
conv_x = layers.Flatten(name='flattened_features')(conv_layer)
# turn image to vector.

conv_x = layers.Dense(fc_layer_size, activation='relu',
                      name='first_layer')(conv_x)
conv_x = layers.Dense(fc_layer_size, activation='relu',
                      name='second_layer')(conv_x)
conv_outputs = layers.Dense(1, activation='sigmoid',
                            name='class')(conv_x)

conv_model = keras.Model(inputs=conv_inputs, outputs=conv_outputs)

customAdam = Adam(lr=1e-6)
conv_model.compile(optimizer=customAdam,  # Optimizer
                   # Loss function to minimize
                   loss="binary_crossentropy",
                   # List of metrics to monitor
                   metrics=["binary_crossentropy",
                            "mean_squared_error"])

# Epoch 5/5 loss: 1.6900 val_loss: 2.0413 val_mean_squared_error: 0.3688

preds = conv_model.predict(x_valid)
preds = np.asarray([pred[0] for pred in preds])
print(np.corrcoef(preds, labels_valid)[0][1])  # 0.15292172

fc_layer_size = 256
img_size = IMG_SIZE

conv_inputs = keras.Input(shape=(img_size[1], img_size[0], 3),
                          name='ani_image')
# first convolutional layer.
conv_layer = layers.Conv2D(48, kernel_size=3,
                           activation='relu')(conv_inputs)
conv_layer = layers.MaxPool2D(pool_size=(2, 2))(conv_layer)

# second convolutional layer.
conv_layer = layers.Conv2D(48, kernel_size=3,
                           activation='relu')(conv_layer)
conv_layer = layers.MaxPool2D(pool_size=(2, 2))(conv_layer)

conv_x = layers.Flatten(name='flattened_features')(conv_layer)
# turn image to vector.

conv_x = layers.Dense(fc_layer_size, activation='relu',
                      name='first_layer')(conv_x)
conv_x = layers.Dense(fc_layer_size, activation='relu',
                      name='second_layer')(conv_x)
conv_outputs = layers.Dense(1, activation='sigmoid',
                            name='class')(conv_x)

conv_model = keras.Model(inputs=conv_inputs, outputs=conv_outputs)

#  Epoch 15/15
# 4096/4096 [==============================] - 154s 38ms/sample -
# loss: 0.8806 - binary_crossentropy: 0.8806 -
# mean_squared_error: 0.2402
# val_loss: 1.5379 - val_binary_crossentropy: 1.5379 -
# val_mean_squared_error: 0.3302
# Labels vs predictions correlation coefficient 0.2188213

# Измерение точности
cat_quantity = sum(labels_valid)

for i in range(1, 10):
    print('threshold :' + str(.1 * i))
    print(sum(labels_valid[preds > .1 * i])
          / labels_valid[preds > .1 * i].shape[0])

# Увеличение свёрточных слоёв
fc_layer_size = 256
img_size = IMG_SIZE

conv_inputs = keras.Input(shape=(img_size[1], img_size[0], 3),
                          name='ani_image')
conv_layer = layers.Conv2D(128, kernel_size=3,
                           activation='relu')(conv_inputs)
conv_layer = layers.MaxPool2D(pool_size=(2, 2))(conv_layer)

conv_layer = layers.Conv2D(128, kernel_size=3,
                           activation='relu')(conv_layer)
conv_layer = layers.MaxPool2D(pool_size=(2, 2))(conv_layer)

conv_x = layers.Flatten(name='flattened_features')(conv_layer)
# turn image to vector.

conv_x = layers.Dense(fc_layer_size, activation='relu',
                      name='first_layer')(conv_x)
conv_x = layers.Dense(fc_layer_size, activation='relu',
                      name='second_layer')(conv_x)
conv_outputs = layers.Dense(1, activation='sigmoid',
                            name='class')(conv_x)

huge_conv_model = keras.Model(inputs=conv_inputs, outputs=conv_outputs)

# epoch 13
# 445s  loss: 0.3749 - binary_crossentropy: 0.3749 -
# mean_squared_error: 0.1190
# val_loss: 0.8217 - val_binary_crossentropy: 0.8217 -
# val_mean_squared_error: 0.2470
# Pearson coerrcoef : 0.30370386
