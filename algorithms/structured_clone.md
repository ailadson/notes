# Structured Algorithm Clone

* Alternative to JSON
* Allows the cloning of cyclic graphs, aka objects that reference other other objects that are in the graph
* Allows the cloning of RegEx, Blobs, Files, ImageData, unlike JSON
* Can't clone functions, dom elements, or errors
* Not a deep copy. Doesn't walk up the prototype chain

### The Jist

Look at each field and copy it over. If it's an object, recurse into in and copy those fields over
