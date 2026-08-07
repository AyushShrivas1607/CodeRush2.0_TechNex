const plannerService = require("../services/planner.service");

exports.getMissionPlan = async (req, res) => {

    try {

        const plan = await plannerService.generatePlan(req.params.missionId);

        res.status(200).json({
            success: true,
            data: plan
        });

    } catch (error) {

        res.status(500).json({
            success: false,
            message: error.message
        });

    }

};