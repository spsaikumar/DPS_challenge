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

### Performace metrics of different models:

+----------------+---------------+-----------------------+-----------+--------+--------+--------+-------+-------+
|    Category    | Accident_Type |         Model         |    MSE    |  RMSE  |  MAE   |   R2   |  COD  |  EVS  |
+----------------+---------------+-----------------------+-----------+--------+--------+--------+-------+-------+
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
+----------------+---------------+-----------------------+-----------+--------+--------+--------+-------+-------+
