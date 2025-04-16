import tensorflow as tf

one = tf.constant(1)
two = tf.constant(2)
sum = tf.add(one, two)
print(sum.numpy())