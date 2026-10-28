# BIT 4131 – Statistical Computing and Reporting  
## Theoretical Explanations & Mathematical Formulations (All Topics)

---

### 1. Measures of Central Tendency and Dispersion
**Theory**: Central tendency summarises the “centre” of data (mean, median, mode). Dispersion measures spread (variance, SD, IQR, range).  
**Formulation**:  
- Mean: \(\bar{x} = \frac{1}{n}\sum x_i\)  
- Variance: \(s^2 = \frac{1}{n-1}\sum (x_i-\bar{x})^2\)  
- Standard deviation: \(s = \sqrt{s^2}\)  
- IQR = \(Q_3 - Q_1\)

### 2. Probability and Conditional Probability
**Theory**: Probability quantifies uncertainty. Conditional probability \(P(A|B) = P(A\cap B)/P(B)\).  
**Formulation**: Bayes’ theorem \(P(A|B) = \frac{P(B|A)P(A)}{P(B)}\).

### 3. Probability Distributions
**Theory**: Discrete (Binomial, Poisson) and continuous (Normal, Exponential) distributions describe random variables.  
**Formulation**: Normal pdf \(f(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}\).

### 4. Sampling Distributions and Central Limit Theorem
**Theory**: The sampling distribution of the sample mean approaches Normal as \(n\) grows, regardless of the population distribution (CLT).  
**Formulation**: \(\bar{X} \sim N(\mu, \sigma^2/n)\) for large \(n\).

### 5. Confidence Intervals
**Theory**: A range that contains the true parameter with a stated confidence level.  
**Formulation**: \(\bar{x} \pm z_{\alpha/2}\frac{s}{\sqrt{n}}\) (known σ or large n).

### 6. Hypothesis Testing
**Theory**: Formal procedure to test claims about population parameters.  
**Formulation**: Test statistic \(z = \frac{\bar{x}-\mu_0}{s/\sqrt{n}}\); reject \(H_0\) if p-value < α.

### 7. Correlation and Covariance
**Theory**: Covariance measures joint variability; correlation standardises it to [-1,1].  
**Formulation**: \(\text{Corr}(X,Y) = \frac{\text{Cov}(X,Y)}{s_X s_Y}\).

### 8. Linear Regression and Least Squares
**Theory**: Models linear relationship \(Y = \beta_0 + \beta_1 X + \varepsilon\).  
**Formulation**: \(\hat{\beta} = (X^TX)^{-1}X^TY\).

### 9. Matrix Algebra in Statistics
**Theory**: Matrices underpin multivariate methods, regression, and PCA.  
**Formulation**: Inverse, determinant, solution of \(Ax=b\).

### 10. Eigenvalues, Eigenvectors and PCA
**Theory**: PCA finds orthogonal directions of maximum variance.  
**Formulation**: \(Av = \lambda v\); principal components ordered by eigenvalues.

### 11. Numerical Optimization
**Theory**: Finding parameter values that minimise/maximise an objective (e.g., likelihood, least squares).  
**Formulation**: \(\hat{\theta} = \arg\min_\theta f(\theta)\).

### 12. Random Numbers and Monte Carlo Methods
**Theory**: Approximate expectations or integrals by random sampling.  
**Formulation**: \(\mathbb{E}[g(X)] \approx \frac{1}{N}\sum g(X_i)\).

### 13. Time-series Analysis
**Theory**: Data ordered in time; decompose into trend, seasonality, residual.  
**Formulation**: \(Y_t = T_t + S_t + R_t\).

### 14. Statistical Data Visualization
**Theory**: Visual summaries reveal patterns, outliers, relationships.  
Common plots: histogram, boxplot, scatter, line, density.

### 15. Data Transformation and Normalization
**Theory**: Transformations improve normality, stabilise variance, or put variables on comparable scales.  
**Formulation**: z-score \(z = (x-\bar{x})/s\); min-max scaling.

### 16. ANOVA and Experimental Design
**Theory**: Tests equality of means across groups.  
**Formulation**: \(F = \frac{\text{MSB}}{\text{MSW}}\).

### 17. Chi-square and Categorical Data Analysis
**Theory**: Tests independence or goodness-of-fit for categorical variables.  
**Formulation**: \(\chi^2 = \sum\frac{(O-E)^2}{E}\).

### 18. Logistic Regression
**Theory**: Models binary outcome via logit link.  
**Formulation**: \(\log\frac{p}{1-p} = \beta_0 + \beta_1 x\).

### 19. Non-parametric Statistical Methods
**Theory**: Rank-based tests that do not assume normality (Wilcoxon, Kruskal-Wallis, Spearman).  

### 20. Bootstrap and Resampling Methods
**Theory**: Estimate sampling distribution by resampling with replacement.  
**Formulation**: Bootstrap SE and percentile CI.

### 21. Multivariate Statistical Analysis
**Theory**: Techniques that handle multiple response variables simultaneously (MANOVA, clustering, factor analysis).  

### 22. Missing-data Analysis and Imputation
**Theory**: Mechanisms (MCAR, MAR, MNAR); single/multiple imputation.  

### 23. Statistical Reporting and Reproducible Analysis
**Theory**: Combine code, results, and narrative in a single reproducible document (Jupyter / R Markdown).

---

*Use the Python scripts in `python_codes/` for complete worked examples, dataset analysis, output and interpretation.*
