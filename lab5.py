from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, session, render_template, request, redirect
import psycopg2

lab5 = Blueprint("lab5", __name__)