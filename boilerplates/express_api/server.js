const express = require("express");
const cors = require("cors");
require("dotenv").config();

const healthRoute = require("./routes/health");

const app = express();
app.use(cors());
app.use(express.json());

app.use("/api", healthRoute);

const PORT = process.env.PORT || 4000;
app.listen(PORT, () => {
    console.log(`Express API running on port ${PORT}`);
});
