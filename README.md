# pifan
pifan provides basic IO fan control of a Raspberry Pi. This was a playful development project for me to familiarize myself with Raspberry Pi, Python, and GPIO control, in addition to just keeping my new shiny Raspberry Pi 4 running cool.

This script ***does*** have the ability to keep the Pi at a specified setpoint using a PID controller and PWM output, but I since the fan I'm using is brushless, PWM results in an obnoxious clicking noise that is louder than just running the fan at 100% output, so I defaulted to using basic on/off control.
 
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

#### Configuration file
To use on/off mode, change the mode config entry to:
```
mode = "on_off"
```

## Deployment

Add additional notes about how to deploy this on a live system


## Authors

* **Eric Baggen** - *Initial work*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

[Jeff Geerling for inspiration of using a Pi fan with the official Raspberry Pi 4 case](https://www.jeffgeerling.com/blog/2019/raspberry-pi-4-needs-fan-heres-why-and-how-you-can-add-one)

