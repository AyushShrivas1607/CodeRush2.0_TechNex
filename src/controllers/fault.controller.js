const Fault=
require("../models/Fault");


const engine=
require("../services/faultEngine");


const {
getIO
}
=require("../config/socket");



exports.inject=
async(req,res)=>{


try{


const {
type,
description
}=req.body;



const fault=
await Fault.create({

    type,

    description

});



engine.addFault(type);



getIO()
.emit(
"faultInjected",
fault
);



res.json({

message:
"Fault injected",

fault

});



}
catch(error){

res.status(500)
.json({
error:error.message
});

}


};





exports.reset=
async(req,res)=>{


const {
type
}=req.body;



engine.removeFault(type);



await Fault.findOneAndUpdate(

{
type,
status:"ACTIVE"
},

{
status:"RESOLVED",
resolvedAt:new Date()
}

);



getIO()
.emit(
"faultResolved",
type
);



res.json({

message:
"Fault removed"

});


};

exports.active=
(req,res)=>{

res.json(

engine.getActiveFaults()

);

};