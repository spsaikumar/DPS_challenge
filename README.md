# AI Engineering Challenge: Digital Product School of UnternehmerTUM

## Description
This challenge for Artificial Intelligence Engineer Consists of 3 tasks.

Mission 1: Create a AI Model
Mission 2: Publish source code & Deploy
Mission 3: Sending the URL of the task

## Demo link
View demo <a href="https://spsaikumar-dps-challenge-app-swrm06.streamlit.app/"><b>Here 💻</b></a>.
Or use this API endpoint  `https://spsaikumar-dps-challenge-app-swrm06.streamlit.app/` to returns your predictions.
#### Note
The endpoint accepts a POST request with a JSON body like this:
```
{
"year" : 2021,
"month" : 1
}
```
It return prediction in the following format:
```
{
"prediction" : value
}
```
## DataFrame

Download the <a href="https://www.opengov-muenchen.de/dataset/monatszahlen-verkehrsunfaelle/resource/40094bd6-f82d-4979-949b-26c8dc00b9a7"><b>Monatszahlen Verkehrsunfälle</b></a> Dataset from the München Open Data Portal. Here you see the number of accidents for specific categories per month.

## Packages:
- pandas
- numpy
- matplotlib
- sklearn
- pickle
- streamlit

## Visualization:
visualization historically the number of accidents per category
### Accidents Category Visualization:

<img src="./images/No. of Accidents per Category_multiplots.png"/>

<br />

### Number of accidents per category:

<img src="./images/No. of Accidents per Category.png"/>

<br />

### Number of accidents per Accident Type:

<img src="./images/No. of Accidents per Accident type.png"/>

<br />

### Performace metrics of different models


|    Category    | Accident_Type |         Model         |    MSE    |  RMSE  |  MAE   |   R2   |  COD  |  EVS  |
|   ----------   | ----------    |         ----------    |---------- |--------|--------|--------|--------|------|
| Alkoholunfälle |   insgesamt   |        Prophet        | 475869.55 | 268.8  | 581.39 | -0.697 | -0.45 | -0.45 |
| Alkoholunfälle |   insgesamt   |         ARIMA         | 286984.07 | 535.71 | 456.96 | -0.023 |  0.16 |  0.0  |
| Alkoholunfälle |   insgesamt   |         SARIMA        | 286984.07 | 535.71 | 456.96 | -0.023 |  0.16 |   0   |
| Alkoholunfälle |   insgesamt   |   Linear Regression   |   153.66  |  12.4  |  9.97  | 0.194  |  0.2  |  0.2  |
| Alkoholunfälle |   insgesamt   |     Decision Tree     |   94.37   |  9.71  |  8.02  | 0.505  |  0.51 |  0.51 |
| Alkoholunfälle |   insgesamt   |     Random Forest     |    63.6   |  7.98  |  6.03  | 0.666  |  0.68 |  0.68 |
| Alkoholunfälle |   insgesamt   |          SVR          |   199.18  | 14.11  | 11.54  | -0.045 |  0.0  |  0.0  |
| Alkoholunfälle |   insgesamt   |          GBT          |    57.6   |  7.59  |  5.95  | 0.698  |  0.71 |  0.71 |
| Alkoholunfälle |   insgesamt   |          XGB          |    64.8   |  8.05  |  6.37  |  0.66  |  0.67 |  0.67 |
| Alkoholunfälle |   insgesamt   |         LGBMR         |   67.76   |  8.23  |  6.56  | 0.644  |  0.65 |  0.65 |
| Alkoholunfälle |   insgesamt   |   RandomSearch_CV-RF  |   70.56   |  8.4   |  6.74  |  0.63  |  0.64 |  0.64 |
| Alkoholunfälle |   insgesamt   |  RandomSearch_CV-GBT  |   81.52   |  9.03  |  6.95  | 0.572  |  0.59 |  0.59 |
| Alkoholunfälle |   insgesamt   |  RandomSearch_CV-XGB  |    64.8   |  8.05  |  6.37  |  0.66  |  0.67 |  0.67 |
| Alkoholunfälle |   insgesamt   | RandomSearch_CV-LGBMR |   67.76   |  8.23  |  6.56  | 0.644  |  0.65 |  0.65 |

<br />


