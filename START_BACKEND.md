# How to Start the Backend Server

## The Problem

The brand logos and banners are not loading because the Flask backend API server is not running. The frontend is trying to fetch data from `http://localhost:5000/api` but getting network errors.

## Solution

You need to start the Flask backend server. Follow these steps:

### Step 1: Install Python Dependencies

Open a terminal and run:

```bash
cd backend
pip install -r requirements.txt
```

If `pip` doesn't work, try:
```bash
pip3 install -r requirements.txt
```

Or with python directly:
```bash
python -m pip install -r requirements.txt
```

Or:
```bash
python3 -m pip install -r requirements.txt
```

### Step 2: Seed the Database (First Time Only)

This populates the MongoDB database with initial brand and product data:

```bash
python seed_data.py
```

Or:
```bash
python3 seed_data.py
```

### Step 3: Start the Backend Server

```bash
python app.py
```

Or:
```bash
python3 app.py
```

The server should start on `http://localhost:5000`

You should see output like:
```
 * Running on http://0.0.0.0:5000
 * Running on http://127.0.0.1:5000
```

### Step 4: Keep the Server Running

Keep this terminal window open and the server running. The frontend (running on port 5173) will now be able to fetch brand and product data from the backend.

## Verify It's Working

1. Open http://localhost:5000/api/health in your browser
2. You should see: `{"database":"connected","status":"healthy"}`
3. Open http://localhost:5000/api/brands to see the brands data with logo_url and banner_url fields

## Troubleshooting

### Port Already in Use
If you get an error that port 5000 is already in use:

**On Linux/Mac:**
```bash
lsof -ti:5000 | xargs kill -9
```

**On Windows:**
```cmd
netstat -ano | findstr :5000
taskkill /PID <PID_NUMBER> /F
```

### Python Not Found
Make sure Python 3 is installed:
```bash
python3 --version
```

If not installed, download from https://python.org

### Module Not Found Errors
If you get `ModuleNotFoundError`, make sure you ran step 1 to install dependencies.

## Alternative: Run in Background

**On Linux/Mac:**
```bash
cd backend
nohup python3 app.py > backend.log 2>&1 &
```

**On Windows:**
Use a separate terminal window or install a process manager like `pm2` or `forever`.
