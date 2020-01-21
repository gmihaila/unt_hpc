import sys
import os
os.environ["CUDA_VISIBLE_DEVICES"]="0,1,2,3"
import tensorflow as tf
import timeit

if __name__ == "__main__":
  if tf.test.is_gpu_available():
    print("\nGPU detected yeeey!\n")
    print("tf version running ", tf.version.VERSION)
    print("\nNum GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
    mirrored_strategy = tf.distribute.MirroredStrategy()
    with mirrored_strategy.scope():
      model = tf.keras.Sequential([tf.keras.layers.Dense(1, input_shape=(1,))])
      model.compile(loss='mse', optimizer='sgd')


    dataset = tf.data.Dataset.from_tensors(([1.], [1.])).repeat(50000).batch(50)
    model.fit(dataset, epochs=10)
    model.evaluate(dataset)

  else:
    print("No GPU detected!")



