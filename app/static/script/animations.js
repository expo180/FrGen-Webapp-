$(document).ready(function(){
$("#check").change(function() {
    if(this.checked) {
        $('#nav-bar').show();
/*home page nav bar animation*/}
  else{
    $('#nav-bar').hide();
}});
$("#submit").click('css', 'background-color:#EC008C')
$("#analytics-icon").click(function(){
  $(".analytics-table").show();  
});
$("#analytics-icon").dblclick(function(){
    $(".analytics-table").hide(); 
})

});
