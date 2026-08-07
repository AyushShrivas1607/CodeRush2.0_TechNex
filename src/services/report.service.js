const Mission = require("../models/Mission");
const Telemetry = require("../models/Telemetry");
const Command = require("../models/Command");

const generateMissionReport = async (missionId) => {

    const mission = await Mission.findById(missionId);

    const telemetry = await Telemetry.find({ missionId });

    const commands = await Command.find({ missionId });

    const averageBattery =
        telemetry.reduce((sum, item) => sum + item.battery, 0) /
        (telemetry.length || 1);

    const averageFuel =
        telemetry.reduce((sum, item) => sum + item.fuel, 0) /
        (telemetry.length || 1);

    const averageTemperature =
        telemetry.reduce((sum, item) => sum + item.temperature, 0) /
        (telemetry.length || 1);

    return {

        missionName: mission.missionName,

        spacecraft: mission.spacecraft,

        status: mission.status,

        telemetryFrames: telemetry.length,

        anomalyCount: telemetry.filter(t => t.anomalyDetected).length,

        approvedCommands:
            commands.filter(c => c.status === "APPROVED").length,

        rejectedCommands:
            commands.filter(c => c.status === "REJECTED").length,

        averageBattery: Number(averageBattery.toFixed(2)),

        averageFuel: Number(averageFuel.toFixed(2)),

        averageTemperature: Number(averageTemperature.toFixed(2))

    };

};

module.exports = {
    generateMissionReport
};