#tesnorflow graph
n_samples = readCSV.nrows - 1

X1 = tf.placeholder(tf.float32, name='X1')
X2 = tf.placeholder(tf.float32, name='X2')
X3 = tf.placeholder(tf.float32, name='X3')
Y = tf.placeholder(tf.float32, name='Y')

W1 = tf.Variable(0.0, name='w1')
W2 = tf.Variable(0.0, name='w2')
W3 = tf.Variable(0.0, name='w3')

Xmean = (X1 + X2 + X3) / 3

Y_predicted = (((X1 - Xmean) ** 2) * W1) + (((X2 - Xmean) ** 2) * W2) + (((X3 - Xmean) ** 2) * W3)

loss = tf.square(Y - Y_predicted, name='loss')

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.0001).minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    writer = tf.summary.FileWriter('./graphs/hackaton', sess.graph)

    for i in range(50):
        total_loss = 0
        for x1, x2, x3, y in readCSV:
            opt, l = sess.run([optimizer, loss], feed_dict={X1: x1, X2: x2, X3: x3, Y: y})
            total_loss += l
        print('Epoch {0}: {1}'.format(i, total_loss / n_samples))

    writer.close()
  
######################################################################################################################
    #web_page
from wsgiref.simple_server import make_server

def hello_world(environ, start_response):
    status = '200 ok'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)

    return csv_reader_class.py

httpd = make_server('', 8005)

print ("Serving on porting 8005....")

httpd.serve_forever()
