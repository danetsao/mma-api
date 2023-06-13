const express = require('express');
const router = express.Router();

const pool = require('../db');

// Gets every line for given character, season, and episode
router.get("/athletes/:name", async (req: any, res: any) => {
    try {
        const { name } = req.params;
        console.log("Searching for " + name);
        const athlete_data = await pool.query("SELECT * FROM top WHERE name_postfix = $1"
            ,[name])
        res.json(athlete_data.rows);
    }
    catch (err) {
        console.error(err);
    }
})

// Get all athlete data
router.get('/athletes', async (req: any, res: any) => {
    try {
        const athlete_data = await pool.query('SELECT * FROM top');
        return res.status(200).json(athlete_data.rows);
    }
    catch (err) {
        console.log(err);
        return res.status(500).json({ message: 'Internal Server Error' });
    }
});


module.exports = router;
export {};