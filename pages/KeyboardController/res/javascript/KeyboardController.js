
function update()
{
	var keySequence = ""

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