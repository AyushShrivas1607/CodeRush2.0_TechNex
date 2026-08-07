const express = require("express");

const router = express.Router();

const telemetryController = require("../controllers/telemetry.controller");

router.post("/", telemetryController.createTelemetry);

router.get("/:missionId", telemetryController.getMissionTelemetry);

router.get("/latest/:missionId", telemetryController.getLatestTelemetry);

module.exports = router;