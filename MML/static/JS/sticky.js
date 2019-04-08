var navbar = document.getElementById("navbar"),
	sticky = navbar.offsetTop;

window.onscroll = function(e) {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}