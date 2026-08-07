const {
    applyFaults
}
=require("./faultEngine");

const spacecraft={


    missionStatus:"IDLE",


    battery:100,


    fuel:1000,


    temperature:25,


    altitude:420,


    velocity:7600,


    communication:true,


    solarPanel:true,


    thruster:true,


    timestamp:new Date()

};



function getState(){

    spacecraft.timestamp=new Date();

    return spacecraft;

}



function updateState(){


    spacecraft.battery-=0.05;


    spacecraft.fuel-=0.1;


    spacecraft.temperature +=
    Math.random()*0.5-0.2;



    spacecraft.altitude +=
    Math.random()*0.1-0.05;



    spacecraft.velocity +=
    Math.random()*2-1;



    applyFaults(spacecraft);



    spacecraft.timestamp=new Date();


}



function resetState(){

    spacecraft.battery=100;

    spacecraft.fuel=1000;

    spacecraft.temperature=25;

    spacecraft.altitude=420;

    spacecraft.velocity=7600;

}


module.exports={

    getState,

    updateState,

    resetState

};