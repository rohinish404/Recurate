const chokidar = require('chokidar');
const http = require('http');
const { WebSocket, WebSocketServer } = require('ws');

const server = http.createServer();
const wss = new WebSocketServer({ server });


wss.on('connection', (ws) => {
   console.log('Client connected');
});

server.listen(8080, () => {
  console.log('WebSocket server is running on http://localhost:8080');
});

const watcher = chokidar.watch('.', {
  ignored: /node_modules/,
  persistent: true
});

watcher.on('change', (path) => {
  console.log(`File ${path} has been changed`);
  wss.clients.forEach((client) => {
    client.send('reload');
  });
});
