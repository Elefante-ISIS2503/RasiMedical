// Defines the routes for the sede API

// Import sede model
const Sede = require('./sede');
const express = require('express');
const router = express.Router();
const collection = require('./index');
module.exports = router;

// Create a sede
router.post('/', async (req, res) => {
    console.log("Registrando sede...");
    console.log(req.body);

    // Create a new sede
    const sede = new Sede({
        name: req.body.name,
        address: req.body.address,
        city: req.body.city,
        medics: req.body.medics,
        phone: req.body.phone
    });

    // Save sede in the database
    try {
        const newSede = await collection.insertOne(sede);
        res.status(201).json(newSede);
        console.log("Sede registrada");
    } catch (err) {
        res.status(400).json({ message: err.message });
        console.log("Error al registrar sede");
    }
});

// Get all sedes
router.get('/', async (req, res) => {
    console.log("Consultando sedes...");
    try {
        const sedes = await collection.find().toArray();
        res.json(sedes);
        console.log("Sedes consultadas");
    } catch (err) {
        res.status(500).json({ message: err.message });
        console.log("Error al consultar sedes");
    }
});


// Health check endpoint
router.get('/health-check/', (req, res) => {
    res.status(200).json({ status: 'ok' });
    console.log("Health check ok");
});