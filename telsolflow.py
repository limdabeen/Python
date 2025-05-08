import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

x_data = [[0,0], [0,1], [1,0], [1,1]]
y_data = [[0], [1], [1], [0]]

I = tf.placeholder(tf.float32, shape=[None, 2])
V = tf.placeholder(tf.float32, shape=[None, 1])

W1 = tf.Variable(tf.random_normal([2, 2]))
b1 = tf.Variable(tf.random_normal([2]))
h = tf.sigmoid(tf.matmul(I, W1) + b1)

W2 = tf.Variable(tf.random_normal([2, 1]))
b2 = tf.Variable(tf.random_normal([1]))
O = tf.sigmoid(tf.matmul(h, W2) + b2)

cost = -tf.reduce_mean(V * tf.log(O) + (1 - V) * tf.log(1 - O))
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(cost)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for i in range(50001):
sess.run(train, feed_dict={I: x_data, V: y_data})
if i % 500 == 0:
print(i, sess.run(cost, feed_dict={I: x_data, V: y_data}))

h_infer = sess.run(O, feed_dict={I: x_data})
print(h_infer)