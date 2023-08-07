/*jslint devel: true */
/*jslint browser: true*/
/*global window*/
/*global $*/
/*global document*/   

window.addEventListener("scroll", function () {
    "use strict";
    var cover = document.getElementById("cover");
    if (window.scrollY > 100 && window.scrollY < 275) {
        cover.style.backgroundColor = '#0005';
    } else if (window.scrollY > 275 && window.scrollY < 550) {
        cover.style.backgroundColor = '#000A';
    } else if (window.scrollY > 550) {
        cover.style.backgroundColor = '#000';
    } else {
        cover.style.backgroundColor = '#0000';
    }
});

window.addEventListener("scroll", function () {
	"use strict";
    cover.classList.toggle("cover-no-visible", window.scrollY > viewportToPixels('75vh'));
});

function viewportToPixels(value) {
    var parts = value.match(/([0-9\.]+)(vh|vw)/)
    var q = Number(parts[1])
    var side = window[['innerHeight', 'innerWidth'][['vh', 'vw'].indexOf(parts[2])]]
    return side * (q/100)
}