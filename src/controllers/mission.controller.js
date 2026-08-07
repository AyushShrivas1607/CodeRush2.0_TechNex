const missionService = require("../services/mission.service");
const socketService = require("../services/socket.service");
exports.createMission = async (req, res) => {
  try {
    const mission = await missionService.createMission(req.body);

    // Notify all connected clients
    socketService.emitMissionUpdate(mission._id.toString(), {
      type: "MISSION_CREATED",
      mission,
    });

    res.status(201).json({
      success: true,
      data: mission,
    });
  } catch (err) {
    res.status(500).json({
      success: false,
      message: err.message,
    });
  }
};

exports.getAllMissions = async (req, res) => {
  try {
    const missions = await missionService.getAllMissions();

    res.json({
      success: true,
      data: missions,
    });
  } catch (err) {
    res.status(500).json({
      success: false,
      message: err.message,
    });
  }
};

exports.getMissionById = async (req, res) => {
  try {
    const mission = await missionService.getMissionById(req.params.id);

    if (!mission) {
      return res.status(404).json({
        success: false,
        message: "Mission not found",
      });
    }

    res.json({
      success: true,
      data: mission,
    });
  } catch (err) {
    res.status(500).json({
      success: false,
      message: err.message,
    });
  }
};

exports.updateMission = async (req, res) => {
  try {
    const mission = await missionService.updateMission(
      req.params.id,
      req.body
    );

    res.json({
      success: true,
      data: mission,
    });
  } catch (err) {
    res.status(500).json({
      success: false,
      message: err.message,
    });
  }
};

exports.deleteMission = async (req, res) => {
  try {
    await missionService.deleteMission(req.params.id);

    res.json({
      success: true,
      message: "Mission deleted successfully",
    });
  } catch (err) {
    res.status(500).json({
      success: false,
      message: err.message,
    });
  }
};