<script type="text/javascript">
var xmlhttp=new XMLHttpRequest();

var param = "respondent id here";

var link = "http://place/"

if ("withCredentials" in xmlhttp) {
	// Most browsers.
	xmlhttp.open("GET","http://54.152.254.107/card/" + param, true);
} else if (typeof XDomainRequest != "undefined") {
	// IE8 & IE9
	xmlhttp = new XDomainRequest();
	xmlhttp.open("GET","http://54.152.254.107/card/" + param);
}

xmlhttp.onload=function(){
	document.getElementById("gift_card_link").href = link + xmlhttp.responseText;
}

xmlhttp.send();
</script>