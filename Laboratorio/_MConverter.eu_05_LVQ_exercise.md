---
jupyter:
  accelerator: GPU
  colab:
    provenance:
    - file_id: "https://github.com/saeedmehrang/Tensorflow_Keras/blob/master/Predict_MPG_of_Cars_Regression_Fully_Connected_Net.ipynb"
      timestamp: 1648621248175
  kernelspec:
    display_name: Python 3
    name: python3
  nbformat: 4
  nbformat_minor: 0
---

:::: {.cell .code execution_count="2" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":2195,\"status\":\"ok\",\"timestamp\":1743567765159,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="AFENaVq92EhW" outputId="b73cebb5-fb75-4937-d2b3-5c8e7c8cc3b8"}
``` python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from google.colab import drive
drive.mount('/content/drive')

import os
os.chdir('/content/drive/MyDrive/Didattica/ML/Exercises/Exercise08_LVQ')
!ls
```

::: {.output .stream .stdout}
    Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount("/content/drive", force_remount=True).
    auto-mpg.data	    LVQ_supervised.ipynb    test.xlsx
    LVQ_exercise.ipynb  LVQ_unsupervised.ipynb  train.xlsx
:::
::::

::: {.cell .markdown id="O2hjwtIFtK_4"}
# Dataset n.1: randomly generated
:::

::: {.cell .code execution_count="3" executionInfo="{\"elapsed\":8,\"status\":\"ok\",\"timestamp\":1743567765309,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="fEtrRG-q2Gus"}
``` python
def plot_samples(Samples, sample_classes=None):
    sns.scatterplot(
        x=Samples[:, 0],
        y=Samples[:, 1],
        alpha=1.0,
        edgecolor="black",
        hue=sample_classes,
    )
    plt.axis('square')
    plt.grid()


def draw_samples(mu, sig, N=100):
    if isinstance(sig[0], list):
        cov = np.array(sig)
    else:
        cov = np.diag(sig)
    Samples = np.random.multivariate_normal(mu, cov, N)
    return Samples
```
:::

:::: {.cell .code execution_count="4" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":430}" executionInfo="{\"elapsed\":352,\"status\":\"ok\",\"timestamp\":1743567769193,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="_uQuOrmX2aV2" outputId="081c42a4-89c5-4ddd-f419-5fc03805d4bc"}
``` python
# Esempio di campioni
plot_samples(draw_samples([10, 0], [5, 5], 100))
```

::: {.output .display_data}
![](17270a555dd4c19cef2c2d99aa5629b406ab6612.png)
:::
::::

:::: {.cell .code execution_count="5" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":433}" executionInfo="{\"elapsed\":431,\"status\":\"ok\",\"timestamp\":1743567772061,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="CGffZgl92YoC" outputId="9224f75c-b885-4cea-affb-2d488a8b38ae"}
``` python
train_2D_rand = np.concatenate([
  draw_samples([-10,  0], [ 3,  3]),
  draw_samples([ 10,-10], [ 2, 10]),
  draw_samples([ 10,  0], [10,  2]),
  ])

train_2D_rand_classes = np.concatenate([
        np.zeros((100, )),
        np.ones((100, )),
    2 * np.ones((100, )),
    ]).astype('int')

plot_samples(train_2D_rand, train_2D_rand_classes)
```

::: {.output .display_data}
![](7074c1993a40b24840b208988fa2b8adf8c1c74e.png)
:::
::::

::: {.cell .markdown id="BbNgFK0stP2T"}
# Dataset n.2: 2D real data
:::

:::: {.cell .code execution_count="7" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":206}" executionInfo="{\"elapsed\":124,\"status\":\"ok\",\"timestamp\":1743567797853,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="hqMGqLARt9P7" outputId="1cb591a8-5ade-4b6f-8ecd-d172b0c1bf2e"}
``` python
train_2D = pd.read_excel('train.xlsx')
test_2D = pd.read_excel('test.xlsx')

train_2D.head()
```

::: {.output .execute_result execution_count="7"}
``` json
{"summary":"{\n  \"name\": \"train_2D\",\n  \"rows\": 500,\n  \"fields\": [\n    {\n      \"column\": \"Height\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 9.961215570602622,\n        \"min\": 143.84124642015303,\n        \"max\": 199.69828988011193,\n        \"num_unique_values\": 500,\n        \"samples\": [\n          163.4259358472361,\n          160.90184435183662,\n          154.16463048792096\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Weight\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 14.808193724245893,\n        \"min\": 40.62413804392293,\n        \"max\": 111.56313735764623,\n        \"num_unique_values\": 500,\n        \"samples\": [\n          62.579847983745964,\n          66.06833823299691,\n          40.94417416497896\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Gender\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Male\",\n          \"Female\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe","variable_name":"train_2D"}
```
:::
::::

::: {.cell .markdown id="Q9yl7cSTuEed"}
\#Dataset n.3: ND real data
:::

:::: {.cell .code execution_count="8" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":243}" executionInfo="{\"elapsed\":1004,\"status\":\"ok\",\"timestamp\":1743567858301,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="MUOAaMdJvbh_" outputId="41011571-76a4-4821-9f3a-ced243359594"}
``` python
column_names = ['MPG','Cylinders','Displacement','Horsepower','Weight',
                'Acceleration', 'Model Year', 'Origin']
train_ND = pd.read_csv('auto-mpg.data', names=column_names,
                       na_values = "?", comment='\t',
                       sep=" ", skipinitialspace=True)

train_ND.head()
```

::: {.output .execute_result execution_count="8"}
``` json
{"summary":"{\n  \"name\": \"train_ND\",\n  \"rows\": 398,\n  \"fields\": [\n    {\n      \"column\": \"MPG\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 7.815984312565782,\n        \"min\": 9.0,\n        \"max\": 46.6,\n        \"num_unique_values\": 129,\n        \"samples\": [\n          17.7,\n          30.5,\n          30.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Cylinders\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1,\n        \"min\": 3,\n        \"max\": 8,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          4,\n          5,\n          6\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Displacement\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 104.26983817119581,\n        \"min\": 68.0,\n        \"max\": 455.0,\n        \"num_unique_values\": 82,\n        \"samples\": [\n          122.0,\n          307.0,\n          360.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Horsepower\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 38.49115993282855,\n        \"min\": 46.0,\n        \"max\": 230.0,\n        \"num_unique_values\": 93,\n        \"samples\": [\n          92.0,\n          100.0,\n          52.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Weight\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 846.8417741973271,\n        \"min\": 1613.0,\n        \"max\": 5140.0,\n        \"num_unique_values\": 351,\n        \"samples\": [\n          3730.0,\n          1995.0,\n          2215.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Acceleration\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 2.7576889298126757,\n        \"min\": 8.0,\n        \"max\": 24.8,\n        \"num_unique_values\": 95,\n        \"samples\": [\n          14.7,\n          18.0,\n          14.3\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Model Year\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 3,\n        \"min\": 70,\n        \"max\": 82,\n        \"num_unique_values\": 13,\n        \"samples\": [\n          81,\n          79,\n          70\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Origin\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 1,\n        \"max\": 3,\n        \"num_unique_values\": 3,\n        \"samples\": [\n          1,\n          3,\n          2\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe","variable_name":"train_ND"}
```
:::
::::
