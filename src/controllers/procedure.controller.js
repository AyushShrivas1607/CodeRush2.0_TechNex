const procedureService = require("../services/procedure.service");

exports.getProcedure = (req, res) => {

    const { type } = req.params;

    const procedure = procedureService.getProcedure(type);

    res.status(200).json({

        success: true,

        data: procedure

    });

};