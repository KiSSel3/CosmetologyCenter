function checkAge(event) {
    const birthdate = prompt("Please enter your birthdate in YYYY-MM-DD format:");

    if (birthdate) {
        const inputDate = new Date(birthdate);
        const today = new Date(); // Get the current date
        const ageDate = new Date(today - inputDate);
        // 1970 is subtracted to calculate the number of years since the Unix epoch (January 1, 1970) to the user's birth year
        const years = Math.abs(ageDate.getUTCFullYear() - 1970);
        const dayOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

        if (years >= 18) {
            alert(`You are ${years} years old. The day of the week of your birthdate is ${dayOfWeek[inputDate.getDay()]}`);
            document.getElementById('content').style.display = 'block';
            return true; // Allow the link to be followed
        } else {
            alert('You must be at least 18 years old to access this page. Parental permission is required.');
            return false; // Prevent the link from being followed
        }
    } else {
        return false; // Prevent the link from being followed if birthdate is not entered
    }
}