---
jupyter:
  colab:
    provenance:
    - file_id: 1xGzyDaCmGdQCPzGGzOih9vQKyHrY0R6p
      timestamp: 1679065243471
    toc_visible: true
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.10.9
  nbformat: 4
  nbformat_minor: 0
---

::: {.cell .markdown id="91L6KMksETEV"}
# Exercise 2: Repeat the analysis for a regression task

Repeat the analysis using the [Diabetes
dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html)
:::

::: {.cell .markdown id="MnOB1yx21q8c"}
#The (K-) Nearest Neighbor regressor

Study and use the [kNN
regressor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html)

What is the main difference with respect to the kNN classifier?
:::

::: {.cell .markdown id="zdb5L1EU1wBm"}
#Validation Use the [Mean Squared
Error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html)
to measure the performance of the regressor.

Use the
[Cross-Validation](https://scikit-learn.org/stable/modules/cross_validation.html)
to select the hyper-parameter vaule.
:::
