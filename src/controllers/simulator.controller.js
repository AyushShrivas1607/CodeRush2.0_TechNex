const simulator=
require("../services/simulatorLoop");


const {
    getState
}=require("../services/digitalTwin");



exports.start=async(req,res)=>{


    simulator.startSimulation();


    res.json({

        message:
        "Simulation Started"

    });


};



exports.stop=async(req,res)=>{


    simulator.stopSimulation();


    res.json({

        message:
        "Simulation Stopped"

    });


};



exports.status=async(req,res)=>{


    res.json({

        running:
        simulator.status(),


        spacecraft:
        getState()

    });


};