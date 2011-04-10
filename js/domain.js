(function() {
   if (!window.addEventListener) return;
	window.addEventListener("load", function() {
		if (!document.querySelectorAll) return;
		var links = document.querySelectorAll('a.shorturl');
		for(var i = 0; i < links.length; i++) {
			links[i].innerHTML = window.location.protocol + '//' + window.location.host + links[i].innerHTML;
		}
	}, false)
})();
