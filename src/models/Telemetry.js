const mongoose = require("mongoose");

const telemetrySchema = new mongoose.Schema(
  {
    missionId: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "Mission",
      required: true,
    },

    battery: {
      type: Number,
      required: true,
      min: 0,
      max: 100,
    },

    fuel: {
      type: Number,
      required: true,
      min: 0,
      max: 100,
    },

    temperature: {
      type: Number,
      required: true,
    },

    voltage: {
      type: Number,
      required: true,
    },

    velocity: {
      type: Number,
      required: true,
    },

    altitude: {
      type: Number,
      required: true,
    },

    signalStrength: {
      type: Number,
      required: true,
      min: 0,
      max: 100,
    },

    solarPanelOutput: {
      type: Number,
      required: true,
    },

    thrusterStatus: {
      type: String,
      enum: ["ACTIVE", "IDLE", "OFF"],
      default: "IDLE",
    },

    anomalyDetected: {
      type: Boolean,
      default: false,
    },

    timestamp: {
      type: Date,
      default: Date.now,
    },
  },
  {
    timestamps: true,
  }
);

module.exports = mongoose.model("Telemetry", telemetrySchema);