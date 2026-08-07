const express = require("express");

const router = express.Router();

const procedureController = require("../controllers/procedure.controller");

router.get("/:type", procedureController.getProcedure);

module.exports = router;