|    Category   | Accident_Type |         Model         |    MSE    |  RMSE  |  MAE   |   R2   |  COD  |  EVS  |
|---------------|---------------|-----------------------|-----------|--------|--------|--------|-------|-------|
| Fluchtunfälle |   insgesamt   |        Prophet        | 475869.55 | 268.8  | 581.39 | -0.697 | -0.45 | -0.45 |
| Fluchtunfälle |   insgesamt   |         ARIMA         | 286984.07 | 535.71 | 456.96 | -0.023 |  0.16 |  0.0  |
| Fluchtunfälle |   insgesamt   |         SARIMA        | 286984.07 | 535.71 | 456.96 | -0.023 |  0.16 |   0   |
| Fluchtunfälle |   insgesamt   |   Linear Regression   |  22996.23 | 151.65 | 116.8  | 0.096  |  0.1  |  0.1  |
| Fluchtunfälle |   insgesamt   |     Decision Tree     |  12682.2  | 112.62 | 83.33  | 0.502  |  0.5  |  0.5  |
| Fluchtunfälle |   insgesamt   |     Random Forest     |  9744.82  | 98.72  | 73.18  | 0.617  |  0.62 |  0.62 |
| Fluchtunfälle |   insgesamt   |          SVR          |  25521.3  | 159.75 | 122.24 | -0.003 |  0.0  |  0.0  |
| Fluchtunfälle |   insgesamt   |          GBT          |  10154.17 | 100.77 | 75.02  | 0.601  |  0.6  |  0.6  |
| Fluchtunfälle |   insgesamt   |          XGB          |  10182.72 | 100.91 | 73.06  |  0.6   |  0.61 |  0.61 |
| Fluchtunfälle |   insgesamt   |         LGBMR         |  11461.87 | 107.06 | 76.03  |  0.55  |  0.55 |  0.55 |
| Fluchtunfälle |   insgesamt   |   RandomSearch_CV-RF  |  12020.19 | 109.64 | 78.93  | 0.528  |  0.53 |  0.53 |
| Fluchtunfälle |   insgesamt   |  RandomSearch_CV-GBT  |  11253.91 | 106.08 | 76.44  | 0.558  |  0.56 |  0.56 |
| Fluchtunfälle |   insgesamt   |  RandomSearch_CV-XGB  |  9373.33  | 96.82  | 70.46  | 0.632  |  0.64 |  0.64 |
| Fluchtunfälle |   insgesamt   | RandomSearch_CV-LGBMR |  11461.87 | 107.06 | 76.03  |  0.55  |  0.55 |  0.55 |


<br />


|     Category    | Accident_Type |         Model         |    MSE    |  RMSE  |  MAE   |   R2   |  COD  |  EVS  |
|---------------  |---------------|-----------------------|-----------|--------|--------|--------|-------|-------|
| Verkehrsunfälle |   insgesamt   |        Prophet        | 475869.55 | 268.8  | 581.39 | -0.697 | -0.45 | -0.45 |
| Verkehrsunfälle |   insgesamt   |         ARIMA         | 286984.07 | 535.71 | 456.96 | -0.023 |  0.16 |  0.0  |
| Verkehrsunfälle |   insgesamt   |         SARIMA        | 286984.07 | 535.71 | 456.96 | -0.023 |  0.16 |   0   |
| Verkehrsunfälle |   insgesamt   |   Linear Regression   | 190406.83 | 436.36 | 345.47 | 0.219  |  0.22 |  0.22 |
| Verkehrsunfälle |   insgesamt   |     Decision Tree     | 105933.24 | 325.47 | 236.18 | 0.565  |  0.57 |  0.57 |
| Verkehrsunfälle |   insgesamt   |     Random Forest     |  53422.3  | 231.13 | 167.24 | 0.781  |  0.78 |  0.78 |
| Verkehrsunfälle |   insgesamt   |          SVR          | 243957.67 | 493.92 | 394.52 | -0.001 |  0.0  |  0.0  |
| Verkehrsunfälle |   insgesamt   |          GBT          |  38605.96 | 196.48 | 151.65 | 0.842  |  0.84 |  0.84 |
| Verkehrsunfälle |   insgesamt   |          XGB          |  72669.09 | 269.57 | 202.41 | 0.702  |  0.7  |  0.7  |
| Verkehrsunfälle |   insgesamt   |         LGBMR         |  72251.2  | 268.8  | 193.06 | 0.703  |  0.7  |  0.7  |
| Verkehrsunfälle |   insgesamt   |   RandomSearch_CV-RF  |  54405.23 | 233.25 | 175.82 | 0.777  |  0.78 |  0.78 |
| Verkehrsunfälle |   insgesamt   |  RandomSearch_CV-GBT  |  59797.36 | 244.53 | 186.68 | 0.755  |  0.76 |  0.76 |
| Verkehrsunfälle |   insgesamt   |  RandomSearch_CV-XGB  |  65215.93 | 255.37 | 202.29 | 0.732  |  0.73 |  0.73 |
| Verkehrsunfälle |   insgesamt   | RandomSearch_CV-LGBMR |  61477.22 | 247.95 | 177.96 | 0.748  |  0.75 |  0.75 |




