import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

print("Loading model...")
model = tf.keras.models.load_model("notebooks/fire_smoke_model.h5")

print("Loading validation data...")
data_dir = "notebooks/data"
img_size = (160, 160)
batch_size = 16

datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
val_generator = datagen.flow_from_directory(
    data_dir, target_size=img_size, batch_size=batch_size,
    class_mode="binary", subset="validation", shuffle=False
)

print("Running predictions...")
val_generator.reset()
preds = model.predict(val_generator, verbose=1)
pred_labels = (preds > 0.5).astype(int).flatten()
true_labels = val_generator.classes
class_names = list(val_generator.class_indices.keys())

print("Building confusion matrix...")
cm = confusion_matrix(true_labels, pred_labels)

plt.figure(figsize=(5,4))
plt.imshow(cm, cmap="Blues")
plt.title("Confusion Matrix")
plt.colorbar()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names, rotation=20)
plt.yticks(tick_marks, class_names)
plt.xlabel("Predicted")
plt.ylabel("Actual")
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(j, i, str(cm[i, j]), ha="center", va="center",
                  color="white" if cm[i, j] > cm.max()/2 else "black", fontsize=14)
plt.tight_layout()
plt.savefig("confusion_matrix.png")
print("Saved confusion_matrix.png")

print("Building sample predictions grid...")
val_generator.reset()
images, labels = next(val_generator)
batch_preds = model.predict(images)

plt.figure(figsize=(12,8))
for i in range(min(8, len(images))):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i])
    true_lbl = class_names[int(labels[i])]
    pred_lbl = class_names[int(batch_preds[i][0] > 0.5)]
    conf = float(batch_preds[i][0])
    color = "green" if true_lbl == pred_lbl else "red"
    plt.title(f"True: {true_lbl}\nPred: {pred_lbl} ({conf:.2f})", fontsize=9, color=color)
    plt.axis("off")
plt.tight_layout()
plt.savefig("sample_predictions.png")
print("Saved sample_predictions.png")

print("All done!")
