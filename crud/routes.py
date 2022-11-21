from flask import  flash, render_template, url_for, redirect, request
from crud import app, db
from crud.forms import AddForm, UpdateForm, Searchform
from crud.models import User

@app.route('/')
@app.route('/home')
def home():
    posts=User.query.all()
    return render_template('home.html',posts=posts,title='Home page')

@app.route('/add/new',methods=['GET','POST'])
def add():
    form=AddForm()
    
    if form.validate_on_submit():
        user=User(firstname=form.firstname.data, lastname=form.lastname.data, designation=form.title.data, email=form.email.data, number=form.number.data, about=form.about.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Contact created for {form.firstname.data} {form.lastname.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('add.html',title='Add page', form=form)

@app.route('/display')
def display():
    return render_template('display.html',title='Display page')

@app.route('/update/<int:post_id>',methods=['GET','POST'])
def update(post_id):
    post=User.query.get_or_404(post_id)
    form=UpdateForm()
    if form.validate_on_submit():
        post.firstname=form.firstname.data
        post.lastname=form.lastname.data
        post.designation=form.title.data
        post.email=form.email.data
        if form.about.data:
            post.about=form.about.data
        else:
            post.about=post.about
        db.session.commit()
        flash('Your Update has been Successfull','success')
        return redirect(url_for('home'))
    elif request.method=='GET':
        form.firstname.data=post.firstname
        form.lastname.data=post.lastname
        form.title.data=post.designation
        form.email.data=post.email
        form.number.data=post.number
        form.about.data=post.about

    return render_template('update.html',title='Update Contact', form= form,post=post)

@app.route('/add/<int:post_id>')
def contact(post_id):
    post=User.query.get_or_404(post_id)
    return render_template('contact.html',title=post.designation, post=post)

@app.route('/delete/<int:post_id>',methods=['POST'])
def delete(post_id):
    post=User.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Contact has been deleted', 'success')
    return redirect(url_for('home'))

@app.route('/search',methods=['GET','POST'])
def search():
    a = request.form.get('q')
    post=User.query.filter_by(firstname=a).first()
    return render_template("search.html",title='Search', result=post)


    
#     #defines what happens when there is a POST request
#     if x.method == "POST":
#         title = x.POST.get("q")
#         return render_template(x,'display.html', { 'title' : title })


#     #defines what happens when there is a GET request
#     else:
#         return render_template(x,'search.html')


    # 
    # return render_template('add.html',title='Add page', form=form)



    

