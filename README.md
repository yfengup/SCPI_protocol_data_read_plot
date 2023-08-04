# SCPI_protocol_data_read_plot
Use the pyserial package to read and plot the measurement data of the instrument in real time through the SCPI protocol

# SCPI protocol

## What is the SCPI protocol

SCPI (Standard Commands for Programmable Instruments) is a standard command set, published in 1990 together with the IEEE 488.2 protocol, which defines a set of standard syntax and commands for controlling programmable test and measurement instruments. A standardized instrument programming language based on existing standards IEEE488.1 and IEEE488.2. Compatibility of programming environments is ensured through the use of standardized programming messages, instrument responses, and data formats.

## What can the SCPI protocol do?

Use SCPI to remotely interact with the instrument, such as configuring instrument parameters, obtaining instrument data, etc. All commands in SCPI exist in the form of ASCII code strings. After the user sends a string to the instrument, the data returned by the instrument is also a string, and then the user needs to analyze the meaning of the returned string. Compatible with various communication methods such as Ethernet, GPIB and serial ports, and no matter which programming language the user uses, such as C++, Java, Python, etc., the SCPI command string sent by the user is also the same.

## Some syntax requirements of the SCPI protocol

Each SCPI command requires an end character, which supports either "\0" or "\n" as the end character. It is recommended to use "\n" as the end character of the command, so that each time the command is sent, the end of the string must be appended with an "n"
The same command generally has two types: setting and query. For example: RATE?, this is a command to query the update rate, where? Indicates that the command is a query command, :RATE 1, which is a command to set the update rate, where 1 means to set the update rate to 1s
SCPI command strings are case insensitive
The lower case of the SCPI command set can be omitted, and the upper case cannot be omitted. When the command
When there are parameters, use an English space to separate the command and the parameter.
Commands are not allowed to be separated by spaces.
When a command has multiple parameters, separate different parameters with commas.

# Use pyserial to read and save (txt and csv files) through the SCPI protocol serial port, and draw the measurement curve in real time

Although the communication protocol used by the instrument is the SCPI protocol, the RS485 interface can still use the serial communication method for interaction.

To read serial port information in Python, you need to use the PySerial module. PySerial is a serial communication library for Python that allows you to access serial ports in Python applications. By using PySerial, we can easily communicate with serial devices, such as Arduino, Raspberry Pi and other devices. This is [pyserial official website](https://pyserial.readthedocs.io/en/latest/pyserial.html), please check it yourself if you encounter any problems.
