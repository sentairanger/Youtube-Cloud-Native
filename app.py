from flask import Flask, render_template, request
from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory(host='192.168.0.14')
led = LED(17, pin_factory=factory)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('led.html')

@app.route('/on')
def on():
    led.on()
    return render_template('led.html')

@app.route('/off')
def off():
    led.off()
    return render_template('led.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
