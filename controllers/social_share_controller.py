from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from init import db
from models.social_share import SocialShare, social_share_schema, social_shares_schema

social_shares_bp = Blueprint('social_share', __name__, url_prefix='/social_shares')

@social_shares_bp.route('/', methods=["GET"])
def get_all_social_shares():
    social_shares = SocialShare.query.all()
    return social_shares_schema.jsonify(social_shares)

@social_shares_bp.route('/<int:social_share_id>', methods=["GET"])
def get_one_social_share(social_share_id):
    social_share = SocialShare.query.get(social_share_id)
    if social_share:
        return social_share_schema.jsonify(social_share)
    else:
        return jsonify({"error": f"Social Share with id {social_share_id} not found"}), 404

@social_shares_bp.route('/', methods=["POST"])
@jwt_required()
def create_social_share():
    body_data = request.get_json()
    share_date = body_data.get('share_date')
    share_message = body_data.get('share_message')
    workout_id = body_data.get('workout_id')
    user_id = get_jwt_identity()

    new_social_share = SocialShare(
        share_date=share_date,
        share_message=share_message,
        workout_id=workout_id,
        user_id=user_id
    )

    db.session.add(new_social_share)
    db.session.commit()

    return social_share_schema.jsonify(new_social_share), 201

@social_shares_bp.route('/<int:social_share_id>', methods=["PUT"])
@jwt_required()
def update_social_share(social_share_id):
    social_share = SocialShare.query.get(social_share_id)
    if not social_share:
        return jsonify({"error": f"Social Share with id {social_share_id} not found"}), 404

    body_data = request.get_json()
    share_date = body_data.get('share_date')
    share_message = body_data.get('share_message')

    social_share.share_date = share_date if share_date else social_share.share_date
    social_share.share_message = share_message if share_message else social_share.share_message

    db.session.commit()

    return social_share_schema.jsonify(social_share)

@social_shares_bp.route('/<int:social_share_id>', methods=["DELETE"])
@jwt_required()
def delete_social_share(social_share_id):
    social_share = SocialShare.query.get(social_share_id)
    if not social_share:
        return jsonify({"error": f"Social Share with id {social_share_id} not found"}), 404

    db.session.delete(social_share)
    db.session.commit()

    return jsonify({"message": f"Social Share with id {social_share_id} has been deleted"}), 200



