from flask import Blueprint, jsonify

api = Blueprint("api", __name__)


@api.route("/api")
def index():
    endpoints = {"/api": "List of all endpoints", "/api/health-check": "Returns status"}
    return jsonify(endpoints)


@api.route("/api/health-check")
def health_check():
    return jsonify({"status": "OK"})
