# Linear Regression Model

In this model, I implement some sort of supervised learning to make predictions of some future data based on trends that have been observed from a training set.

## With one variable (X)

To demonstrate the linear regression learning algorithm with a single variable, a data set has been provided in `data_set.txt`. Assume that the data provided represent the profit margin for a retail store with respect to the population of the city in which the store is located.

- After plotting the data, we have a scatter that looks like this:
  ![profit by city population plot](https://res.cloudinary.com/iyikuyoro/image/upload/c_scale,w_600/v1576093356/GitHub%20Readme%20Images/Screenshot_2019-12-11_at_20.40.54.png)
- From the scatter plot above, I am going to use a straight line:
<strong>
  <p style="text-align: center; color: blue;">
    h<sub>&#x3b8;</sub>(x) = &#x3b8;<sub>0</sub> + &#x3b8;<sub>1</sub>x
  </p>
</strong>

- To calculate the cost, we will use a simplified version of the mean squared error:
<strong>
  <p style="text-align: center; color: blue;">
    J(&#x3b8;<sub>0</sub>, &#x3b8;<sub>1</sub>) = 1/2m * sum(h<sub>&#x3b8;</sub>(x<sup>(i)</sup>) - y<sup>(i)</sup>)<sup>2</sup>
  </p>
</strong>
<p style="text-align: center;">where m is the number of training examples</p>

- The cost is minimized using gradient decent by which the values of &#x3b8; are updated by
  <strong></strong>
