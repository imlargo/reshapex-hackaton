TECHNICAL INFORMATION


CSS/CSX
General information on commissioning, integra‐
tion and operation of devices in IO-Link mode

Described product
IO Link - CSS/CSX

Manufacturer
SICK AG
Erwin-Sick-Str. 1
79183 Waldkirch
Germany

Legal information
This work is protected by copyright. Any rights derived from the copyright shall be reserved for SICK AG. Reproduc‐
tion of this document or parts of this document is only permissible within the limits of the legal determination
of Copyright Law. Any modification, abridgment or translation of this document is prohibited without the express
written permission of SICK AG.
The trademarks stated in this document are the property of their respective owner.
© SICK AG. All rights reserved.

Original document
This document is an original document of SICK AG.




2       T E C H N I C A L I N F O R M A T I O N | CSS/CSX                                         9405579/2024-07-30 | SICK
                                                                                                Subject to change without notice

CONTENTS


Contents
                                   1    About this document........................................................................                              4
                                        1.1       Purpose of this document........................................................................                4
                                        1.2       Intended use.............................................................................................       4
                                        1.3       Symbols.....................................................................................................    4

                                   2    Description of IO-Link.......................................................................                            5

                                   3    Documentation and accessories....................................................                                        6

                                   4    Physical layer.....................................................................................                      7

                                   5    Integration of the sensor into the control level.............................                                            8

                                   6    Accessories for visualization, parameterization and integra‐
                                        tion.......................................................................................................              9

                                   7    Setting, configuration and integration........................................... 10

                                   8    Process data structure..................................................................... 11

                                   9    Service data....................................................................................... 13
                                        9.1       Device identification.................................................................................         13
                                        9.2       General device settings............................................................................            14
                                        9.3       Teach-in/Detection settings.....................................................................               19
                                        9.4       Installation/Diagnostics...........................................................................            27
                                        9.5       Smart Tasks..............................................................................................      30

                                   10   Sensor replacement/data storage................................................. 34

                                   11   Events................................................................................................... 37
                                        11.1 Event Qualifier..............................................................................................       37
                                        11.2 Event Code...................................................................................................       37

                                   12   Use case: Setting the process data................................................ 43

                                   13   Technical data.................................................................................... 44

                                   14   List of abbreviations.......................................................................... 45

                                   15   Index.................................................................................................... 46




9405579/2024-07-30 | SICK                                                                                   T E C H N I C A L I N F O R M A T I O N | CSS/CSX     3
Subject to change without notice

1 ABOUT THIS DOCUMENT


1               About this document
1.1             Purpose of this document
The ISDU descriptions in this document apply to IO-Link-capable sensors.
In some cases, functions may be described in this document which are not supported by individual sensors. The
functions in question are marked accordingly (see "Symbols", page 4).
The individual range of functions of a single sensor is shown in full in the IODD overview on the respective product
page at www.sick.coml.

1.2             Intended use
Use IO-Link only as described in this documentation.

1.3             Symbols

NOTICE
This symbol indicates important information.


NOTE
This symbol provides additional information, e.g., dependencies / interactions between the described function and
other functions, or when individual functions are not supported by every sensor.




4       T E C H N I C A L I N F O R M A T I O N | CSS/CSX                                          9405579/2024-07-30 | SICK
                                                                                                 Subject to change without notice

DESCRIPTION OF IO-LINK 2


2                     Description of IO-Link
IO-Link communication interface
The product has the IO-Link communication interface.
IO-Link communication is a Master-Device communication system.
The sensor can be used in standard I/O mode (SIO) or in IO-Link mode (IOL). All automation functions and other
parameter settings are effective in IO-Link mode and in standard I/O mode.
The following functions are supported via this standard IO-Link communication interface:
•       Flexible sensor settings
•       Digital transmission of the sensor signals to the IO-Link Master
•       Visualization and configuration of the sensor
•       Diagnosis / Condition Monitoring
•       Device identification
•       Easy device replacement
•       Events
A detailed description of the adjustable functions and associated indices can be found in the technical information
“IO-Link description”, available for download at www.sick.com.

IO-Link and control integration
IO-Link is a non-proprietary internationally standardized communication technology which makes it possible to
communicate with sensors and actuators in industrial environments (IEC 61131-9).
IO-Link devices communicate with higher-level control systems via an IO-Link Master. The IO-Link devices are
connected to these via a point-to-point connection.
IO-Link Master are available in different versions. In most cases, they are remote fieldbus gateways or input cards
for the backplane bus of the control used.
For an IO-Link Device to communicate with the control system, both the IO-Link Master and the IO-Link Device must be
created (integrated) in the hardware configuration in the control system manufacturer's engineering tool.
Not all manufacturers of control systems support the use of the IO-Link device description file (IO-link Device
Descreption = IODDs). If a third-party IO-Link Master is used, the IO-Link Device can also be integrated by manually
entering the relevant sensor parameters directly during hardware configuration.
To ensure that the IO-Link Device can be easily integrated into the control program, SICK also provides function
blocks for many control systems. Among other things, these function blocks make it easier to read and write the
individual sensor parameters and support the interpretation of the process data supplied by the IO-Link Device . You
can also download them free of charge from the homepage: www.sick.com.
A number of tutorial videos are available on SICK's YouTube channel to assist with the integration of SICK IO-Link
Mastern: www.youtube.com/SICKSensors.
If you have any questions, SICK Technical Support is available to help all over the world.




9405579/2024-07-30 | SICK                                                          T E C H N I C A L I N F O R M A T I O N | CSS/CSX   5
Subject to change without notice

3 DOCUMENTATION AND ACCESSORIES


3                Documentation and accessories
Accessory components and additional information are available for integrating and setting the IO-Link device. You
will find documentation and software, accessories and links to the SICK Product ID.

SICK product ID
The SICK product ID uniquely identifies the product. It also serves as the address of the web page with information
on the product.
The SICK product ID comprises the host name pid.sick.com, the part number (P/N), and the serial number (S/N),
each separated by a forward slash.
For many products, the SICK product ID is displayed as text and QR code on the type label and/or on the
packaging.




Figure 1: SICK product ID

Documentation and software
•    IODD: Device description file
•    IODD overview: List of IODD contents
•    IO-Link description: Detailed description of the process, service data and events of the IO-Link device
•    SOPAS ET: Configuration software as a free download
•    The documentation for SOPAS ET is stored in the system folder on your computer with the download:
     C:\Program Files (x86)\SOPAS ET\help
•    Visualization file (SDD = SOPAS Device Description) for operation via SOPAS ET.
•    Function Block Factory

IO-Link products can be easily connected to a computer via USB using the SiLink master. You can quickly and easily
test or parameterize the connected products using the SOPAS ET (SICK Engineering Tool with graphic user navigation
and convenient visualization).

Accessories
•    IO-Link master
•    SiLink2 Master, www.sick.com/1061790
•    Connecting cables




6        T E C H N I C A L I N F O R M A T I O N | CSS/CSX                                        9405579/2024-07-30 | SICK
                                                                                                Subject to change without notice

PHYSICAL LAYER 4


4                     Physical layer
The device data is automatically communicated to the IO-Link Master . It is important to ensure that the IO-Link
Master used supports this performance data.

NOTICE
The maximum current consumption of the IO-Link Device (including load at the outputs) must not exceed the
permissible output current of the respective port on the IO-Link Master .

Table 1: Physical layer – System data
 SIO Mode                                                  Yes
 Min. Cycle Time                                           1.8 ms
 Baud rate                                                 COM 3 (230.4 kbit/s)
 Process Data Length PD In (from Device to Master)         12 bytes
 IODD Version                                              V1.0
 Supported IO-Link Version                                 1.1.0




9405579/2024-07-30 | SICK                                                         T E C H N I C A L I N F O R M A T I O N | CSS/CSX   7
Subject to change without notice

5 INTEGRATION OF THE SENSOR INTO THE CONTROL LEVEL


5                Integration of the sensor into the control level
Connecting the IO-Link device to the IO-Link Master
To operate the product in IO-Link mode, it must be connected to a suitable IO-Link Master. This is used for further
integration into the control system.

NOTE
The cable length between the IO-Link Master and IO-Link device: maximum 20 m.

To enable the IO-Link device to be taken into account in the automation structure, the device must be registered
by the IO-Link Master or PLC manufacturer via an engineering tool and the communication relationship must be
parameterized. The device description IODD can be used for this purpose. It contains information on identification,
device parameters, process and diagnostics data, communication properties, and more.
Download the IODD-File from www.sick.com or from the IODD-Finder of the IO-Link consortium (IODD finder). Make
sure you always use the latest IODD-File .

NOTE
After successful connection of the product to the IO-Link Master, the green (Power) LED flashes to indicate a
functioning IO-Link communication between the master and device.




8        T E C H N I C A L I N F O R M A T I O N | CSS/CSX                                          9405579/2024-07-30 | SICK
                                                                                                  Subject to change without notice

ACCESSORIES FOR VISUALIZATION, PARAMETERIZATION AND INTEGRATION 6


6                     Accessories for visualization, parameterization and integration
IO-Link products can be easily connected to a computer via USB using the SiLink Master. The connected products
can be tested or parameterized quickly and easily using the program SOPAS ET (SICK Engineering Tool with graphical
user guidance and convenient visualization).

The following IO-Link-specific information is available at www.sick.com:
•       SOPAS ET as a free download
•       Visualization file (SDD = SOPAS Device Description) for operation via SOPAS ET.
•       Overview of available IO-Link Master for the integration of IO-Link Devices.




9405579/2024-07-30 | SICK                                                          T E C H N I C A L I N F O R M A T I O N | CSS/CSX   9
Subject to change without notice

7 SETTING, CONFIGURATION AND INTEGRATION


7                Setting, configuration and integration
In addition to the manual setting on the device, the sensor can also be configured via IO-Link.
Configuration via the REST interface of the IO-Link Masters is also possible. Please read the operating instructions
for the IO-Link Masters.
A list of all functions that can be configured can be found in the IODD and the IO link overview.

Setting options
Setting via buttons (limited setting options if necessary)
Configuration via IO-Link
1.   Setting via SiLink2 Master (SOPAS ET)
2.   Setting via IO-Link Master (PLC)
     ° IO-Link Master from the PLC manufacturer
     ° IO-Link Master from third-party manufacturer (SICK), more manual effort
Integrating the IO-Link device into the PLC
To simplify programming in the PLC, device-specific function blocks can be generated via the Function Block
Factory.
Function blocks simplify acyclical communication (service data communication) between the PLC and IO-Link
Device and the interpretation of process data. They provide device parameters and correct device data types and
translate the parameters provided into indices and sub-indices.




10       T E C H N I C A L I N F O R M A T I O N | CSS/CSX                                            9405579/2024-07-30 | SICK
                                                                                                    Subject to change without notice

PROCESS DATA STRUCTURE 8


8                     Process data structure
Download the IODD-File from www.sick.com or from the IODD-Finder of the IO-Link consortium (IODD finder). Make
sure you always use the latest IODD-File .
Process data is transmitted cyclically. There is no confirmation of receipt.
The cycle time is set by the master, whereby the minimum cycle time of the sensor cannot be undercut.

NOTE
The service data (acyclic data) does not influence the cycle time.

Process data structure
Depending on the application requirements, the process data content can be changed via parameter index 120
(Process Data Select), see table 14.

Evaluation Mode (Default), Color Match Value (CMV) + Q1 ... Q4 + all Qint status
Index 120 = 0
Table 2: Process data structure - Evaluation Mode
     Byte number                   0             1   2             3       4              5   6             7             8             9            10         11
                                        CMV               CMV                   CMV                CMV                                                  QL
      Function Slot                                                                                                      Qint status
                                        QL4               QL3                   QL2                QL1                                             + diagnostics
       Data type                       Uint16            Uint16                Uint16             Uint16
                                                                                                                                     Bitmap
       CMV area                        0...999           0...999               0...999            0...999
                                                                                                                               see table 4, page 12

The CMV value shows the degree of match to the taught-in color. The sensitivity setting (switching threshold) refers
to the CMV value:
999 = full match
0 = no match

Measurement Mode, Lab / RGB measurement + Q1 ... Q4 + all Qint status
Index 120 = 1
2 options for the measurement mode when using ISDU 296:
a)      RGB = Receive signal of the red-green-blue channel
        Index 296 = 0 (default)
b)      Lab = standardized Lab color space, based on L = lightness, a = green/red scale, b = blue/yellow scale
        Index 296 = 1 (values in 1/100)
For interpretation of the data, see table 3 RGB: black: 0 - 0 - 0 / white: 255 - 255 - 255 / gloss: > 255
Lab color space: black: 0 - 0 - 0 / white: 100 - 0 - 0 / gloss: L-value > 100
The gloss level depends on the alignment angle of the sensor.
Table 3: Process data structure - Measurement Mode
     Byte number                   0             1   2             3       4              5   6             7             8             9            10         11
                                                                                                   CMV                                                  QL
      Function Slot                    Red / L       Green / a                 Blue / b                                  Qint status
                                                                                                   QL1                                             + diagnostics
       Data type                       INT16             INT16                 INT16              Uint16
      RGB range                    0...2551)                       0...2551)
                                                                                                                                       Bitmap
     Lab range in                                                                                 0...999
                               0...160.00/100            -128.00...+127.00/100                                                   table 4 and table 5
       1/100
