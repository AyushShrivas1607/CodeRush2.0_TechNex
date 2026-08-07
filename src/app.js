const express = require("express");
const cors = require("cors");
const morgan = require("morgan");

const missionRoutes = require("./routes/mission.routes");
const commandRoutes = require("./routes/command.routes");
const telemetryRoutes = require("./routes/telemetry.routes");
const plannerRoutes = require("./routes/planner.routes");
const procedureRoutes = require("./routes/procedure.routes");
const reportRoutes = require("./routes/report.routes");

// NEW ROUTES
const simulatorRoutes = require("./routes/simulator.routes");
const faultRoutes = require("./routes/fault.routes");
const alertRoutes = require("./routes/alert.routes");

const app = express();

app.use(cors());
app.use(express.json());
app.use(morgan("dev"));

// Existing Routes
app.use("/api/missions", missionRoutes);
app.use("/api/commands", commandRoutes);
app.use("/api/telemetry", telemetryRoutes);
app.use("/api/planner", plannerRoutes);
app.use("/api/procedure", procedureRoutes);
app.use("/api/reports", reportRoutes);

// NEW ROUTES
app.use("/api/simulator", simulatorRoutes);
app.use("/api/faults", faultRoutes);
app.use("/api/alerts", alertRoutes);

app.get("/", (req, res) => {
  res.json({
    success: true,
    message: "Space Mission Backend Running",
  });
});

module.exports = app;