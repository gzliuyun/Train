// JavaScript Document
var tag = [false,false,false,false,false,false,false];
function check_username(id){
	var username=document.getElementById(id).value;
	
	for(var i=0;i<username.length;i++){
        var text=username.charAt(i);
        if(!(text<=9&&text>=0)&&!(text>='a'&&text<='z')&&!(text>='A'&&text<='Z')&&text!="_")
        {
         	document.getElementById("user_name").innerHTML="<span  style=\"color:red\" class=\"glyphicon glyphicon-remove\"></span>";
         	tag[0] = false;
			return;
        }
    }
	if(username.length>=6){
		document.getElementById("user_name").innerHTML="<span  style=\"color:green\" class=\"glyphicon glyphicon-ok\"></span>";	
		tag[0] = true;
	}
	else{
		document.getElementById("user_name").innerHTML="<span></span>";
		tag[0] = false;
	}
}
function check_password(id){
	var password=document.getElementById(id).value;
	
	for(var i=0;i<password.length;i++){
        var text=password.charAt(i);
        if(!(text<=9&&text>=0)&&!(text>='a'&&text<='z')&&!(text>='A'&&text<='Z')&&text!="_")
        {
         	document.getElementById("pass_word").innerHTML="<span  style=\"color:red\" class=\"glyphicon glyphicon-remove\"></span>";
         	tag[1] = false;
			return;
        }
    }
	if(password.length>=6){
		document.getElementById("pass_word").innerHTML="<span  style=\"color:green\" class=\"glyphicon glyphicon-ok\"></span>";	
		tag[1] = true;
	}
	else{
		document.getElementById("pass_word").innerHTML="<span></span>";
		tag[1] = false;
	}
}
function check_surepassword(id){
	var surepassword=document.getElementById(id).value;
	var password = document.getElementById("password").value;
	if( password == surepassword){
		document.getElementById("sure_password").innerHTML="<span  style=\"color:green\" class=\"glyphicon glyphicon-ok\"></span>";
		tag[2] = true;
		return;
	}
	if(password.length < surepassword.length){
		document.getElementById("sure_password").innerHTML="<span  style=\"color:red\" class=\"glyphicon glyphicon-remove\"></span>";
		tag[2]= false;
		return;
	}
	else{
		document.getElementById("sure_password").innerHTML="<span></span>";
		tag[2] = false;
	}
}

function check_realname(id){
	var realname=document.getElementById(id).value;
	var reg = /^[\u4E00-\u9FA5]+$/; 
	if(!reg.test(realname)){
		document.getElementById("real_name").innerHTML="<span  style=\"color:red\" class=\"glyphicon glyphicon-remove\"></span>";
		tag[3] = false;
		return;
	}
	if(realname.length>=2){
		document.getElementById("real_name").innerHTML="<span  style=\"color:green\" class=\"glyphicon glyphicon-ok\"></span>";	
		tag[3] = true;
	}
	else{
		document.getElementById("real_name").innerHTML="<span></span>";
		tag[3] = false;
	}
}

function check_idcard(id){
	var idcard=document.getElementById(id).value;
	for(var i=0;i<idcard.length;i++){
        var text=idcard.charAt(i);
        if(!(text<=9&&text>=0)&&!(text>='A'&&text<='Z')){
			document.getElementById("id_card").innerHTML="<span  style=\"color:red\" class=\"glyphicon glyphicon-remove\"></span>";
			tag[4] = false;
			return;
		}
	}
	if(idcard.length==18){
		document.getElementById("id_card").innerHTML="<span  style=\"color:green\" class=\"glyphicon glyphicon-ok\"></span>";	
		tag[4] = true;
	}
	else if(idcard.length>18){
		document.getElementById("id_card").innerHTML="<span  style=\"color:red\" class=\"glyphicon glyphicon-remove\"></span>";
		tag[4]= false
	}
	else{
		document.getElementById("id_card").innerHTML="<span></span>";
		tag[4] = false
	}
}

function check_phonenumber(id){
	var phonenumber=document.getElementById(id).value;
	for(var i=0;i<phonenumber.length;i++){
        var text=phonenumber.charAt(i);
		if( (i==0&&text!=1) || !(text<=9&&text>=0) ){
			document.getElementById("phone_number").innerHTML="<span  style=\"color:red\" class=\"glyphicon glyphicon-remove\"></span>";
			tag[5] = false;
			return;
		}
	}
	if(phonenumber.length==11){
		document.getElementById("phone_number").innerHTML="<span  style=\"color:green\" class=\"glyphicon glyphicon-ok\"></span>";	
		tag[5] = true;
	}
	else if(phonenumber.length > 11){
		document.getElementById("phone_number").innerHTML="<span  style=\"color:red\" class=\"glyphicon glyphicon-remove\"></span>";
		tag[5] = false;
	}
	else{
		document.getElementById("phone_number").innerHTML="<span></span>";
		tag[5] = false;
	}
}
function check_email(id){
	var mail=document.getElementById(id).value;
	var reg =  /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  	var ismail= reg.test(mail);
 	if (!ismail ) {
     	document.getElementById("e_mail").innerHTML="<span></span>";
		tag[6] = false;
  	}
  	else{
  		document.getElementById("e_mail").innerHTML="<span  style=\"color:green\" class=\"glyphicon glyphicon-ok\"></span>";
  		tag[6] = true;
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