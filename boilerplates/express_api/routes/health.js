const router = require("express").Router();

router.get("/health", (req, res) => {
    res.json({ status: "ok", service: "express-api" });
});

module.exports = router;
