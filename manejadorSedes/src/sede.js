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
    city: String
});

// compile the model
const Sede = mongoose.model('Sede', sedeSchema);

// export the model
module.exports = Sede;