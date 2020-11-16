function checkit() { // Side bar
    console.log("sikofdjlo");
    if (document.getElementById("sideBar").style.display != "flex") {
        document.getElementById("reqSideBar").style.width = "80%";
        setTimeout(() => {
            document.getElementById("sideBar").style.display = "flex";
        }, 150);
    } else {
        document.getElementById("sideBar").style.display = "none"
        document.getElementById("reqSideBar").style = "0%";
    }

}
function searchOrClear() {
    console.log(document.getElementById("twoDiffIcons"));
    if (document.getElementById("twoDiffIcons").src.includes("/Images/cross.png")) {
        document.getElementById("searchText").value = "";
        chngImg()
    }
}
function chngImg() {
    // console.log(document.getElementById(e.id).value);
    if (document.getElementById("searchText").value.length > 0) {
        document.getElementById("twoDiffIcons").src = "/Images/cross.png"
    } else {
        document.getElementById("twoDiffIcons").src = "/Images/b.png"
    }
}
