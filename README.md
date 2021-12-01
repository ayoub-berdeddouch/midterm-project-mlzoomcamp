#  Midterm Project - MLZOOMCAMP


# Dataset 
![Abalone Shell](https://i.pinimg.com/736x/88/fd/0e/88fd0ea8830ef739e830439f8eff13c6--abalone-shell-sea-shells.jpg)


* [Abalone Data Set Archive](https://archive.ics.uci.edu/ml/datasets/abalone)

* [Abalone Data Set Kaggle](https://www.kaggle.com/rodolfomendes/abalone-dataset)

## Source

Data comes from an original (non-machine-learning) study:
Warwick J Nash, Tracy L Sellers, Simon R Talbot, Andrew J Cawthorn and Wes B Ford (1994)
"The Population Biology of Abalone (_Haliotis_ species) in Tasmania. I. Blacklip Abalone (_H. rubra_) from the North Coast and Islands of Bass Strait",
Sea Fisheries Division, Technical Report No. 48 (ISSN 1034-3288)

## Original Owners of Database

* Marine Resources Division
* Marine Research Laboratories - Taroona

Department of Primary Industry and Fisheries, Tasmania
GPO Box 619F, Hobart, Tasmania 7001, Australia
(contact: Warwick Nash +61 02 277277, wnash '@' dpi.tas.gov.au)

## Donor of Database

Sam Waugh (Sam.Waugh '@' cs.utas.edu.au)
Department of Computer Science, University of Tasmania
GPO Box 252C, Hobart, Tasmania 7001, Australia

---

## Data Set Information

Predicting the age of abalone from physical measurements. The age of abalone is determined by cutting the shell through the cone, staining it, and counting the number of rings through a microscope -- a boring and time-consuming task. Other measurements, which are easier to obtain, are used to predict the age. Further information, such as weather patterns and location (hence food availability) may be required to solve the problem.

From the original data examples with missing values were removed (the majority having the predicted value missing), and the ranges of the continuous values have been scaled for use with an ANN (by dividing by 200).


---

## Attribute Information

Given is the attribute name, attribute type, the measurement unit and a brief description. 

The number of rings is the value to predict: either as a continuous value or as a classification problem.

| Name | Data Type | Measurement Unit | Description|
|:---|:---|:---|:---|
| `Sex` | nominal | -- | M, F, and I (infant)|
| `Length` | continuous | mm | Longest shell measurement|
| `Diameter` | continuous | mm | perpendicular to length|
| `Height` | continuous | mm | with meat in shell|
| `Whole weight` | continuous | grams | whole abalone|
| `Shucked weight` | continuous | grams | weight of meat|
| `Viscera weight` | continuous | grams | gut weight (after bleeding)|
| `Shell weight` | continuous | grams | after being dried|
| `Rings` | integer | -- | +1.5 gives the age in years|

## Problem Statement

Predicting the `Age of Abalone` from physical measurements. The age of abalone is determined by cutting the shell through the cone, staining it, and counting the number of `rings` through a microscope -- a laborious task. Other measurements, which are easier to obtain, are used to predict the age. Further information, such as weather patterns and location (hence food availability) may be required to solve the problem. However, for this problem we shall assume that the abalone's physical measurements are sufficient to provide an accurate age prediction.

The **abalone's** age is equal to the number of rings `+ 1.5`, another issue in the dataset is the presence of zeros, and possible multicollinearity.

---

#  Deployment of model

I am currently using Windows, so I am using Flask/gunicorn in order to deploy the model. To deploy this model with Flask/gunicorn, please use: 
```console
pipenv run gunicorn --bind 0.0.0.0:9696 predict:app
```
# Virtual Environment/venv

I used pipenv for the virtual environment. In order to use the same venv as me, do use: 
```console 
pip install pipenv
```

To replicate the environment, on your command line, use 
```console
pipenv install numpy pandas scikit-learn==0.24.2 statsmodels flask gunicorn
```

You can run the environment using `pipenv shell`, and deploy the model as normal.


# Docker

**Note**: to perform the following steps you should logon to your DockerHub Account ( `Logi & Password`)

I have built the model and pushed it to ayoubberd/abalone-age-prediction:latest . 
To use it just 
```console
docker pull ayoubberd/abalone-age-prediction:latest
```

Or in order to take the model from the docker container I built, just replace 
```Dockerfile
FROM python:3.8.12-slim 

#with 

FROM ayoubberd/abalone-age-prediction:latest in the dockerfile.
```

If you choose to build a docker file locally instead, here are the steps to do so:

1. Create a Dockerfile as such:
```Dockerfile
FROM python:3.8.12-slim

LABEL maintainer="Ayoub Berdeddouch"

ENV PYTHONUNBUFFERED=TRUE

RUN pip --no-cache-dir install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN set -ex && pipenv install --deploy --system
# RUN pipenv install --deploy --system 

COPY ["predict.py", "model_n_estimators=400.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]

```

This allows us to `install python, run pipenv and its dependencies, run our predict script and our model itself and deploys our model using Flask/gunicorn`.

Similarly, you can just use the dockerfile in this repository.

2. Build the Docker Container with :
```console
 docker build -t abalone-age-prediction .
 ```

3. Run the Docker container with:

```console
Docker run -it -p 9696:9696 abalone-age-prediction:latest 
```

Now we can use our model through 
```console
python predict-test.py
```

4. tag the docker container with:

```console

docker tag abalone-age-prediction ayoubberd/abalone-age-prediction:latest

```
5. Push it Docker registry with :

```console
docker push ayoubberd/abalone-age-prediction:latest

```


# Heroku

The web app will show like this ( I need to upload the model which is about 100Mo)

![Abalone Age Prediciton](https://github.com/ayoub-berdeddouch/midterm-project-mlzoomcamp/blob/main/screenshot.png)




# Errors after Deadline of midterm

I had to upload the model which was about 100Mo so after that the repo got just the model and I couldn't revert it.

![Error just for proof](https://github.com/ayoub-berdeddouch/midterm-project-mlzoomcamp/blob/main/git_err_model.png)

![Error just for proof](https://github.com/ayoub-berdeddouch/midterm-project-mlzoomcamp/blob/main/git_error.png)




# Want to Contribute?
* Fork 🍴 the repository and send PRs.
* Do ⭐ this repository if you like the content.

Made with 💟 by [Ayoub Berdeddouch](https://github.com/ayoub-berdeddouch)

**Connect with me:**

<p align="center">
  <a href="https://linkedin.com/in/ayoub-berdeddouch/" target="blank"><img align="center" src="https://www.vectorlogo.zone/logos/linkedin/linkedin-tile.svg" alt="https://www.linkedin.com/in/ayoub-berdeddouch/" height="30" width="30" /></a>
  <a href="https://www.twitter.com/ABerdeddouch/" target="blank"><img align="center"  src="https://img.icons8.com/color/48/000000/twitter--v2.png" alt="https://www.twitter.com/ABerdeddouch/" height="30" width="30" /></a>
  <a href="https://ayoubberdeddouch.com" target="blank">
    <img align="center" src="https://img.icons8.com/clouds/100/000000/domain.png" alt="https://ayoubberdeddouch.com" height="30" width="30" /></a>
  
</p>
