function requestFullscreen (element) {
  if(element.requestFullscreen) {
    element.requestFullscreen();
  } else if(element.mozRequestFullScreen) {
    element.mozRequestFullScreen();
  } else if(element.webkitRequestFullscreen) {
    element.webkitRequestFullscreen();
  } else if(element.msRequestFullscreen) {
    element.msRequestFullscreen();
  }
}

function exitFullscreen() {
  if(document.exitFullscreen) {
    document.exitFullscreen();
  } else if(document.mozCancelFullScreen) {
    document.mozCancelFullScreen();
  } else if(document.webkitExitFullscreen) {
    document.webkitExitFullscreen();
  }
}

let body = document.body,
    section = document.getElementsByTagName('section')[0],
    div = document.getElementsByTagName('div')[0];

body.addEventListener('click', () => {
  requestFullscreen(body);
});

section.addEventListener('click', (e) => {
  // e.stopPropagation();
  requestFullscreen(section);
});

div.addEventListener('click', (e) => {
  // e.stopPropagation();
  requestFullscreen(div);
});
