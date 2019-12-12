# Linear Regression Models

In this model, I implement some sort of supervised learning to make predictions of some future data based on trends that have been observed from a training set.

## With one variable (X)

To demonstrate the linear regression learning algorithm with a single variable, a data set has been provided in `data_set.txt`. Assume that the data provided represent the profit margin for a retail store with respect to the population of the city in which the store is located.

The algorithm uses the data set in make predictions predictions on profit based on city population. In order to achieve this, the example data is used to find the mean square error or the cost for each data pair. Then the gradient decent algorithm is applied to the cost function to minimize the cost for the data set. This helps us compute the values of &#x3b8;<sub>0</sub> and &#x3b8;<sub>1</sub>.

With the values of &#x3b8;<sub>0</sub> and &#x3b8;<sub>1</sub> computed, we can then use the equation below to make other predictions of values not in the training set.

<strong>
  <p style="text-align: center; color: blue;">
    h<sub>&#x3b8;</sub>(x) = &#x3b8;<sub>0</sub> + &#x3b8;<sub>1</sub>x
  </p>
</strong>

The Cost Function (where **m** is the number of training examples):
<strong>
  J(&#x3b8;<sub>0</sub>, &#x3b8;<sub>1</sub>) = 1/2m * sum(h<sub>&#x3b8;</sub>(x<sup>(i)</sup>) - y<sup>(i)</sup>)<sup>2</sup>
</strong>

Applying gradient decent to compute &#x3b8;:
<strong>
  &#x3b8;<sub>j</sub> := &#x3b8;<sub>j</sub> - &#x3b1; * 1/m * sum(h<sub>&#x3b8;</sub>(x<sup>(i)</sup>) - y<sup>(i)</sup>)* x<sub>j</sub><sup>(i)</sup>
</strong>

For the data set provided, we get the following values for &#x3b8;<sub>0</sub> and &#x3b8;<sub>1</sub> respectively: -3.87, 1.19. Therefore our best fit line will be:

![plot showing best fit line](https://res.cloudinary.com/iyikuyoro/image/upload/c_scale,w_600/v1576102385/GitHub%20Readme%20Images/Screenshot_2019-12-11_at_23.03.36.png)

We can then predict that for a city population of 70,000, the store is likely to make a profit of 44645.45.
