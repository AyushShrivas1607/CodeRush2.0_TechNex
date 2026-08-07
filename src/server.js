require("dotenv").config();

const http = require("http");

const app = require("./app");

const connectDB = require("./config/db");

const { initializeSocket } = require("./config/socket");

const PORT = process.env.PORT || 5000;

connectDB();

const server = http.createServer(app);

initializeSocket(server);

server.listen(PORT, () => {

    console.log(`🚀 Server Running on Port ${PORT}`);

});