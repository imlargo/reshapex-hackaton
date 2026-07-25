OPERATING INSTRUCTIONS


Sensor Integration Gateway - SIG350
PROFINET

Integration Products

Described product
                                   SIG – Sensor Integration Gateway
                                   SIG350 - PROFINET

                                   Manufacturer
                                   SICK AG
                                   Erwin-Sick-Str. 1
                                   79183 Waldkirch
                                   Germany

                                   Legal information
                                   This work is protected by copyright. Any rights derived from the copyright shall be
                                   reserved for SICK AG. Reproduction of this document or parts of this document is
                                   only permissible within the limits of the legal determination of Copyright Law. Any modi‐
                                   fication, abridgment or translation of this document is prohibited without the express
                                   written permission of SICK AG.
                                   The trademarks stated in this document are the property of their respective owner.
                                   © SICK AG. All rights reserved.

                                   Original document
                                   This document is an original document of SICK AG.




                                                                                                   54PM




                                                                                         NO

                                                                                      2006/42/EC
                                                                                       SAFETY




2   O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                        8027832./2022-06-10 | SICK
                                                                                                          Subject to change without notice

CONTENTS


Contents
                                   1   About this document........................................................................                              5
                                       1.1     Further information...................................................................................            5
                                       1.2     Explanation of symbols............................................................................                5

                                   2   Safety information............................................................................                           6
                                       2.1     Intended use.............................................................................................        6
                                       2.2     Improper use.............................................................................................        6
                                       2.3     General safety notes................................................................................             7
                                       2.4     Notes on UL approval...............................................................................              7

                                   3   Product description...........................................................................                           8
                                       3.1     General information..................................................................................             8
                                       3.2     Operating elements and status indicators..............................................                           13

                                   4   Transport and storage....................................................................... 17
                                       4.1     Transport...................................................................................................     17
                                       4.2     Transport inspection.................................................................................            17
                                       4.3     Storage......................................................................................................    17

                                   5   Mounting............................................................................................. 18
                                       5.1     Prerequisites.............................................................................................       18
                                       5.2     Module mounting......................................................................................            18
                                       5.3     Mounting of functional earth...................................................................                  19
                                       5.4     Rotary switch cover...................................................................................           20
                                       5.5     Scope of delivery.......................................................................................         21

                                   6   Electrical installation........................................................................ 22
                                       6.1     Electrical installation................................................................................          22
                                       6.2     Pin assignment.........................................................................................          22
                                       6.3     Supply concept.........................................................................................          24
                                       6.4     Derating.....................................................................................................    25

                                   7   Commissioning.................................................................................. 26
                                       7.1     IP address.................................................................................................      26
                                       7.2     MAC address.............................................................................................         26
                                       7.3     Rotary switch.............................................................................................       27
                                       7.4     PROFINET parameters..............................................................................                28
                                       7.5     Data security.............................................................................................       28

                                   8   Operation............................................................................................ 29
                                       8.1     Profinet integration...................................................................................          29
                                       8.2     Dual Talk....................................................................................................    51
                                       8.3     Web interface............................................................................................        67
                                       8.4     SOPAS Engineering Tool...........................................................................                77



8027832./2022-06-10 | SICK                                                    O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350    3
Subject to change without notice

CONTENTS


                                    9           Troubleshooting................................................................................. 80
                                                9.1        Reset to factory settings..........................................................................            80
                                                9.2        Device restart............................................................................................     80
                                                9.3        Updating firmware....................................................................................          80
                                                9.4        Fault diagnosis..........................................................................................      81

                                    10          Disassembly and disposal............................................................... 82

                                    11          Maintenance...................................................................................... 83

                                    12          Technical data.................................................................................... 84
                                                12.1 General technical data.............................................................................                  84

                                    13          Annex.................................................................................................. 87




4    O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                                                            8027832./2022-06-10 | SICK
                                                                                                                                               Subject to change without notice

ABOUT THIS DOCUMENT 1


1                     About this document
1.1                   Further information

                                   NOTE
                                   All the documentation available for the device can be found on the online product page
                                   at:
                                   b    www.sick.de/SIG350
                                   The following information is available for download from this page:
                                   •    Type-specific online data sheets for device variants, containing technical data and
                                        dimensional drawings
                                   •    EU declaration of conformity for the product family
                                   •    Dimensional drawings and 3D CAD dimension models in various electronic for‐
                                        mats
                                   •    These operating instructions, available in English and German, and in other lan‐
                                        guages if necessary
                                   •    Other publications related to the devices described here
                                   •    Publications dealing with accessories
                                   •    IO-Link driver files and IO-Link Technical Information v1.1


1.2                   Explanation of symbols
                                   Warnings and important information in this document are labeled with symbols. The
                                   warnings are introduced by signal words that indicate the extent of the danger. These
                                   warnings must be observed at all times and care must be taken to avoid accidents,
                                   personal injury, and material damage.

                                   DANGER
                                   … indicates a situation of imminent danger, which will lead to a fatality or serious
                                   injuries if not prevented.


                                   WARNING
                                   … indicates a potentially dangerous situation, which may lead to a fatality or serious
                                   injuries if not prevented.


                                   CAUTION
                                   … indicates a potentially dangerous situation, which may lead to minor/slight injuries if
                                   not prevented.


                                   NOTICE
                                   … indicates a potentially harmful situation, which may lead to material damage if not
                                   prevented.


                                   NOTE
                                   … highlights useful tips and recommendations as well as information for efficient and
                                   trouble-free operation.




8027832./2022-06-10 | SICK                                           O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   5
Subject to change without notice

2 SAFETY INFORMATION


2             Safety information
2.1           Intended use
                                     The SIG350 is a remote IO-Link input and output module for connecting a PROFINET
                                     network.

                                     Intended use requires that the device is used industrially indoors without any spe‐
                                     cific climatic and atmospheric requirements. Operation of the device according to its
                                     intended use and enclosure rating IP 67 are only guaranteed if open male and female
                                     connectors are sealed with blind plugs. Intended use also includes EMC-compliant
                                     electrical installation.
                                     If the product is used for any other purpose or modified in any way, all warranty claims
                                     against SICK AG will be void.

                                     NOTE
                                     This document is aimed at the trained specialist personnel. Qualified specialist person‐
                                     nel are persons who are familiar with work such as the installation and operation of the
                                     product, and who have the necessary qualifications for this activity. All claims against
                                     the manufacturer in respect of warranty and liability shall be invalidated in the event of
                                     damage resulting from unauthorized manipulation or incorrect use. The operating entity
                                     is responsible for ensuring that the work safety regulations and accident prevention
                                     regulations applicable in the specific individual case are observed.




2.2           Improper use
                                      •       The device does not constitute a safety-relevant device according to the EC Machi‐
                                              nery Directive (2006/42 / EC).
                                      •       The device must not be used in explosion-hazardous areas.
                                      •       Any other use that is not described as intended use is prohibited.
                                      •       Any use of accessories not specifically approved by SICK AG is at your own risk.
                                     The device is not suitable for the following applications (this list is not exhaustive):
                                      •       As a safety device to protect persons, their hands, or other body parts
                                      •       Underwater
                                      •       In explosion-hazardous areas
                                      •       Outdoors, without additional protection

                                     NOTICE
                                     Danger due to improper use!
                                     Any improper use can result in dangerous situations.
                                     Therefore, observe the following information:
                                     b        The device should be used only in line with intended use specifications.
                                     b        All information in these operating instructions must be strictly complied with.




6     O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                           8027832./2022-06-10 | SICK
                                                                                                               Subject to change without notice

SAFETY INFORMATION 2


2.3                   General safety notes

2.3.1                 Safety notes
                                     ■   Read the operating instructions before commissioning.
                                     ■

                                                        Connection, mounting, and setting may only be performed by skilled per‐
                                         son.
                                     ■        NO
                                           2006/42/EC
                                            SAFETY
                                                        Not a safety component in accordance with the EU Machinery Directive.
                                     ■


                                                When commissioning, protect the device from moisture and contamination.
                                     ■   These operating instructions contain information required during the life cycle of
                                         the sensor.

2.4                   Notes on UL approval
                                     UL Environmental Rating: Enclosure type 1




8027832./2022-06-10 | SICK                                                  O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   7
Subject to change without notice

3 PRODUCT DESCRIPTION


3               Product description
3.1             General information
                                       The SIG350 IO-Link Master is a gateway for connecting IO-Link devices as well input
                                       and/or output signals for data integration into a PLC via PROFINET . Parallel to the
                                       fieldbus communication, the data can also be transmitted to a network via the inte‐
                                       grated IIOT interfaces (REST API, MQTT or OPC UA). It is intended for use in industrial
                                       environments that require enclosure rating up to IP67.
                                       The module has eight IO-Link Master channels and eight universal digital channels
                                       (PNP). The device is connected to an M12 female connector that can be operated
                                       either in the Class A or Class B connection type.
                                       In addition, the SIG350 has a powerful user interface that can be accessed either using
                                       the SOPAS ET software from SICK or directly via the web interface. This is used to
                                       parameterize the SIG350 and the connected devices.

                                       The SIG350 can be commissioned using the following methods
                                       • Engineering tool of the PLC manufacturer
                                       • Integrated web interface
                                       • SICK SOPAS Engineering Tool application
                                       • Dual Talk interface
                                       Parameterization
                                       • Parameterization via PROFINET is performed using the engineering tool of the
                                           PLC manufacturer to access the SIG350 directly. Depending on which type of
                                           PLC engineering tool is used, parameterization of the SIG350 and the connected
                                           devices is done in different ways.
                                       • The integrated web interface of the SIG350 provides direct access for parameter‐
                                           ization via a suitable web interface on devices connected to the same Ethernet
                                           network as the SIG350.
                                       • It is also possible to connect the SIG350 to the SOPAS Engineering Tool from SICK
                                           via Ethernet for parameterization. The SOPAS Engineering Tool application can be
                                           downloaded at www.sick.com.
                                       • The SIG350 also has different IIoT interfaces (Dual Talk) that provide direct access
                                           for higher-level automation operations.

3.1.1           PROFINET
                                       The Profinet technology was developed by Siemens and the member companies of the
                                       Profibus user organization. Profinet based on Ethernet-TCP/IP. Profinet can be used
                                       to implement solutions for manufacturing technology, process automation, building
                                       automation as well as for the entire spectrum of drive technology up to synchronous
                                       motion control applications. Profinet is an open communication protocol according to
                                       IEC 61784.
                                       The SIG350 supports PROFINET specification 2.41 and follows the guideline “IO-Link
                                       Integration – Edition 2 Specification for PROFINET Version 1.1 – February 2020 Order
                                       No.: 2.832.”
                                       The PROFINET interface of the SIG350 has the following features:
                                       Table 1: Device properties
                                        Properties                                        Values
                                        Transmission rate                                 100 Mbit/s
                                        Maximum distance between                          100 m
                                        nodes



8       O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                       8027832./2022-06-10 | SICK
                                                                                                             Subject to change without notice

PRODUCT DESCRIPTION 3


                                   Properties                       Values
                                   Process data                     Max. 33 bytes at input and 32 bytes at output per port
                                                                    Minimum cycle time: 1 ms
                                   Asynchronous data                Is supported
                                   Observed standard                IEEE802.3u (100Base-Tx)
                                   Conformity class                 Class C
                                   NetLoad class                    III
                                   Ethernet connections             2
                                   PROFINET features                Media redundancy (MRP), network diagnostics (MIB/SNMP),
                                                                    topology detection, connection diagnostics (forward/back‐
                                                                    ward), link diagnostics (link length measurement), I&M0...3,
                                                                    automatic device replacement, gear reduction, OpenVAS
                                                                    tested

                                   Data exchange
                                   The PROFINET concept has a modular structure. Data is exchanged between the con‐
                                   troller, also called the IO controller, and the connected participants, the IO devices, by
                                   means of Ethernet telegrams.
                                   The devices exchange data cyclically according to the provider-consumer principle. The
                                   devices operate simultaneously as receiver (consumer) and sender (provider). The
                                   IO-devices send input data to the controller and receive output data from it.
                                   Other components of the communication protocol are telegrams in the form of acyclic
                                   communication for the transmission of parameters.

                                   Communication
                                   The communication of the SIG350 is based on a full-duplex Ethernet network with 100
                                   Mbit/s. Auto negotiation is supported.

                                   RT
                                   Within a PROFINET network, process data and alarms are always transmitted in real
                                   time (RT). With this type of data exchange, bus cycle times in the range of a few
                                   milliseconds can be achieved with the SIG350. This enables the transmission of time-
                                   critical process data between network components in real-time communication.

                                   IRT
                                   Synchronous data exchange with Profinet is defined in the isochronous real time (IRT)
                                   concept. The data exchange cycles are normally in the range of a few hundred micro‐
                                   seconds up to four milliseconds.
                                   The difference to real-time communication is essentially that the start of a bus cycle
                                   is maintained with the highest precision. The start of a bus cycle can deviate by a
                                   maximum of 1 µs (jitter). IRT is required for motion control applications (positioning
                                   processes), for example. The use of special IRT switches is required.
                                   The SIG350 can also be used in IRT networks.

                                   MRP
                                   The Media Redundancy Protocol (MRP) according to IEC 62439 describes PROFINET
                                   redundancy with a typical reconfiguration time of < 200 ms after an error. The error-free
                                   operation of an automation system involves a media redundancy manager (MRM) and
                                   several media redundancy clients (MRC) arranged in a ring.
                                   The SIG350 thus enables the construction of a highly available network infrastructure.



8027832./2022-06-10 | SICK                                                O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   9
Subject to change without notice

3 PRODUCT DESCRIPTION

                                    Conformance classes
                                    PROFINET is a communication system optimized for performance, although the com‐
                                    plete range of functions is not always required in every automation system. There
                                    are therefore 3 conformance classes (CC-A, CC-B and CC-C) with certain minimum
                                    requirements from the point of view of the plant operator.
                                    The SIG350 supports the requirements of Conformance Class C (CC-C) for the inte‐
                                    grated switch. Conformance Class C includes the requirements of Classes A and B. CC-
                                    C also enables high-precision, deterministic data transmission including synchronous
                                    applications.

                                    Fast start-up (FSU)
                                    Fast start-up is an accelerated start-up process that enables the SIG350 to establish
                                    communication in a PROFINET network after a very short time. For example, this
                                    enables faster tool changes. Thanks to the FSU function, the network is ready for
                                    communication in less than 2200 ms.

                                    Shared devices
                                    With the shared devices functionality, two controllers can access the same I/O device
                                    via the PROFINET interface. A particular advantage is the use of shared devices in
                                    systems with standard and fail-safe controllers.

                                    DCP
                                    The SIG350 uses the DCP protocol to automatically assign IP addresses.

                                    Net load class III
                                    The SIG350 offers expanded resistance to the netload according to netload class III.

                                    LLDP
                                    The LLDP protocol is used to detect devices in the environment (neighborhood detec‐
                                    tion).

                                    SNMP
                                    The SNMPv1 protocol (according to PROFINET standard V2.35) handles the monitoring
                                    of the network components and communication between master and device (stand-
                                    alone operation not possible). The SIG350 can send SNMP messages on request.

                                    Alarm & diagnostic messages
                                    The SIG350 supports advanced PROFINET alarm and diagnostic messages.

                                    I&M data
                                    Identification and maintenance data (I&M) is information that is stored on the module.
                                    The modules can be clearly identified via the I&M data. The identification data consists
                                    of manufacturer information, e.g. Part and serial number for the module and can
                                    only be read. The maintenance data consists of plant-specific information, such as
                                    installation location and installation date. It is created during project planning and
                                    stored retentively in the module.

                                    GSDML
                                    The GSDML offers the option of configuring and parameterizing the I/O ports on the
                                    master devices within an engineering tool of a PLC. It is provided at www.sick.com/
                                    SIG350.




10   O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                     8027832./2022-06-10 | SICK
                                                                                                        Subject to change without notice

PRODUCT DESCRIPTION 3


3.1.2                 IO-Link
                                   IO-Link is a standard (IEC 61131-9) that can be used to connect intelligent devices at
                                   the sensor and actuator level to an automation system.
                                   The SIG350 complies with IO-Link specification V1.1.3.

                                   Communication
                                   Communication takes place between a master and a device. An IO-Link Master con‐
                                   tains one or more ports. One device can be connected per port, which means that
                                   IO-Link is point-to-point communication and not a fieldbus. The IO-Link Master forms
                                   the interface between the higher-level fieldbus level and the IO-Link system.
                                   IO-Link is functional and enables advanced diagnostics of sensors and actuators or
                                   simple and fast parameterization through bidirectional communication. The IO-Link
                                   devices are connected to the master via unshielded 3-, 4- or 5-wire standard cables of
                                   a maximum length of 20 m.
                                   The SIG350 supports IO-Link communication at the following speeds:
                                   •    COM 1 → 4,800 baud
                                   •    COM 2 → 28,400 baud
                                   •    COM 3 → 230,400 baud
                                   The module automatically selects the communication speed that matches the IO-Link
                                   device.

                                   IO-Link modus (IOL)
                                   IO-Link communication (C/Q) is activated at pin 4, so an IO-Link device can be con‐
                                   nected.

                                   IO-Link call
                                   The acyclic data allows the device parameters to be written by an IO-Link device or
                                   parameters, measured values and diagnostic data to be read by an IO-Link device.
                                   The following tasks can be performed:
                                   • Parameterization/Configuration of an IO-Link device during operation.
                                   • Diagnosis of an IO-Link device by reading out diagnostic parameters.
                                   • Execution of IO-Link port functions.
                                   • Saving/Restoring of IO-Link device parameters.
                                   The data on the IO-Link device is uniquely addressed with index and subindex. The
                                   access to this data takes place with the so-called IOL-CALL block. This is usually
                                   provided by the PLC manufacturer as a handling block.

                                   Data storage mode
                                   The data storage mode allows IO-Link devices to be exchanged without any configura‐
                                   tion in the event of service. Both the IO-Link Master and the IO-Link device store the
                                   device parameters. During data storage, these different parameter data memories are
                                   synchronized.
                                   In the event of device replacement, the master writes the stored device parameters
                                   to the new device. The application can be restarted without further intervention via a
                                   configuration tool or the like.
                                   If the IO-Link Master is replaced, the new master reads the IO-Device parameters from
                                   the device and saves them. The “Save and Restore” data storage function must be
                                   activated for this purpose. The application can also be restarted here without further
                                   intervention via a configuration tool or the like.
                                   The data retention mode is only available for devices that comply with IO-Link version
                                   V1.1 and higher.

