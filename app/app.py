import bcrypt
import dotenv import load_dotenv
import os
import jwt 

load_dotenv() 

from flask import Flask, request, jsonify, request, g
from flask_cors import CORS
from auth_middleware import token_required
import psycopg2, psycopg2.extras


app = Flask(__name__)
CORS(app)

def get_db_connection():