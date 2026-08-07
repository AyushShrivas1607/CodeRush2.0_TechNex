const axios = require("axios");

const AI_URL = process.env.AI_SERVICE_URL;

const predictTelemetry = async (telemetry) => {
    try {

        const response = await axios.post(
            `${AI_URL}/predict`,
            telemetry
        );

        return response.data;

    } catch (err) {

        console.error("AI Service Error:", err.message);

        return {
            success: false,
            anomaly: false,
            risk: "UNKNOWN",
            score: 0,
            recommendation: null
        };
    }
};

module.exports = {
    predictTelemetry
};