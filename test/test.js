assert = require('assert');

hasher = require('../hasher');

tests = require('./tests.json');

tests.forEach(function(t){
	console.log(t.data, t.options);
	assert.equal(hasher.hash("md5",t.data,t.options),t.md5sum);
	assert.equal(hasher.hash("sha1",t.data,t.options),t.sha1sum);
	assert.equal(hasher.hash("sha256",t.data,t.options),t.sha256sum);
	assert.equal(hasher.hash("sha512",t.data,t.options),t.sha512sum);
});