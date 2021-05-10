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
