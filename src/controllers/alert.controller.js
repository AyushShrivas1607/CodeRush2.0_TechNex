const Alert =
require("../models/Alert");

exports.getAlerts =
async(req,res)=>{

    const alerts =
    await Alert.find()
    .sort({
        timestamp:-1
    });

    res.json(alerts);

};

exports.getActiveAlerts =
async(req,res)=>{

    const alerts =
    await Alert.find({
        active:true
    });

    res.json(alerts);

};

exports.clearAlert =
async(req,res)=>{

    await Alert.findByIdAndUpdate(
        req.params.id,
        {
            active:false
        }
    );

    res.json({
        message:"Alert cleared"
    });

};