1)   With gloss or mirroring, the value rises above 255 up to the maximum value of the data type.


9405579/2024-07-30 | SICK                                                                                   T E C H N I C A L I N F O R M A T I O N | CSS/CSX        11
Subject to change without notice

8 PROCESS DATA STRUCTURE




                                                                                             Figure 3: RGB color space




Figure 2: Lab color space
Table 4: Status - Qint
 Byte number                                               Byte 8                                                        Byte 9
     Bit offset         31         30         29         28     27     26     25       24       23    22     21     20       19         18        17        16
                       Qint       Qint       Qint       Qint    Qint   Qint   Qint    Qint     Qint   Qint   Qint   Qint     Qint      Qint      Qint      Qint
      Bitmap
                       24         23         22         21      20     19     18      17       16     15     14     13       12        11        10         9
                                                                                     0 = False/OFF
      States
                                                                                      1 = True/ON

Table 5: Status - QL + Diagnostics + Qint
 Byte number                                              Byte 10                                                    Byte 11
     Bit offset         15         14         13         12     11     10      9       8        7      6      5      4        3          2         1         0
                                                                                                          PD        QoR
                       Qint       Qint       Qint       Qint    Qint   Qint   Qint    Qint     Rese Rese
      Bitmap                                                                                             inva‐      Alar     QL4       QL3       QL2       QL1
                        8          7          6          5       4      3      2       1       rved rved
                                                                                                          lid        m
                                                                                     0 = False/OFF
      States
                                                                                      1 = True/ON

QL output: physically available on connector pins (number of physical QLs depending on model)
Qint output: only available via IO-Link process data




12          T E C H N I C A L I N F O R M A T I O N | CSS/CSX                                                                         9405579/2024-07-30 | SICK
                                                                                                                                    Subject to change without notice

SERVICE DATA 9


9                     Service data
Service data is only exchanged between the controller and the IO-Link device via the IO-Link master on request
from the controller (acyclical). The service data is referred to as ISDUs. With ISDU, users can read information
about the status of the connected IO-Link device and/or write new parameters to change the configuration.
The corresponding counterpart confirms receipt of the data.
If the IO-Link device does not respond within five seconds, the master reports a communication error.

9.1                   Device identification
System
Table 6: Device identification
 ISDU
                                                                                  Data
                                                                         Data
 Index                             Sub-      Name                                 reposi‐   Length         Access          Default value
                                                                         type
                                   Index                                          tory
 DEC              HEX
 16               0x10                       Vendor Name                                    7 bytes                        SICK AG
                                                                                            64
 17               0x11                       Vendor text                                                                   www.sick.com
                                                                                            bytes
                                   -                                     String
                                                                                            18
 18               0x12                       Product Name                         -                        ro              CSS-XXXXXX
                                                                                            bytes
 19               0x13                       Product ID                                     9 bytes                        see ISDU 219
                                   0         Product ID                  Record             7 bytes
 219              0xDB
                                   1         Product ID IO-Link Device   String             7 bytes

Vendor Name                            Manufacturer name as UTF-8 string
Vendor text                            Manufacturer text as UTF-8 string
Product Name                           Complete type designation of the connected sensor as UTF-8 string
Product ID                             The Product ID is also the order number of the connected IO-Link device. The Product ID can
                                       be found under ISDU 219 in order to provide a family IODD for a device family.
Table 7: Device identification - Product Text / Serial Number
 ISDU
                                                                                  Data
                                                                         Data
 Index                             Sub-      Name                                 reposi‐   Length         Access          Default value
                                                                         type
                                   Index                                          tory
 DEC              HEX
                                                                                            64
 20               0x14                       Product Text                                                                  Color Sensor
                                   -                                     String   -         bytes          ro
 21               0x15                       Serial number                                  8 bytes                        YYWWnnnn

Format of the serial number:
YYWWnnnn (Y = year, W = week, n = sequential numbering)

Version
Table 8: Device identification - Version
 ISDU
                                                                                  Data
                                                                         Data
 Index                             Sub-      Name                                 reposi‐   Length         Access          Default value
                                                                         type
                                   Index                                          tory
 DEC              HEX
                                                                                            12
 22               0x16             -         Hardware version            String   -                        ro              Xnnn
                                                                                            bytes
                                                                                            12
 23               0x17             -         Firmware version            String   -                        ro              n.n.n.nnn.X.
                                                                                            bytes



9405579/2024-07-30 | SICK                                                                           T E C H N I C A L I N F O R M A T I O N | CSS/CSX   13
Subject to change without notice

9 SERVICE DATA

These ISDUs display hardware and software versions.
n = consecutive numbering
Hardware version: X = letter with 3-digit number (UTF-8 string)
Software version: 5-digit with extension identifier, with dot separation (UTF-8 string)

User-specific entries
Table 9: Device identification - Specific tag
ISDU
                                                                        Data
                                                               Data
Index                      Sub-         Name                            reposi‐   Length Access Default value Value/range
                                                               type
                           index                                        tory
DEC         HEX
                                        Application-specific
24          0x18           -                                            yes       32              *******
                                        tag                    String                      rw
                                                                                  bytes
64          0x40           -            Device-specific tag             no                        *******

You can save any text with a maximum length of 32 characters at Application-specific tag . This can be useful for
describing the exact position or task of the sensor in the overall machine. The Application-specific tag is saved via
the Data repository .
You can also save any text with a maximum length of 32 characters at Device-specific tag . This indicator is NOT
saved in the Data repository and is therefore available for information that is temporary or only valid on the specific
device for which it was defined.

NOTE
The user can enter any UTF-8 character


9.2               General device settings
Overview of all standard commands
Standardized teach-in commands and reset commands can be sent via the Standard Command .
Table 10: General device settings - Standard Commands
ISDU
                                                                        Data
                                                               Data                               Default
Index                      Sub- Name                                    reposi‐   Length Access             Value/range
                                                               type                               value
                           Index                                        tory
DEC         HEX
                                                                                                            Teach-in commands
                                                                                                            65 = Single value Teach
                                                                                                            71 = Start multi value teach
                                                                                                            72 = Stop multi value teach
                                                                                                            79 = Abort teach-in sequence
                                                                                                            220 = Remove Teach Object
2           0x02           -            Standard command       UInt     -         8 bits   wo
                                                                                                            Reset Commands:
                                                                                                            128 = Device Reset
                                                                                                            129 = Application Reset
                                                                                                            130 = Restore factory settings
                                                                                                            228 = Reset diagnostic parame‐
                                                                                                            ters

Teach-in commands                                     For details on Teach-in Commands, see table 32
Reset Commands                                        For details on Reset Commands, see table 11




14        T E C H N I C A L I N F O R M A T I O N | CSS/CSX                                                            9405579/2024-07-30 | SICK
                                                                                                                     Subject to change without notice

SERVICE DATA 9


Reset
Table 11: General device settings - Restore Factory Settings
 ISDU
                                                                Data
                                                         Data                             Default
 Index                         Sub- Name                        reposi‐   Length Access                  Value/range
                                                         type                             value
                               index                            tory
 DEC            HEX
                                                                                                         128 = Device Reset
                                                                                                         129 = Application Reset
 2              0x02           -   Standard command      UInt   -         8 bits   wo                    130 = Restore Factory Settings
                                                                                                         228 = Reset diagnostic parame‐
                                                                                                         ters

