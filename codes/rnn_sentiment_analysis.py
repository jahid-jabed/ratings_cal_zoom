# -*- coding: utf-8 -*-
"""RNN_Sentiment_Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/125xdmzaKWEgVdfaFqJmh6p45GjFV_KNw

Importing Libraries
--
"""

import numpy as np
import pandas as pd

from google.colab import drive
drive.mount('/content/drive')

"""Data Preprocessing
--
"""

import pickle

pickle_in = open("/content/drive/MyDrive/SQA/Project Works/Datasets/Pickle Data/X_All_R.pickle", "rb")
X = pickle.load(pickle_in)

pickle_in = open("/content/drive/MyDrive/SQA/Project Works/Datasets/Pickle Data/Y_All_R.pickle", "rb")
Y = pickle.load(pickle_in)

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
tokens_model = Tokenizer(num_words = 64)

X = list(map(str, X))
tokens_model.fit_on_texts(X)

seq = tokens_model.texts_to_sequences(X)

word_index = tokens_model.word_index

max_length = 47

from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
X = pad_sequences(seq, maxlen=max_length)
Y = np.asarray(Y)

X.shape

Y.shape

Y = Y - 1

"""Training and Test Splitting
--
"""

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.9, random_state=1)
X_test, X_val, Y_test, Y_val = train_test_split(X_test, Y_test, test_size=0.05, random_state=1)

print('Train:', len(X_train), '\nTest:', len(X_test), '\nValidation:', len(X_val))

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models
from keras.callbacks import ModelCheckpoint

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

total_words = len(word_index)+1
embedding_dim = 4

model = models.Sequential()
model.add(layers.Embedding(total_words, embedding_dim, input_length=max_length, name='embedding_layer'))
model.add(layers.SimpleRNN(64, activation='relu', name='rnn1'))
model.add(layers.Dense(5, activation='softmax'))

model.summary()

from keras.callbacks import ModelCheckpoint

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
epochs = 15

filepath = '/content/drive/MyDrive/SQA/Project Works/Datasets/Pickle Data/RNN/model_rnn-{epoch:02d}-performance-{val_accuracy:.2f}-{val_loss:.2f}.hdf5'

checkpoint_acc = ModelCheckpoint(filepath=filepath, monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')
checkpoint_loss = ModelCheckpoint(filepath=filepath, monitor='val_loss', verbose=1, save_best_only=True, mode='min')

callbacks = [checkpoint_acc, checkpoint_loss]

history = model.fit(X_train, Y_train, validation_data=(X_val, Y_val), epochs=epochs, callbacks=callbacks)

"""Learning Visualization
--
"""

import matplotlib.pyplot as plt

train_acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

train_loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(18, 6))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, train_acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, train_loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

"""Performance Analysis
--
"""

model = tf.keras.models.load_model('/content/drive/MyDrive/SQA/Project Works/Datasets/Pickle Data/RNN/model_rnn-14-performance-0.47-1.32.hdf5')

records = model.evaluate(X_test, Y_test)

predictions = model.predict(X_test) # predict output for all test data

scores = tf.nn.softmax(predictions)
Y_pred = []
for score in scores:
  Y_pred.append(np.argmax(score))
Y_pred = np.array(Y_pred) # predicted labels

# Defining function for confusion matrix plot
def plot_confusion_matrix(Y_test, Y_pred, Classes, normalize=False, title=None, cmap=plt.cm.Blues):

    # Compute the confusion matrix
    conf_mat = confusion_matrix(Y_test, Y_pred)
    if normalize:
        conf_mat = conf_mat.astype('float32') / conf_mat.sum(axis=1)[:, np.newaxis]
        print(title)
    else:
        print(title)

    fig, ax = plt.subplots(figsize=(6,6))
    im = ax.imshow(conf_mat, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)

    # We want to show all ticks...
    ax.set(xticks=np.arange(conf_mat.shape[1]), yticks=np.arange(conf_mat.shape[0]),
           xticklabels=Classes, yticklabels=Classes,
           title=title, ylabel='True label', xlabel='Predicted label')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
   
    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = conf_mat.max() / 2.
    for i in range(conf_mat.shape[0]):
        for j in range(conf_mat.shape[1]):
            ax.text(j, i, format(conf_mat[i, j], fmt),
                    ha="center", va="center",
                    color="white" if conf_mat[i, j] > thresh else "black")
    fig.tight_layout()

    return ax

np.set_printoptions(precision=2)

from sklearn.metrics import confusion_matrix

#Plotting the confusion matrix
confusion_mtx = confusion_matrix(Y_test, Y_pred)

# Plotting non-normalized confusion matrix
plot_confusion_matrix(Y_test, Y_pred, Classes = ['*    ', '**   ', '***  ', '**** ', '*****'], title='Confusion Matrix')

#Plotting normalized confusion matrix
plot_confusion_matrix(Y_test, Y_pred, Classes = ['*    ', '**   ', '***  ', '**** ', '*****'], normalize = True, title = 'Confusion Matrix - Normalized')

from sklearn import metrics

def get_metrics(true_labels, predicted_labels):
  print('Accuracy:', np.round(metrics.accuracy_score(true_labels, predicted_labels), 4))
  print('Precision:', np.round(metrics.precision_score(true_labels, predicted_labels, average='weighted'),4))
  print('Recall:', np.round(metrics.recall_score(true_labels, predicted_labels, average='weighted'), 4))
  print('F1 Score:', np.round(metrics.f1_score(true_labels, predicted_labels, average='weighted'), 4))

get_metrics(Y_test, Y_pred)
  
def display_classification_report(true_labels, predicted_labels, Classes):
  report = metrics.classification_report(y_true=true_labels, y_pred=predicted_labels, target_names=Classes)
  print("\nReport:\n"+report)

display_classification_report(Y_test, Y_pred, Classes=['*    ', '**   ', '***  ', '**** ', '*****'])

import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import roc_curve, auc, roc_auc_score

target= ['*    ', '**   ', '***  ', '**** ', '*****']

# set plot figure size
fig, c_ax = plt.subplots(1,1, figsize = (12, 8))

# function for scoring roc auc score for multi-class
def multiclass_roc_auc_score(y_test, y_pred, average="macro"):
  lb = LabelBinarizer()
  lb.fit(y_test)
  y_test = lb.transform(y_test)
  y_pred = lb.transform(y_pred)
  
  for (idx, c_label) in enumerate(target):
    fpr, tpr, thresholds = roc_curve(y_test[:,idx].astype(int), y_pred[:,idx])
    c_ax.plot(fpr, tpr, label = '%s (AUC:%0.2f)' % (c_label, auc(fpr, tpr)))
  
  c_ax.plot(fpr, fpr, 'b-', label = 'Random Guessing')
  return roc_auc_score(y_test, y_pred, average=average)

print('ROC AUC score:', multiclass_roc_auc_score(Y_test, Y_pred))

c_ax.legend()
c_ax.set_xlabel('False Positive Rate')
c_ax.set_ylabel('True Positive Rate')
plt.show()

