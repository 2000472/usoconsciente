from flask import Flask, render_template, request, url_for, flash, redirect
import os, datetime
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import abort

project_dir = os.path.dirname(os.path.abspath(__file__))

database_file = "sqlite:///{}" . format(os.path.join(project_dir, "database.db"))

app = Flask('__name__')
app.config['SECRET_KEY'] = 'aaa111bbb222ccc333'
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
db = SQLAlchemy(app)

class Dicas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    criacao = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    titulo = db.Column(db.String(100), nullable=False)
    conteudo1 = db.Column(db.String(1000), nullable=False)
    conteudo2 = db.Column(db.String(1000), nullable=True)
    conteudo3 = db.Column(db.String(1000), nullable=True)
    conteudo4 = db.Column(db.String(1000), nullable=True)
    conteudo5 = db.Column(db.String(1000), nullable=True)
    conteudo6 = db.Column(db.String(1000), nullable=True)
    conteudo7 = db.Column(db.String(1000), nullable=True)
    conteudo8 = db.Column(db.String(1000), nullable=True)
    conteudo9 = db.Column(db.String(1000), nullable=True)
    conteudo10 = db.Column(db.String(1000), nullable=True)
    conteudo11 = db.Column(db.String(1000), nullable=True)
    conteudo12 = db.Column(db.String(1000), nullable=True)
    conteudo13 = db.Column(db.String(1000), nullable=True)
    conteudo14 = db.Column(db.String(1000), nullable=True)
    conteudo15 = db.Column(db.String(1000), nullable=True)
    conteudo16 = db.Column(db.String(1000), nullable=True)
    conteudo17 = db.Column(db.String(1000), nullable=True)
    conteudo18 = db.Column(db.String(1000), nullable=True)
    conteudo19 = db.Column(db.String(1000), nullable=True)
    conteudo20 = db.Column(db.String(1000), nullable=True)
    fonte = db.Column(db.String(100), nullable=True)
    fontelink = db.Column(db.String(200), nullable=True)
    imagem = db.Column(db.String(200), nullable=True)

@app.route('/')

def index():
    dicas = Dicas.query.all()
    return render_template('index.html', dicas=dicas)

def get_dica(dica_id):
    dica = Dicas.query.filter_by(id=dica_id).first()
    if dica is None:
        abort(404)
    return dica

@app.route('/<int:dica_id>/dicas_visualizacao')

def dicas_visualizacao(dica_id):
    dica = get_dica(dica_id)
    return render_template('dicas_visualizacao.html', dica=dica)

@app.route('/dicas_inclusao', methods=('GET', 'POST'))

def dicas_inclusao():

    if request.method=='POST':
        titulo = request.form['titulo']
        conteudo1 = request.form['conteudo1']
        conteudo2 = request.form['conteudo2']
        conteudo3 = request.form['conteudo3']
        conteudo4 = request.form['conteudo4']
        conteudo5 = request.form['conteudo5']
        conteudo6 = request.form['conteudo6']
        conteudo7 = request.form['conteudo7']
        conteudo8 = request.form['conteudo8']
        conteudo9 = request.form['conteudo9']
        conteudo10 = request.form['conteudo10']
        conteudo11 = request.form['conteudo11']
        conteudo12 = request.form['conteudo12']
        conteudo13 = request.form['conteudo13']
        conteudo14 = request.form['conteudo14']
        conteudo15 = request.form['conteudo15']
        conteudo16 = request.form['conteudo16']
        conteudo17 = request.form['conteudo17']
        conteudo18 = request.form['conteudo18']
        conteudo19 = request.form['conteudo19']
        conteudo20 = request.form['conteudo20']
        fonte = request.form['fonte']
        fontelink = request.form['fontelink']
        imagem = request.form['imagem']

        if not titulo:
            flash('O título é obrigatório')
        else:
            dica = Dicas(
                titulo=titulo,
                conteudo1=conteudo1,
                conteudo2=conteudo2,
                conteudo3=conteudo3,
                conteudo4=conteudo4,
                conteudo5=conteudo5,
                conteudo6=conteudo6,
                conteudo7=conteudo7,
                conteudo8=conteudo8,
                conteudo9=conteudo9,
                conteudo10=conteudo10,
                conteudo11=conteudo11,
                conteudo12=conteudo12,
                conteudo13=conteudo13,
                conteudo14=conteudo14,
                conteudo15=conteudo15,
                conteudo16=conteudo16,
                conteudo17=conteudo17,
                conteudo18=conteudo18,
                conteudo19=conteudo19,
                conteudo20=conteudo20,
                fonte=fonte,
                fontelink=fontelink,
                imagem = imagem)
            db.session.add(dica)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('dicas_inclusao.html')

@app.route('/<int:id>/dicas_alteracao', methods=('GET', 'POST'))

def dicas_alteracao(id):

    dica = get_dica(id)

    if request.method=='POST':
        titulo = request.form['titulo']
        conteudo1 = request.form['conteudo1']
        conteudo2 = request.form['conteudo2']
        conteudo3 = request.form['conteudo3']
        conteudo4 = request.form['conteudo4']
        conteudo5 = request.form['conteudo5']
        conteudo6 = request.form['conteudo6']
        conteudo7 = request.form['conteudo7']
        conteudo8 = request.form['conteudo8']
        conteudo9 = request.form['conteudo9']
        conteudo10 = request.form['conteudo10']
        conteudo11 = request.form['conteudo11']
        conteudo12 = request.form['conteudo12']
        conteudo13 = request.form['conteudo13']
        conteudo14 = request.form['conteudo14']
        conteudo15 = request.form['conteudo15']
        conteudo16 = request.form['conteudo16']
        conteudo17 = request.form['conteudo17']
        conteudo18 = request.form['conteudo18']
        conteudo19 = request.form['conteudo19']
        conteudo20 = request.form['conteudo20']
        fonte = request.form['fonte']
        fontelink = request.form['fontelink']
        imagem = request.form['imagem']

        if not titulo:
            flash('O título é obrigatório')
        else:
            dica.titulo = titulo
            dica.conteudo1 = conteudo1
            dica.conteudo2 = conteudo2
            dica.conteudo3 = conteudo3
            dica.conteudo4 = conteudo4
            dica.conteudo5 = conteudo5
            dica.conteudo6 = conteudo6
            dica.conteudo7 = conteudo7
            dica.conteudo8 = conteudo8
            dica.conteudo9 = conteudo9
            dica.conteudo10 = conteudo10
            dica.conteudo11 = conteudo11
            dica.conteudo12 = conteudo12
            dica.conteudo13 = conteudo13
            dica.conteudo14 = conteudo14
            dica.conteudo15 = conteudo15
            dica.conteudo16 = conteudo16
            dica.conteudo17 = conteudo17
            dica.conteudo18 = conteudo18
            dica.conteudo19 = conteudo19
            dica.conteudo20 = conteudo20
            dica.fonte = fonte
            dica.fontelink = fontelink
            dica.imagem = imagem
            db.session.commit()
            return redirect(url_for('dicas_visualizacao', dica_id=id))

    return render_template('dicas_alteracao.html', dica=dica)

@app.route('/<int:id>/dicas_exclusao', methods=('POST',))

def dicas_exclusao(id):

    dica = get_dica(id)
    db.session.delete(dica)
    db.session.commit()
    flash('"{}" foi apagado com sucesso!' . format(dica.titulo))
    return redirect(url_for('index'))