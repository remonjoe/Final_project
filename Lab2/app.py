from flask import Flask, request, send_file, render_template
import os
import urllib.parse

# ✅ Step 1: Create app FIRST
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/display')
def display_image():
    # 🔥 Get raw query string
    raw_query = request.query_string.decode('utf-8')

    # 🔥 Extract file manually
    filename = ''
    if 'file=' in raw_query:
        filename = raw_query.split('file=')[1]
        if '&' in filename:
            filename = filename.split('&')[0]

    # 🔒 Block direct traversal
    if "../" in filename or "..\\" in filename or filename.startswith("/"):
        return "Blocked: Direct path traversal not allowed", 403

    # ✅ Decode AFTER filtering
    decoded_path = urllib.parse.unquote(filename)

    # 🐞 Debug prints (will show in terminal)
    print("RAW:", filename)
    print("DECODED:", decoded_path)

    # ⚠️ Vulnerable join (for lab)
    file_path = os.path.join("static", decoded_path)

    try:
        return send_file(file_path)
    except Exception as e:
        return f"Error: {str(e)}", 404

# ✅ Step 2: Run app LAST
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)