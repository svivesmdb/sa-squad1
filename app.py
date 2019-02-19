#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from forms import *
import os
from dao import *



#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

ATLAS_URL = "mongodb+srv://squad1:squad1@myatlascluster-izhs1.gcp.mongodb.net/test?retryWrites=true"


app = Flask(__name__)
app.config.from_object('config')


appDao = DAO(ATLAS_URL)


# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    print(appDao.getProofPoints())
    
    form = SearchForm(request.form)
    return render_template('pages/placeholder.home.html', form=form)


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')

@app.route('/proofpoint', methods=['GET', 'POST'])
def proofpoint():
    if request.method == 'POST':
        customerCompany = request.form['customerCompany']
        customerIndustry = request.form['customerIndustry']
        customerProject = request.form['customerProject']
        customerProjectDescription = request.form['customerProjectDescription']
        useCase = request.form['useCase']
        creationDate = request.form['creationDate']
        owner_id = request.form['owner_id']

        appDao.addProofPoint(customerCompany, customerIndustry, customerProject, customerProjectDescription, useCase, creationDate, owner_id)
        pass
    elif request.method == 'GET':
        form = ProofPointForm(request.form)
        # @Alessandro: Create a form like 'proofpoint.html' to show the form to insert a new proofpoint.
        #   also remember that it should have a field for uploading ppt files.
        return render_template('forms/login.html', form=form)


@app.route('/login')
def login():
    form = LoginForm(request.form)
    return render_template('forms/login.html', form=form)


@app.route('/register')
def register():
    form = RegisterForm(request.form)
    return render_template('forms/register.html', form=form)


@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)

# Error handlers.


@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
'''
if __name__ == '__main__':
    app.run()
'''
# Or specify port manually:

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

