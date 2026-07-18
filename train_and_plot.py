import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

print("Loading data...")
data_dir = "notebooks/data"
img_size = (160, 160)
batch_size = 16

datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    rotation_range=15,
    zoom_range=0.15,
    horizontal_flip=True
)

train_generator = datagen.flow_from_directory(
    data_dir, target_size=img_size, batch_size=batch_size,
    class_mode="binary", subset="training", shuffle=True
)
val_generator = datagen.flow_from_directory(
    data_dir, target_size=img_size, batch_size=batch_size,
    class_mode="binary", subset="validation", shuffle=False
)

print("Class indices:", train_generator.class_indices)

print("Building model...")
base_model = MobileNetV2(input_shape=(160, 160, 3), include_top=False, weights="imagenet")
base_model.trainable = False

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(64, activation="relu")(x)
output = Dense(1, activation="sigmoid")(x)

model = Model(inputs=base_model.input, outputs=output)
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

print("Training...")
history = model.fit(train_generator, validation_data=val_generator, epochs=10)

print("Saving graph...")
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(history.history["accuracy"], label="Train Accuracy")
plt.plot(history.history["val_accuracy"], label="Val Accuracy")
plt.title("Model Accuracy")
plt.xlabel("Epoch")
plt.legend()

plt.subplot(1,2,2)
plt.plot(history.history["loss"], label="Train Loss")
plt.plot(history.history["val_loss"], label="Val Loss")
plt.title("Model Loss")
plt.xlabel("Epoch")
plt.legend()

plt.tight_layout()
plt.savefig("training_curves.png")
print("Graph saved as training_curves.png")
