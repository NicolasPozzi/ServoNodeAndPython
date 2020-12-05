const Gpio = require('pigpio').Gpio;

const motor = new Gpio(17, {mode: Gpio.OUTPUT});

let pulseWidth = 1000;
let increment = 1000;

setInterval(() => {
  motor.servoWrite(pulseWidth);

  pulseWidth += increment;
  if (pulseWidth >= 3000) {
    increment = -1000;
  } else if (pulseWidth <= 100) {
    increment = 1000;
  }
}, 1000);