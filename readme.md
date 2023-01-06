# HausApp2

Web app to help you find a renting place in Sydney and Melbourne, Australia

This is a rebuild of HausApp. After Heroku shutdown their free tier I decided to recreate the project.
The original stack used on the webapp parte Bokeh for the graphs, Flask for the backend and Boostrap for the frontend


## Architecture

The project use multiple free to use tools on the cloud for each architecural component

![architecture](static\hausApp.drawio.png)

#### Data extraction
Scrapy for data scrapping and Zyte for scheduling jobs

#### Backend
Container runs Python API to clean and summaries data and store it on Firebase

#### Database
Persistent storage of cleaned data. It also reduses the workload for the webapp server.

#### Webapp
Frontend Build on Dash (Flask + React + Plotly)
It also replaces a scheduling server, by creating a number of queries to check update the data and run mantainability scripts

#### Monitoning


## Tech stack