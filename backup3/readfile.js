const fs = require("fs");
var number = 1;
fs.readFile(`out${number}.txt`, "utf-8", (err, data) => {
    if (err) {
        throw err;
    }

    var lines = data.trim().split("\n");
    var numberQuestion = lines.length / 8;
    console.log(lines.length);
    console.log(numberQuestion);
    var questions = [];
    for (var i = 0; i < lines.length; i += 8) {
        var tmpObject = {
            question: lines[i + 0],
            a: lines[i + 1],
            b: lines[i + 2],
            c: lines[i + 3],
            d: lines[i + 4],
            correctAnswer: lines[i + 5],
            numebrRight: lines[i + 6],
            numberWrong: lines[i + 7],
            key: function () {
                if (this.correctAnswer === "1") {
                    return this.a;
                }
                if (this.correctAnswer === "2") {
                    return this.b;
                }
                if (this.correctAnswer === "3") {
                    return this.c;
                }
                if (this.correctAnswer === "4") {
                    return this.d;
                }
            },
        };
        questions.push(tmpObject);
    }

    var totalQuestionAnswered = 0;

    fs.writeFile(`qp${number}.json`, JSON.stringify(questions), (err) => {
        if (err) {
            throw err;
        }
        console.log("JSON data is saved.");
    });
});
