let videos = document.getElementsByTagName('video');

if(navigator.mediaDevices.getUserMedia) {
  let prom = navigator.mediaDevices.getUserMedia({ video : true });
  prom.then((stream) => {
    Array.from(videos).forEach(vid =>{
      vid.srcObject = stream;
      vid.play();
    })
  });
}
