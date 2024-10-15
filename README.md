


# Raspberry Pi Live Video Streaming

**Stream live video from your Raspberry Pi to your mobile device over the same Wi-Fi hotspot.**

## Features

- **Real-Time Streaming**: View live video feed from the Raspberry Pi camera on your mobile device.
- **Web-Based Interface**: Access the stream through any modern web browser without needing additional apps.
- **Mobile-Friendly Design**: Optimized for seamless viewing on smartphones and tablets.

## Hardware Requirements

- **Raspberry Pi**: Model 3B+, 4, or later for optimal performance.
- **Camera Module**: Raspberry Pi Camera Module V2 or HQ Camera.
- **Power Supply**: Adequate power adapter for the Raspberry Pi.
- **MicroSD Card**: 8GB or larger with Raspberry Pi OS installed.
- **Wi-Fi Hotspot**: Ensure both Raspberry Pi and the mobile device are connected to the same Wi-Fi network.
- **Cables and Connectors**: Necessary cables for connecting the camera module to the Raspberry Pi.

## Software Requirements

- **Operating System**: Raspberry Pi OS (64-bit recommended) or another compatible Linux distribution.
- **Python 3.x**: Pre-installed on Raspberry Pi OS.
- **Python Libraries**:
  - `Flask`: Web framework for serving the video stream.
  - `OpenCV`: Computer vision library for capturing and processing video frames.

## Installation

1. **Clone the Repository**

   Clone this repository to your Raspberry Pi to access all necessary files.

   ```bash
   git clone https://github.com/Tajbir09/pi-live-stream.git
   cd pi-live-stream
   ```

2. **Set Up the Camera**

   - **Connect the Camera**: Attach the camera module to the Raspberry Pi's camera interface (CSI port).
   - **Enable the Camera**:
     - Open the terminal and run `sudo raspi-config`.
     - Navigate to **Interface Options** > **Camera** > **Enable**.
     - Reboot the Raspberry Pi to apply changes:

       ```bash
       sudo reboot
       ```

3. **Install Required Libraries**

   Ensure that `Flask` and `OpenCV` are installed on your Raspberry Pi to handle the video streaming functionality.

   ```bash
   pip3 install flask opencv-python
   ```

   *Note: If `pip3` is not installed, you can install it using `sudo apt-get install python3-pip`.*

## Usage

### Running the Stream

- **File to Run**: `live_stream.py`
  
  Execute this Python script on your Raspberry Pi to start the live video stream.

  ```bash
  python3 live_stream.py
  ```

### Accessing the Stream on Mobile

1. **Connect to the Same Wi-Fi Network**

   Ensure your mobile device is connected to the same Wi-Fi hotspot as the Raspberry Pi.

2. **Find Raspberry Pi’s IP Address**

   - Use the Raspberry Pi terminal to find its IP address by running `hostname -I`.
   - Alternatively, refer to the network settings on your router to identify connected devices.

3. **Open Web Browser on Mobile**

   - Launch any web browser on your mobile device (e.g., Chrome, Safari).
   - Enter the following URL, replacing `<Raspberry_Pi_IP>` with the actual IP address of your Raspberry Pi:
     ```
     http://<Raspberry_Pi_IP>:5000/
     ```
   - Example:
     ```
     http://192.168.1.10:5000/
     ```

4. **View the Live Stream**

   The browser will display the live video feed from your Raspberry Pi’s camera.

## Project Structure

```
pi-live-stream/
├── assets/
│   └── pi_camera.jpg
├── live_stream.py
├── README.md
├── LICENSE
└── .gitignore
```

- **assets/**: Contains images and other static assets related to the project.
- **live_stream.py**: Python script for capturing and streaming video.
- **README.md**: Documentation file (this file).
- **LICENSE**: Licensing information.
- **.gitignore**: Specifies files and directories to be ignored by Git.

## Troubleshooting

- **Camera Not Detected**
  - Verify that the camera module is securely connected to the Raspberry Pi's CSI port.
  - Ensure the camera is enabled in the Raspberry Pi settings.
  - Test the camera functionality with a simple capture command.

    ```bash
    raspistill -o test.jpg
    ```

    If the camera is working, this command should capture an image named `test.jpg`.

- **Stream Not Accessible**
  - Confirm both devices are on the same Wi-Fi network.
  - Double-check the Raspberry Pi’s IP address.
  - Ensure no firewall settings are blocking port `5000`.

- **Low Video Quality or Lag**
  - Reduce the camera resolution for better performance.
  - Ensure a strong Wi-Fi signal to minimize latency.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- **OpenCV**: For providing robust computer vision libraries.
- **Flask**: For the lightweight web framework facilitating easy streaming.
- **Raspberry Pi Foundation**: For enabling powerful and versatile computing on a small scale.
- **Community Contributors**: Special thanks to all contributors who have helped improve this project.



