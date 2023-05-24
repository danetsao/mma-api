
# MMA API :martial_arts_uniform: :boxing_glove:

### A REST API for getting current information on mma athletes.

## Table of Contents
- [Overview](#overview)
- [To Do](#to-do)
- [Deployment](#deployment)
    - [Scraping](#scraping)
    - [Database](#database)
    - [API](#api)
- [Environment Variables](#environment-variables)
- [Usage](#usage)

---

## Overview

This is an MMA API that scraped data from [ufc.com](https://www.ufc.com/rankings), stores it in a Postgres database, and has a node + express api to give information on the athletes. 

If you have questions, or comments feel free to reach out. I plan to continue working at this and open up some issues for others to contribute with. If you are interested in contributing, see contribution guidelines [here](https://github.com/danetsao/mma-api/blob/main/CONTRIBUTING.md)

## To Do
Right now, we are working on a few different thigns
- Configuring a database
- Building a showcase website/frontend
    - [Nextjs](https://nextjs.org/)
- Building a community to contribute to the project
- Add other methods of storing scraped data
    - Excel
- Deployment for remote use of api
    - [AWS RDS](https://aws.amazon.com/rds/) + Server Hosting
- Addition of other fighting leagues and sports
    - Would need to reconfig large portion of api & add scraping, but could be cool.
    - MMA
        - [ONEFC](https://www.onefc.com/)
        - [Bellator](https://www.bellator.com/)
        - [PFL](https://www.pflmma.com/)
    - Other sports
        - May be better suited for another project
        - Boxing
        - BJJ

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
I recommend you uncomment the print statements so you can see your data.
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

## Usage
There is a wide array of uses for the project. Some ideas:

- Analytics
- Blog
- Data science 

[⬆️ Back to Top ⬆️](#table-of-contents)