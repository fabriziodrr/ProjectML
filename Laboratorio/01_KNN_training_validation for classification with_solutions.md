---
jupyter:
  colab:
    provenance:
    - file_id: 1xGzyDaCmGdQCPzGGzOih9vQKyHrY0R6p
      timestamp: 1679065243471
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
<https://scikit-learn.org/stable/datasets/toy_dataset.html#>:\~:text=7.1.6.%20Breast%20cancer%20wisconsin%20(diagnostic)%20dataset%C2%B6
:::

::: {.cell .markdown collapsed="false" id="JqgZbyzPlVsH"}
#Preliminary operations
:::

::: {.cell .code execution_count="24" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":1078,\"status\":\"ok\",\"timestamp\":1773912547709,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="m4joevqGlVsI" outputId="62e13462-bea3-4e57-b840-1211ead663da"}
``` python
from google.colab import drive
drive.mount('/content/drive')
import os
os.chdir('/content/drive/MyDrive/Didattica/ML/Exercises/Exercise01-02_training_validation')

import numpy as np
import matplotlib.pyplot as plt
```

::: {.output .stream .stdout}
    Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount("/content/drive", force_remount=True).
:::
:::

::: {.cell .code execution_count="25" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":35}" executionInfo="{\"elapsed\":12,\"status\":\"ok\",\"timestamp\":1773912547710,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="2POILcJnCnc9" outputId="4cf308ff-823c-454f-c309-d3c8396182b8"}
``` python
import sklearn
sklearn.__version__
```

::: {.output .execute_result execution_count="25"}
``` json
{"type":"string"}
```
:::
:::

::: {.cell .markdown id="Wjl0s4bWnaW9"}
#Dataset

We use the
[load_breast_cancer](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html)
function provided by the [scikit-learn](https://scikit-learn.org)
package.
:::

::: {.cell .code execution_count="26" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":4,\"status\":\"ok\",\"timestamp\":1773912547712,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="f0PCz6XrlVsJ" outputId="b0fde27a-e97a-4e38-a94a-b00074e434c5"}
``` python
from sklearn.datasets import load_breast_cancer

# import the data to use
dataset = load_breast_cancer()

class_names = dataset.target_names
num_classes = len(class_names)

for c, class_name in enumerate(class_names):
  print("Class {} has {} samples".format(class_name, (dataset.target==c).sum()))
print("")
for f, feature_name in enumerate(dataset.feature_names):
  print("Feature {} is '{}'".format(f, feature_name))
```

::: {.output .stream .stdout}
    Class malignant has 212 samples
    Class benign has 357 samples

    Feature 0 is 'mean radius'
    Feature 1 is 'mean texture'
    Feature 2 is 'mean perimeter'
    Feature 3 is 'mean area'
    Feature 4 is 'mean smoothness'
    Feature 5 is 'mean compactness'
    Feature 6 is 'mean concavity'
    Feature 7 is 'mean concave points'
    Feature 8 is 'mean symmetry'
    Feature 9 is 'mean fractal dimension'
    Feature 10 is 'radius error'
    Feature 11 is 'texture error'
    Feature 12 is 'perimeter error'
    Feature 13 is 'area error'
    Feature 14 is 'smoothness error'
    Feature 15 is 'compactness error'
    Feature 16 is 'concavity error'
    Feature 17 is 'concave points error'
    Feature 18 is 'symmetry error'
    Feature 19 is 'fractal dimension error'
    Feature 20 is 'worst radius'
    Feature 21 is 'worst texture'
    Feature 22 is 'worst perimeter'
    Feature 23 is 'worst area'
    Feature 24 is 'worst smoothness'
    Feature 25 is 'worst compactness'
    Feature 26 is 'worst concavity'
    Feature 27 is 'worst concave points'
    Feature 28 is 'worst symmetry'
    Feature 29 is 'worst fractal dimension'
:::
:::

::: {.cell .code execution_count="27" executionInfo="{\"elapsed\":8,\"status\":\"ok\",\"timestamp\":1773912547732,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="ClSBee5qVx46"}
``` python
X = dataset.data
y = dataset.target
```
:::

::: {.cell .markdown id="J0wwn_aMaoya"}
##Let\'s **simulate the private test set**
:::

::: {.cell .code execution_count="28" executionInfo="{\"elapsed\":10,\"status\":\"ok\",\"timestamp\":1773912547747,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="fV5uLlsDatUW"}
``` python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,       y,       random_state=111, test_size=.5)
```
:::

::: {.cell .markdown id="k9hjqxMoawP1"}
From now on, the test set will be used once to compute the performance
of the model.
:::

::: {.cell .markdown id="m4QUMTkIXF3G"}
## Data split into actual training and validation sets
:::

::: {.cell .code execution_count="29" executionInfo="{\"elapsed\":1,\"status\":\"ok\",\"timestamp\":1773912547754,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="bq51hFLc0iTW"}
``` python
X_train, X_val,  y_train, y_val  = train_test_split(X_train, y_train, random_state=222, test_size=.5)
```
:::

::: {.cell .code execution_count="30" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":38,\"status\":\"ok\",\"timestamp\":1773912547797,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="EGbQpi0yamKf" outputId="551a1b18-3730-40c6-b6e6-ef4c18153d2f"}
``` python
print("Training set: {} samples".format(len(X_train)))
print("Validation set: {} samples".format(len(X_val)))
print("Test set: {} samples".format(len(X_test)))
```

::: {.output .stream .stdout}
    Training set: 142 samples
    Validation set: 142 samples
    Test set: 285 samples
:::
:::

::: {.cell .markdown id="0uYyVKx1V0o0"}
##Data normalization

Z-scoring: the standard feature scaling

    mu = X_train.mean(0)
    sig = X_train.std(0)

    X_train -= mu
    X_train /= sig

    X_val -= mu
    X_val /= sig

    X_test -= mu
    X_test /= sig
:::

::: {.cell .markdown id="Ke9qbZCYbLbO"}
We use the
[StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)
class
:::

::: {.cell .code execution_count="31" executionInfo="{\"elapsed\":1,\"status\":\"ok\",\"timestamp\":1773912547808,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="jy0YaUNDZ-4x"}
``` python
from sklearn.preprocessing import StandardScaler as Scaler
```
:::

::: {.cell .markdown id="-eBI2LK5bZGv"}
Alternatively, we use the
[RobustScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html)
class if we suppose that outliers may be in the training data. This
computes robust training data statistics (e.g., median instead of mean).
:::

::: {.cell .code execution_count="32" executionInfo="{\"elapsed\":0,\"status\":\"ok\",\"timestamp\":1773912547809,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="quWIOYmAZkvJ"}
``` python
from sklearn.preprocessing import RobustScaler as Scaler
```
:::

::: {.cell .code execution_count="33" executionInfo="{\"elapsed\":0,\"status\":\"ok\",\"timestamp\":1773912547812,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="Q1e25hbBZuH6"}
``` python
scaler  = Scaler()
X_train = scaler.fit_transform(X_train)   # compute the statistics and use them to scale the training set
X_val   = scaler.transform(X_val)         # do *not* compute statistics, but use the previously computed ones to scale the validation set
X_test  = scaler.transform(X_test)        # do *not* compute statistics, but use the previously computed ones to scale the test set
```
:::

::: {.cell .markdown id="of4hbmH-XNC2"}
#Classifier initialization and training loop We use the [MultiLayer
Perceptron](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html),
however for the purpose of this exercise, any classifier can be used as
a black box. The Scikit-Learn library provides a common interface to
multiple Machine Learning models.
:::

::: {.cell .code execution_count="34" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":6,\"status\":\"ok\",\"timestamp\":1773912547823,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="GgvYv3VSPfi1" outputId="55780808-106d-43b9-8aef-fae99191c8cd"}
``` python
from sklearn.neighbors import KNeighborsClassifier as Classifier
from sklearn.metrics import accuracy_score

#classifier = MLPClassifier(random_state=1, hidden_layer_sizes=10000, batch_size=len(X_train))
classifier = Classifier(n_neighbors=3)

# Training Loop
classifier.fit(X_train, y_train)#, classes=[0, 1])

train_acc = accuracy_score(y_train, classifier.predict(X_train))
valid_acc = accuracy_score(y_val, classifier.predict(X_val))

print("Training accuracy: {:.2f} %".format(train_acc*100))
print("Validation accuracy: {:.2f} %".format(valid_acc*100))
```

::: {.output .stream .stdout}
    Training accuracy: 95.77 %
    Validation accuracy: 93.66 %
:::
:::

::: {.cell .markdown id="BlC5LM4NbatD"}
#Full training at varying of the hyperparameter
:::

::: {.cell .code execution_count="40" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":447}" executionInfo="{\"elapsed\":1618,\"status\":\"ok\",\"timestamp\":1773912705751,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="5tSKAizIbaJ5" outputId="0adb1683-b403-4aec-9916-44503c663da9"}
``` python
from tqdm import tqdm
K = range(1, min(100, len(X_train)))
train_acc_, valid_acc_ = [], []
for k in tqdm(K, desc="Training KNN for k={}".format(k)):
  classifier = Classifier(n_neighbors=k)
  classifier.fit(X_train, y_train)
  train_acc_.append(accuracy_score(y_train, classifier.predict(X_train)))
  valid_acc_.append(accuracy_score(y_val, classifier.predict(X_val)))

k_best = K[np.argmax(valid_acc_)]
valid_acc_best = np.max(valid_acc_)

plt.figure()
plt.plot(K, train_acc_, label="training accuracy")
plt.plot(K, valid_acc_, label="validation accuracy")
plt.plot(K, np.ones((len(K),))*valid_acc_best, ':r', label="best validation accuracy")
plt.legend()
plt.show()
```

::: {.output .stream .stderr}
    Training KNN for k=99: 100%|██████████| 99/99 [00:01<00:00, 84.18it/s]
:::

::: {.output .display_data}
![](0afd4831f4721a4d9d6dbe749452e15e47de9f67.png)
:::
:::

::: {.cell .markdown id="yMzJ26_5cCHE"}
#Binary classifier performance metrics on the test set
:::

::: {.cell .code execution_count="42" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":41,\"status\":\"ok\",\"timestamp\":1773912832117,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="ciyNTfsDJhHN" outputId="ee4e0bb3-2b14-457b-c9ab-e295ade9a4f8"}
``` python
classifier = Classifier(n_neighbors=k_best)
classifier.fit(X_train, y_train)

y_test_predicted = classifier.predict(X_test)
test_acc = accuracy_score(y_test, y_test_predicted)
print("Test accuracy: {:.2f} %".format(test_acc*100))
```

::: {.output .stream .stdout}
    Test accuracy: 95.09 %
:::
:::

::: {.cell .code execution_count="43" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":104,\"status\":\"ok\",\"timestamp\":1773912833703,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="wetz4t8pcZml" outputId="43b7b09c-41ea-40fd-a034-f341214c6472"}
``` python
y_test_predicted_proba = classifier.predict_proba(X_test)

for l, p in zip(y_test_predicted, y_test_predicted_proba):
  print(l, 'with prob.', p)
```

::: {.output .stream .stdout}
    1 with prob. [0.11111111 0.88888889]
    1 with prob. [0. 1.]
    1 with prob. [0.11111111 0.88888889]
    0 with prob. [0.55555556 0.44444444]
    1 with prob. [0. 1.]
    0 with prob. [1. 0.]
    1 with prob. [0.11111111 0.88888889]
    0 with prob. [0.66666667 0.33333333]
    1 with prob. [0. 1.]
    0 with prob. [1. 0.]
    0 with prob. [0.55555556 0.44444444]
    1 with prob. [0.44444444 0.55555556]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    0 with prob. [1. 0.]
    1 with prob. [0.11111111 0.88888889]
    0 with prob. [0.77777778 0.22222222]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    0 with prob. [1. 0.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    0 with prob. [0.55555556 0.44444444]
    1 with prob. [0.11111111 0.88888889]
    0 with prob. [0.88888889 0.11111111]
    0 with prob. [1. 0.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    0 with prob. [1. 0.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    0 with prob. [1. 0.]
    0 with prob. [0.77777778 0.22222222]
    1 with prob. [0.11111111 0.88888889]
    0 with prob. [1. 0.]
    0 with prob. [1. 0.]
    0 with prob. [1. 0.]
    1 with prob. [0. 1.]
    0 with prob. [0.66666667 0.33333333]
    1 with prob. [0. 1.]
    1 with prob. [0.11111111 0.88888889]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    0 with prob. [1. 0.]
    1 with prob. [0.11111111 0.88888889]
    1 with prob. [0.33333333 0.66666667]
    1 with prob. [0. 1.]
    0 with prob. [1. 0.]
    1 with prob. [0. 1.]
    1 with prob. [0.11111111 0.88888889]
    0 with prob. [0.88888889 0.11111111]
    1 with prob. [0.33333333 0.66666667]
    1 with prob. [0.33333333 0.66666667]
    0 with prob. [1. 0.]
    1 with prob. [0. 1.]
    0 with prob. [1. 0.]
    0 with prob. [0.77777778 0.22222222]
    1 with prob. [0. 1.]
    1 with prob. [0.11111111 0.88888889]
    1 with prob. [0. 1.]
    0 with prob. [0.77777778 0.22222222]
    0 with prob. [1. 0.]
    1 with prob. [0.11111111 0.88888889]
    0 with prob. [1. 0.]
    0 with prob. [1. 0.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    0 with prob. [1. 0.]
    1 with prob. [0.33333333 0.66666667]
    1 with prob. [0.22222222 0.77777778]
    0 with prob. [0.55555556 0.44444444]
    0 with prob. [1. 0.]
    1 with prob. [0. 1.]
    1 with prob. [0.22222222 0.77777778]
    1 with prob. [0.22222222 0.77777778]
    1 with prob. [0.22222222 0.77777778]
    0 with prob. [1. 0.]
    1 with prob. [0.44444444 0.55555556]
    1 with prob. [0. 1.]
    0 with prob. [0.66666667 0.33333333]
    0 with prob. [1. 0.]
    0 with prob. [0.66666667 0.33333333]
    1 with prob. [0. 1.]
    0 with prob. [0.88888889 0.11111111]
    0 with prob. [1. 0.]
    1 with prob. [0.11111111 0.88888889]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    0 with prob. [1. 0.]
    0 with prob. [1. 0.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    0 with prob. [1. 0.]
    1 with prob. [0. 1.]
    0 with prob. [0.77777778 0.22222222]
    1 with prob. [0. 1.]
    1 with prob. [0.11111111 0.88888889]
    0 with prob. [1. 0.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0.11111111 0.88888889]
    1 with prob. [0.11111111 0.88888889]
    1 with prob. [0. 1.]
    0 with prob. [1. 0.]
    1 with prob. [0.11111111 0.88888889]
    1 with prob. [0. 1.]
    0 with prob. [0.88888889 0.11111111]
    0 with prob. [1. 0.]
    0 with prob. [1. 0.]
    0 with prob. [1. 0.]
    1 with prob. [0. 1.]
    0 with prob. [1. 0.]
    1 with prob. [0.11111111 0.88888889]
    1 with prob. [0. 1.]
    1 with prob. [0.11111111 0.88888889]
    1 with prob. [0.22222222 0.77777778]
    1 with prob. [0.11111111 0.88888889]
    1 with prob. [0.11111111 0.88888889]
    0 with prob. [0.88888889 0.11111111]
    1 with prob. [0.22222222 0.77777778]
    0 with prob. [1. 0.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    0 with prob. [0.66666667 0.33333333]
    1 with prob. [0.11111111 0.88888889]
    1 with prob. [0.22222222 0.77777778]
    0 with prob. [1. 0.]
    1 with prob. [0. 1.]
    0 with prob. [1. 0.]
    1 with prob. [0. 1.]
    1 with prob. [0.11111111 0.88888889]
    0 with prob. [1. 0.]
    1 with prob. [0.11111111 0.88888889]
    1 with prob. [0. 1.]
    0 with prob. [1. 0.]
    0 with prob. [0.55555556 0.44444444]
    0 with prob. [0.77777778 0.22222222]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    0 with prob. [0.88888889 0.11111111]
    1 with prob. [0. 1.]
    1 with prob. [0.33333333 0.66666667]
    1 with prob. [0.11111111 0.88888889]
    0 with prob. [0.55555556 0.44444444]
    1 with prob. [0.33333333 0.66666667]
    1 with prob. [0. 1.]
    1 with prob. [0.33333333 0.66666667]
    0 with prob. [1. 0.]
    1 with prob. [0.22222222 0.77777778]
    1 with prob. [0.11111111 0.88888889]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0.33333333 0.66666667]
    0 with prob. [1. 0.]
    0 with prob. [1. 0.]
    0 with prob. [0.77777778 0.22222222]
    0 with prob. [1. 0.]
    1 with prob. [0.22222222 0.77777778]
    1 with prob. [0. 1.]
    1 with prob. [0.22222222 0.77777778]
    1 with prob. [0.11111111 0.88888889]
    1 with prob. [0.11111111 0.88888889]
    1 with prob. [0. 1.]
    0 with prob. [0.88888889 0.11111111]
    0 with prob. [0.66666667 0.33333333]
    1 with prob. [0.22222222 0.77777778]
    0 with prob. [1. 0.]
    0 with prob. [0.88888889 0.11111111]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    0 with prob. [1. 0.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    0 with prob. [1. 0.]
    1 with prob. [0. 1.]
    1 with prob. [0.11111111 0.88888889]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0.11111111 0.88888889]
    0 with prob. [1. 0.]
    1 with prob. [0.11111111 0.88888889]
    0 with prob. [1. 0.]
    1 with prob. [0.44444444 0.55555556]
    0 with prob. [1. 0.]
    0 with prob. [0.88888889 0.11111111]
    0 with prob. [0.88888889 0.11111111]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0.11111111 0.88888889]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0.11111111 0.88888889]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    0 with prob. [1. 0.]
    0 with prob. [1. 0.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0.22222222 0.77777778]
    0 with prob. [1. 0.]
    0 with prob. [1. 0.]
    1 with prob. [0.33333333 0.66666667]
    0 with prob. [0.66666667 0.33333333]
    0 with prob. [0.66666667 0.33333333]
    1 with prob. [0. 1.]
    1 with prob. [0.11111111 0.88888889]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    0 with prob. [0.88888889 0.11111111]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0.22222222 0.77777778]
    1 with prob. [0.22222222 0.77777778]
    0 with prob. [1. 0.]
    0 with prob. [1. 0.]
    1 with prob. [0.44444444 0.55555556]
    0 with prob. [1. 0.]
    1 with prob. [0.11111111 0.88888889]
    0 with prob. [1. 0.]
    1 with prob. [0. 1.]
    0 with prob. [1. 0.]
    1 with prob. [0. 1.]
    1 with prob. [0.33333333 0.66666667]
    1 with prob. [0.11111111 0.88888889]
    1 with prob. [0.33333333 0.66666667]
    0 with prob. [1. 0.]
    1 with prob. [0.11111111 0.88888889]
    1 with prob. [0. 1.]
    0 with prob. [0.66666667 0.33333333]
    1 with prob. [0. 1.]
    0 with prob. [1. 0.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    0 with prob. [0.88888889 0.11111111]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0.22222222 0.77777778]
    1 with prob. [0. 1.]
    1 with prob. [0.11111111 0.88888889]
    1 with prob. [0. 1.]
    1 with prob. [0.33333333 0.66666667]
    0 with prob. [1. 0.]
    0 with prob. [1. 0.]
    1 with prob. [0. 1.]
    0 with prob. [1. 0.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    0 with prob. [1. 0.]
    1 with prob. [0. 1.]
    0 with prob. [1. 0.]
    1 with prob. [0. 1.]
    1 with prob. [0.11111111 0.88888889]
    1 with prob. [0.11111111 0.88888889]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    0 with prob. [0.88888889 0.11111111]
    0 with prob. [1. 0.]
    0 with prob. [0.88888889 0.11111111]
    1 with prob. [0. 1.]
    0 with prob. [1. 0.]
    1 with prob. [0. 1.]
    1 with prob. [0. 1.]
    1 with prob. [0.11111111 0.88888889]
:::
:::

::: {.cell .markdown id="FJrPI9d4bxZf"}
##Compute the Precision, Recall and F1-score
:::

::: {.cell .code execution_count="80" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":14,\"status\":\"ok\",\"timestamp\":1773907807803,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="kMKdgcsGb7l-" outputId="483c34a8-3bd6-4102-afde-6cf7e89e3ba2"}
``` python
# Write here the code
from sklearn.metrics import precision_recall_fscore_support
Precision, Recall, Fscore, Support = precision_recall_fscore_support(y_test, y_test_predicted)
print(Precision[1], Recall[1], Fscore[1], Support[1])
```

::: {.output .stream .stdout}
    0.9056603773584906 0.9113924050632911 0.9085173501577287 316
:::
:::

::: {.cell .code execution_count="81" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":22,\"status\":\"ok\",\"timestamp\":1773907807827,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="jo7D9KzSbPSu" outputId="08784186-8b1e-46b8-8e89-4875c00f8ca4"}
``` python
TP = np.logical_and(y_test==1, y_test_predicted==1).sum()
TN = np.logical_and(y_test==0, y_test_predicted==0).sum()
FP = np.logical_and(y_test==0, y_test_predicted==1).sum()
FN = np.logical_and(y_test==1, y_test_predicted==0).sum()

Precision_ = TP/(TP+FP)
Recall_ = TP/(TP+FN)
Fscore_ = 2*Precision_ * Recall_/(Precision_ + Recall_)
Support_ = (y_test==1).sum()
print(Precision_, Recall_, Fscore_, Support_)
```

::: {.output .stream .stdout}
    0.9056603773584906 0.9113924050632911 0.9085173501577287 316
:::
:::

::: {.cell .markdown id="d3e4qGaAbNWc"}
##Compute the ROC curve and the AUROC
:::

::: {.cell .code execution_count="82" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":452}" executionInfo="{\"elapsed\":248,\"status\":\"ok\",\"timestamp\":1773907808076,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="lPJnfFiSbTwV" outputId="92af30e4-75bb-4cd0-ba16-9ac7bc65c93e"}
``` python
# Write here the code
from sklearn.metrics import roc_curve, roc_auc_score
fpr, tpr, tau = roc_curve(y_test, y_test_predicted_proba[:,1])
AUC = roc_auc_score(y_test, y_test_predicted_proba[:,1])
plt.plot(fpr, tpr)
plt.scatter(FP/(TN+FP), TP/(TP+FN), c='r')
plt.legend(['ROC', 'operating point'])
plt.title(AUC)
plt.show()
```

::: {.output .display_data}
![](901f49fa448c956cd565d7d3cbe48f10af96d03e.png)
:::
:::

::: {.cell .code execution_count="83" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":141}" executionInfo="{\"elapsed\":33,\"status\":\"error\",\"timestamp\":1773907808110,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="gnKDHoaKv6QP" outputId="d4154c3e-68e8-466c-c558-00954defa18e"}
``` python
TAU_[:3]
```

::: {.output .error ename="NameError" evalue="name 'TAU_' is not defined"}
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    /tmp/ipykernel_1554/551476359.py in <cell line: 0>()
    ----> 1 TAU_[:3]

    NameError: name 'TAU_' is not defined
:::
:::

::: {.cell .code executionInfo="{\"elapsed\":48,\"status\":\"aborted\",\"timestamp\":1773907808154,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="-pnjFvvOwAEW"}
``` python
y_test_predicted_proba_neg
```
:::

::: {.cell .code executionInfo="{\"elapsed\":66,\"status\":\"aborted\",\"timestamp\":1773907808173,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="i5DoWurLa50S"}
``` python
y_test_predicted_proba_sorted = np.sort(y_test_predicted_proba[:, 1])
TAU_ = (y_test_predicted_proba_sorted[1:] + y_test_predicted_proba_sorted[:-1])/2
TAU_ = np.concatenate((-np.zeros((1,))-.0000001, TAU_, .0000001+np.ones((1,))))

y_test_predicted_proba_pos = y_test_predicted_proba[y_test==1, 1]
y_test_predicted_proba_neg = y_test_predicted_proba[y_test==0, 1]
fpr_ = [(y_test_predicted_proba_neg >= tau_).mean() for tau_ in TAU_]
tpr_ = [(y_test_predicted_proba_pos >= tau_).mean() for tau_ in TAU_]
auc_ = sklearn.metrics.auc(fpr_, tpr_)

plt.plot(fpr_, tpr_)
plt.scatter(FP/(TN+FP), TP/(TP+FN), c='r')
plt.legend(['ROC', 'operating point'])
plt.title(auc_)
plt.show()
```
:::

::: {.cell .markdown id="SUVkHd_EqSxW"}
#Validation protocols
:::

::: {.cell .markdown id="bbkN8sl5qV_G"}
##Random hold-out At each iteration, a fixed portion of random samples
is hold out for validation while the remaining ones are used for
training. This function returns the indexes to extract from the whole
dataset array the training and validation subsets.
:::

::: {.cell .code executionInfo="{\"elapsed\":70,\"status\":\"aborted\",\"timestamp\":1773907808177,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="OB2iNqtwlVsL"}
``` python
def random_split(N, p=.2, seed=1234):
  assert 0 < p < 1, "p must be in ]0,1["

  np.random.seed(seed)
#  i = np.random.randint(low=0, high=K, size=N)  # modify this line to avoid train/val overlapping
  i = np.random.permutation(N)

  i_val = i[:int(N * p)]
  i_train = i[int(N * p):]
  return i_train, i_val

print(random_split(10, .2))
```
:::

::: {.cell .markdown id="u0akoe24yaP1"}
Perform the random hold-out validation
:::

::: {.cell .markdown collapsed="false" id="lH-MG8e8lVsM"}
##Exhaustive cross-validation The whole dataset is partitioned into
folds. At each iteration, in turns one fold is used for validation while
the remaining ones are used for training.
:::

::: {.cell .code executionInfo="{\"elapsed\":71,\"status\":\"aborted\",\"timestamp\":1773907808178,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="-gtNAb18rGR9"}
``` python
from IPython.display import Image
Image(url='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/LOOCV.gif/800px-LOOCV.gif')
```
:::

::: {.cell .markdown id="MOJXR1nNyjJJ"}
Perform the cross-validation manually or using the [sklearn
functions](https://scikit-learn.org/stable/modules/cross_validation.html)
:::

::: {.cell .code executionInfo="{\"elapsed\":72,\"status\":\"aborted\",\"timestamp\":1773907808181,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="6mjTG6MEwR9O"}
``` python
def exhaustive_split(N, K, seed=1234, plot_k_val=False):
  if K > N:
      raise ValueError("K must be less or equal to N")

  np.random.seed(seed)
  k_val = np.random.randint(low=0, high=K, size=N)

  if plot_k_val:
      plt.scatter(np.arange(0, N), k_val)
      plt.xlabel('samples')
      plt.xticks(np.arange(0, N))
      plt.ylabel("fold")
      plt.yticks(np.arange(0, K))
      plt.show()

  M_train = []
  M_val = []
  for k in range(K):
      m_val   = (k_val == k)
      m_train = (k_val != k)

      M_train.append(m_train)
      M_val.append(m_val)

  return M_train, M_val

M_train, M_val = exhaustive_split(10, 10, 1234, True)
for m_train, m_val in zip(M_train, M_val):
  print("\n- train", m_train, m_train.sum(), "samples")
  print("- val  ", m_val, m_val.sum(), "samples")
```
:::

::: {.cell .markdown id="q_PjACNhwWnN"}
Perform cross-validation
:::

::: {.cell .code executionInfo="{\"elapsed\":27,\"status\":\"aborted\",\"timestamp\":1773907808181,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="PM3r7OZGwYlk"}
``` python
n_neighbors = 3
N = len(X)
K = 10

M_train, M_val = exhaustive_split(N, K, seed=0)

print("Starting %d-fold exhaustive cross-validation:" % K)
k, Acc = 0, []
for m_train, m_val in zip(M_train, M_val):
  X_train = X[m_train]
  y_train = y[m_train]
  X_val = X[m_val]
  y_val = y[m_val]

  print("fold", k)
  classifier = MLPClassifier(random_state=1, hidden_layer_sizes=hidden_layer_sizes,
                           batch_size=len(X_train), early_stopping=True)
  classifier.fit(X_train, y_train)
  Acc.append(classifier.score(X_val, y_val))
  k += 1

print("\nMean accuracy and standard deviation: {:.4f} - {:.4f}".format(np.mean(Acc), np.std(Acc)))
```
:::

::: {.cell .markdown collapsed="false" id="A5PdIO4YlVsM"}
###Leave-one-out When the dataset is tiny, in turns one sample is
hold-out at each iteration, or equivalently the number of folds equals
the number of samples.
:::

::: {.cell .code executionInfo="{\"elapsed\":7,\"status\":\"aborted\",\"timestamp\":1773907808182,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="8b6TRfJHxOKL"}
``` python
# Re-write the exhaustive_split function in order to perform both cross-validation and leave-one-out
def exhaustive_split(N, K, seed=1234, plot_k_val=False):
  if K > N:
      raise ValueError("K must be less or equal to N")

  np.random.seed(seed)
  if K < N:
    k_val = np.random.randint(low=0, high=K, size=N)
  else:
    k_val = np.arange(N)

  if plot_k_val:
      plt.scatter(np.arange(0, N), k_val)
      plt.xlabel('samples')
      plt.xticks(np.arange(0, N))
      plt.ylabel("fold")
      plt.yticks(np.arange(0, K))
      plt.show()

  M_train = []
  M_val = []
  for k in range(K):
      m_val   = (k_val == k)
      m_train = (k_val != k)

      M_train.append(m_train)
      M_val.append(m_val)

  return M_train, M_val

M_train, M_val = exhaustive_split(10, 10, 1234, True)
for m_train, m_val in zip(M_train, M_val):
  print("\n- train", m_train, m_train.sum(), "samples")
  print("- val  ", m_val, m_val.sum(), "samples")
```
:::

::: {.cell .markdown id="STc5FsKGyxKG"}
Perform the leave-one-out cross-validation
:::

::: {.cell .code executionInfo="{\"elapsed\":2,\"status\":\"aborted\",\"timestamp\":1773907808182,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="7u0C71EaxS0T"}
``` python
n_neighbors = 3
N = len(X)
K = N

M_train, M_val = exhaustive_split(N, K, seed=0)

print("Starting %d-fold exhaustive cross-validation:" % K)
k, Acc = 0, []
for m_train, m_val in zip(M_train, M_val):
  X_train = X[m_train]
  y_train = y[m_train]
  X_val = X[m_val]
  y_val = y[m_val]

  print("fold", k)
  classifier = MLPClassifier(random_state=1, hidden_layer_sizes=hidden_layer_sizes,
                           batch_size=len(X_train), early_stopping=True)
  classifier.fit(X_train, y_train)
  Acc.append(classifier.score(X_val, y_val))
  k += 1

print("\nMean accuracy and standard deviation: {:.4f} - {:.4f}".format(np.mean(Acc), np.std(Acc)))
```
:::

::: {.cell .markdown id="B4HvIMJgszKD"}
##Stratified sampling cross-validation Random partitioning of the
dataset does not assure to preserve the original class proportions. To
preserve this, we use the
[StratifiedShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html)
function.
:::

::: {.cell .markdown id="BdXnllhIuYAW"}
We have an unbalanced dataset
:::

::: {.cell .code executionInfo="{\"elapsed\":16046,\"status\":\"aborted\",\"timestamp\":1773907808183,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="Yza5bpySxbm_"}
``` python
for c, class_name in enumerate(class_names):
    print("- class {} samples:\t\t{}".format(class_name, (y==c).sum()))
```
:::

::: {.cell .markdown id="Q_Db-RuBzGSF"}
Use the StratifiedShuffleSplit to create training and validation folds
having the same class proportions
:::

::: {.cell .code executionInfo="{\"elapsed\":16045,\"status\":\"aborted\",\"timestamp\":1773907808183,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="zg49C7yzxdKu"}
``` python
from sklearn.model_selection import StratifiedShuffleSplit
sss = StratifiedShuffleSplit(n_splits=10, test_size=0.2, random_state=0)

for k, (train_index, val_index) in enumerate(sss.split(X, y)):
    print("\nFold", k)
    for c, class_name in enumerate(class_names):
        print("- class {} samples (train, val):\t\t{} , {}".format(class_name, (y[train_index]==c).sum(), (y[val_index]==c).sum()))
```
:::

::: {.cell .code executionInfo="{\"elapsed\":16045,\"status\":\"aborted\",\"timestamp\":1773907808184,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="_QQv2Kioxiqq"}
``` python
### Perform a stratified sampling validation on the unbalanced (X_, y_) dataset
n_neighbors = 3
N = len(X)
K = 10
p = 1/K

print("Starting %d-fold cross-validation with random splits:" % K)
Acc = []
for k, (i_train, i_val) in enumerate(sss.split(X, y)):

  X_train = X[i_train]
  y_train = y[i_train]
  X_val = X[i_val]
  y_val = y[i_val]

  print("fold", k)
  classifier = MLPClassifier(random_state=1, hidden_layer_sizes=hidden_layer_sizes,
                           batch_size=len(X_train), early_stopping=True)
  classifier.fit(X_train, y_train)
  Acc.append(classifier.score(X_val, y_val))

print("\nMean accuracy and standard deviation: {:.4f} - {:.4f}".format(np.mean(Acc), np.std(Acc)))
```
:::
