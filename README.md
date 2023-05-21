
# MMA API :martial_arts_uniform: :boxing_glove:

### A REST API for getting current information on mma athletes.

## Table of Contents
- [Overview](#overview)
- [Deployment](#deployment)
    - [Scraping](#scraping)
    - [Database](#database)
    - [API](#api)
- [Environment Variables](#environment-variables)

## Overview

This is an MMA API that scraped data from [ufc.com](https://www.ufc.com/), stores it in a Postgres database, and has a node + express api to give information on the athletes. 

If you have questions, or comments feel free to reach out. I plan to continue working at this and open up some issues for others to contribute with. If you are interested in contributing, see contribution guidelines [here](https://github.com/danetsao/mma-api)

## Deployment

### Scraping

It's easy to get started scraping.

```bash
  git clone https://github.com/danetsao/mma-api.git
```
```bash
  cd scraping
```
```bash
  pip install -r requirements.txt
```
```bash
  python scrape.py
```
For further use such as storage or api, see Environment Variables to continue.

### Database

Here we will config and store the scraped info in a db.
This assumes you have configured your .env variables and have Postgres installed locally.

```bash
  cd database
```
```bash
  python db.py
```

### API

Start in the root directory

```bash
  npm install
```
```bash
  npm run dev
```
Now visit localhost:3000 and use the api.
## Environment Variables

For specific functionly, you will need to add the following environment variables to your .env file

To store scraped information to database (needed to run api locally)

PostgreSQL Database

`DB_HOST`

`DB_PORT`

`DB_NAME`

`DB_USER`

`DB_PASSWORD`

If you need help configuring a PostgreSQL database, see [documentation](https://www.postgresql.org/docs/)