Device reset                                 The sensor performs a restart.
Application Reset                            Reset all application-relevant parameters.
Restore factory settings                     The sensor is reset to factory settings.
Reset diagnostic parameters                  Resetting the diagnostic key figures (minimum & maximum temperature (ISDU
                                             153/4,153/5), operating hours counter (ISDU 190/2).

Locking functions
Table 12: General device settings - Device Access Locks
 ISDU
                                                                Data
                                                         Data                             Default
 Index                         Sub- Name                        reposi‐   Length Access                  Value/range
                                                         type                             value
                               Index                            tory
 DEC            HEX
                                                                                                         0 = Data Storage & LocalUserIn‐
                                                                                                         terface available
                                   Device access locks                                                   2 = Data Storage locked
 12             0x0C           -                         Record yes       2 bytes rw      0
                                   (Key lock)                                                            8 = Local User Interface locked
                                                                                                         10 = Data Storage & LocalUserIn‐
                                                                                                         terface locked

Various functions of a sensor can be locked or unlocked with Device Access Locks .
Bit 1 = Data Storage
Bit 3 = Key Lock
 0 0 0 0 0 0 0 0                         0 0 0 0 0 0 0 1
Bit 15                                  Bit 7       Bit 0
0 dec = Data Storage & LocalUserInterface available: Data storage and key lock enabled
2 dec = Data Storage locked: Data storage blocked
8 dec = Local User Interface locked: Key lock disabled
10 dec = Data Storage & LocalUserInterface locked: Data storage and control panel locked
Table 13: General device settings - Key Lock Type
 ISDU
                                                                Data
                                                         Data                             Default
 Index                         Sub- Name                        reposi‐   Length Access                  Value/rangeT
                                                         type                             value
                               Index                            tory
 DEC            HEX
                                                                                                         0 = Interface fully locked
 160            0xA0           -   Key Lock Type         UInt   yes       1 byte   rw     0              1 = Teach-in available
                                                                                                         2 = reserved

The Key Lock Type defines the available configuration options for the operating elements when the key lock is active:
0 = Interface fully locked: completely blocked
1 = Teach-in available: Teach-in available



9405579/2024-07-30 | SICK                                                                 T E C H N I C A L I N F O R M A T I O N | CSS/CSX   15
Subject to change without notice

9 SERVICE DATA

Process data
Table 14: General device settings - Process data select
ISDU
                                                                      Data
                                                              Data                              Default
Index                      Sub- Name                                  reposi‐   Length Access             Value/range
                                                              type                              value
                           Index                                      tory
Dec        Hex
                                                                                                          0 = Evaluation Mode
120        0x78            -            Process data select   UInt    yes       1 byte   rw     0
                                                                                                          1 = Measurement Mode

The process data content that the sensor is to output cyclically can be determined via Process data select .
Evaluation Modeoutput of the CMV values (color match)
Measurement Mode: Measured value output of the current color
Table 15: Installation/Diagnostics - Measurement Color Space
ISDU
                                                                      Data
                                                              Data                              Default
Index                      Sub-         Name                          reposi‐   Length Access             Value/range
                                                              type                              value
                           Index                                      tory
DEC        HEX
                                        Measurement Color                                                 0 = RGB
296        0x128           -                                  UInt    yes       1 byte   rw
                                        Space                                                             1 = LAB

Setting the type of color measurement value - applies to the setting Measurement Mode in ISDU 120 (for details see
section 8).
Table 16: Installation/Diagnostics - Process Data Input / Output
ISDU
                                                                      Data
                                                              Data                              Default
Index                      Sub-         Name                          reposi‐   Length Access             Value/range
                                                              type                              value
                           Index                                      tory
DEC        HEX
                                                                                12
40         0x28            Process Data Input                 PD in   -                  ro     -         Referring to Process Data PD-in
                                                                                bytes

With the ISDU 40, the process data can be queried acyclically.

Device configuration
Table 17: General device settings - Sender configuration
ISDU
                                                                      Data
                                                              Data                              Default
Index                      Sub- Name                                  reposi‐   Length Access             Value/range
                                                              type                              value
                           Index                                      tory
DEC        HEX
                                                                                                          0 = Sender active
97         0x61            -            Sender configuration Uint     -         1 byte   rw     0
                                                                                                          1 = Sender not active

This ISDU can be used to switch off the Send LED.
If the transmitter is deactivated, PD invalid is output (process data invalid), all other values are 0.




16        T E C H N I C A L I N F O R M A T I O N | CSS/CSX                                                           9405579/2024-07-30 | SICK
                                                                                                                    Subject to change without notice

SERVICE DATA 9


Table 18: General device settings - Pin 2 configuration
 ISDU
                                                                   Data
                                                            Data                             Default
 Index                         Sub-    Name                        Reposi‐   Length Access                  Value/range
                                                            type                             value
                               Index                               tory
 DEC            HEX
                                                                                                            0 = Deactivated
                                                                                                            1 = External input (Smart Task)
                                                                                                            20 = Blanking
                                                                                                            34 = Switching output QL2
 121            0x79           -       Pin2 configuration   Uint   yes       1 byte   rw     39
                                                                                                            39 = Switching output QL1
                                                                                                            80 = Single value teach QL1
                                                                                                            81 = Single value teach QL2
                                                                                                            90 = Activate job bank (LSB)

Pin 2 in the device connector plug (or white wire if connecting cable is used) can be assigned various output
functions via Pin 2 configuration .
Deactivated                           The signal level at pin 2 is not evaluated.
External input (Smart Task)           Input function for "Smart Task" control
Blanking                              Blanking
                                      During blanking, all values in the process data remain frozen.
Switching output QL2 + Switching out‐ Digital outputs for QL1 + QL2
put QL1
Single value teach QL1 + Single value Single teach-in for QL1 + QL2
teach QL2
Activate job bank (LSB)               Activation of a job bank (LSB)

NOTE
With the 8-pin variant, the function of pin 1 is configured with ISDU 122.

Table 19: General device settings - Pin 5 configuration
 ISDU
                                                            Data   Data                      Default
 Index                         Sub- Name                                     Length Access                  Value/Range
                                                            type   storage                   value
 DEC            HEX            index
                                                                                                            0 = Deactived
                                                                                                            1 = External input (Smart Task)
                                                                                                            20 = Blanking
 122            0x7A           -       Pin5 configuration   Uint   no        8 bits   rw     1
                                                                                                            80 = Single value teach QL1
                                                                                                            81 = Single value teach QL2
                                                                                                            90 = Activate job bank (MSB)

Configuration of the MF input on pin 5:
Deactivated                           Signal level at pin 5 is not evaluated.
External input (Smart Task)           Input function for "Smart Task" control
Blanking                              During blanking, all values in the process data remain frozen.
Single value teach QL1 + Single value Single teach-in for QL1 + QL2
teach QL2
Activate job bank (MSB)               Activation of a job bank (MSB)




9405579/2024-07-30 | SICK                                                                    T E C H N I C A L I N F O R M A T I O N | CSS/CSX   17
Subject to change without notice

9 SERVICE DATA

Device search
Table 20: Device identification - Find me
ISDU
                                                                       Data
                                                              Data                               Default
Index                      Sub- Name                                   reposi‐   Length Access             Value/range
                                                              type                               value
                           Index                                       tory
DEC        HEX
                                                                                                           0 = Find Me deactivated
204        0xCC            -            Find me               UInt     no        8 bits    rw    0         1 = Find Me activated, yellow LED
                                                                                                           blinks with 1Hz

A connected sensor can be clearly identified via Find me . For machines with several identical sensors, it is
therefore possible to uniquely identify the device with which communication is currently taking place.
When Find me is activated, the yellow LED of the sensor flashes at 1 Hz.

Event configuration
Table 21: General device settings - Notification Handling
ISDU
                                                                       Data
                                                              Data                               Default
Index                      Sub- Name                                   reposi‐   Length Access             Value/range
                                                              type                               value
                           index                                       tory
DEC        HEX
                                                                                                           0 = All enabled
                                                                                                           1 = All disabled
                                                                                                           2 = Events enabled, PD invalid
227        0xE3            -            Notification Handling Uint     yes       1 byte    rw    0
                                                                                                           flag disabled
                                                                                                           3 = Events disabled, PD invalid
                                                                                                           flag enabled

In Notification handling , the generation of IO-Link events and the invalidity flag (status byte: bit 5 (table 5)) of the
process date can be activated / deactivated in the sensor.

Display configuration
Table 22: General device settings - Display settings
ISDU
                                                                       Data
                                                              Data
Index                      Sub- Name                                   reposi‐   Length Access Default     Value/range
                                                              type
                           Index                                       tory
DEC        HEX
                                        Display settings      Record             2 bytes         -
                                                                                                           0 = OFF
                           1            Energy saving mode    UInt               8 bits          1
234        0xEA                                                        yes                 rw              1 = ON
                                                                                                           0 = Not turned
                           2            Turn display          UInt               8 bits          0
                                                                                                           1 = Turned

Energy saving mode                 When energy-saving mode is activated, the display is switched off 20 seconds after the last input.
                                   The display is reactivated by pressing any button.
Turn display                       Rotation of the display by 180°.

Device information
Table 23: Device information - Hardware Variant
ISDU
                                                                       Data
                                                              Data                               Default
Index                      Sub-         Name                           reposi‐   Length Access             Value/range
                                                              type                               value
                           Index                                       tory
DEC        HEX
                                                                                                           0 = Standard IO
440        0x1B8           -            Hardware Variant      UInt     -         1 byte    ro              1 = Advanced IO
                                                                                                           2 = RS-485


18        T E C H N I C A L I N F O R M A T I O N | CSS/CSX                                                            9405579/2024-07-30 | SICK
                                                                                                                     Subject to change without notice

SERVICE DATA 9


The hardware variant can be used to read out the interfaces of the connected variant:
0 = Standard IO (M12/5-pin with 2 x IO)
1 = Advanced IO (M12/8-pin with 5 x IO)
2 = RS-485 (M12/8-pin with RS485 + 3 x IO)
Table 24: Device identification - Device ID Setup
 ISDU
                                                                 Data
                                                        Data                                 Default
 Index                         Sub- Name                type
                                                                 reposi‐     Length Access
                                                                                             value
                                                                                                            Value/range
                               Index                             tory
 DEC            HEX
                                                                                             838926
 16000          0x3E80 -           Device ID Setup      UInt     -           4 bytes rw             8389262
                                                                                             2

The IO-Link Device ID can be selected here for initialization when establishing a connection.

9.3                   Teach-in/Detection settings
Operating settings
Table 25: Teach-in/detection - Operating Mode
 ISDU
                                                                 Data
                                                        Data                                 Default
 Index                         Sub- Name                         reposi‐     Length Access                  Value/range
                                                        type                                 value
                               Index                             tory
 DEC            HEX
                                                                                                            0 = Mark / Object positioning
                                                                                                            1 = Fast sorting
 110            0x6E           -   Operating Mode       UInt     yes         1 byte   rw     0
                                                                                                            2 = Object separation
                                                                                                            3 = Color verification

Selection of the preset that the sensor should use for color evaluation. This results in the type of evaluation (see
table 29) and the response time (see table 27).
 Mark / Object positioning                    Response time = no averaging
                                              CMV threshold = 900
                                              Output Mode = Standard
 Fast sorting                                 Response time = low averaging
                                              CMV threshold = 800
                                              Output Mode = Best Fit Mode
 Object separation                            Response time = high averaging
                                              CMV threshold = 800
                                              Output Mode = Best Fit Mode
 Color verification                           Response time = highest averaging
                                              CMV threshold = 950
                                              Output Mode = Standard

Table 26: Teach-in/detection - Currently selected operating mode
 ISDU
                                                                 Data
                                                        Data                                 Default
 Index                         Sub- Name                         reposi‐     Length Access                  Value/range
                                                        type                                 value
                               Index                             tory
 DEC            HEX
                                                                                                            0 = Mark / Object positioning
                                                                                                            1 = Fast sorting
                                   Currently selected
 83             0x53           -                        UInt     -           1 byte   ro     0              2 = Object separation
                                   operating mode
                                                                                                            3 = Color verification
                                                                                                            255 = Manual setting

Read out the currently selected operating mode according to the setting in ISDU 110.



9405579/2024-07-30 | SICK                                                                    T E C H N I C A L I N F O R M A T I O N | CSS/CSX   19
Subject to change without notice

9 SERVICE DATA

Table 27: Teach-in/detection - Measurement averaging
ISDU
                                                                    Data
                                                             Data                              Default
Index                     Sub-         Name                         reposi‐   Length Access              Value/range
                                                             type                              value
                          Index                                     tory
DEC         HEX
                                                                                                         0 = No averaging
                                                                                                         1 = Low averaging
                                       Measurement aver‐
89          0x59          0                                  UInt   yes       8 bits   rw      0         2 = Medium averaging
                                       aging
                                                                                                         3 = High averaging values
                                                                                                         4 = Highest averaging

The filtering of the measured value can be set via Measurement averaging . The more values are included in the
calculation, the lower the noise of the signal. However, this is at the expense of the sensor's response (latency).
Table 28: Response times CSS HighSpeed versus HighResolution
CSS HighSpeed                                                             CSS HighResolution
0 = 36 μs                                                                 0 = 120 μs
1 = 72 μs                                                                 1 = 1 ms
2 = 150 μs                                                                2 = 7.7 ms
3 = 300 μs                                                                3 = 62 ms
4 = 600 μs                                                                4 = 500 ms

Table 29: Output Mode
ISDU
                                                                    Data
                                                             Data                              Default
Index                     Sub- Name                                 reposi‐   Length Access              Value/range
                                                             type                              value
                          index                                     tory
DEC         HEX
                                                                                                         0 = Standard
293         0x125         -            Output Mode           UInt   yes       8 bits   rw      0         1 = Best Fit Mode
                                                                                                         2 = Coded Mode

Output Mode:
Standard: each output switches according to its individual setting (teach-in and sensitivity).
Best Fit Mode: only one output (Qint) is active if several colors are taught in. The quint with the closest match to the
currently measured color is set as active.
Color Mode: such as Best Fit Mode. In addition, the number of the active Qint is output as a binary code on the QLs.
Table 30: Sensing Distance Compensation
ISDU
                                                                    Data
                                                             Data                              Default
Index                     Sub- Name                                 reposi‐   Length Access              Value/range
                                                             type                              value
                          index                                     tory
DEC         HEX
                                                                                                         0 = Deactivated
294         0x126         -            Distance regulation   UInt   yes       8 bits   rw      1
                                                                                                         1 = Activated

Distance regulation: Sensing range compensation (only for High Resolution models)
Table 31: Color Mode
ISDU
                                                                    Data
                                                             Data                              Default
Index                     Sub- Name                                 reposi‐   Length Access              Value/range
                                                             type                              value
                          index                                     tory
DEC         HEX
                                                                                                         0 = C + I mode
295         0x127         -            Color Mode            UInt   yes       8 bits   rw      0
                                                                                                         1 = C mode

C + I mode: both the color and its intensity are considered here
C modeevaluation of the color without its intensity (no gray levels distinguishable)


20       T E C H N I C A L I N F O R M A T I O N | CSS/CSX                                                           9405579/2024-07-30 | SICK
                                                                                                                   Subject to change without notice

SERVICE DATA 9


Teach-in
Table 32: Teach-in/detection - Teach-in Commands
 ISDU
                                                                     Data
                                                            Data                                  Default
 Index                         Sub- Name                             reposi‐     Length Access                   Value/range
                                                            type                                  value
                               index                                 tory
 DEC            HEX
                                                                                                                 65 = Single Value Teach-in
                                                                                                                 71 = Start Multi Value Teach
 2              0x02           -       Standard command     UInt     -           8 bits     wo                   72 = Stop Multi Value Teach
                                                                                                                 79 = Abort Teach-in sequence
                                                                                                                 220 = Remove Teach Object

The selection of the Qint for which the teach-in is to be carried out is determined via ISDU 58 (Teach-in channel).
 Single Value Teach-in             Static teach-in of a color using Single Value Teach-in
 Start Multi Value Teach-in        This function can be used to teach in the color to be detected while the process is running. To do
 + Stop Multi Value Teach-         this, the teach-in process is started by writing the value 71. From this point on, the sensor records
 in                                the color values and interprets them. Write the value 72 to end the dynamic teach-in process.
 Abort Teach-in sequence           Writing the value 79 interrupts a running teach-in process (Multi Value Teach-in).
 Remove Teach Object               Deletes the teach-in values of the currently selected Qint / Teach-in channel (ISDU 58).

Table 33: Teach-in/detection - Teach-in channel / Teach state
 ISDU
                                                                     Data
                                                            Data                                  Default
 Index                         Sub-    Name                          reposi‐     Length Access                   Value/range
                                                            type                                  value
                               Index                                 tory
 DEC            HEX
                                                                                                                 0 = Qint.1
                                                                                                                 1 = Qint.2
 58             0x3A           -       Teach-in channel     UInt     -           1 byte     rw    0              2 = Qint.3
                                                                                                                 ...
                                                                                                                 23 = Qint.24
                                                                                                                 0 = Idle
                                                                                                                 3 = SP12 success
 59             0x3B           -       Teach-in status      UInt     -           1 byte     ro    0              4 = Wait for command
                                                                                                                 5 = Busy
                                                                                                                 7 = Error

Selection of the Qint switching output for the next teach-in via the system command.
The Teach-in status shows the current status of the teach-in process.
A teach-in can only be sent in the status Idle and Error .
The status always refers to the Qint. channel currently selected in Teach-in channel (ISDU 58).
Table 34: Teach-in/detection - Quality of Teach
 ISDU
                                                                     Data
                                                            Data                                  Default
 Index                         Sub-    Name                          reposi‐     Length Access                   Value/range
                                                            type                                  value
                               Index                                 tory
 DEC            HEX
 114            0x72           -       Quality of Teach     UInt     -           1 byte     ro    -              0 ... 100 [in %]

The teach-in quality depends on the teach-in type:
•       Single value teach-inalways 100%
•       Multi value teach-indecreasing value with increasing distribution of the taught-in color spectrum




9405579/2024-07-30 | SICK                                                                         T E C H N I C A L I N F O R M A T I O N | CSS/CSX   21
Subject to change without notice

9 SERVICE DATA

Quality of Run
Table 35: Teach-in - Quality of Run
ISDU
                                                                                              Le
                                                                      Data         Data                  Default
Index                      Sub- Name                                                          ngt Access               Value/Range
                                                                      type         storage               value
                           index                                                              h
DEC         HEX
                                                                                              1b
175         0xAF                        Quality of Run                UInt         yes            rw      0            0 ... 100
                                                                                              yte

Quality of Run shows the process quality resulting from the current measured color value in relation to the set
sensitivity and the maximum CMV value 999. Value in %.
ISDU 297 (see table 37) specifies this value specifically for each taught-in color. ISDU 175 outputs the minimum
of all quality values as the worst-case scenario.
Table 36: Teach-in - Quality of run alarm, switching threshold
ISDU
                                                                   Data      Data                         Default
Index                      Sub- Name                               type      storage
                                                                                         Length Access
                                                                                                          value
                                                                                                                       Value/Range
DEC         HEX            index
176         0xB0           Quality of run alarm threshold Uint               yes         1 byte   rw      50           0 ... 90

Alarm threshold for the process quality (ISDU 175) - if the value falls below the set value, a status bit (see table 5)
is set and an IO-Link event (see table 60) is output. Value in %.
Table 37: Quality Levels
ISDU
                                                                             Data
                                                                   Data                                   Default
Index                      Sub- Name                                         reposi‐     Length Access                 Value/range
                                                                   type                                   value
                           index                                             tory
DEC         HEX
                                                                   Array
                                                                                         24
297         0x129          -            Quality Levels             24 x      -                    ro
                                                                                         bytes
                                                                   UINT8

Quality Levels shows the process quality of all 24 color banks.

Teach-in data 1 to 24
Here are the teach-in data for the associated Qint. Outputs are stored.
The teach-in data contains all relevant information on the colors stored in each case. This means that each
taught-in color can be transferred to another sensor, for example.
Table 38: Teach-in data - Qint.
ISDU
                                                                                    Data
                                                                          Data                                          Default
Index                              Sub- Name                                        reposi‐    Length         Access                  Value/range
                                                                          type                                          value
                                   Index                                            tory
DEC            HEX
                                                Qint. teach data          Record               44 bytes




22        T E C H N I C A L I N F O R M A T I O N | CSS/CSX                                                                          9405579/2024-07-30 | SICK
                                                                                                                                   Subject to change without notice

SERVICE DATA 9


 ISDU
                                                                       Data
                                                               Data                                         Default
 Index                             Sub- Name                           reposi‐   Length       Access                        Value/range
                                                               type                                         value
                                   Index                               tory
 DEC               HEX
 60                0x3C            1    Nucleus L              Float   yes       4 bytes      rw
 62                0x3E            2    Nucleus a              Float   yes       4 bytes      rw
 16384             0x4000
 16386             0x4002          3    Nucleus b              Float   yes       4 bytes      rw
 16388             0x4004          4    Rotation L             Float   yes       4 bytes      rw
 16390             0x4006          5    Rotation a             Float   yes       4 bytes      rw
 16392             0x4008
 16394                             6    Rotation b             Float   yes       4 bytes      rw
                   0x400A
 16396             0x400C          7    Extent L               Float   yes       4 bytes      rw
 16398             0x400E          8    Extent A               Float   yes       4 bytes      rw
 16400             0x4010
 16402             0x4012          9    Extent B               Float   yes       4 bytes      rw
 16404             0x4014               Application Hystere‐
                                   10                          UInt    yes       2 bytes      rw
 16406             0x4016               sis R
 16408             0x4018               Application Hystere‐
 16410             0x401A          11                          UInt    yes       2 bytes      rw
                                        sis G
 16412             0x401C
                                        Application Hystere‐
 16414             0x401E          12                          UInt    yes       2 bytes      rw
                                        sis B
 16416             0x4020
 16418             0x4022
 16420             0x4024
 16422             0x4026          13   Signal Damping         UInt    yes       2 bytes      rw
 16424             0x4028
 16426             0x402A

Qint. teach data for Qint. 1 to Qint. 24:
ISDU 60 = Qint. 1 teach data
ISDU 62 = Qint. 2 teach data
ISDU 16384 = Qint. 3 teach data
...
ISDU 16426 = Qint. 24 teach data
Nucleus: Describes the center point of the teach-in object as a LAB triple
Rotation: Describes the rotation of the extension of the teach-in object around the core as a LAB vector
Extent: Describes the extent of the rotated teach-in object as a 3D vector
Application Hysteresis: Describes the signal noise measured during teach-in
Signal Damping: Selected signal attenuation for teach-in objects




9405579/2024-07-30 | SICK                                                                  T E C H N I C A L I N F O R M A T I O N | CSS/CSX   23
Subject to change without notice

9 SERVICE DATA




Figure 4: Signal noise
Table 39: Teach-in data - Qint.
 ISDU
                                                                               Data
                                                                      Data                                  Default
 Index                             Sub- Name                                   reposi‐   Length    Access                Value/range
                                                                      type                                  value
                                   Index                                       tory
 DEC           HEX
                                                Qint. configuration   Record             3 bytes
 61            0x3C                             Referenced Teach
                                   1                                  UInt     yes       1 byte    rw       0            0 ... 31
 63            0x3E                             Object
 16385         0x4000
 16387         0x4002
 16389         0x4004
 16391         0x4006
 16393         0x4008
 16395         0x400A
 16397         0x400C
 16399         0x400E
 16401         0x4010
 16403         0x4012
 16405         0x4014
 16407         0x4016              2            Sensitivity           UInt     yes       2 bytes   rw       900          0 ... 999
 16409         0x4018
 16411         0x401A
 16413         0x401C
 16415         0x401E
 16417         0x4020
 16419         0x4022
 16421         0x4024
 16423         0x4026
 16425         0x4028
 16427         0x402A

Qint. configuration for Qint. 1 to Qint. 24:
ISDU 61 = Qint. 1 configuration
ISDU 63 = Qint. 2 configuration
ISDU 16385 = Qint. 3 configuration
...

24        T E C H N I C A L I N F O R M A T I O N | CSS/CSX                                                             9405579/2024-07-30 | SICK
                                                                                                                      Subject to change without notice

SERVICE DATA 9


ISDU 16427 = Qint. 24 configuration
Referenced Teach Object: Assignment of the sensitivity threshold for the associated teach-in object.
Sensitivity: Sensitivity value in relation to the degree of match (CMV), determines the color match at which the
respective Qint switches
•       0 = no match (Qint always ON)
•       999 = full match
Table 40: Teach-in / Names of Qint.
 ISDU
                                                                   Data
                                                          Data                               Default
 Index                         Sub- Name                  type
                                                                   reposi‐   Length Access
                                                                                             value
                                                                                                            Value/range
                               Index                               tory
 DEC            HEX
                                                                             192
                               -    Names Qint. 1 to 16   Record -                           -
                                                                             bytes
                                                                             12
                               1    Name Qint. 1          String   yes               rw
                                                                             bytes
                                                                             12
                               2    Name Qint. 2          String   yes               rw
                                                                             bytes
                                                                             12
                               3    Name Qint. 3          String   yes               rw
                                                                             bytes
                                                                             12
                               4    Name Qint. 4          String   yes               rw
                                                                             bytes
                                                                             12
                               5    Name Qint. 5          String   yes               rw
                                                                             bytes
                                                                             12
                               6    Name Qint. 6          String   yes               rw
                                                                             bytes
                                                                             12
                               7    Name Qint. 7          String   yes               rw
                                                                             bytes
                                                                             12
 4081           0xFF1          8    Name Qint. 8          String   yes               rw
                                                                             bytes
                                                                                                            Color 1 ... 16
                                                                             12
                               9    Name Qint. 9          String   yes               rw
                                                                             bytes
                                                                             12
                               10   Name Qint. 10         String   yes               rw
                                                                             bytes
                                                                             12
                               11   Name Qint. 11         String   yes               rw
                                                                             bytes
                                                                             12
                               12   Name Qint. 12         String   yes               rw
                                                                             bytes
                                                                             12
                               13   Name Qint. 13         String   yes               rw
                                                                             bytes
                                                                             12
                               14   Name Qint. 14         String   yes               rw
                                                                             bytes
                                                                             12
                               15   Name Qint. 15         String   yes               rw
                                                                             bytes
                                                                             12
                               16   Name Qint. 16         String   yes               rw
                                                                             bytes




9405579/2024-07-30 | SICK                                                                    T E C H N I C A L I N F O R M A T I O N | CSS/CSX   25
Subject to change without notice

9 SERVICE DATA

ISDU
                                                                     Data
                                                            Data                               Default
Index                    Sub- Name                                   reposi‐   Length Access             Value/range
                                                            type                               value
                         Index                                       tory
DEC      HEX
                                                                               96
                         -            Names Qint. 17 to 24 Record -                            -
                                                                               bytes
                                                                               12
                         1            Name Qint. 17         String   yes               rw
                                                                               bytes
                                                                               12
                         2            Name Qint. 18         String   yes               rw
                                                                               bytes
                                                                               12
                         3            Name Qint. 19         String   yes               rw
                                                                               bytes
                                      Name Teach Object                        12
4082     0xFF2           4                                  String   yes               rw
                                      20                                       bytes
                                                                                                         Color 17 ... 24
                                                                               12
                         5            Name Qint. 21         String   yes               rw
                                                                               bytes
                                                                               12
                         6            Name Qint. 22         String   yes               rw
                                                                               bytes
                                                                               12
                         7            Name Qint. 23         String   yes               rw
                                                                               bytes
                                                                               12
                         8            Name Qint. 24         String   yes               rw
                                                                               bytes

A name can be assigned to each teach-in object.




26      T E C H N I C A L I N F O R M A T I O N | CSS/CSX                                                            9405579/2024-07-30 | SICK
                                                                                                                   Subject to change without notice

SERVICE DATA 9


9.4                   Installation/Diagnostics
Reading all color match values (CMV)
Table 41: Installation/Diagnostics - Color Match Values
                    ISDU
                                                                              Data
                                                                    Data                                  Default
          Index                                     Name                     reposi‐   Length Access                               Value/range
                                   Sub-Index                        type                                   value
                                                                               tory
    DEC            HEX
                                                                                        48
                                       -       Color Match Values   Record                                     -                      0 ... 999
                                                                                       bytes
                               Byte 47-48           CMV 1            UInt       -      2 bytes   ro                                   0 ... 999
                               Byte 45-46           CMV 2            UInt       -      2 bytes   ro                                   0 ... 999
                               Byte 43-44           CMV 3            UInt       -      2 bytes   ro                                   0 ... 999
                               Byte 41-42           CMV 4            UInt       -      2 bytes   ro                                   0 ... 999
                               Byte 39-40           CMV 5            UInt       -      2 bytes   ro                                   0 ... 999
                               Byte 37-38           CMV 6            UInt       -      2 bytes   ro                                   0 ... 999
                               Byte 35-36           CMV 7            UInt       -      2 bytes   ro                                   0 ... 999
                               Byte 33-34           CMV 8            UInt       -      2 bytes   ro                                   0 ... 999
                               Byte 31-32           CMV 9            UInt       -      2 bytes   ro                                   0 ... 999
                               Byte 29-30           CMV 10           UInt       -      2 bytes   ro                                   0 ... 999
                               Byte 27-28           CMV 11           UInt       -      2 bytes   ro                                   0 ... 999
    165           0xA5
                               Byte 25-26           CMV 12           UInt       -      2 bytes   ro                                   0 ... 999
                               Byte 23-24           CMV 13           UInt       -      2 bytes   ro                                   0 ... 999
                               Byte 21-22           CMV 14           UInt       -      2 bytes   ro                                   0 ... 999
                               Byte 19-20           CMV 15           UInt       -      2 bytes   ro                                   0 ... 999
                               Byte 17-18           CMV 16           UInt       -      2 bytes   ro                                   0 ... 999
                               Byte 15-16           CMV 17           UInt       -      2 bytes   ro                                   0 ... 999
                               Byte 13-14           CMV 18           UInt       -      2 bytes   ro                                   0 ... 999
                               Byte 11-12           CMV 19           UInt       -      2 bytes   ro                                   0 ... 999
                                   Byte 9-10        CMV 20           UInt       -      2 bytes   ro                                   0 ... 999
                                   Byte 7-8         CMV 21           UInt       -      2 bytes   ro                                   0 ... 999
                                   Byte 5-6         CMV 22           UInt       -      2 bytes   ro                                   0 ... 999
                                   Byte 3-4         CMV 23           UInt       -      2 bytes   ro                                   0 ... 999
                                   Byte 1-2         CMV 24           UInt       -      2 bytes   ro                                   0 ... 999

The CMV shows the degree of compliance with the individual teach-in objects:
0 = no match
999 = full match




9405579/2024-07-30 | SICK                                                                         T E C H N I C A L I N F O R M A T I O N | CSS/CSX   27
Subject to change without notice

9 SERVICE DATA

System status
Table 42: Device State
 ISDU
                                                                         Data
                                                                 Data                              Default
 Index                       Sub- Name                                   reposi‐   Length Access             Value/range
                                                                 type                              value
                             Index                                       tory
 DEC         HEX
                                                                                                             0 = Device is OK
                                                                                                             1 = Maintenance required
 36          0x24            -            Device Status          Uint    -         1 byte    ro    0         2 = Out of specification1)
                                                                                                             3 = Functional check1)
                                                                                                             4 = Failure1)
