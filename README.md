---
layout: post
title: ZCU106
date:  2021-06-29 00:00:00 -1000
categories:
---

* TOC
{:toc}

# Vivado Installation

* Download installer: `Xilinx_Unified_2021.1_0610_2318_Lin64.bin`
* Run installer and then download a local network drive image

    This makes it easier to install on multiple PCs later...

* For Ubuntu 20.04, before running `./xsetup`, first do the following:

    `sudo ln -s /lib/x86_64-linux-gnu/libtinfo.so.6  /lib/x86_64-linux-gnu/libtinfo.so.5` 

    If you don't do this, the installer will fail at a later stage.

* run `./xsetup`
* Install Vitis: this includes Vivado!
* Install PetaLinux

# KV260

* [Official Documentation](https://www.xilinx.com/products/som/kria/kv260-vision-starter-kit.html#documentation)
* [Motherboard Schematic](https://www.xilinx.com/member/forms/download/design-license.html?cid=3eb7e365-5378-461f-b8b0-bb3dad84eb4e&filename=xtp682-kria-k26-carrier-card-schematic.zip)
* [Kria K26 SOM Wiki](https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/1641152513/Kria+K26+SOM)

* [Kria SOM Carrier Card - Design Guide](https://www.xilinx.com/support/documentation/user_guides/som/ug1091-carrier-card-design.pdf)
	
	* How to design a board that uses a Kria SOM.
	* Figure 1 is important because it shows which SOM pins are going where.

* [Kria K26 SOM Data Sheet](https://www.xilinx.com/support/documentation/data_sheets/ds987-k26-som.pdf)

	* Quite a bit of overlap with the SOM Carrier Card Design Guide.

* [Kria KV260 Vision AI Starter Kit DataSheet](https://www.xilinx.com/support/documentation/data_sheets/ds986-kv260-starter-kit.pdf)

	*  Low of useful info.

* [Kria KV260 Vision AI Starter Kit User Guide](https://www.xilinx.com/support/documentation/user_guides/som/1_0/ug1089-kv260-starter-kit.pdf)

	* Describes connectors, boot devices and firmware, getting started info, tools integration overview, board reset and firmware update/recovery.
	

* Download petalinux image from [this getting started link](https://www.xilinx.com/products/som/kria/kv260-vision-starter-kit/kv260-getting-started/setting-up-the-sd-card-image.html), 
  not from [this one](https://xilinx.github.io/kria-apps-docs/docs/smartcamera/smartcamera_landing.html).
* Once the initial getting started is up and running, then use the command line options of the github smartcamera page.
	* E.g. try with different resolution, try with rtsp -> VLC


* [KV260 Vitis - Design Examples Repo](https://github.com/Xilinx/kv260-vitis)

	* [Board Files](https://github.com/Xilinx/kv260-vitis/tree/release-2020.2.2_k26/platforms/vivado/board_files)

# SOM240 pinout to Start Kit

* Based on schematic, board files, and project xdc

	* [kv260_ispMipiRx_vcu_DP](https://github.com/Xilinx/kv260-vitis/blob/release-2020.2.2_k26/platforms/vivado/kv260_ispMipiRx_vcu_DP/xdc/pin.xdc)

See `kv260_pinout.py`.

M2C: module to carrier board
C2M: carrier board to module


* IAS0 connector: OnSemi image access system (IAS) camera module interfacesupporting four MIPI lanes. 
  Connects to OnSemi AP1302 ISP device sensor 0 interface.
* IAS1 connector: OnSemi IAS camera module interface supporting four MIPI lanes.
* JTAG: when FTDI chip has `LS_OE_B` pin asserted then JTAG pins are driven. Otherwise, the JTAG connector can take over.


# Tutorial

* [Xilinx ZCU102 Tutorial](https://xilinx.github.io/Embedded-Design-Tutorials/master/docs/Introduction/ZynqMPSoC-EDT/README.html)

* [Zynq UltraScale+ Device - Technical Reference Manual](https://www.xilinx.com/support/documentation/user_guides/ug1085-zynq-ultrascale-trm.pdf)

    Required reading for better general understanding of how IOs are mapped etc.
