# switchdin-test
Skills Test for SwitchDin Implementing the MQTT Pattern and has the following components:

- A client which publishes a random number at random intervals
- A subscriber which subscribes to the above random number and calculates 1,5,30 Minute Averages and publishes it to different topics
- A subscriber which subscribes to the various averages and prints them out in a tabular format using the PrettyTable Python Module

Modules Required
- Paho
- PrettyTable
