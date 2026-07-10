# IoT_SmartPlug_MSc_Project

- IoT Smart Plug Project to:
    
  1)  explore MQTT
  2)  read sensor data from an IoT device
  3)   end commands to the device
  4)   make graphs of the data gathered.
  5)   create a UX case study

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

- - - 

# UX Case Study - Voltrix

-  ### Overview
      **Voltrix** , an app idea as a first Introduction to UX Case Studies, was developed during an IoT Project in *Advanced Digital Design & Embedded Systems*.

    The primary purpose of this app is to allow its users advanced control of their devices connected to a SmartPlug, either through real-time monitoring and interaction, or through time-schedules.

-  ### Hypothesis

    The Modern lifestyle forces people *ab invito* out of their homes for the majority of the day. Being able to monitor, operate and automate your home appliances becomes more significant with each passing day.

   Specifically, some groups of people, such as parents, people with stress disorders, or tight time schedules, are going to notice an immediate impact on their way of life.  

  
-  ### Features:
    
    1) Easily add & name new devices through their QR code
    2) List of registered devices and their Connection Status
    3) Interactive list of connected devices(& groups) with ON/OFF slider and options
    4) Overview of all registered devices (& groups) Power Usage with Uptime 
    5) Extensive single device power usage analytics of last hour/day/week through Graphical Interface  
    6) Operation according to Time Schedule or Timer for specific device or group
    7) Option of handling devices through user specified tag

       -  
    8) Shortcut widget to turn ON or OFF a specific device
    9) Notification for STATUS change of Device through Time Schedule or Timer
  
-  ### StoryBoard
    The storyboard is for a hypothetical target user of the app - This demonstrates how an app such as Voltrix can make or break the day of a person that has a tight schedule and minimal time at his home in between his work and other activities.

   It highlights three of our key features which are:

   -  Remote ON/OFF switch for connected devices ( Turned Water Heater ON)
   -  Real time monitoring of a Device's Power usage through Hour/Day/Week Graph ( Monitoring if Washer/Dryer program finished - Power consumption dropped)
   -  Automation of device through Time Schedule (Washer/Dryer Example)
 
     
-  ### User Flow for Onboarding

    This User Flow demonstrates the on-boarding, configuration and use of a Smart Plug Device
   
    <img width="1079" height="898" alt="Voltrix User Flow SS" src="https://github.com/user-attachments/assets/0bc671b7-adb2-46c7-85b4-524ebcd804d7" />

    Made with [canva](https://www.canva.com)
-  ### Mind map

    This Mind Map showcases possible actions the users of Voltrix will be able to execute through the use of the App. 

    <img width="765" height="754" alt="Voltrix Mind Map" src="https://github.com/user-attachments/assets/718492ba-91fb-4ff8-b423-11cff49fd2ef" />

    Made with [canva](https://www.canva.com)
-  ### Wireframes
    <img width="1250" height="1507" alt="Voltrix_Wireframes" src="https://github.com/user-attachments/assets/44b9c017-50f9-46b6-92d4-6b0f8837a901" />

     Made with [Evolus-Pencil](https://github.com/OneToolsCollection/evolus-pencil)
-  ### Conclusion

  
-  ### Annotations

  