1)    Not supported by the device

Device is OK: Device is in order
Maintenance required : Action required, e.g. teach-in
Out of specification: Out of specification, not supported by the device
Functional check: Function test, not supported by the device
Failure: Error status, not supported by the device
Table 43: Installation/Diagnostics - Device status
 ISDU
                                                                         Data
                                                                 Data                              Default
 Index                       Sub- Name                                   reposi‐   Length Access             Value/range
                                                                 type                              value
                             index                                       tory
 DEC         HEX
                                          Detailed device sta‐                     15
                                                                 Array                                       -
                                          tus                                      bytes
                                          Event 1                                  3 bytes                   0xE48CA4 = Warning appeared -
                                                                                                             Quality of run alarm
                                          Event 2                                  3 bytes
                                                                                                             0xE48CA0 = Warning appeared -
                                          Event 3                                  3 bytes                   Short circuit on output pin
                                          Event 4                                  3 bytes                   0xE48CA8 = Warning appeared
                                                                                                             - Alarm upper temperature thresh‐
 37          0x25            -                                           -                   ro    -         old
                                                                 -                                           0xE48CAB = Warning appeared
                                                                                                             - Alarm operating hours
                                                                                                             0xE48CAF = Warning appeared -
                                          Event 5                                  3 bytes                   Alarm lower temperature threshold
                                                                                                             0xF45000 = Error appeared -
                                                                                                             Device hardware fault
                                                                                                             0x000000 = no event
                                                                                                             appeared

