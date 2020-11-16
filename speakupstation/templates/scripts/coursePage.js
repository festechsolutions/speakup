
function checkOut(e) {
    console.log(e);
    console.log(e.target.id);
    if (e.target.id == "discription") {
        document.getElementById("discription").style.display = "none";
    }
}
// tracker
function showTracker() {
    document.getElementById("MainChildDad").style.display = "flex";
    document.getElementById("mainConts").style.opacity = "0.5";
    setTimeout(() => {
        document.getElementById("childb3Dad").style.height = "200px";
    }, 150);
}
document.getElementById("MainChildDad").onclick = function (e) {
    console.log(e);
    if (e.target.id == "MainChildDad") {
        document.getElementById("childb3Dad").style.height = "0px";
        setTimeout(() => {
            document.getElementById("MainChildDad").style.display = "none";
            document.getElementById("mainConts").style.opacity = "1";
        }, 150);
    }
}
// description
function showDiscription() {
    document.getElementById("MainChildDad1").style.display = "flex";
    document.getElementById("mainConts").style.opacity = "0.5";
    setTimeout(() => {
        document.getElementById("childb3Dad1").style.height = "150px";
    }, 150);
}
document.getElementById("MainChildDad1").onclick = function (e) {
    console.log(e);
    if (e.target.id == "MainChildDad1") {
        document.getElementById("childb3Dad1").style.height = "0px";
        setTimeout(() => {
            document.getElementById("MainChildDad1").style.display = "none";
            document.getElementById("mainConts").style.opacity = "1";
        }, 150);
    }
}
