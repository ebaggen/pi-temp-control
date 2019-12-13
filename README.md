# PiFan
PiFan provides basic IO fan control of a Raspberry Pi. This was a playful development project for me to familiarize myself with Raspberry Pi, Python, and GPIO control, in addition to just keeping my new shiny Raspberry Pi 4 running cool.

This script ***does*** have the ability to keep the Pi at a specified setpoint using a PID controller and PWM output, but I since the fan I'm using is brushless, PWM results in an obnoxious clicking noise that is louder than just running the fan at 100% output, so I defaulted to using basic on/off control.
 
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

#### Hardware Needed ####

***TODO***

#### Wiring

***TODO***

#### Configuration file

##### On/Off Mode

To use on/off mode, change the mode config entry to:
```
mode = "on_off"
```
In on/off mode, the fan will turn on when the internal temperature exceeds the On Temperature, and off when falling below the Off Temperature. These temperatures can be changed in the configuration file.

##### Variable Speed Mode

Want your fan to change speed based on how far away the internal temperature is from a defined setpoint? PiFan supports this through the implementation of a basic PID controller. The control variable is a speed setpoint between 0 and 100%, which is passed as a PWM duty cycle of the digital output controlling the fan.

## Authors

* **Eric Baggen** - *Initial work*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

[Jeff Geerling for inspiration of using a Pi fan with the official Raspberry Pi 4 case](https://www.jeffgeerling.com/blog/2019/raspberry-pi-4-needs-fan-heres-why-and-how-you-can-add-one)

