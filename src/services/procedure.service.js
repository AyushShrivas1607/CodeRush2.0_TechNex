const runbooks = require("../data/runbooks.json");

const getProcedure = (anomalyType) => {

    return runbooks[anomalyType] || {

        command: "NO_ACTION",

        recommendation: "Continue monitoring the spacecraft.",

        severity: "LOW"

    };

};

module.exports = {
    getProcedure
};