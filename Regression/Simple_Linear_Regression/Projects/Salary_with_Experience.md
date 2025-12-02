# 📘 Example: Predicting Salary from Years of Experience

---

## 1. **Problem**

A company wants to predict an employee’s **salary** based on their **years of experience**.

* **Input (X):** Years of experience.
* **Output (Y):** Salary.

---

## 2. **Dataset (Sample Data)**

| Years of Experience (X) | Salary (\$ in 1000s) (Y) |
| ----------------------- | ------------------------ |
| 1                       | 40                       |
| 2                       | 45                       |
| 3                       | 50                       |
| 4                       | 55                       |
| 5                       | 60                       |
| 6                       | 65                       |
| 7                       | 70                       |

---

## 3. **Visualizing the Data**

If you plot this data:

* X-axis = Years of Experience.
* Y-axis = Salary.

You’ll see the points form a **straight line trend**.

---

## 4. **Linear Regression Equation**

The model tries to find the best-fit line:

$$
Salary = β_0 + β_1 \times (Experience)
$$

Suppose the model finds:

$$
Salary = 35 + 5 \times (Experience)
$$

* $β_0 = 35$ → Starting salary (base, even with 0 experience).
* $β_1 = 5$ → Salary increases by 5 (i.e., \$5000) for each additional year of experience.

---

## 5. **Making Predictions**

* If someone has **2 years of experience**:

  $$
  Salary = 35 + 5(2) = 45 \ (\$45,000)
  $$

* If someone has **5 years of experience**:

  $$
  Salary = 35 + 5(5) = 60 \ (\$60,000)
  $$

* If someone has **10 years of experience**:

  $$
  Salary = 35 + 5(10) = 85 \ (\$85,000)
  $$

---

## 6. **Why is This Useful?**

* **HR Department** can predict fair salaries for new hires.
* **Employees** can estimate expected growth.
* **Managers** can plan budgets based on future salary projections.

---

## 7. **Graph (Conceptual)**

```
Salary (Y)
  ^
  |                           *
  |                        *
  |                     *
  |                  *
  |               *
  |            *
  |_________*____________________> Experience (X)
             1   2   3   4   5   6   7
```

The `*` points are actual data, and the **line through them** is the regression line.

---

✅ This example clearly shows **how linear regression works in real life**:
It takes input (experience), fits a straight line, and allows predictions (salary).

