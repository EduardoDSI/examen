from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_geek():
      return '''
      <!DOCTYPE html>
      <html lang="es">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Mi Perfil</title>
          <style>
              body {
                  font-family: Arial, sans-serif;
                  margin: 0;
                  padding: 0;
                  background-color: #f0f0f0;
              }

              .perfil {
                  width: 80%;
                  max-width: 600px;
                  margin: 50px auto;
                  background-color: #fff;
                  padding: 20px;
                  border-radius: 8px;
                  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                  text-align: center;
              }

              img {
                  width: 150px;
                  height: 150px;
                  border-radius: 50%;
                  margin-bottom: 20px;
              }

              h1 {
                  color: #333;
              }

              p {
                  color: #666;
              }

              ul {
                  list-style: none;
                  padding: 0;
              }

              li {
                  margin-bottom: 10px;
              }

              button {
                  background-color: #007bff;
                  color: #fff;
                  padding: 10px 20px;
                  border: none;
                  border-radius: 5px;
                  cursor: pointer;
                  font-size: 16px;
                  margin-top: 20px;
              }

              button:hover {
                  background-color: #0056b3;
              }
          </style>
      </head>
      <body>
          <div class="perfil">
              <img src="https://cdn-icons-png.flaticon.com/512/3135/3135768.png" alt="Tu Foto">
              <h1>John Doe</h1>
              <p>CEO & Founder, Example</p>
              <ul>
                  <li>Hardvard University</li>
              </ul>
              <button>Contact</button>
          </div>
      </body>
      </html>
      '''

if __name__ == "__main__":
   app.run(debug=True)
