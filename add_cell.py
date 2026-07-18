import nbformat

nb = nbformat.read("notebooks/train_model.ipynb", as_version=4)

code = """import matplotlib.pyplot as plt

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
print("Graph saved")
"""

nb.cells.append(nbformat.v4.new_code_cell(code))
nbformat.write(nb, "notebooks/train_model.ipynb")
print("Cell added successfully")
