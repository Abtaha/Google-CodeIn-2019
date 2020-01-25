let formatTime = unixTime => {
	let date = new Date(unixTime * 1000);
	let hours = date.getHours();
	let minutes = "0" + date.getMinutes();
	let seconds = "0" + date.getSeconds();

	if (hours > 12) {
		hours -= 12;
		let formattedTime =
			hours + ":" + minutes.substr(-2) + ":" + seconds.substr(-2) + " pm";
		return formattedTime;
	}

	let formattedTime =
		hours + ":" + minutes.substr(-2) + ":" + seconds.substr(-2) + " am";
	return formattedTime;
};

let setDataFuture = (data, unit) => {
	document.getElementById(
		"imageF"
	).innerHTML = `<img src="https://openweathermap.org/img/wn/${data.list[0].weather[0].icon}@2x.png"></img>`;
	document.getElementById("tempF").innerHTML =
		data.list[0].main.temp + (unit === "metric" ? " °C" : " °F");
	document.getElementById("windF").innerHTML =
		"Wind Speed: " +
		data.list[0].wind.speed +
		(unit === "metric" ? " m/s" : " MPH") +
		" Angle: " +
		data.list[0].wind.deg +
		"°";

	if (data.list[0].rain) {
		document.getElementById("rainfallF").innerHTML =
			data.list[0].rain["3h"] + " mm" + " Rain";
	}
};

let setDataCurrent = (data, unit) => {
	document.getElementById(
		"image"
	).innerHTML = `<img src="https://openweathermap.org/img/wn/${data.weather[0].icon}@2x.png"></img>`;
	document.getElementById("temp").innerHTML =
		data.main.temp + (unit === "metric" ? " °C" : " °F");
	document.getElementById("wind").innerHTML =
		"Wind Speed: " +
		data.wind.speed +
		(unit === "metric" ? " m/s" : " MPH") +
		" Angle: " +
		data.wind.deg +
		"°";

	if (data.rain) {
		document.getElementById("rainfall").innerHTML =
			data.rain["1h"] + " mm" + " Rain";
	}
	document.getElementById("sunrise").innerHTML =
		"Sunrise: " + formatTime(data.sys.sunrise);
	document.getElementById("sunset").innerHTML =
		"Sunset: " + formatTime(data.sys.sunset);
};

function fetchData() {
	let apiKey = "44fab34208e6e11b007fd5207deaf1ff";
	let city = document.getElementById("inputCity").value;
	let unit = document.getElementById("inputUnit").value;

	document.getElementsByClassName("mainContainer")[0].style = "display: flex";

	fetch(
		`https://api.openweathermap.org/data/2.5/weather?q=${city}&units=${unit}&appid=${apiKey}`
	)
		.then(function(resp) {
			return resp.json();
		})
		.then(function(data) {
			setDataCurrent(data, unit);
		})
		.catch(function(err) {
			console.log(err);
			alert("Please Enter a valid City, Country and Unit");
		});

	fetch(
		`https://api.openweathermap.org/data/2.5/forecast?q=${city}&units=${unit}&appid=${apiKey}`
	)
		.then(function(resp) {
			return resp.json();	
		})
		.then(function(data) {
			setDataFuture(data, unit);
		})
		.catch(function(err) {
			console.log(err);
			alert("Please Enter a valid City");
		});
}
