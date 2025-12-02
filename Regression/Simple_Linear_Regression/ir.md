**Simple Linear Regression** is a statistical method used to model the relationship between two continuous variables. It assumes that there is a linear relationship between the dependent variable (also called the response or output) and the independent variable (also called the predictor or input).

The general form of a simple linear regression equation is:

\[
y = \beta_0 + \beta_1 x + \epsilon
\]

Where:
- \( y \) is the dependent variable.
- \( x \) is the independent variable.
- \( \beta_0 \) is the intercept (the value of \( y \) when \( x = 0 \)).
- \( \beta_1 \) is the slope (how much \( y \) changes for a unit change in \( x \)).
- \( \epsilon \) is the error term (the difference between the observed and predicted values of \( y \)).

### Steps to perform Simple Linear Regression:
1. **Collect Data:** Obtain a dataset with pairs of values for the independent variable \( x \) and dependent variable \( y \).
2. **Calculate the coefficients:**
   - The slope (\( \beta_1 \)) is calculated as:
   
   \[
   \beta_1 = \frac{N(\sum x_i y_i) - (\sum x_i)(\sum y_i)}{N(\sum x_i^2) - (\sum x_i)^2}
   \]

   - The intercept (\( \beta_0 \)) is calculated as:
   
   \[
   \beta_0 = \frac{\sum y_i - \beta_1 \sum x_i}{N}
   \]

   Where:
   - \( N \) is the number of data points.
   - \( x_i \) and \( y_i \) are the individual data points of \( x \) and \( y \).
   
3. **Make Predictions:** Use the equation \( y = \beta_0 + \beta_1 x \) to make predictions for the dependent variable \( y \) for any given value of \( x \).
4. **Evaluate the Model:**
   - **R-squared (\( R^2 \))**: Measures the proportion of variance in the dependent variable that is predictable from the independent variable.
   - **Mean Squared Error (MSE)**: Measures the average of the squared differences between the actual and predicted values of \( y \).

### Example (Python code with Scikit-learn):
Here's how you can implement Simple Linear Regression in Python using Scikit-learn:

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Sample data
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Independent variable (reshaped for sklearn)
y = np.array([1, 2, 1.3, 3.75, 2.25])  # Dependent variable

# Create a Linear Regression model
model = LinearRegression()

# Fit the model to the data
model.fit(x, y)

# Make predictions
y_pred = model.predict(x)

# Coefficients
print(f"Intercept (β0): {model.intercept_}")
print(f"Slope (β1): {model.coef_}")

# Evaluate the model
print(f"Mean Squared Error (MSE): {mean_squared_error(y, y_pred)}")
print(f"R-squared: {r2_score(y, y_pred)}")

# Plot the data and the regression line
plt.scatter(x, y, color='blue', label='Data')
plt.plot(x, y_pred, color='red', label='Regression Line')
plt.xlabel('Independent Variable (x)')
plt.ylabel('Dependent Variable (y)')
plt.legend()
plt.show()
```
