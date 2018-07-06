# Image2Canvas
Converts an image to a HTML 5 canvas
Will take an image like this one:

![Cat picture](https://raw.githubusercontent.com/EdLynch/Image2Canvas/master/FinishedExample/cat.jpg)

And convert it to a html and js file like below:
```
<!DOCTYPE html>
<html>
<head>
<title>Image to Canvas</title>
</head>
<body>
<canvas id="myCanvas" width="960" height="585"></canvas>
</body>
<script src="script.js"></script>
</html>
```
```
var c = document.getElementById('myCanvas');var ctx = c.getContext('2d');
ctx.beginPath();
ctx.fillRect(0,0,1,1);
ctx.fillStyle = 'rgb(31,37,0)';
ctx.stroke();
ctx.closePath();
ctx.beginPath();
ctx.fillRect(1,0,1,1);
ctx.fillStyle = 'rgb(53,57,20)';
ctx.stroke();
ctx.closePath();
ctx.beginPath();
ctx.fillRect(2,0,1,1);
ctx.fillStyle = 'rgb(65,69,36)';
ctx.stroke();
ctx.closePath();
...
```

It maps the image pixel by pixel to a HTML5 canvas.

You could just use this, but where's the fun in that?
```
ctx.drawImage();
```
