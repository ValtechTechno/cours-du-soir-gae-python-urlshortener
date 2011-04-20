(function() {
   if (!window.addEventListener) return;
	if (!document.querySelectorAll) return;

	window.addEventListener("load", function() {

		var osWichDoesntSupportInputSelection = navigator.userAgent.match(/iPhone/i) || navigator.userAgent.match(/iPad/i) || navigator.userAgent.match(/iPod/i);
		var notification = document.getElementById('notification');

		var links = document.querySelectorAll('.shorturl');
		for(var i = 0; i < links.length; i++) {

			var el = links[i];

			if (!osWichDoesntSupportInputSelection) {
				if (el.nodeName == 'A') {
					el.style.display = 'none';
				} else if (el.nodeName == 'INPUT') {
					el.style.display = el.nextSibling.style.display = 'inline';

					(function() {
						var input = el;
						el.nextSibling.addEventListener("click", function() { 
							input.select();
							notification.style.top = '-40px';
							showSlowly();
							window.setTimeout(hideSlowly, 4000);
						}, false);
					})();
				}
			}
		}

		var showSlowly = function() {
			notification.style.top = (parseInt(notification.style.top, 10) + 5) + 'px';
			if (parseInt(notification.style.top, 10) < 0)
				setTimeout(showSlowly, 10);
		};


		var hideSlowly = function() {
			notification.style.top = (parseInt(notification.style.top, 10) - 5) + 'px';
			if (parseInt(notification.style.top, 10) > -40)
				setTimeout(hideSlowly, 10);
		};

	}, false)
})();