The detailed Device Status shows up to 5 events of the warning and error type that are currently present. The
information is available as a data string of 5 x 3 bytes, in the order in which it occurs.
Byte 1: Event qualifier, section 11.1
Byte 2 + 3: Event code, section 11.2




28          T E C H N I C A L I N F O R M A T I O N | CSS/CSX                                                            9405579/2024-07-30 | SICK
                                                                                                                       Subject to change without notice

SERVICE DATA 9


Condition monitoring
Table 44: Installation/Diagnostics - Temperature
 ISDU
                                                                   Data
                                                          Data                               Default
 Index                         Sub- Name                           reposi‐   Length Access                  Value/range
                                                          type                               value
                               index                               tory
 DEC            HEX
                               0   Temperature            Record             5 bytes
                               1   Current temperature    INT                8 bits                         -127 ... 127 °C
                                   Max. temperature all
                               2                        INT                  8 bits                         -127 ... 127 °C
                                   time

 153            0x99               Min. temperature all            -                   ro    -
                               3                          INT                8 bits                         -127 ... 127 °C
                                   time
                                   Max. temperature
                               4                          INT                8 bits                         -127 ... 127 °C
                                   since last reset
                                   Min. temperature
                               5                          INT                8 bits                         -127 ... 127 °C
                                   since last reset

Read out the operating temperature of the sensor. The values of Max. temperature since last reset and Min. temperature
since last reset are deleted via the Standard command Reset diagnostic parameters (index 2, value 228).
Table 45: Installation/Diagnostics - Alarm thresholds for diagnostic parameters
 ISDU
                                                                   Data
                                                          Data                               Default
 Index                         Sub- Name                           reposi‐   Length Access                  Value/range
                                                          type                               value
                               Index                               tory
 DEC            HEX
                                   Alarm thresholds for
                                   diagnostic parame‐     Record             6 bytes         -
                                   ters                            yes
                                   Upper Temperature
                               1                          INT                1 byte          80
 179            0xB3               Threshold                                           rw
                                   Lower Temperature
                               2                          INT      yes       1 byte          -30
                                   Threshold
                                   Operating Hours
                               3                          INT      yes       4 bytes         40000
                                   Threshold

The Parameter Alarm threshold for diagnostic parameters offers the option of defining alarm thresholds for certain
diagnostic values provided by the device. If these alarm thresholds are exceeded or not reached, a corresponding
event is generated.
Table 46: Installation/Diagnostics - Operating hours
 ISDU
                                                                   Data
                                                          Data                               Default
 Index                         Sub- Name                           reposi‐   Length Access                  Value/range
                                                          type                               value
                               index                               tory
 DEC            HEX
                               0   Operating hours        Record             8 bytes
                                                                             32 bits
                                                                             (Off‐
                               1   Total operating hours UInt                                               0 ... 1000000
                                                                             set 32
 190            0xBE                                               -         bits)   ro      -
                                                                             32 bits
                                   Operating hours                           (Off‐
                               2                          UInt                                              0 ... 1000000
                                   since last reset                          set 0 b
                                                                             its)

The Total operating hours parameter displays how many total hours (h) the device has already been in operation. This
value cannot be reset.



9405579/2024-07-30 | SICK                                                                    T E C H N I C A L I N F O R M A T I O N | CSS/CSX   29
Subject to change without notice

9 SERVICE DATA

Parameter Operating hours since last reset displays how many hours (h) the device has been in operation since the
last reset of the diagnostic parameters. The diagnostic parameters are reset using the Reset diagnostic parameter
standard command (index 2, value 228).
Table 47: Teach-in/detection - Standard command
ISDU
                                                                           Data
                                                                  Data                                   Default
Index                         Sub- Name                           type
                                                                           reposi‐       Length Access
                                                                                                         value
                                                                                                                   Value/range
                              index                                        tory
DEC           HEX
                                                                                                                   228 = Reset diagnostic parame‐
2             0x02            -            Standard command       UInt     -             1 byte    wo    -
                                                                                                                   ter

Resetting the minimum and maximum temperature (ISDU 1534/4, 153/5) and the operating hours (ISDU 190/2)
since the last reset.
Table 48: Installation/Diagnostics - Distance to Object
               ISDU
                                                                                Data
                                                                   Data                                  Default
           Index                Sub-                Name                       reposi‐   Length Access                      Value/range
                                                                   type                                   value
                               Index                                             tory
     DEC           HEX
                                             Distance to Object   Record                 3 bytes
                                  1                Distance        UInt                  2 bytes                             0 ... 5000
     229         0xE5                                                             -                 ro       -      0 = Distance in range / valid
                                  2          Distance Qualifier    UInt                  1 byte                     3 = No distance information /
                                                                                                                          distance invalid

Distance information only available for the CSS High Resolution variants.
Distance: Unit = 1/10 mm, measured value only if available, otherwise the value is 0.
Distance Qualifier: 0 = distance value valid (within the working range matching the sensor), 3 = no distance
information available
Distance information for the CSS High Resolution variants.

9.5                  Smart Tasks
Smart Tasks process the various Smart Sensor signals for detection and measurement, linking them to binary
switching signals from an external sensor if necessary. These signals can be imported via pin 2 (see Pin 2
configuration, ISDU 121). The Smart Task uses this data to generate the requisite process information – tailored
to the task at hand in the plant. This saves time during data evaluation in the control, accelerates machine
processes, and makes high-performance, cost-intensive additional hardware unnecessary.
•     Decentralized signal analysis directly at the sensor
•     Faster signal capture and processing
•     Through Smart Tasks, Smart Sensors deliver the information that the plant process actually requires – no
      separate data preparation necessary in the control




30           T E C H N I C A L I N F O R M A T I O N | CSS/CSX                                                                9405579/2024-07-30 | SICK
                                                                                                                            Subject to change without notice

SERVICE DATA 9


9.5.1                 Smart Task A10
Table 49: Smart Task - Inverter Ext. input
 ISDU
                                                                   Data
                                                          Data                               Default
 Index                         Sub- Name                           reposi‐   Length Access                  Value/range
                                                          type                               value
                               Index                               tory
 DEC            HEX
                                                                                                            true = Inverted
                               -   Inverter Ext.input     Record yes         1 byte   rw
                                                                                                            false = Not inverted
                                   Inverter Ext.input 1                                                     true = Inverted
 1093           0x445          1                          UInt     yes       1 bit    rw     0
                                   (Pin 2 / Pin 1)                                                          false = Not inverted
                                   Inverter Ext.input 2                                                     true = Inverted
                               2                          UInt     yes       1 bit    rw     0
                                   (Pin 5)                                                                  false = Not inverted

The Inverter Ext. input function allows you to change the signal logic of a pin 2 / pin 5 configured as Ext. input .
The setting is made according to the bit pattern:
'00000000'
Bit 0 = Inverter external input 2 (pin 5), default = 0
Bit 1 = Inverter external input 1 (pin 2), default = 0

NOTE
Pin 2 applies to the 5-pin version. In the 8-pin version, this is pin 1.

Table 50: Smart Task - SLTI Version
 ISDU
                                                                   Data
                                                          Data                               Default
 Index                         Sub- Name                           reposi‐   Length Access                  Value/range
                                                          type                               value
                               Index                               tory
 DEC            HEX
 1208           0x4B8          -   SLTI Version           String   -         8 bytes ro      1.1.0

The version identifier can be read out with the ISDU 1208.
The SLTI version contains the version number of the Smart Task basic logic.
1.1.0: 3-digit version identifier, with dot separation (UTF-8 string)
Table 51: Smart Task - Input Selector
 ISDU
                                                                   Data
                                                          Data                               Default
 Index                         Sub- Name                           reposi‐   Length Access                  Value/range
                                                          type                               value
                               Index                               tory
 DEC            HEX
                               -   Input Selector 1 ... 4 Record yes         4 bytes rw
                                                                                                            true = Qint.1 selected
                               1   Qint. 1                UInt     yes       1 bit    rw     1
                                                                                                            false = Qint.1 not selected
                                                                                                            true = Qint.2 selected
                               2   Qint. 2                UInt     yes       1 bit    rw     0
                                                                                                            false = Qint.2 not selected
 1209           0x4B9                                                                                       true = Qint.3 selected
                               3   Qint. 3                UInt     yes       1 bit    rw     0
 1214           0x4BE                                                                                       false = Qint.3 not selected
 1219           0x4C3                                                                                       true = Qint.4 selected
 1224           0x4C8          4   Qint. 4                UInt     yes       1 bit    rw     0
                                                                                                            false = Qint.4 not selected
                                                                                                            true = Qint.5 selected
                               5   Qint. 5                UInt     yes       1 bit    rw     0
                                                                                                            false = Qint.5 not selected
                                                                                                            true = Qint.6 selected
                               6   Qint. 6                UInt     yes       1 bit    rw     0
                                                                                                            false = Qint.6 not selected
                               7   Qint. 7                UInt     yes       1 bit    rw     0              true = Qint.7 selected


9405579/2024-07-30 | SICK                                                                    T E C H N I C A L I N F O R M A T I O N | CSS/CSX   31
Subject to change without notice

9 SERVICE DATA

ISDU
                                                                   Data
                                                            Data                              Default
Index                    Sub- Name                                 reposi‐    Length Access             Value/range
                                                            type                              value
                         Index                                     tory
DEC       HEX
                                                                                                        false = Qint.7 not selected
                                                                                                        true = Qint.8 selected
                         8            Qint. 8               UInt   yes        1 bit   rw      0
                                                                                                        false = Qint.8 not selected
                                                                                                        true = Qint.9 selected
                         9            Qint. 9               UInt   yes        1 bit   rw      0
                                                                                                        false = Qint.9 not selected
                                                                                                        true = Qint.10 selected
                         10           Qint. 10              UInt   yes        1 bit   rw      0
                                                                                                        false = Qint.10 not selected
                                                                                                        true = Qint.11 selected
                         11           Qint. 11              UInt   yes        1 bit   rw      0
                                                                                                        false = Qint.11 not selected
                                                                                                        true = Qint.12 selected
                         12           Qint. 12              UInt   yes        1 bit   rw      0
                                                                                                        false = Qint.12 not selected
                                                                                                        true = Qint.13 selected
                         13           Qint. 13              UInt   yes        1 bit   rw      0
                                                                                                        false = Qint.13 not selected
                                                                                                        true = Qint.14 selected
                         14           Qint. 14              UInt   yes        1 bit   rw      0
                                                                                                        false = Qint.14 not selected
                                                                                                        true = Qint.15 selected
                         15           Qint. 15              UInt   yes        1 bit   rw      0
                                                                                                        false = Qint.15 not selected
                                                                                                        true = Qint.16 selected
                         16           Qint. 16              UInt   yes        1 bit   rw      0
                                                                                                        false = Qint.16 not selected
                                                                                                        true = Qint.17 selected
                         17           Qint. 17              UInt   yes        1 bit   rw      0
                                                                                                        false = Qint.17 not selected
                                                                                                        true = Qint.18 selected
                         18           Qint. 18              UInt   yes        1 bit   rw      0
                                                                                                        false = Qint.18 not selected
                                                                                                        true = Qint.19 selected
                         19           Qint. 19              UInt   yes        1 bit   rw      0
                                                                                                        false = Qint.19 not selected
                                                                                                        true = Qint.20 selected
                         20           Qint. 20              UInt   yes        1 bit   rw      0
                                                                                                        false = Qint.20 not selected
                                                                                                        true = Qint.21 selected
                         21           Qint. 21              UInt   yes        1 bit   rw      0
                                                                                                        false = Qint.21 not selected
                                                                                                        true = Qint.22 selected
                         22           Qint. 22              UInt   yes        1 bit   rw      0
                                                                                                        false = Qint.22 not selected
                                                                                                        true = Qint.23 selected
                         23           Qint. 23              UInt   yes        1 bit   rw      0
                                                                                                        false = Qint.23 not selected
                                                                                                        true = Qint.24 selected
                         24           Qint. 24              UInt   yes        1 bit   rw      0
                                                                                                        false = Qint.24 not selected
                                                                                                        true = Ext.input 1 selected
                         25           Ext.input 1           UInt   yes        1 bit   rw      0
                                                                                                        false = Ext.input 1 not selected
                                                                                                        true = Ext.input 2 selected
                         26           Ext.input 2           UInt   yes        1 bit   rw      0
                                                                                                        false = Ext.input 2 not selected

