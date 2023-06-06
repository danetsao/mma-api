import express from 'express';
import { Request, Response } from 'express';
// import db 
const pool = require('./db');

const app = express();
const port = 3000;

app.get('/', (req: any, res: any) => {
    res.send('Hello World!');
});

// Get all athlete data
app.get('/athlete', async (req, res) => {
    try {
        const athlete_data = await pool.query('SELECT * FROM top');
        return res.status(200).json(athlete_data.rows);
    }
    catch (err) {
        console.log(err);
        return res.status(500).json({ message: 'Internal Server Error' });
    }
});


// Get athlete data by name
app.get('/athlete/:athlete_postfix', (req, res) => {
    const athlete_postfix = req.params.athlete_postfix;
    const first = athlete_postfix.split('-')[0];
    const last = athlete_postfix.split('-')[1];

    //Query database for athlete data.

    const obj = {
        url: 'https://www.ufc.com/athlete/' + athlete_postfix,
        first: first,
        last: last
    }; 
    res.json(obj);
});

// funciton to validate weight class
function validate(weightclass: string) {
    const weightclasses = ['strawweight', 'flyweight', 'bantamweight', 'featherweight', 'lightweight', 'welterweight', 'middleweight', 'light-heavyweight', 'heavyweight'];
    return weightclasses.includes(weightclass);
}

// To get top 15 athletes by weight class, by default mens
app.get('/:weightclass', (req, res) => {
    const weightclass = req.params.weightclass;
    if (!validate(weightclass)) {
        res.status(400);
        res.send('Invalid weight class');
        return;
    }
    // Return all athlete data
    //Query database for all athlete data.
    const obj = {
        data: 'all athlete data'
    };
    res.json(obj);
});

// Listen for incoming requests
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
