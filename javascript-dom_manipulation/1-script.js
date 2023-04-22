#!/usr/bin/node
// Script that updates the text color of the header element to red
// when the user clicks on the tag DIV#red_header

const element = document.querySelector('header');

element.addEventListener('click', () => {
  element.style.color = '#FF0000';
});
