import datetime
from flask import redirect
from flask import request
from flask import url_for
from flask import render_template
from config import app

class Openw: 
    def __init__(self, comp, winnerid, year=None): 
        self.comp = comp
        self.winnerid = winnerid
        self.year = year

@app.route('/OpenWater', methods=['GET', 'POST'])
def openwater_page():
    if request.method == 'GET':
        Openwater = app.store.get_openw()
        now = datetime.datetime.now()
        return render_template('OpenWater.html', Openwater=Openwater,
                               current_time=now.ctime())
    elif 'delete' in request.form:
        keys = request.form.getlist('openw_to_delete')
        for key in keys:
            app.store.delete_openw(int(key))
            return redirect(url_for('openwater_page'))
    elif 'update' in request.form:
        keys = request.form.getlist('openw_to_delete')
        for key in keys:
            return render_template('openw_update.html',key=key)
    elif 'add' in request.form:
        return render_template('openw_add.html')
@app.route('/OpenWater/<int:key>')
def openw_page(key):
    Openwater= app.store.get_openw(key)
    now = datetime.datetime.now()
    return render_template('OpenWater.html', Openwater=Openwater, current_time=now.ctime())

@app.route('/OpenWater/add')
def openw_add():
    comp = request.form['competition']
    winnerid = request.form['winnerid']
    year = request.form['year'] 
    openw = Openw(comp,winnerid, year)
    app.store.add_openw(openw)
    return redirect(url_for('openwater_page'))


@app.route('/OpenWater/update/<key>',methods=['GET' , 'POST'])
def openw_update(key):
    if request.method == 'POST':
        comp = request.form['competition']
        winnerid = request.form['winnerid']
        year = request.form['year']
        keys = request.form.getlist('openw_to_update')
        app.store.update_openw(int(key),comp,winnerid,year)
        return redirect(url_for('openwater_page'))


@app.route('/OpenWater/search2')
def openw_search2():
    now = datetime.datetime.now()
    return render_template('openw_search.html', current_time=now.ctime())

@app.route('/OpenWater/search', methods=['GET' , 'POST'])
def openw_search():
    if request.method == 'POST':
        word =request.form['word']
        Openwater=app.store.search_openw(word)
        now = datetime.datetime.now()
        return render_template('OpenWater.html', Openwater=Openwater, current_time=now.ctime())

@app.route('/OpenWater/tables')
def openw_tables():
    now = datetime.datetime.now()
    return render_template('openw_tables.html', current_time=now.ctime())
