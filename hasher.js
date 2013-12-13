var crypto = require('crypto');
var _ = require('lodash');
var util = require('util');

var hash = function(hash_type,data,options){
	if (!options) {		
		options = {}
	}
	_.defaults(options,{
		"sort_keys": true,
		"sort_arrays": false,
	});	
	var h = crypto.createHash(hash_type);

	s = "";
	if(_.isArray(data)){
		if (options.sort_arrays) {
			data.sort();
		}
		data.forEach(function(i){
			s += hash(hash_type,i,options);
		})
	} else if (_.isString(data)){
		s = data;
	} else if (_.isNumber(data)) {
		s = util.format("%d",data);
	} else if (_.isPlainObject(data)) {
		var ks = _.keys(data);
		if(options.sort_keys) {
			ks.sort();
		}
		ks.forEach(function(k){
			s += k + hash(hash_type,data[k],options);
		})
	} else {
		console.log(typeof data);
	}

	return h.update(s).digest('hex');;
}

module.exports.hash = hash;