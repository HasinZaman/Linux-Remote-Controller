var mouseDown = false

var mousePos = [undefined, undefined]
var mouseTap = []

var delta = [undefined, undefined]

//touch pad controls
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

		for(var i1 = 0; i1 < 2; i1++)
		{
			delta[i1] = mousePos[1][i1] - mousePos[0][i1]
		}

		console.log(delta)

		mousePos = [undefined, undefined]
	}

	setTimeout(update, 100)
}

update()
