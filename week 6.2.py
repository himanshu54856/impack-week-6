# MongoDB is a document database used to build highly available aand scalable internet application .A non-relational database is a databse that doed not use the tabulatr schema of rows and columns found in most traditional databse eyetems.Mongo Db is faster and more scalable .
'''It is non relational and document-oriented database.
   it has dynamic schema.
   it is much faster than RDBMS.
   it contains heterogeneous data
   it provide great flexibility to the field in the documents.'''


# CONNECTING TO MongoDB from python -

cons MongoClient =require('mongodb').MongoClient:
cons assert = require('assert');
//connection URL
const url='mongodb':
//Database Name
const dbname='myproject':
MongoClient.connect(url,function(err,client){
    assert.equal(null,err):
    consol.log("connected successfully to server ");
    const db = client.db(dbName);
    client.close():
})