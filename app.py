from flask import Flask, render_template
import subprocess
import os
import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get the username
    username = os.getenv('USER', subprocess.getoutput('whoami'))
    
    # Get the full name (you should replace this with your actual name)
    name = "Vaibhav Kumar"  # Replace with your actual name
    
    # Get current time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    
    # Get top output
    top_output = subprocess.getoutput('top -b -n 1')
    
    return render_template('htop.html', 
                          name=name, 
                          username=username, 
                          server_time=server_time, 
                          top_output=top_output)

if __name__ == '__main__':
    # Run the app on 0.0.0.0 to make it accessible from outside the container
    app.run(host='0.0.0.0', port=5000, debug=True)

