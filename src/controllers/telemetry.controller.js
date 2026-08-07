const telemetryService = require("../services/telemetry.service");
const aiService = require("../services/ai.service");
const commandService = require("../services/command.service");

exports.createTelemetry = async (req, res) => {
    try {

        // Save telemetry
        const telemetry =
            await telemetryService.createTelemetry(req.body);

        // AI Prediction
        const aiResult =
            await aiService.predictTelemetry(req.body);

        // Update anomaly flag
        if (aiResult.anomaly) {

            telemetry.anomalyDetected = true;

            await telemetry.save();

            // Create Pending Command
            await commandService.createCommand({

                missionId: telemetry.missionId,

                command: aiResult.recommendation,

                recommendation: aiResult.reason

            });

        }

        res.status(201).json({

            success: true,

            telemetry,

            ai: aiResult

        });

    } catch (err) {

        res.status(500).json({

            success: false,

            message: err.message

        });

    }
};
exports.getMissionTelemetry = async (req, res) => {

    try {

        const telemetry =
            await telemetryService.getMissionTelemetry(
                req.params.missionId
            );

        res.json({
            success: true,
            data: telemetry
        });

    } catch (err) {

        res.status(500).json({
            success: false,
            message: err.message
        });

    }

};

exports.getLatestTelemetry = async (req, res) => {

    try {

        const telemetry =
            await telemetryService.getLatestTelemetry(
                req.params.missionId
            );

        res.json({
            success: true,
            data: telemetry
        });

    } catch (err) {

        res.status(500).json({
            success: false,
            message: err.message
        });

    }

};