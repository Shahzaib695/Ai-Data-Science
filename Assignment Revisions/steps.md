# Your EDA roadmap

## 0. Load and understand the dataset

First question:

> **What data did I receive?**

Check:

```python
df.shape
df.head()
df.info()
df.columns
```

You want to know:

* How many rows?
* How many columns?
* What does each row represent?
* What are the data types?
* Which columns are numerical/categorical?

---

# 1. Missing values

Question:

> **What information is missing?**

```python
df.isnull().sum()
```

Also calculate percentages when useful:

```python
df.isnull().mean() * 100
```

### What do I do with missing values?

**Don't automatically fill them.**

First ask:

> Why is this missing?

Possible approaches:

* Numerical → median/mean **if appropriate**
* Categorical → mode or `"Unknown"` **if appropriate**
* Large amount missing → possibly drop the column
* Missingness has meaning → preserve it
* Some rows may be impossible to use → potentially drop rows

You make the decision based on the data.

---

# 2. Duplicates

Question:

> **Are some observations repeated?**

```python
df.duplicated().sum()
```

If duplicates exist, investigate them.

Exact duplicates can usually be removed:

```python
df = df.drop_duplicates()
```

But don't assume two rows with the same person/name are duplicates. They might represent different observations.

---

# 3. Numerical variables

Now ask:

> **What does the distribution of my numerical data look like?**

Start with:

```python
df.describe()
```

Look for:

* strange minimums
* strange maximums
* huge standard deviations
* suspicious values
* skewness

---

# 4. Histograms — "How is this numerical variable distributed?"

Use a **histogram** when you want to see the distribution of one numerical variable.

For example:

```python
sns.histplot(df['Age'], kde=True)
```

It answers:

> Are most values around the middle?
> Is the distribution skewed?
> Are there multiple groups?
> Are there extreme values?

### Mental rule

**Numerical distribution → histogram**

---

# 5. Boxplot — "Are there potential outliers?"

Use:

```python
sns.boxplot(x=df['Age'])
```

A boxplot gives you:

```text
        lower whisker
             |
     ┌─────────────┐
-----|     │       |----- 
     └─────────────┘
       Q1  median Q3
```

The important parts are:

* Q1 = 25th percentile
* Median = 50th percentile
* Q3 = 75th percentile

And:

```text
IQR = Q3 - Q1
```

Potential outlier boundaries:

```text
Lower = Q1 - 1.5 × IQR
Upper = Q3 + 1.5 × IQR
```

Anything outside those boundaries is a **potential outlier**.

### Very important:

**Outlier ≠ bad data.**

Suppose you're analyzing salaries:

```text
50k
55k
60k
65k
500k
```

500k is an outlier.

But it might be completely legitimate.

So you **investigate** an outlier before deleting it.

---

# 6. What do I actually do with outliers?

Ask:

### A. Is it impossible?

Example:

```text
Age = -12
Age = 250
```

That's bad data.

→ Correct it if you know the correct value, otherwise make it missing (`NaN`) or exclude it depending on context.

### B. Is it possible but unusual?

Example:

```text
Age = 92
```

That's unusual compared with your dataset but perfectly possible.

→ **Keep it.**

### C. Is it a measurement/data-entry error?

Example:

```text
Salary = 999999999
```

when everyone else is around 50k.

→ Investigate and potentially correct/remove.

### D. Is it legitimate?

Example:

```text
Fare = $500
```

on Titanic.

Could be legitimate.

→ Keep it.

**Never use "IQR says outlier → delete it" as your rule.**

---

# 7. Categorical variables

Now ask:

> **What categories exist and how common are they?**

Use:

```python
df['Sex'].value_counts()
```

or:

```python
df['Pclass'].value_counts()
```

### Bar chart

Use a **bar chart** for categorical counts.

```python
sns.countplot(data=df, x='Sex')
```

Mental rule:

**Categorical → value_counts / bar chart**

