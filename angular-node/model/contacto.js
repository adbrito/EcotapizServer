
var express = require('express');


var router = express.Router();


class ContactoModel
{
	constructor(name, email, mensaje)
	{
		
		this.name = name;
		
		this.email = email;
		
		this.mensaje = mensaje;
	}

	
}

module.exports = ContactoModel;

//export default ContactoModel;