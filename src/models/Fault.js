const mongoose=require("mongoose");


const faultSchema=
new mongoose.Schema({

    type:{
        type:String,
        required:true
    },


    status:{
        type:String,
        default:"ACTIVE"
    },


    description:String,


    createdAt:{
        type:Date,
        default:Date.now
    },


    resolvedAt:Date


});


module.exports=
mongoose.model(
"Fault",
faultSchema
);