8027832./2022-06-10 | SICK                                          O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   11
Subject to change without notice

3 PRODUCT DESCRIPTION

3.1.3           Dual Talk (IIoT interfaces)
                                       The SIG350 features Dual Talk functionality, which allows the user to address the
                                       module from IT networks and integrate it into Internet-of-Things applications.

                                       The SIG350 contains the following interfaces:
                                       • MQTT JSON
                                       • REST API JSON
                                       • OPC UA
                                       REST API
                                       The Representational State Transfer – Application Programming Interface (REST API) is
                                       a programmable interface that uses HTTP requests for GET and POST data. This allows
                                       access to detailed device information. The format is JSON.
                                       The REST API interface of the SIG350 complies with the JSON Integration for IO-Link
                                       standard version V1.0.0 published by the IO-Link community.

                                       MQTT
                                       The MQTT (Message Queuing Telemetry Transport) protocol is an open network protocol
                                       for machine-to-machine communication that enables the transmission of telemetric
                                       data between devices.
                                       An MQTT client is integrated in the SIG350, which enables the device to publish certain
                                       information to an MQTT broker. The format is JSON.
                                       The publication of messages can either take place periodically or be triggered man‐
                                       ually.
                                       The MQTT interface of the SIG350 complies with the JSON Integration for IO-Link
                                       standard version V1.0.0 published by the IO-Link community.

                                       OPC UA
                                       OPC United Architecture (OPC UA) is a platform-independent standard with a service-
                                       oriented architecture for communication in and with industrial automation systems.
                                       The OPC UA standard is based on the client-server principle and enables machines
                                       and devices to communicate horizontally with each other and vertically with the ERP
                                       system or the cloud, regardless of the preferred fieldbus. The SIG350 provides an OPC
                                       UA server at field device level, to which an OPC UA client can connect to exchange
                                       information securely. The interface complies with the IO-Link Companion specification
                                       (version V1.0).

3.1.4           Web interface
                                       The SIG350 has an integrated web interface that provides functions for device configu‐
                                       ration and the display of status and diagnostic information via a web interface. The web
                                       interface provides an overview of the configuration and status of the device.
                                       The graphical user interface ensures fast and intuitive operation.
                                       The prerequisite for using the web interface is the existence of a valid IP address. This
                                       can be set via the rotary switches directly on the device or via the DCP tool. SICK also
                                       offers the SOPAS ET engineering tool, which can be used to configure the SIG350.

                                       For the SIG350, the default IP address when delivered is: 192.168.0.1

                                       To access the web interface, type http:// followed by the IP address, e.g. http://
                                       192.168.0.1, in the address bar of your web browser. If the device status page is
                                       not displayed, check your browser and firewall settings.



12      O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                       8027832./2022-06-10 | SICK
                                                                                                             Subject to change without notice

PRODUCT DESCRIPTION 3


3.2                   Operating elements and status indicators

3.2.1                 Model structure

                                                                                                  6
                                          S4                                                 S8
                                           0                 1      0                        1


                                   1
                                          S3                                                 S7
                                           0                 1      0                        1    7

                                          S2                                                 S6
                                           0                 1      0                        1



                                          S1                                                 S5
                                           0                 1      0                        1


                                   2            BF SF      LNK1 ST LNK2


                                                           ACT1         ACT2
                                                                               UA US


                                                                                POWER




                                                             SIG350
                                                                                                  8

                                   3
                                           PWR1                                     PWR2

                                                    x100          x10          x1


                                   4

                                   5
                                           P1                                           P2



                                                                                                  9
                                   Figure 1: Model structure
                                   1       Sensor/Actuator connection (8x): IO-Link port S1 – S8
                                   2       LED status indicators for bus and device status
                                   3       Voltage supply (2x): Voltage input (PWR1) and output (PWR2)
                                   4       Rotary switch
                                   5       Ethernet connection (2x): Ethernet Port P1 – P2
                                   6       Mounting opening
                                   7       LED display for IO-Link port S1 – S8 (2x per port)
                                   8       Marking labels (removable)
                                   9       Connection for functional earth


3.2.2                 Status indicators




8027832./2022-06-10 | SICK                                                                            O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   13
Subject to change without notice

3 PRODUCT DESCRIPTION



                                     S4                                   S8   1
                                      0              1    0               1



                                     S3                                   S7
                                      0              1    0               1



                                     S2                                   S6
                                      0              1    0               1



                                     S1                                   S5
                                      0              1    0               1

                                           BF SF   LNK1 ST LNK2   UA US


                                                   ACT1    ACT2   POWER
                                                                               2
                                    Figure 2: Status indicators
                                    1              LED status indicator for IO-Link port S1 – S8:
                                                   Each input and output is assigned its own status display:
                                                   - Channel 0 corresponds to pin 4
                                                   - Channel 1 corresponds to pin 2
                                    2              Status indicator for bus and device status
                                                   - LED BF = Bus fault
                                                   - LED SF = System fault
                                                   - LED LNK1 = Link 1
                                                   - LED ACT1 = Activity 1
                                                   - LED ST = Status
                                                   - LED LNK2 = Link 2
                                                   - LED ACT2 = Activity 2
                                                   - LED POWER UA = Supply voltage actuator
                                                   - LED POWER US = Supply voltage sensor


                                    Table 2: LEDs for IO-Link port S1 – S8
                                     LED                  Display                  Description
                                     0                    Off                      Pin 4 is not used/deactivated
                                                          Green                    Pin 4 is configured as IO-Link.
                                                                                   Communication active.
                                                          Flashing green           Pin 4 is configured as IO-Link.
                                                          (1 Hz)                   No communication.
                                                          Flashing green           Pin 4 is configured as IO-Link, but is in Pre-Operate mode. e.g.
                                                          (10 Hz)                  discrepancy DeviceID
                                                          Yellow                   Pin 4 is configured as a binary signal: 24V
                                                                                   - DI visible in process data
                                                                                   - DO can be switched via process data
                                                          Red                      Pin 4 is configured as DO:
                                                                                   Overload/Short-circuit on pin 4
                                                          Flashing red             Pin 4 is configured as DI or DO:
                                                          (1 Hz)                   Overload/Sensor supply short-circuit
                                                          Flashing red             Pin 4 is configured as IO-Link:
                                                          (2 Hz)                   - Data storage error




14   O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                                               8027832./2022-06-10 | SICK
                                                                                                                                  Subject to change without notice

PRODUCT DESCRIPTION 3


                                   LED       Display             Description
                                   1         Off                 Pin 2 is not used/deactivated
                                             Yellow              Pin 2 is configured as a binary signal: 24V
                                                                 - DI visible in process data
                                                                 - DO can be switched via process data
                                             Red                 Pin 2 is configured as DO:
                                                                 Overload/Short-circuit on pin
                                             Flashing red        Overload/Sensor supply short-circuit
                                             (1 Hz)

                                   Table 3: LEDs for bus system and status
                                   LED       Display             Description
                                   BF        Off                 Module is switched off
                                             Red                 No connection to bus system. No configuration
                                             Flashing red        No data exchange
                                             (2 Hz)
                                   SF        Off                 Module is switched off
                                             Red                 System error
                                             Flashing red        DCP signal service is initiated via bus
                                             (1 Hz)
                                   ST        Green               Module operating without errors
                                             Flashing green      The operation requested by the position of the rotary switch is
                                             (4 Hz)              performed. Do not switch off the device
                                                                 .
                                             Flashing red        Invalid rotary switch position. System does not start.
                                             (1 Hz)
                                             Red                 Initialization error:

                                                                 • Rotary switch operation failed etc.
                                                                 • Hardware problem
                                                                 • No valid configuration
                                   Table 4: LEDs for Ethernet communication
                                   LED       Display             Description
                                   LNK1 + Off                    No connection to network
                                   LNK2                          à Check cable connections
                                             Green               Connection to network present
                                   ACT1 +    Off                 Module is not sending/receiving Ethernet frames
                                   ACT2                          à Check cable connections
                                             Yellow flashing     Module is sending/receiving Ethernet frames

                                   Table 5: LEDs for supply voltage
                                   LED       Display             Description
                                   UA        Off                 No voltage: UA < 11 V
                                             Green               Module operating without errors: 18 V ≤ UA ≤ 30 V
                                             Red                 Undervoltage: 11 V ≤ UA < 18 V
                                             Flashing red        Overvoltage: UA > 30 V
                                             (4 Hz)




8027832./2022-06-10 | SICK                                               O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   15
Subject to change without notice

3 PRODUCT DESCRIPTION

                                     LED            Display                        Description
                                     US             Off                            No voltage: US < 11 V
                                                    Green                          Module operating without errors: 18 V ≤ US ≤ 30 V
                                                    Red                            Undervoltage: 11 V ≤ US < 18 V
                                                    Flashing red                   Overvoltage: US > 30 V
                                                    (4 Hz)




16   O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                                            8027832./2022-06-10 | SICK
                                                                                                                               Subject to change without notice

TRANSPORT AND STORAGE 4


4                     Transport and storage
4.1                   Transport
                                   For your own safety, please read and observe the following notes:

                                   NOTE
                                   Damage to the device due to improper transport.
                                   ■    The device must be packaged for transport with protection against shock and
                                        moisture.
                                   ■    Recommendation: Use the original packaging as it provides the best protection.
                                   ■    Transport should be performed by specialist staff only.
                                   ■    The utmost care and attention is required at all times during unloading and
                                        transportation on company premises.
                                   ■    Note the symbols on the packaging.
                                   ■    Do not remove packaging until immediately before you start mounting.


4.2                   Transport inspection
                                   Immediately upon receipt at the receiving work station, check the delivery for complete‐
                                   ness and for any damage that may have occurred in transit. In the case of transit
                                   damage that is visible externally, proceed as follows:
                                   ■    Do not accept the delivery or only do so conditionally.
                                   ■    Note the scope of damage on the transport documents or on the transport compa‐
                                        ny’s delivery note.
                                   ■    File a complaint.

                                   NOTE
                                   Complaints regarding defects should be filed as soon as these are detected. Damage
                                   claims are only valid before the applicable complaint deadlines.


4.3                   Storage
                                   Store the device under the following conditions:
                                   ■    Recommendation: Use the original packaging.
                                   ■    Do not store outdoors.
                                   ■    Store in a dry, dust-protected place.
                                   ■    To allow any residual dampness to evaporate, do not package in airtight contain‐
                                        ers.
                                   ■    Do not expose to aggressive substances.
                                   ■    Protect from sunlight.
                                   ■    Avoid mechanical shocks.
                                   ■    Storage temperature: see "Technical data", page 84.
                                   ■    Relative humidity: see "Technical data", page 84.
                                   ■    For storage periods longer than 3 months, regularly check the general condition of
                                        all components and the packaging.




8027832./2022-06-10 | SICK                                          O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   17
Subject to change without notice

5 MOUNTING


5             Mounting
5.1           Prerequisites
                                     The following requirements must be met when mounting the SIG350:
                                      •       Level mounting surface free of mechanical stress.
                                      •       Provide suitable earthing.
                                      •       Select suitable mounting location with regard to vibration and impact load, temper‐
                                              ature and humidity see "General technical data", page 84.
                                      •       Protected to prevent the connecting cables from being torn off by personnel or the
                                              device.
                                      •       For proper installation and improved heat dissipation, keeping a minimum dis‐
                                              tance of 3 mm between two modules is recommended.
                                      •       When using angled plug connectors, a minimum distance of 50 mm must be
                                              maintained between two modules.
                                      •       Mount modules in such a way that they cannot be used as climbing aids.

                                     NOTE
                                     To ensure IP 67 protection, all unused connections must be covered with sealing
                                     caps. These are not included in the scope of delivery and must be ordered separately.
                                     Suitable sealing caps can be found at SICK.com (part number 5309189). In addition,
                                     connected cables and sealing caps must be fastened with the appropriate torque (see
                                     manufacturer’s specifications).


5.2           Module mounting
                                     The SIG350 is mounted using two screws (max. M6) and two washers.
                                     The fixing screws and tightening torques depend on the substrate of the mounting
                                     location. Always tighten the screws carefully and observe the maximum permissible
                                     tightening torque of 3 Nm.




18    O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                         8027832./2022-06-10 | SICK
                                                                                                             Subject to change without notice

MOUNTING 5




                                   Figure 3: Mounting the module

                                   Mounting
                                   •    Position M6 screw in the upper mounting opening and tighten lightly.
                                   •    Align housing
                                   •    Position another M6 screw in the lower mounting opening and tighten lightly.
                                   •    Tighten both screws with a max. tightening torque of 3 Nm.
                                   •    Ground module: see "Mounting of functional earth", page 19.

5.3                   Mounting of functional earth
                                   The module must be grounded to a metal base via a ground strap. To ensure functional
                                   earth, the module must be mounted with conductive screws. The fixing screws and
                                   tightening torques depend on the substrate of the mounting location. Always tighten the
                                   screws carefully and observe the maximum permissible tightening torque of 1.2 Nm.

                                   NOTE
                                   The ground strap and the associated screws for the functional earth are not included
                                   with delivery. This set is available as an accessory (part number 5346121).




8027832./2022-06-10 | SICK                                          O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   19
Subject to change without notice

5 MOUNTING

                                     Mounting




                                     Figure 4: Mounting the ground strap


                                      •       Place the ground strap in the opening provided in the housing for functional earth.
                                      •       Position washer on ground strap and fasten to module with M4 screw.
                                      •       Observe the tightening torque of 1.2 Nm.
                                      •       Align ground strap
                                      •       Tighten the lower end of the ground strap with another M4 screw and two washers
                                              at the mounting location, observing the tightening torque.

5.4           Rotary switch cover
                                     The rotary switches are provided with a cover to ensure IP protection. To operate the
                                     rotary switches, the cover must be removed. The cover must then be refitted.

                                     The rotary switch cover is fastened with two M3 screws. The permitted tightening torque
                                     is 0.8 Nm.




20    O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                         8027832./2022-06-10 | SICK
                                                                                                             Subject to change without notice

MOUNTING 5




                                   Figure 5: Mounting of rotary switch cover



5.5                   Scope of delivery
                                   Included in the scope of delivery of the SIG350:

                                   •    SIG350 IO-Link Master module
                                   •    Quickstart instructions
                                   •    20 marking labels

                                   NOTE
                                   No screws are included in the scope of delivery.




8027832./2022-06-10 | SICK                                              O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   21
Subject to change without notice

6 ELECTRICAL INSTALLATION


6             Electrical installation
6.1           Electrical installation
                                     The SIG350 is used in electrical installations. When working on the module or the plant,
                                     the safety rules of electrical engineering must be observed.
                                     The following information must be observed, depending on the connection type:
                                      •       Switch off the power supply to the device before starting work on it.
                                      •       The connection of the network and IO-Link cable of the SIG350 must be voltage-
                                              free (UB = 0 V). Only apply voltage/switch on the voltage supply (UB > 0 V) once all
                                              electrical connections have been established.
                                      •       All unused male and female connectors must be sealed with sealing caps to
                                              ensure enclosure rating IP 67.
                                      •       If possible, each of the sensor/bus and actuator power supplies should be drawn
                                              from different sources. The total current of the module must not exceed 16 A.
                                      •       In case of separate actuator and sensor supply, always switch on the sensor
                                              voltage first and then the actuator voltage to ensure error-free function of the
                                              digital inputs and outputs.
                                      •       An incorrect supply voltage may result in damage to the device.
                                      •       Cables and/or modules damaged by short-circuits can overheat and cause fires.
                                              Provide sensible current monitoring or fuse. The fuse protection must be designed
                                              for max. 16 A.
                                      •       During operation of the module, the device surface may heat up. If necessary,
                                              wear suitable thermal gloves.
                                      •       Only install cables and accessories that comply with the requirements and regu‐
                                              lations for safety, electromagnetic compatibility and, if applicable, telecommunica‐
                                              tions terminal equipment and the specification requirements.
                                      •       Observe the derating when using the product. The ambient temperature and the
                                              current have an influence on the heating of the product (see "Derating", page 25)

                                     NOTE
                                     Only operate the product with DC 24 V PELV (Protective Extra-Low Voltage) or SELV
                                     (Safety Extra-Low Voltage) voltage sources.
                                     There is a risk of electric shock if this is not observed.
                                     Only use a power supply unit that allows max. 60 V DC or 25 V AC in the event of a
                                     fault.


6.2           Pin assignment

                                     NOTE
                                     You will find a large selection of connection cables at www.sick.com

                                     Explanation of the connection diagrams
                                     • DI = Digital input
                                     • DO = Digital output
                                     • FE = Functional earth
                                     • n. c. = Not connected
                                     • Rx+ = Receiver +
                                     • Rx- = Receiver -
                                     • Tx+ = Sender +
                                     • Tx- = Sender –
                                     • US = Sensor voltage
                                     • UA = Actuator voltage

