import express from 'express';
import { Request, Response } from 'express';

const athleteJson = require('./athlete.json');
const all_routes = require('express-list-endpoints');
// import db 

const app = express();
const port = 3000;

app.get('/', (req: any, res: any) => {
    res.send('Hello From Json!');
});

// Get all athlete data
app.get("/athletes/", async (req: Request, res: Response) => {
  const {id} = req.params;
  try {
    await res.status(200).send(athleteJson);
  }
  catch (err) {
    res.status(500).send(err);
  }
});

app.get("/athletes/:name", async (req: Request, res: Response) => {
    const {name} = req.params;
    console.log("Searching for " + name)
    try {
        const cur_athlete_data = athleteJson.filter((weight_class: any) => weight_class.filter((athlete: any) => athlete.name_postfix === name));
      console.log(cur_athlete_data);
        res.status(200).send(cur_athlete_data);
    }
    catch (err) {
      res.status(500).send(err);
    }
  });


// Listen for incoming requests
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
