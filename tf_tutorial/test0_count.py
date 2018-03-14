import tensorflow as tf

# set state to a variable set to 0
state = tf.get_variable("state",dtype=tf.int32, initializer=tf.constant(0))

# set one to a constant set to 1
one = tf.constant(1)

# update phase adds state and one and then assigns to stateaddition =

def addition():
    my_add=tf.add(state,one)
    return my_add

def update():
    my_update = tf.assign(state, addition())
    return my_update
# create a session
with tf.Session() as sess:
    # initialize session variables
    sess.run(tf.global_variables_initializer())

    print ("The starting state is", sess.run(state))# TODO session execution command here

    print ("Run the update 10 times...")
    for count in range(10):
        # execute the update
        sess.run(update())
        # TODO session execution command here

    print ("The end state is", sess.run(state))# TODO session execution command here