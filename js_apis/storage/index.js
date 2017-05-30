let localGetInput = document.getElementById('local-get'),
    localGetValue = document.getElementById('local-get-val'),
    localGetBtn = document.getElementById('local-get-btn'),
    localSetKey = document.getElementById('local-set-key'),
    localSetVal = document.getElementById('local-set-val'),
    localSetBtn = document.getElementById('local-set-btn');

let sessionGetInput = document.getElementById('session-get'),
    sessionGetValue = document.getElementById('session-get-val'),
    sessionGetBtn = document.getElementById('session-get-btn'),
    sessionSetKey = document.getElementById('session-set-key'),
    sessionSetVal = document.getElementById('session-set-val'),
    sessionSetBtn = document.getElementById('session-set-btn');

localGetBtn.addEventListener('click', () => {
  let key = localGetInput.value;
  let val = localStorage.getItem(key);
  localGetValue.innerHTML = val;
});

localSetBtn.addEventListener('click', () => {
  let key = localSetKey.value;
  let val = localSetVal.value;
  localStorage.setItem(key, val);
  localSetKey.value = "";
  localSetVal.value = "";
});

sessionGetBtn.addEventListener('click', () => {
  let key = sessionGetInput.value;
  let val = sessionStorage.getItem(key);
  sessionGetValue.innerHTML = val;
});

sessionSetBtn.addEventListener('click', () => {
  let key = sessionSetKey.value;
  let val = sessionSetVal.value;
  sessionStorage.setItem(key, val);
  sessionSetKey.value = "";
  sessionSetVal.value = "";
});
