from flask import Blueprint, request, jsonify
from init import db
from models.social_share import SocialShare

social_share_bp = Blueprint('social_shares', __name__, url_prefix='/social_shares')

@social_share_bp.route('/', methods=['POST'])
def create_social_share():
    user_id = request.json['user_id']
    workout_id = request.json['workout_id']
    shared_on = request.json['shared_on']

    new_social_share = SocialShare(user_id=user_id, workout_id=workout_id, shared_on=shared_on)
    db.session.add(new_social_share)
    db.session.commit()

    return jsonify({
        "id": new_social_share.id,
        "user_id": new_social_share.user_id,
        "workout_id": new_social_share.workout_id,
        "shared_on": new_social_share.shared_on
    })

@social_share_bp.route('/', methods=['GET'])
def get_social_shares():
    social_shares = SocialShare.query.all()
    result = []
    for social_share in social_shares:
        result.append({
            "id": social_share.id,
            "user_id": social_share.user_id,
            "workout_id": social_share.workout_id,
            "shared_on": social_share.shared_on
        })
    return jsonify(result)

@social_share_bp.route('/<int:id>', methods=['GET'])
def get_social_share(id):
    social_share = SocialShare.query.get(id)
    return jsonify({
        "id": social_share.id,
        "user_id": social_share.user_id,
        "workout_id": social_share.workout_id,
        "shared_on": social_share.shared_on
    })

@social_share_bp.route('/<int:id>', methods=['PUT'])
def update_social_share(id):
    social_share = SocialShare.query.get(id)

    user_id = request.json['user_id']
    workout_id = request.json['workout_id']
    shared_on = request.json['shared_on']

    social_share.user_id = user_id
    social_share.workout_id = workout_id
    social_share.shared_on = shared_on

    db.session.commit()

    return jsonify({
        "id": social_share.id,
        "user_id": social_share.user_id,
        "workout_id": social_share.workout_id,
        "shared_on": social_share.shared_on
    })

@social_share_bp.route('/<int:id>', methods=['DELETE'])
def delete_social_share(id):
    social_share = SocialShare.query.get(id)
    db.session.delete(social_share)
    db.session.commit()

    return jsonify({
        "message": "Social share deleted"
    })