For programming QL1 ... QL4: Selection of the Qint. to be linked according to bit pattern:
 0 0 0 0 0 0 0 0                             0 0 0 0 0 0 0 0                 0 0 0 0 0 0 0 0               0 0 0 0 0 0 0 1
Bit 31                                      Bit 23                           Bit 15                        Bit 7        Bit 0




32      T E C H N I C A L I N F O R M A T I O N | CSS/CSX                                                           9405579/2024-07-30 | SICK
                                                                                                                  Subject to change without notice

SERVICE DATA 9


Table 52: Smart Task - Logic
 ISDU
                                                                   Data
                                                            Data                             Default
 Index                         Sub-    Name                        reposi‐   Length Access                  Value/range
                                                            type                             value
                               Index                               tory
 DEC            HEX
 1210           0x4BA
 1215           0x4BF                                                                                       1 = And
                               -       Logic 1 ... 4        UInt             1 byte   rw     2
 1220           0x4C4                                                                                       2 = Or
 1225           0x4C9

For logical linking of the selected Qint in Input Selector 1.
Table 53: Smart Task - Timer
 ISDU
                                                                   Data
                                                            Data                             Default
 Index                         Sub-    Name                        reposi‐   Length Access                  Value/range
                                                            type                             value
                               Index                               tory
 DEC            HEX
                                                                                                            0 = Deactivated
 1211           0x4BB
                                                                                                            1 = T-on delay
 1216           0x4C0
                               -       Timer 1 ... 4        UInt             1 byte   rw     0              2 = T-off delay
 1221           0x4C5
                                                                                                            3 = T-on/T-off delay
 1226           0x4CA
                                                                                                            4 = Impulse

For setting a time function for QL1...4.
T-on delayoN delay
T-off delayoFF switching delay
T-on/T-off delayoN/OFF switching delay
Impulsefixed pulse time
Table 54: Smart Task - Time Setup
 ISDU
                                                                   Data
                                                            Data                             Default
 Index                         Sub- Name                           reposi‐   Length Access                  Value/range
                                                            type                             value
                               Index                               tory
 DEC            HEX
 1212           0x4BC
 1217           0x4C1                                                                                       0 ... 30000 = Time value in
                               -       Time Setup 1 ... 4   UInt             2 bytes rw      1
 1222           0x4C6                                                                                       ms
 1227           0x4CB

For setting the desired time for the time function.
1 ... 30,000 in ms, factory setting = 1 ms
Table 55: Smart Task - Inverter
 ISDU
                                                                   Data
                                                            Data                             Default
 Index                         Sub-    Name                        reposi‐   Length Access                  Value/range
                                                            type                             value
                               Index                               tory
 DEC            HEX
 1213           0x4BD
 1218           0x4C2                                                                                       0 = Not inverted
                               -       Inverter 1 ... 4     UInt             1 byte   rw     0
 1223           0x4C7                                                                                       1 = Inverted
 1228           0x4CC

To set the inversion of QL1...4.
0 = Not inverted
1 = Inverted




9405579/2024-07-30 | SICK                                                                    T E C H N I C A L I N F O R M A T I O N | CSS/CSX   33
Subject to change without notice

10 SENSOR REPLACEMENT/DATA STORAGE


10               Sensor replacement/data storage
All IO-Link Device have a backup and restore functionality - Data Storage (DS). Thanks to the IO-Link Data Storage
function, previous parameters can be saved and transferred to the replacement device, eliminating the need to
re-parameterize the replacement device.
In the world of automation, there are several names for the same function:
•    Data storage
•    Backup and restore
•    Parameter server
•    Device replacement

NOTE
The DSfunction was introduced with the IO-Link specification V1.1.
It is therefore possible that devices older than 2013 were programmed according to the IO-Link specification V1.0
and do not support the entire feature.

Data storage function
Replacing a IO-Link Device requires the replacement hardware and the application-specific parameterization of the
device.
When data storage is activated, the IO-Link Master always saves the last valid setting parameters of all connected
IO-Link Device in its local memory. If one of the connected IO-Link Devices is replaced with a functionally compatible
replacement device, the IO-Link Master automatically transfers the last valid parameter set of the predecessor
sensor to the new IO-Link Device.
When activating the new IO-Link Device in the IO-Link Master, you can choose between different IO-Link Master
behaviors:
•    NONE: No backup of the device parameters is made in the IO-Link Master .
•    BACKUP/RESTORE: The IO-Link Master saves the parameterization of the connected IO-Link Devices (initially
     automatically) and is ready to restore it in the event of a device replacement.
•    RESTORE: No automatic backup of the device parameters is performed in the IO-Link Master . Manually
     initiated backups are possible. The IO-Link Master monitors the port and restores the parameterization when a
     replacement device is detected.

NOTE
•    To be able to use data storage, it must be activated in the IO-Link Master .
•    If the changeover of one or more sensor parameters is initiated via the control unit, the control unit must
     activate the so-called Data Storage Upload Request-Flag as the final command in the sensor. Only this initiates
     the data repository.
•    Depending on the data volume and the IO-Link Master used, the upload/download of sensor parameters via
     the data storage function can take between a few hundred milliseconds and up to three seconds (typical
     values; values may vary in individual cases).
•    For details on the use of data storage, see "IO-Link Interface and System Specification, V1.1.2, Chapter 10.4
     Data Storage (DS)" under www.io-link.com, menu item Downloads.
•    Parameters that do not participate in data storage are marked in the IODD overview.




34       T E C H N I C A L I N F O R M A T I O N | CSS/CSX                                           9405579/2024-07-30 | SICK
                                                                                                   Subject to change without notice

SENSOR REPLACEMENT/DATA STORAGE 10


NOTE
To set the DSfunction, read the manufacturer-specific instructions for the IO-Link Master.




Figure 5: Web server user interface of a SIG350 from SICK


Validation
The Validation function is always available in conjunction with the DS functionality, even if Data Storage is not being
used.
When replacing a device, it must be ensured that it is replaced by a compatible device. For this reason, the DS
functionality includes a check for the correct device.
For this purpose, the Device ID and Vendor ID of the connected device are compared with the ID data in the DS.
If the IDs match the IDs saved in the backup of the IO-Link Masters , the IO-Link Master continues and compares the
parameterization of the device with those saved in the DS.
If the IDs do not match, an error event is triggered to inform the above-mentioned communication layers of the
mismatch:
Table 56: EventCodes for ports1)
 EventCode ID                Definition and recommended maintenance action                                                 Type
 0x0000 to                   Reserved
 0x17FF
 0x1800                      No device (communication)                                                                     Error
                             Trigger: SMI_PortEvent (0x1800) by SM_PortMode (COMLOST)
 0x1801                      Startup parametrization error - check parameter                                               Error
 0x1802                      Incorrect Vendor ID - Inspection Level mismatch                                               Error
                             Trigger: SM_PortMode (COM_FAULT)
 0x1803                      Incorrect Device ID - Inspection Level mismatch                                               Error
                             Trigger: SM_PortMode (COM_FAULT)

Backup
Depending on the data backup behavior setting (BACKUP/RESTORE), IO-Link Master automatically creates the first
backup (Backup) of the application-specific parameterization.
If all settings on the device are correct, the backup is complete.
In most cases, however, adjustments are necessary: the content of Backup must then be updated. With the
selection RESTORE , the Backup must always be created manually.
There are various options for parameterizing IO-Link Devices. There are therefore various options for updating the
content of the Backup .


1)      Source: IO-Link Interface and System Specification V1.1.3, June 2019

9405579/2024-07-30 | SICK                                                               T E C H N I C A L I N F O R M A T I O N | CSS/CSX   35
Subject to change without notice

10 SENSOR REPLACEMENT/DATA STORAGE

DS update options
•    Parameter changes on the device itself (display, buttons, potentiometer, etc.):
     All changes made directly to the device are automatically reported to IO-Link Master . The IO-Link Device informs
     the IO-Link Master about parameter changes and the IO-Link Master updates its data memory accordingly.
     NOTICE
     The Backup is not updated in RESTOREmode!



•    Parameter changes via PLC (also SICK function blocks) or other programming tools:
     If PLC programs or other application-specific processes access the device via the IO-Link interface and
     change parameters, no automatic action takes place. The user program itself must ensure that the content
     of the data memory is updated after the adjustments. The function modules offered by SICK to simplify the
     exchange of service data do not trigger Backupupdates. System commands for controlling the data storage
     functionality are available for this purpose.
     Table 57: System commands for data storage functionality
     Command (hex)                       Command (dec)      Command name         M/O            Definition
     0x00                                0                  Reserved
     0x01                                1                  ParamUploadStart     0              Start parameter
                                                                                                upload
     0x02                                2                  ParamUploadEnd       0              Stop parameter
                                                                                                upload
     0x03                                3                  ParamDownloadStart   0              Start parameter down‐
                                                                                                load
     0x04                                4                  ParamDownloadEnd     0              Stop parameter down‐
                                                                                                load
     0x05                                5                  ParamDownloadStore   0              Finalize parameteriza‐
                                                                                                tion and start data
                                                                                                storage
     If the changes made by the PLC communication are to be recorded in the DS, the IO-Link Device must signal
     this to the IO-Link Master via an IO-Link event.
     This event is generated by the device when it receives the system command ParamDownloadStore (index 0x02,
     value 0x05).
     → To add new parameters to the Backup of the DS, write an ISDU with the value 0x05 to the System Command
     ISDU (index 2) at the end of your sequence.


•    Engineering tools such as SOPAS (off-site commissioning):
     Engineering tools are obliged to set the DS upload flag after parameterization has been completed via their
     graphical user interfaces. This applies both to engineering tools that use the IO-Link interface itself (note:
     new since V1.1.3) and if additional interfaces such as TCP/IP, USB are used.
     NOTE
     Since engineering tools did not behave in this way before IO-Link Interface Version V1.1.3 , pay particular
     attention to whether the IO-Link Master updates its DS content when the IO-Link Device is connected back to the
     IO-Link Master .



•    Cloud interfaces/Dual Talk (IIoT connections, such as REST API, MQTT or OPC UA):
     Cloud interfaces from IO-Link Master often offer the option of changing parameters from IO-Link Devices .
     The same applies to these interfaces as for access by PLC programs - there is no automatic update. The
     respective DS update commands of the cloud protocol must be sent to IO-Link Master .




36      T E C H N I C A L I N F O R M A T I O N | CSS/CSX                                           9405579/2024-07-30 | SICK
                                                                                                  Subject to change without notice

EVENTS 11


11                    Events
IO-Link events
With Events (events), an IO-Link Device reports events to the IO-Link Master without being prompted to do so by the
IO-Link Master.
Events are the only way for an IO-Link Device to report a sporadic event, information or problem. An IO-Link Master can
use events to inform about port-specific events, e.g. the disconnection of an IO-Link Device from the IO-Link Master.

NOTE
Not all IO-Link Master support the event mechanism, especially older ones. You can deactivate the generation of
events on the device page in “Notification handling (ISDU 227)”.

An event consists of:
•       Event Qualifier: Specification of information about:
        - Instance (event instance)
        - Source (event source)
        - Type (event type)
        - Mode (event mode)
•       Event Code: Details of the event content

11.1                  Event Qualifier
The Event Qualifier (event qualifier) is a byte that contains some important information about the event.
Table 58: Event qualifier
 Mode                                   Type                            Source          Instance
        Bit 7                      6           5              4                  3             2                        1                      Bit 0
 0 = reserved                           0 = reserved                    0 = Device      0 = unknown
 1 = Event single shot                  1 = Notification                1 = Master      1 ... 3 = reserved
 2 = Event disappears                   2 = Warning                                     4 = Application
 3 = Event appears                      3 = Error

