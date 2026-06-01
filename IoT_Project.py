import sys,ssl,os
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from threading import Timer
from datetime import datetime

class IoTExample:
    def __init__(self):
        self._establish_mqtt_connection()

    def start(self):
        #Blocks program run so it doesnt finish in order to wait for messages
        self.client.loop_forever()
    
    def disconnected(self,argos= None):
        self.finishing = True
        # Method to disconnect from MQTT broker
        self.client.disconnect()
    
#You need to fill this in, here we will place the commands for connecting to the broker
    def _establish_mqtt_connection(self):
        print("I need to be completed")

# This is the callback that will be called after the connection is established
    def _on_connect(self, client, userdata, flags, rc):
        print("I need to be completed")

# This is the callback that will be called whenever a new message is received
    def _on_message(self, client, userdata, msg):
        print(msg.topic+' '+str(msg.payload))

# This is the callback that will be called whenever a new log event is created
    def _on_log(self, client, userdata, level, buf):
        print('log: ', buf)


    
    
try:
    iot_example = IoTExample()
    iot_example.start()
except KeyboardInterrupt:
    print("Interrupted")
    try:
        iot_example.disconnect()
        sys.exit(0)
    except SystemExit:
        os._exit(0)
 
"""
self.client = mqtt.Client(client_id=f"iotlesson{random.randint(0, 99999)}")

self.client.on_connect = self._on_connect
self.client.on_log = self._on_log
self.client.on_message = self._on_message:
self.client.tls_set_context(ssl.create_default_context())
self.client.username_pw_set('iotlesson', 'iotlesson123456!')
self.client.connect('kube.cs.uowm.gr', 8883)
#After we connect we subscribe to the topic we wanna see
client.subscribe('iotlesson_eventbus/grafeio113/out/#')

#Non-Blocking Method so program continues so that we can show graphics
# self.client.loop_start()
#Method to send msg to MQTT broker 1st param== topic , 2nd param == message content
self.client.publish('iotlesson_eventbus/grafeio113/in/ZWave_8_Metered_Wall_Plug_Switch_on_desk_Switch/command', 'ON')


# Graphics of measurements
def _prepare_graph_window(self):
    # Plot variables
    plt.rcParams['toolbar'] = 'None'
    self.ax = plt.subplot(111)
    self.dataX = []
    self.dataY = []
    self.first_ts = datetime.now()
    self.lineplot, = self.ax.plot(
        self.dataX, self.dataY, linestyle='­­', marker='o', color='b'
        )
    self.ax.figure.canvas.mpl_connect('close_event', self.disconnect)
    self.finishing = False
    self._my_timer()

def _refresh_plot(self):
    if len(self.dataX) > 0:
        self.ax.set_xlim(min(self.first_ts, min(self.dataX)),max(max(self.dataX), datetime.now()))
        self.ax.set_ylim(min(self.dataY) * 0.8, max(self.dataY) *1.2)
        self.ax.relim()
    else:
        self.ax.set_xlim(self.first_ts, datetime.now())
        self.ax.relim()
    plt.draw()

def _add_value_to_plot(self, value):
    self.dataX.append(datetime.now())
    self.dataY.append(value)
    self.lineplot.set_data(self.dataX, self.dataY)
    self._refresh_plot()

def _my_timer(self):
    self._refresh_plot()
    if not self.finishing:
        Timer(1.0, self._my_timer).start()

def _on_message(self, client, userdata, msg):
    if msg.topic == 'iotlesson_eventbus/grafeio113/out/ZWave_8_Metered_Wall_Plug_Switch_on_desk_Sensor_power/state':
        self._add_value_to_plot(float(msg.payload))
    print(msg.topic+' '+str(msg.payload))

def __init__(self):
    self.ax = None
    self._establish_mqtt_connection()
    self._prepare_graph_window()

defstart(self):
    if self.ax:
        self.client.loop_start()
        plt.show()
    else:
        self.client.loop_forever()

# Remote Control of Device
def _button_on_clicked(self, event):
    self.client.publish('iotlesson_eventbus/grafeio113/in/ZWave_8_Metered_Wall_Plug_Switch_on_desk_Switch/command'
    , 'ON')

def _button_off_clicked(self, event):
    self.client.publish('iotlesson_eventbus/grafeio113/in/ZWave_8_Metered_Wall_Plug_Switch_on_desk_Switch/command'
    , 'OFF')

axcut = plt.axes([0.0, 0.0, 0.1, 0.06])
self.bcut = Button(axcut, 'ON')
axcut2 = plt.axes([0.1, 0.0, 0.1, 0.06])
self.bcut2 = Button(axcut2, 'OFF')
self.state_field = plt.text(1.5, 0.3, 'STATE: ­')
self.bcut.on_clicked(self._button_on_clicked)
self.bcut2.on_clicked(self._button_off_clicked)
"""