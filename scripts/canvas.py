#!bin/env/python3

from IPython.display import HTML, Image
from google.colab.output import eval_js
from base64 import b64decode

canvas_html = """

<style>
  .colors-buttons div {
      width: 30px;
      height: 30px;
      margin: 2px;
      position:bottom}
  div {
      display: flex;
  }
  .canvas div {
    display: flex-grow;
  }

  canvas{border:1px solid black !important;}
</style>

<div class="canvas">
<canvas width=%d height=%d></canvas>
</div>

<div class="colors-buttons">
  <div class="color" style="background-color: #000000;" id-color="#000000"></div>
  <div class="color" style="background-color: #FFFFFF;" id-color="#FFFFFF"></div>
  <div class="color" style="background-color: #FFFF00;" id-color="#FFFF00"></div>
  <div class="color" style="background-color: #FF00FF;" id-color="#FF00FF"></div>
  <div class="color" style="background-color: #00FFFF;" id-color="#00FFFF"></div>
  <div class="color" style="background-color: #FF0000;" id-color="#FF0000"></div>
  <div class="color" style="background-color: #0000FF;" id-color="#0000FF"></div>
  <div class="color" style="background-color: #00FF00;" id-color="#00FF00"></div>
</div>

<button>Finish</button>


<script>



var canvas = document.querySelector('canvas')
var ctx = canvas.getContext('2d')
ctx.strokeStyle = 'black';
ctx.lineWidth = %d


var button = document.querySelector('button')
var mouse = {x: 0, y: 0}
canvas.addEventListener('mousemove', function(e) {
  mouse.x = e.pageX - this.offsetLeft
  mouse.y = e.pageY - this.offsetTop
})

canvas.onmousedown = ()=>{
  ctx.beginPath()
  ctx.moveTo(mouse.x, mouse.y)
  canvas.addEventListener('mousemove', onPaint)
}
canvas.onmouseup = ()=>{
  canvas.removeEventListener('mousemove', onPaint)
}
var onPaint = ()=>{
  ctx.lineTo(mouse.x, mouse.y)
  ctx.stroke()
}

const colors = document.getElementsByClassName('color');
Array.from(colors).forEach(color => {
    color.addEventListener('click', (event) => {
        const colorSelected = event.target.getAttribute('id-color');
        ctx.strokeStyle = colorSelected;
    });
});

var data = new Promise(resolve=>{
  button.onclick = ()=>{
    resolve(canvas.toDataURL('image/png'))
  }
})
</script>
"""

def draw(filename='drawing.png', w=600, h=300, line_width=1):
  display(HTML(canvas_html % (w, h, line_width)))
  data = eval_js("data")
  binary = b64decode(data.split(',')[1])
  with open(filename, 'wb') as f:
    f.write(binary)
  return len(binary)