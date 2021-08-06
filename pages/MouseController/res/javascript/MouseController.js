var mouseDown = false

var mousePos = [undefined, undefined]
var mouseTap = []

var delta = [undefined, undefined]

//touch pad controls
$("#touchpad").on("touchstart",function(event){
	mousePos[0] = [event.pageX, event.pageY]
})

$("#touchpad").on("touchmove",function(event){
	mousePos[1] = mousePos[0]
	mousePos[0] = [event.pageX, event.pageY]
})

//left click
$("#leftClick").on("vmousedown",function(event){
	buttonPress("leftDown")
})

$("#leftClick").on("vmouseup",function(event){
	buttonPress("leftUp")
})

//right click
$("#rightClick").on("vmousedown",function(event){
	buttonPress("rightUp")
})

$("#rightClick").on("vmouseup",function(event){
	buttonPress("rightDown")
})

function buttonPress(buttonName)
{
	$.ajax
	({
		type:"POST",
		data:
		{
			page:"MouseController",
			action: "buttonPress",
			button: buttonName
		}
	})
}

function update()
{
	if(mousePos[0] != undefined && mousePos[1] != undefined)
	{
		for(var i1 = 0; i1 < 2; i1++)
		{
			delta[i1] = mousePos[1][i1] - mousePos[0][i1]
		}
		console.log(delta)
		$.ajax
		({
			type:"POST",
			data:
			{
				page:"MouseController",
				action: "move",
				deltaX: delta[0],
				deltaY: delta[1],
			}
		})

		mousePos = [undefined, undefined]
	}

	setTimeout(update, 100)
}

update()
