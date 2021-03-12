# CS6910-Assignments
Code for assignments and projects for CS6910: Fundamentals of Deep Learning by Sujay and Avyay

1. The notebook is made such that the cells can be run sequentially

2. For creating a model, the syntax is given below. It is almost the same as in tensorflow/keras.

    ```python
    # define the model architecture in the list passed to NeuralNet() class
    model = NeuralNet([FC(784, 64), RelU(), FC(64, 10)], use_wandb=False)
    optimizer = NAG() # use any of the 6 available losses here
    loss = CrossEntropyLossFromLogits() use any of the 2 available losses
    ```

3. To compile the model so that it knows what loss and optimizer it's working with, use the following syntax

    `model.compile(loss=loss, optimizer=optimizer)`

4. To train the model, you have to specify both training and validation datasets along with batch size and number of    epochs to train for in the given syntax

    `model.fit(train_images, train_labels, val_images, val_labels, batch_size=128, epochs=5)`

5. To evaluate the model on a separate test dataset, use the following command

    `model.evaluate(test_images, test_labels)`