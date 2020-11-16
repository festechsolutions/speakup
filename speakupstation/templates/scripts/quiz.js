var correctAns = "Two";

function myFunc(e) {
    // console.log(e);
    var fetchedValue = document.getElementById(e).innerHTML;
    console.log(fetchedValue);
    if (fetchedValue == correctAns){
        document.getElementById("myModal1").style.display = "block";
    }else{
        document.getElementById("myModal2").style.display = "block";
    }
}