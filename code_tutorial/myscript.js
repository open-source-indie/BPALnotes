document.querySelectorAll('.btn').forEach(element => {
	element.addEventListener('click', () => {
		element.innerText = "you clicked me"
	})
})