22    O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                          8027832./2022-06-10 | SICK
                                                                                                              Subject to change without notice

ELECTRICAL INSTALLATION 6


                                   IO-Link ports
                                   Tightening torque = 0.6 Nm
                                   The length of cable of the sensor and actuator lines is generally limited to 30 m.
                                   If an IO-Link connection is active, the length of cable is limited to max. 20 m.
                                   Table 6: IO-Link ports (S1 – S8): M12 female contact, A-coded, port class A/B
                                    PIN        IO-Link port class A                               IO-Link port class B11)
                                    Pin 1      L + (Us+)                                          L + (Us+)
                                    Pin 2      DI/DO                                              2L + (UA+)
                                    Pin 3      L - (Us-)                                          L - (Us-)
                                    Pin 4      IO-Link/DI/DO                                      IO-Link/DI/DO
                                    Pin 5      L - (Us-)                                          L - (Us-)
                                                                          1                           2

                                                                          5

                                                                          4                           3

                                   1)   No galvanic separation

                                   Ethernet ports
                                   Tightening torque = 0.6 Nm
                                   Table 7: Ethernet ports (P1 – P2): M12 female contact, D-coded
                                    PIN        Description
                                    Pin 1      Tx +
                                    Pin 2      Rx +
                                    Pin 3      Tx -
                                    Pin 4      Rx -
                                    Pin 5      n. c.
                                                                          1                           2

                                                                          5

                                                                          4                           3


                                   Supply ports
                                   US: 18 ... 30 V DC
                                   UA: 18 … 30 V DC
                                   Tightening torque = 0.6 Nm
                                   Table 8: Power ports (PWR1 – PWR2): M12 male connector/female contact, L-coded
                                    PIN        Description
                                    Pin 1      +24 V DC US
                                    Pin 2      0V
                                    Pin 3      0V
                                    Pin 4      +24 V DC UA
                                    Pin 5      GND




8027832./2022-06-10 | SICK                                             O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   23
Subject to change without notice

6 ELECTRICAL INSTALLATION

                                      PIN            Description
                                                                                        1                    5

                                                                                        2                    4


                                                                                                  3

                                                                                            Figure 6: PWR1

                                                                                        5                    1


                                                                                        4                    2


                                                                                                  3

                                                                                            Figure 7: PWR2


6.3           Supply concept

                                     CAUTION
                                     Product damage when the permissible leakage current is exceeded.
                                     Product damage and/or damage to other connected products if the maximum permissi‐
                                     ble leakage current is exceeded.
                                     In addition, observe the derating, i.e. the maximum current depending on the ambient
                                     temperature.

                                     Voltage supply
                                     The 24 V voltage supply is fed in via port PWR1. The maximum current carrying capacity
                                     of the module is 16 A. The module has two supply lines, which are not galvanically
                                     isolated:
                                      •       Supply line 1 (US) connects 1L+ (pin 1) to L- (pin 3).
                                      •       Supply line 2 (UA) connects 2L+ (pin 4) to L- (pin 2).
                                     Subsequent modules can be supplied with power via the PWR2 port. This leakage
                                     current must be taken into account when designing the supply. The total leakage
                                     current is limited to 16 A.

                                     Sensor supply
                                     The devices connected to the module are supplied via IO-Link ports S1 – S8. When
                                     designing the supply, the requirements of the connected sensors and actuators must
                                     be taken into account. The maximum current for the supply of all connected devices is
                                     limited to 10 A.
                                     The maximum current per port is <= 4 A. The upper limit for the current on the
                                     individual pins of IO-Link ports S1-S8 is:
                                     Table 9: Current carrying capacity of the pins on IO-Link ports S1 – S8
                                      PIN                                               Current carrying capacity
                                      1 (US)                                            <=2 A
                                      2 (UA)                                            <=2 A
                                      4 (UA)                                            <=2 A




24    O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                                8027832./2022-06-10 | SICK
                                                                                                                    Subject to change without notice

ELECTRICAL INSTALLATION 6


6.4                   Derating
                                   Observe the derating when using the SIG350. The ambient temperature and the current
                                   have an influence on the heating of the module.
                                   The product provides temperature and current readings that you can display via the
                                   web interface or read out via Dual Talk interfaces.
                                   The following figure shows the maximum permissible current (I) that may be drawn by
                                   the device, depending on the ambient temperature (T):
                                   I [A]

                                   16
                                   14
                                   12
                                   10
                                    8
                                    6
                                    4
                                    2
                                    0
                                    -30 -20 -10    0   10 20 30 40 50 60 70                  T [°C]

                                   Figure 8: Derating sensor current US/actuator current UA

                                   I [A]
                                   16
                                   14
                                   12
                                   10
                                    8
                                    6
                                    4
                                    2
                                    0
                                    -30 -20 -10    0   10 20 30 40 50 60 70                  T [°C]

                                   Figure 9: Derating total current IO-Link ports (total current S1 – S8)

                                   I [A]

                                   2.5
                                     2
                                   1.5
                                     1
                                   0.5
                                     0
                                     -30 -20 -10   0   10 20 30 40 50 60 70                  T [°C]

                                   Figure 10: Derating current per sensor supply and output (per pin 1, 2, and 4 at IO-Link port S1 –
                                   S8)




8027832./2022-06-10 | SICK                                               O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   25
Subject to change without notice

7 COMMISSIONING


7             Commissioning
                                     When the supply voltage is switched on for the first time, the SIG350 starts with the
                                     factory settings.
                                     To enable parameterization, the module must be configured to suit the network environ‐
                                     ment. For this purpose, various preparatory measures must be taken before parameter‐
                                     ization can be started.


7.1           IP address
                                     The module requires an IP address so that it can be addressed via the Ethernet
                                     network.

                                     NOTE
                                     When delivered, the SIG350 has the default IP address:
                                     192.168.0.1
                                     and the subnet mask
                                     255.255.255.0
                                     The name when delivered is sig350.

                                     The SIG350 supports the following methods for IP address assignment:
                                     1    DCP
                                     2    DHCP
                                     3    Static

                                     DCP
                                     The SIG350 supports IP address assignment via Discovery and the basic configuration
                                     protocol (DCP).
                                     The controller can assign an available IP address to the SIG350 during start-up. The
                                     controller and the module must be in the same subnet for this.
                                     The device IP address is assigned on the basis of the device name, which for this
                                     reason must be unique. The name in the delivery state is sig350.
                                     The default IP address of the SIG350 is 192.168.0.1 and the subnet mask is
                                     255.255.255.0.

                                     DHCP
                                     The SIG350 IO-Link Master supports the Dynamic Host Configuration Protocol for
                                     assigning IP addresses.
                                     DHCP is deactivated by default. To activate DHCP, open the web browser and change
                                     the address mode from static to DHCP.
                                     As soon as DHCP is activated, the IO-Link Master attempts to obtain an address from
                                     a DHCP server. When a new IP address is assigned by a DHCP server, the module
                                     immediately switches to the new IP address.
                                     Alternatively, DHCP can also be activated via the rotary switches.

                                     Static
                                     The module has rotary switches with which the last octet of the IP address can be
                                     adjusted manually. In the Ethernet configuration area of the web interface, the default
                                     IP address can also be changed statically.

7.2           MAC address
                                     Each device has a uniquely assigned MAC address that cannot be changed by the user.
                                     The assigned MAC address is printed on the module.

26    O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                      8027832./2022-06-10 | SICK
                                                                                                          Subject to change without notice

COMMISSIONING 7



