#!/usr/bin/node
// Script that adds a li element to a list
// when the user clicks on the element with id add_item

const addElement = document.querySelector('#add_item');
const list = document.querySelector('.my_list');

addElement.addEventListener('click', () => {
  const li = document.createElement('li'); // Creates a new li element
  li.innerHTML = 'Item'; // Adds text to the li element
  list.appendChild(li); // Adds the li element to the list
});
