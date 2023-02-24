from flask import request, render_template, redirect, url_for
from app import db
from .import bp as app
from .models import Post

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        p = Post(
            body=request.form.get('post_body'),
            user_id=1
        )
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('home'))
    context = {
        'posts': Post.query.order_by(Post.date_created.desc()).all()
    }
    return render_template('home.html', **context)


@app.route('/<id>')
def blog_single(id):
    # for p in posts:
    #     if p['id'] == int(id):
    #         post = p
    #         break
    post = Post.query.get(id)
    context = {
        'post': post
    }
    return render_template('blog/single.html', **context)
