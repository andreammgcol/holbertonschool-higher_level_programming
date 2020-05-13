#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const tasks = JSON.parse(body);
    const result = {};
    const report = [];

    for (const task of tasks) {
      if (task.completed) {
        const userFound = report.find(element => element.id === task.userId);
        if (!userFound) {
          report.push({ id: task.userId, count: 1 });
        } else {
          userFound.count += 1;
        }
      }
    }

    for (const item of report) {
      result[item.id] = item.count;
    }

    console.log(result);
  }
});
