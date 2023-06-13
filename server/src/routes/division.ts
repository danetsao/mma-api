const express = require('express');
const router = express.Router();

const pool = require('../db');

// Gets every line for given character, season, and episode
router.get("/division/:division_name", async (req: any, res: any) => {
    try {
        var { division_name } = req.params;

        console.log("Searching for all athletes in division " + division_name);
        const athlete_data = await pool.query("SELECT * FROM top WHERE weight_class = $1"
            ,[division_name])
        res.status(200).json(athlete_data.rows);
    }
    catch (err) {
        console.error(err);
    }
})

// Gets top 5 athletes in a given division
router.get("/division/:division_name/top5", async (req: any, res: any) => {
    try {
        var { division_name } = req.params;

        console.log("Searching for top 5 athletes in division " + division_name);
        const athlete_data = await pool.query("SELECT * FROM top WHERE weight_class = $1 ORDER BY rank LIMIT 5"
            ,[division_name])
        res.status(200).json(athlete_data.rows);
    }
    catch (err) {
        console.error(err);
    }
})

// Get p4p rankings
router.get('/p4p', async (req: any, res: any) => {
    try {
        console.log("Searching for all athletes in p4p rankings ");
        const athlete_data = await pool.query("SELECT * FROM top WHERE p4p_rank >= 0");
        
        console.log(athlete_data);
        athlete_data.rows.sort((a: any, b: any) => (a.p4p_rank > b.p4p_rank) ? 1 : -1);
        res.status(200).json(athlete_data.rows);
    }
    catch (err) {
        console.error(err);
    }
})


module.exports = router;
