## Fullscreen

- method attached to DOM element
- vendor-prefixed :(
  - webkit, moz
- `element#[prefix]requestFull(s||S)creen`
- avoid fullscreen-ing the body element. Causes odd behavior

## Page Visibility

- lets dev know when user has switch windows or tabs
- can save resources (animation/ajax)
- vendor-prefixed :(
  - webkit, moz, ms
- a document event called `[prefix]visibilitychange`, determined by `document.[prefix](h/H)idden`

## GetUserMedia

- gives dev access to users audio-visual devices (camera and mic)
- `navigator.mediaDevices.getUserMedia(constraints)`
  - returns a promise
  - `constraints` is an object specifying the type and requirements of the media. see [here](https://developer.mozilla.org/en-US/docs/Web/API/MediaStreamConstraints) and [here](https://developer.mozilla.org/en-US/docs/Web/API/MediaTrackConstraints)
  - errors include: NotAllowedError, NotFoundError, NotReadableError, OverConstrainedError
  - old API was `navigator.getUserMedia(cb, err)`. Use [polyfill](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia) for most compatibility

## Performance + User Timing + Navigation Timing

- very high-resolution monotonic clock and performance stats
- `performance.now()`
- `performance.navigation`
- `performance.timing`
- `performance.mark(name)`
- `performance.measure(name, start, end)`
- Getting Entries'


## Web Workers

- `new Worker(url_to_worker)`
- messages are sent between worker and parent through `postMessage`
- messages are received between worker and parent through `onmessage`
- Stop a worker by `worker.terminate()` or internally as `close()`
- More workers will give diminished returns. Keep to around `navigator.hardwareConcurrency`
- Workers have access to the `importScripts(url[s])` function. runs code in `url[s]`
- `SharedWorker`s
  - communicate via a port object

## Local + Session Storage

- API to manipulate storage object in browser
- Local storage has no expiration date
- Session storage last until browser is closed
- Storage Object
  - `length`
  - `key(n)`
  - `getItem(key)`
  - `setItem(key, value)`
  - `removeItem(key)`
  - `clear()`

## IndexDB

- transactional database system that store large files, blobs, and other structured data
- uses indexes for fast high-performance lookup
- stores objects supported by the structured clone algorithm (see below)
- Flow:
  * Specify Schema
  * Open DB connection
  * Make transactions

### Structured Algorithm Clone

* Alternative to JSON
* Allows the cloning of cyclic graphs, aka objects that reference other other objects that are in the graph
* Allows the cloning of RegEx, Blobs, Files, ImageData, unlike JSON
* Can't clone functions, dom elements, or errors
* Not a deep copy. Doesn't walk up the prototype chain

**The Jist**: Look at each field and copy it over. If it's an object, recurse into in and copy those fields over

## Service Workers [TODO]

- API for making offline a better experience
- specify a default offline experience w/ a cache


## Web Sockets [TODO]

- require client server coordination
- client
- server

## Vibrate

- `navigator.vibrate(ms/pattern)`
- return false if not using a phone
