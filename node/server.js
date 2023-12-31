var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');

http.createServer(function(req, res){

    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);
    });
}
    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
	totalUptime = os.uptime();
	hours = Math.floor(totalUptime / 3600);
        minutes = Math.floor((totalUptime % 3600) / 60);
        seconds = Math.floor(totalUptime % 60);
        uptimeString = `${hours} hrs ${minutes} mins ${seconds} sec`;    
	totalMem = os.totalmem() / (1024 * 1024);
	freeMem = os.freemem() / (1024 * 1024);
	CPUs = os.cpus().length;
        html=`    
        <!DOCTYPE html>
        <html>
          <head>
            <title>Node JS Response</title>
          </head>
          <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: ${uptimeString}</p>
            <p>Total Memory: ${totalMem} Mb</p>
            <p>Free Memory: ${freeMem} Mb</p>
            <p>Number of CPUs: ${CPUs}</p>            
          </body>
        </html>` 
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }
}).listen(3000);

console.log("Server listening on port 3000");
