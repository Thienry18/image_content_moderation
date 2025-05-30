import tensorflow as tf

print("🧠 TensorFlow version:", tf.__version__)

# Cek perangkat GPU
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print("✅ GPU terdeteksi:")
    for gpu in gpus:
        print("  -", gpu)
else:
    print("❌ GPU tidak terdeteksi. Menggunakan CPU.")

# Tes operasi kecil di GPU (jika tersedia)
try:
    with tf.device('/GPU:0'):
        a = tf.constant([[1.0, 2.0]])
        b = tf.constant([[3.0], [4.0]])
        c = tf.matmul(a, b)
    print("🚀 Operasi berhasil dijalankan di GPU:", c.numpy())
except RuntimeError as e:
    print("⚠️ RuntimeError:", e)
except Exception as e:
    print("⚠️ Error lain:", e)
