
// import mongo
const { MongoClient, ServerApiVersion } = require('mongodb');

// import express
const express = require('express');

// url de conexion a la base de datos
const uri = "mongodb+srv://SedeUsername:SedePassword@sedecuster.kdog3dc.mongodb.net/?retryWrites=true&w=majority";

// Create a MongoClient with a MongoClientOptions object to set the Stable API version
const client = new MongoClient(uri, {
    serverApi: {
        version: ServerApiVersion.v1,
        strict: true,
        deprecationErrors: true,
    }
});

// Connect to the MongoDB cluster
async function run() {

    // Connect the client to the server	(optional starting in v4.7)
    await client.connect();
    // Send a ping to confirm a successful connection
    await client.db("admin").command({ ping: 1 });
    console.log("Successfully connected to MongoDB!");

}

console.log("Connecting to MongoDB... Please wait...")

// Connect to MongoDB cluster
run().catch(console.dir);

// defines the db and collection
const db = client.db("SedeDB");
const collection = db.collection("Sedes");

// export the collection    
module.exports = collection;



// Create express app
const app = express();
const port = 8080;
app.use(express.json());


// Use sede routes in the App
app.use('/sedes', require('./sedeRoutes'));

// Start the express server
app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});

