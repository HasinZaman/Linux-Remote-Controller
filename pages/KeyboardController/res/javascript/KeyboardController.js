
function update()
{
	var keySequence = ""

	if($("#keyboardInput").val() != "")
	{
		keySequence = $("#keyboardInput").val()

		console.log(keySequence)

		$("#keyboardInput").val("")
	}

	setTimeout(update, 100)
}