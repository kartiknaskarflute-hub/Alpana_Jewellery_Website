ALPANA JEWELLERY WEBSITE — WINDOWS SETUP

1. Extract this ZIP file.
2. Open the extracted Alpana_Jewellery_Website folder.
3. Click the address bar in File Explorer, type cmd, and press Enter.
4. Run these commands one at a time:

python -m pip install -r requirements.txt
python app.py

5. Open this address in your browser:
http://127.0.0.1:5000

To stop the website, return to CMD and press Ctrl+C.

The supplied logo is copied as-is to static/alpana-logo.png.
The address, phone number, collection text and social links are demo placeholders.

Responsive support: the site includes a viewport setting and CSS breakpoints for desktop, tablet and mobile. Run locally at http://127.0.0.1:5000; to open it on another device, both devices must be on the same Wi-Fi and the Flask app must bind to 0.0.0.0, with firewall/network access configured.
