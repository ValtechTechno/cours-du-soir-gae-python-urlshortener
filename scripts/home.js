(function() {
   if (!window.addEventListener) return;
	window.addEventListener("load", function() {

		ZeroClipboard.setMoviePath('scripts/ZeroClipboard.swf');

		if (!document.querySelectorAll) return;

		var links = document.querySelectorAll('.shorturl');
		for(var i = 0; i < links.length; i++) {
			// Add host to link
			links[i].innerHTML = window.location.protocol + '//' + window.location.host + links[i].innerHTML;

			// Add code to copy to clipboard
			var clip = new ZeroClipboard.Client();
         clip.setText(links[i].innerHTML);
			clip.glue(links[i].nextSibling);
		}

	}, false)
})();
