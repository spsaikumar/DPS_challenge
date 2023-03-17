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

### Number of accidents per category
<img src="./images/No. of Accidents per Category.png"/>

<br />

### Number of accidents per Accident Type
<img src="./images/No. of Accidents per Accident type.jpg"/>

<br />

### Performace metrics of different models:
<img src="./images/Alkoholunfälle_insgesamt_table.png"/>
<img src="./images/Fluchtunfälle_insgesamt_table.png"/>
<img src="./images/Verkehrsunfälle_insgesamt_table.png"/>

<br />
