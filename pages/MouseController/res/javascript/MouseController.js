var mouseDown = false

var mousePos = [undefined, undefined]
var mouseTap = []

$("#touchpad").on("vmousedown",function(event){
	mousePos[0] = [event.pageX, event.pageY]
})

$("#touchpad").on("vmouseup",function(event){
	mousePos[1] = [event.pageX, event.pageY]
})

function update()
{
	if(mousePos[0] != undefined && mousePos[1] != undefined)
	{
		console.log(mousePos)
		mousePos = [undefined, undefined]
	}
}
