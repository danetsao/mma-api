const express = require('express');
const router = express.Router();

const pool = require('../db');

// Gets every line for given character, season, and episode
router.get("/division/:division_name", async (req: any, res: any) => {
    try {
        var { division_name } = req.params;
        // turn division_name first letter to uppercase
        division_name = division_name.charAt(0).toUpperCase() + division_name.slice(1);

        console.log("Searching for all athletes in division " + division_name);
        const athlete_data = await pool.query("SELECT * FROM top WHERE weight_class = $1"
            ,[division_name])
        res.json(athlete_data.rows);
    }
    catch (err) {
        console.error(err);
    }
})

module.exports = router;
