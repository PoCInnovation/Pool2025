/*
**   SOFTWARE Pool 2024 - Day 2 - Morning
**   Music Database
**   Made with <3 by PoC
*/

import { MongoClient } from 'mongodb';
import * as fs from "fs";

// Remember always getting the url from a .env, this is an example but in real life we always store the credentials in a safer place.
const url = 'mongodb://admin:pass@localhost:27017';
const dbName = 'poc-mongo-db';
const client = new MongoClient(url);
const resources = JSON.parse(fs.readFileSync('resources.json', 'utf8'));

const createData = async (artistsCollection, musicsCollection) => {
    await artistsCollection.insertMany(resources.artists);
    await musicsCollection.insertMany(resources.musics);
    console.log('Data inserted successfully');
}

async function run() {
    try {
        await client.connect();
        console.log('Connected to the database');
        const db = client.db(dbName);
        console.log('Created database with name ' + dbName);
        const artistsCollection = db.collection('artists');
        const musicsCollection = db.collection('musics');

        await createData(artistsCollection, musicsCollection);
    } finally {
        await client.close();
        console.log('Connection closed');
    }
}

run().catch(console.error);
