$(document).ready(function(){
  $("form#contact-us").submit(function(event) {
    event.preventDefault();

    var userName=$("#name").val();
    var email=$("#email").val();
    var comment=$("#comment").val();
    if(userName&&email&&comment){
      alert("Hi "+userName +". Thank you for contacting Online Charity Management. We'll get back to you.");
    
    }
    else{
      alert("All fields required");
    }
    $("form").trigger("reset");
  });
});