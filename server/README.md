# MMA Athletes API

This is the API documentation for the UFC Athletes API.
The API provides information on UFC athletes and their fights.

## Read the documentation here or visit the demo [website](google.com) when finished

## Authentication

All endpoints require authentication. You must include a bearer token in the 'Authorization' header of each request.

## Base URL

`https://localhost:3000/v1`

## Group Athletes

### Athletes Collection [/athlete]

#### List All Athletes [GET]

+ Response 200 (application/json)

        [
            {
                "first": "leon",
                "last": "edwards"
            },
            {
                "first": "jon",
                "jon": "jones
            }
        ]


### Athletes Collection [/athlete/first-last]

#### List Athlete by Name [GET]

+ Response 200 (application/json)

        {
            "first": "leon",
            "last": "edwards"
        }