from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import cv2
import keras
from keras.datasets import cifar10
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Dense, Activation
from keras.layers import BatchNormalization, Dropout, Flatten
from keras import optimizers
from keras import regularizers
from sklearn.model_selection import train_test_split
import time


# The function to creat a convolutional neural network
def creat_net(train_data, class_num):
    weight_decay = 0.0005     # Set the value of weight decay as 0.0005
    my_model = Sequential()   # Initialize my model

    # The 1st convolutional layer: I have to think about the shape of input data
    my_model.add(Conv2D(64, (3, 3), padding='same', input_shape=train_data.shape[1:],
                 kernel_regularizer=regularizers.l2(weight_decay)))
    my_model.add(Activation('relu'))
    my_model.add(BatchNormalization())
    my_model.add(Dropout(0.3))

    # The 2nd convolutional layer
    my_model.add(Conv2D(64, (3, 3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    my_model.add(Activation('relu'))
    my_model.add(BatchNormalization())

    # The 1st max-pooling layer
    my_model.add(MaxPool2D(pool_size=(2, 2)))

    # The 3rd convolutional layer
    my_model.add(Conv2D(128, (3, 3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    my_model.add(Activation('relu'))
    my_model.add(BatchNormalization())
    my_model.add(Dropout(0.4))

    # The 4th convolutional layer
    my_model.add(Conv2D(128, (3, 3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    my_model.add(Activation('relu'))
    my_model.add(BatchNormalization())

    # The 2nd max-pooling layer
    my_model.add(MaxPool2D(pool_size=(2, 2)))

    # The 5th convolutional layer
    my_model.add(Conv2D(256, (3, 3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    my_model.add(Activation('relu'))
    my_model.add(BatchNormalization())
    my_model.add(Dropout(0.4))

    # The 6th convolutional layer
    my_model.add(Conv2D(256, (3, 3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    my_model.add(Activation('relu'))
    my_model.add(BatchNormalization())
    my_model.add(Dropout(0.4))

    # The 7th convolutional layer
    my_model.add(Conv2D(256, (3, 3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    my_model.add(Activation('relu'))
    my_model.add(BatchNormalization())

    # The 3rd max-pooling layer
    my_model.add(MaxPool2D(pool_size=(2, 2)))

    # The 8th convolutional layer
    my_model.add(Conv2D(512, (3, 3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    my_model.add(Activation('relu'))
    my_model.add(BatchNormalization())
    my_model.add(Dropout(0.4))

    # The 9th convolutional layer
    my_model.add(Conv2D(512, (3, 3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    my_model.add(Activation('relu'))
    my_model.add(BatchNormalization())
    my_model.add(Dropout(0.4))

    # The 10th convolutional layer
    my_model.add(Conv2D(512, (3, 3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    my_model.add(Activation('relu'))
    my_model.add(BatchNormalization())

    # The 4th max-pooling layer
    my_model.add(MaxPool2D(pool_size=(2, 2)))

    # The 11th convolutional layer
    my_model.add(Conv2D(512, (3, 3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    my_model.add(Activation('relu'))
    my_model.add(BatchNormalization())
    my_model.add(Dropout(0.4))

    # The 12th convolutional layer
    my_model.add(Conv2D(512, (3, 3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    my_model.add(Activation('relu'))
    my_model.add(BatchNormalization())
    my_model.add(Dropout(0.4))

    # The 13th convolutional layer
    my_model.add(Conv2D(512, (3, 3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    my_model.add(Activation('relu'))
    my_model.add(BatchNormalization())

    # The 5th max-pooling layer
    my_model.add(MaxPool2D(pool_size=(2, 2)))
    my_model.add(Dropout(0.5))

    # The fully connected layers
    my_model.add(Flatten())
    my_model.add(Dense(512, kernel_regularizer=regularizers.l2(weight_decay)))
    my_model.add(Activation('relu'))
    my_model.add(BatchNormalization())

    my_model.add(Dropout(0.5))
    my_model.add(Dense(class_num))
    my_model.add(Activation('softmax'))

    # The summary of the model that will show the number of parameters
    my_model.summary()
    return my_model


# The function to normalize input data to be zero mean and unit variance
def normal_process(train_data, test_data):
    mean_value = np.mean(train_data, axis=(0, 1, 2, 3))     # Calculate the mean value
    std_value = np.std(train_data, axis=(0, 1, 2, 3))       # Calculate the standard deviation
    train_data = (train_data-mean_value)/(std_value+1e-7)   # Normalize the training data
    test_data = (test_data-mean_value)/(std_value+1e-7)     # Normalize the testing data
    return train_data, test_data


# The function to try different types of parameter setting and plot accuracy curves
def net_accuracy_demo(train_data, train_label, test_data, test_label):
    # Initialize necessary variables
    batch_size = 128
    class_num = 10
    epoch_num = 100
    learning_rate = 0.1
    lr_decay = 1e-6
    lr_drop = 20

    # Pre-process the data by converting class vectors into binary class metrics and changing data types
    train_data = train_data.astype('float32')
    test_data = test_data.astype('float32')
    train_data, test_data = normal_process(train_data, test_data)
    train_label = keras.utils.to_categorical(train_label, class_num)
    test_label = keras.utils.to_categorical(test_label, class_num)

    # Creat a convolutional neural network
    vgg_cifar10 = creat_net(train_data, class_num)

    # To implement the data augmentation
    datagen = ImageDataGenerator(
        featurewise_center=False,  # Set input mean as 0 over the entire dataset
        samplewise_center=False,  # Set each sample mean as 0
        featurewise_std_normalization=False,  # Divide inputs by standard deviation of the dataset
        samplewise_std_normalization=False,   # Divide each input by its standard deviation
        zca_whitening=False,  # Utilize ZCA whitening
        rotation_range=15,    # Randomly rotate images
        width_shift_range=0.1,   # Randomly shift images horizontally (fraction of total width)
        height_shift_range=0.1,  # Randomly shift images vertically (fraction of total height)
        horizontal_flip=True,   # Randomly flip images
        vertical_flip=False)    # Randomly flip images
    # Apply the operations above to training data
    datagen.fit(train_data)

    # Initialize the stochastic gradient descend optimizer
    sgd = optimizers.SGD(lr=learning_rate, decay=lr_decay, momentum=0.9, nesterov=True)

    # Train the model by using the SGD optimizer
    vgg_cifar10.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

    val = (test_data, test_label)  # Regard the test data as validation data
    training_history = vgg_cifar10.fit(train_data, train_label,
                                       batch_size=batch_size, epochs=epoch_num,
                                       validation_data=val, shuffle=True)

    # Plot the accuracy curve
    plt.figure()
    plt.plot(training_history.history['accuracy'], linestyle='solid', color='green')
    plt.plot(training_history.history['val_accuracy'], linestyle='solid', color='red')
    plt.title("The accuracy curves of the trained model")
    plt.ylabel("The values of accuracy")
    plt.xlabel("The ith epoch")
    plt.legend(["Train accuracy", "Test accuracy"], loc='lower right')
    plt.savefig("The accuracy curves")
    plt.show()

    # Plot the loss curve
    plt.figure()
    plt.plot(training_history.history['loss'], linestyle='dashed', color='yellow')
    plt.plot(training_history.history['val_loss'], linestyle='dashed', color='blue')
    plt.title("The loss curves of the trained model")
    plt.ylabel("The values of loss")
    plt.xlabel("The ith epoch")
    plt.legend(["Train loss", "Test loss"], loc='upper right')
    plt.savefig("The loss curves")
    plt.show()

    # Show the final testing score
    test_score = vgg_cifar10.evaluate(test_data, test_label)

    return test_score


def main():
    # Import training data, training labels, testing data, and testing labels
    (TrainData, TrainLabel), (TestData, TestLabel) = cifar10.load_data()
    print('Train_data shape', TrainData.shape)  # train_data: (50000, 32, 32, 3)
    print('Train_label shape', TrainLabel.shape)  # train_label: (50000, 1)
    print('Test_data shape', TestData.shape)  # test_data: (10000, 32, 32, 3)
    print('Test_label shape', TestLabel.shape)  # test_label: (10000, 1)

    # Randomly drop the training data
    TrainData1, temp_TrainData, TrainLabel1, temp_TrainLabel = \
        train_test_split(TrainData, TrainLabel, test_size=1-0.6, stratify=TrainLabel)
    print('Train_data1 shape', TrainData1.shape)
    print('Train_label1 shape', TrainLabel1.shape)

    # Get the test accuracy and loss value
    TestScore = net_accuracy_demo(TrainData, TrainLabel, TestData, TestLabel)
    print("The loss for the testing samples:", TestScore[0])
    print("The accuracy for the testing samples:", TestScore[1])


if __name__ == '__main__':
    time_start = time.time()
    main()
    print('The program is over successfully!')
    time_end = time.time()
    print('Running time for the PixelHop transform part: %s Seconds' % (time_end - time_start))

