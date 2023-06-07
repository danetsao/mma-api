import express from 'express';
import { Request, Response } from 'express';

const all_routes = require('express-list-endpoints');
// import db 

const pool = require('./db');

const app = express();
const port = 3000;

app.get('/', (req: any, res: any) => {
    res.send('Hello World!');
});

// Get all athlete data
const athleteRoutes = require('./routes/athlete');
app.use(athleteRoutes);

// Get all division data
const divisionRoutes = require('./routes/division');
app.use(divisionRoutes);


// Route "/routes" returns all routes
app.get('/routes', (req: Request, res: Response) => {
    res.send(all_routes(app));
});


// Listen for incoming requests
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