7.3                   Rotary switch
                                   The SIG350 has three rotary switches on the lower side of the SIG350 with which
                                   various settings can be made manually. These include setting the last octet of the IP
                                   address, but also performing a factory reset.
                                   In the delivery state, the rotary switches are set to: 000.
                                             "                     "                      " 
                                         (                     (                        (

                                   & '             !     & '                 !    & '                !
                                         $ %   #               $ %       #              $ %      #

                                         x100                      x10                      x1

                                   Figure 11: Rotary switch position in delivery state


                                   To change settings in the module using the rotary switches, proceed as follows:
                                   1         Set the rotary switch to the desired position.
                                   2         Disconnect the module from the voltage supply.
                                   3         Supply the module with voltage again.
                                   4         Wait at least 10 seconds until the settings are loaded.
                                   The new settings are then accepted and saved in the module.

                                   Exception:
                                   The procedure is different for rotary switch setting 979 (factory settings):
                                   1         Disconnect the module from the voltage supply.
                                   2         Set the rotary switch to position 979.
                                   3         Supply module with voltage.
                                   4         Wait at least 2 minutes until the settings are loaded.
                                   5         Disconnect the module from the voltage supply again.
                                   6         Set the rotary switch to position 000 or another desired position.
                                   7         Reconnect the module to the voltage supply.

                                   NOTE
                                   The previously saved settings for fieldbus protocols are not affected by this position.
                                   Communication is then started if the switches are left in this position.
                                   However, setting the positions to the previous state is recommended.

                                   Table 10: Meaning of rotary switch settings
                                   X100            X10             X1            Description
                                   0               0               0             Delivery state
                                                                                 The standard network configuration is used:
                                                                                 - IP address = 192.168.0.1
                                                                                 - Subnet mask = 255.255.255.0
                                                                                 - IP gateway = 0.0.0.0
                                                                                 When the IP address is changed, the last saved address is used.
                                   0               0               1             Manual IP address
                                   …               …               …             With switch settings 0-0-1 ... 2-5-4, a fixed IP address can be set
                                                                                 manually:
                                   2               5               4             The last octet of the preset IP address is set here (default:
                                                                                 192.168.0.xxx).




8027832./2022-06-10 | SICK                                                                  O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   27
Subject to change without notice

7 COMMISSIONING

                                      X100           X10            X1              Description
                                      8              8              8               IP address reset
                                                                                    A standard IP address is used. If the IP address was changed with
                                                                                    other methods (e.g. web interface), the IP address will be reset to
                                                                                    default IP address 192.168.0.1 when the master reboots.
                                      9              1              1               Safe mode
                                                                                    This mode is used to deactivate the Dual Talk services.
                                                                                    The safe mode deactivates:
                                                                                    - Web interface
                                                                                    - OPC UA
                                                                                    - MQTT
                                                                                    - REST API
                                                                                    The previously saved settings for fieldbus protocols are not
                                                                                    affected by this position, so communication will start even if you
                                                                                    leave the switches in this position. However, setting the positions
                                                                                    to the previous state is recommended.
                                      9              1              3               Deactivation of WebUI and REST API
                                      9              7              9               Factory reset
                                                                                    The device performs a factory reset. This also resets the network
                                                                                    parameters to the default values. No communication is possible in
                                                                                    this operating mode.
                                                                                    The IP address is set to 0.0.0.0.


7.4           PROFINET parameters
                                     The SIG350 has the following PROFINET parameters when delivered or after a factory
                                     reset:
                                     Table 11: PROFINET parameters
                                      PROFINET name                                 No name assigned
                                      IP address                                    When delivered: 192.168.0.1
                                                                                    Factory reset: 0.0.0.0
                                      Subnet mask                                   255.255.255.0
                                      Vendor ID                                     0x0101
                                      Device ID                                     0x1102


7.5           Data security
                                     Proper project and other planning is an important prerequisite for ensuring the confi‐
                                     dentiality, availability and integrity of data.
                                     products are intended for use in local networks. Observe the following notes when
                                     using products in your plant:
                                      •       Do not connect control components and control networks to an open network
                                              such as the Internet or an office network.
                                      •       Protect the control components and control networks with the use of a firewall.
                                      •       Close all services not required by your application (see "Rotary switch", page 27) to
                                              reduce the risk of cyber attacks and thus increase cyber security.
                                      •       Restrict physical and electronic access to all automation components to an
                                              authorized group of persons.
                                      •       To reduce the risk of unauthorized persons gaining access to your system, be sure
                                              to change the default passwords and IP addresses before initial commissioning.




28    O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                                               8027832./2022-06-10 | SICK
                                                                                                                                   Subject to change without notice

OPERATION 8


8                     Operation
8.1                   Profinet integration
                                         The SIG350 can exchange process data and parameters via PROFINET. For this pur‐
                                         pose, the IO-Link Master must be connected to a suitable programmable logic control‐
                                         ler (PLC).

8.1.1                 Project planning in TIA Portal
                                         These instructions describe an example integration of the SIG350 into a PROFINET
                                         network.
                                         The system integration and parameterization described in the following shows a good
                                         example of how the SIG350 is used together with the TIA Portal V15 project planning
                                         software from Siemens. If you use other controllers and project planning software,
                                         observe the corresponding documentation.
                                         SICK does not assume any liability for the correctness and completeness of the con‐
                                         tents.

8.1.1.1               Adding SIG350 to the project

8.1.1.1.1                          Reading in GSDML file
                                         The device data required for project planning is stored in GSDML (“Generic Station
                                         Description Markup Language”) files. The GSDML file makes the possible data module
                                         available with input or output of different data widths.
                                         Download the corresponding GSDML file under www.sick.com/SIG350 and save the
                                         GSDML file at a place where you have access with the control software.
                                         Start the control software and read the GSDML file via the “Manage device description
                                         files” item into the hardware catalog of the control program.




8027832./2022-06-10 | SICK                                               O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   29
Subject to change without notice

8 OPERATION




                                       Figure 12: Hardware catalog


                                       The SIG350 is located in the TIA Portal in the folder structure of the hardware catalog at
                                       Other field devices > PROFINET IO > Gateway > SICK AG > SIG > SIG350

8.1.1.1.2                  Setting up network connection
                                       To include the SIG350 in the project, select the corresponding SIG350 entry in the
                                       hardware catalog and drag and drop it to a free position in the “Devices & networks”
                                       topology view.




30      O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                      8027832./2022-06-10 | SICK
                                                                                                            Subject to change without notice

OPERATION 8




                                   Figure 13: Network view


                                   Once the SIG350 is inserted in the network view, the network of the module must be
                                   assigned. To do so, click on “Unassigned” at the module symbol with the left mouse
                                   button and select the corresponding IO controller.
                                   A green visualized connection between the controller and SIG350 should then be
                                   displayed.




                                   Figure 14: IO controller assignment manual - 1




                                   Figure 15: IO controller assignment manual - 2

                                   Alternatively, the connection can also be established by clicking on the light green
                                   square in the network view, which symbolizes the interface. Hold and drag to the
                                   desired interface (green square) on your IO controller. The visualized green connection
                                   is created when you release the mouse button.




8027832./2022-06-10 | SICK                                             O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   31
Subject to change without notice

8 OPERATION




                                       Figure 16: IO controller assignment via drag & drop


                                       Select the module with a double click to continue configuration.




                                       Figure 17: Further configuration


8.1.1.1.3                  Configuring and assigning device name and IP address
                                       PROFINET devices are addressed via a unique device name. This can be freely assigned
                                       by the user, but may only be used once in the network.
                                       Configuring device name and IP address
                                       To configure the device name, the PROFINET address and the IP address, click on the
                                       SIG350 icon in the network view and a menu opens. In this menu, under the General
                                       rider, go to PROFINET interface. You can make the desired configurations there

                                        •       A click on the device symbol or on the first line of the device overview opens
                                                the settings for PROFINET interface > Ethernet addresses. Device name and PRO‐
                                                FINET address (IP) can be configured here:




                                       Figure 18: Ethernet addresses



32      O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                      8027832./2022-06-10 | SICK
                                                                                                            Subject to change without notice

OPERATION 8


                                   •    Check whether the controller and the module are in the same Ethernet subnet.

                                   •    Accept the default settings for IP address and device name or change them if
                                        desired.

                                   •    Transfer the configuration to your controller.

                                   •    For a setup to work correctly, the selected device name must be programmed
                                        online into the module. Right-click on the selected module. Then click on Assign
                                        device name.




                                   Figure 19: Assigning device name


                                   The new IO device should already be accessible via PROFINET:




                                   Figure 20: Go online




8027832./2022-06-10 | SICK                                            O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   33
Subject to change without notice

8 OPERATION




                                    Figure 21: Online mode


                                     •       Enter the same device name that was configured in the offline project.




                                    Figure 22: Assigning device name


                                    Assigning device names
                                    After the device name has been configured, it must be assigned to the module. To do
                                    this, select the SIG350 in the device view and click on the right mouse button to select
                                    the “Assign name” command.
                                    The device name must correspond to the names previously configured under “Proper‐
                                    ties”.
                                    The identification is done via the MAC address or via the LED flash test. The MAC
                                    address is indicated on the label on the side of the SIG350.




34   O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                        8027832./2022-06-10 | SICK
                                                                                                           Subject to change without notice

OPERATION 8




                                         Figure 23: Assigning device name


8.1.1.2               Configuring SIG350

8.1.1.2.1                          Fast start-up (FSU)
                                         The SIG350 also has the “Prioritized start-up” function.
                                         If the prioritized start-up, also called “Fast start-up” (FSU), is activated, the modules
                                         start up within < 2 s.
                                         To activate the function, several settings must be made in the hardware configuration.
                                         The corresponding parameters are set directly in the module.

                                          •   Select module (PN-IO) in the topology overview
                                          •   Under PROFINET interface > Advanced options > Interface options, activate a
                                              check mark at Prioritized start-up.




8027832./2022-06-10 | SICK                                                  O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   35
Subject to change without notice

8 OPERATION




                                       Figure 24: Activating prioritized start-up


                                       During conventional connection setup, connection parameters are negotiated between
                                       the individual PNIO devices, which results in a time delay.
                                       To prevent this delay and to ensure optimal start-up in < 2 s, the connection parame‐
                                       ters for each port (participating in the FSU) must be permanently parameterized.
                                        •       The transmission speed on all connected ports must be permanently set to
                                                100 Mbit.
                                                This eliminates time-consuming negotiation of the connection parameters during
                                                module start-up.
                                        •       Auto-negotiation must not be activated.
                                                This eliminates time-consuming negotiation of the connection wire pairs during
                                                module start-up.
                                        •       Observe port direction: Port 1 IN Port 2 OUT
                                        •       Unassigned PNIO ports (e.g. last module in the line topology) do not have to be
                                                changed over.

                                       This completes the necessary settings for using FSU.

8.1.1.2.2                  Media Redundancy Protocol (MRP) configuration
                                       The SIG350 supports the ring topology with media redundancy, which is enabled by
                                       means of the Media Redundancy Protocol (MRP).

                                       Setting up MRP manager
                                       For a ring configuration, 2 ports, a managed switch or a CPU must be set as MRP
                                       manager. The remaining participants must be set up as clients.
                                       Select the according managed switch and navigate to PROFINET Interface > Advanced
                                       options > Media redundancy. Set Manager (Auto) role in the media redundancy set‐
                                       tings. In addition, check the Diagnostics interruption box.




36      O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                       8027832./2022-06-10 | SICK
                                                                                                             Subject to change without notice

OPERATION 8




                                   Figure 25: Setting up MRP manager

                                   Setting up MRP client
                                   Select the SIG350 and navigate to PROFINET Interface > Advanced options > Media
                                   redundancy. For the SIG350, the media redundancy role must be set to “Client”. “Not
                                   participant” is set by default. In addition, the diagnostic alarm must be activated.
                                   The SIG350 must be in the same MRP domain as the MRP master.




                                   Figure 26: Setting up MRP client

                                   With the ring topology, it is possible to build up a redundant system. That means in
                                   normal operation, one side of the ring line is deactivated by the MRP master. If the line
                                   is damaged/cut at a point in the ring, the deactivated branch is reactivated and two
                                   linear topologies are created.
                                   MRP cycle times
                                   To ensure uninterrupted operation, the response monitoring time should be < 200 ms.
                                   This is because the MRP master needs a certain time to activate the second string. If
                                   the response monitoring time is smaller than the switchover time of the MRP master,
                                   this leads to a communication abort.
                                   This response monitoring time is calculated from the “Update time” and the “Accepted
                                   update time without IO data” factor:




8027832./2022-06-10 | SICK                                             O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   37
Subject to change without notice

8 OPERATION




                                       Figure 27: Setting up MRP cycle times

                                       MRP domain
                                       Call up the overview of ring participants via Domain Management | MRP Domains |
                                       mrpdomain-1.
                                       Assign the PROFINET Managed Switch to the IO controller and save the created project.
                                       Click on the PNIE subnet. The bus PLC_1.PROFINET IO system (100) is displayed.
                                       Assign the SIG350 module to the IO controller.

                                       All participants of the ring configuration are displayed under Devices.




                                       Figure 28: Setting up MRP domain


8.1.1.2.3                  Isochronous real time (IRT) configuration
                                       For this communication type, special hardware components that are real-time capable
                                       (IRT), such as a controller, are required.
                                       The module is not an active participant in the IRT data exchange. It supports loss-free
                                       forwarding of IRT telegrams for synchronized fieldbus devices in the same Ethernet
                                       subnet.

                                       NOTE
                                       To use the IRT configuration, media redundancy must not be activated.




38      O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                       8027832./2022-06-10 | SICK
                                                                                                             Subject to change without notice

OPERATION 8


                                   Open the IRT-capable controller with a double click and under Advanced options >
                                   Real-time setting > Synchronization, select Sync Master for the synchronization role




                                   Figure 29: IRT communication: Setting up Sync Master




                                   Figure 30: IRT communication: Setting up Sync Slave


                                   Then set up the SIG350 as a Sync Slave. To do this, select the module and activate it
                                   under PROFINET interface > Advanced options > Real-time settings > Synchronization
                                   for RT class IRT.

8.1.1.3               Configuration submodule
                                   The device model represents process data and acyclic data in the following slots:




8027832./2022-06-10 | SICK                                            O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   39
Subject to change without notice

8 OPERATION

                                       Table 12: Process data and acyclic data slots
                                        Slot           Subslot                Designation               Function
                                        0                                     SIG350-0004AP1 Device access point (DAP): Main module
                                                                              00
                                                       X1                     PN-IO                     PROFINET functions
                                                       X1 P1                  Port 1 – M12              Ethernet port functions
                                                       X1 P2                  Port 2 – M12
                                        1              1                      IO-Link Master            IO-Link Master functions for all ports (e.g. State of
                                                                                                        pin 2/pin 4).
                                                       Port S1 …              Various                   Display of the IO-Link device data for parameteriza‐
                                                       Port S8                                          tion of the IO-Link device.


8.1.1.3.1                  Slot 1/ 1: IO-Link Master
                                       Access to the digital signals at the inputs of the individual ports is done via this
                                       submodule. The process data structure can be configured via the “PD Layout” module
                                       parameter.

                                       Table 13: Process data format (port-based format)
                                        Byte             Bit 7            Bit 6           Bit 5        Bit 4       Bit 3        Bit 2      Bit 1          Bit 0
                                        0                    S4DI2            S4DI4           S3DI2       S3DI4       S2DI2        S2DI4       S1DI2 S1DI4
                                        1                S8DI2            S8DI4           S8DI2        S8DI4       S8DI2        S8DI4      S8DI2          S8DI4

                                       Table 14: Process data format (pin-based format)
                                        Byte             Bit 7            Bit 6           Bit 5        Bit 4       Bit 3        Bit 2      Bit 1          Bit 0
                                        0                    S8DI2            S7DI4           S6DI4       S5DI4       S4DI4        S3DI4       S2DI4 S1DI4
                                        1                S8DI2            S7DI2           S6DI2        S5DI2       S4DI2        S3DI2      S2DI2          S1DI2

                                       Table 15: Process data meaning
                                        Designation                           Value           Meaning
                                        SxDI2 / SxDI4                                     0                     Pin 2 / Pin 4 of port x is Low (or deactivated)
                                                                              1               Pin 2 / Pin 4 of port x is High


8.1.1.3.1.1                            Module parameters
                                       The properties of the I/Q pin (pin 2 / pin 4) can be configured via the module parame‐
                                       ters of the corresponding port.
                                       Table 16: Digital configuration
                                        Parameter name                                Information
                                        Digital IO layout configura‐                  0: Port-based format
                                        tion                                          1: Pin-based format
                                        Digital Output substitute                     0: Sets the state of the digital output to Low
                                        configuration                                 2: Sets the state of the digital output to the last value


8.1.1.3.2                  Slot 1/ Port S1 … S8: IO-Link, Digital Input, Digital Output
                                       The SIG350 has 8 sensor/actuator ports that can be assigned to specific IO-Link devi‐
                                       ces. For each IO-Link port (S1 - S8), it must be defined which device type is connected
                                       to the port: Digital input, digital output or an IO-Link device.
                                       Double-clicking on the module opens the device view with the corresponding configura‐
                                       tions.



40      O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                                                     8027832./2022-06-10 | SICK
                                                                                                                                           Subject to change without notice

OPERATION 8




                                   Figure 31: Standard configuration of the IO-Link ports in the delivery state.

                                   The available submodules of the SIG350 are displayed in the hardware catalog on
                                   the right-hand side. Different submodules are available for the different process data
                                   lengths.




8027832./2022-06-10 | SICK                                               O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   41
Subject to change without notice

8 OPERATION




                                       Figure 32: Hardware catalog of available submodules


8.1.1.3.2.1                            Generic IO-Link device
                                       The IO-Link specification defines three types of data that are exchanged between the
                                       IO-Link Master and IO-Link device:
                                        •       Cyclic process data (access via corresponding submodule address).
                                        •       Acyclic data in the form of device data, ISDUs (see section XXX - IOL-call).
                                        •       Acyclic data as events (see “PortStatus” table or Profinet diagnostics).
                                       The process data and its status information (port qualifiers) are transmitted cyclically
                                       after communication has been established. For each IO-Link port, the transmission
                                       time can be parameterized individually as the IO-Link cycle time.
                                       The SIG350 uses incoming process data (Process Data In; data from the IO-Link Master
                                       to the PLC) and outgoing process data (Process DataOut; data from the PLC to the
                                       IO-Link Master).
                                       The process data of the connected device can be 0 to 32 bytes in size (input and
                                       output) and are transmitted via the set address ranges.


42      O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                            8027832./2022-06-10 | SICK
                                                                                                                  Subject to change without notice

OPERATION 8


                                   Port S1...S8 must be configured according to the process data length of the connected
                                   device. The information on the required process data lengths can be found in the doc‐
                                   umentation of the connected IO-Link device. Contact the manufacturer of the IO-Link
                                   device to do so.
                                   IO-Link xI/yO + PQI: The process data length consists of x bytes incoming and y bytes
                                   outgoing. In addition, a byte with Port Qualifier Information (PQI) is transmitted, which
                                   provides the following status information:
                                   Table 17: PQI description
                                   Bit                             Description
                                   Bit 7                           Validity of the device process data (PQ)
                                                                   0 = Invalid IO process data from device
                                                                   1 = Valid IO process data from device
                                   Bit 6                           Display of a port/device error (DevErr)
                                                                   0 = No error/no warning
                                                                   1 = Error/warning for device or port
                                   Bit 5                           Device communication (DevCom)
                                                                   0 = No device available
                                                                   1 = Device detected and in PREOPERATE or OPERATE state
                                   Bit 4                           Port activation (PortActive)
                                                                   0 = Port deactivated via port function
                                                                   1 = Port activated
                                   Bit 3                           Substitute device detection (SubstDev)
                                                                   0 = No substitute device detected (identical serial number)
                                                                   1 = Substitute device detected (different serial number)
                                   Bit 2                           New parameter (NewPar)
                                                                   0 = No change of the device parameter detected
                                                                   1 = Change of device parameter detected: Master has per‐
                                                                   formed a data memory upload and a new IOLD backup object
                                                                   (0xB904) is available
                                   Bit 1                           Reserved always “0”
                                   Bit 0                           Reserved always “0”

                                   If no suitable configuration module is available for the device, the next largest data
                                   length must be selected.
                                   Example
                                   For an IO-Link device that supplies 8 bytes of input and 2 bytes of output process data,
                                   the IO-Link 8I / 8O + PQI submodule should be selected, since no submodule exists
                                   with this combination.

                                   Click on a suitable submodule that corresponds to the process data length of the
                                   connected device to select it. The submodule can be dragged into the corresponding
                                   free port-related IO-Link subslot using the drag and drop function of the left mouse
                                   button.

                                   NOTE
                                   When using the IO-Link device in SIO mode, use a digital input or digital output module
                                   at the corresponding subslot.



8.1.1.3.2.1.1                      Module parameters
                                   The properties of the I/Q pin (pin 2) can be configured via the module parameters of
                                   the corresponding port.


8027832./2022-06-10 | SICK                                           O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   43
Subject to change without notice

8 OPERATION

                                    Digital configuration
                                    Table 18: Digital configuration
                                     Parameter name                        Information
                                     Digital Input Logic I/Q               0: Digital Input not inverted (NO normally open)
                                     Pin                                   1: Digital Input inverted (NC normally closed)
                                     Digital Input Filter                  0: no Filter               Level changes below the filter time are ignored.
                                     Time I/Q Pin                          30: 3 ms Filter Time
                                                                           150: 15 ms Filter
                                                                           Time
                                                                           200: 20 ms Filter
                                                                           Time
                                     Digital Output Static                 0: Disable                 Power AUX allows the support of Class B devi‐
                                     On I/Q Pin                            1: Enable                  ces with additional voltage supply (UA), but
                                                                                                      without galvanic separation.

                                    NOTE
                                    Access to the state of the I/Q pins is via Slot1/1: IO-Link Master.
                                    After the first configuration of the device, this port configuration is stored on the IO-Link
                                    Master in a non-volatile manner. This means that the next time the port is switched
                                    on, it will be preconfigured with these settings before the controller sends a new port
                                    configuration.

                                    IO-Link Port parameter
                                    Table 19: IO-Link Port parameter
                                     Parameter name                           Information
                                     Enable Port diagnosis                    0: Disable          IO-Link device events of the type “Warning” and
                                                                              1: Enable           “Errors” are transferred to the Profinet diagnostics.
                                                                              (default)           This parameter can be used to deactivate this
                                                                                                  function.
                                     Enable Process Alarm                     0: Disable          Activation of IO-Link device events of the “Notifica‐
                                                                              1: Enable           tion” type as process alarm.
                                                                              (default)
                                     Configuration Source                     0: PDCT (Port    Parameterization with IO-Link tool: Two-stage com‐
                                                                              and Device Con‐ missioning is used at this IO-Link port. There is
                                                                              figuration Tool) no explicit port parameterization in the PLC via the
                                                                                               PROFINET engineering tool. Port parameterization
                                                                                               and device parameterization can be performed
                                                                                               using tools that support the standardized PDCT
                                                                                               interface (Port and Device Configuration Tool).
                                                                              1: PNIO             Parameterization is done in the PLC via the PROFI‐
                                                                                                  NET engineering tool.
                                     Enable Input fraction                    0: Disable          Activates monitoring of the process data length of
                                                                              1: Enable           the submodule against process data length of the
                                                                                                  connected device.
                                     Enable Pull/Plug                         0: Disable          Connection termination/Connection setup on the
                                                                                                  device is signaled via the Profinet diagnostics
                                                                              1: Enable           Connection termination/Connection setup on the
                                                                                                  device is signaled via the Profinet “Hardware com‐
                                                                                                  ponent removed” message




44   O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                                              8027832./2022-06-10 | SICK
                                                                                                                                 Subject to change without notice

OPERATION 8


                                   Parameter name            Information
                                   I/Q Behavior              0: deactivated    Configuration of pin 2 behavior.
                                                             1: Digital Input
                                                             2: Digital Output
                                                             5: Power AUX

                                                             NOTE
                                                             Power AUX allows the support of class B devices with additional
                                                             voltage supply (Ua), but without galvanic separation.

                                   Port Mode                 0: Deactivated        Deactivated port.
                                                             1: IOL_Manual         IO-Link port parameterization active: Single-stage
                                                                                   commissioning is used at this IO-Link port. The
                                                                                   explicit port parameterization for inspection level,
                                                                                   port cycle time, manufacturer ID and device ID is
                                                                                   done in the PLC via the PROFINET engineering tool.
                                                             2: IOL_Autostart Automatic IO-Link parameterization: No explicit
                                                                              port parameterization is used at this IO-Link port.
                                                                              Basic assignments such as inspection level, port
                                                                              cycle time, manufacturer ID, and device ID are
                                                                              not required. Corresponding parameters are deter‐
                                                                              mined by the connected IO-Link device.
                                                             3: DI_C/Q             Configuration of pin 4 as digital input
                                                             4: DO_C/Q             Configuration of pin 4 as digital output
                                   Validation/Backup (is     0: no Device check                         No device inspection: No inspection
                                   only considered in port                                              is performed on this IO-Link port
                                   mode IOL_Manual)                                                     regarding the correct device ID, man‐
                                                                                                        ufacturer ID or serial number.
                                                             1: type compatible device                  Type-compatible device (V1.0): An
                                                             (V1.0)                                     inspection is performed on the IO-
                                                                                                        Link port with regard to the correct
                                                                                                        IO-Link revision (V1.0), device ID and
                                                                                                        manufacturer ID.
                                                             2: type compatible device                  Type-compatible device (V1.1): On
                                                             (V1.1)                                     the IO-Link port, an
                                                                                                        inspection concerning the revision
                                                                                                        ID, device ID and
                                                                                                        manufacturer ID is done.
                                                             3: type compatible V1.1                    Type-compatible device (V1.1) with
                                                             device with Backup + Restore               backup + restore: An inspection is
                                                                                                        performed on the IO-Link port with
                                                                                                        regard
                                                                                                        to the revision ID, device ID and man‐
                                                                                                        ufacturer ID. Data storage (reading
                                                                                                        and writing) is permitted.
                                                             4: type compatible V1.1                    Type-compatible device (V1.1) with
                                                             device with Restore                        restore: On the IO-Link port, an
                                                                                                        inspection is performed with regard
                                                                                                        to the revision ID, device ID and man‐
                                                                                                        ufacturer ID. Data storage (writing) is
                                                                                                        allowed.




8027832./2022-06-10 | SICK                                            O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   45
Subject to change without notice

8 OPERATION

                                        Parameter name                           Information
                                        Port cycle time (is only 0: as fast as possible
                                        considered in port mode 16: 1.6 ms
                                        IOL_Manual)              32: 3.2 ms
                                                                 48: 4.8 ms
                                                                 68: 8.0 ms
                                                                 73: 10.0 ms
                                                                 78: 12.0 ms
                                                                 88: 16.0 ms
                                                                 98: 20.0 ms
                                                                 133: 40.0 ms
                                                                 158: 80.0 ms
                                                                 183: 120.0 ms
                                        Vendor ID (is only con‐                  Expected manufacturer ID of the IO-Link device connected to the
                                        sidered in port mode                     IO-Link port (unsigned integer 16)
                                        IOL_Manual)                              Example:
                                                                                 Manufacturer ID SICK AG = 26
                                        Device ID (is only con‐                  Expected device ID of the IO-Link device connected to the IO-Link
                                        sidered in port mode                     port (unsigned integer 32)
                                        IOL_Manual)                              Example:
                                                                                 SIG100 = 8389010


8.1.1.3.2.2                            Digital modules
                                       The selection of the corresponding module determines the behavior of pin C/Q (pin 4).
                                       Pin I/Q (pin 2) can still be configured both as an input and as an output.

                                       NOTE
                                       The level depends on the configured Digital Input Logic parameter, which can thus be
                                       inverted.

                                       Table 20: Process data submodules
                                        Submodule name                           Direc‐   Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0
                                                                                 tion
                                        Digital input                            On       0      0      0       0      0         0      0         0         SxDI
                                                                                                                                                            1
                                        Digital output                           Off      0      0      0       0      0         0      0         0         SxD
                                                                                                                                                            O1

                                       Table 21: Process data coding
                                        Designation                   Val Meaning
                                                                      ue
                                        SxDI1                         0       Pin 4 of port x is Low (SIO mode, digital input)
                                                                      1       Pin 4 of port x is High (SIO mode, digital input)
                                        SxDO1                         0       Pin 4 of port x is set to Low (SIO mode, digital output)
                                                                      1       Pin 4 of port x is set to High (SIO mode, digital output)


8.1.1.3.2.2.1                          Digital input
                                       The slot is addressed as a digital input. The connected device is set to SIO mode and
                                       no communication to the connected device is possible.
                                       Digital configuration




46      O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                                               8027832./2022-06-10 | SICK
                                                                                                                                     Subject to change without notice

OPERATION 8


                                   Table 22: Digital configuration
                                   Parameter name              Information
                                   Digital Input Logic I/Q     0: Digital Input not inverted (NO normally open)
                                   Pin                         1: Digital Input inverted (NC normally closed)
                                   Digital Input Filter        0: no Filter                              Level changes below the filter time are
                                   Time I/Q Pin                30: 3 ms Filter Time                      ignored.
                                                               150: 15 ms Filter Time
                                                               200: 20 ms Filter Time
                                   Digital Output Static       0: Disable
                                   On I/Q Pin                  1: Enable
                                   Digital Input Logic C/Q 0: Digital Input not inverted (NO normally open)
                                   Pin                     1: Digital Input inverted (NC normally closed)
                                   Digital Input Filter        0: no Filter                              Level changes below the filter time are
                                   Time C/Q Pin                30: 3 ms Filter Time                      ignored.
                                                               150: 15 ms Filter Time
                                                               200: 20 ms Filter Time

                                   Port Configuration
                                   Table 23: Port Configuration
                                   Parameter name Information
                                   Enable Port diag‐      0: Disable              IO-Link device events of the type “Warning” and “Errors”
                                   nosis                  1: Enable               are transferred to the Profinet diagnostics. This parame‐
                                                          (default)               ter can be used to deactivate this function.
                                   Configuration          0: PDCT (Port and Parameterization with IO-Link tool: Two-stage commis‐
                                   Source                 Device Configura‐ sioning is used at this IO-Link port. There is no explicit
                                                          tion Tool)        port parameterization in the PLC via the PROFINET engi‐
                                                                            neering tool. Port parameterization and device parame‐
                                                                            terization can be performed using tools that support the
                                                                            standardized PDCT interface (Port and Device Configura‐
                                                                            tion Tool).
                                                          1: PNIO                 Parameterization is done in the PLC via the PROFINET
                                                                                  engineering tool.
                                   I/Q Behavior           0: deactivated          Configuration of pin 2 behavior.
                                                          1: Digital Input
                                                          2: Digital Output
                                                          5: Power AUX

                                                          NOTE
                                                          Power AUX allows the support of class B devices with additional voltage
                                                          supply (Ua), but without galvanic separation.

                                   Port cycle time (is    0: as fast as possible
                                   only considered        16: 1.6 ms
                                   in port mode           32: 3.2 ms
                                   IOL_Manual)            48: 4.8 ms
                                                          68: 8.0 ms
                                                          73: 10.0 ms
                                                          78: 12.0 ms
                                                          88: 16.0 ms
                                                          98: 20.0 ms
                                                          133: 40.0 ms
                                                          158: 80.0 ms
                                                          183: 120.0 ms




8027832./2022-06-10 | SICK                                                    O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   47
Subject to change without notice

8 OPERATION

8.1.1.3.2.2.2                          Digital output
                                       The slot is addressed as a digital output. The connected device is set to SIO mode and
                                       no communication to the connected device is possible.
                                       Digital configuration
                                       Table 24: Digital configuration
                                        Parameter name Information
                                        Digital Input Logic 0: Digital Input not inverted (NO normally open)
                                        I/Q Pin             1: Digital Input inverted (NC normally closed)
                                        Digital Input Filter 0: no Filter                          Level changes below the filter time are ignored.
                                        Time I/Q Pin         30: 3 ms Filter Time
                                                             150: 15 ms Filter Time
                                                             200: 20 ms Filter Time
                                        Digital Output                0: Disable
                                        Static On I/Q Pin             1: Enable
                                        Digital Output    0: Disable
                                        Static On C/Q Pin 1: Enable

                                       Port Configuration
                                       Table 25: Port Configuration
                                        Parameter name Information
                                        Enable Port diag‐             0: Disable          IO-Link device events of the type “Warning” and “Errors”
                                        nosis                         1: Enable           are transferred to the Profinet diagnostics. This parame‐
                                                                      (default)           ter can be used to deactivate this function.
                                        Configuration                 0: PDCT (Port and Parameterization with IO-Link tool: Two-stage commis‐
                                        Source                        Device Configura‐ sioning is used at this IO-Link port. There is no explicit
                                                                      tion Tool)        port parameterization in the PLC via the PROFINET engi‐
                                                                                        neering tool. Port parameterization and device parame‐
                                                                                        terization can be performed using tools that support the
                                                                                        standardized PDCT interface (Port and Device Configura‐
                                                                                        tion Tool).
                                                                      1: PNIO             Parameterization is done in the PLC via the PROFINET
                                                                                          engineering tool.
                                        I/Q Behavior                  0: deactivated      Configuration of pin 2 behavior.
                                                                      1: Digital Input
                                                                      2: Digital Output
                                                                      5: Power AUX

                                                                      NOTE
                                                                      Power AUX allows the support of class B devices with additional voltage
                                                                      supply (Ua), but without galvanic separation.

                                        Port cycle time (is           0: as fast as possible
                                        only considered               16: 1.6 ms
                                        in port mode                  32: 3.2 ms
                                        IOL_Manual)                   48: 4.8 ms
                                                                      68: 8.0 ms
                                                                      73: 10.0 ms
                                                                      78: 12.0 ms
                                                                      88: 16.0 ms
                                                                      98: 20.0 ms
                                                                      133: 40.0 ms
                                                                      158: 80.0 ms
                                                                      183: 120.0 ms




48      O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                                        8027832./2022-06-10 | SICK
                                                                                                                              Subject to change without notice

OPERATION 8


8.1.1.4               Profinet diagnostics
                                         The SIG350 sends diagnostic information in the form of alarms according to PROFINET
                                         specification V2.3. Diagnostics are reported to the PLC in the form of “coming” and
                                         “going” alarms. If an alarm is only present for a short time, it is advantageous if a
                                         diagnostic buffer is available in the PLC. With this diagnostic buffer, the alarm details
                                         can be evaluated later. If the PLC does not provide a diagnostic buffer, it should be
                                         created as user software.

8.1.1.4.1                          Diagnostic messages to IO-Link ports

                                         NOTE
                                         Please consult the device documentation for manufacturer-specific IO-Link events.

                                         IO-Link events
                                          • Warning = Profinet diagnostic messages
                                          • Error = Profinet diagnostic messages
                                          • Notifications = Profinet process alarm

8.1.2                 Factory reset
                                         The Reset to factory settings function can be executed with the following steps:
                                         •    Click on Connect online in the TIA Portal.
                                         •    After the connection, select the relevant module.
                                         •    Open the SIG350 in the project navigation. Double click on Online & diagnostics
                                         •    In the Functions tab, click on Reset to factory settings. Another window opens here.
                                         •    If necessary, activate the Retain I&M data selection if it should not be deleted.
                                         •    Press the Reset button. The module is reset to the factory settings.

                                         After the factory reset, besides the PROFINET device name, the IP address and the
                                         SNMP parameters are reset. The following default values are then stored in the mod‐
                                         ule:

                                         Table 26: Standard values after factory reset
                                          Settings                                                       Value
                                          IP address                                                     0.0.0.0
                                          Subnet mask                                                    0.0.0.0
                                          Router address                                                 0.0.0.0
                                          PROFINET device name                                           Non-existent


8.1.3                 Function blocks

8.1.3.1               Siemens function blocks
                                         The controller manufacturers offer various generic function blocks for reading data from
                                         the IO-Link Master as easily as possible. The function block for IO-Link basic functions
                                         is called IOLCall.
                                         This function block can send ISDU read/write commands, but does not know any
                                         additional information about the exchanged data and the connected devices.
                                         IOL_Call
                                         IOL_CALL is an add-on to the PROFINET protocol that can be used to access IO-Link
                                         On-Request data (ISDU parameters). It is specified in the document “IO-Link Integration
                                         - Edition 2, Guideline for PROFINET” Version 1.0 - June 2017 (order no. 2.832) of the
                                         PROFIBUS user organization (PNO).


8027832./2022-06-10 | SICK                                                    O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   49
Subject to change without notice

8 OPERATION

                                    IOL_CALL can be located in a PLC as a function block (FB). The FB requires at least the
                                    following parameters:

                                    Table 27: Parameter function block
                                     Function name                 Index               Byte      Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0
                                     IOL_Call                      46080    0                    IOL_CALL extended function number (0x08)
                                                                   (0xB400)
                                                                            1                    IOL_CALL Port
                                                                                       2         IOL_CALL function call index (0xFE4A)
                                                                                       3
                                                                                       4         IOL_CALL controller/status
                                                                                       5         IOL_CALL index
                                                                                       6
                                                                                       7         IOL_CALL subindex
                                                                                       8         IOL_CALL data
                                                                                       …
                                                                                       N

                                    Table 28: IOL_Call
                                     Parameter                                     Definition
                                     ID                                            Address of one of the available IO-Link device submodules or
                                                                                   the IO-Link Master submodule (IOLM subslot 1.1), see reference
                                                                                   figure.
                                     CAP                                           The Client Access Point (CAP) represents the PROFINET data set
                                                                                   index that provides the “tunnel” to the IO-Link system. The value of
                                                                                   this index is 46080.
                                     Port                                          Number of the IO-Link port on which the function is to be executed
                                                                                   (1 to 8). This value is not relevant if IOL_CALL is called via one of
                                                                                   the IO-Link device submodules, since a submodule is permanently
                                                                                   connected to a port.
                                     RD/WR                                         Specifies whether the On-Request data is to be read (RD) or writ‐
                                                                                   ten (WR).
                                     IOL_Index                                     Index of the On-Request data or command code for the port func‐
                                                                                   tion
                                     IOL_Subindex                                  Subindex of the On-Request data or command code for the port
                                                                                   function
                                     IOL_Data                                      On-Request data to be written to or read from the IO-Link device




50   O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                                               8027832./2022-06-10 | SICK
                                                                                                                                  Subject to change without notice

OPERATION 8


                                   NOTE
                                   The HW ID for the SICK device and IOL-Call module is assigned to slot 1.1 of the
                                   hardware configuration.




8.1.3.2               SICK function blocks
                                   With the Function Block Factory digital software service, SICK is providing a unique
                                   possibility of generating specific PLC function blocks that go far beyond the range of
                                   performance of Siemens function blocks. Further information about the exchanged
                                   data and the connected devices is available here.
                                   Function blocks for any IO-Link device (manufacturer-independent) can be generated
                                   individually via the Function Block Factory. These function blocks are fully tested and
                                   documented. They considerably facilitate and accelerate PLC programming and prevent
                                   errors. This can save time and money in production processes.
                                   Additional information on the Function Block Factory from SICK can be found on the
                                   homepage:
                                   www.sick.com/functionblockfactory

8.2                   Dual Talk

8.2.1                 Communication via REST-API
                                   The SIG350 provides a REST API with JSON data format for accessing the data of the
                                   connected devices. These operating instructions provide an overview of the available
                                   device functions and the access mechanisms.
                                   The REST API interface corresponds to the standard of the IO-Link community, which
                                   was defined in the document “JSON Integration for IO-Link” with version 1.0.0 (as of
                                   March 2020, part number 10.2020).

8.2.1.1               General description of the interface
                                   The REST API is a client-server interface and enables the client to request data from
                                   the server via defined resources. The REST API is stateless, which means that no
                                   information about the connection status and no information about the server or client
                                   is required.



8027832./2022-06-10 | SICK                                           O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   51
Subject to change without notice

8 OPERATION

                                         The operation is based on HTTP methods. Common HTTP methods are GET, POST,
                                         PUT and DELETE. For the SIG350, the GET and POST request methods are particularly
                                         relevant, where the request and response data is represented in JSON format. JSON,
                                         or JavaScript Object Notation, is a minimal, visually readable format for structuring
                                         data. It is mainly used to transmit data between a server and a web application as an
                                         alternative to XML.
                                         Table 29: HTTP methods
                                             HTTP method                        Description
                                             GET                                Requests the specified data from the server (= data is only read and
                                                                                not changed)
                                             POST                               The payload is transmitted to the server (= write data)
                                             DELETE                             Deletes the specified resources on the server (= data is deleted)


8.2.1.2           API documentation
                                         The current documentation (also called Open API) of the API interface can be down‐
                                         loaded at www.sick.de/SIG350. This document defines all available variables and
                                         methods of the API interface of the SIG350.
                                         The OPEN API documentation is in JSON/YAML format and can be used with appropri‐
                                         ate software tools such as Swagger, Postman or Insomnia.

8.2.1.3           API structure

                                         Request
                                         To request data, a command must be sent to the server, in this case the SIG350. This
                                         command is structured in HTTP format:
                                         URL schema: http://[IP-Adresse]/[BasePath]/[Resource]
                                          •        The IP address corresponds to the valid IP address of the module. The default
                                                   IP address of the SIG350 is 192.168.0.1. If necessary, the default address has
                                                   already been changed via the PLC or the web interface.
                                          •        The BasePath is defined in the standard of the IO-Link community: /iolink/v1
                                          •        The resource is used to address the corresponding parameter which is to be read
                                                   or written:
                                         E.g.: /masters/{masterNumber}/ports/{portNumber}/configuration
                                         An overview of the available variables and methods can be found in section XXX and in
                                         the standard of the IO-Link community.
                                         Thus, an example URL for reading the port configuration of port S3 is as follows:
                                         http://192.168.0.1/iolink/v1/masters/1/ports/3/configuration

                                         NOTE
                                         The {masterNumber} variable is always 1, because the SIG350 gateway has only one
                                         master.

                                         Response
                                         For each request, the SIG350 responds with status information and data or only status
                                         information if no data is available. Depending on the request, this response can contain
                                         several pieces of information. In case of an error, the corresponding error code (see
                                         section XXX) is returned.
                                         The response corresponds to the following format:

                                         {

52        O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                                           8027832./2022-06-10 | SICK
                                                                                                                                   Subject to change without notice

OPERATION 8


                                   “name1”: value1
                                   “name2”: value2
                                   “name…”: value…
                                   }

                                   •       The “name” corresponds to the name of the object: e.g. Vendor ID
                                   •       The “value” corresponds to the value of the object: e.g.: 26
                                   Thus, an example response is as follows:
                                   {
                                   “Vendor ID”: 26
                                   “Device ID”: 8389238
                                   “deviceAlias”: Flow_control_1
                                   }

                                   NOTE
                                   No specific response time can be guaranteed for the use of the REST API interface
                                   since the HTTP requests are based on a standard TCP mechanism. The response time
                                   also depends on the system environment and system load. When using the web UI at
                                   the same time, the response time increases.


8.2.1.4               Available variables and methods
                                   The SIG mainly supports the GET and POST methods. For selected variables, the
                                   DELETE function is also supported.
                                   All API calls are executed synchronously. This means that every request is followed by a
                                   response. A minimum response time cannot be defined for the REST API commands, as
                                   this is also dependent in particular on the system environment and load used.
                                   The following gives an overview of the available variables and methods. Detailed infor‐
                                   mation and examples can be downloaded in the Open API documentation via the SICK
                                   website, see www.sick.com.
                                   REST API resources
                                   Table 30: Overview of REST API HTTP resources
                                       Resource                                           Description
                                       /gateway                                           Addressing the gateway
                                       /masters                                           List of all available master variables and identi‐
                                                                                          fication information
                                       /master/{masterNumber}                             Addressing of a specific master
                                       /master/{masterNumber} /ports                      List of all available ports at a specific master
                                                                                          including port number, status information and
                                                                                          deviceAlias
                                       /master/{masterNumber} /ports/{portNum‐            Addressing of a specific port connection at a
                                       ber}                                               specific master
                                       /devices                                           Addressing of all connected devices at all mas‐
                                                                                          ters
                                       /devices/{deviceAlias}                             Addressing a specific device via the device
                                                                                          name

                                   /gateway
                                   Additional resources are defined for the individual HTTP methods:

8027832./2022-06-10 | SICK                                             O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   53
Subject to change without notice

8 OPERATION

                                    Table 31: Gateway Resource overview(/iolink/v1/gateway)
                                     Resource                              HTTP        Description
                                                                           Method
                                     /identification                       GET         Read out of identification data (e.g. MAC address or
                                                                                       serial number of the device)
                                     /capabilities                         GET         Information on device functions
                                     /configuration                        GET         Read out of device or Ethernet configuration (e.g.
                                                                                       DHCP or IP address)
                                     /configuration                        POST        Writing of device or Ethernet configuration

                                    /masters
                                    In principle, more than one IO-Link Master can be addressed via a gateway. The differ‐
                                    ent masters are numbered consecutively in the request, starting with 1 for the first
                                    master.
                                    NOTE
                                    The {masterNumber} variable is always 1, because the SIG350 gateway has only one
                                    master.
                                    Further resources are also available here:
                                    Table 32: Overview of the master resource (/iolink/v1/masters/1)
                                     Resource                              HTTP        Description
                                                                           Method
                                     /capabilities                         GET         Read out of functions of the specific IO-Link Master
                                                                                       (e.g. the number of ports or the maximum voltage
                                                                                       supply)
                                     /identification                       GET         Read out of identification data of the specific IO-
                                                                                       Link Master (e.g. vendor ID, serial number or firm‐
                                                                                       ware version)
                                     /identification                       POST        Writing of identification data of the specific master
                                                                                       (e.g. LocationTag, functionTag)


                                    /masters/{masterNumber}/ports
                                    With the following resources, additional information of the individual ports at a specific
                                    master can be called up:
                                    Table 33: Overview of the port resource (/iolink/v1/masters/1/ports)
                                     Resource                              HTTP        Description
                                                                           Method
                                     /capabilities                         GET         Read out of functions of the specific port (e.g. port
                                                                                       type or max. voltage supply)
                                     /status                               GET         Read out of current status of a specific port (e.g.
                                                                                       deactivated or the IO-Link version of the connected
                                                                                       IO-Link device)
                                     /configuration                        GET         Read out of configuration of a specific port (e.g.
                                                                                       cycle time or deviceAlias of the connected IO-Link
                                                                                       device)
                                     /configuration                        POST        Writing of configuration on a specific port (e.g. devi‐
                                                                                       ceAlias)
                                     /datastorage                          GET         Read out of Data Storage object
                                     /datastorage                          POST        Writing of Data Storage object

                                    /devices



54   O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                                     8027832./2022-06-10 | SICK
                                                                                                                        Subject to change without notice

OPERATION 8


                                   The connected devices are addressed via the deviceAlias. If no deviceAlias is defined,
                                   then the default value (e.g. master1port6) is used.
                                   Example:
                                   An IO-Link device with deviceAlias “sensor34” is connected to port 6. The addressing is
                                   performed with the request
                                   GET/iolink/v1/devices/sensor34/identification
                                   However, if no deviceAlias is defined and thus the default value is used, then the
                                   request changes as follows:
                                   GET/iolink/v1/devices/master1port6/identification
                                   The description master1port6 therefore stands for the sixth port on the first master.

                                   All connected devices are listed via the GET /iolink/v1/devices request.

                                   The following resources can be used to call up additional information on the connected
                                   devices:
                                   Table 34: Gateway Resource overview(/iolink/v1/device)
                                   Resource               HTTP                  Description
                                                          Method
                                   /capabilities          GET                   Read out of device information of the connected
                                                                                device (e.g. min. cycle time)
                                   /identification        GET                   Read out of device identification data
                                   /identification        POST                  Writing of device identification data
                                   Process data
                                   /processdata/value     GET                   Read out of process data (input and output data) of
                                                                                a specific IO-Link device
                                   /processdata           GET                   Read out of process input data of a specific IO-Link
                                   /getdata/value                               device
                                   /processdata           GET                   Read out of process output data of a specific IO-
                                   /setdata/value                               Link device
                                   /processdata/value     POST                  Writing of process output data on a specific IO-Link
                                                                                device
                                   Parameter values
                                   /parameters            GET                   Read out of parameter values of a specific device
                                   /{index}/value                               by means of the index
                                   /parameters            GET                   Read out of parameter values of a specific device
                                   /{index}/subindices                          by means of the index and subindex
                                   /{subindex}/value
                                   /parameters            POST                  Writing of a parameter value using the index
                                   /{index}/value
                                   /parameters            POST                  Writing of a parameter value using the index and
                                   /{index}/subindices                          subindex
                                   /{subindex}/value
                                   Events
                                   /events                GET                   Read out of all events for a specific device

                                   /vendor




8027832./2022-06-10 | SICK                                          O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   55
Subject to change without notice

8 OPERATION

                                         Table 35: Vendor-specific JSON settings(/iolink/v1/vendor/masters/{masternum-
                                         ber})
                                             Resource                           HTTP            Description
                                                                                Method
                                             /diagnostics /value                GET             Read out of average value of the master
                                             /ports/{portnumber}/               GET             Read out of minimum and maximum current values
                                             statistics/current                                 at the specific port
                                             /ports/{portnumber}/               GET             Read out of minimum and maximum voltage values
                                             statistics/voltage                                 at the specific port
                                             /ports/{portnumber}/ GET                           Read out of minimum and maximum temperature
                                             statistics/temperature                             values at the specific port
                                             /ports/{portnumber}/               GET             Read out of actual current values at the specific
                                             diagnostics                                        port
                                             /current
                                             /ports/{portnumber}/               GET             Read out of actual voltage values at the specific
                                             diagnostics                                        port
                                             /voltage
                                             /ports/{portnumber}/               GET             Read out of actual temperature values at the spe‐
                                             diagnostics                                        cific port
                                             /temperature


8.2.1.5           Status code and error messages
                                         Errors may occur when processing HTTP requests. Several errors are defined.
                                         The following rules apply to troubleshooting:
                                          •        If multiple errors occur while processing the request, only the first detected error is
                                                   responded to.
                                          •        If no REST API commands are available, error 103 is returned.

                                         Error messages are structured as follows:
                                         {
                                         “code”: 102,
                                         “message”: “Internal communication error”
                                         }
                                         The following table provides an overview of the possible error codes:

                                         Table 36: Error messages
                                             Error       HTTP           Message                           Note
                                             code        code
                                             General error
                                             101         500            Internal server error             This error can occur with any request
                                             102         500            Internal communication error      This error can occur with any request
                                             103         404            Operation not supported           This error is returned if the requested
                                                                                                          function does not exist.
                                             104         400            Action locked by another client   Fieldbus controller or another participant
                                                                                                          blocks access
                                             105         501            IODD feature not supported        SIG350 does not support IODDs
                                             106         501            MQTT feature not supported
                                             150         403            Permission denied                 Access is not allowed. Check access
                                                                                                          rights in the configuration. This error can
                                                                                                          occur with any request.


56        O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                                        8027832./2022-06-10 | SICK
                                                                                                                                Subject to change without notice

OPERATION 8


                                   Error    HTTP        Message                                     Note
                                   code     code
                                   JSON parsing error
                                   201      400         JSON parsing failed                         Error while parsing the incoming JSON
                                                                                                    value
                                   202      400         JSON data value invalid                     Error while parsing a specific JSON value,
                                                                                                    such as an incorrect IP address
                                   203      400         JSON data type invalid                      E.g.: data type string instead of number
                                   204      400         Enumeration value unknown
                                   205      400         JSON data value out of range                Exceeds the minimum or maximum value
                                   206      400         JSON data value out of bounds               An array/string was accessed whose max‐
                                                                                                    imum length was exceeded.
                                   207      400         deviceAlias is not unique
                                   208      400         POST request without content
                                   Error during resource access
                                   301      404         Resource not found                          E.g. incorrect URL
                                   302      404         masterNumber not found
                                   303      404         portNumber not found
                                   304      404         deviceAlias not found
                                   305      400         Query parameter name invalid
                                   306      400         Query parameter value invalid
                                   307      400         Port is not configured to IO-Link           E.G.: IOLINK_MANUAL or IOLINK_AUTOS‐
                                                                                                    TART mode
                                   308      404         IO-Link device is not accessible            E.g. not connected or communication
                                                                                                    error
                                   309      404         IO-Link parameter not found
                                   310      404         IO-Link parameter access not
                                                        supported by the device
                                   311      400         IO-Link parameter access error              The additional “iolinkErrorCode” and
                                                                                                    “iolinkErrorMessage” fields contain the
                                                                                                    IO-Link error code and the event text from
                                                                                                    the ErrorTypes table.
                                   312      404         IO-Link parameter name is not               Please use the format [Name]_[Index].
                                                        unique
                                   DataStorage error
                                   401      400         Data storage mismatch                       No match between configured device and
                                                                                                    data from data memory. Check device ID.
                                   Processing error in the process data
                                   501      400         I/Q is not configured as DIGI‐              Writing process data on I/Q is not possi‐
                                                        TAL_OUTPUT                                  ble
                                   502      400         C/Q is not configured as DIGI‐              Writing process data on C/Q is not possi‐
                                                        TAL_OUTPUT                                  ble
                                   503      400         IO-Link device has no output
                                                        process data
                                   Error in the payload
                                   701      400         Data set incomplete
                                   702      400         Data set not applicable                     The entire data set is denied
                                   703      400         Data set combination incompati‐ The entire data set is denied
                                                        ble


8027832./2022-06-10 | SICK                                               O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   57
Subject to change without notice

8 OPERATION

8.2.2             MQTT client
                                         The SIG350 provides a MQTT interface with JSON data format for accessing the data of
                                         the IO-Link Master and of the connected devices. These operating instructions provide
                                         an overview of the available messages and the access mechanisms.


8.2.2.1           General description
                                         The MQTT (Message Queuing Telemetry Transport) protocol is an open network protocol
                                         for machine-to-machine communication that enables the transmission of telemetric
                                         data between devices. The built-in MQTT client allows the device to publish a specific
                                         set of information to an MQTT broker.
                                         Messages are published once after the device is started and then when the corre‐
                                         sponding value is changed. However, the sending of the message does not take place
                                         immediately, but cyclically, every 5 seconds. In addition to the payload, so-called topics
                                         are also transmitted in the messages. This allows for mapping and hierarchical identifi‐
                                         cation.
                                         The data structure of the messages is in JSON format and is directly oriented on the
                                         schema of the REST API (see "API structure", page 52).
                                         Quality of Service cannot be configured and is set to “At most once”, i.e. messages are
                                         only sent once without confirmation from the client or broker.
                                         If the connection is lost, a Last Will is sent with the following message:

                                         Table 37: Last Will message
                                          Topic                                               Message
                                          EXIT                                                “Publisher”: “Offline”

                                         The MQTT functions are activated in the delivery state. The MQTT client can be deacti‐
                                         vated either via the web interface or directly via the rotary switches.

8.2.2.2           Messages – topics
                                         The following gives an overview of the available messages. The composition of the
                                         topics is based on the REST API schema and is composed as follows:
                                         {client head topic}/[BasePath]/[Domain]/{Parameter}
                                          •       The {clientHeadTopic} variable can be assigned via the WebUI. The MAC address is
                                                  used as the default value.
                                          •       The BasePath is oriented on the REST API standard and is defined at: /iolink/v1
                                          •       Via [Domain]/{Parameter}, the respective message is identified:
                                                  e.g.: /masters/{masterNumber}/ports/{portNumber}/configuration
                                          •       The payload of the message is formatted equivalent to the REST API and can
                                                  be taken from the OPEN API document, see "Available variables and methods",
                                                  page 53 or www.sick.com.
                                         Table 38: MQTT topics
                                          Domain Topic                                             Description
                                          gateway {clientHeadTopic}/iolink/v1/gate‐                Read out of identification data (e.g. MAC
                                                  way/identification                               address or serial number of the device)
                                                         {clientHeadTopic}/iolink/v1/gate‐         Information on device functions
                                                         way/capabilities
                                                         {clientHeadTopic}/iolink/v1/gateway/con‐ Read out of device or Ethernet configura‐
                                                         figuration                               tion (e.g. DHCP or IP address)




58        O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                                8027832./2022-06-10 | SICK
                                                                                                                        Subject to change without notice

OPERATION 8


                                   Domain Topic                                                  Description
                                   masters {clientHeadTopic}/iolink/v1/mas‐                      Read out of identification data of the spe‐
                                           ters/{masterNumber}/identification                    cific IO-Link Master (e.g. vendor ID, serial
                                                                                                 number or firmware version)
                                            {clientHeadTopic}/iolink/v1/mas‐                     Read out of functions of the specific IO-
                                            ters/{masterNumber}/capabilities                     Link Master (e.g. the number of ports or
                                                                                                 the maximum voltage supply)
                                            {clientHeadTopic}/iolink/v1/mas‐        Diagnostics configuration (e.g. max./min.
                                            ters/{masterNumber}/diagnostics/config‐ voltage, temperature, current)
                                            uration
                                            {clientHeadTopic}/iolink/v1/mas‐                     Average value of supply voltage, tempera‐
                                            ters/{masterNumber}/diagnostics/value                tures and total current
                                   ports    {clientHeadTopic}/iolink/v1/mas‐                     Read out of functions of the specific port
                                            ters/{masterNumber}/ports/{portNum‐                  (e.g. port type or max. voltage supply)
                                            ber}/capabilities
                                            {clientHeadTopic}/iolink/v1/mas‐                     Read out of current status of a specific
                                            ters/{masterNumber}/ports/{portNum‐                  port (e.g. deactivated or the IO-Link ver‐
                                            ber}/status                                          sion of the connected IO-Link device)
                                            {clientHeadTopic}/iolink/v1/mas‐                     Read out of configuration of a specific
                                            ters/{masterNumber}/ports/{portNum‐                  port (e.g. cycle time or deviceAlias of the
                                            ber}/configuration                                   connected IO-Link device)
                                            {clientHeadTopic}/iolink/v1/mas‐                     Configuration of current limitation
                                            ters/{masterNumber}/ports/{portNum‐
                                            ber}/diagnostics/configuration
                                            {clientHeadTopic}/iolink/v1/mas‐                     Read out of actual current values at the
                                            ters/{masterNumber}/ports/{portNum‐                  specific port
                                            ber}/diagnostics/current
                                            {clientHeadTopic}/iolink/v1/mas‐                     Read out of actual voltage values at the
                                            ters/{masterNumber}/ports/{portNum‐                  specific port
                                            ber}/diagnostics/voltage
                                            {clientHeadTopic}/iolink/v1/mas‐                     Read out of actual temperature values at
                                            ters/{masterNumber}/ports/{portNum‐                  the specific port
                                            ber}/diagnostics/temperature
                                            {clientHeadTopic}/iolink/v1/mas‐                     Read out of minimum and maximum cur‐
                                            ters/{masterNumber}/ports/{portNum‐                  rent values at the specific port
                                            ber}/statistics/current
                                            {clientHeadTopic}/iolink/v1/mas‐                     Read out of minimum and maximum volt‐
                                            ters/{masterNumber}/ports/{portNum‐                  age values at the specific port
                                            ber}/statistics/voltage
                                            {clientHeadTopic}/iolink/v1/mas‐                     Read out of minimum and maximum tem‐
                                            ters/{masterNumber}/ports/{portNum‐                  perature values at the specific port
                                            ber}/statistics/temperature
                                   mqtt     {clientHeadTopic}/iolink/v1/mqtt/configu‐ Information on MQTT configuration
                                            ration
                                            {clientHeadTopic}/iolink/v1/mqtt/connec‐ MQTT connection status
                                            tionstatus
                                   devices {clientHeadTopic}/iolink/v1/devices/mas‐ Read out of process data (input and out‐
                                           ter1port1/processdata/value              put data) of a specific IO-Link device
                                            {clientHeadTopic}/iolink/v1/devices/mas‐ Read out of process input data of a spe‐
                                            ter1port1/processdata/getdata/value      cific IO-Link device
                                            {clientHeadTopic}/iolink/v1/devices/mas‐ Read out of process output data of a spe‐
                                            ter1port1/processdata/setdata/value      cific IO-Link device
                                            {clientHeadTopic}/iolink/v1/devices/mas‐ Read out of all events for a specific device
                                            ter1port1/events


8027832./2022-06-10 | SICK                                            O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   59
Subject to change without notice

8 OPERATION

8.2.3             Description of OPC UA Server

8.2.3.1           Data model
                                         The SIG350 has an OPC UA interface. OPC UA is a platform-independent standard with
                                         a service-oriented architecture for communication in and with industrial automation
                                         systems.
                                         The SIG350 module provides an OPC UA server at field device level, to which an OPC UA
                                         client can connect to exchange information.
                                         The OPC UA device model is based on the general device specification:
                                         OPC 10000-100: OPC Unified Architecture
                                         Part 100: Devices
                                         Release 1.03.1
                                         2021-12-07
                                         https://reference.opcfoundation.org/DI/docs/
                                         In addition, the IO-Link Companion specification is implemented with the exception that
                                         all functionality related to the IODD is not supported by the SIG350.
                                         OPC 30120: OPC Unified Architecture for IO-Link
                                         IO-Link: OPC Unified Architecture
                                         Release 1.0
                                         2018-12-01
                                         https://reference.opcfoundation.org/IOLink/docs/
                                         Basically, device access in OPC UA is done via objects and thus follow an object-ori‐
                                         ented approach. Parts of an object can be variables, methods or events. The structure
                                         and content of objects are each described by corresponding data types, which are
                                         defined either specific to profiles or devices. Objects can be derived from several
                                         base classes and inherit the corresponding properties in the form of attributes and
                                         references.
                                          •       Attributes provide information about the object and essentially enable access to
                                                  the payload.
                                          •       References describe the hierarchical arrangement of the object in the device
                                                  model and the relationship to other objects.
                                         All object data types are derived from the UANode base class and thus have properties
                                         (attributes) that enable access in the OPC UA address space via “nodes”. For example,
                                         the “NodeId” attribute can be used to access the instance of individual objects, since
                                         this allows them to be uniquely identified, see "Access to process data", page 67.
                                         More information and a detailed, comprehensive description of OPC UA can be found at
                                         https://reference.opcfoundation.org/.




60        O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                        8027832./2022-06-10 | SICK
                                                                                                                Subject to change without notice

OPERATION 8


8.2.3.2               Commissioning with UA Expert




                                   Figure 33: UA Expert




                                   Figure 34: Entry of IP address with port


                                   •    Entry of IP address with port (default 4840)
                                   •    If necessary, log in with the appropriate user authorization
                                   •    Establishing a connection
                                   Then the device model of the connected device is automatically loaded and displayed
                                   accordingly.
                                   •    DeviceSet: Serves as entry point for accessing the device instance, thus enabling,
                                        for example, the reading of configuration parameters or IO-Link process data.
                                   •    Server: Access to the basic functions of the OPC UA server.
                                   For the sake of clarity, only an excerpt of the corresponding server objects is listed here.




8027832./2022-06-10 | SICK                                              O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   61
Subject to change without notice

8 OPERATION

                                    Table 39: Server objects
                                     Browser name/Hierarchy                        Class      Description
                                     0, “NamespaceArray”                           Variable   Shows all implemented namespaces in the address
                                                                                              range.
                                                                                              This is particularly important for accessing device
                                                                                              objects. Access is granted the NodeId, which is
                                                                                              composed of the NamspaceIndex and a numeric
                                                                                              identifier.
                                                                                              Example:




                                    Table 40: DeviceInformation object
                                     Browser name/Hierarchy                        Class      Description
                                     7, “AppInfo”                                  Object     Enables the read out of device information, e.g.:
                                                                                              device version, part number, etc.




62   O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                                          8027832./2022-06-10 | SICK
                                                                                                                             Subject to change without notice

OPERATION 8


                                   Browser name/Hierarchy       Class                Description
                                   7, “MaintenanceInforma‐      Object               Reading and writing of additional maintenance
                                   tion”                                             information, e.g. description text, date of commis‐
                                                                                     sioning, etc.




                                   Table 41: IO-Link Master object
                                                                     Browser name                          Class          Description
                                                                     3, “Alarms”                           Object         Reading of errors and
                                                                                                                          warnings
                                                                     3, “Capabilities”                     Object         Number of ports Maximum
                                                                                                                          current consumption
                                                                     3, “DeviceID”                         Variable DeviceID
                                                                     2, “Diagnostics”                      Object         Diagnostic information on
                                                                                                                          current consumption, volt‐
                                                                                                                          age and temperature
                                                                     2, “Identification”                   Object         Master Type, Location and
                                                                                                                          Faction Tag
                                                                     3, “MasterConfigura‐                  Variable Not used
                                                                     tionDisabled”
                                                                     2, “MethodSet”                        Object         Methods for rebooting the
                                                                                                                          device and resetting the
                                                                                                                          statistics
                                                                     2, “ParameterSet”                     Object         Variable collection of all
                                                                                                                          master variables
                                                                     3, “Port00” …                         Object         Access point to the port
                                                                     3, “Port07”                                          objects and variables.
                                                                     3, “Statistics”                       Object         Measured minimum and
                                                                                                                          maximum current, temper‐
                                                                                                                          ature, voltage. IO-Link
                                                                                                                          WakeupCount, FrameOk‐
                                                                                                                          Count and RetryCount.
                                                                     3, “VendorID”                         Variable ManufacturerID




8027832./2022-06-10 | SICK                                               O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   63
Subject to change without notice

8 OPERATION

                                    Table 42: IO-Link Port object
                                                                                       Browser name           Class    Description
                                                                                       3, “Alarms”            Object   Reading of errors and
                                                                                                                       warnings
                                                                                       3, “Capabilities”      Object   Pin 2 support. Maximum
                                                                                                                       current consumption Port‐
                                                                                                                       Class.
                                                                                       3, “Configuration”     Object   Reading of port configura‐
                                                                                                                       tion. DeviceID, VendorID,
                                                                                                                       cycle time, pin 2 configura‐
                                                                                                                       tion, Port mode, validation
                                                                                                                       and backup.
                                                                                       3, “Device”            Object   Access point to the device
                                                                                                                       objects and variables.
                                                                                       3, “DeviceConfigura‐   Variable Not used
                                                                                       tionDisabled”
                                                                                       2, “Diagnostics”       Object   Diagnostic information on
                                                                                                                       current consumption, volt‐
                                                                                                                       age and temperature
                                                                                       3, “Information”       Object   Used cycle time, baud
                                                                                                                       rate, status and connection
                                                                                                                       quality.
                                                                                       2, “MethodSet”         Object   Method for setting the con‐
                                                                                                                       figuration
                                                                                       0, “NodeVersion”       Variable Version of the OPC UA port
                                                                                                                       object
                                                                                       2, “ParameterSet”      Object   Variable collection
                                                                                       3, “SIOProcessData”    Object   Pin 2 and pin 4 assignment
                                                                                       3, “Statistics”        Object   Measured minimum and
                                                                                                                       maximum current, temper‐
                                                                                                                       ature, voltage. IO-Link
                                                                                                                       WakeupCount, FrameOk‐
                                                                                                                       Count and RetryCount.




64   O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                                          8027832./2022-06-10 | SICK
                                                                                                                             Subject to change without notice

OPERATION 8


                                   Table 43: IO-Link Device object
                                                                 Browser name                      Class          Description
                                                                 3, “Alarms”                       Object         Reading of errors and warnings
                                                                 3, “DeviceAccess‐                 Variable DeviceAccesslock
                                                                 Locks”
                                                                 2, “DeviceHealth”                 Variable Device state
                                                                 3, “DeviceID”                     Variable DeviceID
                                                                 3, “General”                      Object         Reading and writing of proc‐
                                                                                                                  ess data, ISDUs. System com‐
                                                                                                                  mands, function and location
                                                                                                                  tags
                                                                                                                  Reset of IO-Link device
                                                                 2, “HardwareRevision” Variable Hardware version
                                                                 2, “Identification”               Object         Identification parameters, e.g.
                                                                                                                  device and VendorID, tags,
                                                                                                                  serial number
                                                                 2, “Manufacturer”                 Variable Manufacturer
                                                                 2, “MethodSet”                    Object         Collection of all device methods
                                                                 3, “MinCycleTime”                 Variable Minimum cycle time
                                                                 2, “Model”                        Variable Product name
                                                                 0, “NodeVersion”                  Variable Version of the OPC UA device
                                                                                                            object
                                                                 2, “ParameterSet”                 Object         Variable collection
                                                                 3, “ProductID”                    Variable Part number
                                                                 3, “ProductText”                  Variable Device text
                                                                 3, “ProfileCharacteris‐           Variable Supported profiles
                                                                 tic”
                                                                 3, “RevisionID”                   Variable IO-Link protocol version
                                                                 2, “SerialNumber”                 Variable Serial number
                                                                 2, “SoftwareRevision”             Variable Firmware version
                                                                 3, “VendorID”                     Variable VendorID
                                                                 3, “VendorText”                   Variable Manufacturer text




8027832./2022-06-10 | SICK                                              O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   65
Subject to change without notice

8 OPERATION




                                    Figure 35: Path




66   O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350    8027832./2022-06-10 | SICK
                                                                                       Subject to change without notice

OPERATION 8


8.2.3.3               Access to process data




                                   Figure 36: Access to process data




8.3                   Web interface
                                   The SIG350 can be accessed via the integrated web interface. The IP address of the
                                   SIG350 must be known for this purpose.
                                   The current IP address can be read out via the SOPAS engineering tool.
                                   When delivered, the default IP address of the SIG350 is: 192.168.0.1.
                                   To access the integrated SIG350 web interface, enter the IP address of the SIG350 in
                                   the address line of the web browser.

                                   NOTE
                                   When using the web interface and the fieldbus communication at the same time, the
                                   response time increases.


                                   NOTE
                                   The SIG350 only supports HTTP, but not the HTTPS protocol.


                                   NOTE
                                   To change settings, it is necessary to log in with a certain user level, see "Logging user
                                   in and out", page 74.


8.3.1                 Web interface structure
                                   The integrated web interface has the following structure:

8027832./2022-06-10 | SICK                                             O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   67
Subject to change without notice

8 OPERATION

                                                                                                               1       234



                                    5                                                                                                  7




                                                               6

                                     •       Connection status
                                     •       User management
                                     •       Language options (German/English)
                                     •       Main menu
                                     •       Overview of the different tabs
                                     •       Show/Hide tab navigation
                                     •       Page contents

                                    Each tab has corresponding tiles that provide different information.

                                    These tiles can be reduced or expanded, e.g. to improve the overview on small moni‐
                                    tors.
                                    To do so, click on the Expandable icon in the title bar of the corresponding tile:




                                    If there an extensive amount of content, the default view of the information tile is set
                                    to the essential information. At the bottom of the tile, the term “More” indicates that
                                    additional information is available.
                                    To make this information visible, the tile view can be expanded by clicking on Expanda‐
                                    ble:




68   O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                        8027832./2022-06-10 | SICK
                                                                                                           Subject to change without notice

OPERATION 8




                                   For some parameterization functions, it may be necessary to activate the edit option
                                   first. These functions are marked by a pencil. The corresponding entry can be changed
                                   by clicking on the pencil:




                                   When configurations are changed in the module, these changes are implemented
                                   immediately. Manual saving of changes is not required.
                                   However, there are some functions that require the changes made to be actively
                                   transmitted to the module. This is represented by a blue button directly below the
                                   corresponding input area.
                                   This is necessary, for example, when writing process data to the device. Whether the
                                   process was successful is reported back directly via a message at the upper right edge
                                   of the web interface. This message disappears automatically after a few seconds.




8027832./2022-06-10 | SICK                                          O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   69
Subject to change without notice

8 OPERATION




                                    “Communication status” menu bar
                                    An overview of the connection status of the SIG350 is integrated in the menu bar




                                    Different statuses are displayed:

                                    1        Gateway
                                                      The green display symbolizes that the SIG350 itself is active.



                                    2        Device connection
                                                      Ethernet communication with device active

                                                      Ethernet communication with device interrupted



                                    3        Controller connection
                                                      The green display symbolizes that the SIG350 is connected to a controller
                                                      and that data is being exchanged.
                                                      If there is no active connection to a controller, a red display appears here.


                                    “Home” tab
                                    The Home page is the start page for the SIG350. It provides an overview of the current
                                    module status and device function.




70   O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                               8027832./2022-06-10 | SICK
                                                                                                                  Subject to change without notice

OPERATION 8




                                   This page is divided into three areas.
                                   •    In the left area the identification data, information about the firmware and soft‐
                                        ware versions as well as the vendor information of the module are displayed.
                                   •    In the middle there is a compact image of the SIG350, which shows for each
                                        port the deviceAlias and the light behavior of the corresponding LEDs. The corre‐
                                        sponding light behavior indicates how the respective port is configured (details see
                                        "Status indicators", page 13)
                                   •    The parameterization of the individual ports is clearly displayed on the right
                                        side. In addition to the settings of pin 2 and pin 4, the deviceAlias, the current
                                        consumption and the communication status can also be read out. This overview
                                        corresponds to the configuration as it has been made on the “Ports” tab.

                                   NOTE
                                   Note that the LED displays do not work in real time.

                                   “Connection options” tab
                                   On the “Connection options” tab, the Ethernet settings such as the IP address or the
                                   subnet mask can be changed. In addition, additional fieldbus information is displayed.




                                   NOTE
                                   To activate the Ethernet parameter changes, the device must be switched off and on
                                   once.



8027832./2022-06-10 | SICK                                           O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   71
Subject to change without notice

8 OPERATION




                                    The OPC UA server is activated and configured via the corresponding settings. It is
                                    possible to restrict the writing of ISDUs and process data via OPC UA. The port can also
                                    be configured.




                                    Using the fieldbus information, the user can store additional data in the device or
                                    read them out from the device. These are basically identification and maintenance
                                    parameters.




                                    It is possible to activate communication via the MQTT settings. For this reason, the
                                    server IP must be entered according to the Ethernet adapter of the MQTT broker. In
                                    addition, a client ID must be assigned, which should be unique per broker.

72   O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                      8027832./2022-06-10 | SICK
                                                                                                         Subject to change without notice

OPERATION 8


                                   Note

                                   NOTE
                                   The MQTT client ID may only consist of alphanumeric characters ([a-z][A-Z][0-9]).


                                   “Ports” tab
                                   Settings for connection ports S1 to S8 can be changed in the “Ports” tab. There is a
                                   separate subpage for each port of the SIG350.
                                   The setting for pin 4 and pin 2 can be made individually on each bottom side. For
                                   example, the minimum cycle time or the port designation (deviceAlias) can be changed
                                   here.
                                   The Data Storage function can be configured for Restore or Backup + Restore according
                                   to the desired use case. If data storage is to be used, Device ID and Vendor ID must be
                                   set.
                                   In addition, further information on the port status, such as communication status, but
                                   also diagnostic data of the respective pins with regard to current and voltage and
                                   temperature, is displayed.
                                   If the Data Storage function has been activated, the complete contents of the data
                                   storage container of a port can be transmitted from one SIG350 to a second SIG350.
                                   For this purpose, the “Download data storage object” button for downloading from
                                   one SIG350 and the “Upload data storage object” button for uploading to the second
                                   SIG350 can be used. The exchange format is JSON.




                                   “Devices” tab
                                   On the Devices tab, the device-specific information of the connected IO-Link device is
                                   displayed. There is a separate subpage for each port of the SIG350.
                                   On each subpage, both the process data and the parameter data can be read out or
                                   configured.
                                   IO-Link data can be read from the connected device (Device to Master), but commands
                                   can also be issued to the connected device (Master to Device). Process data from or to
                                   the IO-Link device is transported cyclically via the fieldbus.
                                   For parameter data, it is necessary that these are explicitly requested by the master.
                                   They are transmitted acyclically.



8027832./2022-06-10 | SICK                                          O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   73
Subject to change without notice

8 OPERATION

                                       Using the ISDU (Index Service Data Unit), access is made via the corresponding index
                                       number and subindex number.

                                       NOTE
                                       The available process data and index number are provided by the manufacturer of the
                                       IO-Link device in the data sheet.


                                       NOTE
                                       If the individual underside for the ports remains empty, then either no IO-Link device is
                                       physically connected to the SIG350 or the connected device is not an IO-Link device.




8.3.2           Logging user in and out
                                       To change settings, you must log in at the Maintenance user level (read and write
                                       access). By default, you are logged in at the Run (read-only) user level, where you can
                                       only view data and parameterization. If you want to change the user, you have to click
                                       on the user icon in the top right corner of the menu bar and select the desired user
                                       name in the dialog.




74      O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                       8027832./2022-06-10 | SICK
                                                                                                             Subject to change without notice

OPERATION 8




                                   If a user other than “Run” is selected, the corresponding password must also be
                                   entered.
                                   Note
                                   Saving the user in a web browser may depend on the cookie settings.
                                   When logging in for the first time, you will be prompted to change the default password.
                                   In the interest of cybersecurity, it is strongly recommended that you create a new, differ‐
                                   ent password. Please remember this password. If you have forgotten your password, it
                                   cannot be reset. Please contact your SICK service partner for what to do in this case.

                                   Table 44: User and default passwords
                                   User                           Default password                               Role description
                                   Operator                       No password required                           Reading parameterization
                                   Maintenance                    Main                                           Reading and writing parame‐
                                                                                                                 terization
                                   Service                        Service level                                  Performing advanced settings
                                                                                                                 like firmware updates.


8.3.3                 Forgotten password
                                   If an individually created password has been forgotten, the default passwords can be
                                   restored with the aid of a factory reset using the corresponding rotary switch combina‐
                                   tion on the device.


8027832./2022-06-10 | SICK                                            O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   75
Subject to change without notice

8 OPERATION

8.3.4             Data Storage
                                         The “Data Storage” function makes it much easier to replace defective IO-Link devices.
                                         This means that the entire parameter set of the device, e.g. switching point, additional
                                         logic or teach-in settings, is stored centrally in the SIG350. When a connection is made
                                         to a compatible device, this stored parameter set is written to the device and it behaves
                                         like the replaced device. There are two different use cases, which are described in the
                                         following:
                                         “Backup + Restore” application case:
                                         Parameters are read and written in both directions (from the IO-Link Master to the
                                         device and vice versa). This mode is predominantly used for commissioning, i.e.
                                         changes to the device parameterization triggered by a teach-in, for example, are
                                         automatically uploaded and stored in the data memory object of the SIG350. Device
                                         replacement is also supported, e.g. the parameterization is automatically copied to the
                                         new device if a device has to be replaced.
                                         “Restore” application case:
                                         In this mode, the parameterization of the connected IO-Link device is saved and frozen.
                                         These parameters cannot be changed by the device, i.e. a teach-in directly at the device
                                         is ignored. The replacement of defective devices is also possible. This requires a certain
                                         degree of device compatibility. For this reason, the Device ID and Vendor ID must be
                                         specified.

8.3.4.1           Example use
                                         The “Data Storage” function of the SIG350 IO-Link Master enables easy replacement
                                         of defective IO-Link sensors. The following example shows step-by-step how the SIG350
                                         can be used to commission a new IO-Link device so that a replacement device is
                                         automatically parameterized according to the original device.

                                          •       Start the web interface and navigate to the “Ports” tab. Select the desired function
                                                  with the “Validation and backup” button. This setting is only available for pin 4, as
                                                  the Data Storage function is restricted to IO-Link communication.




                                          •       As soon as the “Backup and Restore” or “Restore” selection has been activated,
                                                  additional buttons appear which serve to validate the connected device.
                                         The Device ID and Vendor ID must correspond to the data of the connected device. This
                                         data is checked in the event of device replacement and an error message is returned in
                                         the event of deviating data.

76        O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                           8027832./2022-06-10 | SICK
                                                                                                                   Subject to change without notice

OPERATION 8




                                   •    In addition, the “Data storage” function tile appears. This function allows down‐
                                        load or upload of records with the stored information from the device. The data
                                        format is JSON.




                                   •    It enables the new master to read out and save the configuration data stored in
                                        the device when the IO-Link Master module is replaced.
                                   To use the Data Storage, the Vendor ID and Device ID of the connected device must be
                                   entered in the validation settings.



8.4                   SOPAS Engineering Tool

                                   With the aid of the SOPAS Engineering Tool, the SIG350 can be called up on a computer
                                   running Microsoft Windows. This is particularly helpful if the IP address of the SIG350 is
                                   not known.
                                   Connect the SIG350 to your computer via Ethernet and start SOPAS ET. When starting
                                   the program, the Ethernet interface is always scanned for connected devices and
                                   devices found appear in the Device Search on the right side of the interface. Double
                                   clicking on the result or dragging and dropping the module makes it possible to add the
                                   module as a new project on the left side. Devices that are already in the project are
                                   grayed out in the search results.




8027832./2022-06-10 | SICK                                           O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   77
Subject to change without notice

8 OPERATION




                                    If the device status appears as offline in the project icon, then the SIG350 must first be
                                    switched online. Click on the offline button to do so.
                                    The IP address of the SIG350 is displayed in the project tile. It can be changed by
                                    clicking on the pencil icon. A window appears with the TCP/IP settings in which changes
                                    can be made.
                                    A restart of the device is then required, which is automatically performed by the device.




78   O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                       8027832./2022-06-10 | SICK
                                                                                                          Subject to change without notice

OPERATION 8


                                   To parameterize the SIG350, double-click on any point on the project icon. The device
                                   window opens, in which all device parameters are displayed. This device window is
                                   identical to the contents of the web interface (see "Web interface structure", page 67).
                                   Here the parameterization can be carried out, parameters can be loaded into or from
                                   the device or parameter values can be observed.

                                   NOTE
                                   The user login is not done via SopasET directly, but via the device interface (see
                                   "Logging user in and out", page 74). The Import/Export parameter is not supported.




8027832./2022-06-10 | SICK                                          O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   79
Subject to change without notice

9 TROUBLESHOOTING


9             Troubleshooting
                                     Various problems can occur when using the SIG350.
                                     If you have problems, SICK Technical Support is available to help. Contact your SICK
                                     Service partner in this case.

                                     However, a large number of problems can be identified and fixed independently with
                                     the help of the following tips:
                                      •       With section 9.4, make sure the LEDs are not reporting problems
                                      •       Check that the network IP address, subnet mask and gateway are configured
                                              correctly.
                                      •       Make sure that the IP address programmed in the IO-Link Master matches the
                                              unique, reserved, configured IP address assigned by the system administrator.
                                      •       Make sure that you use the correct cable types on the correct connections and
                                              that all cables are firmly connected.
                                      •       Disconnect the IO-Link device from the master and reconnect it. Possibly the
                                              master had not correctly identified the connected device.
                                      •       Restart the IO-Link Master.
                                      •       Check whether the Data Storage function has been activated correctly.
                                      •       Reset the module to factory settings (see "Reset to factory settings", page 80 )
                                      •       Update the firmware of the module (see "Updating firmware", page 80)


9.1           Reset to factory settings
                                     In some cases it is helpful to reset the module to the factory settings. To do this, use
                                     either the web interface or the corresponding rotary switch position.
                                     By resetting to the factory settings, all parameterizations made are lost and must be
                                     carried out again.
                                     We recommend creating a backup before resetting to the factory settings. As soon as
                                     the module has been reset to factory settings, all parameterizations made are deleted
                                     and cannot be restored. A backup can save considerable effort in the event of an error.
                                     Changes to settings in the web interface require maintenance or service rights. If these
                                     are not available, the Settings tab is grayed out and cannot be edited.


9.2           Device restart
                                     In some cases it is necessary to restart the module. To do this, either use the web
                                     interface or switch the voltage supply off and on.

9.3           Updating firmware
                                     To ensure that the device is up to date, the firmware of the SIG350 can be updated.
                                     Use the web interface to do this.
                                     The appropriate firmware file for the corresponding module variant is required. The
                                     firmware file can be obtained from SICK support if required and always comprises a .zip
                                     file.
                                     Changes to settings in the web interface require maintenance or service rights. If these
                                     are not available, the Settings tab is grayed out and cannot be edited.

                                     NOTE




80    O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                          8027832./2022-06-10 | SICK
                                                                                                              Subject to change without notice

TROUBLESHOOTING 9


                                   Never perform a firmware update during operation of the system in which the module is
                                   installed. The plant must first be shut down properly or brought into a safe operational
                                   status before any firmware update.
                                   Performing an update
                                   The firmware version used on the module can be found via the web interface. To do
                                   this, access the web interface via the IP address of the module.
                                   You will find the currently used firmware version on the home page.




                                   The following steps are necessary to perform a firmware update:
                                   •    Change user level to Service. Password: servicelevel
                                   •    Open the main menu in the menu bar and select the Deviceà Update firmware
                                        function
                                   •    Upload file: Clicking on the “Select file” button opens a dialog window where you
                                        can select the location of the .zip file. Clicking on OK saves the file in the flash
                                        memory of the module.
                                   •    At the end of the process, a status message appears with the result of the update.
                                        If the result is positive, a module restart is required to permanently save the
                                        firmware from the flash memory to the module. The module performs this restart
                                        automatically. Manual restart is not required.
                                   •    During this restart, the new firmware is loaded on the device. As a result, the
                                        firmware version displayed on the Home page is updated.

9.4                   Fault diagnosis
                                   Basically, the error state of the device is signaled by the individual LEDs, see 3.2.2.
                                   Protocol-specific errors can be found in the respective sub-section.
                                   •    Profinet: see "Profinet diagnostics", page 49
                                   •    REST API: see "API structure", page 52




8027832./2022-06-10 | SICK                                           O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   81
Subject to change without notice

10 DISASSEMBLY AND DISPOSAL


10           Disassembly and disposal
                                    The SIG350 must be disposed of in line with applicable country-specific regulations.
                                    When disposing of them, you should try to recycle them (especially the precious met‐
                                    als).

                                                Note
                                                Disposal of batteries, electrical and electronic devices
                                                · In accordance with international regulations, batteries, rechargeable batteries and
                                                electrical and electronic devices must not be disposed of with household waste.
                                                · The owner is required by law to dispose of these devices at the appropriate public
                                                collection points at the end of their service life.




                                                ·        This symbol on the product, its packaging or in the document indicates that a
                                                product is subject to the specified regulations.




82   O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                                  8027832./2022-06-10 | SICK
                                                                                                                     Subject to change without notice

MAINTENANCE 11


11                    Maintenance
                                   Sensor Integration Gateways from SICK are maintenance-free.
                                   We recommend performing the following on a regular basis:

                                   · Clean device
                                   · Check screw connections and plug connections
                                   No modifications may be made to devices.
                                   Subject to change without notice. The specified product features and technical data do
                                   not constitute a written warranty.




8027832./2022-06-10 | SICK                                         O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   83
Subject to change without notice

12 TECHNICAL DATA


12             Technical data
12.1           General technical data
                                      Mechanical data
                                                                                                                                               25
                                                                                                                                             (0.98)




                                                  S4                                                  S8
                                                   0                  1      0                        1



                                                  S3                                                  S7
                                                   0                  1      0                        1

                                      1
                                                  S2                                                  S6
                                                   0                  1      0                        1




                                                                                                               200.1 (7.88)
                                                                                                                              209.4 (8.24)                 225.4 (8.87)
                                                  S1                                                  S5
                                                   0                  1      0                        1

                                                         BF SF      LNK1 ST LNK2        UA US


                                                                    ACT1         ACT2    POWER
                                                                                                           4
                                                                      SIG350
                                                                                                           5

                                      2
                                                   PWR1                                      PWR2

                                                             x100          x10          x1



                                                                                                           6

                                      3
                                                    P1                                           P2




                                                                                                                                              23
                                                                           8 7                                                               (0.91)
                                                             62.7 (2.47)                                                                     35.9 (1.41)

                                      Figure 37: Dimensional drawing



                                      Mechanical data
                                      Table 45: Mechanical data
                                       Housing material                                                    Plastic (Valox 553)
                                       Enclosure rating as per IEC                                         IP 67 (only with connected cables)1)
                                       60529
                                       Dimensions (L x W x H)                                              225 mm x 63 mm x 37.4 mm
                                       Mounting type                                                       2-hole screw mounting
                                       Weight                                                              486 g
                                      1)    If the appropriate cables are not connected to all ports, the free ports must be screwed tight with sealing
                                            plugs (part number 5309189) to ensure IP protection.

                                      Operating conditions

                                      NOTE EMC
                                      This equipment is not intended for use in residential areas and may not provide ade‐
                                      quate protection against radio reception in these environments.



84     O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                                                                                     8027832./2022-06-10 | SICK
                                                                                                                                                                          Subject to change without notice

TECHNICAL DATA 12


                                   Table 46: Operating conditions
                                    Operating temperature             -25 °C ... +70 °C1)
                                    Storage temperature               -40 °C ... +80 °C1)
                                    EMC                               EN 61000-6-2:2016
                                                                      EN 61000-6-4:2020
                                    Impact load                       EN 60068-2-27
                                   1)   Permissible relative humidity 0% ... 95% (non-condensing)

                                   Electrical data
                                   Table 47: Electrical data
                                    Voltage supply UA 18 ... 30 V DC1)
                                    Voltage supply US 18 ... 30 V DC1)
                                    Voltage supply         Current consumption                                  ≤ 180 mA @ 24 V2)
                                    (PWR1 and              Max. current carrying capacity                       ≤ 16 A, US3)
                                    PWR2)
                                                                                                                ≤ 16 A, UA3)
                                    Port (S1-S8)           Pin 1 max. supply current                            2A
                                                           Pin 2 max. supply current (DO)                       2A
                                                           Pin 4 max. supply current (DO)                       2A
                                                           Max. current carrying capacity per                   4A
                                                           port
                                                           Max. current carrying capacity of all                10 A
                                                           IO-Link ports (S1-S8)4)
                                                           Input characteristics                                EN 61131-2 type 1 + type 3
                                    Protection class       III5)
                                   1)   Each for US and UA, typ. supply voltage 24 V DC
                                   2)   Without load, sensors and outputs switched off
                                   3)   ≤ +40 °C (see "Derating", page 25).
                                   4)   Max. current per port includes both the output current (pin 4 and pin 2, if applicable) and the current
                                        consumption of the connected device (pin 1).
                                   5)   When using a SELV or PELV power supply unit

                                   PROFINET
                                   Table 48: PROFINET
                                    PROFINET/IP port                  2 x 100 Base-Tx
                                    Cable type according to           Min. STP CAT 5 /ST CAT 5e
                                    802.3
                                    Data transmission rate            100 Mbit/s
                                    Max. cable length                 100 m
                                    Flow control                      Half duplex/Full duplex (IEEE 802.33x-Pause)
                                    PROFINET features                 Media redundancy (MRP),
                                                                      network diagnostics (MIB/SNMP),
                                                                      topology detection,
                                                                      port diagnostics (forward/backward),
                                                                      link diagnostics (link length measurement),
                                                                      I&M0 ... 4,
                                                                      automatic device replacement,
                                                                      gear reduction,
                                                                      OpenVAS tested
                                    GSD file                          Available (V2.41)
                                    NetLoad class                     III
                                    Conformity class                  C

