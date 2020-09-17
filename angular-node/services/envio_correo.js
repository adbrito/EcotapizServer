const nodeMailer = require('nodemailer');
const contacto = require('../model/contacto.js');

function enviar_correo(contacto){
let transporter = nodeMailer.createTransport({
            service: 'gmail',
            auth: {
                user: 'allibrito1@gmail.com',//process.env.EMAIL || 'abc@gmail.com', // TODO: your gmail account
                pass: 'Gmail2020'//process.env.PASSWORD || '1234' // TODO: your gmail password
            }
        });
        
        // Step 2
        let mailOptions = {
            from: "ecotapiz@hotmail.com", // TODO: email sender
           to: 'allibrito1@gmail.com', // TODO: email receiver
          subject: contacto.name +" le ha enviado un correo",
            text: "Se está tratando de comunicar con usted "+contacto.name+"\n\n\n Contenido del mensaje: "+contacto.mensaje+"\n\n"+
            "Correo proporcionado: "+ contacto.email+ " \n\nCorreo enviado desde la página de Ecotapiz\n"
        };
        
        // Step 3
        transporter.sendMail(mailOptions, (err, data) => {
            console.log(data);
            if (err) {
                return console.log('Error occurs');
            }
            return console.log('Email sent!!!');
        });
}


module.exports = enviar_correo;
