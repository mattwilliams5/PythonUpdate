import hashlib
import secrets
from flask import Blueprint, jsonify, abort, request
from ..models import Tweet, User, db


def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


def valiate_user(username, password):
    if 'username' not in request.json or 'password' not in request.json:
        return abort(400)
    if len(request.json["username"]) <= 3 or len(request.json["password"]) < 8:
        return abort(400)


bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    users = User.query.all()  # ORM performs SELECT query
    result = []
    for u in users:
        result.append(u.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    u = User.query.get_or_404(id)
    return jsonify(u.serialize())


@bp.route('', methods=['POST'])
def create():
    # req body must contain user_id and content
    valiate_user(request.json['username'], password=request.json['password'])

    # construct User
    u = User(
        username=request.json['username'],
        password=request.json['password']
    )
    u.password = scramble(u.password)

    db.session.add(u)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(u.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    u = User.query.get_or_404(id)
    try:
        db.session.delete(u)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)


@bp.route('/<int:id>', methods=['PUT'])
def update(id: int):
    u = User.query.get_or_404(id)
    valiate_user(username=request.json['username'],
                 password=request.json['password'])

    u.username = request.json['username']
    u.password = scramble(request.json['password'])
    db.session.commit()  # execute CREATE statement
    return jsonify(u.serialize())


@bp.route('/<int:id>/liked_tweets', methods=['GET'])
def liked_tweets(id: int):
    u = User.query.get_or_404(id)
    result = []
    print(u.liked_tweets)
    for u in u.liked_tweets:
        result.append(u.serialize())
    return jsonify(result)
