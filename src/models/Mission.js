const mongoose = require("mongoose");

const missionSchema = new mongoose.Schema(
  {
    missionName: {
      type: String,
      required: true,
      trim: true,
    },

    spacecraft: {
      type: String,
      required: true,
    },

    orbitType: {
      type: String,
      enum: ["LEO", "MEO", "GEO", "HEO"],
      default: "LEO",
    },

    missionDuration: {
      type: Number,
      required: true,
    },

    status: {
      type: String,
      enum: ["PLANNED", "RUNNING", "COMPLETED", "FAILED"],
      default: "PLANNED",
    },

    createdBy: {
      type: String,
      default: "Operator",
    },
  },
  {
    timestamps: true,
  }
);

module.exports = mongoose.model("Mission", missionSchema);