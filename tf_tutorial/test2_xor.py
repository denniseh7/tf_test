# -- imports --
import tensorflow as tf

# -- constant data --
x = [[0,0],[1,1],[1,0],[0,1]]# TODO
y_ = [[0],[0],[1],[1]]# TODO

# -- induction --
# 1x2 input -> 2x3 hidden sigmoid -> 3x1 sigmoid output

# Layer 0 = 1x2 input# TODO
x0 = tf.constant(x, dtype=tf.float32)# TODO
y0 = tf.constant(y_, dtype=tf.float32)# TODO

# Layer 1 = 2x3 hidden sigmoid # TODO
#m1 = tf.Variable(tf.random_uniform([2, 3], minval=0.1, maxval=0.9, dtype=tf.float32))
#b1 = tf.Variable(tf.random_uniform([3], minval=0.1, maxval=0.9, dtype=tf.float32))
m1 = tf.get_variable("m1", tf.random_uniform([2,3], minval=0.1, maxval=0.9, dtype=tf.float32))# TODO
b1 = # TODO
h1 = # TODO

# Layer 2 = 3x1 output # TODO
m2 = # TODO
b2 = # TODO
y_out = # TODO


# -- loss --

# loss : sum of the squares of y0 - y_out
loss = # TODO

# training step : gradient decent (1.0) to minimize loss
train = # TODO


# -- training --
# run 500 times using all the X and Y
# print out the loss and any other interesting info
with tf.Session() as sess:
    # TODO session execution command here
    print "\nloss"
    for step in range(500):
        # TODO session execution command here
        if (step + 1) % 100 = # TODO
            print # TODO session execution command here

    results = # TODO
    labels = # TODO
    for label, result in zip(*(labels, results)):
        print ""
        print label
        print result

print ""