Type
Type (event type) are classified as follows:
Table 59: Type
 Value             Definition           Description
 0                 Reserved             -
 1                 Notification         For information purposes only; the system is not restricted.
 2                 Warning              System is still functional, but impaired in some way. You must rectify the problem as quickly
                                        as possible by taking appropriate measures.
 3                 Error                The system is no longer functional. Depending on the cause of the error, it may be possible to
                                        restore the function.


11.2                  Event Code
An event outputs a 2-byte long Event Code that contains the cause for the occurrence of the event.
The information on the event source from Event Qualifier can be used to differentiate where the event comes from.




9405579/2024-07-30 | SICK                                                                      T E C H N I C A L I N F O R M A T I O N | CSS/CSX       37
Subject to change without notice

11 EVENTS

11.2.1             Device-specific events

NOTE
Not all IO-Link masters support the event mechanism.
In Notification Handling (Index 227), the generation of events can be deactivated on the device side.

IO-Link Devices support manufacturer-specific Event Codes, which must be described in the documentation belonging
to the IO-Link Device .
The following device-specific events are supported:
Table 60: Device-specific Events
 Code
                                    Name                       Type           Note                                      Action
 Dec             Hex
 20480           0x5000             Device hardware fault      Error          Fatal device error                        Replacement required.
                                                                              Triggered in the event of a short cir‐
                                                                                                                        Check device connec‐
 36000           0x8CA0             Short circuit on Qx        Warning        cuit on at least one digital output.
                                                                                                                        tion.
                                                                              Overcurrent detection.
                                                                              Parameters have been amended
                                                                              (only when changing the sensing
 36001           0x8CA1             New parameters             Notification   range using control elements on the None
                                                                              sensor housing or using the external
                                                                              teach-in via pin 2).
                                                                                                                        Clean the optical surfa‐
 36004           0x8CA4             Quality of run alarm       Warning        Operational safety alarm                  ces (sensor and reflec‐
                                                                                                                        tor).
                                    Alarm upper temperature                   Upper temperature threshold has
 36008           0x8CA8                                        Warning                                                  Cool down sensor.
                                    threshold                                 been exceeded.
                                                                              Alarm threshold for operating hours       Prepare on-site service
 36011           0x8CAB             Alarm operating hours      Warning
                                                                              reached                                   or device exchange.
                                    Alarm lower temperature                   Lower temperature threshold has
 36015           0x8CAF                                        Warning                                                  Warm up sensor.
                                    threshold                                 been exceeded.

Example of device-specific Event Code
Sensor from SICK sends the event "Successful teach-in":




Figure 6: Source: Logix Designer, Studio 5000 using SIG350 as IO-Link Master

Common Event Codes are defined in the IO-Link interface specification (Table D.1):
Table 61: Event Codes for IO-Link Devices2)
 Event Code ID                      Definition and recommended maintenance                 DeviceStatus         Type
                                    action                                                 Value
 0x0000                             No malfunction                                         0                    Notification
 0x1000                             General malfunction – unknown error                    4                    Error
 0x1001 to                          Reserved
 0x17FF


2)     Source: IO-Link Interface Specification V1.1.3, June 2019; Table D.1 - EventCodes for Devices

38         T E C H N I C A L I N F O R M A T I O N | CSS/CSX                                                                 9405579/2024-07-30 | SICK
                                                                                                                           Subject to change without notice

EVENTS 11


 Event Code ID                     Definition and recommended maintenance                    DeviceStatus           Type
                                   action                                                    Value
 0x1800 to                         Vendor specific
 0x18FF
 0x1900 to                         Reserved
 0x3FF
 0x4000                            Temperature fault – Overload                              4                      Error
 0x4001 to                         Reserved
 0x420F
 0x4210                            Device temperature overrun – Clear source of heat         2                      Warning
 0x4211 to                         Reserved
 0x421F
 0x4220                            Device temperature underrun – Insulate Device             2                      Warning
 0x4221 to                         Reserved
 0x4FFF
 0x5000                            Device hardware fault – Device exchange                   4                      Error
 0x5001 to                         Reserved
 0x500F
 0x5010                            Component malfunction – Repair or exchange                4                      Error
 0x5011                            Non volatile memory loss – Check batteries                4                      Error
 0x5012                            Batteries low – Exchange batteries                        2                      Warning
 0x5013 to                         Reserved
 0x50FF
 0x5100                            General power supply fault – Check availability           4                      Error
 0x5101                            Fuse blown/open – Exchange fuse                           4                      Error
 0x5102 to                         Reserved
 0x510F
 0x5110                            Primary supply voltage overrun – Check tolerance          2                      Warning
 0x5111                            Primary supply voltage underrun – Check tolerance         2                      Warning
 0x5112                            Secondary supply voltage fault (Port Class B) – Check     2                      Warning
                                   tolerance
 0x5113 to                         Reserved
 0x5FFF
 0x6000                            Device software fault – Check firmware revision           4                      Error
 0x6001 to                         Reserved
 0x631F
 0x6320                            Parameter error – Check data sheet and values             4                      Error
 0x6321                            Parameter missing – Check data sheet                      4                      Error
 0x6322 to                         Reserved
 0x634F
 0x6350                            Reserved
 0x6351 to                         Reserved
 0x76FF
 0x7700                            Wire break of a subordinate device – Check installation   4                      Error
 0x7701 to                         Wire break of subordinate device 1 …device 15 – Check     4                      Error
 0x770F                            installation
 0x7710                            Short circuit – Check installation                        4                      Error
 0x7711                            Ground fault – Check installation                         4                      Error



9405579/2024-07-30 | SICK                                                                            T E C H N I C A L I N F O R M A T I O N | CSS/CSX   39
Subject to change without notice

11 EVENTS

Event Code ID                     Definition and recommended maintenance                  DeviceStatus   Type
                                  action                                                  Value
0x7712 to                         Reserved
0x8BFF
0x8C00                            Technology specific application fault – Reset Device    4              Error
0x8C01                            Simulation active – Check operational mode              3              Warning
0x8C02 to                         Reserved
0x8C0F
0x8C10                            Process variable range overrun – Process Data uncertain 2              Warning
0x8C11 to                         Reserved
0x8C1F
0x8C20                            Measurement range exceeded – Check application          4              Error
0x8C21 to                         Reserved
0x8C2F
0x8C30                            Process variable range underrun – Process Data uncer‐   2              Warning
                                  tain
0x8C31 to                         Reserved
0x8C3F
0x8C40                            Maintenance required – Cleaning                         1              Warning
0x8C41                            Maintenance required – Refill                           1              Warning
0x8C42                            Maintenance required – Exchange wear and tear parts     1              Warning
0x8C43 to                         Reserved
0x8C9F
0x8CA0 to                         Vendor specific
0x8DFF
0x8E00 to                         Reserved
0xAFFF
0xB000 to                         Reserved for Safety extensions
0xB0FF
0xB100 to                         Reserved for profiles
0xBFFF
0xC000 to                         Reserved
0xFF90
0xFF91                            Data Storage upload request ("DS_UPLOAD_REQ") –         0              Notification (single shot)
                                  internal, not visible to user
0xFF92 to                         Reserved
0xFFAF
0xFFB0 to                         Reserved for Wireless extensions
0xFFB7
0xFFB8 to                         Reserved
0xFFFF

Example of common Event Code
Sensor from SICK transmits the event of a "short circuit" fault occurring:




40       T E C H N I C A L I N F O R M A T I O N | CSS/CSX                                                            9405579/2024-07-30 | SICK
                                                                                                                    Subject to change without notice

EVENTS 11




Figure 7: Source: Logix Designer, Studio 5000 using SIG350 as IO-Link Master


11.2.2                Port-specific events
Port-specific events are events that are output by the IO-Link-Master. The reason for their occurrence has something
to do with the port to which a device is connected.
A distinction is also made here between common Event Codes that are specified in the IO-Link interface specifica‐
tion (Table D.2) and events that are IO-Link Master-specific:
Table 62: EventCodes for ports 3)
 EventCode ID                         Definition and recommended maintenance action                                  Type
 0x0000 to                            Reserved
 0x17FF
 0x1800                               No Device (communication) Trigger: SMI_PortEvent (0x1800) by                   Error
                                      SM_PortMode (COMLOST)
 0x1801                               Startup parametrization error – check parameter                                Error
 0x1802                               Incorrect VendorID – Inspection Level mismatch Trigger: SM_PortMode Error
                                      (COMP_FAULT)
 0x1803                               Incorrect DeviceID – Inspection Level mismatch Trigger: SM_PortMode Error
                                      (COMP_FAULT)
 0x1804                               Short circuit at C/Q – check wire connection                                   Error
 0x1805                               PHY overtemperature – check Master temperature and load                        Error
 0x1806                               Short circuit at L+ – check wire connection                                    Error
 0x1807                               Overcurrent at L+ – check power supply (e.g. L1+)                              Error
 0x1808                               Device Event overflow                                                          Error
 0x1809                               Backup inconsistency – memory out of range (2048 octets) Trigger:              Error
                                      SMI_PortEvent (0x1809) by DS_Fault (SizeCheck_Fault)
 0x180A                               Backup inconsistency – identity fault Trigger: SMI_PortEvent (0x180A)          Error
                                      by DS_Fault (Identification_Fault)
 0x180B                               Backup inconsistency – Data Storage unspecific error Trigger: SMI_Por‐ Error
                                      tEvent (0x180B) by DS_Fault (All other incidents)
 0x180C                               Backup inconsistency – upload fault                                            Error
 0x180D                               Parameter inconsistency – download fault                                       Error
 0x180E                               P24 (Class B) missing or undervoltage                                          Error
 0x180F                               Short circuit at P24 (Class B) – check wire connection (e.g. L2+)              Error
 0x1810                               Short circuit at I/Q – check wiring                                            Error
 0x1811                               Short circuit at C/Q (if digital output) – check wiring                        Error
 0x1812                               Overcurrent at I/Q – check load                                                Error
 0x1813                               Overcurrent at C/Q (if digital output) – check load                            Error
 0x1814 to                            Reserved
 0x1EFF
 0x1F00 to                            Vendor specific
 0x1FFF

3)      Source: IO-Link Interface Specification V1.1.3, June 2019, Table D.2 - EventCodes for Ports

9405579/2024-07-30 | SICK                                                                             T E C H N I C A L I N F O R M A T I O N | CSS/CSX   41
Subject to change without notice

11 EVENTS

 EventCode ID                                   Definition and recommended maintenance action                           Type
 0x2000 to                                      Safety extensions
 0x2FFF
 0x3000 to                                      Wireless extensions
 0x3FFF
 0x4000 to                                      Reserved
 0x5FFF
 0x6000                                         Invalid cycle time Trigger: SM_PortMode (CYCTIME_FAULT)                 Error
 0x6001                                         Revision fault – incompatible protocol version Trigger: SM_PortMode     Error
                                                (REVISION_FAULT)
 0x6002                                         ISDU batch failed – parameter inconsistency?                            Error
 0x6003 to                                      Reserved
 0xFF20
 0xFF211)                                       DL: Device plugged in ("NEW_SLAVE") – PD stop Trigger: SM_Port‐         Notification
                                                Mode (COMREADY); see Figure 71 (T10)
 0xFF221)                                       Device communication lost ("DEV_COM_LOST") Trigger: see Figure          Notification
                                                101 (T9)
 0xFF231)                                       Data Storage identification mismatch ("DS_IDENT_MISMATCH") Trig‐        Notification
                                                ger: see Figure 104 (T15)
 0xFF241)                                       Data Storage buffer overflow ("DS_BUFFER_OVERFLOW") Trigger: see        Notification
                                                Figure 104 (T17)
 0xFF251)                                       Data Storage parameter access denied ("DS_ACCESS_DENIED") Trig‐         Notification
                                                ger: see Figure 104 (T29), Figure 105 (T32), Figure 107 (T39)
 0xFF26                                         Port status changed ‒ Use "SMI_PortStatus" service for port status in   Notification
                                                detail Trigger: see Figure 101 (T12)
 0xFF27                                         Data Storage upload completed and new data object available Trigger:    Notification
                                                see Figure 104 (T26)
 0xFF28 to                                      Reserved
 0xFF30
 0xFF311)                                       DL: Incorrect Event signalling ("EVENT") Trigger: none                  Notification
 0xFF32 to 0xFFFF                               Reserved
1)   No more required due to SMI Event concept. Not recommended for new implementations.

Example of common port-specific Event Code
SIG350 sends the port event of a disappearing 'No Device (communication)' error:




Figure 8: Source: Logix Designer, Studio 5000 using SIG350 as IO-Link Master




42          T E C H N I C A L I N F O R M A T I O N | CSS/CSX                                                                       9405579/2024-07-30 | SICK
                                                                                                                                  Subject to change without notice

USE CASE: SETTING THE PROCESS DATA 12


