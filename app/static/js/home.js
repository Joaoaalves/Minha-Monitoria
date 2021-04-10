// ABRIR MENU LATERAL
function abrirNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

// FECHAR MENU LATERAL
function fecharNav() {
  document.getElementById("mySidenav").style.width = "0";
}

// SALVAR
var listaMonitoriasSalvas = [];
function salvar(chave, monitoriasSalvas) {
  if(monitoriasSalvas.length > 14){
    alert("Armazenamento de monitorias cheio, exclua alguma para abrir mais espaço");
  }
  else{
    var i, verifica = false;
    for(i=0; i<monitoriasSalvas.length; i++){
      if(chave == monitoriasSalvas[i])
        verifica = true;
    }
    if(verifica)
      alert("Monitoria já foi adicionada");
    else{      
      //// Parte do codigo para evitar a realizacao do reload a cada adicao/remocao de monitoria da lista de monitorias salvas
      // listaMonitoriasSalvas.push(chave);

      $.getJSON('/salvar?chave='+chave, function(){});
      window.location.reload(false);
    }
  }
}

// REMOVER
function remover(chave, monitoriasSalvas) {

  //// Parte do codigo para evitar a realizacao do reload a cada adicao/remocao de monitoria da lista de monitorias salvas
  // var i;
  // var tempListaMonitoriasSalvas = [];
  // for(i=0; i<listaMonitoriasSalvas.length; i++){
  //   if(listaMonitoriasSalvas[i] == chave)
  //     continue;
  //   tempListaMonitoriasSalvas.push(listaMonitoriasSalvas[i]);
  // }
  // listaMonitoriasSalvas = tempListaMonitoriasSalvas;

  $.getJSON('/removerMonitoriaSalva?chave='+chave, function(){});
  window.location.reload(false);
}