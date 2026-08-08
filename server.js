const path = require('path');
const express = require('express');
// ... other requires

const app = express();
app.use(express.json());
app.use(express.static(path.join(__dirname, 'templates')));

// ... your routes ...

app.listen(3000, () => console.log('Secure Mission IdP API Gateway running on port 3000'));