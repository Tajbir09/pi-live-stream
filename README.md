# Raspberry Pi Live Video Streaming

![Raspberry Pi](https://github.com/Tajbir09/pi-live-stream)

*Stream live video from your Raspberry Pi to your mobile device over the same Wi-Fi hotspot.*

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Stream](#running-the-stream)
  - [Accessing the Stream on Mobile](#accessing-the-stream-on-mobile)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview

The **Raspberry Pi Live Video Streaming** project allows you to stream real-time video from your Raspberry Pi's camera module to any device connected to the same Wi-Fi hotspot, such as a smartphone or tablet. This setup is ideal for monitoring, surveillance, or simply viewing the Raspberry Pi's camera feed remotely.

## Features

- **Real-Time Streaming**: View live video feed from the Raspberry Pi camera on your mobile device.
- **Web-Based Interface**: Access the stream through any modern web browser without needing additional apps.
- **Responsive Design**: Optimized for viewing on both desktop and mobile devices.
- **Automatic IP Detection**: Easily find and display the Raspberry Pi's IP address for quick access.

## Hardware Requirements

To set up the live video streaming, you will need the following hardware components:

- **Raspberry Pi**: Model 3B+, 4, or later for optimal performance.
- **Camera Module**: Raspberry Pi Camera Module V2 or HQ Camera.
- **Power Supply**: Adequate power adapter for the Raspberry Pi.
- **MicroSD Card**: 8GB or larger with Raspberry Pi OS installed.
- **Wi-Fi Hotspot**: Ensure both Raspberry Pi and the mobile device are connected to the same Wi-Fi network.
- **Cables and Connectors**: Necessary cables for connecting the camera module to the Raspberry Pi.

## Software Requirements

Ensure the following software is installed and properly configured on your Raspberry Pi:

- **Operating System**: Raspberry Pi OS (64-bit recommended) or another compatible Linux distribution.
- **Python 3.x**: Pre-installed on Raspberry Pi OS.
- **Python Libraries**:
  - `Flask`: Web framework for serving the video stream.
  - `OpenCV`: Computer vision library for capturing and processing video frames.

## Installation

Follow these steps to set up the live video streaming feature on your Raspberry Pi.

### 1. Clone the Repository

Clone this repository to your Raspberry Pi:

```bash
git clone https://github.com/yourusername/pi-live-stream.git
cd pi-live-stream
