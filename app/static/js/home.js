// COMPARTILHAR
function compartilhar() {
  document.getElementById("containerDropdown").classList.toggle("show");
}

// User Container
user_container = document.getElementById("user-container");
user_btn = document.getElementById("user-btn");
user_btn.onclick = function(){
    user_container.style.display = "inline-block";
}
$(document).mouseup(function(e) 
{
    var container = $(user_container);
    if (!container.is(e.target) && container.has(e.target).length === 0) 
    {
        container.hide();
    }
});

window.onclick = function(event) {
  if (!event.target.matches('.botaoCompartilhar')) {
    var dropdowns = document.getElementsByClassName("containerDropdown");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}

// ABRIR MENU LATERAL
function abrirNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

// FECHAR MENU LATERAL
function fecharNav() {
  document.getElementById("mySidenav").style.width = "0";
}

// SALVAR
$(function salvar(chave) {
	$('a#test').on('click', function(e) {
		alert("Salvar")
		e.preventDefault()
		$.getJSON('/salvar?chave='+chave, function(data) {});
		return false;
	});
});