// COMPARTILHAR
function compartilhar() {
  document.getElementById("containerDropdown").classList.toggle("show");
}

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