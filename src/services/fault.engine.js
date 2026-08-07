const Fault=
require("../models/Fault");


let activeFaults=[];



function addFault(type){


    if(!activeFaults.includes(type)){

        activeFaults.push(type);

    }


}

function removeFault(type){


    activeFaults=
    activeFaults.filter(
        fault=>fault!==type
    );


}



function clearFaults(){


    activeFaults=[];


}



function getActiveFaults(){

    return activeFaults;

}




function applyFaults(spacecraft){



    activeFaults.forEach(
    fault=>{


        switch(fault){


            case "BATTERY_FAILURE":

                spacecraft.battery-=2;

                break;



            case "FUEL_LEAK":

                spacecraft.fuel-=5;

                break;



            case "OVERHEATING":

                spacecraft.temperature+=5;

                break;



            case "COMMUNICATION_LOSS":

                spacecraft.communication=false;

                break;



            case "SOLAR_FAILURE":

                spacecraft.solarPanel=false;

                break;



            case "THRUSTER_FAILURE":

                spacecraft.velocity+=
                Math.random()*50-25;

                break;



        }


    });



    return spacecraft;

}



module.exports={


addFault,

removeFault,

clearFaults,

getActiveFaults,

applyFaults

};