---

# 8. Relationships between two variables

Now EDA gets interesting.

Ask:

> **Does X appear to be related to Y?**

### Numerical + numerical

Use a **scatter plot**.

Example:

> Age vs Fare

```python
sns.scatterplot(data=df, x='Age', y='Fare')
```

Mental rule:

**Numerical + numerical → scatter plot**

You're looking for:

* positive relationship
* negative relationship
* no obvious relationship
* clusters
* outliers

---

### Categorical + numerical

Use a **boxplot**.

Example:

> Fare across passenger classes

```python
sns.boxplot(data=df, x='Pclass', y='Fare')
```

Mental rule:

**Category + numerical → boxplot**

You can compare distributions between groups.

---

### Categorical + categorical

Use a **countplot**, often with `hue`.

Example:

> Survival by sex

```python
sns.countplot(data=df, x='Sex', hue='Survived')
```

Mental rule:

**Category + category → countplot**

---

# 9. Correlation

When you have numerical variables:

```python
df.corr(numeric_only=True)
```

This tells you how strongly numerical variables move together **linearly**.

Typical interpretation:

```text
+1  → strong positive relationship
 0  → little/no linear relationship
-1  → strong negative relationship
```

You can visualize it with a **heatmap**:

```python
sns.heatmap(df.corr(numeric_only=True), annot=True)
```

Mental rule:

**Many numerical variables → correlation matrix / heatmap**

But remember:

> **Correlation does not prove causation.**

---

# 10. Multivariate analysis

Now combine multiple variables.

For Titanic, for example, you might ask:

> Does survival differ by **sex AND passenger class**?

That's where `hue`, grouping, pivot tables, etc. become useful.

This is where you stop merely describing columns and start **asking questions about the dataset**.

---

# Your plot cheat sheet

Save this mentally:

| Question                                    | Tool/Plot               |
| ------------------------------------------- | ----------------------- |
| What does one numerical variable look like? | **Histogram**           |
| Are there potential numerical outliers?     | **Boxplot**             |
| How many of each category?                  | **Bar/countplot**       |
| Numerical vs numerical?                     | **Scatterplot**         |
| Category vs numerical?                      | **Boxplot**             |
| Category vs category?                       | **Countplot + hue**     |
| How do many numerical variables relate?     | **Correlation heatmap** |
| How does something change over time?        | **Line plot**           |

You don't need 20 different plots. Those cover a huge amount of practical EDA.

---

# And your IQR cheat sheet

Suppose:

```python
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
```

Then:

```text
IQR = Q3 - Q1

Lower boundary = Q1 - 1.5 × IQR
Upper boundary = Q3 + 1.5 × IQR
```

Then identify:

```python
outliers = df[
    (df['Age'] < lower_boundary) |
    (df['Age'] > upper_boundary)
]
```

But **don't delete them immediately**.

Your thought process should be:

> IQR identified this → why is it an outlier? → is it impossible, erroneous, or legitimately unusual? → decide.

That's actual EDA.

---

# The most important thing for you

Don't turn this into another course.

For every column, train yourself to ask:

**1. What type of variable is this?**

**2. What question am I trying to answer?**

**3. What tool/plot answers that question?**

**4. What did I discover?**

**5. What action, if any, does that discovery justify?**

That's your EDA loop.

And I want you to **write down your findings**, not just run commands.

For example:

> "`Age` has missing values. Its distribution is right/left skewed. The boxplot shows several potential outliers, but they are within a plausible human-age range, so I will not remove them."

That sentence demonstrates much more EDA ability than knowing 50 Seaborn functions.

### For Titanic, start now.

**Step 1 only:** load `train.csv` and inspect `shape`, `head()`, and `info()`.

Then **you tell me what you notice before I tell you what to do next.**

This time, I'm going to deliberately resist doing the thinking for you. That's how we'll find out whether your EDA grip is actually improving.