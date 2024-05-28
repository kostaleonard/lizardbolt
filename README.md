# LizardBolt

![logo](media/logo_256_256_with_name.jpg)

The LizardBolt is a cell phone made from a Raspberry Pi.

I have organized this repository as a minimal guide for reproducing the work.

## Parts

* [Raspberry Pi 4B](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)
* [Elecrow 5 inch Raspberry Pi touch display](https://www.elecrow.com/hdmi-5-inch-800x480-tft-display-for-raspberry-pi-b-p-1384.html)
* [Rii Mini Bluetooth Keyboard](http://www.riitek.com/product/259.html)
* [SIM800C USB to GSM Module](https://a.co/d/1KzBXUG)
* A pair of headphones that use a 3.5mm jack
* [USB 2.0 mini microphone](https://a.co/d/guWN2m7)

## Assembly

### OS image

1. Use the [Raspberry Pi Imager](https://www.raspberrypi.com/software/) to install a clean OS image on your SD card. I used 64 bit Raspbian.
2. Attach an HDMI monitor (not the 5 inch display since that will take some configuration), mouse, and keyboard to the Pi, turn it on, and follow the initial setup instructions.
3. Pair the Bluetooth keyboard with the Pi. You can do this step at any time, whenever you're ready to stop using your USB keyboard.

### Display

You can perform these steps with the HDMI monitor still connected, or via SSH.

1. On the Pi, open a terminal and navigate to your home directory.
2. Run the following. You can look on the GitHub page to see what the script does. Basically it just adds configuration for the screen size and other details in `/boot/firmware/config.txt`. It also installs software that allows the touchscreen to work. The `LCD5-show` script is for the 5 inch screens, so if you bought a different size screen from the same manufacturer, you can run one of the other scripts.
```shell
git clone https://github.com/goodtft/LCD-show.git
chmod -R 755 LCD-show
cd LCD-show/
sudo ./LCD5-show
```
3. Attach the display to the Pi by plugging in the GPIO pins and the HDMI connector that comes with the display. There is only one way to plug in the display so that the HDMI connector lines up correctly, so this step should hopefully be intuitive.
4. Restart the Pi. The display should turn on and show the desktop screen. The touchscreen should work.

![](media/pi_display_plugin.jpeg)
![](media/pi_display_on_1.jpeg)
![](media/pi_display_on_2.jpeg)

### Battery

TODO

### Fan

TODO do we need a fan?

### Audio (output)

Plug in any pair of headphones into your Pi's 3.5mm jack.

### Microphone (input)

Plug in the USB 2.0 mini microphone.
Your device should recognize it as a microphone immediately and display a microphone icon in the top right.

You can test your microphone using the `arecord` and `aplay` commands.

1. Run `arecord -l`. You should see your device as an input option. Probably it will be the only option.
2. Run `arecord hello.wav`. The microphone will now start recording. Say some words into the microphone and press `CTRL-C` when you're done.
3. Run `aplay hello.wav`. It will play back your recording in your headphones.

### Cellular

Reference the following design document throughout this process: [SIM800C_Hardware_Design_V1.02](https://www.elecrow.com/download/SIM800C_Hardware_Design_V1.02.pdf).
I am a software engineer, not an electrical engineer, so I can only make a guess at some of the meaning.
Still, I found it informative.

You can also check out the [SIM800C Series AT Command Manual V1.01](https://www.digikey.jp/htmldatasheets/production/1833952/0/0/1/sim800-series-at-command-manual.html) for more information on available AT commands.

1. Plug the SIM800C USB to GSM Module into one of the USB ports. I plugged into the bottom center port. You should see a new entry in `/dev/`. Mine was `/dev/ttyUSB0`. You should also see a flashing LED on the board. For me, the LED appeared to be flashing at 64ms on, 800ms off, which appears to correspond with the "Not registered the network" state in Table 21. Intuitively this makes sense to me since I haven't yet put in the SIM card or sent commands to the device.
2. Run [`gsm_hello_world.py`](lizardbolt/gsm_hello_world.py) to test your connection. At this point, you just want to make sure you get back "OK" when you send "AT".

### Case and form factor

TODO current plan:

* Use custom 3D printing service to commission a case. Ask for digital design and keep in git.
* Case should be foldable so that the keyboard rests on top of the screen but does not touch the screen. Case should snap shut so that it remains shut when carrying. Case should allow a user to hold the device by the keyboard when unfolded (unless this would make the case excessively bulky).
* Case should expose all of the following I/O ports:
  * USB 2.0 and 3.0 ports on left side of screen.
  * RJ-45 Ethernet port next to USB ports.
  * 3.5mm audio jack on top of screen.
  * HDMI ports on top of screen (there are 3 mini HDMI ports and one large HDMI port between the Pi and the screen; the center mini HDMI on the Pi and the large HDMI on the screen are connected and do not need to be exposed)
  * TODO access to phone battery for recharging.
  * USB-C port on keyboard for recharging.
* Case should allow the following components to be stored snugly (they should not come out if case is flipped upside down or is in motion) in the case itself:
  * Stylus.
  * SIM800C USB to GSM Module.
* Bottom of case should have logo embedded (coloring depends on pricing, could be completely subdued).
* Case should have holes for better heat dissipation? Ask electrical engineers.
* Case should be black or steel gray.

## References

* [PiPhone](https://github.com/climberhunt/PiPhone)
