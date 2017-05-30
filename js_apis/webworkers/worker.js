importScripts('other.js');

onmessage = (e) => {
  let max = e.data.countTo;
  let i = 0;

  while(i++ < max) console.log(i);

  postMessage("Done with worker!");
}
