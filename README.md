# My journey to learning ML 
As a hands-on learner, I learn by doing. Thus, to explore ML, I will start by working on small projects, working my way up to more complicated ones and I will document my journey through this repository.   
If any project is not my original idea, I will include the link to the original creator. 
My current goal is to have a good understanding of Neural Networks by the end of June 2021. 

## Projects 
### Cartoonify 
Turn any picture into a cartoon! 
- Used OpenCV with Python to edit an image and give it a "cartoon effect"
- Original source: https://data-flair.training/blogs/cartoonify-image-opencv-python/

### Single Layer Perceptrons
To learn about Neural Networks, I started by exploring the simplest one there is, a single layered perceptron.     

To begin, I followed [this simple tutorial](https://towardsdatascience.com/first-neural-network-for-beginners-explained-with-code-4cfd37e06eaf) and created a Perceptron for the logical operation "Inclusive OR", then expanded it just a little to also include the logical operator "AND".    

Afterwards, I read more about Perceptron Learning Rules in [this chapter](http://hagan.okstate.edu/4_Perceptron.pdf). Very highly recommended.     

At this point, I was comfortable enough to write a simple perceptron myself. I created a Perceptron to predict whether an individual has diabities using the Pima Indian Diabities dataset from Kaggle. To test its accuracy, I first randomly shuffle the dataset, then split 60-40 for training and testing. Afterwards, I ran it a few times and found that on average, it accurately predicted the outcome on 60-70% of the test data.       

Understandbly, this is a small sample with multiple variables, thus the single layer perceptron will likely not do well with new data. I predict that using an Aritifical Neural Network with more hidden layers will make the predicitons more accurate. I will use the same dataset as I continue to learn about ANN and see how the accuracy of predicitons improve. 

### Artifical Neural Network using Tensorflow 
At this point, I had a clearer understanding of the structure and goal of an Artifical Neural Network (ANN) and how we go from one layer to another using the weights and biases. During the "learning" or "training" step, the network uses the training data to modify the weights and bias to get a neural network with better accuracy. But that raised the question, how exactly does the ANN know how to modify the weights and biases? That is done through a process called **backpropagation**. 
To understand the math behind backpropogation, I read this [article](https://medium.com/analytics-vidhya/feedforward-and-backpropagation-mathematics-behind-a-simple-artificial-neural-network-fd3f3ae15e3b) that explains the process for a network with two hidden layers with two nodes. The same ideas are generalized for larger networks. A small warning, a basic background in linear algebra and multivariant calculus is needed to follow the article.    

Now that we understand the math behind the ANN, we can use frameworks that have already implemented those algorithms to build our first ANN. I wanted to use [Tensorflow](https://www.tensorflow.org/) as it is one of the most frameworks for machine learning. To do so, I started with [this step-by-step tutorial](https://becominghuman.ai/step-by-step-neural-network-tutorial-for-beginner-cc71a04eedeb) to build an ANN that classifies articles of clothes using the [Fashion MNIST dataset](https://www.kaggle.com/zalando-research/fashionmnist). However, since the article is for beginners, it left me wanting more answers. I wanted to understand why the author made some of the choices that he made. For that I did some more reading. Here's a list of questions that I had and the articles I read to get a better explanation

- Why use Sequential Model? What other models are there?     
[Keras Models Explanation](https://data-flair.training/blogs/keras-models/)
- What is the difference between the sigmoid and softmax functions? Why use one over the other? How to determine what activation function to use in general? [Sigmoid vs Softmax](https://dataaspirant.com/difference-between-softmax-function-and-sigmoid-function/)   
 [How to choose an activation function](https://machinelearningmastery.com/choose-an-activation-function-for-deep-learning/)
- Can increasing the epochs cause overfitting? If so, how to chose an optimal value?      
 [Yes, too many epochs can cause overfitting.](https://towardsdatascience.com/epoch-vs-iterations-vs-batch-size-4dfb9c7ce9c9)    
 [Keras's EarlyStopping() function to avoid overfitting](https://www.geeksforgeeks.org/choose-optimal-number-of-epochs-to-train-a-neural-network-in-keras/)
 - What are the adam and rmsprop optimizers? Why pick one over the other?      
 [Momentum, RMSProp and Adam Optimizations](https://blog.paperspace.com/intro-to-optimization-momentum-rmsprop-adam/) 

 Towards the end of the tutorial, we see that the accuracy was not getting any better by making the network wider and deeper. The author then suggests using a Convolutional Neural Network (CNN) instead. As CNN is a seprate class of networks, I will dive deeper into it in a seprate project instead.
