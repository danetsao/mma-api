import express from 'express';

const app = express();
const port = 3000;

app.get('/', (req: any, res: any) => {
    res.send('Hello World!');
});

// Get all athlete data
app.get('/athlete', (req, res) => {
    // Return all athlete data
    //Query database for all athlete data.
    const obj = {
        data: 'all athlete data'
    };
    res.json(obj);
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

// Listen for incoming requests
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
