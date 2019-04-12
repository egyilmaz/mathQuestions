function EvalAndSubmit(qid, answer, meta){
    var input = document.getElementById("user_input").value;
    var out = answer +"<br>"+ meta+"<br>";
    document.getElementById("check_result_"+qid).innerHTML = out
}
