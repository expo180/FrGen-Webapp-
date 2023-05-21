$(document).ready(function(){
$("#check").change(function() {
    if(this.checked) {
        $('#nav-bar').show();
/*home page nav bar animation*/}
  else{
    $('#nav-bar').hide();
}});
$(".usefool-links").click(function(){
    alert("Vous allez être redirigé vers une autre page")
});
$("#pers-grh").click(function(){
    $("main").fadeOut();
    $("#pers-grh").css('border-color', 'white')
    $(".profil-hidden").slideDown().addClass("active-profile")
    $(".cours-hidden").hide();
    $(".bilan-hidden").hide();
    $(".certification-hidden").hide();
    $(".bank-hidden").hide();
    $(".jeux-hidden").hide();
    $("#e-learn").css('border-color', '#20BDFF');
    $("#thinking").css('border-color', '#20BDFF');
    $("#banking").css('border-color', '#20BDFF');
    $("#certificate").css('border-color', '#20BDFF');
    $("#chess").css('border-color', '#20BDFF');

});
$("#pers-grh").dblclick(function(){
    $(".profil-hidden").hide();
    $("#pers-grh").css('border-color', '#20BDFF')
    $("main").slideUp().show();


});
$("#e-learn").click(function(){
    $("main").fadeOut();
    $("#e-learn").css('border-color', 'white')
    $(".cours-hidden").slideDown().addClass("active-bank")
    $(".profil-hidden").hide();
    $(".bilan-hidden").hide();
    $(".certification-hidden").hide();
    $(".bank-hidden").hide();
    $(".jeux-hidden").hide();
    $("#thinking").css('border-color', '#20BDFF');
    $("#banking").css('border-color', '#20BDFF');
    $("#certificate").css('border-color', '#20BDFF');
    $("#chess").css('border-color', '#20BDFF');
    $("#pers-grh").css('border-color', '#20BDFF');

});
$("#e-learn").dblclick(function(){
    $(".cours-hidden").hide();
    $("#e-learn").css('border-color', '#20BDFF')
    $("main").slideUp().show();


});
$("#thinking").click(function(){
    $("main").fadeOut();
    $("#thinking").css('border-color', 'white')
    $(".bilan-hidden").slideDown().addClass("active-bank")
    $(".profil-hidden").hide();
    $(".cours-hidden").hide();
    $(".certification-hidden").hide();
    $(".bank-hidden").hide();
    $(".jeux-hidden").hide();
    $("#e-learn").css('border-color', '#20BDFF')
    $("#banking").css('border-color', '#20BDFF');
    $("#certificate").css('border-color', '#20BDFF');
    $("#chess").css('border-color', '#20BDFF');
    $("#pers-grh").css('border-color', '#20BDFF');
    

});

$("#thinking").dblclick(function(){
    $(".bilan-hidden").hide();
    $("#thinking").css('border-color', '#20BDFF')
    $("main").slideUp().show();


});

$("#banking").click(function(){
    $("main").fadeOut();
    $("#banking").css('border-color', 'white')
    $(".bank-hidden").slideDown().addClass("active-bank");
    $(".profil-hidden").hide();
    $(".certification-hidden").hide();
    $(".cours-hidden").hide();
    $(".bilan-hidden").hide();
    $(".jeux-hidden").hide();
    $("#e-learn").css('border-color', '#20BDFF')
    $("#thinking").css('border-color', '#20BDFF')
    $("#certificate").css('border-color', '#20BDFF');
    $("#chess").css('border-color', '#20BDFF');
    $("#pers-grh").css('border-color', '#20BDFF');

});
$("#banking").dblclick(function(){
    $(".bank-hidden").hide();
    $("#banking").css('border-color', '#20BDFF')
    $("main").slideUp().show();
    $("footer").slideUp().show();


});
$("#certificate").click(function(){
    $("main").fadeOut();
    $("#certificate").css('border-color', 'white')
    $(".certification-hidden").slideDown().addClass("active-bank")
    $(".profil-hidden").hide();
    $(".cours-hidden").hide();
    $(".bilan-hidden").hide();
    $(".bank-hidden").hide();
    $(".jeux-hidden").hide();
    $("#e-learn").css('border-color', '#20BDFF')
    $("#thinking").css('border-color', '#20BDFF')
    $("#banking").css('border-color', '#20BDFF')
    $("#chess").css('border-color', '#20BDFF');
    $("#pers-grh").css('border-color', '#20BDFF');

});
$("#certificate").dblclick(function(){
    $(".certification-hidden").hide();
    $("#certificate").css('border-color', '#20BDFF')
    $("main").slideUp().show();
});
$("#chess").click(function(){
    $("main").fadeOut();
    $("#chess").css('border-color', 'white')
    $(".jeux-hidden").slideDown().addClass("active-bank");
    $(".profil-hidden").hide();
    $(".cours-hidden").hide();
    $(".bilan-hidden").hide();
    $(".bank-hidden").hide();
    $(".certification-hidden").hide();
    $("#e-learn").css('border-color', '#20BDFF')
    $("#thinking").css('border-color', '#20BDFF')
    $("#banking").css('border-color', '#20BDFF')
    $("#certificate").css('border-color', '#20BDFF')
    $("#pers-grh").css('border-color', '#20BDFF');

});
$("#chess").dblclick(function(){
    $(".jeux-hidden").hide();
    $("#chess").css('border-color', '#20BDFF');
    $("main").slideUp().show();


});

$("#analytics-icon").click(function(){
  $(".analytics-table").show();  
});
$("#analytics-icon").dblclick(function(){
    $(".analytics-table").hide(); 
})

});
