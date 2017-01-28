let worker = new Worker('worker.js');

worker.postMessage({ countTo : Math.floor(Math.random() * 10)  });

worker.onmessage = (e) => {
  console.log(e.data);
}

console.log("Main Thread Done!");
