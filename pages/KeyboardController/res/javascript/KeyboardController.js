var backspace = false
$("button#backSpace").on("vmousedown",function(){
	if (!backspace)
	{
		backspace = true
	}
})
$("button#backSlash").on("vmouseup",function(){
	backspace = false
})

$("button#enter").click(function(){
	buttonPress("enter")
})

function buttonPress(buttonName)
{
	$.ajax
	({
		type:"POST",
		data:
		{
			page:"KeyboardController",
			action: "buttonPress",
			button: buttonName
		}
	})
}

function update()
{
	var keySequence = ""

	if(backspace)
	{
		buttonPress("backspace")
	}

	if($("#keyboardInput").val() !== "" && $("#keyboardInput").val() !== undefined)
	{
		$.ajax
		({
			type:"POST",
			data:
			{
				page: "KeyboardController",
				action: "keySequence",
				keySequence: $("#keyboardInput").val()
			}
		})

		$("#keyboardInput").val("")
	}

	setTimeout(update, 100)
}

update()