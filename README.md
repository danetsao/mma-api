
# MMA API

A brief description of what this project does and who it's for


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
