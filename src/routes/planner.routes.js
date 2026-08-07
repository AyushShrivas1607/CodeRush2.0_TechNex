const express = require("express");
const router = express.Router();

const plannerController = require("../controllers/planner.controller");

router.get("/:missionId", plannerController.getMissionPlan);

module.exports = router;