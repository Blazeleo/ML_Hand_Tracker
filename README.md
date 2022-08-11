# ML Hand Tracker

A Unity and python based project that gets a person's hand position using OpenCV and renders a virtual hand onto unity. This virtual hand can interact with all kinds of elements in the virtual environment.

![Demo](https://i.ibb.co/1Mynmh3/ezgif-com-gif-maker.gif)

## Tech Stack
 - Open CV With Python
 - Unity
## Working
We need to run the python file in the background to run the OpenCV image recognition service. The data generated is then sent over a UDP connection to the unity environment, which uses the coordinate data for each finger to render out a virtual hand. This is all done in realtime as well
