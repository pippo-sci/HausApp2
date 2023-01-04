# HausApp2

Web app to help you find a renting place in Sydney and Melbourne, Australia

This is a rebuild of HausApp. After Heroku shutdown their free tier I decided to recreate the proyect.
The original stack used on the webapp parte Bokeh for the graphs, Flask for the backend and Boostrap for the frontend


## Architecture

The project use multiple free to use tools on the cloud for each architecural component

#### Data extraction
Scrapy for data scrapping and Zyte for scheduling jobs

#### Backend
Container runs Python script to clean and summaries data and store it on Firebase

#### Webapp
Frontend Build on Dash (Flask + React + Plotly)
It also replaces a scheduling server, by creating a number of queries to check update the data and run mantainability scripts

#### Monitoning


## Tech stack