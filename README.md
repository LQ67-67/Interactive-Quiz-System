# Interactive-Quiz-System
Raspberry Pi Projects with Explorer HAT Pro

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
