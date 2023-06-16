import express from 'express';
import { Request, Response } from 'express';

const all_routes = require('express-list-endpoints');

const pool = require('./db');

const app = express();
const port = 3000;

app.get('/', (req: any, res: any) => {
    res.send('Hello World!');
});

app.get('/routes', (req: Request, res: Response) => {
    res.send(all_routes(app));
});

const athleteRoutes = require('./routes/athlete');
app.use(athleteRoutes);

const divisionRoutes = require('./routes/division');
app.use(divisionRoutes);

const randomRoutes = require('./routes/random');
app.use(randomRoutes);

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
