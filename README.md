**People count application With Deepstream SDK and Transfer Learning Toolkit**

* [Description](#description)
* [Prerequisites](#prerequisites)
* [Getting Started](#GettingStarted)
* [Build](#build)
* [Run](#run)
* [Output](#output)
* [References](#references)
<p align="center">
  <img src="images/test.png">
</p>

## Description 

  This is a sample application for counting people entering/leaving in a building using NVIDIA Deepstream SDK, Transfer Learning Toolkit (TLT) and pre-trained models. This application can be used to build real-time occupancy analytics application for smart buildings, hospitals, retail, etc. The application is based on deepstream-test5 sample application.

   It can take streaming video or Neon camera as input, counts the number of people crossing a tripwire. In this application, you will learn:

  - How to use PeopleNet model from NGC
  - How to use NvDsAnalytics plugin to draw line and count people crossing the line
 
  You can extend this application to change region of interest, use cloud-to-edge messaging to trigger record in the DeepStream application or build analytic dashboard or database to store the metadata.

To learn how to build this demo step-by-step, check out the on-demand webinar on [Creating Intelligent places using DeepStream SDK](https://info.nvidia.com/iva-occupancy-webinar-reg-page.html?ondemandrgt=yes).

## Prerequisites

- Neon-201A-JNX or Neon-202A-JNX with jetpack [5.1.2](https://aiot-ist.github.io/neon/neon-2000-jnx/howtoflashimage/)

- Download PeopleNet model: [https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/peoplenet/files]

- This application is based on deepstream-test5 application. More about test5 application: [https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_ref_app_test5.html]

## Getting Started

- Preferably clone the repo in /opt/nvidia/deepstream/deepstream-6.3/sources/apps/sample_apps
  
  ```
  sudo apt-get update && sudo apt-get upgrade -y
  sudo apt-get install libjson-glib-dev libgstrtspserver-1.0-dev -y
  sudo chmod 777 -R /opt/nvidia/deepstream/deepstream-6.3/
  git clone https://github.com/AIoT-IST/deepstream-occupancy-analytics.git /opt/nvidia/deepstream/deepstream-6.3/sources/apps/sample_apps/deepstream-occupancy-analytics/
  ```

- Download peoplnet model: 
```
cd /opt/nvidia/deepstream/deepstream-6.3/sources/apps/sample_apps/deepstream-occupancy-analytics/deepstream-occupancy-analytics/config && ./model.sh
```
- For Jetson use:  bin/jetson/libnvds_msgconv.so

## Build and Configure

- Set CUDA_VER in the MakeFile as per platform.

  For Jetson, CUDA_VER=11.4
  ```
  cd /opt/nvidia/deepstream/deepstream-6.3/sources/apps/sample_apps/deepstream-occupancy-analytics && make
  ```

## Run 

  ```
  cd /opt/nvidia/deepstream/deepstream-6.3/sources/apps/sample_apps/deepstream-occupancy-analytics/
  ./deepstream-test5-analytics -c config/dstest_occupancy_analytics.txt
  ```

## Modify the boarder
  ```
  cd /opt/nvidia/deepstream/deepstream-6.3/sources/apps/sample_apps/deepstream-occupancy-analytics/tool
  python3 preview.py
  ```

## Output

  The output will look like this: 

  ![alt-text](images/kafka_messages.gif)

  Where you can see the kafka messages for entry and exit count.

## References

- CREATE INTELLIGENT PLACES USING NVIDIA PRE-TRAINED VISION MODELS AND DEEPSTREAM SDK: [https://info.nvidia.com/iva-occupancy-webinar-reg-page.html?ondemandrgt=yes]
- Deepstream SDK: [https://developer.nvidia.com/deepstream-sdk]
- Deepstream Quick Start Guide: [https://docs.nvidia.com/metropolis/deepstream/dev-guide/index.html#page/DeepStream_Development_Guide/deepstream_quick_start.html#]
- Transfer Learning Toolkit: [https://developer.nvidia.com/transfer-learning-toolkit]
- forked from https://github.com/NVIDIA-AI-IOT/deepstream-occupancy-analytics
