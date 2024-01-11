from flask import Flask, send_from_directory
import random

// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyDaU-LHpozaLTKqFpftegL0Wq18uqeIg1k",
  authDomain: "titan-software-beta.firebaseapp.com",
  databaseURL: "https://titan-software-beta-default-rtdb.firebaseio.com",
  projectId: "titan-software-beta",
  storageBucket: "titan-software-beta.appspot.com",
  messagingSenderId: "1004416146288",
  appId: "1:1004416146288:web:cd338a8694a1ba96b64db5"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);


app = Flask(__name__)

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)


@app.route("/rand")
def hello():
    return str(random.randint(0, 100))


if __name__ == "__main__":
    app.run(debug=True)
