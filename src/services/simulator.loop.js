const {
    checkTelemetry
} = require("./alert.engine");

const {
    updateState,
    getState
}
=require("./digitalTwin");


const {
    getIO
}
=require("../config/socket");


const {
    generateTelemetry
}
=require("./telemetryGenerator");



let running=false;

let interval;



function startSimulation(){


    if(running)
        return;



    running=true;



    interval=setInterval(async()=>{


        updateState();



        const telemetry =
await generateTelemetry();

await checkTelemetry(telemetry);

getIO().emit(
    "telemetry",
    telemetry
);



        if(getIO()){


            getIO()
            .emit(
                "telemetry",
                telemetry
            );


        }



    },1000);


}




function stopSimulation(){


    running=false;


    clearInterval(interval);


}



function status(){

    return running;

}



module.exports={

startSimulation,

stopSimulation,

status

};