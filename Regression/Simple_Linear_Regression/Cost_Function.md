## 💡 What is the Cost Function in Linear Regression?

In **Linear Regression**, our goal is to find the **best-fitting straight line**:

[
\hat{Y} = β_0 + β_1X
]

that predicts (Y) (dependent variable, like salary) from (X) (independent variable, like CGPA or experience).

To measure **how well the line fits the data**, we use a **Cost Function** — a formula that calculates **how much error** exists between our predictions and the actual data.

---

## 🎯 Purpose of the Cost Function

👉 The **Cost Function** helps us *quantify the error*.
👉 Our goal is to **minimize** this cost so that predictions are as close to reality as possible.

---

## 🧮 The Mathematical Formula

The most common cost function used in Linear Regression is the **Mean Squared Error (MSE)**:

[
J(β_0, β_1) = \frac{1}{2m} \sum_{i=1}^{m} (h_θ(x_i) - y_i)^2
]

Let’s break it down:

| Symbol         | Meaning                                                                        |
| -------------- | ------------------------------------------------------------------------------ |
| (J(β_0, β_1))  | Cost function (value to minimize)                                              |
| (m)            | Number of data points                                                          |
| (h_θ(x_i))     | Predicted value for data point i → (β_0 + β_1x_i)                              |
| (y_i)          | Actual output value                                                            |
| (\frac{1}{2m}) | Normalizes the error (average), and ½ is for easy derivative calculation later |

---

## 💬 Step-by-Step Intuition

1. **Make Predictions:**
   Use your model (line) to predict values of Y for all given Xs.
   Example:
   If (X = 5), (Ŷ = β_0 + β_1×5)

2. **Find Errors (Residuals):**
   [
   \text{Error} = Y - \hat{Y}
   ]
   This shows how far each prediction is from the true value.

3. **Square Each Error:**
   To remove negatives and penalize large errors.

4. **Sum All Errors and Divide by n:**
   To find the average error → Mean Squared Error.

---

## 📉 Geometric Meaning

* Imagine several points scattered around a line.
* Each vertical distance between a point and the line is an **error**.
* The Cost Function tells us the **total “distance”** of all points from the line (in squared form).
* The smaller this value, the **better the line fits**.

---

## 🧠 Why We Minimize It

The line with the **lowest cost function value** is the **best-fit line**.
We can find it by:

* Using **Ordinary Least Squares (OLS)** (analytical solution), or
* Using **Gradient Descent** (iterative optimization method).

---

## 📊 Example in Code

```python
import numpy as np

# Actual vs Predicted
Y_actual = np.array([10, 20, 30, 40, 50])
Y_pred = np.array([12, 22, 28, 43, 48])

# Calculate Cost (MSE)
m = len(Y_actual)
cost = (1/(2*m)) * np.sum((Y_pred - Y_actual)**2)

print("Cost Function Value (MSE):", cost)
```

🧩 Output:

```
Cost Function Value (MSE): 6.9
```

➡️ This means on average, our model’s squared error is 6.9 units (lower is better).

---

## 🧭 Summary Table

| Concept                  | Description                                     |
| ------------------------ | ----------------------------------------------- |
| **Objective**            | Find line that minimizes total prediction error |
| **Formula**              | ( J = \frac{1}{2m}\sum (Ŷ - Y)^2 )             |
| **Best Fit Line**        | Occurs when cost function is minimal            |
| **Minimization Methods** | OLS or Gradient Descent                         |
| **Key Output**           | (β_0) (intercept) and (β_1) (slope)             |




[Cost Function](../Images/Cost_Function.png)

The X-axis shows different possible slope (β1) values,
and the Y-axis shows the cost (error) for each slope.

🟦 Notice the U-shaped “bowl” curve — this represents the cost function.

The lowest point on this curve is where the cost is minimal, meaning that’s the best value of 𝛽1 for your linear regression line — the line that fits the data best.