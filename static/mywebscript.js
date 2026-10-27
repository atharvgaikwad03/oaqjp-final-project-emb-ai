let RunSentimentAnalysis = () => {
    let textToAnalyse = document.getElementById("textToAnalyse").value;
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("output").innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyse=" + encodeURIComponent(textToAnalyse), true);
    xhttp.send();
}
