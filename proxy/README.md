# Python API Proxy for Express
This project demonstrates a simple Python script acting as a proxy to forward requests from the script to an Express API. This can be useful for various purposes, such as adding an additional layer of security, logging requests, or modifying requests and responses.

## Getting Started
### Prerequisites
Make sure you have following installed

- Python 3.x

### Installation
1. Clone this repository
```bash
git clone https://github.com/nhatquang99/homebase-challenge.git
```
2. Navigate to the project directory
```bash
cd proxy
```
3. Run project
```bash
python3 proxy.py
```

### Configuration
1. Open `proxy.py`
2. Adjust the configuration variables:
  * EXPRESS_API_URL: Set the URL of your Express API.

## Testing
```bash
curl http://127.0.0.1:5001/api/users
```

This will be equivalent to making a request to `http://localhost:3000/users`.

