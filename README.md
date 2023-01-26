# HueSPIKE
Control a Hue lightbulb with the SPIKE Prime (and Anton's LMS-ESP32 board)

# Anton's MINDSTORMS Hacks

See: https://antonsmindstorms.com/

LMS-ESP32 board: https://antonsmindstorms.com/product/wifi-python-esp32-board-for-mindstorms/

Setting up hardware: https://antonsmindstorms.com/2022/11/18/lms-esp32-tutorials-part-0-how-to-get-started/

Tutorial on communication: https://antonsmindstorms.com/2022/11/15/lms-esp32-tutorial-part-1-uartremote/

# Code

`spike.py` is installed on the LEGO Education SPIKE Prime Hub (running SPIKE 2 firmware)

`boot.py` is installed on the LMS-ESP32 board so that it automatically runs on powerup

# Effect

When you push SPIKE Prime Force Sensor in Port B: the Hue light turns on.

When you push SPIKE Prime Force Sensor in Port D: the Hue light turns off.

If the light is on and you spin the SPIKE Prime Motor in Port F: the Hue light changes to a random color.

# Description/Demo Video

[![Hue Control](https://img.youtube.com/vi/GrWgpg3aBRw/0.jpg)](https://youtu.be/GrWgpg3aBRw)
