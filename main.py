
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Api_web")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="id">
    <head>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Api_web</title>
      <style>
        body {
          background: #101827;
          color: white;
          font-family: Arial, sans-serif;
          text-align: center;
          padding: 50px 16px;
        }
        .card {
          max-width: 420px;
          margin: auto;
          padding: 24px;
          background: #1e293b;
          border-radius: 16px;
        }
        a { color: #67e8f9; }
      </style>
    </head>
    <body>
      <div class="card">
        <h1>Api_web 🚀</h1>
        <p>Website berhasil online!</p>
        <p><a href="/api">Tes API</a></p>
        <p><a href="/docs">Dokumentasi API</a></p>
      </div>
    </body>
    </html>
    """

@app.get("/api")
def api():
    return {
        "status": "success",
        "message": "API berhasil berjalan!"
    }

@app.get("/health")
def health():
    return {"status": "ok"}
