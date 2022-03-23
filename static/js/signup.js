msg=document.getElementById("message").innerHTML
if (msg){
        document.getElementById("msg").classList.add("msg2");
        setTimeout(myfunction,3000);
        function myfunction(){
            document.getElementById("msg").classList.remove("msg2");
            document.getElementById("message").innerHTML=""
        }
    
}