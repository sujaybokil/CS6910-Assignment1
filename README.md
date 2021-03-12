# CS6910-Assignments: Assignment 1

## Authors: Sujay Bokil (ME17B120) and Avyay Rao (ME17B130)

1. The notebook is made such that the cells can be run sequentially

2. For creating a model, the syntax is given below. It is almost the same as in tensorflow/keras.

    ```python
    # define the model architecture in the list passed to NeuralNet() class
    model = NeuralNet([FC(784, 64), RelU(), FC(64, 10)], use_wandb=False)
    optimizer = NAG() # use any of the 6 available losses here
    loss = CrossEntropyLossFromLogits() use any of the 2 available losses
    ```

3. To compile the model so that it knows what loss and optimizer it's working with, use the following syntax

    ```python
    model.compile(loss=loss, optimizer=optimizer)
    ```

4. To train the model, you have to specify both training and validation datasets along with batch size and number of    epochs to train for in the given syntax

    ```python
    model.fit(train_images, train_labels, val_images, val_labels, batch_size=128, epochs=5)
    ```

5. To evaluate the model on a separate test dataset, use the following command

    ```python
    model.evaluate(test_images, test_labels)
    ```

6. For running a wandb sweep, find out the train() function for setting up wandb sweeps using our framework. Set up a wandb sweep as follows and run the sweep using the commands shown.

    ```python

    # setting up hyperparameter configurations for the sweep
    sweep_config = {
        "name": "Sweep Test Master",
        "method": "grid",
        "parameters": {
                "epochs": {
                    "values": [5, 10]
                },
                "n_layers": {
                    "values": [3, 4, 5]
                }
            }
        }

    # setting up the sweep
    sweep_id = wandb.sweep(sweep_config)

    # running the sweep
    wandb.agent(sweep_id, function=train)
    ```

## Available options for the neural network

1. Loss functions

    ```python
    CrossEntropyLossFromLogits()
    MSELossFromLogits()

    ```

2. Activation functions

    ```python
    Sigmoid()
    RelU()
    Tanh()

    ```

3. Optimizers 

    ```python
    SGD()
    Momentum()
    NAG()
    RMSprop()
    Adam()
    Nadam()

    ```

4. Layers

    ```python
    FC() # represents fully connected layer
    ```