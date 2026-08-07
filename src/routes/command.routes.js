const express = require("express");

const router = express.Router();

const commandController = require("../controllers/command.controller");

router.post("/", commandController.createCommand);

router.get("/:missionId", commandController.getMissionCommands);

router.patch("/:id/approve", commandController.approveCommand);

router.patch("/:id/reject", commandController.rejectCommand);

module.exports = router;