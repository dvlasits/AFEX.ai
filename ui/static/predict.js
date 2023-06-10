$(document).ready(function () {
    console.log("ready!");
});

function predict() {
    let sendData = { 'input': $("#seq-input").val() };

    $.ajax({
        url: '/predict-api',
        type: "POST",
        data: JSON.stringify(sendData),
        contentType: "application/json; charset=utf-8",
        success: function (recData) {
            let chars = recData.seq;
            let group = recData.labels;
            let output = $("#result");
            output.empty();
            for (var i = 0; i < chars.length; i++) {
                let ch = chars.charAt(i);
                let cl = group.charAt(i);
                if (cl == '1') {
                    output.append("<span class='green'>" + ch + "</span>");
                }
                else if (cl == '2') {
                    output.append("<span class='red'>" + ch + "</span>");
                }
                else {
                    output.append("<span>" + ch + "</span>");
                }

            }

            let probs_out = $("#pred-func-output");
            probs_out.empty();
            let probs = recData.probs;
            for (var i = 0; i < probs.length; i++) {
                probs_out.append("<span>" + probs[i][0] +"</span>");
                probs_out.append("<span>" + probs[i][1] +"</span>");
            }

            let explanation_out = $("#pred-explanation");
            explanation_out.empty();
            let expl = recData.explanation;
            for (var i = 0; i < expl.length; i++) {
                if (expl[i][1] == "1") {
                    explanation_out.append("<span class='green'>" + expl[i][0] +"</span>");
                }
                else if (expl[i][1] == "2") {
                    explanation_out.append("<span class='red'>" + expl[i][0] +"</span>");
                }
                else {
                    explanation_out.append("<span>" + expl[i][0] +"</span>");
                }
                
                explanation_out.append("<span>" + expl[i][2] +"</span>");
            }
        }
    });
}