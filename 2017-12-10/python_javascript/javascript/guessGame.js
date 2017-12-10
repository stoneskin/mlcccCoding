var randomNumber = Math.floor(Math.random() * 6 ) + 1;

var guess = prompt('I am thinking of a random number between 1 and 6. What is it?');

while(true){

	if (parseInt(guess) === randomNumber ) {

	  document.write('<p>You guessed the number!</p>');
	  document.write(guess);
	  break;
	}  else {
	 
	guess = prompt('Sorry, you are wrong, please guess again:');

	}
}