const commandService = require("../services/command.service");

// Create Command
exports.createCommand = async (req, res) => {
    try {
        const command = await commandService.createCommand(req.body);

        res.status(201).json({
            success: true,
            data: command
        });

    } catch (err) {

        res.status(500).json({
            success: false,
            message: err.message
        });

    }
};

// Get Commands
exports.getMissionCommands = async (req, res) => {

    try {

        const commands = await commandService.getMissionCommands(
            req.params.missionId
        );

        res.json({
            success: true,
            data: commands
        });

    } catch (err) {

        res.status(500).json({
            success: false,
            message: err.message
        });

    }

};

// Approve
exports.approveCommand = async (req, res) => {

    try {

        const command = await commandService.approveCommand(req.params.id);

        res.json({
            success: true,
            data: command
        });

    } catch (err) {

        res.status(500).json({
            success: false,
            message: err.message
        });

    }

};

// Reject
exports.rejectCommand = async (req, res) => {

    try {

        const command = await commandService.rejectCommand(req.params.id);

        res.json({
            success: true,
            data: command
        });

    } catch (err) {

        res.status(500).json({
            success: false,
            message: err.message
        });

    }

};