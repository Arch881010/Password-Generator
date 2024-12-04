/** @format */

document.addEventListener("DOMContentLoaded", function () {
	const passwordForm = document.getElementById("passwordForm");
	passwordForm.addEventListener("submit", function (event) {
		event.preventDefault();

		const salt = document.getElementById("salt").value;
		const length = document.getElementById("length").value;
		const pepper = document.getElementById("pepper").value;

		const data_url = `${window.location.origin}/generate?salt=${salt}&length=${length}&pepper=${pepper}`;

		fetch(data_url)
			.then((response) => response.json())
			.then((data) => {
				const password = data.password;
				document.getElementById("generatedPassword").textContent = password;
				console.log(password);
			})
			.catch((error) => {
				console.error("Error:", error);
			});
	});

	const copyPasswordButton = document.getElementById("copyPassword");
	copyPasswordButton.addEventListener("click", function () {
		const generatedPassword =
			document.getElementById("generatedPassword").textContent;
		navigator.clipboard
			.writeText(generatedPassword)
			.then(() => {
				alert("Password copied to clipboard!");
			})
			.catch((err) => {
				console.error("Failed to copy password: ", err);
			});
	});
});
