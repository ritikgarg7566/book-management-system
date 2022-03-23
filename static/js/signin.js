console.log("ritik")
msg=document.getElementById("message").innerHTML
if (msg){
    if (msg=="your account has been successfully create"){
        document.getElementById("msg").classList.add("msg1");
        document.getElementById("msg").classList.remove("msg2");
        setTimeout(myfunction,3000);
        function myfunction(){
            document.getElementById("msg").classList.remove("msg1");
            document.getElementById("message").innerHTML=""
        }

    }
    else{
        document.getElementById("msg").classList.add("msg2");
        document.getElementById("msg").classList.remove("msg1");
        setTimeout(myfunction,3000);
        function myfunction(){
            document.getElementById("msg").classList.remove("msg2");
            document.getElementById("message").innerHTML=""
        }
    }
}