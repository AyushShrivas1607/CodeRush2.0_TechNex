const Command = require("../models/Command");

// Create Command
const createCommand = async (data) => {
    return await Command.create(data);
};

// Get Commands of a Mission
const getMissionCommands = async (missionId) => {
    return await Command.find({ missionId }).sort({ createdAt: -1 });
};

// Approve Command
const approveCommand = async (id, approvedBy = "Operator") => {
    return await Command.findByIdAndUpdate(
        id,
        {
            status: "APPROVED",
            approvedBy,
            approvedAt: new Date()
        },
        { new: true }
    );
};

// Reject Command
const rejectCommand = async (id) => {
    return await Command.findByIdAndUpdate(
        id,
        {
            status: "REJECTED"
        },
        { new: true }
    );
};

module.exports = {
    createCommand,
    getMissionCommands,
    approveCommand,
    rejectCommand
};