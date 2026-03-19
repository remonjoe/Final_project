from flask import Flask, request, render_template, send_file
import os

app = Flask(__name__)

# Your 8 hardware products
products = [
    {"name": "Industrial Hammer", "image": "tool1.jpg"},
    {"name": "Power Drill", "image": "tool2.jpg"},
    {"name": "Wrench Set", "image": "tool3.jpg"},
    {"name": "Circular Saw", "image": "tool4.jpg"},
    {"name": "Heavy Duty Pliers", "image": "tool5.jpg"},
    {"name": "Leveler", "image": "tool6.jpg"},
    {"name": "Tape Measure", "image": "tool7.jpg"},
    {"name": "Screwdriver Kit", "image": "tool8.jpg"}
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

#@app.route('/display')
#def display_image():
#    filename = request.args.get('image')
#    
    # Base directory is /app/static/images
    # We join them without any validation
#    path = os.path.join("static/images", filename)
    
#    try:
        # This will follow the ../ all the way to the root
#        return send_file(path)
#    except Exception as e:
 #       return f"File not found at: {path}", 404

@app.route('/display')
def display_image():
    filename = request.args.get('image')
    
    # Path construction: static/images/../../../flag.txt
    # This resolves to /flag.txt on the Linux system
    path = os.path.join("static/images", filename)
    
    try:
        return send_file(path)
    except Exception as e:
        return f"File not found. Searched at: {path}", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
