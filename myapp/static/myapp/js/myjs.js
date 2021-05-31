
// const eventBox = document.getElementById('event-box')
// const countdownBox = document.getElementById('countdown-box')

// console.log(eventBox.textContent)
// const eventDate = Date.parse(eventBox.textContent)
// console.log(eventDate)


// setInterval(()=>{
// 	const now = new Date().getTime()
// 	console.log(now)

// 	const diff = eventDate - now
// 	console.log(diff)
	
// 	const d = Math.floor(eventDate / (1000 *60 *60 *24) - (now /(1000 *60 *60 *24)))
// 	const h = Math.floor(eventDate / (1000 *60 *60 ) - (now /(1000 *60 *60 ) %24))
// 	const h = Math.floor(eventDate / (1000 *60  ) - (now /(1000 *60  ) %60))
// 	const s = Math.floor(eventDate / (1000  ) - (now /(1000  ) %60))
// 	console.log(d)


// 	if (diff>0) {
// 	countdownBox.innerHTML = d + " days" +h+ "hours" + m+ " minunt"
// 	} else{
// 		countdownBox.innerHTML =" countDown completed"
// 	}
// },1000)

