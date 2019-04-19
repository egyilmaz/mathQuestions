function EvalAndSubmit(qid){
    var ans = document.getElementById("hidden_answer_"+qid)
    if (ans.style.display === "none") {
        ans.style.display = "block";
    } else {
        ans.style.display = "none";
    }
}
