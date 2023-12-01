// Defines the routes for the sede API

// Import sede model
const Sede = require('./sede');
const express = require('express');
const router = express.Router();
const collection = require('./index');
const request = require('request');
module.exports = router;


// IP DEL BROKER:
let kong_ip = "10.128.0.22:8000"


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

    // check the existence of the doctors in the doctors service
    let doctors = await getDoctors();
    // turns the doctors json into an array
    doctors = doctors["profesionales"]

    for (let i = 0; i < sede.medics.length; i++) {
        if (!doctors.includes(sede.medics[i])) {
            console.log("El doctor " + sede.medics[i] + " no existe");
            console.log("Registrando sede fallido");
            res.status(400).json({ message: "El doctor " + sede.medics[i] + " no existe" });
            break;
        }
    }

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
        // only get the last 5 elements of the array if its length is greater than 5
        if (sedes.length > 5) {
            sedes = sedes.slice(sedes.length - 5, sedes.length);
        }
        res.json(sedes);
        console.log("Sedes consultadas");
    } catch (err) {
        res.status(500).json({ message: err.message });
        console.log("Error al consultar sedes");
    }
});

// Get all doctors from the doctors service
// this is a support function to get the doctors from the doctors service
// and to check the existence of the doctors in the doctors service
function getDoctors() {
    return new Promise((resolve, reject) => {
        console.log("Consultando doctores...");
        request.get('http://' + kong_ip + '/postAllDoctors', (err, res, body) => {
            if (err) {
                reject(err);
            }
            resolve(JSON.parse(body));
            console.log("Se encontraron", JSON.parse(body)["profesionales"].length, "doctores");
        }
        )
    })
}


// get all doctors from a sede
router.get('/:id/doctors', async (req, res) => {
    console.log("Consultando doctores de la sede...");
    try {
        const sede = await collection.findOne({ _id: req.params.id });
        let doctors = await getDoctors();
        let sedeDoctors = [];
        // check if the doctor id is in the sede doctors array
        for (let i = 0; i < doctors.length; i++) {
            if (sede.medics.includes(doctors[i].id)) {
                sedeDoctors.push(doctors[i]);
            }
        }
        res.json(sedeDoctors);
        console.log("Doctores de la sede consultados");
    } catch (err) {
        res.status(500).json({ message: err.message });
        console.log("Error al consultar doctores de la sede");
    }
});


// Health check endpoint
router.get('/health-check/', (req, res) => {
    res.status(200).json({ status: 'ok' });
    console.log("Health check ok");
});