/*jslint devel: true */
/*jslint browser: true*/
/*global window*/
/*global $*/
/*global document*/

$(document).ready(function () {
 "use strict";
 var menuClr = $('.wedge'), colorBody = $('body');
 menuClr.click(function () {
		if (colorBody.hasClass('dark')) { colorBody.addClass('light'); colorBody.removeClass('dark'); } else { colorBody.addClass('dark'); colorBody.removeClass('light'); }
	});
});

$(document).ready(function () {
 "use strict";
 var menuBtn = $('.btn-menu'), ind = $('.navigation-items');
 menuBtn.click(function () {
		if (ind.hasClass('navigation-inactive')) { ind.addClass('navigation-active'); ind.removeClass('navigation-inactive'); }
	});
});

$(document).ready(function () {
 "use strict";
 var menuSrx = $('.icon-search'), srx = $('.search');
 menuSrx.click(function () {
		if (srx.hasClass('search-invisible')) { srx.addClass('search-visible'); srx.removeClass('search-invisible'); } else { srx.addClass('search-invisible'); srx.removeClass('search-visible'); }
	});
});

$(document).ready(function () {
 "use strict";
 var clseSrx = $('.close-search'), srx = $('.search');
 clseSrx.click(function () {
		if (srx.hasClass('search-visible')) { srx.addClass('search-invisible'); srx.removeClass('search-visible'); }
	});
});

$(document).ready(function () {
 "use strict";
 var clseNav = $('.close-navigation'), nav = $('.navigation-items');
 clseNav.click(function () {
		nav.addClass('navigation-inactive');
		nav.removeClass('navigation-active');
	});
});

window.onload = function () {
	"use strict";
	var carga = document.getElementById('my-loader-page');
	carga.style.visibility = 'hidden';
	carga.style.opacity = '0';
};

$(document).ready(function () {
	"use strict";
	var buscador = $('#table').DataTable();
 $("#input-search").keyup(function () {
  buscador.search($(this).val()).draw();
  if ($("#input-search").val() === "") {
   $(".content-search").fadeOut(300);
  } else {
   $(".content-search").fadeIn(300);
  }
 });
});

window.addEventListener("scroll", function () {
	"use strict";
	var header = document.getElementById("navigation");
	header.classList.toggle("top", window.scrollY > 100);
});

window.addEventListener("scroll", function () {
	"use strict";
	var header = document.getElementById("navigation");
	header.classList.toggle("sticky", window.scrollY > 0);
});

var lastScrollTop = 0;
window.addEventListener("scroll", function () {
	"use strict";
	var nav = document.getElementById("navigation"), srx = $('.search'), ntn = $('.navigation'), ind = $('.navigation-items'), st = window.pageYOffset || document.documentElement.scrollTop;
	if (st > lastScrollTop && (ind.hasClass('navigation-inactive')) && (srx.hasClass('search-invisible') && (ntn.hasClass('top')))) {
		ntn.addClass('invisible');
		ntn.removeClass('visible');
		nav.style.transition = '0.33s';
	} else {
		ntn.addClass('visible');
		ntn.removeClass('invisible');
	}
	lastScrollTop = st;
}, false);

x = Math.round(getRandom() * 10)
switch( x ) {
	case 2:
		document.documentElement.style.setProperty('--main-bright-color', 'var(--bright-red)');
		document.documentElement.style.setProperty('--main-dark-color', 'var(--dark-red)');
		break;
	case 4:
		document.documentElement.style.setProperty('--main-bright-color', 'var(--bright-green-two)');
		document.documentElement.style.setProperty('--main-dark-color', 'var(--dark-green-two)');
		break;
	default:
		document.documentElement.style.setProperty('--main-bright-color', 'var(--bright-blue-two)');
		document.documentElement.style.setProperty('--main-dark-color', 'var(--dark-blue-two)');	
}

function getRandom() {
	return Math.random();
}

