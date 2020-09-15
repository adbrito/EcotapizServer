var express = require('express');
var router = express.Router();
var ContactoService = require('../services/contactoS');
var envio= require('../services/envio_correo.js');
//import { envio_correo } from '../services/envio_correo.js';



router.get('/', function(req, res, next) {
  res.json('hola');
});

router.post('/',async(req,res,next)=>{
	const body=req.body;
	//console.log("el body",body);

	try{
		const contacto= await ContactoService.create(body);
		//console.log("contacto:",contacto);
		envio(contacto);
		//envio_correo(contacto);
		return res.status(201).json({contacto:contacto});
	}
	catch(err){

		console.log("hay error",err)
		return res.status(400).json({error: err.message});
	}


});


module.exports = router;
