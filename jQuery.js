jQuery(document).ready(function() {
    jQuery('.tabs .tab-links a').on('click', function(e)  {
        var currentAttrValue = jQuery(this).attr('href');
 
        // Show/Hide Tabs
        jQuery('.tabs ' + currentAttrValue).show().siblings().hide();
 
        // Change/remove current tab to active
        jQuery(this).parent('li').addClass('active').siblings().removeClass('active');
 
        e.preventDefault();
    });
	jQuery(".Fibonacci").click(function() {
		var places = parseInt(prompt("How many numbers of the Fibonacci Sequence do you want to go to?"));
		var number = 1;
		var numberOld = 0;
		var numberAdd = 0;
		var numbersToPrint = [];
		while (places!==0) {
    		numberAdd = numberOld;
    		numberOld = number;
 		   	number += numberAdd;
 		   	places -= 1;
    		numbersToPrint.push(number);
		};
		document.getElementById("FibonacciOutput").innerHTML = numbersToPrint;
	});
	jQuery(".Collatz").click(function() {
		var steps = 0;
		var numbersToPrint = [];
		var number = parseInt(prompt("Please choose a number. Make sure it is whole and positive."));
		if (number%1 !== 0) {
			console.log("That choice isn't valid. Hit Run and try again, this time making sure it is actually a number.");  
		}
		else if (number< 1) {
			console.log("That choice isn't valid. Hit Run and try again, this time making sure it is whole and positive.");
		}
		else {
			while (number!==1) {
				if (number%2===0) {
					var number = number/2;
					steps += 1;
					numbersToPrint.push(number);
				 }
				else {
					number *= 3;
					number += 1;
					steps += 1;
					numbersToPrint.push(number);
				 }
			}
		document.getElementById("CollatzOutput").innerHTML = (numbersToPrint);
		document.getElementById("CollatzOutput2").innerHTML = ("Congratulations! You're done! It took " + steps + " steps.");
     }
	});
	jQuery(".Weekday").click(function() {
		var year = parseInt(prompt("Please enter a historical year."), 10);
		var month = prompt("Please enter a historical month. Use 1-12 or the month names.").toLowerCase();
		switch (true){
			case (month=="january"||month=="jan"):
				month = 1;
				break;
			case (month=="february"||month=="feb"):
				month = 2;
				break;
			case (month=="march"||month=="mar"):
				month = 3;
				break;
			case (month=="april"||month=="apr"):
				month = 4;
				break;
			case (month=="may"):
				month = 5;
				break;
			case (month=="june"):
				month = 6;
				break;
			case (month=="july"):
				month = 7;
				break;
			case (month=="august"||month=="aug"):
				month = 8;
				break;
			case (month=="september"||month=="sept"):
				month = 9;
				break;
			case (month=="october"||month=="oct"):
				month = 10;
				break;
			case (month=="november"||month=="nov"):
				month = 11;
				break;
			case (month=="december"||month=="dec"):
				month = 12;
				break;
			default:
				month = parseInt(month, 10);
		}
		var day = parseInt(prompt("Please enter a historical day."), 10);
		var today = new Date();
		var dayToday = today.getDate();
		var monthToday = today.getMonth()+1;
		var yearToday = today.getFullYear();
		var weekdayToday = today.getDay() + 1;
		console.log (""+ weekdayToday + ", " + monthToday + " " + dayToday +", " + yearToday);
		var daysBetween = 0;
		while (year !== yearToday) {
			if (yearToday > year){
				if (monthToday >= 3) {
					if ((yearToday%4===0 && yearToday%100!==0)||(yearToday%400===0)) {
					daysBetween += 366;
					yearToday -= 1;
					}
					else {
					daysBetween += 365;
					yearToday -= 1;
				   }
				}
			else {
				if (((yearToday-1)%4===0 && (yearToday-1)%100!==0)||((yearToday-1)%400===0)) {
				daysBetween += 366;
				yearToday -= 1;
				}
				else {
				daysBetween += 365;
				yearToday -= 1;
			   }
			}
		}
		else {
			yearToday += 1;
				if (monthToday >= 3) {
					if ((yearToday%4===0 && yearToday%100!==0)||(yearToday%400===0)) {
					daysBetween += 366;
					}
					else {
					daysBetween += 365;
				   }
				}
				else {
					if (((yearToday-1)%4===0 && (yearToday-1)%100!==0)||((yearToday-1)%400===0)) {
					daysBetween += 366;
					}
					else {
					daysBetween += 365;
				   }
				}
			}
		}
		while (month !== monthToday) {
			if (monthToday>month) {
				monthToday -= 1;
				if ((monthToday === 2)&&(yearToday%4===0 && yearToday%100!==0)||(yearToday%400===0)) {
					daysBetween += 29;
				}
				else if (monthToday===2) {
					daysBetween += 28;
				}
				else if ((monthToday===9)||(monthToday===4)||(monthToday===6)||(monthToday===11)) {
					daysBetween += 30;
				}
				else {
					daysBetween += 31;
				}
			}
			else {
				if ((monthToday === 2)&&(yearToday%4===0 && yearToday%100!==0)||(yearToday%400===0)) {
					daysBetween -= 29;
				}
				else if (monthToday===2) {
					daysBetween -= 28;
				}
				else if ((monthToday===9)||(monthToday===4)||(monthToday===6)||(monthToday===11)) {
					daysBetween -= 30;
				}
				else {
					daysBetween -= 31;
				}
				monthToday += 1;
			}
		}
		if (dayToday === day) {
			daysBetween += 0;
		}
		else if (dayToday > day) {
			daysBetween += (dayToday - day);
		}
		else {
			daysBetween -= (day - dayToday);
		}
		switch ((((weekdayToday-1)-(daysBetween%7)+7)%7)){
			case 0:
				weekDay = ("Sunday.");
				break;
			case 1:
				weekDay = ("Monday.");
				break;
			case 2:
				weekDay = ("Tuesday.");
				break;
			case 3:
				weekDay = ("Wednesday.");
				break;
			case 4:
				weekDay = ("Thursday.");
				break;
			case 5:
				weekDay = ("Friday.");
				break;
			case 6:
				weekDay = ("Saturday.");
				break;
			default:
				console.log ("Error. Please try again, or contact Preston with some whining.");
		}
		document.getElementById("WeekdayOutput").innerHTML = ("Your day fell on " + weekDay);
	});
});// JavaScript Document