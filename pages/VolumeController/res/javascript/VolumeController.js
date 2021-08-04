volumeUpCond = false
volumeDownCond = false
volume = 0

//volume up and down buttons are hold
$("button#volumeUp").bind("vmousedown",function(){
	if (!volumeDownCond)
	{
		volumeUpCond = true

		$(this).attr("data-pressCond",1)
	}
})

$("button#volumeDown").bind("vmousedown",function(){
	if (!volumeUpCond)
	{
		volumeDownCond = true

		$(this).attr("data-pressCond",1)
	}
})

//volume up and down buttons are released
$("button#volumeUp").bind("vmouseup",function(){
	volumeUpCond = false

	$(this).attr("data-pressCond",0)
})

$("button#volumeDown").bind("vmouseup",function(){
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
$("button#skipNext").click(function(){
	buttonPress("skipNext")
})
$("button#skipPrev").click(function(){
	buttonPress("skipPrev")
})

function buttonPress(buttonName)
{
	$.ajax
	({
		type:"POST",
		data:
		{
			page:"VolumeController",
			action: "buttonPress",
			button: buttonName
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

function getStateResponse(result)
{
	var tmp = JSON.parse(result)
	//console.log(result)

	volume = tmp["volume"]
	if(tmp["muted"])
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
	}else if($("button#volumeDown").attr("data-pressCond") == 1){
		buttonPress("decreaseVolume")
	}

	$("#volumeBar").css("width", volume+"%")
	$("#volumeBar").css("height", volume+"%")

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