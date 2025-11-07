function initConverter(conversionType) {
  const convertBtn = document.getElementById('convert-btn');
  const clearBtn = document.getElementById('clear-btn');
  const fromUnit = document.getElementById('from-unit');
  const toUnit = document.getElementById('to-unit');
  const fromValue = document.getElementById('from-value');
  const toValue = document.getElementById('to-value');
  const resultMessage = document.getElementById('result-message');
  const descResult = document.getElementById('desc-result');
  const errorMessage = document.getElementById('error-message');
  const errorText = document.getElementById('error-text');

  socket.on('conversion_result', function(data) {
    if (data.success) {
      toValue.value = data.short_result;
      descResult.textContent = data.desc_result;
      resultMessage.style.display = 'block';
      errorMessage.style.display = 'none';
    } else {
      errorText.textContent = data.error || (typeof translations !== 'undefined' ? translations.error_occurred : 'An error occurred during conversion');
      errorMessage.style.display = 'block';
      resultMessage.style.display = 'none';
      toValue.value = '';
    }
  });

  function performConversion() {
    const value = parseFloat(fromValue.value);
    if (isNaN(value)) {
      errorText.textContent = typeof translations !== 'undefined' ? translations.enter_valid_number : 'Please enter a valid number';
      errorMessage.style.display = 'block';
      resultMessage.style.display = 'none';
      toValue.value = '';
      return;
    }
    if (value === 0 && fromValue.value.trim() !== '0') {
      toValue.value = '';
      resultMessage.style.display = 'none';
      errorMessage.style.display = 'none';
      return;
    }

    socket.emit(conversionType, {
      from_unit: fromUnit.value,
      to_unit: toUnit.value,
      from_value: value
    });
  }

  convertBtn.addEventListener('click', performConversion);

  clearBtn.addEventListener('click', function() {
    fromValue.value = '';
    toValue.value = '';
    resultMessage.style.display = 'none';
    errorMessage.style.display = 'none';
  });

  fromValue.addEventListener('input', performConversion);
  fromUnit.addEventListener('change', performConversion);
  toUnit.addEventListener('change', performConversion);
}
