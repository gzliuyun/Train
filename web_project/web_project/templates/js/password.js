// JavaScript Document
var tag = [false,false,false];
function check_oldpassword(id){
	var password=document.getElementById(id).value;
	for(var i=0;i<password.length;i++){
        var text=password.charAt(i);
        if(!(text<=9&&text>=0)&&!(text>='a'&&text<='z')&&!(text>='A'&&text<='Z')&&text!="_")
        {
         	document.getElementById("old").innerHTML="<span  style=\"color:red\" class=\"glyphicon glyphicon-remove\"></span>";
         	tag[0] = false;
			return;
        }
    }
	if(password.length>=6){
		document.getElementById("old").innerHTML="<span  style=\"color:green\" class=\"glyphicon glyphicon-ok\"></span>";	
		tag[0] = true;
	}
	else{
		document.getElementById("old").innerHTML="<span></span>";
		tag[0] = false;
	}
}
function check_newpassword(id){
	var password=document.getElementById(id).value;
	
	for(var i=0;i<password.length;i++){
        var text=password.charAt(i);
        if(!(text<=9&&text>=0)&&!(text>='a'&&text<='z')&&!(text>='A'&&text<='Z')&&text!="_")
        {
         	document.getElementById("new").innerHTML="<span  style=\"color:red\" class=\"glyphicon glyphicon-remove\"></span>";
         	tag[1] = false;
			return;
        }
    }
	if(password.length>=6){
		document.getElementById("new").innerHTML="<span  style=\"color:green\" class=\"glyphicon glyphicon-ok\"></span>";	
		tag[1] = true;
	}
	else{
		document.getElementById("new").innerHTML="<span></span>";
		tag[1] = false;
	}
}
function check_surepassword(id){
	var surepassword=document.getElementById(id).value;
	var password = document.getElementById("newpassword").value;
	if( password == surepassword){
		document.getElementById("sure_new").innerHTML="<span  style=\"color:green\" class=\"glyphicon glyphicon-ok\"></span>";
		tag[2] = true;
		return;
	}
	if(password.length < surepassword.length){
		document.getElementById("sure_new").innerHTML="<span  style=\"color:red\" class=\"glyphicon glyphicon-remove\"></span>";
		tag[2]= false;
		return;
	}
	else{
		document.getElementById("sure_new").innerHTML="<span></span>";
		tag[2] = false;
	}
}
function enter(){
	for(var i = 0; i < tag.length; i++){
		if(tag[i]==false){
			alert('输入有误！请重新输入...')
			return false;
		}
	}
	return true;
}