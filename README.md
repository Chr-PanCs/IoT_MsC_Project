# IoT_MQTT_MSc_Project
IoT Project to explore MQTT, read sensor data from an IoT device, send commands to the device and make graphs of the data gathered.
- - -

**MQTT** (Message Queuing Telemetry Transport) is a lightweight messaging protocol designed for IoT (Internet of Things) applications using a publish/subscribe model. It ensures reliable, real-time communication with minimal code and bandwidth, making it ideal for resource-constrained devices and low-bandwidth networks. Industries like IoT, mobile internet, Internet of Vehicles (IoV), and power systems widely adopt MQTT for its efficiency.

Benefits of MQTT for Python users:

- Open-source and backed by a strong community.
- Simple API for connecting, publishing, and subscribing to MQTT messages.
- Supports multiple security options.
- Regularly updated to keep pace with IoT advancements.

- - - 


### Connecting with the MQTT Broker

We connect with the MQTT Broker and we subscribe to the topics we want to get updates on.

https://github.com/Chr-PanCs/IoT_MsC_Project/blob/7d0200622931ffaa62f3f4341c79032b73f4ec25/IoT_Project.py#L33

- - - 
### Interactive Graphics Interface 

We create an Interactive Graphics Interface with the Power Draw data we got from the MQTT broker with interactive controls to turn the outlet ON or OFF 

- *Graph*
https://github.com/Chr-PanCs/IoT_MsC_Project/blob/7d0200622931ffaa62f3f4341c79032b73f4ec25/IoT_Project.py#L75

- *Remote Control of IoT Device*
https://github.com/Chr-PanCs/IoT_MsC_Project/blob/7d0200622931ffaa62f3f4341c79032b73f4ec25/IoT_Project.py#L123


- *Full Interactive Interface* with real-time updates

    - Picture & GIF

<img width="642" height="503" alt="GUI example" src="https://github.com/user-attachments/assets/46b0fccf-2afc-43b4-bc90-a860ece9a3d5" />
  
<img width="642" height="503" alt="GUI example" src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWRpcnpxMW1pZW1zbjg4aXUwbmd4cWZrZTVsd2F6NXIxbGQ5N3BpNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Ohc1YwM4xKo2asuuWT/giphy.gif" />
