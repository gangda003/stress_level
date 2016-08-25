/*
 * Module Dependencies
 */
var express = require('express');
var httpProxy = require('http-proxy');



var apiForwardingUrl = 'http://localhost:4010';



//******** The root directory of this /app
var server = express();
server.set('port', 3000);
server.use(express.static(__dirname + '/app'));




var apiProxy = httpProxy.createProxyServer();

console.log('Forwarding API requests to ' + apiForwardingUrl);


// Grab all requests to the server with "/space/".
server.all("/space/*", function(req, res) {
    apiProxy.web(req, res, {target: apiForwardingUrl});
});

server.listen(server.get('port'), function() {
    console.log('Express server listening on port ' + server.get('port'));
});