const Telemetry = require("../models/Telemetry");

const createTelemetry = async (data) => {
    return await Telemetry.create(data);
};

const getMissionTelemetry = async (missionId) => {
    return await Telemetry.find({ missionId }).sort({ timestamp: 1 });
};

const getLatestTelemetry = async (missionId) => {
    return await Telemetry
        .findOne({ missionId })
        .sort({ timestamp: -1 });
};

module.exports = {
    createTelemetry,
    getMissionTelemetry,
    getLatestTelemetry
};