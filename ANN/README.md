## Artifical Neural Network

We use Tensorflow to create a network to categorize fashion articles using the Fashion MNIST dataset. We start by loading the dataset, flatting the input from 2D to 1D and changing the output to categorical. Changing the ouput to categorical can be best illustrated through an example: instead of the output being the number 3 for the dress category, it is the vector [0,0,0,1,0,0,0,0,0,0], i.e. the vector with the index 3 set to 1 and all the other indicies set to 0. 

Thus, the output layer in our network contains 10 nodes, where only one of the nodes will be set to 1 at the end of execution. This layout of the output layer is called a One-Hot Vector.     

We start with a network with 784 inputs, a hidden layer with 10 nodes, and an ouput layer. Then, we make it wider and deeper. This is how the accuracy on the test data changes in response to changing the network:
- model1: 
    - Hidden Layers: 1
    - Nodes per hidden layer: 10
    - Accuray: 84.26%
- model2: 
    - Hidden Layers: 1
    - Nodes per hidden layer: 50
    - Accuracy: 87.53%
- model3:
    - Hidden Layers: 2
    - Nodes per hidden layer: 50
    - Accuracy: 87.8%