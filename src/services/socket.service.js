const { getIO } = require("../config/socket");

const emitTelemetry = (missionId, telemetry) => {
  getIO().to(missionId).emit("telemetry", telemetry);
};

const emitAnomaly = (missionId, anomaly) => {
  getIO().to(missionId).emit("anomaly", anomaly);
};

const emitMissionUpdate = (missionId, data) => {
  getIO().to(missionId).emit("mission-update", data);
};

const emitCommandUpdate = (missionId, command) => {
  getIO().to(missionId).emit("command-approved", command);
};

module.exports = {
  emitTelemetry,
  emitAnomaly,
  emitMissionUpdate,
  emitCommandUpdate,
};