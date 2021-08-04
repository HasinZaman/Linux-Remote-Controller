volumeUpCond = false
volumeDownCond = false
volume = 0

portraitMode = true

//volume up and down buttons are hold
$("button#volumeUp").on("vmousedown",function(){
	if (!volumeDownCond)
	{
		volumeUpCond = true

		$(this).attr("data-pressCond",1)
	}
})
$("button#volumeDown").on("vmousedown",function(){
	if (!volumeUpCond)
	{
		volumeDownCond = true

		$(this).attr("data-pressCond",1)
	}
})

//volume up and down buttons are released
$("button#volumeUp").on("vmouseup",function(){
	volumeUpCond = false

	$(this).attr("data-pressCond",0)
})
$("button#volumeDown").on("vmouseup",function(){
	volumeDownCond = false

	$(this).attr("data-pressCond",0)
})

//volume mute
$("button#volumeMute").click(function(){
	buttonPress("toggleMute")
})
$("button#playPause").click(function(){
	buttonPress("togglePlayPause")
})

function buttonPress(buttonName)
{
	$.ajax
	({
		type:"POST",
		data:
		{
			page:"VolumeController",
			action:"buttonPress",
			button:buttonName
		}
	})
}

function getState()
{
	$.ajax
	({
		type:"POST",
		data:
		{
			page:"VolumeController",
			action:"getState"
		},
		success: getStateResponse
	})
}

var tmp
function getStateResponse(result)
{
	tmp = result
	//console.log(result)

	volume = result["volume"]
	if(result["muted"])
	{
		$("button#volumeMute").attr("data-pressCond",1)
	}
	else
	{
		$("button#volumeMute").attr("data-pressCond",0)
	}
	setTimeout(update, 100)
}

function update()
{
	if($("button#volumeUp").attr("data-pressCond") == 1){
		buttonPress("increaseVolume")
		$("button#volumeMute").attr("data-pressCond",0)
	}else if($("button#volumeDown").attr("data-pressCond") == 1){
		buttonPress("decreaseVolume")
		$("button#volumeMute").attr("data-pressCond",0)
	}

	portraitMode = window.screen.width <= window.screen.height

	if(portraitMode)
	{
		$("#volumeBar").css("width", volume+"%")
	}
	else
	{
		$("#volumeBar").css("height", volume+"%")
	}

	$("button[data-pressCond=1]").addClass("pressed")
	$("button[data-pressCond=0]").removeClass("pressed")

	if($("button#volumeMute").attr("data-pressCond") == 1)
	{
		$("#volumeBar").addClass("muted")
	}
	else
	{
		$("#volumeBar").removeClass("muted")
	}

	getState()
}

update()