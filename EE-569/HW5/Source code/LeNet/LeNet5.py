import numpy as np
import matplotlib.pyplot as plt
import cv2
import keras
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Dense, Activation, Dropout, Flatten
from keras import optimizers


# The function to creat a convolutional neural network
def creat_net(train_data, class_num, ini_name):
    my_model = Sequential()

    # The 1st convolutional layer
    my_model.add(Conv2D(6, kernel_initializer=ini_name, bias_initializer='zeros',
                        kernel_size=5, strides=1, padding='valid', input_shape=train_data.shape[1:]))
    my_model.add(Activation('relu'))

    # The 1st max-pooling layer
    my_model.add(MaxPool2D(pool_size=(2, 2), strides=2, padding='valid'))
    # my_model.add(Dropout(0.25))

    # The 2nd convolutional layer
    my_model.add(Conv2D(16, kernel_initializer=ini_name, bias_initializer='zeros',
                        kernel_size=5, strides=1, padding='valid'))
    my_model.add(Activation('relu'))

    # The 2nd max-pooling layer
    my_model.add(MaxPool2D(pool_size=(2, 2), strides=2, padding='valid'))
    # my_model.add(Dropout(0.25))

    # The 3 fully connected layers
    my_model.add(Flatten())
    # The first one
    my_model.add(Dense(120))
    my_model.add(Activation('relu'))
    # my_model.add(Dropout(0.25))
    # The second one
    my_model.add(Dense(84))
    my_model.add(Activation('relu'))
    # my_model.add(Dropout(0.25))
    # The third one
    my_model.add(Dense(class_num))
    my_model.add(Activation('softmax'))

    # The summary of the model
    my_model.summary()
    return my_model


# The function to try different types of parameter setting and plot accuracy curves
def net_accuracy_demo(train_data, train_label, test_data, test_label,
                      ini_name, i, learning_rate, decay_value):
    # Declare necessary variables
    batch_size = 32
    class_num = 10
    epoch_num = 20

    # Pre-process the data by converting class vectors into binary class metrics
    train_label = keras.utils.to_categorical(train_label, class_num)
    test_label = keras.utils.to_categorical(test_label, class_num)

    # Creat a convolutional neural network
    lenet5 = creat_net(train_data, class_num, ini_name)

    # Initialize the stochastic gradient descend optimizer
    sgd = optimizers.SGD(lr=learning_rate, decay=decay_value, momentum=0.85, nesterov=True)

    # Train the model by using the SGD optimizer
    lenet5.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
    train_data = train_data.astype('float32')
    test_data = test_data.astype('float32')
    train_data /= 255
    test_data /= 255

    val = (test_data, test_label)
    training_history = lenet5.fit(train_data, train_label, batch_size=batch_size, epochs=epoch_num,
                                  validation_data=val, shuffle=True)

    # Plot training & validation accuracy curves
    plt.plot(training_history.history['loss'], linestyle='dashed', color='yellow')
    plt.plot(training_history.history['accuracy'], linestyle='solid', color='green')
    plt.plot(training_history.history['val_loss'], linestyle='dashed', color='blue')
    plt.plot(training_history.history['val_accuracy'], linestyle='solid', color='red')
    plt.title("The performance curves of the trained model")
    plt.ylabel("The values of relevant performance")
    plt.xlabel("The ith epoch")
    plt.legend(["Train loss", "Train accuracy", "Test loss", "Test accuracy"], loc='upper right')
    plt.savefig("The %s performance curves" % i)
    plt.show()

    test_score = lenet5.evaluate(test_data, test_label)

    return test_score


def main():
    # Declare necessary variables

    # import training data, training labels, testing data, and testing labels
    (TrainData, TrainLabel), (TestData, TestLabel) = cifar10.load_data()
    TestLoss = []
    TestAccuracy = []
    
    # Three initialization methods
    InializerName1 = 'glorot_uniform'
    InializerName2 = 'glorot_normal'
    InializerName3 = 'he_uniform'
    
    """
    # The case1: the initializer is "glorot_uniform", the learning rate is 0.02, the decay is 0.0001
    TestScore1 = net_accuracy_demo(TrainData, TrainLabel, TestData, TestLabel,
                                   InializerName1, 1, 0.02, 0.0001)
    TestLoss.append(TestScore1[0])
    TestAccuracy.append(TestScore1[1]) 
    
    
    # The case2: the initializer is "glorot_uniform", the learning rate is 0.01, the decay is 0.00001
    TestScore2 = net_accuracy_demo(TrainData, TrainLabel, TestData, TestLabel,
                                   InializerName1, 2, 0.01, 0.00001)
    TestLoss.append(TestScore2[0])
    TestAccuracy.append(TestScore2[1])
    # The case3: the initializer is "glorot_normal", the learning rate is 0.03, the decay is 0.0002
    TestScore3 = net_accuracy_demo(TrainData, TrainLabel, TestData, TestLabel,
                                   InializerName2, 3, 0.03, 0.0002)
    TestLoss.append(TestScore3[0])
    TestAccuracy.append(TestScore3[1])
    # The case4: the initializer is "he_uniform", the learning rate is 0.02, the decay is 0.0001
    TestScore4 = net_accuracy_demo(TrainData, TrainLabel, TestData, TestLabel,
                                   InializerName3, 4, 0.02, 0.0001)
    TestLoss.append(TestScore4[0])
    TestAccuracy.append(TestScore4[1])
    # The case5: the initializer is "glorot_uniform", the learning rate is 0.04, the decay is 0.0003
    TestScore5 = net_accuracy_demo(TrainData, TrainLabel, TestData, TestLabel,
                                   InializerName1, 5, 0.04, 0.0003)
    TestLoss.append(TestScore5[0])
    TestAccuracy.append(TestScore5[1])
    

    print('train_data shape', TrainData.shape)  # train_data: (50000, 32, 32, 3)
    print('train_label shape', TrainLabel.shape)  # train_label: (50000, 1)
    print('test_data shape', TestData.shape)  # test_data: (10000, 32, 32, 3)
    print('test_label shape', TestLabel.shape)  # test_label: (10000, 1)

    for i, LossValue in enumerate(TestLoss):
        print("For case %s, the loss for the testing samples:" % (i+1), LossValue)
    for i, AccuracyValue in enumerate(TestAccuracy):
        print("For case %s, the accuracy for the testing samples:" % (i+1), AccuracyValue)
    """

    TestScore6 = net_accuracy_demo(TrainData, TrainLabel, TestData, TestLabel,
                                   InializerName3, 6, 0.02, 0.0001)
    print("The loss for the testing samples:", TestScore6[0])
    print("The accuracy for the testing samples:", TestScore6[1])


if __name__ == '__main__':
    main()
    print('The program is over successfully!')
