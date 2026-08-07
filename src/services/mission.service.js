const Mission = require("../models/Mission");

const createMission = async (data) => {
  return await Mission.create(data);
};

const getAllMissions = async () => {
  return await Mission.find().sort({ createdAt: -1 });
};

const getMissionById = async (id) => {
  return await Mission.findById(id);
};

const updateMission = async (id, data) => {
  return await Mission.findByIdAndUpdate(id, data, {
    new: true,
  });
};

const deleteMission = async (id) => {
  return await Mission.findByIdAndDelete(id);
};

module.exports = {
  createMission,
  getAllMissions,
  getMissionById,
  updateMission,
  deleteMission,
};
