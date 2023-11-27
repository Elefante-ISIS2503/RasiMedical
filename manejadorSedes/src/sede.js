// Defines a Sede model
// A sede has a name, address and city

const mongoose = require('mongoose');

// define the sede schema
const sedeSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    address: String,
    city: String,
    // Una sede tiene una lista de id's de medicos
    // Pero no existe una referencia a la coleccion de medicos
    medics: [String],
    phone: String

});

// compile the model
const Sede = mongoose.model('Sede', sedeSchema);

// export the model
module.exports = Sede;