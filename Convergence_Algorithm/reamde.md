# 1. What is a Convergence Algorithm?

A **convergence algorithm** is a procedure that repeatedly updates model parameters (like slope and intercept) until the **cost function stops decreasing**.
Linear regression typically uses **Gradient Descent** as its convergence algorithm.

The algorithm keeps updating parameters until they *converge* to the minimum point.
This minimum point is where the cost is smallest.

---

# 2. Why do we need a Convergence Algorithm?

Because

* we do not know the correct slope and intercept
* we need a systematic method to search for optimal values
* the cost function has a U shape
* the minimum point gives us the best line

Gradient Descent gradually moves down the cost graph until it reaches the minimum.

---

# 3. How Gradient Descent Helps Convergence

Gradient Descent does two things:

1. Checks the **direction of steepest descent**, meaning which direction reduces cost.
2. Takes a **step** in that direction using a learning rate.

The formula:

[
β_1 = β_1 - \alpha \frac{\partial J}{\partial β_1}
]

[
β_0 = β_0 - \alpha \frac{\partial J}{\partial β_0}
]

Where

* (α) is the **learning rate**
* (\frac{\partial J}{\partial β}) is the **slope of cost function** (gradient)
* New value of (β) moves toward minimum

---

# 4. What is Convergence?

Convergence happens when:

[
\text{Change in cost between steps becomes almost zero}
]

For example
If cost was

* Step 1: 520
* Step 2: 300
* Step 3: 150
* Step 4: 78
* Step 5: 74
* Step 6: 73.8
* Step 7: 73.799
* Step 8: 73.79899

The algorithm has nearly stopped improving.
This is called **convergence**.

---

# 5. How to Know Convergence Happened?

We check any of these:

### a. Change in cost is very small

[
|J_{\text{new}} - J_{\text{old}}| < 0.0001
]

### b. Gradients become nearly zero

[
\frac{\partial J}{\partial β_0} \approx 0,\
\frac{\partial J}{\partial β_1} \approx 0
]

### c. Maximum iteration limit is reached

For example
Stop after 3000 iterations.

---

# 6. Convergence Depends on the Learning Rate

### If learning rate is too small

The algorithm moves very slowly.

### If learning rate is too large

The algorithm jumps over the minimum, cost increases instead.

### If learning rate is good

The algorithm steadily reduces cost and reaches the minimum smoothly.

---

# 7. Graphical Understanding

Imagine standing on a hill.
You want to reach the lowest point.
You take steps downward.
If your steps are correctly sized, you reach the bottom.
This bottom is your best fit line.

This process of walking downward until you stop improving is **convergence**.

---

# 8. Summary of the Convergence Algorithm

| Step | Explanation                                       |
| ---- | ------------------------------------------------- |
| 1    | Start with random slope and intercept             |
| 2    | Compute predictions                               |
| 3    | Compute cost                                      |
| 4    | Compute gradient (direction of steepest decrease) |
| 5    | Update slope and intercept                        |
| 6    | Repeat until cost stops decreasing                |
| 7    | Parameters have converged                         |
---
