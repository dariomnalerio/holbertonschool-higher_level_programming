#!/usr/bin/node
// Script that toggles the class of the header element
// when the user clicks on the tag id toggle_header

const toggleHeader = document.querySelector("#toggle_header");
const header = document.querySelector("header");

toggleHeader.addEventListener("click", () => {
  header.classList.toggle("red");
  header.classList.toggle("green"); // Toggles between red and green
});
