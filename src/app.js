const express = require("express");
const cors = require("cors");
const morgan = require("morgan");

const missionRoutes = require("./routes/mission.routes");
const commandRoutes = require("./routes/command.routes");
const telemetryRoutes = require("./routes/telemetry.routes");

const app = express();

app.use(cors());
app.use(express.json());
app.use(morgan("dev"));

app.use("/api/missions", missionRoutes);
app.use("/api/commands", commandRoutes);
app.use("/api/telemetry", telemetryRoutes);

app.get("/", (req, res) => {
  res.json({
    success: true,
    message: " Space Mission Backend Running",
  });
});

module.exports = app;