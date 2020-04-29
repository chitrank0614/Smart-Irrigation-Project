//python api url
api_url = "http://127.0.0.1:5000";

function deleteCookies() {
	setCookie("username", "", -1);
}

function setCookie(cname, cvalue, exdays) {
	var dt = new Date();
	dt.setTime(dt.getTime() + exdays * 24 * 60 * 60 * 1000);
	var expires = "expires=" + dt.toUTCString();
	document.cookie = cname + "=" + cvalue + "; " + expires;
}
function getCookie(cname) {
	var name = cname + "=";
	var ca = document.cookie.split(";");
	for (var i = 0; i < ca.length; i++) {
		var c = ca[i];
		while (c.charAt(0) == " ") c = c.substring(1);
		if (c.indexOf(name) == 0) return c.substring(name.length, c.length);
	}
	return "";
}
function checkCookie() {
	username = getCookie("username");
	if (username != "") {
		return true;
	} else {
		return false;
	}
}

async function getSiteNameLogo() {
	response = await makeAsyncPostRequest("/get-site-name-logo", {});
	document.getElementById("logo").src = response.result["Logo"];
	document.getElementById("brandName").innerHTML = response.result["Name"];
}

function logout() {
	deleteCookies();
	location.replace("index.html");
}

function makeAsyncGetRequest(path) {
	return new Promise(function (resolve, reject) {
		axios.get(api_url + path).then(
			(response) => {
				var returnObj = response.data;
				resolve(returnObj);
			},
			(error) => {
				reject(error);
			}
		);
	});
}

function makeAsyncPostRequest(path, queryObject) {
	return new Promise(function (resolve, reject) {
		axios.post(api_url + path, queryObject).then(
			(response) => {
				var returnObj = response.data;
				console.log("Async Post Request");
				resolve(returnObj);
			},
			(error) => {
				reject(error);
			}
		);
	});
}

function makeGetRequest(path) {
	axios.get(api_url + path).then(
		(response) => {
			var returnObj = response.data;
			return returnObj;
		},
		(error) => {
			return error;
		}
	);
}

function makePostRequest(path, queryObject) {
	axios.post(api_url + path, queryObject).then(
		(response) => {
			var returnObj = response.data;
			return returnObj;
		},
		(error) => {
			return error;
		}
	);
}

function topNavToggle() {
	var x = document.getElementById("topNav");
	if (x.className === "topnav") {
		x.className += " responsive";
	} else {
		x.className = "topnav";
	}
}
