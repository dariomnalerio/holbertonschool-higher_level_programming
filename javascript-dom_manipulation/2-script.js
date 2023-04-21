#!/usr/bin/node
// Script that adds the class red to the header element
// when the user clicks on the tag with id red_header

const header = document.querySelector("header");
const toggleHeader = document.querySelector("#red_header");

toggleHeader.addEventListener("click", () => {
  header.style.color = "#FF0000";
});