8027832./2022-06-10 | SICK                                                    O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   85
Subject to change without notice

12 TECHNICAL DATA

                                     Observed standard                             IEEE802.3u (100Base-Tx)

                                    Ethernet
                                    Table 49: Ethernet
                                     Ethernet interface                            2x100 Base-Tx (with switch)
                                     Cable type according to                       Min. STP CAT 5 /ST CAT 5e
                                     IEEE 802.3
                                     Data transmission rate                        100 Mbit/s
                                     Max. cable length                             100 m
                                     Flow control                                  Half duplex/Full duplex (IEEE 802.33x-Pause)
                                     Open TCP ports                                80 (HTTP)
                                                                                   1883 (MQTT)
                                                                                   2122 (SOPAS)
                                                                                   4840 (OPC UA)
                                                                                   44818 (Ethernet/IP Encapsulation messages based on TCP
                                                                                   Explicit messaging)
                                                                                   50111 (Open for 30 seconds after power up)
                                     Open UDP ports                                68 (DHCP Client)
                                                                                   161 (SNMP Server)
                                                                                   2222 (implied messages IO)
                                                                                   30718 (CoLa scan receiver)
                                                                                   30719... 30738 (CoLa scan sender: if a port is blocked by the
                                                                                   application, the next port is used).
                                                                                   34964 (Profinet RPC Endpointmapper)
                                                                                   44818 (Ethernet/IP Encapsulation messages based on UDP)
                                                                                   49152 (Profinet RPC Device Server)
                                     MQTT version                                  V3.1.1

                                    Additional information:
                                    Table 50: Additional information
                                     Max. number of I/Os that                      104 E/As (8 + 8x6x2 combined with SIG100)
                                     can be connected:
                                     Max. number of I/O-Link                       8
                                     signals that can be con‐
                                     nected:
                                     Ethernet ports:                               2
                                     Max. switching frequency:                     50 Hz

                                    IO-Link
                                    Table 51: IO-Link
                                     Specification                                 V1.0.0 ... V1.1.3
                                     Connection class                              Class A
                                                                                   Class 1)
                                     Transmission rate                             COM1 / COM2 / COM3
                                     Min. IO-Link cycle time                       1 ms
                                     Detection of transmission                     Automatic
                                     rate
                                    1)    Class B is achieved by using pin 2 as output for the voltage supply. Freely configurable per port, no
                                          galvanic separation between US and UA.


