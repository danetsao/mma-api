const express = require('express');
const router = express.Router();

const pool = require('../db');

// Gets a rnadom athlete from all athletes
router.get("/random", async (req: any, res: any) => {
    try {
        console.log("Searching for random athlete");
        const athlete_data = await pool.query("SELECT * FROM top ORDER BY RANDOM() LIMIT 1");
        res.status(200).json(athlete_data.rows);
    }
    catch (err) {
        console.error(err);
    }
})

// Gets a random athlete by id from a given division
router.get("/random/:division_name", async (req: any, res: any) => {
    try {
        var { division_name } = req.params;
        console.log("Searching for random athlete in division " + division_name);
        const athlete_data = await pool.query("SELECT * FROM top WHERE weight_class = $1 ORDER BY RANDOM() LIMIT 1"
            ,[division_name])
        res.status(200).json(athlete_data.rows);
    }
    catch (err) {
        console.error(err);
    }
})

module.exports = router;
export {};