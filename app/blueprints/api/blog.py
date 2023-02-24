from flask import request, jsonify
from app.blueprints.blog.models import Post
from app import db
from .import bp as api 

@api.route('/blog')
def get_posts():
    """
    [POST] /api/v1/blog
    """
    return jsonify([p.to_dict() for p in Post.query.all()])

@api.route('/blog/<id>')
def get_post(id):
    """
    [POST] /api/v1/blog/<id>
    """
    return jsonify(Post.query.get(id).to_dict())


@api.route('/blog', methods=['POST'])
def create_post():
    """
    [POST] /api/v1/blog
    """
    data = request.get_json()
    print(data)
    p = Post(
        body = data.get('body'),
        user_id = data.get('user_id'))
    db.session.add(p)
    db.session.commit()    
    return jsonify(p.to_dict())


@api.route('/blog/<id>', methods=['DELETE'])
def delete_post(id):
    """
    [POST] /api/v1/blog/<id>
    """
    p = Post.query.get(id)
    db.session.delete(p)
    db.session.commit()
    return jsonify([p.to_dict() for p in Post.query.all()])
