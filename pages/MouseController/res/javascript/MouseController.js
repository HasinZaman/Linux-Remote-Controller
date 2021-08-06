var mouseDown = false

var mouseTouch = false
var mousePos = [undefined, undefined]
var mouseTap = []

var delta = [undefined, undefined]

var sensitivity = localStorage['MouseController'] || '1'

sensitivity = parseInt(sensitivity)

$('#sensitivity input').on('input propertychange', 
	function()
	{
		sensitivity = parseInt($('#sensitivity input').val())
		localStorage["MouseController"] = String(sensitivity)
	}
)

//touch pad controls
$("#touchpad").on("vmousedown",
	function(event)
	{
		mouseTouch = true
		mousePos[0] = [event.pageX, event.pageY]
	}
)

$("#touchpad").on("vmousemove", function(event)
	{
		if(mouseTouch)
		{
			mousePos[1] = mousePos[0]
			mousePos[0] = [event.pageX, event.pageY]
		}	
	}
)

$("#touchpad").on("vmouseup", function(event)
	{
		mouseTouch = false
		mousePos = [undefined, undefined]
	}
)

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
			delta[i1] = -1 * (mousePos[1][i1] - mousePos[0][i1])
		}

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
	}

	setTimeout(update, 100)
}

update()