12                    Use case: Setting the process data
Configuring the process data setting
           1

Detecting color
                                   2
                                                      4                               5

                      Write                                                      Write
               Process Data Select             Write value 1                 Measurement                             Write value 1
                    Index 120                                                 Color Space
                                                                              Index 296

                                   3                                                   6
                                                                                                                                    7
                        Write value                                               Write value
                        0 default                                                 0 default



                                                                           Measurement                           Measurement
                  Evaluation Mode                                            Mode RGB                              Mode LAB
                = Color Match Value,                                     RGB-measurement +                     LAB-measurement +
                       Q1...Q4,                                                 Q1...Q4,                              Q1...Q4,
                   all Qint status                                          all Qint status                       all Qint status

1          Align sensor with color object
2          Set the desired measuring function via Process Data Select Index 120
3          Write value 0 = Evaluation Mode (factory setting)
           Transmission of the CMV values (color match) for 4 taught-in colors, as well as the switching states for 24 colors and
           the diagnostic status of the sensor
4          Write value 1 = Measurement Mode
           Transmission of the color measurement of the current color and its CMV value, as well as the switching states for 24
           colors and the diagnostic status of the sensor
5          Set the desired type of color measurement via Measurement Color Space Index 296
6          Write value 0 = RGB (factory setting)
           Transfer of the RGB values, i.e. the red, green and blue components of the current color
7          Write value 1 = LAB
           Transmission of the Lab color space of the current color and its CMV value, as well as the switching states for 24 colors
           and the diagnostic status of the sensor




9405579/2024-07-30 | SICK                                                                  T E C H N I C A L I N F O R M A T I O N | CSS/CSX   43
Subject to change without notice

13 TECHNICAL DATA


13               Technical data
Table 63: Mechanics/Electronics
Cable length of IO-Link master and IO-Link device            max. 20 m
IO-Link specification                                        V1.1




44       T E C H N I C A L I N F O R M A T I O N | CSS/CSX                 9405579/2024-07-30 | SICK
                                                                         Subject to change without notice

LIST OF ABBREVIATIONS 14


14                    List of abbreviations
Table 64: List of abbreviations
 IODD              IO Device Description           Device description file of an IO-Link device
 ISDU              Indexed Service Data Unit       Service data object in IO-Link
 COM1                                              COM1 = 4.8 kbit/s
 COM2              SDCI communication mode         COM2 = 38.4 kbit/s
 COM3                                              COM3 = 230.4 kbit/s
 SDCI              Single-drop digital interface   Official (specification) name for IO-Link technology
 SDD               SOPAS ET Device Description     Device description file / driver for SICK SOPAS ET software




9405579/2024-07-30 | SICK                                                       T E C H N I C A L I N F O R M A T I O N | CSS/CSX   45
Subject to change without notice

15 INDEX


15                      Index
I                                                                                                        16384 Qint. 3 teach data............................................................ 23
                                                                                                         16385 Qint. 3 configuration........................................................ 24
ISDU                                                                                                     16386 Qint. 4 teach data............................................................ 23
   0002 Standard command............................................................ 30                  16387 Qint. 4 configuration........................................................ 24
   0002 Standard command (OVERVIEW)...................................... 14                             16388 Qint. 5 teach data............................................................ 23
   0002 Standard command (Restore)........................................... 15                         16389 Qint. 5 configuration........................................................ 24
   0002 Standard command (teach command)............................. 21                                 16390 Qint. 6 teach data............................................................ 23
   0012 Device access locks (Key lock).......................................... 15                      16391 Qint. 6 configuration........................................................ 24
   00160 Key Lock Type................................................................... 15             16392 Qint. 7 teach data............................................................ 23
   0016 Vendor Name...................................................................... 13             16393 Qint. 7 configuration........................................................ 24
   0017 Vendor text.......................................................................... 13         16394 Qint. 8 teach data............................................................ 23
   0018 Product Name..................................................................... 13             16395 Qint. 8 configuration........................................................ 24
   0019 Product ID........................................................................... 13         16396 Qint. 9 teach data............................................................ 23
   0020 Product text......................................................................... 13         16397 Qint. 9 configuration........................................................ 24
   0021 Serial number..................................................................... 13            16398 Qint. 10 teach data.......................................................... 23
   0022 Hardware version................................................................ 13              16399 Qint. 10 configuration...................................................... 24
   0023 Firmware version................................................................ 13              16400 Qint. 11 teach data.......................................................... 23
   0024 Application-specific tag...................................................... 14                16401 Qint. 11 configuration...................................................... 24
   0036 Device Status...................................................................... 28           16402 Qint. 12 teach data.......................................................... 23
   0037 Detailed device status........................................................ 28                16403 Qint. 12 configuration...................................................... 24
   0040 Process data input............................................................. 16               16404 Qint. 13 teach data.......................................................... 23
   0058 Teach-in channel................................................................. 21             16405 Qint. 13 configuration...................................................... 24
   0059 Teach................................................................................... 21      16406 Qint. 14 teach data.......................................................... 23
   0060 Qint. 1 teach data............................................................... 23             16407 Qint. 14 configuration...................................................... 24
   0061 Qint. 1 configuration........................................................... 24              16408 Qint. 15 teach data.......................................................... 23
   0062 Qint. 2 teach data............................................................... 23             16409 Qint. 15 configuration...................................................... 24
   0063 Qint. 2 configuration........................................................... 24              16410 Qint. 16 teach data.......................................................... 23
   0064 Device-specific name......................................................... 14                 16411 Qint. 16 configuration...................................................... 24
   0083 Currently selected operating mode................................... 19                          16412 Qint. 17 teach data.......................................................... 23
   0089 Measurement averaging.................................................... 20                     16413 Qint. 17 configuration...................................................... 24
   0097 Sender configuration.......................................................... 16                16414 Qint. 18 teach data.......................................................... 23
   0110 Operation Mode.................................................................. 19              16415 Qint. 18 configuration...................................................... 24
   0114 Quality of teach................................................................... 21           16416 Qint. 19 teach data.......................................................... 23
   0120 Process data select............................................................ 16               16417 Qint. 19 configuration...................................................... 24
   0121 Pin2 configuration.............................................................. 17              16418 Qint. 20 teach data.......................................................... 23
   0122 Pin5 configuration.............................................................. 17              16419 Qint. 20 configuration...................................................... 24
   0153 Temperature........................................................................ 29           16420 Qint. 21 teach data.......................................................... 23
   0165 Color Match Values............................................................ 27                16421 Qint. 21 configuration...................................................... 24
   0175 Quality of Run..................................................................... 22           16422 Qint. 22 teach data.......................................................... 23
   0176 Quality of run alarm threshold........................................... 22                     16423 Qint. 22 configuration...................................................... 24
   0179 Alarm thresholds for diagnostic parameters.................... 29                                16424 Qint. 23 teach data.......................................................... 23
   0190 Operating hours.................................................................. 29             16425 Qint. 23 configuration...................................................... 24
   0204 Find me............................................................................... 18        16426 Qint. 24 teach data.......................................................... 23
   0219 Product ID........................................................................... 13         16427 Qint. 24 configuration...................................................... 24
   0227 Notification Handling.......................................................... 18               4081 Names Qint. 1 ... 16........................................................... 25
   0229 Distance to object.............................................................. 30              4082 Names Qint. 17 ... 24......................................................... 26
   0234 Display settings................................................................... 18           Distance regulation....................................................................... 20
   0293 Output mode....................................................................... 20         ISDU1211
   0295 Color Mode.......................................................................... 20          Timer 1.......................................................................................... 33
   0296 Measurement Color Space................................................ 16                    ISDU1212
   0297 Quality Levels...................................................................... 22          Time 1............................................................................................ 33
   0440 – Hardware Variant............................................................. 18            ISDU1216
   1093 Inverter ext. input (Smart Task A10)................................. 31                         Timer 2.......................................................................................... 33
   1208 SLTI version......................................................................... 31      ISDU1220
   1209 Selector 1............................................................................ 31        Logic 3........................................................................................... 33
   1210 Logic 1................................................................................. 33   ISDU1221
   1213 Inverter 1............................................................................. 33       Timer 3.......................................................................................... 33
   1214 Selector 2............................................................................ 31     ISDU1225
   1215 Logic 2................................................................................. 33      Logic 4........................................................................................... 33
   1217 Time 2................................................................................. 33    ISDU1226
   1218 Inverter 2............................................................................. 33       Timer 4.......................................................................................... 33
   1219 Selector 3............................................................................ 31
   1222 Time 3................................................................................. 33
   1223 Inverter 3............................................................................. 33
   1224 Selector 4............................................................................ 31
   1227 Time 4................................................................................. 33
   1228 Inverter 4............................................................................. 33
   16000 – Device ID Setup............................................................. 19


46             T E C H N I C A L I N F O R M A T I O N | CSS/CSX                                                                                                          9405579/2024-07-30 | SICK
                                                                                                                                                                        Subject to change without notice

INDEX 15




9405579/2024-07-30 | SICK          T E C H N I C A L I N F O R M A T I O N | CSS/CSX   47
Subject to change without notice

9405579/2024-07-30/en
                        Australia                                 Hungary                          Slovenia
                        Phone +61 (3) 9457 0600                   Phone +36 1 371 2680             Phone +386 591 78849
                               1800 33 48 02 – tollfree           E-Mail ertekesites@sick.hu       E-Mail office@sick.si
                        E-Mail sales@sick.com.au                  India                            South Africa
                        Austria                                   Phone +91-22-6119 8900           Phone +27 10 060 0550
                        Phone +43 (0) 2236 62288-0                E-Mail info@sick-india.com       E-Mail info@sickautomation.co.za
                        E-Mail office@sick.at                     Israel                           South Korea
                        Belgium/Luxembourg                        Phone +972 97110 11              Phone +82 2 786 6321/4
                        Phone +32 (0) 2 466 55 66                 E-Mail info@sick-sensors.com     E-Mail infokorea@sick.com
                        E-Mail info@sick.be                       Italy                            Spain
                        Brazil                                    Phone +39 02 27 43 41            Phone +34 93 480 31 00
                        Phone +55 11 3215-4900                    E-Mail info@sick.it              E-Mail info@sick.es
                        E-Mail comercial@sick.com.br              Japan                            Sweden
                        Canada                                    Phone +81 3 5309 2112            Phone +46 10 110 10 00
                        Phone +1 905.771.1444                     E-Mail support@sick.jp           E-Mail info@sick.se
                        E-Mail cs.canada@sick.com                 Malaysia                         Switzerland
                        Czech Republic                            Phone +603-8080 7425             Phone +41 41 619 29 39
                        Phone +420 234 719 500                    E-Mail enquiry.my@sick.com       E-Mail contact@sick.ch
                        E-Mail sick@sick.cz                       Mexico                           Taiwan
                        Chile                                     Phone +52 (472) 748 9451         Phone +886-2-2375-6288
                        Phone +56 (2) 2274 7430                   E-Mail mexico@sick.com           E-Mail sales@sick.com.tw
                        E-Mail chile@sick.com                     Netherlands                      Thailand
                        China                                     Phone +31 (0) 30 204 40 00       Phone +66 2 645 0009
                        Phone +86 20 2882 3600                    E-Mail info@sick.nl              E-Mail marcom.th@sick.com
                        E-Mail info.china@sick.net.cn             New Zealand                      Turkey
                        Denmark                                   Phone +64 9 415 0459             Phone +90 (216) 528 50 00
                        Phone +45 45 82 64 00                            0800 222 278 – tollfree   E-Mail info@sick.com.tr
                        E-Mail sick@sick.dk                       E-Mail sales@sick.co.nz          United Arab Emirates
                        Finland                                   Norway                           Phone +971 (0) 4 88 65 878
                        Phone +358-9-25 15 800                    Phone +47 67 81 50 00            E-Mail contact@sick.ae
                        E-Mail sick@sick.fi                       E-Mail sick@sick.no              United Kingdom
                        France                                    Poland                           Phone +44 (0)17278 31121
                        Phone +33 1 64 62 35 00                   Phone +48 22 539 41 00           E-Mail info@sick.co.uk
                        E-Mail info@sick.fr                       E-Mail info@sick.pl              USA
                        Germany                                   Romania                          Phone +1 800.325.7425
                        Phone +49 (0) 2 11 53 010                 Phone +40 356-17 11 20           E-Mail info@sick.com
                        E-Mail info@sick.de                       E-Mail office@sick.ro            Vietnam
                        Greece                                    Singapore                        Phone +65 6744 3732
                        Phone +30 210 6825100                     Phone +65 6744 3732              E-Mail sales.gsg@sick.com
                        E-Mail office@sick.com.gr                 E-Mail sales.gsg@sick.com
                        Hong Kong                                 Slovakia
                        Phone +852 2153 6300                      Phone +421 482 901 201
                        E-Mail ghk@sick.com.hk                    E-Mail mail@sick-sk.sk


                        Detailed addresses and further locations at www.sick.com




                        SICK AG | Waldkirch | Germany | www.sick.com