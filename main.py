import time
import board
import busio
import terminalio
import displayio
import digitalio
from adafruit_bme280 import basic as adafruit_bme280
from adafruit_display_text import label
from adafruit_ssd1351 import SSD1351
from adafruit_display_shapes.sparkline import Sparkline
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.line import Line


# |--- We are setting up our GPIO pins and and digital logic here ---|

# Create sensor object, using the board's default I2C bus.
i2c = busio.I2C(board.GP1, board.GP0)  # SCL, SDA
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 996.21

#| Setting up button stuff |
# Setting up the button
button = digitalio.DigitalInOut(board.GP22)
button.switch_to_input(pull = digitalio.Pull.UP)

# Used for cycling through graphs when button pushed
i = 1


# | Setting up the OLED with displayio |
# Release any resources currently in use for the displays
displayio.release_displays()

# Setting pins to Pico GP pins
clk_pin, mosi_pin, reset_pin, dc_pin, cs_pin = board.GP18, board.GP19, board.GP16, board.GP20, board.GP17
    
spi = busio.SPI(clock = clk_pin, MOSI = mosi_pin)

display_bus = displayio.FourWire(spi, command = dc_pin, chip_select = cs_pin, reset = reset_pin, baudrate=16000000)

display = SSD1351(display_bus, width=128, height=128)

# |--- Creating canvas and graphs ---|

# This is our root group
splash = displayio.Group()
display.root_group = splash

# Our four different graph subgroups
tempGraph = displayio.Group() # Temperature
humGraph = displayio.Group() # Humidity
presGraph = displayio.Group() # Atmospheric Pressure
altGraph = displayio.Group() # Altitude

# Adding graph subgroups to root group
splash.append(tempGraph)
splash.append(humGraph)
splash.append(presGraph)
splash.append(altGraph)

# Graph size for all graphs
chart_width = 108
chart_height = 117

# | Temperature Graph |

# Minimum temp
temp = 10

# Title
tempTitle = label.Label(terminalio.FONT,
                          text = "Temperature °C",
                          color = 0xffffff,
                          anchor_point = (1, 0.5),
                          anchored_position = (128, 5)
                          )
tempGraph.append(tempTitle)

# Horizontal lines and y axis labels
for x in range(123, 8, -int(110/10)):
    maxTemp_area = label.Label(terminalio.FONT,
                          text = str(temp),
                          color = 0xffffff,
                          anchor_point = (0, 0.5),
                          anchored_position = (0, x)
                          )
    tempGraph.append(maxTemp_area)
    tempGraph.append(Line(15, x, 123, x, 0x5a5a5a))
    temp += 2
    
# Vertical lines to complete the graph
for x in range(15, 125, int(120/10)):
    tempGraph.append(Line(x, 14, x, 123, 0x5a5a5a))

# Dynamic graph line that displays data
tempSparkline = Sparkline(width = chart_width,
                       height = chart_height,
                       max_items = 120,
                       y_min = 10,
                       y_max = 30,
                       x = 16,
                       y = 10,
                       color = 0x08ff08)
tempGraph.append(tempSparkline)


# | Humidity graph |

# Minumum humidity
hum = 40

# Title
humTitle = label.Label(terminalio.FONT,
                          text = "Humidity %",
                          color = 0xffffff,
                          anchor_point = (1, 0.5),
                          anchored_position = (128, 5)
                          )
humGraph.append(humTitle)

# Horizontal lines and y axis labels
for x in range(123, 8, -int(110/10)):
    maxHum_area = label.Label(terminalio.FONT,
                          text = str(hum),
                          color = 0xffffff,
                          anchor_point = (0, 0.5),
                          anchored_position = (0, x)
                          )
    humGraph.append(maxHum_area)
    humGraph.append(Line(15, x, 123, x, 0x0000b9))
    hum += 5
    
# Vertical lines to complete the graph
for x in range(15, 125, int(120/10)):
    humGraph.append(Line(x, 14, x, 123, 0x0000b9))

# Dynamic graph line that displays data
humSparkline = Sparkline(width = chart_width,
                       height = chart_height,
                       max_items = 120,
                       y_min = 40,
                       y_max = 90,
                       x = 16,
                       y = 10,
                       color = 0xffff00)
humGraph.append(humSparkline)

# | Atmospheric Pressure Graph

# Minimum pressure
pres = 870

