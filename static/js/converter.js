function initConverter(conversionType) {
  const fromUnit = document.getElementById('from-unit');
  const toUnit = document.getElementById('to-unit');
  const fromValue = document.getElementById('from-value');
  const toValue = document.getElementById('to-value');
  const resultMessage = document.getElementById('result-message');
  const descResult = document.getElementById('desc-result');
  const errorMessage = document.getElementById('error-message');
  const errorText = document.getElementById('error-text');
  const copyBtn = resultMessage ? resultMessage.querySelector('.copy-btn') : null;

  // Copy to clipboard functionality
  if (copyBtn && !copyBtn.dataset.listenerAdded) {
    copyBtn.dataset.listenerAdded = 'true';
    copyBtn.addEventListener('click', function() {
      const textToCopy = toValue.value;
      if (textToCopy) {
        navigator.clipboard.writeText(textToCopy).then(function() {
          // Visual feedback - briefly change icon or show tooltip
          const originalTitle = copyBtn.getAttribute('title');
          copyBtn.setAttribute('title', typeof translations !== 'undefined' ? translations.copied || 'Copied!' : 'Copied!');
          setTimeout(function() {
            copyBtn.setAttribute('title', originalTitle);
          }, 2000);
        }).catch(function(err) {
          console.error('Failed to copy text: ', err);
        });
      }
    });
  }

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

  fromValue.addEventListener('input', performConversion);
  fromUnit.addEventListener('change', performConversion);
  toUnit.addEventListener('change', performConversion);
}

function initEncoderDecoder(encodeEvent, decodeEvent, resultEvent) {
  const encodeBtn = document.getElementById('encode-btn');
  const decodeBtn = document.getElementById('decode-btn');
  const inputText = document.getElementById('input-text');
  const outputText = document.getElementById('output-text');
  const resultMessage = document.getElementById('result-message');
  const descResult = document.getElementById('desc-result');
  const errorMessage = document.getElementById('error-message');
  const errorText = document.getElementById('error-text');
  const copyBtn = resultMessage ? resultMessage.querySelector('.copy-btn') : null;
  
  let currentMode = 'encode';

  function setMode(mode) {
    currentMode = mode;
    if (mode === 'encode') {
      encodeBtn.classList.add('active');
      decodeBtn.classList.remove('active');
    } else {
      decodeBtn.classList.add('active');
      encodeBtn.classList.remove('active');
    }
    // Clear output when switching modes
    outputText.value = '';
    resultMessage.style.display = 'none';
    errorMessage.style.display = 'none';
  }

  encodeBtn.addEventListener('click', () => setMode('encode'));
  decodeBtn.addEventListener('click', () => setMode('decode'));

  function performConversion() {
    const text = inputText.value.trim();
    if (!text) {
      outputText.value = '';
      resultMessage.style.display = 'none';
      errorMessage.style.display = 'none';
      return;
    }

    const eventName = currentMode === 'encode' ? encodeEvent : decodeEvent;
    socket.emit(eventName, { text: text });
  }

  socket.on(resultEvent, function(data) {
    if (data.success) {
      outputText.value = data.result;
      descResult.textContent = data.result;
      resultMessage.style.display = 'block';
      errorMessage.style.display = 'none';
    } else {
      errorText.textContent = data.error || (typeof translations !== 'undefined' ? translations.error_occurred : 'An error occurred');
      errorMessage.style.display = 'block';
      resultMessage.style.display = 'none';
      outputText.value = '';
    }
  });

  // Copy to clipboard functionality
  if (copyBtn && !copyBtn.dataset.listenerAdded) {
    copyBtn.dataset.listenerAdded = 'true';
    copyBtn.addEventListener('click', function() {
      const textToCopy = outputText.value;
      if (textToCopy) {
        navigator.clipboard.writeText(textToCopy).then(function() {
          const originalTitle = copyBtn.getAttribute('title');
          copyBtn.setAttribute('title', typeof translations !== 'undefined' ? translations.copied || 'Copied!' : 'Copied!');
          setTimeout(function() {
            copyBtn.setAttribute('title', originalTitle);
          }, 2000);
        }).catch(function(err) {
          console.error('Failed to copy text: ', err);
        });
      }
    });
  }

  inputText.addEventListener('input', performConversion);
}
