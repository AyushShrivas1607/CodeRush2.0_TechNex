const { Server } = require("socket.io");

let io;

const initializeSocket = (server) => {
  io = new Server(server, {
    cors: {
      origin: process.env.CLIENT_URL,
      methods: ["GET", "POST"],
    },
  });

  io.on("connection", (socket) => {
    console.log(`✅ Client Connected: ${socket.id}`);

    socket.on("joinMission", (missionId) => {
      socket.join(missionId);

      console.log(`${socket.id} joined room ${missionId}`);

      socket.emit("joinedMission", {
        success: true,
        missionId,
      });
    });

    socket.on("leaveMission", (missionId) => {
      socket.leave(missionId);

      console.log(`${socket.id} left room ${missionId}`);
    });

    socket.on("disconnect", () => {
      console.log(`❌ Client Disconnected: ${socket.id}`);
    });
  });
};

const getIO = () => io;

module.exports = {
  initializeSocket,
  getIO,
};