# Title
presTitle = label.Label(terminalio.FONT,
                          text = "Pressure (hPa)",
                          color = 0xffffff,
                          anchor_point = (1, 0.5),
                          anchored_position = (128, 5)
                          )
presGraph.append(presTitle)

# Horizontal lines and y axis labels
for x in range(123, 8, -int(90/10)):
    maxPres_area = label.Label(terminalio.FONT,
                          text = str(pres),
                          color = 0xffffff,
                          anchor_point = (0, 0.5),
                          anchored_position = (0, x)
                          )
    presGraph.append(maxPres_area)
    presGraph.append(Line(18, x, 126, x, 0xca0000))
    pres += 10
    
# Vertical lines to complete the graph
for x in range(18, 128, int(120/10)):
    presGraph.append(Line(x, 14, x, 123, 0xca0000))

# Dynamic graph line that displays data
presSparkline = Sparkline(width = chart_width,
                       height = chart_height,
                       max_items = 120,
                       y_min = 870,
                       y_max = 930,
                       x = 19,
                       y = 10,
                       color = 0x00def0)
presGraph.append(presSparkline)


# | Altitude graph |

# Minimum altitude
alt = 800

# Title
altTitle = label.Label(terminalio.FONT,
                          text = "Altitude (k-meters)",
                          color = 0xffffff,
                          anchor_point = (1, 0.5),
                          anchored_position = (128, 5)
                          )
altGraph.append(altTitle)

# Horizontal lines and y axis labels
for x in range(123, 8, -int(110/10)):
    maxAlt_area = label.Label(terminalio.FONT,
                          text = str(alt),
                          color = 0xffffff,
                          anchor_point = (0, 0.5),
                          anchored_position = (0, x)
                          )
    altGraph.append(maxAlt_area)
    altGraph.append(Line(18, x, 126, x, 0xc35600))
    alt += 2
    
# Vertical lines to complete the graph
for x in range(18, 128, int(120/10)):
    altGraph.append(Line(x, 14, x, 123, 0xc35600))

# Dynamic graph line that displays data
altSparkline = Sparkline(width = chart_width,
                       height = chart_height,
                       max_items = 120,
                       y_min = alt,
                       y_max = 1500,
                       x = 19,
                       y = 10,
                       color = 0x00fff7)
altGraph.append(altSparkline)

# Set visibility of target object inside of layer
def layerVisibility(state, layer, target):
    try:
        if state == "show":
            time.sleep(0.1)
            layer.append(target)
        elif state == "hide":
            layer.remove(target)
    except ValueError:
        pass
    
layerVisibility("show", splash, tempGraph)
layerVisibility("hide", splash, humGraph)
layerVisibility("hide", splash, presGraph)
layerVisibility("hide", splash, altGraph)

def switch_view(what_view):
    if what_view == 1:
        layerVisibility("hide", splash, humGraph)
        layerVisibility("hide", splash, presGraph)
        layerVisibility("hide", splash, altGraph)
        layerVisibility("show", splash, tempGraph)
    elif what_view == 2:
        layerVisibility("show", splash, humGraph)
        layerVisibility("hide", splash, presGraph)
        layerVisibility("hide", splash, altGraph)
        layerVisibility("hide", splash, tempGraph)
    elif what_view == 3:
        layerVisibility("hide", splash, humGraph)
        layerVisibility("show", splash, presGraph)
        layerVisibility("hide", splash, altGraph)
        layerVisibility("hide", splash, tempGraph)
    elif what_view == 4:
        layerVisibility("hide", splash, humGraph)
        layerVisibility("hide", splash, presGraph)
        layerVisibility("show", splash, altGraph)
        layerVisibility("hide", splash, tempGraph)

while True:
    if button.value == False:
        if i == 1:
            switch_view(2)
            i = 2
        elif i == 2:
            switch_view(3)
            i = 3
        elif i == 3:
            switch_view(4)
            i = 4
        elif i == 4:
            switch_view(1)
            i = 1
    
    display.auto_refresh = False
    tempSparkline.add_value(bme280.temperature)
    humSparkline.add_value(bme280.relative_humidity)
    presSparkline.add_value(bme280.pressure)
    altSparkline.add_value(bme280.altitude)
    display.auto_refresh = True
    print("\nTemperature: %0.1f C" % bme280.temperature)
    print("Humidity: %0.1f %%" % bme280.relative_humidity)
    print("Pressure: %0.1f hPa" % bme280.pressure)
    print("Altitude: %0.2f meters" % bme280.altitude)
    time.sleep(0.1)
