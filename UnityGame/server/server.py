#
#   Image classification server in Python
#   Binds REP socket to tcp://*:5555
#   Expects image bits from client, replies with b"Scissors", b"Rock", b"Paper" according to model classification
#

import time
import zmq
import cv2
import tensorflow as tf
from tensorflow import keras
import numpy as np
from keras.preprocessing import image
import os
#import matplotlib.pyplot as plt
from PIL import Image
import io

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
#i = 0;
print("server up")
model = keras.models.load_model('step_decay_model/')
while True:
	pred = b"None" 
	print("\nWaiting for image...")
	#  Wait for next request from client
	message = socket.recv()
	time.sleep(0.1) #Small delay to wait for the texture to be made
	f = open('image.txt', 'wb')
	f.write(message)
	f.close()
	
	newsize = (150, 150)
	img = Image.open(io.BytesIO(message)).resize(newsize)
	
    # Image Preprocessing
	img = img.convert("RGB")
	x = np.array(img).astype(np.float32) 	
	x/=255.0
	mean, std = x.mean(), x.std()
	x=(x-mean) / std
	x = np.expand_dims(x, axis=0)
	images = np.vstack([x])

	classes = model.predict(images, batch_size=10)
	print(classes[0])
	i= classes[0]
	if round(i[0]) == 1: #paper
        print("Model prediction: Paper")
		pred = b"Paper"	
	elif round(i[1]) == 1: #rock
        print("Model prediction: Rock")
		pred = b"Rock"
	else: #scissors
        print("Model prediction: Scissors")
		pred = b"Scissors" 

	time.sleep(1)

	#  Send reply back to client
	#  In the real world usage, after you finish your work, send your output here
    print(f'sending \"{pred}\" to client')
	socket.send(pred)
	print("DONE")