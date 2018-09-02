// Modifications in index.html:
// Line 7: the link to jquery library
// Line 423: added the script tag pointing to problem3.js

// Task 1
toRed = $($('ul li')[0]) // see comment under task 3
toRed.css('background-color', 'red')

// Task 2
toBlue = toRed.find('li')
toBlue.css('color', 'blue')

// Task 3
$('ol:first li').append(' in the list!')
// contrast this with 'Task 1': that required casting the resulting
// object to a Jquery object; this does not require the casting

// Task 4
$('body').css('background-color', '#eee')

// Task 5
$('a').click(function(){alert('You have clicked on a link! You will now be redirected...')})
