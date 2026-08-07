const express = require("express");
const router = express.Router();

const missionController = require("../controllers/mission.controller");

router.post("/", missionController.createMission);

router.get("/", missionController.getAllMissions);

router.get("/:id", missionController.getMissionById);

router.put("/:id", missionController.updateMission);

router.delete("/:id", missionController.deleteMission);

module.exports = router;