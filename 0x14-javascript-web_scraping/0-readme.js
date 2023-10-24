#!/usr/bin/node

const fs = require('fs');
const file_name = process.argv[2];

fs.readFile(file_name, 'utf8', (err, data) => {
	if (err) {
		console.error(err);
	}
	else {
		console.log(data)
	}
});
