const Alert = require("../models/Alert");
const { getIO } = require("../config/socket");

async function createAlert(type, severity, message) {

    const exists = await Alert.findOne({
        type,
        active: true
    });

    if (exists)
        return;

    const alert = await Alert.create({
        type,
        severity,
        message
    });

    const io = getIO();

    if (io) {
        io.emit("alert", alert);
    }
}

async function resolveAlert(type) {

    await Alert.findOneAndUpdate(
        {
            type,
            active: true
        },
        {
            active: false
        }
    );

}

async function checkTelemetry(data) {

    // Battery

    if (data.battery < 20)
        await createAlert(
            "LOW_BATTERY",
            "CRITICAL",
            "Battery below 20%"
        );
    else
        await resolveAlert("LOW_BATTERY");


    // Fuel

    if (data.fuel < 100)
        await createAlert(
            "LOW_FUEL",
            "WARNING",
            "Fuel level is low"
        );
    else
        await resolveAlert("LOW_FUEL");


    // Temperature

    if (data.temperature > 80)
        await createAlert(
            "OVERHEATING",
            "CRITICAL",
            "Temperature exceeded 80°C"
        );
    else
        await resolveAlert("OVERHEATING");


    // Communication

    if (!data.communication)
        await createAlert(
            "COMMUNICATION_LOST",
            "CRITICAL",
            "Communication lost"
        );
    else
        await resolveAlert("COMMUNICATION_LOST");


    // Altitude

    if (data.altitude < 300)
        await createAlert(
            "LOW_ALTITUDE",
            "WARNING",
            "Altitude below safe threshold"
        );
    else
        await resolveAlert("LOW_ALTITUDE");


    // Velocity

    if (data.velocity > 9000)
        await createAlert(
            "HIGH_VELOCITY",
            "WARNING",
            "Velocity exceeds safe limit"
        );
    else
        await resolveAlert("HIGH_VELOCITY");

}

module.exports = {
    checkTelemetry
};