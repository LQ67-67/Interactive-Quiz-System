# Interactive-Quiz-System
Raspberry Pi Projects with Explorer HAT Pro

## 🛠️ The Gear

Both projects utilize the **Explorer HAT Pro**, which mounts directly onto the Raspberry Pi's GPIO header111. This HAT provides a safe and easy way to connect sensors and LEDs using a mini-breadboard.

**Required Components:**

- Raspberry Pi 4 (or 3B+) with power supply2.
- Explorer HAT Pro3.
- 
    
    **Project 1:** TMP36 Analog Temperature Sensor4.
    
- 
    
    **Project 2:** 1x Blue LED, 1x Red LED, 2x 470Ω Resistors5555.
    
- 
    
    **Both:** 1x Buzzer and Jumper wires6.
    

If your Explorer HAT Pro isn't set up yet, you'll need to do the following:

```bash
curl https://get.pimoroni.com/i2c | bash
sudo apt-get install python-smbus
sudo apt-get install python-pip
sudo pip install explorerhat

```

Those commands will install set up I2C and install the Explorer HAT Python library.

Next, you'll want to plug your Explorer HAT Pro into the 40 pin GPIO connector on your Raspberry Pi. You can check it's working by typing the following straight in the terminal:

```bash
python -c 'import time, explorerhat; explorerhat.light.on(); time.sleep(1); explorerhat.light.off()'

```

That should light up all four of the LEDs on the Explorer HAT Pro board for a second and then switch them all off again. If that works, then your Explorer HAT Pro is good to go!

---
### 🏆 The Interactive Quiz System

Now we switch roles. Instead of reading data, we will use a web page to control the physical world. We will build a quiz where a correct answer lights a Blue LED, and a wrong answer lights a Red LED and buzzes14.

### Hardware Setup

We will use the **Output** pins (OUT) on the Explorer HAT Pro.

- **Blue LED (Correct):** Connect Anode (+) to **OUT2** via a 470Ω resistor. Connect Cathode (-) to GND15151515.
- **Red LED (Incorrect):** Connect Anode (+) to **OUT3** via a 470Ω resistor. Connect Cathode (-) to GND16161616.
- 
    
    **Buzzer:** Keep connected to **OUT1**17.
    

> 
> 
> 
> **⚠️ Safety Tip:** Ensure you use separate resistors for each LED to prevent burning them out18.
> 

**Visual Reference:**

https://cdn.learn.pimoroni.com/article/explorer-hat-pro-pin-entry-system/assets/explorer_pin_entry.png?width=1024

### The Code (Python + Flask)

This app uses a POST request to check the user's answer. Based on the result, it triggers the specific hardware pins.
