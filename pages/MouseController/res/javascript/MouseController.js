var mouseDown = false

var mousePos = [undefined, undefined]

$("body").on("vmousedown",function(event){
	mousePos[0] = event
})

$("body").on("vmouseup",function(event){
	mousePos[1] = event
})

function update()
{
	if(mousePos[0] != undefined && mousePos[1] != undefined)
	{
		console.log(mousePos)
		mousePos = [undefined, undefined]
	}
}
