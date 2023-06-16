
<div align="center">
  <h3 href="https://github.com/danetsao/mma-api">
   MMA API :martial_arts_uniform: :boxing_glove:
  </h3>

  <p align="center">
    A REST API for getting current information on mma athletes.
    <br />
    <br />
    <a href="https://github.com/danetsao/mma-api"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#deployment">Try it yourself</a>
    ·
    <a href="https://github.com/danetsao/mma-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/danetsao/mma-api/issues">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#overview">Overview</a>
    </li>
    <li>
      <a href="#scraping">Scraping</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#environment-variables">Environment Variables</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="https://github.com/danetsao/mma-api/blob/main/CONTRIBUTING.md">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## Overview

This is an MMA API that scraped data from [ufc.com](https://www.ufc.com/rankings), stores it in a Postgres database, and has a node + express api to give information on the athletes.

A supplemental [mma-scraping](https://github.com/danetsao/mma-scraping) repository is used to configre the database and can be used for much more.

## Scraping

See [mma-scraping](https://github.com/danetsao/mma-api) to get started scraping mma data.

You can use this repo to config the database used in this api.

## Getting Started

### Prerequisites

prereqs

### Environment Variables

For specific functionly, you will need to add the following environment variables to your .env file

To store scraped information to database (needed to run api locally)

PostgreSQL Database

`DB_HOST`

`DB_PORT`

`DB_NAME`

`DB_USER`

`DB_PASSWORD`

If you need help configuring a PostgreSQL database, see [documentation](https://www.postgresql.org/docs/)

### Installations

installations

## License

Distributed under the MIT License. See LICENSE for more information.

## Acknowledgments

* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
* [valish](https://github.com/valish/mma-api)

[⬆️ Back to Top ⬆️](#table-of-contents)