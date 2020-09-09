# ACM Research Coding Challenge (Fall 2020)

## No Collaboration Policy

**You may not collaborate with anyone on this challenge.** You _are_ allowed to use Internet documentation. If you _do_ use existing code (either from Github, Stack Overflow, or other sources), **please cite your sources in the README**.

## Submission Procedure

Please follow the below instructions on how to submit your answers.

1. Create a **public** fork of this repo and name it `ACM-Research-Coding-Challenge`. To fork this repo, click the button on the top right and click the "Fork" button.
2. Clone the fork of the repo to your computer using . `git clone [the URL of your clone]`. You may need to install Git for this (Google it).
3. Complete the Challenge based on the instructions below.
4. Email the link of your repo to research@acmutd.co with the same email you used to submit your application. Be sure to include your name in the email.

## Question One

![Image of Cluster Plot](ClusterPlot.png)
<br/>
Given the following dataset in `ClusterPlot.csv`, determine the number of clusters by using any clustering algorithm. **You're allowed to use any Python library you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file.


## Introduction

Before this project, I had no prior experience in Data Science, clustering algorithms, or even Python. I first had to do a lot of research on the subject and the language before I started working on this project

## Research

Due to my lack of knowledge in Data Science, I started off by watching videos since I consider myself a visual learner and the explanations would be simpler before I read more detailed articles. Ultimately I decided to use the K-mean Clustering, a method I choose because of its linear complexity O(n) and its simplicity for less experienced people in the field of Data Science.I also came across the elbow method which was useful to find the optimal k - value

## The program

The method I used to solve this problem was the k-means method, a method used to group data points into k clusters. These clusters are based on vector distances from points or centers on the graph. In order to solve this, we first need an optimal k - value. For that, I used a method called the “elbow method”, which compares distortions and k values. I used a third-party library called sci-kit learn that would take the data points and run them into clusters based on a range I set (1-15). With this, we are able to graph the result which shows the most optimal value for k was 3. However, in order for the program to find this k-value, I used an approximation where the first instance of a decrease of 50% would become the k-value(I came up this through trial and error from other examples during my research). This matched the result of the graph and now we have the optimal k- value. 
<br/>
![Image of optimal k - value](C:\Users\01sud\Coding-Challenge\figure_1.png)
<br/>
Then using Sci-kit learning and matplot, we were able to graph the clusters based on the k-value.
![Image of Clustered data points](C:\Users\01sud\Coding-Challenge\figure_2.png)

## Python libraries

NumPy <br/>
Panda <br/>
Sci-kit learn <br/>
Matplot <br/>

## Sources
https://towardsdatascience.com/the-5-clustering-algorithms-data-scientists-need-to-know-a36d136ef68 

https://scikit-learn.org/stable/auto_examples/cluster/plot_mean_shift.html#sphx-glr-auto-examples-cluster-plot-mean-shift-py  

https://www.geeksforgeeks.org/ml-determine-the-optimal-value-of-k-in-k-means-clustering/

https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html 

https://realpython.com/k-means-clustering-python/

https://www.tutorialspoint.com/machine_learning_with_python/machine_learning_with_python_clustering_algorithms_k_means.htm 

https://stackoverflow.com/  

https://pythonprogramming.net/forecasting-predicting-machine-learning-tutorial/ 

https://www.geeksforgeeks.org/  

https://blog.exploratory.io/k-means-clustering-deciding-how-many-clusters-to-build-d33fd9c68088 

https://predictivehacks.com/k-means-elbow-method-code-for-python/  

https://www.datadriveninvestor.com/2020/01/21/elbow-method-metric-which-helps-in-deciding-the-value-of-k-in-k-means-clustering-algorithm/  

https://medium.com/analytics-vidhya/how-to-determine-the-optimal-k-for-k-means-708505d204eb  

https://blog.cambridgespark.com/how-to-determine-the-optimal-number-of-clusters-for-k-means-clustering-14f27070048f 


## Videos

https://www.youtube.com/watch?v=1XqG0kaJVHY 

https://www.youtube.com/watch?v=ZueoXMgCd1c 

