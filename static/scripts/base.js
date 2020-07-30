$(window).resize(function() {
	if (window.innerWidth < 768) {
		let actions = document.getElementById('shortUrlActions');
		let arr = actions.className.split(" ");
	  
	  if (arr.indexOf('mt-2') == -1) {
	    actions.className += " mt-2";
		}
		if (arr.indexOf('resultAction') != -1) {
	    actions.className = actions.className.replace('resultAction', '');
		}
	}

	if (window.innerWidth >= 768) {
		let actions = document.getElementById('shortUrlActions');
		let arr = actions.className.split(" ");
	  
	  if (arr.indexOf('resultAction') == -1) {
	    actions.className += " resultAction";
		}
		if (arr.indexOf('mt-2') != -1) {
	    actions.className = actions.className.replace('mt-2', '');
		}
	}
});


$(document).on('submit', '#shortenerForm', function(e) {
	e.preventDefault();

	$.ajax({
		type: 'POST',
		url: 'shorten/',

		data: {
			"long_url": $('#longUrl').val()
		},

		success: function(response) {
			let data = JSON.parse(response, null);
			if (data != null){
				$('#shortUrlDiv').css('display', 'block');
				$('#shortUrl').val(data['shortUrl']);
				$('#goShortUrl').attr('href', data['shortUrl']);
			}
		},

		error: function(jqXHR) {
			alert("Status: " + jqXHR.status + " " + jqXHR.statusText
      +"\nPlease try again later.");
		}
	});
});


function copyUrl() {
  /* Get the text field */
  let urlField = document.getElementById("shortUrl");

  /* Select the text field */
  urlField.select();
  urlField.setSelectionRange(0, 99999); /*For mobile devices*/

  /* Copy the text inside the text field */
  try {
    var successful = document.execCommand('copy');
    var msg = successful ? 'successful' : 'unsuccessful';
    console.log('Fallback: Copying text command was ' + msg);
  } catch (err) {
    console.error('Fallback: Oops, unable to copy', err);
  }

  let btn = document.getElementById("copyUrlBtn");
  btn.innerHTML = 'Copied';
  btn.className = btn.className.replace('info', 'success');
}

function hideShortUrl() {
	document.getElementById('shortUrlDiv').style.display = 'none';
	let btn = document.getElementById("copyUrlBtn");
    btn.innerHTML = 'Copy';
    btn.className = btn.className.replace('success', 'info');
}

