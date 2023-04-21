#!/usr/bin/node
// Prints the number of completed tasks by user id

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(body);
    const completedTasks = {};
    for (const task of tasks) { // for each task
      if (task.completed) { // if the task is completed
        if (completedTasks[task.userId]) { // if the user has completed tasks
          completedTasks[task.userId]++;
        } else {
          completedTasks[task.userId] = 1; // if it's the first completed task for the user
        }
      }
    }
    console.log(completedTasks);
  }
});
