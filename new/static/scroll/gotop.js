(function() {


function $(id){
	return document.getElementById(id);
}

function goTop(acceleration, time) {
	acceleration = acceleration || 0.1;
	time = time || 12;

	var dx = 0;
	var dy = 0;
	var bx = 0;
	var by = 0;
	var wx = 0;
	var wy = 0;

	if (document.documentElement) {
		dx = document.documentElement.scrollLeft || 0;
		dy = document.documentElement.scrollTop || 0;
	}
	if (document.body) {
		bx = document.body.scrollLeft || 0;
		by = document.body.scrollTop || 0;
	}
	var wx = window.scrollX || 0;
	var wy = window.scrollY || 0;

	var x = Math.max(wx, Math.max(bx, dx));
	var y = Math.max(wy, Math.max(by, dy));

	var speed = 1 + acceleration;
	window.scrollTo(Math.floor(x / speed), Math.floor(y / speed));
	if(x > 0 || y > 0) {
		var invokeFunction = "top.goTop(" + acceleration + ", " + time + ")"
		window.setTimeout(invokeFunction, time);
	}
	return false;
}

//*
function scrollTop(){
	var el = $('gotop');
	var stop = (document.body.scrollTop || document.documentElement.scrollTop);
	if(stop>400){
		if(el.style.display!='block'){ 
			el.style.display='block'; 
			smoothopaque(el, 0, 100, 1); 
		}
	}
	else 
		el.style.display='none';
		
	return false;
}


// установка opacity
function setopacity(el, opacity){
	el.style.opacity = (opacity/100);
	el.style.filter = 'alpha(opacity=' + opacity + ')';
};

if (window.addEventListener){
	window.addEventListener("scroll", scrollTop, false);
	window.addEventListener("load", scrollTop, false);
}
else if (window.attachEvent){
	window.attachEvent("onscroll", scrollTop);
	window.attachEvent("onload", scrollTop);
}	


window['top'] = {};
window['top']['goTop'] = goTop;			
			
})();