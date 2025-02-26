const express = require ('express')

const server = express();

//localhost: 3000/cursos
server.get('/cursos', (req, res) =>{

    return res.json({ cursos : "Node Js"})
})

server.listen(3000)