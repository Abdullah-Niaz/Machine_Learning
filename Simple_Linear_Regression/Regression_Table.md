## 🧮 1. Dependent Variable

* **Meaning:**
  The main variable you’re trying to predict or explain.
* **Example:**
  In predicting **house prices**, the dependent variable = `Price`.

---

## 🧩 2. Independent Variables (Predictors)

* **Meaning:**
  The variables that explain changes in the dependent variable.
* **Example:**
  `Size`, `Rooms`, and `Location Score` might affect `Price`.

---

## 📈 3. Coefficient (β or Estimate)

* **Meaning:**
  It shows **how much the dependent variable changes** when one predictor increases by **1 unit**, keeping others constant.
* **Sign Interpretation:**

  * Positive β → as the variable increases, the dependent variable increases.
  * Negative β → as the variable increases, the dependent variable decreases.
* **Formula:**
  [
  Y = β_0 + β_1X_1 + β_2X_2 + ... + ε
  ]
* **Example:**
  If `Size` = 120, it means every extra square foot adds **$120** to the house price.

---

## ⚖️ 4. Intercept (β₀)

* **Meaning:**
  The expected value of the dependent variable when **all independent variables are 0**.
* **Example:**
  If intercept = 50,000, it means when `Size=0`, `Rooms=0`, and `Location=0`, the base house price starts at **$50,000**.

---

## 📉 5. Standard Error (SE)

* **Meaning:**
  It measures the **accuracy** of each coefficient — smaller SE means the estimate is more reliable.
* **Why important:**
  Large SE means the coefficient might not be precise.
* **Example:**
  If coefficient = 120 and SE = 10 → it’s very precise.
  If coefficient = 120 and SE = 80 → very uncertain.

---

## 🧮 6. t-Statistic (t-value)

* **Meaning:**
  Tests if the coefficient is **significantly different from 0**.
  It tells how many standard errors away from 0 your coefficient is.
* **Formula:**
  [
  t = \frac{β}{SE}
  ]
* **Example:**
  If β = 120, SE = 10 → t = 12.
  Large |t| means strong evidence that the variable matters.

---

## 📊 7. p-Value

* **Meaning:**
  Probability that the coefficient is **not actually different from 0** (i.e., by random chance).
* **Interpretation:**

  * p < 0.05 → statistically significant (strong evidence)
  * p ≥ 0.05 → not significant (weak evidence)
* **Example:**
  p = 0.001 → very significant.
  p = 0.40 → not significant.

---

## 📉 8. R-squared (R²)

* **Meaning:**
  Measures how well the model **explains the variation** in the dependent variable.
* **Formula:**
  [
  R^2 = 1 - \frac{SS_{res}}{SS_{tot}}
  ]
  where
  ( SS_{res} ) = residual (error) sum of squares,
  ( SS_{tot} ) = total sum of squares.
* **Interpretation:**

  * R² = 0 → model explains nothing.
  * R² = 1 → model explains everything perfectly.
* **Example:**
  R² = 0.85 → model explains 85% of variation in price.

---

## 🧾 9. Adjusted R-squared

* **Meaning:**
  Like R², but it **penalizes** you for adding too many unnecessary variables.
* **Use:**
  Better for comparing models with different numbers of predictors.

---

## 📊 10. F-statistic and its p-value

* **Meaning:**
  Tests if the **entire regression model** is statistically significant (i.e., at least one variable matters).
* **Example:**
  F = 50, p < 0.001 → model as a whole is significant.

---

## 🪫 11. Residuals

* **Meaning:**
  The **difference between actual and predicted values**.
* **Use:**
  To check model accuracy and whether errors are random or patterned.

---

### ✅ Example Summary Table

| Variable        | Coefficient (β) | Std. Error | t-value | p-value | Interpretation     |
| --------------- | --------------- | ---------- | ------- | ------- | ------------------ |
| **Intercept**   | 50,000          | 5,000      | 10.0    | 0.000   | Base price         |
| **Size (sqft)** | 120             | 10         | 12.0    | 0.000   | +$120 per sq ft    |
| **Rooms**       | 5,000           | 2,000      | 2.5     | 0.015   | +$5,000 per room   |
| **Location**    | 10,000          | 3,000      | 3.3     | 0.001   | +$10,000 per score |

**R² = 0.85 →** Model explains 85% of variation in price
**F-statistic (p < 0.001)** → Model is statistically significant

