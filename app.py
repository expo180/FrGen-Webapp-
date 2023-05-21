#coded by Bader Salissou Saadou
#frame_genesis routes and MySQL configuration

from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re


# Initialize Flask
app = Flask(__name__)
app.secret_key = 'Theawesomebss7441$'

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Theawesomebss7441$'
app.config['MYSQL_DB'] = 'frame_genesis'

# initialize MySQL
mysql = MySQL(app)


@app.route("/")
@app.route("/acceuil/")
def home():
    return render_template('index.html')


@app.route("/cours/")
@app.route("/acceuil/cours/")
def courses():
    return render_template('computer_science.html')


@app.route("/Développement_web/")
@app.route("/cours/Développement_web/")
@app.route("/acceuil/cours/Développement_web/")
def web_dev():
    return render_template('web.html')

@app.route("/Sciences_des_données/")
def data():
    return render_template('data_science.html')

@app.route("/Intelligence_artificielle/")
def IA():
    return render_template('intelligence_artificielle.html')

@app.route("/Robotique_et_systèmes_embarqués/")
def robotics():
    return render_template('robotics.html')

@app.route("/Microsoft_Office/")
def office():
    return render_template('office.html')

@app.route("/Hacking_éthique/")
def hacking():
    return render_template('hacking.html')

@app.route("/Flutter/")
def flutter():
    return render_template('flutter.html')

@app.route("/Unity/")
def unity():
    return render_template('unity.html')

@app.route("/Ingénierie_DevOps/")
def devOps():
    return render_template('devOps.html')

@app.route("/blender/")
def blender():
    return render_template('blender.html')

@app.route("/cryptomonnaie/")
def bitcoin():
    return render_template('crypto.html')

@app.route("/équipe/rejoindre_l'_équipe/postes_vacants/")
@app.route("/postes_vacants/")
def jobs():
    return render_template("postes.html")


@app.route("/équipe/rejoindre_l'_équipe/")
def équipe():
    return render_template("équipe.html")


@app.route("/questionnaire_de_paiement/")
def questionnaire():
    return render_template('question_paiement.html')


@app.route("/paiement/")
def paiement():
    return render_template("charge.html")


@app.route("/Faire_un_don/")
@app.route("/acceuil/Faire_un_don/")
def gift():
    return render_template('gift.html')


@app.route("/Se_connecter/", methods=['GET', 'POST'])
def connexion():
    msg = ''
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email and password:
            cursor =  mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM student_accounts WHERE email = %s AND password = %s', (email, password,))
            account = cursor.fetchone()
            if account:
                session['loggedin'] = True
                session['id'] = account[0]
                session['email'] = account[3]
                msg = 'Vous êtes maintenant connecté à votre compte!'
                return render_template('utilisateur.html', username=account['first_name'])
            else:
                msg = "Mot de passe ou adresse e-mail incorrect"
        else:
            msg = 'Veuillez remplir tous les champs!'
    return render_template('Se_connecter.html', msg=msg)


@app.route("/Se_connecter/Créer_un_nouveau_compte/", methods=['GET', 'POST'])
def nouvel_utilisateur():
    msg = ''
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        email = request.form['email']
        if first_name and last_name and password and email:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM student_accounts WHERE first_name = %s', (first_name,))
            account = cursor.fetchone()
            if account:
                msg = 'Ce compte existe déjà!'
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = 'Adresse e-mail invalide!'
            else:
                cursor.execute('INSERT INTO student_accounts (first_name, last_name, email, password) VALUES (NULL, %s, %s, %s, %s)', (first_name, last_name, email, password,))
                msg = 'Votre compte a été créé avec succès'
                return redirect(url_for('connexion'))
        else:
            msg = 'Veuillez remplir tous les champs!'
    return render_template('nouvel_utilisateur_un.html', msg=msg)


@app.route("/Page_d'acceuil/")
def dashboard():
    if 'loggedin' in session:
        return render_template('utilisateur.html', username=session['first_name'])
    else:
        return redirect(url_for('connexion'))


@app.route("/documentation/")
def documentation():
    return render_template('documentation.html')


@app.route("/jeux/")
def jeux():
    return render_template("jeux.html")


@app.route("/livres/")
def livres():
    return render_template("livres.html")


@app.route("/musique/")
def musique():
    return render_template('musiques.html')


@app.route("/outils/")
def outils():
    return render_template('musiques.html')


@app.route("/boutique/")
def boutique():
    return render_template("boutique.html")


@app.route("/cartographie3D/")
def cartographie():
    return render_template("cartographie.html")


@app.route("/Devenez_instructeur/")
def instructor():
    return render_template("instructeur_form.html")

@app.route("/HTML5&CSS3_documentation/")
def hypertext():
    return render_template('HTML5&CSS3_doc.html')

@app.route("/Javascript_documentation/")
def Javascript():
    return render_template('javascript_doc.html')

@app.route("/MATLAB_documentation/")
def MATLAB():
    return render_template('MATLAB_doc.html')

@app.route("/Bootstrap_documentation/")
def Bootstrap():
    return render_template('Bootstrap_doc.html')

@app.route("/Physique_quantique_documentation/")
def quantum():
    return render_template('quantum_doc.html')

@app.route("/Théorie_de_la_relativité_documentation/")
def relativity():
    return render_template('relativity_doc.html')

@app.route("/Equations_différentielles_documentation/")
def differential_equations():
    return render_template('differential_equations_doc.html')

@app.route("/Fonctions_logarithmes_documentation/")
def logarithmic_functions():
    return render_template('logarithmic_functions_doc.html')

@app.route("/Bilan_psychologique/")
def psy():
    return render_template('bilan_psy.html')
