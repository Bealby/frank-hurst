// Scroll To Top START

function scrollFunction() {
    var myScrollToTopBtn = document.getElementById("page-top-link");
    if (window.pageYOffset > 700) {
        myScrollToTopBtn.style.display = "block";
        myScrollToTopBtn.style.visibility = "visible";
    } else {
        myScrollToTopBtn.style.display = "none";
        myScrollToTopBtn.style.visibility = "hidden";
    }
}

window.onscroll = function () { scrollFunction() };

function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}