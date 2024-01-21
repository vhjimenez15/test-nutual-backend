from app import db
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.avm.models import AVM
from app.avm.schemas import AVMSchema
from app.avm.helper import helper_create_avm

avmBp = Blueprint('avm', __name__)


# get one element id
@avmBp.route("/avm/list/<id>", methods=['GET'])
@jwt_required()
def list_one_avm(id):
    avm_object = AVM.query.get(id)
    schema = AVMSchema()
    return jsonify(
        {
            'message': 'Successful',
            'data': schema.dump(avm_object)
        }
    )


# filter elements
@avmBp.route("/avm/list", methods=['GET'])
@jwt_required()
def list_avm():
    avm_objects = AVM.query.order_by(AVM.city).all()
    schemas = AVMSchema(many=True)
    return jsonify(
        {
            'message': 'Successful',
            'data': schemas.dump(avm_objects)
        }
    )


# create element
@avmBp.route("/avm/create", methods=['POST'])
@jwt_required()
def create_avm():
    try:
        data = request.json
        data = helper_create_avm(data)
        schema = AVMSchema()
        new_element = AVM(**schema.dump(data))
        db.session.add(new_element)
        db.session.commit()
        return jsonify({'message': 'Successful'})
    except Exception:
        return jsonify({'message': 'Error in data create'})


# update element
@avmBp.route("/avm/update/<id>", methods=['PUT'])
@jwt_required()
def update_avm(id):
    data = request.json
    avm_object = AVM.query.get(id)
    if not avm_object:
        return jsonify({'message': f'Id {id} not found'}), 400
    schema = AVMSchema(partial=True)
    AVM.query.filter_by(id=id).update(schema.dump(data))

    db.session.commit()
    return jsonify({'message': 'Successful'})


# delete element
@avmBp.route("/avm/delete/<id>", methods=['DELETE'])
@jwt_required()
def delete_avm(id):
    avm_object = AVM.query.get(id)
    if not avm_object:
        return jsonify({'message': f'Id {id} not found'}), 400
    db.session.delete(avm_object)
    db.session.commit()
    return jsonify({'message': 'Successful'})


# filter elements
@avmBp.route("/avm/m2", methods=['GET'])
@jwt_required()
def list_m2_avm():
    args = request.args
    city = args.get('city')
    avm_objects = []
    m2_prom = 0
    if city:
        avm_objects = AVM.query.order_by(
            AVM.city).filter(AVM.city.like(f"%{city}%"))
        area_all = [item.total_area for item in avm_objects]
        len_items = len(area_all)
        if len_items > 0:
            m2_prom = sum(area_all)/len_items
    schemas = AVMSchema(many=True)
    return jsonify(
        {
            'message': 'Successful',
            'data': {
                'mean_m2': round(m2_prom, 2),
                'items': schemas.dump(avm_objects)
            }
        }
    )
