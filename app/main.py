from flask import Blueprint, render_template
from . import db


main = Blueprint('main', __name__)

@main.route("/")
def home():
    return render_template('index.html')


@main.route("/cours/")
def courses():
    return render_template('computer_science.html')


@main.route("/Développement_web/")
def web_dev():
    return render_template('web.html')

@main.route("/Sciences_des_données/")
def data():
    return render_template('data_science.html')

@main.route("/Intelligence_artificielle/")
def IA():
    return render_template('intelligence_artificielle.html')

@main.route("/Robotique_et_systèmes_embarqués/")
def robotics():
    return render_template('robotics.html')

@main.route("/Microsoft_Office/")
def office():
    return render_template('office.html')

@main.route("/Hacking_éthique/")
def hacking():
    return render_template('hacking.html')

@main.route("/Flutter/")
def flutter():
    return render_template('flutter.html')

@main.route("/Unity/")
def unity():
    return render_template('unity.html')

@main.route("/Ingénierie_DevOps/")
def devOps():
    return render_template('devOps.html')

@main.route("/blender/")
def blender():
    return render_template('blender.html')

@main.route("/cryptomonnaie/")
def bitcoin():
    return render_template('crypto.html')

@main.route("/postes_vacants/")
def jobs():
    return render_template("postes.html")


@main.route("/rejoindre_l'_équipe/")
def équipe():
    return render_template("équipe.html")


@main.route("/questionnaire_de_paiement/")
def questionnaire():
    return render_template('question_paiement.html')


@main.route("/paiement/")
def paiement():
    return render_template("charge.html")


@main.route("/Faire_un_don/")
def gift():
    return render_template('gift.html')

@main.route("/documentation/")
def documentation():
    return render_template('documentation.html')


@main.route("/jeux/")
def jeux():
    return render_template("jeux.html")


@main.route("/livres/")
def livres():
    return render_template("livres.html")


@main.route("/musique/")
def musique():
    return render_template('musiques.html')


@main.route("/outils/")
def outils():
    return render_template('musiques.html')


@main.route("/boutique/")
def boutique():
    return render_template("boutique.html")


@main.route("/cartographie3D/")
def cartographie():
    return render_template("cartographie.html")


@main.route("/Devenez_instructeur/")
def instructor():
    return render_template("instructeur_form.html")

@main.route("/HTML5&CSS3_documentation/")
def hypertext():
    return render_template('HTML5&CSS3_doc.html')

@main.route("/Javascript_documentation/")
def Javascript():
    return render_template('javascript_doc.html')

@main.route("/MATLAB_documentation/")
def MATLAB():
    return render_template('MATLAB_doc.html')

@main.route("/Bootstrap_documentation/")
def Bootstrap():
    return render_template('Bootstrap_doc.html')

@main.route("/Physique_quantique_documentation/")
def quantum():
    return render_template('quantum_doc.html')

@main.route("/Théorie_de_la_relativité_documentation/")
def relativity():
    return render_template('relativity_doc.html')

@main.route("/Equations_différentielles_documentation/")
def differential_equations():
    return render_template('differential_equations_doc.html')

@main.route("/Fonctions_logarithmes_documentation/")
def logarithmic_functions():
    return render_template('logarithmic_functions_doc.html')

@main.route("/Bilan_psychologique/")
def psy():
    return render_template('bilan_psy.html')

@main.route("/Page_d'acceuil/")
def dashboard():
   return render_template('utilisateur.html') 