86   O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350                                               8027832./2022-06-10 | SICK
                                                                                                                                  Subject to change without notice

ANNEX 13


13                    Annex




8027832./2022-06-10 | SICK         O P E R A T I N G I N S T R U C T I O N S | Sensor Integration Gateway - SIG350   87
Subject to change without notice

8027832./2022-06-10/en
                         Australia                                 Hungary                          Slovakia
                         Phone +61 (3) 9457 0600                   Phone +36 1 371 2680             Phone +421 482 901 201
                                1800 33 48 02 – tollfree           E-Mail ertekesites@sick.hu       E-Mail mail@sick-sk.sk
                         E-Mail sales@sick.com.au                  India                            Slovenia
                         Austria                                   Phone +91-22-6119 8900           Phone +386 591 78849
                         Phone +43 (0) 2236 62288-0                E-Mail info@sick-india.com       E-Mail office@sick.si
                         E-Mail office@sick.at                     Israel                           South Africa
                         Belgium/Luxembourg                        Phone +972 97110 11              Phone +27 10 060 0550
                         Phone +32 (0) 2 466 55 66                 E-Mail info@sick-sensors.com     E-Mail info@sickautomation.co.za
                         E-Mail info@sick.be                       Italy                            South Korea
                         Brazil                                    Phone +39 02 27 43 41            Phone +82 2 786 6321/4
                         Phone +55 11 3215-4900                    E-Mail info@sick.it              E-Mail infokorea@sick.com
                         E-Mail comercial@sick.com.br              Japan                            Spain
                         Canada                                    Phone +81 3 5309 2112            Phone +34 93 480 31 00
                         Phone +1 905.771.1444                     E-Mail support@sick.jp           E-Mail info@sick.es
                         E-Mail cs.canada@sick.com                 Malaysia                         Sweden
                         Czech Republic                            Phone +603-8080 7425             Phone +46 10 110 10 00
                         Phone +420 234 719 500                    E-Mail enquiry.my@sick.com       E-Mail info@sick.se
                         E-Mail sick@sick.cz                       Mexico                           Switzerland
                         Chile                                     Phone +52 (472) 748 9451         Phone +41 41 619 29 39
                         Phone +56 (2) 2274 7430                   E-Mail mexico@sick.com           E-Mail contact@sick.ch
                         E-Mail chile@sick.com                     Netherlands                      Taiwan
                         China                                     Phone +31 (0) 30 229 25 44       Phone +886-2-2375-6288
                         Phone +86 20 2882 3600                    E-Mail info@sick.nl              E-Mail sales@sick.com.tw
                         E-Mail info.china@sick.net.cn             New Zealand                      Thailand
                         Denmark                                   Phone +64 9 415 0459             Phone +66 2 645 0009
                         Phone +45 45 82 64 00                            0800 222 278 – tollfree   E-Mail marcom.th@sick.com
                         E-Mail sick@sick.dk                       E-Mail sales@sick.co.nz          Turkey
                         Finland                                   Norway                           Phone +90 (216) 528 50 00
                         Phone +358-9-25 15 800                    Phone +47 67 81 50 00            E-Mail info@sick.com.tr
                         E-Mail sick@sick.fi                       E-Mail sick@sick.no              United Arab Emirates
                         France                                    Poland                           Phone +971 (0) 4 88 65 878
                         Phone +33 1 64 62 35 00                   Phone +48 22 539 41 00           E-Mail contact@sick.ae
                         E-Mail info@sick.fr                       E-Mail info@sick.pl              United Kingdom
                         Germany                                   Romania                          Phone +44 (0)17278 31121
                         Phone +49 (0) 2 11 53 010                 Phone +40 356-17 11 20           E-Mail info@sick.co.uk
                         E-Mail info@sick.de                       E-Mail office@sick.ro            USA
                         Greece                                    Russia                           Phone +1 800.325.7425
                         Phone +30 210 6825100                     Phone +7 495 283 09 90           E-Mail info@sick.com
                         E-Mail office@sick.com.gr                 E-Mail info@sick.ru              Vietnam
                         Hong Kong                                 Singapore                        Phone +65 6744 3732
                         Phone +852 2153 6300                      Phone +65 6744 3732              E-Mail sales.gsg@sick.com
                         E-Mail ghk@sick.com.hk                    E-Mail sales.gsg@sick.com


                         Detailed addresses and further locations at www.sick.com




                         SICK AG | Waldkirch | Germany | www.sick.com