# HIC - The Hiker's Information Companion.

  This was a project I set out to finish during reading week of Fall 2023. It's meant to be a mobile weather station of sorts used for hiking that runs off an external power source (AA's in this case). The OLED displays graphs for temperature, humidity, atmospheric pressure, and altitude using the BME280 sensor. Pressing the button to the right of the OLED cycles through the graphs. Graphs are not volatile, so cycling through the graphs won't lose data, but if the system gets turned off, then data will be lost.

  I used CircuitPython and the Thonny IDE. I probably could have used VS Code or something a little more heavyweight, but Thonny allowed me to do what I wanted to and was pretty straightforward to use. The libraries included are detailed in the following image.

![image](https://github.com/DavidJamesAdam/HIC---The-Hiker-s-Information-Companion./assets/51091241/8e6b3fed-1c29-4448-84a4-0e60d41a5a57)

Components used:
- BME280
- SSD 1351 OLED screen
- Raspberry Pi Pico
- External power supply
- Push button

  It all started with coming across an article from SlashGear [The Raspberry Pi Creation You'll Want To Bring On A Hike](https://www.slashgear.com/1421026/raspberry-pi-altitude-reader/). Getting the BME280 running was pretty straightforward. The [documentation](https://learn.adafruit.com/adafruit-bme280-humidity-barometric-pressure-temperature-sensor-breakout/downloads) associated with the sensors had some excellent tips and code snippets.

  The next milestone was to get the OLED wired up. It was very tough coming across some good documentation or tutorials for using the SSD1351 with the pico, but I eventually came across [this](https://www.youtube.com/watch?v=TGcLY4kgq2o&t=225s&ab_channel=educ8s.tv) video that gave a layout of wiring and code. After some adjusting the code a bit, I got a short demo working.

  ![IMG_20231113_233030_052](https://github.com/DavidJamesAdam/HIC---The-Hiker-s-Information-Companion./assets/51091241/575e7a15-af72-4baf-b4f3-7a8101a90114)


  The next hurdle was creating the graphs from scratch. Luckily, Adafruit has some great tutorials and the documentation associated with the libraries I was using had really nice breakdowns and code examples. Using Sparkline from the shapes library, it allowed information to be updated in real time. Once I got one graph done, it was easy to make the other three and program the push button to cycle through the graphs. [Here's](https://youtu.be/tgIHHFBBK1g) a video of the final product.

Front view

![PXL_20231117_002222801 RAW-01 COVER](https://github.com/DavidJamesAdam/HIC---The-Hiker-s-Information-Companion./assets/51091241/a934a139-4a6c-4a71-8778-f19d05a9ddc6)

Back view

![PXL_20231117_002234306 RAW-01 COVER](https://github.com/DavidJamesAdam/HIC---The-Hiker-s-Information-Companion./assets/51091241/b027b28b-ecfe-4bbe-83b9-1cdd45534502)

Schematic

![HIC_schem](https://github.com/DavidJamesAdam/HIC---The-Hiker-s-Information-Companion./assets/51091241/716490e8-9fec-43eb-8437-c86ae011b4df)

Breadboard layout 

![HIC_bb](https://github.com/DavidJamesAdam/HIC---The-Hiker-s-Information-Companion./assets/51091241/eb92e0d7-4d9b-46f9-884f-eb0cf3b26d7e)

Resources used

BME280
- https://learn.adafruit.com/adafruit-bme280-humidity-barometric-pressure-temperature-sensor-breakout/downloads

SSD1351 OLED and libraries
- https://www.youtube.com/watch?v=TGcLY4kgq2o&t=225s&ab_channel=educ8s.tv
- https://docs.circuitpython.org/projects/display-shapes/en/latest/index.html
- https://docs.circuitpython.org/projects/display_text/en/latest/index.html
- https://learn.adafruit.com/circuitpython-display-support-using-displayio
- https://learn.adafruit.com/adafruit-1-5-color-oled-breakout-board/circuitpython-displayio-quickstart

Other resources
- https://www.digikey.ca/en/maker/projects/clue-sensor-plotter-in-circuitpython/ca8e5c08f67d46bd88b5315118661fd7
- https://learn.adafruit.com/multi-tasking-with-circuitpython/buttons
- https://learn.adafruit.com/multi-tasking-with-circuitpython/no-sleeping
- https://www.youtube.com/watch?v=0OX5qHCODqQ&ab_channel=JohnGallaugher
- https://learn.adafruit.com/making-a-pyportal-user-interface-displayio/the-full-code
