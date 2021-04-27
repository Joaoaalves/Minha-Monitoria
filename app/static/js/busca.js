listaMonitoriasSalvas = [];
window.onload = initPage;

function initPage(){
  var url_string = window.location.href;
  var url = new URL(url_string);
  var m = url.searchParams.get("m");
  if(m == 1){
    document.getElementById("mySidenav").style.width = "250px";
  }
}

// ABRIR MENU LATERAL
function abrirNav() {
  var url_string = window.location.href;
  var url = new URL(url_string);
  var m = url.searchParams.get("m");
  if(m == 1)
    window.location.href = window.location.href;
  else
    window.location.href = window.location.href + "&m=1";
}

// FECHAR MENU LATERAL
function fecharNav() {
  document.getElementById("mySidenav").style.width = "0";
}

// SALVAR
function salvar(chave, monitoriasSalvas) {
  var verifica = false;
  for(var j=0; j<listaMonitoriasSalvas.length; j++){
    if(listaMonitoriasSalvas[j] == chave){
      verifica = true;
    }
  }
  if(verifica){
    alert("Essa monitoria já foi adicionada");
  }
  else {
    if(monitoriasSalvas.length > 14){
      alert("Armazenamento de monitorias cheio, exclua alguma para abrir mais espaço");
    }
    else{
      var i;
      verifica = false;
      for(i=0; i<monitoriasSalvas.length; i++){
        if(chave == monitoriasSalvas[i]){
          verifica = true;
        }
      }
      if(verifica){
        alert("Essa monitoria já foi adicionada");
      }
      else{
        listaMonitoriasSalvas.push(chave);
        console.log(listaMonitoriasSalvas);
        $.getJSON('/salvar?chave='+chave, function(){});
      }
    }
  }
}

// REMOVER
function remover(chave, monitoriasSalvas) {
  for(var j = 0; j<listaMonitoriasSalvas.length; j++){
    if(listaMonitoriasSalvas[j] == chave){
      listaMonitoriasSalvas[j] = '';
    }
  }
  $.getJSON('/removerMonitoriaSalva?chave='+chave, function(){});
  var url_string = window.location.href;
  var url = new URL(url_string);
  var m = url.searchParams.get("m");
  if(m == 1 || m == 0){
    var temp = window.location.href.toString();
    temp = temp.slice(0, temp.length-4);
    window.location.href = temp;
  }
}