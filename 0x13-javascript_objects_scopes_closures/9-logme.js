#!/usr/bin/node
let count = 0;
/* <number arguments already printed>: <current argument value> */
exports.logMe = function (value) { 
	console.log(`${count++}: ${value}`);
};
