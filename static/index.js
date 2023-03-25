function retiraMoedaOutroSelect(selectedValue) {
  var select2 = document.getElementById('moeda_target');
  for (var i = 0; i < select2.options.length; i++) {
    var option = select2.options[i];
    if (option.value === selectedValue) {
      option.disabled = true;
      option.hidden = true;
    } else {
      option.disabled = false;
      option.hidden = false;
    }
  }
}
