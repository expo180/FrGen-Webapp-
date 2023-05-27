function carte(){
	document.getElementById('pay').innerHTML = '';
	document.getElementById('Nita').innerHTML = '';
	document.getElementById('country').innerHTML = '';
	document.getElementById('heading').innerHTML = '<h2>Infos de paiement</h2>';
	document.getElementById('carte').innerHTML = "<label>Entrez le numéro de la carte:</label><input type='text' placeholder='345 122 890'>\n<label>Date d'\expiration:</label><input type='text' placeholder='MM/YY'>\n<label>CVV:</label><input type='text' placeholder='127'>\n<input type='submit' value='envoyer'>"
}
function autres(){
	document.getElementById('heading').innerHTML = '<h2>Infos de paiement</h2>';
	document.getElementById('carte').innerHTML = '';
	document.getElementById('pay').innerHTML = "<select><option>- Veuillez sélectionner votre zone géographique -</option>\n<option id='asie'>Asie</option>\n<option id='amérique'>Amérique</option>\n<option id='afrique' onclick='afrique()'>Afrique</option>\n<option id='europe'>Europe</option></select>";
}
function afrique(){
	document.getElementById('carte').innerHTML = '';
	document.getElementById('country').innerHTML = '<select><option>- Veuillez sélectionner votre méthode de paiement préférée -</option><option>Airtel Money</option><option>Al-Izza transfert</option><option>Amana transfert</option><option>BNIF-Afuwa</option><option>Moov Flooz</option><option onclick="Nita()">Nita</option><option>Orange Money</option><option>Western Union</option><option>Zeyna Transfert</option></select>'
}
function Nita(){
	document.getElementById('carte').innerHTML = '';
	document.getElementById('Nita').innerHTML = "<label>Nom de l'expéditeur: </label><input type='text' placeholder='Julien Yves-DelaCroix'>\n<label>Numéro de téléphone(exp):</label><input type='text' placeholder='+250 89659812'>\n<label>CVV:</label><input type='text' placeholder='127'>\n<input type='submit' value='envoyer'>"
}
