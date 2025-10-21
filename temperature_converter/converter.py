import webbrowser
import tempfile

# Create HTML content for temperature converter
html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Temperature Converter</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #1e1e2f, #2e2e4f);
            color: white;
            text-align: center;
            padding-top: 100px;
        }
        h1 {
            color: #00bcd4;
        }
        .container {
            background: #2c2c3c;
            width: 350px;
            margin: auto;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 0px 15px rgba(0,0,0,0.5);
        }
        input, select, button {
            margin: 10px;
            padding: 8px;
            border-radius: 8px;
            border: none;
            font-size: 16px;
        }
        button {
            background-color: #00bcd4;
            color: white;
            cursor: pointer;
        }
        button:hover {
            background-color: #0197a7;
        }
        p {
            font-size: 18px;
            color: #f4f4f4;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌡 Temperature Converter</h1>
        <p>Convert between Celsius, Fahrenheit, and Kelvin</p>
        <input type="number" id="tempInput" placeholder="Enter temperature">
        <select id="fromScale">
            <option value="C">Celsius</option>
            <option value="F">Fahrenheit</option>
            <option value="K">Kelvin</option>
        </select>
        <select id="toScale">
            <option value="C">Celsius</option>
            <option value="F">Fahrenheit</option>
            <option value="K">Kelvin</option>
        </select>
        <br>
        <button onclick="convertTemp()">Convert</button>
        <p id="result"></p>
    </div>

    <script>
        function convertTemp() {
            let temp = parseFloat(document.getElementById("tempInput").value);
            let from = document.getElementById("fromScale").value;
            let to = document.getElementById("toScale").value;
            let result = 0;

            if (isNaN(temp)) {
                document.getElementById("result").innerHTML = "Please enter a valid number!";
                return;
            }

            if (from === to) {
                result = temp;
            } else if (from === "C" && to === "F") {
                result = (temp * 9/5) + 32;
            } else if (from === "C" && to === "K") {
                result = temp + 273.15;
            } else if (from === "F" && to === "C") {
                result = (temp - 32) * 5/9;
            } else if (from === "F" && to === "K") {
                result = (temp - 32) * 5/9 + 273.15;
            } else if (from === "K" && to === "C") {
                result = temp - 273.15;
            } else if (from === "K" && to === "F") {
                result = (temp - 273.15) * 9/5 + 32;
            }

            document.getElementById("result").innerHTML =
                temp + " " + from + " = " + result.toFixed(2) + " " + to;
        }
    </script>
</body>
</html>
"""

# Create a temporary HTML file and open it in browser
with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html') as f:
    f.write(html_content)
    webbrowser.open('file://' + f.name)
