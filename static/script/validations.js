$(document).ready(function(){
    $("#nom").change(function(){
        console.log("You did something")
    });
    $("#next").click(function(){
        $(".input-elements").hide();
        $(".account-creation").addClass("account-creation-active").fadeIn();
        $(".error-msg").fadeIn();
    });
    $("#check").change(function(){
        if(this.checked){
            $("#submit").css("background-color", "#EC008C");
        }
        else{
            $("#submit").css("background-color", "none");
        }
    });
    $("#prev").click(function(){
        console.log("Hello world");
        $(".input-elements").show();
        $(".account-creation").hide();

    })
    var passwordRegExp = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/; 
   
});