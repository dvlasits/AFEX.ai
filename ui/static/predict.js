$(document).ready(function () {
    console.log("ready!");
});

function predict() {
    console.log("predict!");

    let chars = "ASDFGHMFAJDSASDFGHMFAJDSASDFGHMFAJDSASDFGHMFAJDSASDFGHMFAJDSASDFGHMFAJDS";
    let group = "000111000000000111111100002222222000111110000220000000000000000000000000";
    let output = $("#result");
    for (var i = 0; i < chars.length; i++) {
        let ch = chars.charAt(i);
        let cl = group.charAt(i);
        if (cl == '1'){
            output.append("<span class='green'>" + ch + "</span>");
        }
        else if (cl == '2'){
            output.append("<span class='red'>" + ch + "</span>");
        }
        else {
            output.append("<span>" + ch + "</span>");
        }
        
    }
}