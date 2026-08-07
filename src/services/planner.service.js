const generatePlan = async (mission) => {

    const start = new Date();

    return [
        {
            step: 1,
            task: "Launch",
            scheduledAt: start,
            status: "PLANNED"
        },
        {
            step: 2,
            task: "Deploy Solar Panels",
            scheduledAt: new Date(start.getTime() + 30 * 60000),
            status: "PLANNED"
        },
        {
            step: 3,
            task: "Orbit Stabilization",
            scheduledAt: new Date(start.getTime() + 60 * 60000),
            status: "PLANNED"
        },
        {
            step: 4,
            task: "Payload Observation",
            scheduledAt: new Date(start.getTime() + 120 * 60000),
            status: "PLANNED"
        },
        {
            step: 5,
            task: "Downlink Telemetry",
            scheduledAt: new Date(start.getTime() + 180 * 60000),
            status: "PLANNED"
        }
    ];

};

module.exports = { generatePlan };