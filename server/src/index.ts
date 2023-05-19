import express from 'express';

const app = express();
const port = 3000;

app.get('/', (req: any, res: any) => {
    res.send('Hello World!');
});

app.get('/test', (req: any, res: any) => {
    res.send('Test');
});

// Listen for incoming requests
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
