#!/usr/bin/node
// Script that updates the text of the header element to New Header!!!
// when the user clicks on the element with id update_header

const header = document.querySelector('header');
const updateHeader = document.querySelector('#update_header');

updateHeader.addEventListener('click', () => {
  header.innerHTML = 'New Header!!!';
});
