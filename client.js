
let argumentos = process.argv.slice(3)
let temp = []
if(argumentos.length !== 0)
    temp = argumentos

let objeto = {
    nombre: temp[0],
    descripcion: temp[1],
    glb: temp[2],
    imagen: temp[3],
    ranking: temp[4]
}

const data = JSON.stringify({
    objeto

});

console.log(objeto.nombre)
console.log(objeto.descripcion)
console.log(objeto.glb)
console.log(objeto.imagen)
console.log(objeto.ranking)


const options = {
    hostname: "localhost",
    port: '8000',
    method: process.argv[2],
    path: "/auto/",
    body: data
};

if(process.argv[2] !== undefined){
    const http = require("http")

    const req = http.request(options, (res) => {
        let data = '';
        res.on('data', (chunk) => {
            data += chunk;
        });

        res.on('end', () => {
            console.log('Status Code:', res.statusCode);
            if (data.length === 0)
                data += "No hay datos en la lista de objetos en el servidor!!!, utilice post para agregar objetos en el servidor"
            console.log(data);
        });

    }).on("error", (err) => {
        console.log("Error: ", err.message);
    });

    req.write(data);
    req.end();
} else {
    console.log("Digite el comando a utilizar, como GET o POST")
}


//const options = new URL(baseUrl);
/*
if(argumentos.length == 0){
    http.get(
        options,
        res => {
            let data = ''

            res.on('data', (chunk) => {
                data += chunk;
            });
            res.on('end', () => {
                console.log("Status code: " + res.statusCode)
                console.log(data);
            });

        }
    )
    .end()
} else {
    const data = {
        atributos: argumentos
    };
    axios.post(options, data)
    .then((res) => {
        console.log(`Status: ${res.status}`);
        console.log('Body: ', res.data);
    }).catch((err) => {
        console.error(err);
    });
}
*/

