import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

x_data = [[0,0], [0,1], [1,0], [1,1]]
y_data = [[0], [1], [1], [0]]

I = tf.placeholder(tf.float32, shape=[None, 2])
V = tf.placeholder(tf.float32, shape=[None, 1])
