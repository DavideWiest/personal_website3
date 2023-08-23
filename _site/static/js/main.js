function timeDifference(date) {
    let now = new Date();
    let givenDate = new Date(date);
    let difference = now - givenDate;
    let seconds = Math.floor(difference / 1000);
    let minutes = Math.floor(seconds / 60);
    let hours = Math.floor(minutes / 60);
    let days = Math.floor(hours / 24);
    let months = Math.floor(days / 30.44);
    let years = Math.floor(months / 12);

    return {
        years: Math.round(years),
        months: Math.round(months % 12),
        days: Math.round(days % 30.44),
        hours: Math.round(hours % 24),
        minutes: Math.round(minutes % 60),
        seconds: Math.round(seconds % 60)
    };
}

var dt = new Date("2006-10-02T02:41:39+01:00");


function updateAge() {
    let result = timeDifference(dt);
    let ageElement = document.getElementById('age');
    ageElement.textContent = ageElement.textContent.split(":")[0] + ": " + `${result.years} years, ${result.months} months, ${result.days} days, ${result.hours} hours, ${result.minutes} minutes, ${result.seconds} seconds`;
}

setInterval(updateAge, 1000);

