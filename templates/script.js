function generateQRCode() {
    var inputWord = document.getElementById("input_word").value;

    // Make an AJAX request to the Python script
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/generate_qr", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var qrImage = document.getElementById("qr_code");
            qrImage.src = xhr.responseText;
        }
    };

    xhr.send(JSON.stringify({ inputWord: inputWord }));
}
