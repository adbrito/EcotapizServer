//import {contactoC} from '../model/contacto.js';
//const {ContactoModel} = require("class");
//import ContactoModel from '../model/ContactoModel';
const ContactoModel = require('../model/contacto.js');
var express = require('express');

class ContactoService
{
	static create(data)
	{
						//console.log(data.name,data.email,data.mensaje);

		let contacto = new ContactoModel(data.name,  data.email, data.mensaje);


		//console.log(contacto);
				//console.log(contacto.name,contacto.email,contacto.mensaje);



		return contacto;
	}
}


module.exports = ContactoService;
