const reportService = require("../services/report.service");

exports.getMissionReport = async (req, res) => {

    const report = await reportService.generateMissionReport(req.params.missionId);

    res.status(200).json({

        success: true,

        data: report

    });

};