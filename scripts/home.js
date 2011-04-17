(function() {

   if (!window.addEventListener) return;
	window.addEventListener("load", function() {

		if (!document.querySelectorAll) return;

		var notification = document.getElementById('notification');

		var links = document.querySelectorAll('.shorturl');
		for(var i = 0; i < links.length; i++) {
			(function() {
				var input = links[i];
				input.value = window.location.protocol + '//' + window.location.host + input.value;

				input.nextSibling.addEventListener("click", function(evt) { 
					input.select();
					notification.style.top = '-40px';
					showSlowly();
					window.setTimeout(hideSlowly, 4000);
				}, false);
			})();
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
