const express = require("express");

const router = express.Router();

const reportController = require("../controllers/report.controller");

router.get("/:missionId", reportController.getMissionReport);

module.exports = router;