$(document).ready(function(){
    $("form#payment-form").submit(function(event) {
      event.preventDefault();
  
      var userName=$("#name").val();
      var email=$("#mail").val();
      var amount=$("#amount").val();
      var message=$("#donation").val();
      if(userName&&email&&message&&amount){
        alert("Hi "+userName +". Thank you for donating.your help is highly appriciated.");
      
      }
      else{
        alert("All fields required");
      }
      $("form").trigger("reset");
    });
  });