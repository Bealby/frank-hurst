// Get the newsModal
var newsModal = document.getElementById("newsModal");

// Get the button that opens the newsModal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the newModal
var span = document.getElementsByClassName("news-close")[0];

// When the user clicks the button, open the newsModal 
btn.onclick = function () {
    newsModal.style.display = "block";
}

// When the user clicks on <span> (x), close the newsModal
span.onclick = function () {
    newsModal.style.display = "none";
}

// When the user clicks anywhere outside of the newsModal, close it
window.onclick = function (event) {
    if (event.target == newsModal) {
        newsModal.style.display = "none";
    }
}