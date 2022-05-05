# market-data

## Description

Script to compute aggregate market data from raw trades

## Usage

Pipe data from a binary executable file into the script using a terminal window. When started, the first line of data must contain “BEGIN”, followed by lines representing trades formated as a JSON object, ending the data stream with the line “END”. Once all trades have been parsed, the script will send to stdout metrics for each market in JSON. One resulting object per market.

Trade input example: 
{"id":121509,"market":5773,"price":1.234,"volume":1234.56,"is_buy":true}

Metric output example: 
{"market":5775,"total_volume":1234567.89,"mean_price":23.33,"mean_volume":6144.299,"volume_weighted_average_price":5234.2,"percentage_buy":0.50}

## Tests

Linux/MacOS: chmod +x ./stdoutinator_arm64_darwin.bin > ./stdoutinator_arm64_darwin.bin | script.py
Windows: stdoutinator_amd64_windows.exe | script.py
