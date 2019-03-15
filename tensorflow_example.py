import tensorflow as tf

a = tf.constant([1.0,2.0],name='a',dtype=tf.float16)
b = tf.constant([4,5],name='b',dtype=tf.float16)

result = tf.add(a,b)

print(result)

print(tf.Session().run(result))