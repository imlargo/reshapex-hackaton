TECHNICAL INFORMATION


Photoelectric sensors
SICK Smart Sensors / IO-Link

Device configuration – Advanced operating instructions

Product described
IO-Link – photoelectric sensors

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




2       T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                       8022709.1ML4/2024-03-11 | SICK
                                                                                                 Subject to change without notice

CONTENTS


Contents
                                   1    About this document........................................................................                                5
                                        1.1       Purpose of this document........................................................................                  5
                                        1.2       Intended use.............................................................................................         5
                                        1.3       Symbols.....................................................................................................      5

                                   2    Description of IO-Link.......................................................................                              6

                                   3    Documentation and accessories....................................................                                          7

                                   4    Physical layer.....................................................................................                        8

                                   5    Integration of the sensor into the control level.............................                                              9

                                   6    Setting, configuration and integration........................................... 10

                                   7    Process data...................................................................................... 11

                                   8    Service data....................................................................................... 13
                                        8.1       Device identification.................................................................................           13
                                        8.2  General device settings............................................................................                   14
                                        8.3  Teach-in/detection settings for WTB, WTF, WTM, WTL and WTS devi‐
                                             ces.............................................................................................................      19
                                        8.4 Teach-in / detection settings for WL and WLA devices..........................                                         24
                                        8.5 Teach-in / detection settings for WLG devices.......................................                                   26
                                        8.6 Teach-in / detection settings for WE / WEO devices..............................                                       31
                                        8.7 Teach-in/Detection settings for WTT devices.........................................                                   33
                                        8.8 Installation / Diagnostics.........................................................................                    37
                                        8.9 Smart Tasks..............................................................................................              42
                                             8.9.1         Smart Task “Basic logic” (A00)...............................................                           42
                                             8.9.2         Smart task “Time measurement and debouncing” (A70)....                                                  44
                                             8.9.3         Smart task “Counter and debouncing” (A71)........................                                       46
                                             8.9.4         Smart Task “Speed and length measurement” (A72)...........                                              48
                                             8.9.5         Smart Tasks “Object and gap monitor” (A73)........................                                      56
                                        8.10 System-specific ISDUs..............................................................................                   58

                                   9    Sensor replacement/data storage................................................. 60

                                   10   Device Backward Compatibility (DBC).................................................... 61

                                   11   Events................................................................................................... 62
                                        11.1 Event Qualifier..............................................................................................         62
                                        11.2 Event Code...................................................................................................         63
                                             11.2.1 Device-specific events.............................................................                            63
                                             11.2.2 Port-specific events.................................................................                          67
                                        11.3 Event     processing             using           the        example             of        EtherNet/IP
                                              (Rockwell Logix Designer, Studio 5000).................................................                              70


8022709.1ML4/2024-03-11 | SICK                                                                   T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors    3
Subject to change without notice

CONTENTS


                                     12          Technical data.................................................................................... 75

                                     13          List of abbreviations.......................................................................... 76

                                     14          Index.................................................................................................... 77




4    T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                           8022709.1ML4/2024-03-11 | SICK
                                                                                                                                  Subject to change without notice

ABOUT THIS DOCUMENT 1


1                  About this document
1.1                Purpose of this document
This document is used to describe the functionality of individual ISDUs of IO-Link-capable devices from the field
of photoelectric sensors, photoelectric proximity sensor and fiber optic sensors (so-called smart sensors). The
following detection principles are covered:
WTB, WTF, WTL, WTS, WTT, WL, WLA, WLG, WE, WEO.
The individual range of functions of a specific sensor is shown in full in its IODD and in its technical information
“IODD-Overview” on the respective product page at www.sick.com. The scope of functions of a specific sensor
cannot be inferred from this document.

1.2                Intended use
Use IO-Link only as described in this documentation.

1.3                Symbols

NOTICE
This symbol indicates important information.


NOTE
This symbol provides additional information, e.g., dependencies / interactions between the described function and
other functions, or when individual functions are not supported by every sensor.




8022709.1ML4/2024-03-11 | SICK                                           T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   5
Subject to change without notice

2 DESCRIPTION OF IO-LINK


2                Description of IO-Link
IO-Link communication interface
The product has the IO-Link communication interface.
IO-Link communication is a Master-Device communication system.
The sensor can be used in standard I/O mode (SIO) or in IO-Link mode (IOL). All automation functions and other
parameter settings are effective in IO-Link mode and in standard I/O mode.
The following functions are supported via this standard IO-Link communication interface:
•    Flexible sensor settings
•    Digital transmission of the sensor signals to the IO-Link Master
•    Visualization and configuration of the sensor
•    Diagnosis / Condition Monitoring
•    Device identification
•    Easy device replacement
•    Events
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




6        T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                           8022709.1ML4/2024-03-11 | SICK
                                                                                                      Subject to change without notice

DOCUMENTATION AND ACCESSORIES 3


3                  Documentation and accessories
Accessory components and additional information are available for integrating and setting the IO-Link device. You
will find documentation and software, accessories and links to the SICK Product ID.

SICK product ID
The SICK product ID uniquely identifies the product. It also serves as the address of the web page with information
on the product.
The SICK product ID comprises the host name pid.sick.com, the part number (P/N), and the serial number (S/N),
each separated by a forward slash.
The SICK product ID is displayed as text and QR code on the type label and/or on the packaging.




Figure 1: SICK product ID

Documentation and software
•      IODD: Device description file
•      IODD overview: List of IODD contents
•      IO-Link description: Detailed description of the process, service data and events of the IO-Link device
•      SOPAS ET: Configuration software as a free download
•      The documentation for SOPAS ET is stored in the system folder on your computer with the download:
       C:\Program Files (x86)\SOPAS ET\help
•      Visualization file (SDD = SOPAS Device Description) for operation via SOPAS ET.
•      Function Block Factory

IO-Link products can be easily connected to a computer via USB using the SiLink master. You can quickly and easily
test or parameterize the connected products using the SOPAS ET (SICK Engineering Tool with graphic user navigation
and convenient visualization).

Accessories
•      IO-Link master
•      SiLink master
•      Connecting cables




8022709.1ML4/2024-03-11 | SICK                                           T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   7
Subject to change without notice

4 PHYSICAL LAYER


4                Physical layer
The device data is automatically communicated to the IO-Link Master . It is important to ensure that the IO-Link
Master used supports this performance data.

NOTICE
The maximum current consumption of the IO-Link Device (including load at the outputs) must not exceed the
permissible output current of the respective port on the IO-Link Master .

The individual IO-Link device data differs from device to device and can be found in the online data sheet of the
respective sensor as well as its addendum to operating instructions:
www.sick.com/[part number] --> Downloads --> Documentation




8        T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                       8022709.1ML4/2024-03-11 | SICK
                                                                                                  Subject to change without notice

INTEGRATION OF THE SENSOR INTO THE CONTROL LEVEL 5


5                  Integration of the sensor into the control level
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




8022709.1ML4/2024-03-11 | SICK                                          T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   9
Subject to change without notice

6 SETTING, CONFIGURATION AND INTEGRATION


6                Setting, configuration and integration
In addition to the manual setting on the device, the sensor can also be configured via IO-Link.
A list of all functions that can be configured can be found in the IODD and the IO link overview.

SOPAS ET
Setting via buttons (limited setting options if necessary)
Configuration via IO-Link
1.   Setting via SiLink-Box (SOPAS ET)
2.   Setting via IO-Link Master (PLC)
     ° IO-Link Master from the PLC manufacturer
     ° IO-Link Master from third-party manufacturer (SICK), more manual effort
Integrating the IO-Link device into the PLC
To simplify programming in the PLC, device-specific function blocks can be generated via the Function Block
Factory.
Function blocks simplify acyclical communication (service data communication) between the PLC and IO-Link
Device and the interpretation of process data. They provide device parameters and correct device data types and
translate the parameters provided into indices and sub-indices.




10       T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                       8022709.1ML4/2024-03-11 | SICK
                                                                                                  Subject to change without notice

PROCESS DATA 7


7                   Process data
Download the IODD-File from www.sick.com or from the IODD-Finder of the IO-Link consortium (IODD finder). Make
sure you always use the latest IODD-File .
Process data are transmitted cyclically. There is no confirmation of receipt.
The master determines the cycle time, whereby this must not be less than the minimum cycle time of the sensor.

NOTE
The service data (acyclic data) does not influence the cycle time.

Process data structure for WTBxx, WTFxx, WTLxx, WTSxx, WLAxx, WLGxx, WSExx, each with “Base logic” Smart
Task
Table 1: Process data structure – Basic logic
      Byte offset                                 Byte 0                                                                                Byte 1
       Bit offset         15       14   13   12            11   10         9           8        7          6         5         4         3          2            1                 0

        Name                                                                Reserved                                                                            QL2               QL1

       Data type                                                                 ---                                                                       Boolean            Boolean
                                                                                                                                                           0 = OFF            0 = OFF
      Description                                                           Reserved
                                                                                                                                                           1 = ON             1 = ON



Process data structure for WTBxx, WTFxx, WTLxx, WTSxx, WLAxx, WLGxx, WSExx, each with “Time measurement
and debouncing” Smart Task
Table 2: Process data structure – Time measurement and debouncing
      Byte offset                                 Byte 0                                                                                Byte 1
       Bit offset         15       14   13   12            11   10         9           8        7          6         5         4         3          2            1                 0

        Name                                                     Time measurement value (tmsval)                                                                QL2               QL1

       Data type                                                        Unsigned integer 14                                                                Boolean            Boolean
                                                                                                                                                           0 = OFF            0 = OFF
      Description                                                    [ms or 10 ms or 100 ms]
                                                                                                                                                           1 = ON             1 = ON



Process data structure for WTBxx, WTFxx, WTLxx, WTSxx, WLAxx, WLGxx, WSExx, each with “Counter and
debouncing” Smart Task
Table 3: Process data structure – Counter and debouncing
      Byte offset                                 Byte 0                                                                                Byte 1
       Bit offset         15       14   13   12            11   10         9           8        7          6         5         4         3          2            1                 0

        Name                                                            Count value (cntval)                                                                    QL2               QL1

       Data type                                                        Unsigned integer 14                                                                Boolean            Boolean
                                                                                                                                                           0 = OFF            0 = OFF
      Description                                                                ---
                                                                                                                                                           1 = ON             1 = ON



Process data structure for WTBxx, WTFxx, WTLxx, WTSxx, WLAxx, WLGxx, WSExx, each with “Speed and length
measurement” Smart Task
Table 4: Process data structure – Speed and length measurement
      Byte offset                                 Byte 0                                                                                Byte 1
       Bit offset         15       14   13   12            11   10         9           8        7          6         5         4         3          2            1                 0

        Name                                  Measurement value length (lngval) resp. Measurement value speed (spdval)                                        Qint. 1             QL1

       Data type                                                             Integer 14                                                                    Boolean            Boolean
                                                                                                                                                           0 = OFF            0 = OFF
      Description                                                        [mm] or [mm/s]
                                                                                                                                                           1 = ON             1 = ON




8022709.1ML4/2024-03-11 | SICK                                                                              T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors             11
Subject to change without notice

7 PROCESS DATA

Process data structure for WTFxx, WTLxx, WTSxx, WLAxx, WLGxx, WSExx, each with “Object and gap monitor”
Smart Task
Table 5: Process data structure – Object and gap monitor
     Byte offset                                             Byte 0                                                                                      Byte 1
      Bit offset         15        14        13         12            11      10         9             8     7          6            5        4          3              2                   1                 0

       Name                                                                Time measurement value (tmsval)                                                            Qint.1              QL Gap           QL Object

     Data type                                                                   Unsigned integer 13                                                             Boolean              Boolean         Boolean

                                                                                                                                                                 0 = OFF              0 = OFF         0 = OFF
     Description                                                                        [ms]
                                                                                                                                                                 1 = ON               1 = ON          1 = ON



NOTE
In order to be able to use the maximum switching frequency for the switching output via pin 2 at the same time as
IO-Link communication, configure pin 2 as Q/or Qint.1. Pin 2/5 configuration (Index 121).

Process data structure for WTT with or without Smart Task “Basic logic”
Table 6: Process data structure - WTTxx with or without Smart Task “Base Logic”
Byte off‐
                              Byte 0                                        Byte 1                                          Byte 2                                                    Byte 3
  set
 Bit off‐
             31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10                                                            9        8         7    6          5        4         3    2       1         0
   set
                                                                                                                                         Qint     Qint   Qint    Qint       Qint   Qint     Qint    Qint    QL     QL
  Name                                         Distance to object                                                Reserved
                                                                                                                                          .8       .7     .6      .5         .4     .3       .2      .1     2      1
  Data
                                              Unsigned integer 16                                                   -                                                       Boolean
  type
 Descrip‐                                                                                                                                                                   0 = OFF
                                                     [mm]                                                        Reserved
  tion                                                                                                                                                                      1 = ON




12             T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                                                              8022709.1ML4/2024-03-11 | SICK
                                                                                                                                                                               Subject to change without notice

SERVICE DATA 8


8                  Service data
Service data is only exchanged between the control and IO-Link sensor via the IO-Link master on request by the
control (acyclically).
The respective counterpart confirms receipt of the data.
If the sensor does not answer within five seconds, the master reports a communication error.

NOTE
Not every function described in this document is available in every sensor. The complete list of the parameters
available in the individual devices can be found in the “Addendum to operating instructions” document, which is
found on the web page of the respective device: www.sick.com/[part number] --> Downloads --> Documents.


8.1                Device identification
Table 7: Device identification
 ISDU
                                                                     Data reposi‐                                       Default
 Index             Sub-      Name                        Data type                  Length                 Access                       Value/range
                                                                     tory                                               value
 DEC      HEX      index

 16       10                 Vendor Name                                            7 bytes                             SICK AG
 18       12                 Product Name                                           18 bytes
                   -                                     String
                                                                                    7 ... 64 bytes max.
 19       13                 Product ID                              -                                     ro
                                                                                    (device specific)
                   0         Product ID                  Record                     7 bytes
 219      DB
                   1         Product ID IO-Link Device   String                     7 bytes


The Product ID contains the part number of the connected IO-Link device. However, older devices may also contain
a reference to index 219. In this case, the Product ID (part number) is stored under index 219.

Table 8: Device identification – Product Text / Serial Number
 ISDU
                                                                     Data reposi‐                                       Default
 Index             Sub-      Name                        Data type                  Length                 Access                       Value/range
                                                                     tory                                               value
 DEC      HEX      index

                                                                                    45 ... 64 bytes max.
 20       14       -         Product Text
                                                                                    (device specific)
                                                         String      -                                     ro
                                                                                    8 ... 16 bytes max.
 21       15       -         Serial Number
                                                                                    (device specific)


Serial number format:
YYWWnnnn (Y = year, W = week, n = sequential numbering)

NOTE
The serial number combined with the part number (Product ID) enables the device to be clearly identified.

Table 9: Device identification – Specific Tag / Specific Name
 ISDU
                                                                     Data reposi‐
 Index             Sub-      Name                        Data type                  Length                 Access       Default value            Value/range
                                                                     tory
 DEC      HEX      index

 24       18       -         Application Specific Tag                yes                                                *******
                                                         String                     32 bytes               rw
 64       40       -         Device Specific Name                    no                                                 *******


Any text with a maximum of 32 characters can be stored in the Application Specific Tag . This can be useful for
describing the exact position or task of the sensor in the overall machine. The Application Specific Tag is saved via
the data repository.
Any text with a maximum of 32 characters can also be stored in the Device Specific Name . This name is not saved
via the data storage and is therefore available for temporary/only valid information for this sensor.




8022709.1ML4/2024-03-11 | SICK                                                                              T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   13
Subject to change without notice

8 SERVICE DATA

Table 10: Device identification - Version
ISDU
                                                                            Data reposi‐                                Default
Index             Sub-        Name                             Data type                   Length              Access                  Value/range
                                                                            tory                                        value
DEC     HEX       Index

                                                                                           4 ... 64 bytes
22      16        -           Hardware version                                                                 ro       xxxx
                                                                                           (device specific)
                                                               String       -
                                                                                           12 ... 64 bytes
23      17        -           Firmware version                                                                 ro       Vxxx.xxx.xxx
                                                                                           (device specific)


This ISDU indicates the hardware and software versions.

Table 11: Device identification - Find me
ISDU
                                                                            Data reposi‐                                Default
Index             Sub-        Name                             Data type                   Length              Access                  Value/range
                                                                            tory                                        value
DEC     HEX       index

                                                                                                                                       0 = Find me deactivated
204     CC        -           Find me                          UInt         no             8 bits              rw       0
                                                                                                                                       1 = Find me activated


The sensor can be uniquely identified using Find me. For machines with several identical sensors, it is therefore
possible to uniquely identify the device with which communication is currently taking place.
When Find me is activated, either the yellow LED or all LEDs of the sensor flash at 1 Hz, depending on the sensor
type.

8.2               General device settings
Table 12: General device settings - Standard command
ISDU
                                                                            Data reposi‐                                Default
Index             Sub-        Name                             Data type                   Length              Access                  Value/range
                                                                            tory                                        value
DEC     HEX       index

                                                                                                                                       129 = Application Reset
                                                                                                                                       130 = Restore Factory Settings
2       02        -           Standard command                 UInt         -              1 byte              wo
                                                                                                                                       208 = Load selected job number
                                                                                                                                       209 = Store to selected job number


Application Reset: resets application-specific settings.
Restore Factory Settings: the sensor is reset to the factory settings.
Load selected job number: the sensor is set to the settings defined by the selected job.
Store to selected job number: the current sensor settings are saved under the selected job.

Table 13: General device settings - Device access locks
ISDU
                                                                            Data reposi‐                                Default
Index             Sub-        Name                             Data type                   Length              Access                  Value/range
                                                                            tory                                        value
DEC     HEX       index

                                                                                                                                       Bit no.
                              Device access locks (key lock)
                                                                                                                                       0                   Not available
                                                                                                                                                           0 = Unlocked
                              Data storage lock                                                                         0              1
                                                                                                                                                           1 = Locked
12      02        -                                            Record       yes            2 bytes             rw
                              Not available                                                                                            2                   Not available
                                                                                                                                                           0 = Unlocked
                              Local user interface lock                                                                 0              3
                                                                                                                                                           1 = Locked
                              Not available                                                                                            4 – 15              Not available


Various functions of a sensor can be locked or unlocked with Device access locks . The functionality has been
recorded in the IO-Link interface specification.
Bit 1     Data storage lock You can lock the data repository functionality using bit 1. When the bit is set, the sensor
                            rejects data repository write requests from the IO-Link master with an error message.
                            For newer devices, the data repository function can no longer be deactivated.
Bit 2     Local Parameteri‐ If the bit is set, the local control elements and the external input on the sensor are
          zation Lock       disabled.



14        T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                                        8022709.1ML4/2024-03-11 | SICK
                                                                                                                                                    Subject to change without notice

SERVICE DATA 8


Bit 3         Local user interfaceThe local control elements on the sensor are locked when the bit is set.
              lock                The lock can be unlocked for a period of 30 seconds: Press the teach-in button for 8
                                  seconds. After the 30 seconds have elapsed, the control elements are automatically
                                  locked again.1
                                  Local user interface lock is not available if the sensor does not have a housing operating
                                  element.
1      If necessary, observe device-specific behavior.

Table 14: General device settings - Physical input / output type configuration pin 2
 ISDU
                                                                           Data reposi‐                         Default
 Index             Sub-      Name                              Data type                  Length   Access                       Value/range
                                                                           tory                                 value
 DEC        HEX    index

                                                                                                                                1 = PNP
                             Physical input / output type
 92         5C     -                                           UInt        yes            1 byte   rw           3               2 = NPN
                             configuration pin 2
                                                                                                                                3 = Push-pull


Physical input/output type configuration pin 2 makes it possible to determine the wiring on pin 2. If the device is used
in an NPN network and pin 2 should be used as an input function, this parameter must be set to 2 = NPN in
advance.

NOTE
Dependency: Pin 2 configuration (Index 121)

Table 15: General device settings - Sender configuration
 ISDU
                                                                           Data reposi‐                         Default
 Index             Sub-      Name                              Data type                  Length   Access                       Value/range
                                                                           tory                                 value
 DEC        HEX    index

                                                                                                                                0 = Sender active
 97         61     -         Sender configuration              UInt        -              1 byte   rw           0
                                                                                                                                1 = Sender not active


This ISDU can be used to switch off the Send LED.
Alternatively, the sensor's Send LED can also be deactivated using the HIGH signal on pin 2 (when Pin 2 configura‐
tion (ISDU 121) is Sender off).
If the settings contradict one another, the Switch-off signal is dominant.
If the sensor does not have a Send LED (e.g. with WExx): Sender configuration is not available.

NOTE
Dependency: Pin 2 configuration Sender off (ISDU 121)

Table 16: General device settings - Oscillation frequency at output
 ISDU
                                                                           Data reposi‐                         Default
 Index             Sub-      Name                              Data type                  Length   Access                       Value/range
                                                                           tory                                 value
 DEC        HEX    Index

 115        73     0         Oscillation frequency at output   UInt        yes            1 byte   rw           10              1 ... 50


The Oscillation frequency at output can be used to set the frequency (in Hz) at which the digital output of the sensor
should oscillate when an object is detected.

NOTE
Only available for MulitPulse devices. For more details on MultiPulse functionality, see the operating instructions for
the corresponding device.




8022709.1ML4/2024-03-11 | SICK                                                                      T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   15
Subject to change without notice

8 SERVICE DATA

Table 17: General device settings - Process data select
ISDU
                                                                              Data reposi‐                     Default
Index               Sub-        Name                            Data type                    Length   Access                 Value/range
                                                                              tory                             value
Dec        Hex      index

                                                                                                                             0 = device specific
                                                                                                                             1 = device specific
120        78       -           Process data select             UInt          yes            1 byte   rw       0             2 = device specific
                                                                                                                             3=…
                                                                                                                             …


Process data select can be used to determine which process data structure of the sensor is to be output cyclically.
The possible process data structures are fixed. See the respective device documentation for details on the process
data structures.

Table 18: General device settings - Pin 2 configuration
ISDU
                                                                              Data reposi‐                     Default
Index               Sub-        Name                            Data type                    Length   Access                 Value/range
                                                                              tory                             value
DEC        HEX      index

                                                                                                                             0 = Deactivated / no function
                                                                                                                             Inputs:
                                                                                                                             1 = External input (Smart Task)
                                                                                                                             16 = Sender off
                                                                                                                             17 = Teach-in
                                                                                                                             Outputs:
                                                                                                               Device spe‐   32 = Detection output Q/
121        79       -           Pin2 configuration              UInt          yes            1 byte   rw
                                                                                                               cific         33 = Quality of run alarm output
                                                                                                                             34 = Switching signal QL2
                                                                                                                             35 = Detection output Qint.1
                                                                                                                             36 = Detection output Qint.2
                                                                                                                             39 = Switching signal QL1
                                                                                                                             40 = Switching signal QL1/
                                                                                                                             43 = Health output


Pin 2 configuration can be used to assign a range of input and output functions to pin 2 in the device connector (or
the white wire when using a connecting cable).
Deactivated                                              The signal level at pin 2 is not evaluated.
External input (Smart Task)                              Input signal; is processed in Smart Task (if present).
Sender off                                               Input signal;
                                                         Level at pin 2 HIGH 1): Sender LED of the sensor switched off
                                                         Level at pin 2 LOW 2): Sender LED of the sensor switched on (unless deactivated
                                                         via the Sender configuration (Index 97).
                                                         Does not apply for WExx devices.
Teach-in                                                 Input signal;
                                                         Level at pin 2 HIGH for at least 1 second 1): Triggers the teach command.
                                                         For WTBxx, WTFxx, WTLxx, WTSxx, WTTxx; the current distance between the
                                                         sensor and the object in the light beam is set as the sensing range, if necessary
                                                         corrected by the set Teach-in offset value (ISDU 90).
                                                         For WLxx, WLGxx, WLAxx and, if necessary, WExx; the sensor’s sensitivity is
                                                         adjusted to the current energetic situation.
Detection output Q/                                      Output signal; signal level device specific
                                                         WTBxx, WTFxx, WTLxx, WTSxx: LOW2) if the detection object is detected by the
                                                         sensor. WLxx, WLGxx, WLAxx, WExx: HIGH1) if the detection object is detected by
                                                         the sensor.
Quality of run alarm output                              Output signal; HIGH1) if the Quality of run value (ISDU 175) undercuts the set
                                                         alarm threshold (Quality of run alarm threshold, ISDU 176).
Switching signal QL2                                     Output signal; switching signal generated from Smart Task.
Detection output Qint.1                                  Output signal; HIGH1) when detection object is detected by sensor via Qint.1
                                                         channel.
Detection output Qint.2                                  Output signal; HIGH1) when detection object is detected by sensor via Qint.2
                                                         channel.
Switching signal QL1                                     Output signal; switching signal generated from Smart Task.
Switching signal QL1/                                    Output signal; inverted signal to QL1.



16          T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                            8022709.1ML4/2024-03-11 | SICK
                                                                                                                                          Subject to change without notice

SERVICE DATA 8


Health output                                          Output signal; inverted signal to Quality of run alarm output.
1)     HIGH = Signal level to L+
2)     LOW = signal level at ground or pin/wire not connected

NOTE
Not every device supports each individual pin 2 function. See IODD of the relevant device for more information.

Table 19: General device settings - Notification Handling
 ISDU
                                                                           Data reposi‐                                   Default
 Index             Sub-      Name                              Data type                  Length             Access                       Value/range
                                                                           tory                                           value
 DEC        HEX    index

                                                                                                                                          0 = All enabled
                                                                                                                                          1 = All disabled
 227        E3     -         Notification Handling             Uint        yes            1 byte             rw           0
                                                                                                                                          2 = Events enabled, PD invalid flag disabled
                                                                                                                                          3 = Events disabled, PD invalid flag enabled


Notification Handling enables the generation of IO-Link events in the sensor and the function for marking the process
data as invalid to be activated/deactivated.

Table 20: General device settings - Display settings
 ISDU
                                                                           Data reposi‐
 Index             Sub-      Name                              Data type                  Length             Access       Default         Value/range
                                                                           tory
 DEC        HEX    Index

                   0         Display settings                  Record                     8 bytes                         -
                                                                                                                                          0 = Digits
                                                                                                                                          1 = Bar graph
                             Display indicator mode, channel                              8 bits
                   1                                           Uint                                                       0               2 = Percentage value
                             1                                                            (Offset 56 bits)
                                                                                                                                          3 = Counter value
                                                                                                                                          4 = Edge value
                                                                                                                                          0 = Digits
                                                                                                                                          1 = Bar graph
                             Display indicator mode, channel                              8 bits
                   2                                           Uint                                                       0               2 = Percentage value
                             2                                                            (Offset 48 bits)
                                                                                                                                          3 = Counter value
                                                                                                                                          4 = Edge value
                                                                                          8 bits
                   3         Display brightness                Uint                                                       50              10 ... 100
                                                                                          (Offset 40 bits)
 234        EA                                                             Yes                               rw
                                                                                          8 bits                                          0 = OFF
                   4         Energy saving mode                Uint                                                       0
                                                                                          (Offset 32 bits)                                1 = ON
                                                                                          8 bits                                          0 = OFF
                   5         Turn display                      Uint                                                       0
                                                                                          (Offset 24 bits)                                1 = ON
                                                                                          8 bits                                          0 = OFF
                   6         Display inversion                 Uint                                                       0
                                                                                          (Offset 16 bits)                                1 = ON
                                                                                          8 bits                                          0 = OFF
                   7         Display alerts                    Uint                                                       0
                                                                                          (Offset 8 bits)                                 1 = ON
                                                                                                                                          1 = English
                                                                                                                                          2 = German
                                                                                          8 bits
                   8         Display language                  Uint                                                       1               7 = Chinese
                                                                                          (Offset 0 bits)
                                                                                                                                          8 = Japanese
                                                                                                                                          10 = Korean


 Display indicator mode,           Display mode channel 1 (corresponds to Qint.1) for displaying the ACTUAL and setpoint values on
 channel 1                         the display in relation to each other.
 Display indicator mode,           Display mode channel 2 (corresponds to Qint.2) for displaying the ACTUAL and setpoint values on
 channel 2                         the display in relation to each other.
 Display brightness                Display brightness
 Energy saving mode                When energy-saving mode is activated, the display is deactivated 120 seconds after the last input.
 Turn display                      Rotation of the display by 180°.
 Display inversion                 Inversion of the display colors of the display.
 Display alerts                    Alarm indicator on the display.
 Display language                  Language of the display texts.




8022709.1ML4/2024-03-11 | SICK                                                                                T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors            17
Subject to change without notice

8 SERVICE DATA


NOTE
The availability of the individual functions is device-specific.

Table 21: General device settings - Eco mode
ISDU
                                                                            Data reposi‐                      Default
Index             Sub-        Name                            Data type                    Length    Access               Value/range
                                                                            tory                              value
DEC     HEX       index

                                                                                                                          0 = Off
235     IB        0           Eco mode                        UInt          yes            3 bytes   rw       0
                                                                                                                          1 = On


When activating eco mode, the display is deactivated 20 s after the last entry.

Table 22: General device settings – Inverter external input
ISDU
                                                                            Data stor‐                        Default
Index             Sub-        Name                            Data type                    Length    Access               Value/Range
                                                                            age                               value
Dec     Hex       index

                                                                                                                          0 = Not inverted
1093    445       -           Inverter external input         UInt          yes            1 byte    rw       0
                                                                                                                          1 = Inverted


If the Inverter external input is activated, all binary input signals read via pin 2 are inverted before device-internal
processing. Teach-in input signals are exceptions. These are always processed non-inverted regardless of the
Inverter external input setting.

NOTE
Depending on the device generation, the Inverter external input only functions for Smart Task input signals and
therefore depending on the setting under ISDU 121 Pin 2 configuration.

Table 23: General device settings - Device ID setup
ISDU
                                                                            Data reposi‐                      Default
Index             Sub-        Name                            Data type                    Length    Access               Value/Range
                                                                            tory                              value
Dec     Hex       index

16000   3E80      -           Device ID setup                 UInt          no             4 bytes   rw       Device ID   Device specific


You can use Device ID setup to set which Device-ID the sensor should work with (according to the value range
supported by the respective sensor). Individual IO-Link device parameters and possibly also the IO-Link device
behavior differ depending on the Device-ID setting. By switching the Device-ID, for example, a fundamentally
different device mode can be activated or the IO-Link-related device behavior of an already controlled predecessor
device can be activated in the current device, thus establishing backwards compatibility.
Switching to Device-ID only takes effect the next time the device is started up.

NOTE
If an older Device-ID is activated, the index 16000 Device ID setup may disappear from the index space of the sensor.
In this case, the system command Restore Factory Settings (index 2, value 130) can be used to restore the default
Device-ID, which supports index 16000 Device ID setup.


NOTE
The IO-Link parameters and IO-Link communication properties for each supported Device-ID are described in the
corresponding IODD.




18        T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                           8022709.1ML4/2024-03-11 | SICK
                                                                                                                                       Subject to change without notice

SERVICE DATA 8


8.3                Teach-in/detection settings for WTB, WTF, WTM, WTL and WTS devices
Table 24: Teach-in/detection - Standard Command
 ISDU
                                                                Data reposi‐                                 Default
 Index             Sub-      Name                   Data type                  Length           Access                       Value/range
                                                                tory                                         value
 DEC       HEX     Index

                                                                                                                             65 = Single value teach / Teach SP1
                                                                                                                             67 = Teach SP1 TP1
 2         2       -         Standard command       UInt        -              1 byte           wo           -
                                                                                                                             68 = Teach SP1 TP2
                                                                                                                             79 = Abort Teach-in sequence


After triggering the command Single value teach or Teach SP1 , the current distance between the sensor and the
object in the light beam is set as the sensing range. Qint.1 SP1 sensing range (index 60) and Qint.2 SP1 sensing range
(index 62) change accordingly.
Alternatively, the sensing range can also be set by first teaching the distance between the sensor and the
object (→ command Teach SP1 TP1) and then teaching the distance between the sensor and the background (→
command Teach SP1 TP2). This completes the teach-in sequence and the sensing range is placed in the middle of
the two teach-in points. The command Teach SP1 TP2 is only executed by the sensor if the command Teach SP1 TP1
has been issued beforehand. Instead of the second command Teach SP1 TP2, this teach-in sequence can also be
ended using the command Abort Teach-in sequence; the last valid SP1 is retained. Teach SP1 TP1 and Teach SP1 TP2 is
only available in the Operation modes "BGS ..." (see index 83).

NOTE
The command Single value teach or Teach SP1 can also be triggered as follows:
•        Triggering teach-in using the teach-in button on the sensor housing (if present).
•        Triggering the teach-in using the HIGH signal (L+) on pin 2 (when Pin 2 configuration (index 121)) is set to
         Teach-in ).


NOTE
Dependency:
•        Teach-in channel (Index 58)
•        Qint.1 SP1 sensing range (Index 60)
•        Qint.2 SP1 sensing range (Index 62)
•        Operation mode (Index 83)
•        Quality of Teach (Index 114)

Table 25: Teach-in/detection - Teach-in channel / Teach state
 ISDU
                                                                Data reposi‐                                 Default
 Index             Sub-      Name                   Data type                  Length           Access                       Value/range
                                                                tory                                         value
 DEC       HEX     Index

                                                                                                                             0 = Default Qint. = Qint.1
 58        3A      -         Teach-in channel       UInt        no             1 byte           rw           0               1 = Qint.1
                                                                                                                             2 = Qint.2
                             Teach-in state         Record                     1 byte

                                                                               1 bit                                         0 = SP1 TP2 not taught or not successfull
                             Teach flag SP1 TP2     Boolean
                                                                               (Offset 5 bit)                                1 = SP1 TP2 successfully taught

                                                                               1 bit                                         0 = SP1 (TP1) not taught or not successfull
                             Teach flag (SP1 TP1)   Boolean
 59        3B      -                                            -              (Offset 4 bit)   ro           -               1 = SP1 (TP1) successfully taught
                                                                                                                             0 = IDLE
                                                                                                                             1 = SP1 SUCCESS
                                                                               4 bit
                             Teach state            UInt                                                                     4 = WAIT FOR COMMAND
                                                                               (Offset 0 bit)
                                                                                                                             5 = BUSY
                                                                                                                             7 = ERROR


Teach-in channel allows you to select the Qint. channel to which the teach-in commands (index 2, value 65, 67
and 68) apply. Depending on the device type, only one teach-in channel is available for the teach-in process. No
teach-in channel other than the preset one can then be used.
The Teach-in state shows the current status of the teach-in procedure.



8022709.1ML4/2024-03-11 | SICK                                                                   T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors           19
Subject to change without notice

8 SERVICE DATA

A teach-in can only be sent in IDLE, SP1 SUCCESS and ERROR status. The status always refers to the Qint. channel
currently selected in Teach-in channel (index 58). The teach flags are designed according to the individual device
equipment.

Table 26: Teach-in/detection - Qint.1
ISDU
                                                                             Data reposi‐                               Default
Index              Sub-        Name                            Data type                    Length             Access                 Value/range
                                                                             tory                                       value
DEC       HEX      Index

                   0           Qint.1 SP1 / SP2                Record                       3 bytes                     -
                                                                                                                        device spe‐
60        3C       1           Qint.1 SP1 sensing range                      yes            16 bits            rw                     device specific
                                                                                                                        cific
                   2           Qint.1 SP2 sensing range                                     8 bits                      -             not used
                   0           Qint.1 configuration            Record                       4 bytes                     -
                                                                                            8 bits
                   1           Qint.1 Switchpoint logic                                                                 128           128 = Vendor specific
                                                                                            (Offset 24 bits)
61        3D                                                                 yes            8 bits             rw
                   2           Qint.1 Switchpoint mode                                                                  128           128 = Vendor specific
                                                                                            (Offset 16 bits)
                                                                                            16 bits
                   3           Qint.1 Switchpoint hysteresis                                                            0             0 = Auto-defined hysteresis
                                                                                            (Offset 0 bits)


Qint.1 SP1 sensing range can be used to adjust the switching distance of the sensor (in mm).
The permissible value range is device-specific and can be found in the data sheet of the respective sensor.
Depending on the device generation, value inputs are accepted over the full 16-bit value range and, if necessary,
automatically corrected by the sensor to the permissible maximum or minimum (older device generations, recog‐
nizable by a value range according to IODD of 0 ... 65535). With newer device generations, the value range
according to IODD already corresponds to the actual operating distance range of the device plus ten percent;
entries beyond this value range are rejected with an error message. The previous input value is retained.
If the current distance between sensor and detection object is the same or less than the set Qint.1 SP1 sensing range
value, the Qint.1 detection signal switches to HIGH.
The selected sensing range can be overwritten by:
•       Triggering teach-in using the teach-in button on the sensor housing.
•       Triggering teach-in using the HIGH signal (L+) on pin 2 (when Pin 2 configuration (index 121) is set to Teach-in ).
Qint.1 SP2 sensing range has no function.
Depending on the device, Qint.1 SP1 / SP2 (index 60) and Qint.2 SP1 / SP2 (index 62) are synchronized with each
other.
A change to one index is automatically applied to the other index.

NOTE
Dependency:
•       Single value teach system command (index 2, value 65).
•       Qint.2 SP1 sensing range (Index 62).

Qint.1 Switchpoint logic has no function.
Qint.1 Switchpoint mode has no function.
Qint.1 Switchpoint hysteresishas no function.

Table 27: Teach-in/detection - Qint.2
ISDU
                                                                             Data reposi‐                               Default
Index              Sub-        Name                            Data type                    Length             Access                 Value/range
                                                                             tory                                       value
DEC       HEX      Index

                   0           Qint.2 SP1 / SP2                Record                       3 bytes                     -
                                                                                                                        device spe‐
62        3E       1           Qint.2 SP1 sensing range                      yes            16 bits            rw                     device specific
                                                                                                                        cific
                   2           Qint.2 SP2 sensing range                                     8 bits                      -             not used




20         T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                                       8022709.1ML4/2024-03-11 | SICK
                                                                                                                                                    Subject to change without notice

SERVICE DATA 8


 ISDU
                                                                         Data reposi‐                                   Default
 Index             Sub-      Name                            Data type                  Length             Access                       Value/range
                                                                         tory                                           value
 DEC        HEX    Index

                   0         Qint.2 configuration            Record                     4 bytes                         -
                                                                                        8 bits
                   1         Qint.2 Switchpoint logic                                                                   128             128 = Vendor specific
                                                                                        (Offset 24 bits)
 63         3F                                                           yes            8 bits             rw
                   2         Qint.2 Switchpoint mode                                                                    128             128 = Vendor specific
                                                                                        (Offset 16 bits)
                                                                                        16 bits
                   3         Qint.2 Switchpoint hysteresis                                                              0               0 = Auto-defined hysteresis
                                                                                        (Offset 0 bits)


The switching distance of the sensor can be set via Qint.2 SP1 sensing range (in mm).
The permissible value range is device-specific and can be found in the data sheet of the respective sensor.
Depending on the device generation, value inputs are accepted over the full 16-bit value range and, if necessary,
automatically corrected by the sensor to the permissible maximum or minimum (older device generations, recog‐
nizable by a value range according to IODD of 0 ... 65535). With newer device generations, the value range
according to IODD already corresponds to the actual operating distance range of the device plus ten percent;
entries beyond this value range are rejected with an error message. The previous input value is retained.
If the current distance between sensor and detection object is the same or less than the set Qint.2 SP1 sensing range
value, the Qint.2 detection signal switches to HIGH.
The selected sensing range can be overwritten by:
•        Triggering teach-in using the teach-in button on the sensor housing.
•        Triggering teach-in using the HIGH 1) signal on pin 2 (if Pin 2 configuration (index 121) is set to Teach-in ).
Qint.2 SP2 sensing range has no function.
Depending on the device, Qint.1 SP1 / SP2 (index 60) and Qint.2 SP1 / SP2 (index 62) are synchronized with each
other. Any changes made to one of the ISDUs are automatically accepted by the other ISDU.

NOTE
Dependency:
•        Single value teach system command (index 2, value 65).
•        Qint.1 SP1 sensing range (Index 60).

Qint.2 Switchpoint logic has no function.
Qint.2 Switchpoint mode has no function.
Qint.2 Switchpoint hysteresis has no function.

Table 28: Teach-in/detection - Detection mode
 ISDU
                                                                         Data reposi‐                                   Default
 Index             Sub-      Name                            Data type                  Length             Access                       Value/range
                                                                         tory                                           value
 DEC        HEX    Index

                                                                                                                                        0 = Switching mode
 83         53     -         Detection mode                  UInt        yes            1 byte             rw           0
                                                                                                                                        1 = Distance measuring mode


Photoelectric proximity sensors which can not only detect binary detection signals, but also the distance to the
object, feature the Detection mode function. Depending on the setting, the photoelectric proximity sensor is in
switching or measuring mode.
The setting of Detection mode also affects Process data select (Index120):
•        In the setting "0 = Switching mode", Process data select is automatically set to "0 = Switching signals".
•        In the setting "1 = Distance measuring mode", Process data select is automatically set to "1 = Distance to object".

NOTE
Dependency:
•        Process data select (Index 120)


1)       HIGH = signal level on L+

8022709.1ML4/2024-03-11 | SICK                                                                              T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   21
Subject to change without notice

8 SERVICE DATA

Table 29: Teach-in/Detection - Operation mode
ISDU
                                                                              Data reposi‐                     Default
Index               Sub-        Name                            Data type                    Length   Access             Value/range
                                                                              tory                             value
DEC       HEX       Index

                                                                                                                         0 = BGS Qint.1, 1 point teach, AS 1
                                                                                                                         1 = BGS Qint.1, 1 point teach, AS 2
                                                                                                                         2 = BGS Qint.1, 2 point teach, AS 1
83        53        -           Operation mode                  UInt          yes            1 byte   rw       0
                                                                                                                         4 = BGS Qint.1 and Qint.2, 1 point teach, AS 1
                                                                                                                         6 = FGS Qint.1, 1 point teach, AS 1
                                                                                                                         16 = Distance measurement


In newer generation devices, index 83 as an Operation mode performs more functions. Explanation of abbreviations:
BGS = Background sup‐                 Setting the switching point to the surface of the object to be detected or slightly behind it. Objects
pression                              further away are not detected. Objects at the switching point or closer objects are detected.
FGS = Foreground sup‐                 Setting the switching point to an unchangeable, fixed background object (e.g. machine part) within
pression                              the maximum sensor scanning range according to the data sheet. Closer objects and a loss of the
                                      optical signal (e.g. due to reflection) are interpreted by the sensor as object detection.
AS = ApplicationSelect                Enables an application-specific fine adjustment of the selected Operation mode.
                                      ApplicationSelect 1: Standard scanning range of the sensor with maximum switching frequency.
                                      ApplicationSelect 2: Increases the scanning range of the sensor and improves the detection of black
                                      and obliquely-oriented objects. This also reduces the switching frequency of the sensor.

The various operating modes correspond to the corresponding settings that can be made via the BluePilot control
unit on the sensor itself.
Functioning in detail:
BGS Qint.1, 1 point teach,            Activates BGS mode on Qint.1 with AS 1 or AS 2. The teach-in variant is also defined, which can be
AS 1                                  activated using the teach-in button on the sensor housing.
BGS Qint.1, 1 point teach,            “1 point teach” corresponds to the Teach SP1 system command (index 2, value 65). “2 point teach”
AS 2                                  corresponds to the Teach SP1 TP1 and Teach SP1 TP2 system command (index 2, value 67 and 68).
                                      Regardless of the mode selected here, any teach-in command via system command (index 2) can be
BGS Qint.1, 2 point teach,            used. Qint.2 has no function in these modes.
AS 1
BGS Qint.1 and Qint.2, 1              Activates BGS mode on Qint.1 and Qint.2 with AS 1. Defined teach-in variant that can be triggered
point teach, AS 1                     via the teach-in button on the sensor housing:
                                      “1 point teach” corresponds to the Teach SP1 system command (index 2, value 65). Regardless of this
                                      mode, any teach-in command via system command (index 2) can be used.
FGS Qint.1, 1 point teach,            Activates FGS mode on Qint.1 with AS 1. Defined teach-in variant that can be triggered via the
AS 1                                  teach-in button on the sensor housing and via system command (index 2):
                                      “1 point teach” or Teach SP1 system command (index 2, value 65). System command Teach SP1 TP1
                                      and Teach SP1 TP2 (index 2, value 67 and 68) are not available. Qint.2 has no function in this mode.
BGS Window Qint.1 and                 Activates BGS mode on Qint.1 and Qint.2 with AS 1. Defined teach-in variant that can be triggered
Qint.2, 1 point teach, AS 1           via the teach-in button on the sensor housing:
                                      “1 point teach” corresponds to the Teach SP1 system command (index 2, value 65). Regardless
                                      of this mode, any teach-in command via system command (index 2) can be used. The window
                                      function is implemented via the logical connection of the Qint.1 and Qint.2 signals in the Smart Task
                                      A00 → see see "Smart Task “Basic logic” (A00)", page 42. The relevant smart task indices are
                                      reconfigured accordingly.
Distance measurement                  Activates the distance measurement function. Teach-in commands as well as Qint.1 and Qint.2 are
                                      not available.

The Operation mode setting also affects Process data select (Index120):
•       In the “16 = Distance measuring” setting, Process data select is automatically set to “1 = Distance to object”.
•       For all other settings, Process data select is automatically set to “0 = Switching signals”.

NOTE
Dependency:
•       Process data select (Index 120)



22          T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                        8022709.1ML4/2024-03-11 | SICK
                                                                                                                                      Subject to change without notice

SERVICE DATA 8


Table 30: Teach-in/Detection - Teach-in offset
 ISDU
                                                                         Data reposi‐                             Default
 Index             Sub-      Name                            Data type                  Length       Access                       Value/range
                                                                         tory                                     value
 DEC      HEX      Index

                                                                                                                                  -100 … +100
 90       5A       -         Teach-in offset                 Int         yes            1 byte       rw           0               Alternatively:
                                                                                                                                  -50 … +50



When this function is in use, when triggering a teach-in command (via the teach-in button on the sensor housing or
via the Single value teach system command (ISDU 2, value 65)), the defined detection point is corrected by the set
value.
This function makes it possible to increase detection reliability, especially for teach-in ongoing processes, by
moving the detection point with the Teach-in offset e.g. “into the object”.

NOTE
Dependency:
Single value teach system command (ISDU 2, value 65)


NOTE
The Teach-in offset does not work if a sensing range is set directly via Qint.x SP1/SP2 (ISDU 60/62).

Table 31: Teach-in/Detection - Current receiver level
 ISDU
                                                                         Data reposi‐                             Default
 Index             Sub-      Name                            Data type                  Length       Access                       Value/range
                                                                         tory                                     value
 DEC      HEX      Index

 180      B4       -         Current receiver level (live)   UInt        -              1 byte       ro           -               0 ... 16383


Current receiver level (live) shows the sensor’s current energy-related receiver level as an absolute value in digits. This
value therefore delivers additional information about the object on which the sensor light spot falls at the time of
read out.
The displayed value is not affected by the teach-in or from other sensor settings. It also does not directly affect the
detection behavior of the sensor. The value is not calibrated and can fluctuate from sensor to sensor.

Table 32: Teach-in/Detection - Distance to object
 ISDU
                                                                         Data reposi‐                             Default
 Index             Sub-      Name                            Data type                  Length       Access                       Value/range
                                                                         tory                                     value
 DEC      HEX      Index

                   0         Distance to object              Record                     3 bytes
                                                                                        16 bits
                   1         Distance                        UInt                                                                 0 … 30000
 229      E5                                                             -              (Offset 8)   ro           -
                                                                                        2 bits                                    0 = Distance in range / valid
                   2         Distance qualifier              UInt
                                                                                        (Offset 0)                                3 = No distance information / distance invalid


This parameter can be used to output the measured distance to the object or the background (if available and in
sensing range) as a Distance in mm or 1/10 mm (depending on the device – see IODD of the respective device
for details). If no measured value can be detected (e.g. because the sensor is facing empty space) or if the
measured value is outside of the specified sensing range, the sensor delivers output value “30,000”, which is to
be interpreted as an invalid measurement.
Each measured value must be linked with the Distance qualifier. This value specifies whether the current output
measured value is valid or not.

NOTE
Separate access to sub-index 1 or 2 is not possible.




8022709.1ML4/2024-03-11 | SICK                                                                        T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors              23
Subject to change without notice

8 SERVICE DATA

8.4                   Teach-in / detection settings for WL and WLA devices
Table 33: Teach-in/Detection - Standard Command
ISDU
                                                                                Data reposi‐                              Default
Index                 Sub-        Name                            Data type                    Length            Access             Value/range
                                                                                tory                                      value
DEC       HEX         Index

2         2           -           Standard command                UInt          -              1 byte            wo       -         65 = Single value teach


For WL devices, we recommend performing a teach-in process after connecting the sensor and aligning it to the
reflector. This automatically adjusts the sensor’s receiver sensitivity, taking into account the current light receiver
level, so that the detection signal is as reliable as possible.
For WLA devices, a teach-in process is not required for detector-related reasons, as these systems guarantee
reliable and robust object detection even at maximum sensitivity (= delivery status).
To be able to use all of the following functions/parameters to their full extent, a teach-in process must be
triggered:
•       Qint.1 SP1 / SP2 (ISDU 60) or Qint.2 SP1 / SP2 (ISDU 62)
•       Quality of run (ISDU 175)
•       Quality of run alarm (ISDU 176)
•       Current receiver level (ISDU 180)
With every teach-in process, the sensor’s current light receiver level, Current receiver level (live) (ISDU 180), is
standardized at 100%. These 100% levels are the energy-based reference values for the aforementioned functions
and parameters. If the teach-in process is not performed, the reference value is undefined and the listed functions
and parameters do not deliver any valid information.
To achieve the same effect as the “Single value teach” standard command, you can trigger teach-in using the
teach-in pushbutton on the sensor housing (if present) or trigger teach-in via the HIGH signal (L+) at pin 2 (when
Pin 2 configuration (ISDU 121) is set to Teach-in).

NOTE
Dependency:
•       Qint.1 SP1 / SP2 (ISDU 60)
•       Qint.2 SP1 / SP2 (ISDU 62)
•       Quality of run (ISDU 175)
•       Quality of run alarm (ISDU 176)
•       Current receiver level (live) (ISDU 180)

Table 34: Teach-in/Detection - Teach-in channel / Teach state
ISDU
                                                                                Data reposi‐                              Default
Index                 Sub-        Name                            Data type                    Length            Access             Value/range
                                                                                tory                                      value
DEC       HEX         Index

58        3A          -           Teach-in channel                UInt          -              1 byte            rw       0         0 … 2 = Default BDC
                                  Teach-in state                  Record                       1 byte

                                                                                               1 bit                                0 = Teachpoint 1 not taught
                                  Teach flags
                                                                                               (Offset 4 bits)                      1 = Teachpoint 1 successfully taught
59        3B          -                                                         -                                ro       -
                                                                                                                                    0 = IDLE
                                                                                               4 bits                               1 = SP1 SUCCESS
                                  Teach state
                                                                                               (Offset 0 bits)                      5 = BUSY
                                                                                                                                    7 = ERROR


Selection of the Qint. channel that is affected by the Single value teach (ISDU 2, value 65) system command.
Only one teach-in channel is available for the teach-in process for WL and WLA devices. Only the preset teach-in
channel can be used.
The Teach state shows the current status of the teach-in process.
A teach-in process can only be performed when the status is IDLE, SP1 SUCCESS and ERROR.
The status always refers to the Qint. channel selected in Teach-in channel (ISDU 58).
The Teach flags have no function for WL and WLA devices.


24            T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                                 8022709.1ML4/2024-03-11 | SICK
                                                                                                                                                 Subject to change without notice

SERVICE DATA 8


Table 35: Teach-in / detection - Qint.1
 ISDU
                                                                              Data reposi‐                                   Default
 Index           Sub-        Name                                 Data type                  Length             Access                       Value/range
                                                                              tory                                           value
 DEC      HEX    Index

                 0           Qint.1 SP1 / SP2                     Record                     2 bytes                         -
                                                                                             8 bits
                 1           SP1 upper threshold (switch-on)                                                                 50              50
 60       3C                                                                                 (Offset 8 bits)
                                                                                             8 bits
                 2           SP2 lower threshold (switch-off)                                                                45              45
                                                                                             (Offset 0 bits)
                 0           Qint.1 configuration                 Record                     4 bytes                         -
                                                                              yes                               rw
                                                                                             8 bits
                 1           Switchpoint logic
                                                                                             (Offset 24 bits)
                                                                                                                             128             128 = Vendor specific
 61       3D                                                                                 8 bits
                 2           Switchpoint mode
                                                                                             (Offset 16 bits)
                                                                                             16 bits
                 3           Switchpoint hysteresis                                                                          0               0 = Auto-defined hysteresis
                                                                                             (Offset 0 bits)


Qint.1 SP1 / SP2 is used to defined the switch-on and switch-off threshold for the detection signal (as percentages).
The selected values are based on the energy-based receiver value (=100%) defined during the last teach-in
process.
SP1 upper threshold (switch-on): Switch-on threshold.
If the Current receiver level (live) (ISDU 180) exceeds the selected switch-on threshold, the Qint.1 detection signal
changes to LOW (no object detected in beam path).
SP2 lower threshold (switch-off): Switch-off threshold.
If the Current receiver level (live) (ISDU 180) falls below the set switch-off threshold, the Qint.1 detection signal
switches to HIGH (object detected in beam path).

NOTE
The default switch-on and switch-off thresholds cannot be adjusted in WL / WLA devices. This is only possible in
WLG devices (see "Teach-in / detection settings for WLG devices", page 26). The settings and their effects are
redundant to those in ISDU 62.


NOTE
Dependency:
•        Qint.2 SP1 / SP2 (ISDU 62)
•        Current receiver level (live) (ISDU 180)

Switchpoint logic has no function.
Switchpoint mode has no function.
Switchpoint hysteresis has no function.

Table 36: Teach-in / detection - Qint.2
 ISDU
                                                                              Data reposi‐                                   Default
 Index               Sub-      Name                               Data type                  Length             Access                       Value/range
                                                                              tory                                           value
 DEC       HEX       Index

                     0         Qint.2 SP1 / SP2                   Record                     2 bytes                         -
                                                                                             8 bits
                     1         SP1 upper threshold (switch-on)                                                               50              50
 62        3E                                                                                (Offset 8 bits)
                                                                                             8 bits
                     2         SP2 lower threshold (switch-off)                                                              45              45
                                                                                             (Offset 0 bit)
                     0         Qint.2 configuration               Record                     4 bytes                         -
                                                                              yes                               rw
                                                                                             8 bits
                     1         Switchpoint logic
                                                                                             (Offset 24 bits)
                                                                                                                             128             128 = Vendor specific
 63        3F                                                                                8 Bit
                     2         Switchpoint mode
                                                                                             (Offset 16 bits)
                                                                                             16 bits
                     3         Switchpoint hysteresis                                                                        0               0 = Auto-defined hysteresis
                                                                                             (Offset 0 bits)




8022709.1ML4/2024-03-11 | SICK                                                                                   T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   25
Subject to change without notice

8 SERVICE DATA

Qint.2 SP1 / SP2 is used to defined the switch-on and switch-off threshold for the detection signal (as percentages).
The selected values are based on the energy-based receiver value (=100%) defined during the last teach-in
process.
SP1 upper threshold (switch-on): Switch-on threshold.
If the Current receiver level (live) (ISDU 180) exceeds the selected switch-on threshold, the Qint.1 detection signal
changes to LOW (no object detected in beam path).
SP2 lower threshold (switch-off): Switch-off threshold.
If the Current receiver level (live) (ISDU 180) falls below the selected switch-off threshold, the Qint.1 detection signal
changes to HIGH (object detected in beam path).

NOTE
The default switch-on and switch-off thresholds cannot be adjusted in WL / WLA devices. This is only possible in
WLG devices (see "Teach-in / detection settings for WLG devices", page 26). The settings and their effects are
redundant to those in ISDU 60.


NOTE
Dependency:
•       Qint.1 SP1 / SP2 (ISDU 60)
•       Current receiver level (live) (ISDU 180)

Switchpoint logic has no function.
Switchpoint mode has no function.
Switchpoint hysteresis has no function.

Table 37: Teach-in / detection - Current receiver level
ISDU
                                                                                Data reposi‐                     Default
Index                 Sub-        Name                            Data type                    Length   Access             Value/range
                                                                                tory                             value
DEC       HEX         Index

180       B4          -           Current receiver level (live)   UInt          -              1 byte   ro       -         0 ... 255


Current receiver level (live) shows the sensor’s current energy-related receiver level (as a percentage). The reference
point (equivalent to 100%) is the Current receiver level (live) at the time of the last teach-in.
For further details, see the Single value teach standard command (ISDU 2, value 65).

NOTE
Dependency:
•       System command Single value teach (ISDU 2, value 65)


8.5                   Teach-in / detection settings for WLG devices
Table 38: Teach-in/detection - Standard Command
ISDU
                                                                                Data reposi‐                     Default
Index                 Sub-        Name                            Data type                    Length   Access             Value/range
                                                                                tory                             value
DEC       HEX         index

2         2           -           Standard command                UInt          -              1 byte   wo       -         65 = Single value teach


For WLG devices, a teach-in process must be performed after connecting the sensor and aligning it to the reflector.
This automatically adjusts the receiver sensitivity of the sensor, taking into account the current light reception
level, so that the detection signal is as reliable as possible, even for highly transparent objects.
In addition, with every teach-in, the current light reception level of the sensor, Current receiver level (live) (index 180),
is standardized at 100%. This 100% level is the energy reference value for the following appliance functions:
•       Qint.1 SP1 / SP2 (Index 60) or Qint.2 SP1 / SP2 (ISDU 62)
•       Quality of teach (Index 114)
•       Quality of run (Index 175)


26            T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                          8022709.1ML4/2024-03-11 | SICK
                                                                                                                                          Subject to change without notice

SERVICE DATA 8


•        Upper threshold (switch-on) dynamic (index 181); effective detector-related switch-on and switch-off thresholds
•        Lower threshold (switch-off) dynamic (index 182); effective detector-related switch-on and switch-off thresholds
The teach-in process must be repeated each time the sensor or reflector is realigned or whenever the sensor or
reflector is replaced in order to guarantee that the energy-related reference signal is always up-to-date, e.g., for
assessing contamination on the sensor’s front screen or the reflector. This also applies to the use of the data
repository function (see "Sensor replacement/data storage", page 60).
If the teach-in process is not performed, the reference value is undefined and the listed functions and parameters
do not deliver any valid information.
The Single value teach standard command has the same effect:
•        Triggering teach-in using the teach pushbutton on the sensor housing (if present).
•        Triggering teach-in using the HIGH signal (L+) on pin 2 (if Pin 2 configuration (index 12) is set to Teach-in ).

NOTE
Dependency:
•        Qint.1 SP1 / SP2 Index 60)
•        Qint.2 SP1 / SP2 (Index 62)
•        Quality of run (Index 175)
•        Quality of run alarm (Index 176)
•        Current receiver level (live) (Index 180)
•        Upper threshold (switch-on) dynamic (Index 181)
•        Lower threshold (switch-off) dynamic (Index 182)

Table 39: Teach-in/detection - Teach-in channel / Teach state
 ISDU
                                                            Data reposi‐                                  Default
 Index             Sub-      Name               Data type                  Length            Access                       Value/range
                                                            tory                                          value
 DEC       HEX     index

 58        3A      -         Teach-in channel   UInt        -              1 byte            rw           0               0 … 2 = Default BDC
                             Teach-in state     Record                     1 byte

                                                                           1 bit                                          0 = Teachpoint 1 not taught
                             Teach flags
                                                                           (Offset 4 bits)                                1 = Teachpoint 1 successfully taught
 59        3B      -                                        -                                ro           -
                                                                                                                          0 = IDLE
                                                                           4 bits                                         1 = SP1 SUCCESS
                             Teach state
                                                                           (Offset 0 bit)                                 5 = BUSY
                                                                                                                          7 = ERROR


Selection of the Qint. channel that is affected by the Single value teach system command (index 2, value 65).
With WLG devices, only one teach-in channel is available for the teach-in process. Only the preset teach-in channel
can be used.
The Teach state shows the current status of the teach-in process. A teach-in process can only be performed in the
status IDLE, SP1 SUCCESS and ERROR .
The status always refers to the Qint. channel currently selected via the Teach-in channel (index 58).
The Teach flags do not have a function for WLG devices.




8022709.1ML4/2024-03-11 | SICK                                                                T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors    27
Subject to change without notice

8 SERVICE DATA

Table 40: Teach-in/detection - Qint.1
ISDU
                                                                               Data reposi‐                               Default
Index               Sub-        Name                               Data type                  Length             Access             Value/range
                                                                               tory                                       value
DEC       HEX       index

                    0           Qint.1 SP1 / SP2                   Record                     2 bytes                     -

                                                                                              8 bits                                10 to 90
                    1           SP1 upper threshold (switch-on)                                                           90
60        3C                                                                                  (Offset 8 bits)                       110 to 200

                                                                                              8 bits                                5 to 85
                    2           SP2 lower threshold (switch-off)                                                          85
                                                                                              (Offset 0 bit)                        105 to 195
                    0           Qint.1 configuration               Record      yes            4 bytes            rw       -
                                                                                              8 bits
                    1           Switchpoint logic
                                                                                              (Offset 24 bits)
                                                                                                                          128       128 = Vendor specific
61        3D                                                                                  8 bits
                    2           Switchpoint mode
                                                                                              (Offset 16 bits)
                                                                                              16 bits
                    3           Switchpoint hysteresis                                                                    0         0 = Auto-defined hysteresis
                                                                                              (Offset 0 bits)


Table 41: Teach-in/detection - Qint.2
ISDU
                                                                               Data reposi‐                               Default
Index               Sub-        Name                               Data type                  Length             Access             Value/range
                                                                               tory                                       value
DEC       HEX       index

                    0           Qint.2 SP1 / SP2                   Record                     2 bytes                     -

                                                                                              8 bits                                10 to 90
                    1           SP1 upper threshold (switch-on)                                                           90
62        3E                                                                                  (Offset 8 bits)                       110 to 200

                                                                                              8 bits                                5 to 85
                    2           SP2 lower threshold (switch-off)                                                          85
                                                                                              (Offset 0 bits)                       105 to 195
                    0           Qint.2 configuration               Record      yes            4 bytes            rw       -
                                                                                              8 bits
                    1           Switchpoint logic
                                                                                              (Offset 24 bits)
                                                                                                                          128       128 = Vendor specific
63        3F                                                                                  8 bits
                    2           Switchpoint mode
                                                                                              (Offset 16 bits)
                                                                                              16 bits
                    3           Switchpoint hysteresis                                                                    0         0 = Auto-defined hysteresis
                                                                                              (Offset 0 bits)


Qint.1 / Qint.2 SP1 / SP2 is used to define the switch-on and switch-off threshold for the detection signal (as
percentages). The selected values are based on the energy-based receiver value (=100%) defined during the last
teach-in process.
SP1 upper threshold (switch-on)switch-on threshold.
If the Current receiver level (live) (index 180) exceeds the selected switch-on threshold or the dynamic switch-on
threshold (see AutoAdapt, index 112), the detection signal Qint.1 changes to LOW (no object detected in the beam
path).
SP2 lower threshold (switch-off)switch-off threshold.
If the Current receiver level (live) (index 180) falls below the selected switch-off threshold or the dynamic switch-off
threshold (see AutoAdapt, index 112), the detection signal Qint.1 changes to HIGH (object detected in the beam
path).
The switch-on threshold must always be higher than the switch-off threshold.
The minimum distance between the switch-on and switch-off threshold is 5% (= hysteresis).
Both switching thresholds must always be both below 100% or above 100%.
Depending on the mode selected via Detection Mode (index 83), the switch-on and switch-off thresholds are
automatically adjusted.
Qint.1 SP1 / SP2 (index 60) and Qint.2 SP1 / SP2 (index 62) are always synchronized.
Any changes made to one of the ISDUs are accepted by the other ISDU.

NOTE
Dependency:
•       Qint.1 SP1 / SP2 (Index 60)
•       Qint.2 SP1 / SP2 (Index 62)
•       Current receiver level (live) (Index 180)


28          T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                                   8022709.1ML4/2024-03-11 | SICK
                                                                                                                                                 Subject to change without notice

SERVICE DATA 8


Switchpoint logic has no function.
Switchpoint mode has no function.
Switchpoint hysteresis has no function.

Table 42: Teach-in/detection - Detection mode
 ISDU
                                                                                Data reposi‐                                         Default
 Index                Sub-         Name                             Data type                  Length                   Access                       Value/range
                                                                                tory                                                 value
 DEC       HEX        index

                                                                                                                                                     Value / Range set 1:
                                                                                                                                                     0 = Highly-transparent objects
                                                                                                                                                     1 = Semi-transparent objects
                                                                                                                                                     2 = Opaque objects
                                                                                                                                                     3 = Bottles / trays
                                                                                                                                                     4 = Foil tear
 83        53         -            Detection mode                   UInt        yes            1 byte                   rw           0
                                                                                                                                                     255 = Manual
                                                                                                                                                     Value / Range set 2:
                                                                                                                                                     0 = Transparent object mode
                                                                                                                                                     1 = Transparent film mode
                                                                                                                                                     2 = Non-transparent mode
                                                                                                                                                     3 = Manual mode


Value / Range set 1 or Value / Range set 2 is implemented depending on the device type.
Detection modes can be used to select how the sensor detects pre-defined object types.
The following factors change depending on the settings:
•        The switch-on and switch-off thresholds Qint.1 SP1 / SP2 (index 60) and Qint.2 SP1 / SP2 (index 62).
•        The settings for AutoAdapt / Continuous threshold adaption (index 112) according to the following table.

Table 43: Switching thresholds
                                                       Switch-on threshold                       Switch-off threshold                    AutoAdapt / Continuous switching threshold tracking
            Highly transparent objects                                           90%                                         85%                                                      On - time-based
             Semi-transparent objects                                            82%                                         77%                                                      On - time-based
                          Opaque objects                                         50%                                         45%                                                      On - time-based
                              Bottles/trays                                      90%                                         50%                                                      On - time-based
                                  Film tear                                     110%                                         105%                                                     On - time-based
                Transparent object mode                                          90%                                         85%                                                      On - time-based
                  Transparent film mode                                         110%                                         105%                                                     On - time-based
                  Non-transparent mode                                           50%                                         45%                                                                  Off
                                   Manual                                    As before                                  As before                                                           As before


Manual mode is activated as soon as the user manually accesses Qint.1 SP1 / SP2 (ISDU 60), Qint.2 SP1 / SP2 (ISDU
62) or AutoAdapt / Continuous threshold adaption (ISDU 112). Switching to manual mode itself does not change any of
the remaining parameters.

NOTE
Dependency:
•        Qint.1 SP1 / SP2 (index 60) or Qint.2 SP1 / SP2 (index 62); nominal detector switch-on and switch-off thresholds
•        AutoAdapt / Continuous threshold adaption (Index 112)
•        Threshold presetting (Index 113)

Table 44: Teach-in/detection - AutoAdapt
 ISDU
                                                                                Data reposi‐                                         Default
 Index                Sub-         Name                             Data type                  Length                   Access                       Value/range
                                                                                tory                                                 value
 DEC       HEX        index

                                                                                                                                                     0 = Off
                                   AutoAdapt / Continuous thresh‐
 112       70         -                                             UInt        yes            1 byte                   rw           0               1 = On – time based
                                   old adaption
                                                                                                                                                     2 = On – event based


AutoAdapt or Continuous threshold adaption cause the detector switch-on and switch-off thresholds to be adjusted
automatically if the sensor detects gradual contamination of the sensor’s front screen or reflector.
As a result, object detection remains stable and secure for longer, even for highly transparent objects. In addition,
cleaning cycles can be extended.

8022709.1ML4/2024-03-11 | SICK                                                                                           T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors          29
Subject to change without notice

8 SERVICE DATA


NOTE
The automatic adjustments of the switch-on and switch-off thresholds by AutoAdapt affect the dynamic switch-on
and switch-off threshold Upper threshold (switch-on) dynamic (index 181) and Lower threshold (switch-off) dynamic (index
182).
The adjustable switch-on and switch-off thresholds Qint.1 SP1 / SP2 (index 60) and Qint.2 SP1 / SP2 (index 62)
remain unaffected.
If the AutoAdapt causes the switch-on and switch thresholds under Qint.1 / Qint.2 to deviate from the dynamic
switch-on and switch-off thresholds, the dynamic switch-on and switch-off thresholds are always used to evaluate
the object detection.

Off                                  AutoAdapt is deactivated.
On – time based                      When this setting is used, the dynamic switching thresholds are adjusted as soon as
                                     the sensor detects that its front screen or reflector is contaminated. This setting is recom‐
                                     mended as the default setting.
On – event based                     With this setting, the dynamic switching thresholds are adjusted incrementally with each
                                     object detection (= event) if the sensor front screen or reflector is contaminated.

NOTE
Dependency:
•       Detection mode (Index 83)
•       Upper threshold (switch-on) dynamic (Index 181)
•       Lower threshold (switch-off) dynamic (Index 182)

Table 45: Teach-in / Threshold presetting
ISDU
                                                                              Data reposi‐                     Default
Index               Sub-        Name                            Data type                    Length   Access             Value/range
                                                                              tory                             value
DEC       HEX       index

                                                                                                                         0 = 10% (Transparent mode)
                                                                                                                         1 = 18% (Transparent mode)
113       71        -           Threshold presetting            UInt          yes            1 byte   rw       0         2 = 40% (Transparent mode)
                                                                                                                         3 = Non-transparent mode
                                                                                                                         4 = Manual mode


For Detection modes Transparent object mode and Transparent foil mode (index 83), the function Threshold presetting can be
used to set the signal attenuation above which object detection should be triggered. The highest sensitivity setting
is 10% and the lowest is 40%.
If Detection mode Non-transparent objects is selected, Threshold presetting automatically switches to Non-transparent
mode. If the switch-on and switch-off thresholds are adjusted manually via Qint.1 SP1 / SP2 (index 60 and 62),
Threshold presetting jumps to Manual mode.

NOTICE
Changes to Threshold presetting can cause the Detection modes (index 83) to change.


NOTE
This function is not available in all WLG devices.


NOTE
Dependency:
•       Detection mode (Index 83)
•       Upper threshold (switch-on) dynamic (Index 181)
•       Lower threshold (switch-off) dynamic (Index 182)
•       Qint.1 SP1 / SP2 (Index 60)
•       Qint.2 SP1 / SP2 (Index 62)




30          T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                       8022709.1ML4/2024-03-11 | SICK
                                                                                                                                     Subject to change without notice

SERVICE DATA 8


Table 46: Teach-in / detection - Current receiver level
 ISDU
                                                                         Data reposi‐                         Default
 Index             Sub-      Name                            Data type                  Length   Access                       Value/range
                                                                         tory                                 value
 DEC       HEX     index

 180       B4      -         Current receiver level (live)   UInt        -              1 byte   ro           -               0 ... 255


The Current receiver level (live) shows the current energy reception level of the sensor (as a percentage). The
reference point (equivalent to 100%) is the light receiver level at the time of the last teach-in.
For further details, see the Single value teach standard command (index 2, value 65).

NOTE
Dependency:
•        System command Single value teach (Index 2, value 65)

Table 47: Teach-in/detection - Threshold
 ISDU
                                                                         Data reposi‐                         Default
 Index             Sub-      Name                            Data type                  Length   Access                       Value/range
                                                                         tory                                 value
 DEC       HEX     index

                             Upper threshold (switch-on)
 181       B5      -                                         UInt        -              1 byte   ro           0               0 ... 255
                             dynamic
                             Lower threshold (switch-off)
 182       B6      -                                         UInt        -              1 byte   ro           0               0 ... 255
                             dynamic


The automatic adjustments of the switch-on and switch-off thresholds (in percent) by AutoAdapt / Continuous thresh‐
old adaption (index 112) affects the dynamic switch-on and switch-off thresholds Upper threshold (switch-on) dynamic
(index 181) and Lower threshold (switch-off) dynamic (index 182).
The switch-on and switch-off thresholds Qint.1 SP1 / SP2 (index 60) and Qint.2 SP1 / SP2 (index 62) that can be
adjusted by the operator, remain unaffected.
If the AutoAdapt function causes the switch-on or switch-off thresholds in Qint.1 / Qint.2 to deviate from the dynamic
switch-on or switch-off threshold, the dynamic switch-on and switch-off thresholds are always used to evaluate the
object detection.

NOTE
Dependency:
•        AutoAdapt (Index 112)


8.6                Teach-in / detection settings for WE / WEO devices
Table 48: Teach-in/detection - Standard Command
 ISDU
                                                                         Data reposi‐                         Default
 Index             Sub-      Name                            Data type                  Length   Access                       Value/range
                                                                         tory                                 value
 DEC       HEX     index

 2         2       -         Standard command                UInt        -              1 byte   wo           -               65 = Single value teach


After connecting the sender and receiver devices and aligning them with each other, a teach-in must be triggered
in order to make full use of the functions described below.
With every teach-in process, the sensor’s current light receiver level is standardized at 100%. This 100% level is
the energy reference value for the following appliance functions:
•        Quality of teach (Index 114)
•        Quality of run (Index 175)
The teach-in process should be repeated again after each realignment of the sender or receiver and after each
replacement of the sender or receiver in order to always ensure an up-to-date energy reference signal, e.g. for
evaluating the contamination on the sender's or receiver’s front screen.
For WE/WEO devices, the teach-in process automatically adjusts the sensor’s receiver sensitivity, taking into
account the current light receiver level, so that the detection signal is as reliable as possible.


8022709.1ML4/2024-03-11 | SICK                                                                    T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   31
Subject to change without notice

8 SERVICE DATA

Triggering the teach-in process using the teach button on the sensor housing (if available) and triggering the
teach-in process using the HIGH signal (L+) on pin 2 (if Pin 2 configuration (index 121) is set to Teach-in is set), if
available.

NOTE
Dependency:
•       Quality of run or operating reserve (index 175)

Table 49: Teach-in/detection - Teach-in channel / Teach state
ISDU
                                                                              Data reposi‐                               Default
Index              Sub-        Name                               Data type                  Length             Access             Value/range
                                                                              tory                                       value
DEC       HEX      index

58        3A       -           Teach-in channel                   UInt        -              1 byte             rw       0         0 … 2 = Default BDC
                               Teach-in state                     Record                     1 byte

                                                                                             1 bit                                 0 = Teachpoint 1 not taught
                               Teach flags
                                                                                             (Offset 4 bits)                       1 = Teachpoint 1 successfully taught
59        3B       -                                                          -                                 ro       -
                                                                                                                                   0 = IDLE
                                                                                             4 bits                                1 = SP1 SUCCESS
                               Teach state
                                                                                             (Offset 0 bit)                        5 = BUSY
                                                                                                                                   7 = ERROR


Selection of the Qint. channel that is affected by the Single value teach system command (index 2, value 65).
For WE/WEO devices, only one teach-in channel is available for the teach-in process. Only the preset teach-in
channel can be used.
The Teach state shows the current status of the teach-in process.
A teach-in can only be sent in the status IDLE, SP1 SUCCESS and ERROR .
The status always refers to the Qint. channel currently selected via Teach-in channel (index 58).
The Teach flags do not have a function for WE/WEO devices.

Table 50: Teach-in/detection - Qint.1
ISDU
                                                                              Data reposi‐                               Default
Index              Sub-        Name                               Data type                  Length             Access             Value/range
                                                                              tory                                       value
DEC       HEX      index

                   0           Qint.1 SP1 / SP2                   Record                     2 bytes                     -
                                                                                             8 bits
                   1           SP1 upper threshold (switch-on)                                                           0         0
60        3C                                                                                 (Offset 8 bits)
                                                                                             8 bits
                   2           SP2 lower threshold (switch-off)                                                          0         0
                                                                                             (Offset 0 bits)
                   0           Qint.1 configuration               Record                     4 bytes                     -
                                                                              yes                               rw
                                                                                             8 bits
                   1           Switchpoint logic
                                                                                             (Offset 24 bits)
                                                                                                                         128       128 = Vendor specific
61        3D                                                                                 8 bits
                   2           Switchpoint mode
                                                                                             (Offset 16 bits)
                                                                                             16 bits
                   3           Switchpoint hysteresis                                                                    0         0 = Auto-defined hysteresis
                                                                                             (Offset 0 bits)


SP1 upper threshold (switch-on) has no function.
SP2 lower threshold (switch-off) has no function.
Switchpoint logic has no function.
Switchpoint mode has no function.
Switchpoint hysteresis has no function.




32         T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                                   8022709.1ML4/2024-03-11 | SICK
                                                                                                                                                Subject to change without notice

SERVICE DATA 8


Table 51: Teach-in/detection - Qint.2
 ISDU
                                                                            Data reposi‐                                   Default
 Index             Sub-      Name                               Data type                  Length             Access                       Value/range
                                                                            tory                                           value
 DEC       HEX     index

                   0         Qint.2 SP1 / SP2                   Record                     2 bytes                         -
                                                                                           8 bits
                   1         SP1 upper threshold (switch-on)                                                               0               0
 62        3E                                                                              (Offset 8 bits)
                                                                                           8 bits
                   2         SP2 lower threshold (switch-off)                                                              0               0
                                                                                           (Offset 0 bits)
                   0         Qint.2 configuration               Record                     4 bytes                         -
                                                                            yes                               rw
                                                                                           8 bits
                   1         Switchpoint logic
                                                                                           (Offset 24 bits)
                                                                                                                           128             128 = Vendor specific
 63        3F                                                                              8 bits
                   2         Switchpoint mode
                                                                                           (Offset 16 bits)
                                                                                           16 bits
                   3         Switchpoint hysteresis                                                                        0               0 = Auto-defined hysteresis
                                                                                           (Offset 0 bits)


SP1 upper threshold (switch-on) has no function.
SP2 lower threshold (switch-off) has no function.
Switchpoint logic has no function.
Switchpoint mode has no function.
Switchpoint hysteresis has no function.

8.7                Teach-in/Detection settings for WTT devices
Table 52: Teach-in/detection - Teach Command
 ISDU
                                                                            Data reposi‐                                   Default
 Index             Sub-      Name                               Data type                  Length             Access                       Value/range
                                                                            tory                                           value
 DEC       HEX     Index

                                                                                                                                           65 = Single Value Teach SP1
 2         02      -         Standard command                   UInt        -              1 byte             wo
                                                                                                                                           66 = Single Value Teach SP2


After the teach-in command has been triggered, the current distance between the sensor and the object in
the light beam is set as the sensing range. Depending on the selected Teach-in channel (index 58), Qint.x SP1
sensing range or Qint.x SP2 sensing range (index 60, 62, 16384, 16386, 16388, 16390, 16392 or 16394) change
accordingly.

NOTE
Dependency:
•        Teach-in channel (Index 58)
•        Qint.x SP1 sensing range or Qint.x SP2 sensing range (ISDU 60, 62, 16384, 16386, 16388, 16390, 16392 or
         16394)

Table 53: Teach-in/detection - Teach-in channel / Teach state
 ISDU
                                                                            Data reposi‐                                   Default
 Index             Sub-      Name                               Data type                  Length             Access                       Value/range
                                                                            tory                                           value
 DEC       HEX     Index

                                                                                                                                           0 = Default Qint = Qint.1
                                                                                                                                           1 = Qint.1
                                                                                                                                           2 = Qint.2
                                                                                                                                           3 = Qint.3
 58        3A      -         Teach-in channel                   UInt        -              1 byte             rw           0               4 = Qint.4
                                                                                                                                           5 = Qint.5
                                                                                                                                           6 = Qint.6
                                                                                                                                           7 = Qint.7
                                                                                                                                           8 = Qint.8




8022709.1ML4/2024-03-11 | SICK                                                                                 T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   33
Subject to change without notice

8 SERVICE DATA

ISDU
                                                                            Data reposi‐                               Default
Index             Sub-        Name                            Data type                    Length             Access                 Value/range
                                                                            tory                                       value
DEC      HEX      Index

                  0           Teach-in state                  Record                       1 byte
                                                                                           1 bit                                     0 = Teachpoint not taught
                  1           Teach flag SP2
                                                                                           (Offset 6 bits)                           1 = Teachpoint successfully taught
                                                                                           1 bit                                     0 = Teachpoint not taught
                  2           Teach flag SP1
59       3B                                                                 -              (Offset 4 bits)    ro       -             1 = Teachpoint successfully taught
                                                                                                                                     0 = IDLE
                                                                                                                                     1 = SP1 SUCCESS
                                                                                           4 bits
                  3           Teach state                                                                                            2 = SP2 SUCCESS
                                                                                           (Offset 0 bits)
                                                                                                                                     5 = BUSY
                                                                                                                                     7 = ERROR


Selection of the Qint. channel that affects the Single value teach SP1 / SP2 system command (index 2, value 65 or
value 66).
The Teach state shows the current status of the teach-in process.
A teach-in can only be sent in the status IDLE, SP1 SUCCESS, SP2 SUCCESS and ERROR .
The status always refers to the Qint. channel currently selected in Teach-in channel (index 58). The Teach flags have
no function for WTT devices.

Table 54: Teach-in/detection - Qint.1 ... Qint.8
ISDU
                                                                            Data reposi‐                               Default
Index             Sub-        Name                            Data type                    Length             Access                 Value/range
                                                                            tory                                       value
DEC      HEX      Index

                  0           Qint.1 SP1 / SP2                Record                       4 bytes                     -
                                                                                           16 bits                     device spe‐
                  1           Qint.1 SP1 sensing range        UInt                                                                   0 … 65535
60       3C                                                                 yes            (Offset 16 bits)   rw       cific
                                                                                           16 bits                     device spe‐
                  2           Qint.1 SP2 sensing range        UInt                                                                   0 … 65535
                                                                                           (Offset 0 bits)             cific
                  0           Qint.1 configuration            Record                       4 bytes                     -
                                                                                           8 bits
                  1           Qint.1 Switchpoint logic        UInt                                                     0             0 = not inverted
                                                                                           (Offset 24 bits)
                                                                                                                                     0 = Deactivated
61       3D                                                                 yes            8 bits             rw                     1 = Single point mode
                  2           Qint.1 Switchpoint mode         UInt                                                     1
                                                                                           (Offset 16 bits)                          2 = Window mode
                                                                                                                                     3 = Two point mode
                                                                                           16 bits
                  3           Qint.1 Switchpoint hysteresis   UInt                                                     0             0 = Vendor specific default
                                                                                           (Offset 0 bits)
                  0           Qint.2 SP1 / SP2                Record                       4 bytes                     -
                                                                                           16 bits                     device spe‐
                  1           Qint.2 SP1 sensing range        UInt                                                                   0 … 65535
62       3E                                                                 yes            (Offset 16 bits)   rw       cific
                                                                                           16 bits                     device spe‐
                  2           Qint.2 SP2 sensing range        UInt                                                                   0 … 65535
                                                                                           (Offset 0 bits)             cific
                  0           Qint.2 configuration            Record                       4 bytes                     -
                                                                                           8 bits
                  1           Qint.2 Switchpoint logic        UInt                                                     0             0 = not inverted
                                                                                           (Offset 24 bits)
                                                                                                                                     0 = Deactivated
63       3F                                                                 yes            8 bits             rw                     1 = Single point mode
                  2           Qint.2 Switchpoint mode         UInt                                                     1
                                                                                           (Offset 16 bits)                          2 = Window mode
                                                                                                                                     3 = Two point mode
                                                                                           16 bits
                  3           Qint.2 Switchpoint hysteresis   UInt                                                     0             0 = Vendor specific default
                                                                                           (Offset 0 bits)
                  0           Qint.3 SP1 / SP2                Record                       4 bytes                     -
                                                                                           16 bits                     device spe‐
                  1           Qint.3 SP1 sensing range        UInt                                                                   0 ... 65535
16384    4000                                                               yes            (Offset 16 bits)   rw       cific
                                                                                           16 bits                     device spe‐
                  2           Qint.3 SP2 sensing range        UInt                                                                   0 ... 65535
                                                                                           (Offset 0 bits)             cific
                  0           Qint.3 configuration            Record                       4 bytes                     -
                                                                                           8 bits
                  1           Qint.3 Switchpoint mode         UInt                                                     0             0 = not inverted
                                                                                           (Offset 24 bits)
                                                                                                                                     0 = Deactivated
16385    4001                                                               yes            8 bits             rw                     1 = Single point mode
                  2           Qint.3 Switchpoint mode         UInt                                                     1
                                                                                           (Offset 16 bits)                          2 = Window mode
                                                                                                                                     3 = Two point mode
                                                                                           16 bits
                  3           Qint.3 Switchpoint hysteresis   UInt                                                     0             0 = Vendor specific default
                                                                                           (Offset 0 bits)




34        T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                                      8022709.1ML4/2024-03-11 | SICK
                                                                                                                                                  Subject to change without notice

SERVICE DATA 8


 ISDU
                                                                         Data reposi‐                                   Default
 Index             Sub-      Name                            Data type                  Length             Access                       Value/range
                                                                         tory                                           value
 DEC      HEX      Index

                   0         Qint.4 SP1 / SP2                Record                     4 bytes                         -
                                                                                        16 bits                         device spe‐
                   1         Qint.4 SP1 sensing range        UInt                                                                       0 ... 65535
 16386    4002                                                           yes            (Offset 16 bits)   rw           cific
                                                                                        16 bits                         device spe‐
                   2         Qint.4 SP2 sensing range        UInt                                                                       0 ... 65535
                                                                                        (Offset 0 bits)                 cific
                   0         Qint.4 configuration            Record                     4 bytes                         -
                                                                                        8 bits
                   1         Qint.4 Switchpoint logic        UInt                                                       0               0 = not inverted
                                                                                        (Offset 24 bits)
                                                                                                                                        0 = Deactivated
 16387    4003                                                           yes            8 bits             rw                           1 = Single point mode
                   2         Qint.4 Switchpoint mode         UInt                                                       1
                                                                                        (Offset 16 bits)                                2 = Window mode
                                                                                                                                        3 = Two point mode
                                                                                        16 bits
                   3         Qint.4 Switchpoint hysteresis   UInt                                                       0               0 = Vendor specific default
                                                                                        (Offset 0 bits)
                   0         Qint.5 SP1 / SP2                Record                     4 bytes                         -
                                                                                        16 bits                         device spe‐
                   1         Qint.5 SP1 sensing range        UInt                                                                       0 ... 65535
 16388    4004                                                           yes            (Offset 16 bits)   rw           cific
                                                                                        16 bits                         device spe‐
                   2         Qint.5 SP2 sensing range        UInt                                                                       0 ... 65535
                                                                                        (Offset 0 bits)                 cific
                   0         Qint.5 configuration            Record                     4 bytes                         -
                                                                                        8 bits
                   1         Qint.5 Switchpoint logic        UInt                                                       0               0 = not inverted
                                                                                        (Offset 24 bits)
                                                                                                                                        0 = Deactivated
 16389    4005                                                           yes            8 bits             rw                           1 = Single point mode
                   2         Qint.5 Switchpoint mode         UInt                                                       1
                                                                                        (Offset 16 bits)                                2 = Window mode
                                                                                                                                        3 = Two point mode
                                                                                        16 bits
                   3         Qint.5 Switchpoint hysteresis   UInt                                                       0               0 = Vendor specific default
                                                                                        (Offset 0 bits)
                   0         Qint.6 SP1 / SP2                Record                     4 bytes                         -
                                                                                        16 bits                         device spe‐
                   1         Qint.6 SP1 sensing range        UInt                                                                       0 ... 65535
 16390    4006                                                           yes            (Offset 16 bits)   rw           cific
                                                                                                                        device spe‐
                   2         Qint.6 SP2 sensing range        UInt                                                                       0 ... 65535
                                                                                                                        cific
                   0         Qint.6 configuration            Record                     4 bytes                         -
                                                                                        8 bits
                   1         Qint.6 Switchpoint logic        UInt                                                       0               0 = not inverted
                                                                                        (Offset 24 bits)
                                                                                                                                        0 = Deactivated
 16391    4007                                                           yes            8 bits             rw                           1 = Single point mode
                   2         Qint.6 Switchpoint mode         UInt                                                       1
                                                                                        (Offset 16 bits)                                2 = Window mode
                                                                                                                                        3 = Two point mode
                                                                                        16 bits
                   3         Qint.6 Switchpoint hysteresis   UInt                                                       0               0 = Vendor specific default
                                                                                        (Offset 0 bits)
                   0         Qint.7 SP1 / SP2                Record                     4 bytes                         -
                                                                                        16 bits                         device spe‐
                   1         Qint.7 SP1 sensing range        UInt                                                                       0 ... 65535
 16392    4008                                                           yes            (Offset 16 bits)   rw           cific
                                                                                        16 bits                         device spe‐
                   2         Qint.7 SP2 sensing range        UInt                                                                       0 ... 65535
                                                                                        (Offset 0 bits)                 cific
                   0         Qint.7 configuration            Record                     4 bytes                         -
                                                                                        8 bits
                   1         Qint.7 Switchpoint logic        UInt                                                       0               0 = not inverted
                                                                                        (Offset 24 bits)
                                                                                                                                        0 = Deactivated
 16393    4009                                                           yes            8 bits             rw                           1 = Single point mode
                   2         Qint.7 Switchpoint mode         UInt                                                       1
                                                                                        (Offset 16 bits)                                2 = Window mode
                                                                                                                                        3 = Two point mode
                                                                                        16 bits
                   3         Qint.7 Switchpoint hysteresis   UInt                                                       0               0 = Vendor specific default
                                                                                        (Offset 0 bits)
                   0         Qint.8 SP1 / SP2                Record                     4 bytes                         -
                                                                                        16 bits                         device spe‐
                   1         Qint.8 SP1 sensing range        UInt                                                                       0 ... 65535
 16394    400A                                                           yes            (Offset 16 bits)   rw           cific
                                                                                                                        device spe‐
                   2         Qint.8 SP2 sensing range        UInt                                                                       0 ... 65535
                                                                                                                        cific




8022709.1ML4/2024-03-11 | SICK                                                                              T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   35
Subject to change without notice

8 SERVICE DATA

ISDU
                                                                           Data reposi‐                               Default
Index            Sub-        Name                            Data type                    Length             Access             Value/range
                                                                           tory                                       value
DEC     HEX      Index

                 0           Qint.8 configuration            Record                       4 bytes                     -
                                                                                          8 bits
                 1           Qint.8 Switchpoint logic        UInt                                                     0         0 = not inverted
                                                                                          (Offset 24 bits)
                                                                                                                                0 = Deactivated
16395   400B                                                               yes            8 bits             rw                 1 = Single point mode
                 2           Qint.8 Switchpoint mode         UInt                                                     1
                                                                                          (Offset 16 bits)                      2 = Window mode
                                                                                                                                3 = Two point mode
                                                                                          16 bits
                 3           Qint.8 Switchpoint hysteresis   UInt                                                     0         0 = Vendor specific default
                                                                                          (Offset 0 bits)



NOTE
The index names of the WTT12LC device variant differ from the names shown here. The index numbers and
function descriptions (if implemented, see IODD description of the respective WTT12LC device) nevertheless also
apply to the WTT12LC.

The switching distance of the individual detection channels of the sensor can be set using Qint.x SP1 sensing range or
Qint.x SP2 sensing range (in mm). The value range is restricted by the sensor’s “max. sensing range” (see sensor data
sheet for “max. sensing range”).
Qint.x Switchpoint logic and Qint.x Switchpoint hysteresis are fixed parameters and cannot be changed.
Qint.x Switchpoint mode adjustments:
Deactivated                           =        No function. The binary output state of Qint.x is set to “0”, regardless of the current
                                               detection status.
Single point mode                     =        The output state of Qint.x switches to “1” if the currently measured distance value
                                               between the sensor and object/background is less than or equal to the value set
                                               under Qint.x SP1 sensing range.
Window mode                           =        The output state of Qint.x switches to “1” If the currently measured distance value
                                               between the sensor and object / background is between the set values of Qint.x SP1
                                               sensing range and Qint.x SP2 sensing range.
Two point mode                        =        If the distance measurement value is falling, the output state of Qint.x switches to
                                               “1” if the distance value between the sensor and object/background is less than or
                                               equal to the value set under Qint.x SP2 sensing range.
                                               If the distance measurement value is rising, the output state of Qint.x switches to “0”
                                               if the currently measured distance value between the sensor and object/background
                                               is greater than or equal to the value set under Qint.x SP1 sensing range.

Table 55: Teach-in/detection - Measurement averaging
ISDU
                                                                           Data reposi‐                               Default
Index            Sub-        Name                            Data type                    Length             Access             Value/range
                                                                           tory                                       value
DEC     HEX      Index

                                                                                                                                0=1
                                                                                                                                1=2
                                                                                                                                2=4
                                                                                                                                3=8
                                                                                                                                4 = 16
89      59       -           Measurement averaging           UInt          yes            1 byte             rw       0
                                                                                                                                5 = 32
                                                                                                                                6 = 64
                                                                                                                                7 = 128
                                                                                                                                8 = 256
                                                                                                                                9 = 512


The Measurement averaging function results in a smoothing of the distance measurement value output in the
process data and under Distance to object (index 229). A moving average filter is generated from a certain number
of measured values. The number of measured values used for the Measurement averaging is set under this index.




36       T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                                  8022709.1ML4/2024-03-11 | SICK
                                                                                                                                             Subject to change without notice

SERVICE DATA 8


Table 56: Teach-in/detection - Teach-in offset
 ISDU
                                                              Data reposi‐                             Default
 Index             Sub-      Name                 Data type                  Length       Access                       Value/range
                                                              tory                                     value
 DEC       HEX     Index

 90        5A      -         Teach-in offset      Int         yes            2 bytes      rw           0               -200 … +200



When this function is used, the defined detection point is corrected by the set value when a teach-in command
is triggered (via the teach-in button on the sensor housing or via the system command Single value teach SP1 / SP2
(index 2, value 65)).
This function can be used to increase detection reliability, especially for teach-in ongoing processes, by moving the
detection point with the Teach-in offset “into the object”, for example.

NOTE
Dependency:
Single value teach SP1 / SP2 system command (index 2, value 65/66)


NOTE
The Teach-in offset does not work with direct range adjustment via Qint.x SP1 / SP2 (index
60/62/16384/16386/16388/16390/16390/16392/16394).

Table 57: Teach-in/Detection - Distance to object
 ISDU
                                                              Data reposi‐                             Default
 Index             Sub-      Name                 Data type                  Length       Access                       Value/range
                                                              tory                                     value
 DEC       HEX     Index

                   0         Distance to object   Record                     3 bytes
                                                                             16 bits
                   1         Distance             UInt                                                                 0 … 30000
 229       E5                                                 -              (Offset 8)   ro           -
                                                                             2 bits                                    0 = Distance in range / valid
                   2         Distance qualifier   UInt
                                                                             (Offset 0)                                3 = No distance information / distance invalid


This parameter can be used to output the measured distance to the object or the background (if available and in
sensing range) as a Distance in mm or 1/10 mm (depending on the device – see IODD of the respective device
for details). If no measured value can be detected (e.g. because the sensor is facing empty space) or if the
measured value is outside of the specified sensing range, the sensor delivers output value “30,000”, which is to
be interpreted as an invalid measurement.
Each measured value must be linked with the Distance qualifier. This value specifies whether the current output
measured value is valid or not.

NOTE
Separate access to sub-index 1 or 2 is not possible.


8.8                Installation / Diagnostics
Table 58: Teach-in/detection - Standard command
 ISDU
                                                              Data reposi‐                             Default
 Index             Sub-      Name                 Data type                  Length       Access                       Value/range
                                                              tory                                     value
 DEC       HEX     index

 2         02      -         Standard command     UInt        -              1 byte       wo           -               228 = Reset diagnostic parameter


The Reset diagnostic parameter system command resets all resettable diagnostic parameters in the device to the
initial value or to zero.

NOTE
Dependency:
•        Operating hours since last reset (Index 190, sub-index 2)


8022709.1ML4/2024-03-11 | SICK                                                             T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors              37
Subject to change without notice

8 SERVICE DATA

Table 59: Installation/diagnostics - Device Status
 ISDU
                                                                               Data reposi‐                                   Default
 Index               Sub-        Name                            Data type                    Length                Access                  Value/Range
                                                                               tory                                           value
 DEC        HEX      index

                                                                                                                                            0 = Device is ok
                                                                                                                                            1 = Maintenance required
                                                                                                                                            2 = Outside the specifications
 36         24       -           Device Status                   UInt          -              8 bits                ro        -
                                                                                                                                            3 = Function check-out
                                                                                                                                            4 = Error
                                                                                                                                            5 – 255 = Reserved
 37         25       -           Detailed Device Status          Array         -              device specific       ro        -             device specific


Device Status shows the current device status.
Detailed Device Status contains a rolling list of the most recent events.
Table 60: Installation/Diagnostics - Quality of teach
 ISDU
                                                                               Data reposi‐                                   Default
 Index               Sub-        Name                            Data type                    Length                Access                  Value/range
                                                                               tory                                           value
 DEC        HEX      index

 114        72       -           Quality of teach                UInt          -              1 byte                ro        -             0 to 100%

Table 61: Installation/Diagnostics - Quality of teach
 ISDU
                                                                               Data reposi‐                                   Default
 Index               Sub-        Name                            Data type                    Length                Access                  Value/range
                                                                               tory                                           value
 DEC        HEX      index

                     -           Quality of teach                UInt                         1 byte                                        0 … 100 %
                     0           Quality of teach                RecordT                      [sum of subindices]                           0 … 100 %
                                                                                              8 bits (Offset: see
                     1           Quality of teach Qint.1 SP1     UIntegerT                                                                  0 … 100 %
                                                                                              IODD)
                                                                                              8 bits (Offset: see
                     2           Quality of teach Qint.1 SP2     UIntegerT                                                                  0 … 100 %
                                                                                              IODD)
                                                                                              8 bits (Offset: see
                     3           Quality of teach Qint.2 SP1     UIntegerT                                                                  0 … 100 %
                                                                                              IODD)
                                                                                              8 bits (Offset: see
                     4           Quality of teach Qint.2 SP2     UIntegerT                                                                  0 … 100 %
 114        72                                                                 -              IODD)                 ro        -
                                                                                              8 bits (Offset: see
                     5           Quality of teach Qint.3 SP1     UIntegerT                                                                  0 … 100 %
                                                                                              IODD)
                                                                                              8 bits (Offset: see
                     6           Quality of teach Qint.3 SP2     UIntegerT                                                                  0 … 100 %
                                                                                              IODD)
                                 ...                             ...                                                                        0 … 100 %
                                                                                              8 bits (Offset: see
                     x           Quality of teach Qint.n SP1     UIntegerT                                                                  0 … 100 %
                                                                                              IODD)
                                                                                              8 bits (Offset: see
                     x+1         Quality of teach Qint.n SP2     UIntegerT                                                                  0 … 100 %
                                                                                              IODD)


Quality of teach provides feedback regarding the quality of the last teach-in process performed.
The Quality of teach value is updated after each teach-in process.
For devices with several active setpoints, one Quality of teach value is output per setpoint. The number of sub-indi‐
ces, the data length as well as the offset of the individual sub-indices are device specific and can be taken from
the respective IODD.
Table 62: Definition Quality of teach for WTB, WTS and WTL devices
           Min. sensing range                    ≤        Teach-in sensing range          ≤        Max. sensing range on black 1)       -         Quality of teach = 100%
      Max. sensing range on black 1)             <        Teach-in sensing range          ≤        Max. sensing range on white 2)       -       Quality of teach = 100 to 10%
                                                                                                          Teach-in error                -           Quality of teach = 0%
1)     6% remission factor
2)     90% remission factor

Table 63: Definition Quality of teach for WL, WLA, WLG, WE and WEO devices with teach-in
                     Operating reserve after teach-in ≥ 3.75                                   -                                Quality of teach = 100%
                  3.75 > Operating reserve after teach-in > 1.0                                -                              Quality of teach = 99% ... 1%
                     Operating reserve after teach-in ≤ 1.0                                    -                                 Quality of teach = 0 %




38           T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                                          8022709.1ML4/2024-03-11 | SICK
                                                                                                                                                         Subject to change without notice

SERVICE DATA 8


NOTE
Dependency:
•        Standard command Single value teach (Index 2, value 65)

Table 64: Installation/Diagnostics - Temperature
 ISDU
                                                                       Data reposi‐                                         Default
 Index             Sub-      Name                          Data type                  Length                   Access                       Value/range
                                                                       tory                                                 value
 DEC        HEX    index

                   0         Temperature                   Record                     5 bytes
                                                                                      8 bits (Offset
                   1         Current temperature                                                                                            -127 ... 127 °C
                                                                                      32 bits)
                                                                                      8 bits (Offset
                   2         Max. temperature all time                                                                                      -127 ... 127 °C
                                                                                      24 bits)
 153        99                                                         -              8 bits (Offset           ro           -
                   3         Min. temperature all time                                                                                      -127 ... 127 °C
                                                                                      16 bits)
                             Max. temperature since last
                   4                                                                  8 bits (Offset 8 bits)                                -127 ... 127 °C
                             reset
                             Min. temperature since last
                   5                                                                  8 bits (Offset 0 bits)                                -127 ... 127 °C
                             reset


Read out the operating temperature of the sensor. The values of Max. temperature since last reset and Min. temperature
since last reset are deleted via the Standard command Reset diagnostic parameters (index 2, value 228).

Table 65: Installation/Diagnostics - Temperature zone
 ISDU
                                                                       Data reposi‐                                         Default
 Index             Sub-      Name                          Data type                  Length                   Access                       Value/range
                                                                       tory                                                 value
 DEC        HEX    index

                                                                                                                                            0 = very cold
                                                                                                                                            1 = cold
 154        9A     -         Temperature zone              UInt        yes            1 byte                   ro           -               2 = ideal
                                                                                                                                            3 = warm
                                                                                                                                            4 = above specified limit


The Temperature zone parameter reports the interior device temperature.

Table 66: Installation/Diagnostics - Remaining sender lifetime
 ISDU
                                                                       Data reposi‐                                         Default
 Index             Sub-      Name                          Data type                  Length                   Access                       Value/range
                                                                       tory                                                 value
 DEC        HEX    index

                                                                                                                                            0 ... 5000
 155        9B     0         Remaining sender lifetime     UInt        -              2 bytes                  ro
                                                                                                                                            65535


Shows the expected number of days until the sender unit will reach the end of its life cycle (the performance
specified in the data sheet can no longer be guaranteed).
65535 = calculation not possible (e.g. because history is not available).

Table 67: Installation/Diagnostics - Quality of run
 ISDU
                                                                       Data reposi‐                                         Default
 Index             Sub-      Name                          Data type                  Length                   Access                       Value/range
                                                                       tory                                                 value
 DEC        HEX    index

                                                                                                                                            0 to 255%
                             Quality of run
 175        AF     -                                       UInt        -              1 byte                   ro           -               0...254 %, 255 =not available
                             Function reserve                                                                                               0 to 99% 1)

1)     Only for WE / WEO devices without teach-in

Quality of run provides continuous feedback on the current energy robustness of the object detection.
Whenever a teach-in command is issued, the current light reception level of the receiver is set as the reference
point and the Quality of run value is set to 100 %. The 0% threshold is automatically determined by the sen‐
sor. Should the energy at the receiver increase or decrease (e.g. due to contamination of the sensor’s front screen
or the reflector, or due to these elements being cleaned; excluding object detection), the Quality of run will change
accordingly.


8022709.1ML4/2024-03-11 | SICK                                                                                  T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   39
Subject to change without notice

8 SERVICE DATA

Function reserve (for WE/WEO devices without teach-in) shows the current operating reserve of the WE/WEO device
in absolute terms.
The light reception level that reaches the limit between “object detected” and “object not detected” is defined as
Function reserve = 1. If, for example, the amount of light energy received doubles, the Function reservevalue increases
to 2.

NOTE
Dependency:
•        Standard Command (index 2) all device-specific teach-in commands.

Table 68: Installation/Diagnostics - Quality of run alarm threshold
 ISDU
                                                                               Data reposi‐                      Default
 Index               Sub-        Name                             Data type                   Length    Access             Value/range
                                                                               tory                              value
 DEC        HEX      index

                                 Quality of run alarm threshold                                                  50        0 … 90%
 176        B0       -           Function reserve alarm thresh‐   UInt         yes            1 byte    rw
                                                                                                                 4         0 ... 99% 1)
                                 old

1)     Only for WE/WEO devices without teach-in

An alarm switching threshold can be defined for Quality of run or Function reserve via Quality of run alarm threshold or
Function reserve alarm threshold.
If the value falls below this alarm switching threshold, the Quality of run alarm output (index 226, subindex 1) is
activated. If the Quality of runor Function reserve value rises again, the alarm is deactivated as soon as the selected
alarm switching threshold is exceeded by five percentage points (= hysteresis).
The alarm signal can also be output as a physical signal via pin 2 (Pin 2 configuration (Index 121)).

NOTE
Dependency:
•        Pin 2 configuration (Index 121)
•        Quality of run alarm output (Index 226, Subindex 1)

Table 69: Installation/Diagnostics - Quality of alignment
 ISDU
                                                                               Data reposi‐                      Default
 Index               Sub-        Name                             Data type                   Length    Access             Value/range
                                                                               tory                              value
 DEC        HEX      index

 177        B1       -           Quality of alignment             UInt         yes            1 byte    ro       -         0 to 100%


Quality of alignment displays the energy currently received by the sensor, regardless of the reference signal or the
teach-in command.
Quality of alignment is used to align the sensor with the reflector as accurately as possible (for WL, WLA and WLG
devices) or to align the sender with the receiver (for WE/WEO devices).
On some devices, this information is also displayed on the alignment aid display (blue LEDs on the top of the
sensor).

Table 70: Installation/Diagnostics - Maintenance prediction
 ISDU
                                                                               Data reposi‐                      Default
 Index               Sub-        Name                             Data type                   Length    Access             Value/range
                                                                               tory                              value
 DEC        HEX      index

                                                                                                                           0 ... 5000
 178        B2       0           Maintenance prediction           UInt         -              2 bytes   ro
                                                                                                                           65535


Shows the expected number of days until maintenance is required. The maintenance prediction is calculated using
the long-term trend of the Quality of run value. Suitable maintenance measures depend on the ambient conditions;
typical measures include readjusting the sensor to the object or cleaning the sensor front panel.
65535 = calculation not possible (e.g. because history is not available).



40           T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                         8022709.1ML4/2024-03-11 | SICK
                                                                                                                                        Subject to change without notice

SERVICE DATA 8


Table 71: Installation/Diagnostics - Alarm thresholds for diagnostic parameters
 ISDU
                                                                             Data reposi‐                                      Default
 Index             Sub-       Name                               Data type                  Length                Access                       Value/range
                                                                             tory                                              value
 DEC        HEX    index

                              Alarm thresholds for diagnostic
                   -                                             Record                     9 bytes
                              parameters
                                                                                            8 bits
                   Device-
                              Upper temperature threshold 1)     Sint                       (Offset device spe‐                80              -127 ... 127
                   specific
                                                                                            cific)
                                                                                            8 bits
                   Device-
                              Lower temperature threshold 1)     Sint                       (Offset device spe‐                -30             -127 ... 127
                   specific
                                                                                            cific)
 179        B3                                                               yes            16 bits               rw
                   Device-    Remaining sender lifetime
                                                                 UInt                       (Offset device spe‐                30              0 ... 5000
                   specific   threshold 2)
                                                                                            cific)
                                                                                            16 bits
                   Device-    Maintenance prediction thresh‐
                                                                 UInt                       (Offset device spe‐                30              0 ... 5000
                   specific   old 3)
                                                                                            cific)
                                                                                            32 bits
                   Device-
                              Operating hours threshold 4)       UInt                       (Offset device spe‐                40000           0 ... 1000000
                   specific
                                                                                            cific)

1)     In relation to index 153 dec, subindex 1 [° C]
2)     In relation to index 155 dec [d]
3)     In relation to index 178 dec [d]
4)     In relation to index 190 dec, subindex 2 [h]

The Parameter Alarm threshold for diagnostic parameters offers the option of defining alarm thresholds for certain
diagnostic values provided by the device. If these alarm thresholds are exceeded or not reached, a corresponding
event is generated.
Future expansion to include additional sub-indices is possible.

NOTE
Dependency:
•        Current temperature (Index 153, sub-index 1)
•        Remaining sender lifetime (Index 155)
•        Maintenance prediction (Index 178)
•        Operating hours since last reset (Index 190, sub-index 2)

Table 72: Installation/Diagnostics - Operating hours
 ISDU
                                                                             Data reposi‐                                      Default
 Index             Sub-       Name                               Data type                  Length                Access                       Value/range
                                                                             tory                                              value
 DEC        HEX    index

                   0          Operating hours                    Record                     8 bytes
                                                                                            32 bits
                   1          Total operating hours              UInt                                                                          0 ... 1000000
 190        BE                                                               -              (Offset 32 bits)      ro           -

                                                                                            32 bits
                   2          Operating hours since last reset   UInt                                                                          0 ... 1000000
                                                                                            (Offset 0 bits)


The Total operating hours parameter displays how many total hours (h) the device has already been in operation. This
value cannot be reset.
Parameter Operating hours since last reset displays how many hours (h) the device has been in operation since the
last reset of the diagnostic parameters. The diagnostic parameters are reset using the Reset diagnostic parameter
standard command (index 2, value 228).

NOTE
Dependency:
•        Reset diagnostics parameter system command (index 2, value 228)
•        Operating hours threshold (Index 179)




8022709.1ML4/2024-03-11 | SICK                                                                                     T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   41
Subject to change without notice

8 SERVICE DATA

Table 73: Installation/Diagnostics - System state
ISDU
                                                                  Data
                                                         Data                                                    Default
Index             Sub-      Name                                  reposi‐         Length               Access               Value/range
                                                         type                                                    value
                  index                                           tory
DEC      HEX
                  0         System state                 Record                   1 byte

                                                                                  1 bit                                     0x00 = No object detected
                            Detection output Qint.1
                                                                                  (Offset 0 bit)                            0x01 = oObject detected

                                                                                                                            1 bit                                 0x00 = No object detected
                            Detection output Qint.2
                                                                                                                            (Offset 1 bit)                        0x01 = Object detected

                                                                                  1 bit                                     0x00 = No object detected
                            Detection output Qint.3
                                                                                  (Offset 2 bits)                           0x01 = Object detected
226      E2                                                       -                                    ro        -
                                                                                  1 bit                                     0x00 = No object detected
                            Detection output Qint.4
                                                                                  (Offset 3 bits)                           0x01 = Object detected
                            Quality of run alarm out‐
                            put [alternatively: "Func‐                            1 bit                                     0x00 = Alarm not active
                            tion reserve alarm out‐                               (Offset 6 bits)                           0x01 = Alarm active
                            put"]

                                                                                  1 bit                                     0x00 = External input FALSE
                            Input signal state Pin 2
                                                                                  (Offset 7 bits)                           0x01 = External input TRUE


System state can be used to request certain device statuses related to the current detection signal Qint.1 and the
Quality of run alarm output. The exact implementation may vary between the different device types.
Dependencies and interaction with:
•       Quality of run alarm threshold / Function reserve alarm threshold (Index 176)

8.9                    Smart Tasks
Smart Tasks process the various Smart Sensor signals for detection and measurement, linking them to binary
switching signals from an external sensor if necessary. These signals can be imported via pin 2 (see Pin 2
configuration, ISDU 121). The Smart Task uses this data to generate the requisite process information – tailored
to the task at hand in the plant. This saves time during data evaluation in the control, accelerates machine
processes, and makes high-performance, cost-intensive additional hardware unnecessary.
•       Decentralized signal analysis directly at the sensor
•       Faster signal capture and processing
•       Through Smart Tasks, Smart Sensors deliver the information that the plant process actually requires – no
        separate data preparation necessary in the control

8.9.1                  Smart Task “Basic logic” (A00)
Logical principle of operation:

                                                                                                                     A00


         Qint.1                             Logic 1                   Timer 1                      Inverter 1              QL1




External input                              Logic 2                   Timer 2                      Inverter 2              QL2




Figure 2: Logical principle of operation A00

Table 74: Smart Tasks - SLTI Version
ISDU
                                                                                     Data reposi‐                                            Default
Index                  Sub-        Name                               Data type                        Length               Access                        Value/range
                                                                                     tory                                                    value
DEC       HEX          index

1080      438          -           SLTI Version                       String         -                 8 bytes              ro               -            -


The SLTI version contains the version number for the Smart Task Basic logic.

42             T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                                                    8022709.1ML4/2024-03-11 | SICK
                                                                                                                                                                     Subject to change without notice

SERVICE DATA 8


Table 75: Smart Tasks - Logic
 ISDU
                                                                Data reposi‐                                  Default
 Index             Sub-      Name                   Data type                  Length           Access                         Value/range
                                                                tory                                          value
 DEC       HEX     index

 1083      43B     -         Logic 1                                           1 byte                                          0 = DIRECT
                                                                                                                               1 = AND
                                                    UInt        yes                             rw            0                2 = OR
 1084      43C     -         Logic 2                                           1 byte                                          3 = Window Mode
                                                                                                                               4 = Hysteresis


The settings for Logic 1 and Logic 2 can be used to logically link the sensor-internal detection signal Qint.1 to another
sensor’s switching signal imported via pin 2.
To do this, the Pin 2 configuration (index 121) must be set to External input .
Direct                             For Logic 1:
                                   Qint.1 signal is transferred without changes and without taking the external signal into
                                   account.
                                   For Logic 2:
                                   The external input signal is transferred without changes and without taking the Qint.1 signal
                                   into account.
AND                                Logical AND operation of Qint.1 and External input.
OR                                 Logical OR linking of Qint.1 and External input.
WINDOW MODE                        See the following diagram
HYSTERESIS MODE                    See the following diagram
WINDOW                                                                                   HYSTERESIS
         Qint. 1                                                                                Qint. 1
                               &                                                                                           &                 S

                                               ≥1    Output

                               &                                                                                          ≥1                 R Q           Output
External input                                                                           External input

Figure 3: Window Mode                                                                    Figure 4: Hysteresis Mode

NOTE
If no physical signal is applied to the external input or if another function is selected for Pin 2 configuration (index
121), the status of the external input is interpreted as logical 0.


NOTE
Dependency:
•        Pin 2 configuration (Index 121)

Table 76: Smart Tasks - Timer
 ISDU
                                                                Data reposi‐                                  Default
 Index             Sub-      Name                   Data type                  Length           Access                         Value/range
                                                                tory                                          value
 DEC       HEX     index

 1085      43D     -         Timer 1 mode                                      1 byte                                          0 = Deactivated
                                                                                                                               1 = T-on delay
                                                                               1 byte
                                                                                                                               2 = T-off delay
                                                                                                              0
 1086      43E     -         Timer 2 mode                                                                                      3 = T-on/T-off
                                                                                                                               4 = Impulse (one shot)
                                                                                                                               5 = T-on delay impulse1
                                                    UInt        yes                             rw
 1087      43F     -         Time 1 setup                                      2 bytes
 1088      440     -         Time 2 setup                                      2 bytes
                                                                                                              1                1 … 30,000 ms
 1091      443     -         Time 1.1 setup1                                   2 bytes
 1092      444     -         Time 2.1 setup1                                   2 bytes

1      Optional functions, device-dependent. Implementation always common, index 1086 value 5, index 1091 and 1092.

Various delay modes can be selected via Timer 1 mode / Timer 2 mode .


8022709.1ML4/2024-03-11 | SICK                                                                    T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   43
Subject to change without notice

8 SERVICE DATA

The associated delay times are set via Time 1 setup / Time 2 setup and, depending on the device, also via Time 1.1
setup / Time 2.1 setup . See the table below for details:
                                                                                                       Index 1092/1093...
                                                           not implemented                                                     implemented
 Timer mode                                      Time 1 setup / Time 2 setup                     Time 1 setup / Time 2 setup         Time 1.1 setup / Time 2.1 setup
 1 = T-on delay                                  T-on delay                                      T-on delay                          -
 2 = T-off delay                                 T-off delay                                     T-off delay                         -
 3 = T-on/T-off                                  T-on delay and T-off delay                      T-on delay                          T-off delay
 4 = Impulse (one shot)                          Impulse                                         Impulse                             -
 5 = T-on delay impulse                          -                                               T-on delay                          Impulse

See the following graphic for details on how the different modes work.




Figure 5: Timer 1 / Timer 2

Table 77: Smart Tasks - Inverter
 ISDU
                                                                               Data reposi‐                             Default
 Index               Sub-        Name                            Data type                    Length           Access                Value/range
                                                                               tory                                     value
 DEC        HEX      index

 1089       441      -           Inverter 1                                                   1 byte                                 0 = Not inverted
                                                                 UInt          yes                             rw       0 1)
 1090       442      -           Inverter 2                                                   1 byte                                 1 = Inverted

1)     Default setting for WL, WLA, WLG, WE and WEO devices: 1 = Inverted

Inverter 1/2 inverts the logical status of the timer 1/2 output signal.

NOTE
Inverting the Timer 1/2 output signal does not affect how the delay modes work.
Please note that by inverting the Timer 1/2 output signal, a set switch-on delay can act as a switch-off delay, for
example.


8.9.2                Smart task “Time measurement and debouncing” (A70)
Logical principle of operation:



44           T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                                   8022709.1ML4/2024-03-11 | SICK
                                                                                                                                                  Subject to change without notice

SERVICE DATA 8


                                                                                                                                                       A70

                                                    Comparator value low           −
Qint.1                 Debouncing 1                                                +             Logic 1          Timer 1             Inverter 1             QL1
                                                                    TIMER

                                                                    tmsval                                                                                   AO
                                         Quality D1

                                                                                   −             Logic 2          Timer 2             Inverter 2             QL2
                                                Comparator value high              +



Figure 6: Logical principle of operation A70

Table 78: Smart Task - Time measurement version
 ISDU
                                                                        Data reposi‐                              Default
 Index             Sub-      Name                          Data type                   Length        Access                       Value/range
                                                                        tory                                      value
 DEC        HEX    index

 1016       3F8    -         Time measurement version      String       -              8 bytes       ro           -               -


SLTI Version contains the version number of the Smart Task sub-function Time measurement.

Table 79: Smart Task - Time base
 ISDU
                                                                        Data reposi‐                              Default
 Index             Sub-      Name                          Data type                   Length        Access                       Value/range
                                                                        tory                                      value
 DEC        HEX    index

                                                                                                                                  3= 1 ms
 1017       3F9    -         Time base                     UInt         yes            1 byte        rw           3               4= 10 ms
                                                                                                                                  5= 100 ms


The time value tmsval is a 14-bit value and can therefore assume a value between 0 and 16383 (dec).
Time base is a factor by which the time measurement result is multiplied. This allows longer times to be meas‐
ured. The resolution and measurement accuracy decrease accordingly.

Table 80: Smart Task - Measuring mode
 ISDU
                                                                        Data reposi‐                              Default
 Index             Sub-      Name                          Data type                   Length        Access                       Value/range
                                                                        tory                                      value
 DEC        HEX    index

                                                                                                                                  0 = target
 1018       3FA    -         Measuring mode                UInt         yes            1 byte        rw           0               1 = gap
                                                                                                                                  2 = target, target + gap


Measuring mode determines which time measurement values are measured.
Target                             Time length measurement of the object passing the sensor.
Gap                                Time length measurement of the gap between two objects passing the sensor.
Target,                            The next time value emitted corresponds to the length of the object expressed as time. The
Target + Gap                       next time value emitted then corresponds to the sum of the time-length measurement of
                                   the object and the subsequent gap to the next object.

Table 81: Smart Task - Comparator value
 ISDU
                                                                        Data reposi‐                              Default
 Index             Sub-      Name                          Data type                   Length        Access                       Value/range
                                                                        tory                                      value
 DEC        HEX    index

 1019       3FB    -         Comparator value low                                      2 bytes                    50
                                                           UInt         yes                          rw                           0 to 16383
 1020       3FC    -         Comparator value high                                     2 bytes                    100

1)     Time in ms, 10 ms, 100 ms - depending on the Measuring mode setup, index 1018 (see above)

Comparator value low and Comparator value high are two independent switching thresholds that refer to the measured
time value.



8022709.1ML4/2024-03-11 | SICK                                                                        T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   45
Subject to change without notice

8 SERVICE DATA

If the measured time value exceeds the set switching thresholds, a logical 1 signal is applied to the output for the
comparator in question.
If the measured time value reaches or falls below the selected switching thresholds, a logical 0 signal is applied to
the output for the comparator in question.
These signals are transferred to the Logic 1 and Logic 2 modules.

Table 82: Smart Task - Debounce version
ISDU
                                                                               Data reposi‐                                    Default
Index                Sub-        Name                            Data type                    Length               Access                Value/range
                                                                               tory                                            value
DEC      HEX         index

1032     408         -           Debounce version                String        -              8 bytes              ro          -


Debounce version contains the version number of the Smart Task sub-function Debouncing.

Table 83: Smart Task - Debouncing
ISDU
                                                                               Data reposi‐                                    Default
Index                Sub-        Name                            Data type                    Length               Access                Value/range
                                                                               tory                                            value
DEC      HEX         index

1033     409         -           Debounce time 1                               yes            2 bytes              rw          0         0 … 30,000 ms
                                                                 UInt
1034     40A         -           Quality D1                                    -              2 bytes              ro          -         0 to 100%


Debounce time 1 can be used to suppress (debounce) short, interfering signals at the Smart Task’s input.
The selected debounce time has the same effect as a switch-on or switch-off delay.
The measured time value tmsval is not affected when debouncing is active. Quality D1 indicates the extent to
which active debouncing is used. The higher the value, the more level changes that took place within the selected
Debounce time 1.

Explanations for indices 1080, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090: see "Smart Task “Basic
logic” (A00)", page 42.

8.9.3                Smart task “Counter and debouncing” (A71)
Logical principle of operation:

                                                                                              Counter mode = off
                                                                                                                                                                         A71

                                                                        Comparator value low            −
        Qint.1                    Debouncing 1                                                          +                   Logic 1      Timer 1           Inverter 1         QL1
                                                                                     COUNTER
                                                    Quality D1                          cntval                                                                                AO
                                                    Quality D2                       reset
                                                                                                        −                   Logic 2      Timer 2           Inverter 2         QL2
External input                    Debouncing 2                       Comparator value high              +

                                                                                              Counter mode = off


Figure 7: Logical principle of operation A71

Table 84: Smart Task - Standard command
ISDU
                                                                               Data reposi‐                                    Default
Index                Sub-        Name                            Data type                    Length               Access                Value/range
                                                                               tory                                            value
DEC      HEX         index

                                                                                                                                         192 = Reset counter
2        2           -           Standard command                UInt          -              1 byte               wo          -
                                                                                                                                         193 = Preset counter


Reset counter resets the counter value cntval to 0.
The counter value can also be reset to 0 using a HIGH signal at the Smart Task’s external input. To do this, the Pin
2 configuration (index 121) must be set to External input.
The current counter value cntval is set to the set value (index 1003) via Standard command Preset counter Preset value .



46           T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                                      8022709.1ML4/2024-03-11 | SICK
                                                                                                                                                     Subject to change without notice

SERVICE DATA 8


NOTE
Dependency:
•        Pin 2 configuration (Index 121)
•        Preset value (Index 1003)

Table 85: Smart Task - Counter version
 ISDU
                                                                 Data reposi‐                          Default
 Index             Sub-      Name                    Data type                  Length    Access                       Value/range
                                                                 tory                                  value
 DEC       HEX     index

 1000      3E8     -         Counter version         String      -              8 bytes   ro           -               -


Counter version contains the version number for the Smart Task sub-function Counter.

Table 86: Smart Task - Counter mode
 ISDU
                                                                 Data reposi‐                          Default
 Index             Sub-      Name                    Data type                  Length    Access                       Value/range
                                                                 tory                                  value
 DEC       HEX     index

                                                                                                                       0 = Up
 1001      3E9     -         Counter mode            UInt        yes            1 byte    rw           0               1 = Down
                                                                                                                       2 = OFF


Counter mode defines whether the counter value cntval is increased or decreased by one with each rising edge from
Debouncing 1 Modul . When Counter mode = OFF: Signal pulses are routed past the counter and comparator module -
see see figure 7, page 46; available from Counter version 1.2.0.
The counter value cntval is a 14-bit value and can therefore assume a value between 0 and 16383 (dec). Time
pulses beyond these thresholds are ignored.

Table 87: Smart Task - Preset
 ISDU
                                                                 Data reposi‐                          Default
 Index             Sub-      Name                    Data type                  Length    Access                       Value/range
                                                                 tory                                  value
 DEC       HEX     index

                                                                                                                       0 = Preset internal disabled
 1002      3EA     -         Preset mode                                        1 byte
                                                     UInt        yes                      rw           0               1 = Preset internal enabled
 1003      3EB     -         Preset value                                       2 bytes                                0 to 16383


If the Preset mode is activated, the counter value cntval is set to Preset value (index 1003) if either the current counter
value cntval exceeds the Comparator value high (index 1005) or if the Standard command Preset counter (index 2, value
193) is set.
The Preset mode is activated when, for example, the counter value cntval is automatically reset to a predefined value
Preset value (index 1003) (typically “1”) when a certain counter value is reached. This allows the Smart Task to be
used as a ring buffer.

NOTE
Dependency:
•        Preset value (Index 1003)
•        Comparator value high (Index 1005)
•        Standard command Preset counter (Index 2, value 193)

Table 88: Smart Task - Comparator value / Counter value
 ISDU
                                                                 Data reposi‐                          Default
 Index             Sub-      Name                    Data type                  Length    Access                       Value/range
                                                                 tory                                  value
 DEC       HEX     index

 1004      3EC     -         Comparator value low                               2 bytes                10
                                                                                          rw
 1005      3ED     -         Comparator value high   UInt        yes            2 bytes                10              0 to 16383
 1006      3EE     -         Counter value                                      2 bytes   ro           -


The Comparator value low and the Comparator value high are two independent switching thresholds that refer to the
Counter value .

8022709.1ML4/2024-03-11 | SICK                                                             T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   47
Subject to change without notice

8 SERVICE DATA

If the Counter value exceeds the set switching thresholds, a logical 1 signal is applied to the output for the
comparator in question.
If the Counter value reaches or falls below the set switching thresholds, a logical 1 signal is applied to the output for
the comparator in question.
These signals are transferred to Logic 1 and to the Logic 2 module.
The Counter value shows the current meter reading.

NOTE
Dependency:
•        Preset mode (Index 1002)
•        Preset value (Index 1003)

Table 89: Smart Task - Debounce version
ISDU
                                                                              Data reposi‐                          Default
Index                Sub-       Name                            Data type                    Length        Access             Value/range
                                                                              tory                                  value
DEC        HEX       index

1032       408       -          Debounce version                String        -              8 bytes       ro       -


The Debounce version contains the version number for the Smart Task sub-function Debouncing.

Table 90: Smart Task - Debouncing
ISDU
                                                                              Data reposi‐                          Default
Index                Sub-       Name                            Data type                    Length        Access             Value/range
                                                                              tory                                  value
DEC        HEX       index

1033       409                  Debounce time 1                               yes                          rw       0         0 … 30,000 ms
1034       40A                  Quality D1                                    -                            ro       -         0 to 100%
                     -                                          UInt                         2 bytes
1035       40B                  Debounce time 2                               yes                          rw       0         0 … 30,000 ms
1036       40C                  Quality D2                                    -                            ro       -         0 to 100%


The Debounce time 1/2 can be used to suppress (debounce) short, interfering signals at the Qint.1 input or External
input of the Smart Task.
The set debounce time acts like a switch-on and switch-off delay.
Quality D1/D2 indicates how much debouncing is required. The higher the value, the more level changes that took
place within the selected Debounce time 1/2 .

Notes on ISDUs 1080, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092: see "Smart Task “Basic
logic” (A00)", page 42

8.9.4                Smart Task “Speed and length measurement” (A72)
Logical principle of operation:

                                                                                                                                            A72
                                       Object length
                 Input selector        measurement
Qint.1                                 Object length                      Measurement
                 (optional)
Qint.n                                 measurement                        threshold 1          −                    Time setup impulse
                                       incremental                                             +                    width
                                       Object speed                                                    Switching
                                                                                                                            ---               QL1
                                       measurement                        Measurement                  mode
                                                                                               −                    Time setup impulse
                                                                          threshold 2
                 Inverter Ext.in                                                               +                    shift                     Qint.1
                                             Ingval / spdval
Ext.in
                                                                                                                                              AO



Figure 8: Logical principle of operation A72




48          T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                           8022709.1ML4/2024-03-11 | SICK
                                                                                                                                         Subject to change without notice

SERVICE DATA 8


The Smart Task “Speed and length measurement” (A72) can measure the length and speed of objects that pass
the sensor on a conveyor belt, for example, and also determine the direction of movement. The Smart Task has
three measurement modes for this purpose:
1      Measurement of the object length (Length)
2      Incremental measurement of the object length (Length incremental)
3      Measurement of the object speed (Speed)
The Smart Task A72 “Speed and length measurement” requires an additional external signal in each of the three
measurement modes. This is supplied to the Smart Sensor via its Pin 2 / white wire.
In measuring mode Length and Speed, an additional binary switching sensor is required that detects the same
measurement object shortly before or shortly after the A72 Smart Sensor, see see figure 9, page 50. To ensure
the measurement accuracy specified in the sensor data sheet, it is recommended that the additional sensor has
the same optical and detection properties as the A72 Smart Sensor used. In addition, the light beams of both
sensors must be aligned exactly parallel.
For a correct length or speed measurement, it is crucial that the conveying speed of the measured object is
constant. If, for example, the movement is accelerated, the sensor determines the average speed between the two
measuring points and the measured object length is then too short.
To achieve a correct length measurement, even with accelerated or delayed movements, the measurement mode
Length incremental must be used.

NOTE
The distance between the Smart Sensor and the additional sensor must be smaller than the smallest object to be
measured. This means that the smallest object to be measured must be detected by both sensors simultaneously
for a short moment.


NOTE
For easy connection of the additional sensor to the Smart Sensor, the Y-connector SYL-1204-G0M11-X1
(6055011, www.sick.com/6055011) or SYL-8204-G0M11-X2 (6055012, www.sick.com/6055012) can be used.

In measuring mode Length incremental, the A72 Smart Sensor requires the HTL signal from a connected incremental
encoder (e.g. SICK DBS36, www.sick.com/dbs36), see see figure 10, page 50.
This measurement mode is particularly recommended if the object movement can be accelerated or decelerated
during the measurement or if the object can come to a standstill during the measurement.
In order to ensure correct length measurement, the encoder must always rotate only in one direction during
measurement. Detection of the movement direction of the object is not possible in this measurement mode.

NOTE
The A72 Smart Sensor can process a maximum of 1,000 encoder pulses per second.


NOTE
The Smart Sensor and the additional sensor or the additional encoder must be connected to the same electrical
potential with their supply voltage.

The measured speed or length value and the direction of movement are provided via the process data, see see
"Process data", page 11. Depending on the set measuring mode, either a length or a speed signal is output. The
direction of movement is indicated by the sign of the measured value (only in measuring mode Speed and Length,
not with Length incremental):
•      • Positive sign: object travels into the measuring distance via the Smart Sensor
•      • Negative sign: object travels into the measuring distance via the additional sensor




8022709.1ML4/2024-03-11 | SICK                                           T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   49
Subject to change without notice

8 SERVICE DATA




Figure 9: Wiring example for measuring mode Length and Speed




Figure 10: Wiring example for measuring mode Length incremental

Table 91: Smart Task – Standard command
ISDU
                                                                             Data reposi‐                     Default
Index              Sub-        Name                            Data type                    Length   Access             Value/range
                                                                             tory                             value
DEC       HEX      index

                                                                                                                        201 = Start and stop reference run
2         02       -           Standard command                UInt          -              1 byte   ro       -         202 = Zero setting for incremental length meas‐
                                                                                                                        urement value


As an alternative to directly entering the distance between the two measuring points (via index 1098 Distance
between measuring points), this distance value can also be determined automatically: The command Start and stop
reference run starts a recording function with which the parameter Distance between measuring points (index 1098) is
automatically set by moving an object at a defined and constant speed through the detection area of the Smart
Sensor and the additional sensor. Process:
•       Input of the constant object speed during the reference run via Object speed for reference run (index 1105).
•       Start the reference run via the command Start and stop reference run (index 2, value 201). Smart Task operating
        state (Index 1109) goes from Operate to Reference run.


50         T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                        8022709.1ML4/2024-03-11 | SICK
                                                                                                                                     Subject to change without notice

SERVICE DATA 8


•        Within the next 20 seconds, an object must be moved through the detection area of the Smart Sensor and
         the additional sensor at exactly the previously entered and constant speed.
•        The parameter Distance between measuring points (index 1098) is overwritten with the new value as soon as the
         object has entered the detection area of the second sensor. The status goes back to Operate (Index 1109).
•        If no object moves through the detection areas of the sensors within 20 seconds of the reference run
         being activated, the reference run is aborted. The sensor returns to the status Operate (index 1109), the
         previous value of Distance between measuring points (index 1098) remains unchanged. The same happens if the
         command Start and stop reference run (index 2, value 201) is sent again within the 20 seconds.
The command Start and stop reference run is only executed by the sensor if the Measurement Mode (index 1097) is set
to Speed or Length .

NOTE
Dependency:
• Measurement mode (Index 1097)
• Distance between measuring points (Index 1098)
• Object speed for reference run (Index 1105)
• Smart Task operating state (Index 1109)

The command Zero setting for incremental length measurement value resets the current measured value of the Smart
Task, output via the process data or via the parameter Length measurement value (index 1106), to zero. This is
necessary, for example, if a measurement is only to start after the measurement object has already entered the
detection area of the A72 Smart Sensor.
The command Zero setting for incremental length measurement value is only executed by the sensor if the Measurement
Mode (index 1097) is set to Length incremental .

Table 92: Smart Task – Speed and Length Measurement version
 ISDU
                                                                     Data reposi‐                          Default
 Index             Sub-      Name                        Data type                  Length    Access                       Value/range
                                                                     tory                                  value
 DEC       HEX     index

                             Speed and Length Measure‐
 1096      448     -                                     String      -              8 bytes   ro           -               -
                             ment version


Speed and Length Measurement version specifies the version of the Smart Task “Speed and length measurement”.

Table 93: Smart Task - Input selector
 ISDU
                                                                     Data reposi‐                          Default
 Index             Sub-      Name                        Data type                  Length    Access                       Value/range
                                                                     tory                                  value
 DEC       HEX     index

                                                                                                                           0 = Qint.1
                                                                                                                           1 = Qint.2
                                                                                                                           2 = Qint.3
 1081      439     -         Input selector              Index       yes            1 byte    rw           0               3 = Qint.4
                                                                                                                           4 = Qint.5
                                                                                                                           5 = Qint.6
                                                                                                                           6 = ...


The Input selector defines which Qint.x detection signal is used for speed and length measurement.

NOTE
This function is only available if the Smart Sensor has more than one Qint.x. The actual scope of the value range is
device specific. For details, see the respective device IODD.

Table 94: Smart Task - Inverter external input
 ISDU
                                                                     Data reposi‐                          Default
 Index             Sub-      Name                        Data type                  Length    Access                       Value/range
                                                                     tory                                  value
 DEC       HEX     index

                                                                                                                           0 = Not inverted
 1093      445     -         Inverter Ext.input          UInt        yes            1 byte    rw           0
                                                                                                                           1 = Inverted




8022709.1ML4/2024-03-11 | SICK                                                                 T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   51
Subject to change without notice

8 SERVICE DATA

The Smart Task A72 speed and length measurement always expects a HIGH signal at the external input (pin 2 or
white wire) when the additional sensor detects an object. If the connected additional sensor supplies a LOW signal
when an object is detected (typical for retro-reflective or through-beam photoelectric sensors), the Inverter Ext.input
must be set to 1 = inverted . If the inverter is set incorrectly, the measurement will not work.

NOTE
This function is only relevant in the measurement modes Speed and Length of the parameter Measurement mode
(index 1097).

Table 95: Smart Task - Measurement mode
ISDU
                                                                             Data reposi‐                      Default
Index              Sub-        Name                            Data type                    Length    Access             Value/range
                                                                             tory                              value
DEC       HEX      index

                                                                                                                         0 = Length [mm]
1097      449      -           Measurement mode                UInt          yes            1 byte    rw       0         1 = Length incremental [mm]
                                                                                                                         2 = Speed [mm/s]


Measurement mode defines which primary measuring task is performed by the Smart Task:
Length                              The length of objects passing by the Smart Sensor and additional sensor is measured. The
                                    measurement result is output in the process data as a millimeter value. The sign of the
                                    measured value indicates the direction of movement of the object:
                                    • Positive sign: object travels into the measuring distance via the Smart Sensor
                                    • Negative sign: object travels into the measuring distance via the additional sensor
                                    The measurement only provides correct values if the parameter Distance between measuring
                                    points (index 1098) is set correctly.
Length incremental                  The length of objects passing by the Smart Sensor is measured. The measurement result is
                                    output in the process data as a millimeter value. The sign of the measured value is always
                                    positive. It is not possible to make a statement about the direction of movement of the
                                    object in this mode. The measurement only provides correct values if the parameter Pulses
                                    per 100 millimeter (index 1099) is set correctly.
Speed                               The speed of objects passing the Smart Sensor and additional sensor is measured. The
                                    measurement result is output in the process data in millimeters per second. The sign of the
                                    measured value indicates the direction of movement of the object:
                                    • Positive sign: object travels into the measuring distance via the Smart Sensor
                                    • Negative sign: object travels into the measuring distance via the additional sensor
                                    The measurement only provides correct values if the parameter Distance between measuring
                                    points (index 1098) is set correctly.
The lengths and speeds measured by the sensor are also output via the parameters Length measurement value (index
1106) and Speed measurement value (index 1107).

NOTE
Dependency:
•       Distance between measuring points (Index 1098)
•       Pulses per 100 millimeter (Index 1099)

Table 96: Smart Task – Distance between measuring points
ISDU
                                                                             Data reposi‐                      Default
Index              Sub-        Name                            Data type                    Length    Access             Value/range
                                                                             tory                              value
DEC       HEX      index

                               Distance between measuring
1098      44A      -                                           UInt          yes            2 bytes   rw       1000      1 … 65,535 [x 100 µm]
                               points [in 100 µm]




52         T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                         8022709.1ML4/2024-03-11 | SICK
                                                                                                                                      Subject to change without notice

SERVICE DATA 8


To ensure that the length or speed measurement (Measurement mode Length or Speed, index 1097) is carried out
correctly, the parameter Distance between measuring points must be set as precisely as possible. This is the physical
distance between the detection point of the A72 Smart Sensor and the detection point of the additional sensor.
The distance is specified in 100 µm (corresponds to 1/10 mm) to increase the measurement accuracy of the
Smart Task.
Example: For a measured distance between the detection points of 150.0 mm, the value “1500” must be entered.

NOTE
Dependency:
•        Measurement mode (Index 1097)

Table 97: Smart Task – Pulses per 100 millimeter
 ISDU
                                                                     Data reposi‐                          Default
 Index             Sub-      Name                        Data type                  Length    Access                       Value/range
                                                                     tory                                  value
 DEC       HEX     index

 1099      44B     -         Pulses per 100 millimeter   UInt        yes            2 bytes   rw           100             1 … 1000


To ensure that the incremental length measurement (Measurement mode Length incremental, index 1097) is carried
out correctly, the parameter Pulses per 100 millimeter must be set as precisely as possible. This is the number of
HTL signal pulses that the incremental encoder sends to the Smart Sensor while the conveyor belt on which the
measurement object is conveyed and to which the encoder is coupled travels 100 mm. The value depends on the
number of pulses per revolution of the encoder, the diameter of the measuring wheel or the conveyor roller and, if
applicable, the thickness of the conveyor belt.
The parameter is only included in the Smart Task calculations in Measurement mode Length incremental (index 1097).

NOTE
Dependency:
•        Measurement mode (Index 1097)

Table 98: Smart Task - Measurement threshold
 ISDU
                                                                     Data reposi‐                          Default
 Index             Sub-      Name                        Data type                  Length    Access                       Value/range
                                                                     tory                                  value
 DEC       HEX     index

 1100      44C     -         Measurement threshold 1     Int         yes            2 bytes   rw           100             - 8191 … +8191
 1101      44D     -         Measurement threshold 2     Int         yes            2 bytes   rw           50              - 8191 … +8191
                                                                                                                           0 = Within time window
 1102      44E     -         Switching mode              UInt        yes            1 bytes   rw           0
                                                                                                                           1 = Out of time window
 1103      44F     -         Time setup impulse width    UInt        yes            2 bytes   rw           500             1 ... 30,000 ms
 1104      450     -         Time setup impulse shift    UInt        yes            2 bytes   rw           0               0 ... 30,000 ms


The Measurement threshold 1 and Measurement threshold 2 are switching thresholds that are based on the measured
length and the measured speed. The two switching thresholds form a switching window, with the larger value
forming the upper switching threshold and the smaller value the lower switching threshold. Depending on the
setting of Switching mode , a logical HIGH signal is generated:
•        Within time window:
         HIGH signal when the lower switching threshold < measured value ≤ upper switching threshold
•        Out of time window:
         HIGH signal when measured value ≤ lower switching threshold; or when the measured value > upper
         switching threshold
The HIGH signal is output as switching pulse QL1. The width of the switching pulse can be adjusted via Time setup
impulse width. Output of the switching pulse can be delayed via Time setup impulse shift.




8022709.1ML4/2024-03-11 | SICK                                                                 T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   53
Subject to change without notice

8 SERVICE DATA


NOTE
The selected pulse width (Time setup impulse width) must always be smaller than the distance in time to the next
measurement object.


NOTE
Dependency:
•       Impulse buffer state (Index 1123)

Table 99: Smart Task- Object speed for reference run
ISDU
                                                                             Data reposi‐                      Default
Index              Sub-        Name                             Data type                   Length    Access             Value/range
                                                                             tory                              value
DEC       HEX      index

1105      451      -           Object speed for reference run   UInt         yes            2 bytes   rw       100       10 … 500 mm/s


As an alternative to directly entering the distance between the two measuring points (via index 1098 Distance
between measuring points), this distance value can also be determined automatically: The command Start and stop
reference run starts a recording function with which the parameter Distance between measuring points (index 1098) is
automatically set by moving an object at a defined and constant speed through the detection area of the Smart
Sensor and the additional sensor. Process:
•       Input of the constant object speed during the reference run via Object speed for reference run (index 1105).
•       Start the reference run via the command Start and stop reference run (index 2, value 201). Smart Task operating
        state (Index 1109) goes from Operate to Reference run.
•       Within the next 20 seconds, an object must be moved through the detection area of the Smart Sensor and
        the additional sensor at exactly the previously entered and constant speed.
•       The parameter Distance between measuring points (index 1098) is overwritten with the new value as soon as the
        object has entered the detection area of the second sensor. The status goes back to Operate (Index 1109).
•       If no object moves through the detection areas of the sensors within 20 seconds of the reference run
        being activated, the reference run is aborted. The sensor returns to the status Operate (index 1109), the
        previous value of Distance between measuring points (index 1098) remains unchanged. The same happens if the
        command Start and stop reference run (index 2, value 201) is sent again within the 20 seconds.
The command Start and stop reference run is only executed by the sensor if the Measurement Mode (index 1097) is set
to Speed or Length .

NOTE
Dependency:
• Measurement mode (Index 1097)
• Distance between measuring points (Index 1098)
• Object speed for reference run (Index 1105)
• Smart Task operating state (Index 1109)

The command Zero setting for incremental length measurement value resets the current measured value of the Smart
Task, output via the process data or via the parameter Length measurement value (index 1106), to zero. This is
necessary, for example, if a measurement is only to start after the measurement object has already entered the
detection area of the A72 Smart Sensor.
The command Zero setting for incremental length measurement value is only executed by the sensor if the Measurement
Mode (index 1097) is set to Length incremental .

NOTE
Dependency:
•       Standard command Start and stop reference run (Index 2, value 201)




54         T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                       8022709.1ML4/2024-03-11 | SICK
                                                                                                                                    Subject to change without notice

SERVICE DATA 8


Table 100: Smart Task - Length measurement value
 ISDU
                                                                      Data reposi‐                          Default
 Index             Sub-      Name                         Data type                  Length    Access                       Value/range
                                                                      tory                                  value
 DEC       HEX     index

 1106      452     -         Length measurement value     Int         -              2 bytes   ro           -               - 8,191 … + 8,191 mm


Provision of the last measured length value.

Table 101: Smart Task - Speed measurement value
 ISDU
                                                                      Data reposi‐
 Index             Sub-      Name                         Data type                  Length    Access       Default         Value/range
                                                                      tory
 DEC       HEX     index

 1107      453     -         Speed measurement value      Int         -              2 bytes   ro           -               - 8,191 … + 8,191 mm/s


Provision of the last measured speed value.

Table 102: Smart Task - Smart Task operating state
 ISDU
                                                                      Data reposi‐                          Default
 Index             Sub-      Name                         Data type                  Length    Access                       Value/range
                                                                      tory                                  value
 DEC       HEX     index

                                                                                                                            0 = Operate
 1109      455     -         Smart Task operating state   UInt        -              1 byte    ro           -
                                                                                                                            1 = Reference run


As an alternative to directly entering the distance between the two measuring points (via index 1098 Distance
between measuring points), this distance value can also be determined automatically: The command Start and stop
reference run starts a recording function with which the parameter Distance between measuring points (index 1098) is
automatically set by moving an object at a defined and constant speed through the detection area of the Smart
Sensor and the additional sensor. Process:
•        Input of the constant object speed during the reference run via Object speed for reference run (index 1105).
•        Start the reference run via the command Start and stop reference run (index 2, value 201). Smart Task operating
         state (Index 1109) goes from Operate to Reference run.
•        Within the next 20 seconds, an object must be moved through the detection area of the Smart Sensor and
         the additional sensor at exactly the previously entered and constant speed.
•        The parameter Distance between measuring points (index 1098) is overwritten with the new value as soon as the
         object has entered the detection area of the second sensor. The status goes back to Operate (Index 1109).
•        If no object moves through the detection areas of the sensors within 20 seconds of the reference run
         being activated, the reference run is aborted. The sensor returns to the status Operate (index 1109), the
         previous value of Distance between measuring points (index 1098) remains unchanged. The same happens if the
         command Start and stop reference run (index 2, value 201) is sent again within the 20 seconds.
The command Start and stop reference run is only executed by the sensor if the Measurement Mode (index 1097) is set
to Speed or Length .

NOTE
Dependency:
• Measurement mode (Index 1097)
• Distance between measuring points (Index 1098)
• Object speed for reference run (Index 1105)
• Smart Task operating state (Index 1109)

The command Zero setting for incremental length measurement value resets the current measured value of the Smart
Task, output via the process data or via the parameter Length measurement value (index 1106), to zero. This is
necessary, for example, if a measurement is only to start after the measurement object has already entered the
detection area of the A72 Smart Sensor.
The command Zero setting for incremental length measurement value is only executed by the sensor if the Measurement
Mode (index 1097) is set to Length incremental .




8022709.1ML4/2024-03-11 | SICK                                                                  T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   55
Subject to change without notice

8 SERVICE DATA


NOTE
Dependency:
•       Standard command Start and stop reference run (Index 2, value 201)

Table 103: Smart Task - Impulse buffer state
ISDU
                                                                             Data reposi‐                            Default
Index              Sub-        Name                            Data type                    Length          Access             Value/range
                                                                             tory                                    value
DEC       HEX      index

                                                                                                                               0 = Green: Buffer OK
1123      463      -           Impulse buffer state            UInt          -              1 byte          ro       -         1 = Yellow: Buffer almost full
                                                                                                                               2 = Red: Buffer overflow


If a pulse delay is set via Time setup impulse shift (index 1104), further switching pulses may be generated while the
delay time of a previous switching pulse is still running. In such a case, up to 16 switching pulses are temporarily
stored and successively output via QL1 .
The Impulse buffer state indicates how full the buffer tank is:
Green:                                         Buffer OK:                                            0 ... 12 QL1 pulses in the buffer
Yellow:                                        Buffer almost full:                                   13 ... 16 QL1 pulses in the buffer
Red:                                           Buffer overflow:                                      Buffer is full. New QL1 pulses will be discarded.

NOTE
Dependency:
•       Time setup impulse shift (Index 1104)


8.9.5              Smart Tasks “Object and gap monitor” (A73)
Logical principle of operation:

                                                                                                                                                A73
                                                           Measurement
                                                           threshold 1 - object         −                            Time setup impulse
                                                                                        +                            width object
             Time Measurement Object                                                                 Switching
                                                                                                                               ---                    QL Object
             (rising to falling edge)                                                                mode object
                                                           Measurement                                               Time setup impulse
                                                           threshold 2 - object         −                            shift object
                                                                                        +
Qint.1                                   tmsval                                                                                                       AO
                                                           Measurement
                                                           threshold 1 - gap            −                            Time setup impulse
             Time Measurement Gap                                                       +                            width gap
             (falling to rising edge)                                                                Switching
                                                                                                                               ---                    QL Gap
                                                                                                     mode gap
                                                           Measurement                                               Time setup impulse
                                                           threshold 2 - gap            −                            shift gap
                                                                                        +                                                             Qint.1


Figure 11: Logical principle of operation A73

The Smart Task “Object and gap monitor” measures the length of the objects that pass the sensor followed by
the gap to the next detection object. In this case, the time between the rising signal edge and the falling signal
edge of the Qint.1 detection signal corresponds to the object length and the time between the falling signal edge
and the rising signal edge of the Qint.1 detection signal corresponds to the length of the gap. The measured time
value for objects and gaps is always output in the sensor’s process data element. The measurement is recorded in
milliseconds (see "Process data", page 11).

NOTE
The measured length value depends on the object’s speed of transportation. If the speed of transportation
increases, the measured time value decreases and vice versa.



56         T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                                8022709.1ML4/2024-03-11 | SICK
                                                                                                                                             Subject to change without notice

SERVICE DATA 8


Table 104: Smart Task - Object + Gap Monitor version
 ISDU
                                                                           Data reposi‐                          Default
 Index             Sub-      Name                              Data type                  Length    Access                       Value/range
                                                                           tory                                  value
 DEC       HEX     index

 1112      458     -         Object + Gap Monitor version      String      -              8 bytes   ro           -               -


Object + Gap Monitor version specifies the version present in the Smart Task sub-function “Object and gap monitor”.

Table 105: Smart Task - Measurement threshold - object
 ISDU
                                                                           Data reposi‐                          Default
 Index             Sub-      Name                              Data type                  Length    Access                       Value/range
                                                                           tory                                  value
 DEC       HEX     index

                             Measurement threshold 1 -
 1113      459     -                                           UInt        yes            2 bytes   rw           200             1 ... 8,190 ms
                             object
                             Measurement threshold 2 -
 1114      45A     -                                           UInt        yes            2 bytes   rw           150             1 ... 8,189 ms
                             object
                                                                                                                                 0 = Object within time window
 1115      45B     -         Switching mode object             UInt        yes            1 byte    rw           0
                                                                                                                                 1 = Object out of time window
 1116      45C     -         Time setup impulse width object   UInt        yes            2 bytes   rw           50              1 ... 30,000 ms
 1117      45D     -         Time setup impulse shift object   UInt        yes            2 bytes   rw           0               0 ... 30,000 ms


Measurement threshold 1 – object and Measurement threshold 2 – object are thresholds that are placed on the measured
time between the rising signal edge and falling signal edge of the detection signal Qint.1(= Object detection).
Together, the two thresholds form a time window, whereby the larger value is the upper threshold and the smaller
value is the lower threshold. A HIGH signal is generated depending on the settings for Switching mode object:
•        Object within time window:
         HIGH signal, when the lower switching threshold < Object time value ≤ Upper switching threshold
•        Object out of time window:
         HIGH signal when the object time value ≤ lower switching threshold or when the object time value > upper
         switching threshold
The HIGH signal can be emitted as a switching pulse: QL Object. The width of the switching pulse can be adjusted
under Time setup impulse width object. Time setup impulse shift object can be used to delay the output of the switching
pulse.

NOTE
The selected pulse width (Time setup impulse width object) must always be smaller than the smallest time distance to
the next object.

Table 106: Smart Task - Measurement threshold - gap
 ISDU
                                                                           Data reposi‐                          Default
 Index             Sub-      Name                              Data type                  Length    Access                       Value/range
                                                                           tory                                  value
 DEC       HEX     index

 1118      45E     -         Measurement threshold 1 - gap     UInt        yes            2 bytes   rw           200             1 ... 8,190 ms
 1119      45F     -         Measurement threshold 2 - gap     UInt        yes            2 bytes   rw           150             1 ... 8,189 ms
                                                                                                                                 0 = Gap within time window
 1120      460     -         Switching mode gap                UInt        yes            1 byte    rw           0
                                                                                                                                 1 = Gap out of time window
 1121      461     -         Time setup impulse width gap      UInt        yes            2 bytes   rw           50              1 ... 30,000 ms
 1122      462     -         Time setup impulse shift gap      UInt        yes            2 bytes   rw           0               0 ... 30,000 ms


Measurement threshold 1 – gap and Measurement threshold 2 – gap are thresholds that are placed on the measured time
between the falling signal edge and rising signal edge of the detection signal Qint.1(= Gap detection). Together, the
two thresholds form a time window, whereby the larger value is the upper threshold and the smaller value is the
lower threshold. A HIGH signal is generated depending on the settings for Switching mode gap:
•        Gap within time window:
         HIGH signal, when the lower switching threshold < Gap time value ≤ Upper switching threshold
•        Gap out of time window:
         HIGH signal when the gap time value ≤ lower switching threshold or when the gap time value > upper
         switching threshold


8022709.1ML4/2024-03-11 | SICK                                                                       T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   57
Subject to change without notice

8 SERVICE DATA

The HIGH signal can be emitted as a switching pulse: QL Gap. The width of the switching pulse can be adjusted
under Time setup impulse width gap. Time setup impulse shift gap can be used to delay the output of the switching pulse.

NOTE
The selected pulse width (Time setup impulse width gap) must always be smaller than the smallest time interval to the
next gap.

Table 107: Smart Task - Impulse buffer state
 ISDU
                                                                                  Data reposi‐                              Default
 Index                  Sub-        Name                            Data type                    Length            Access             Value/range
                                                                                  tory                                      value
 DEC        HEX         index

                                                                                                                                      0 = Green: Buffer OK
 1123       463         -           Impulse buffer state            UInt          -              1 byte            ro       -         1 = Yellow: Buffer almost full
                                                                                                                                      2 = Red: Buffer overflow


When a pulse delay is selected using Time setup impulse shift object (index 1117) and/or Time setup impulse shift gap
(index 1122), further switching pulses may be generated while the delay time of a previous switching pulse is still
running. In this case, up to 16 switching pulses are temporarily stored and successively output via QL Object and QL
Gap .
Impulse buffer state indicates how full the buffer is:
Green:                                   Buffer OK:                               0 to 12 QL Object- / QL Gap pulses in the buffer
Yellow:                                  Buffer almost full:                      13 to 16 QL Object- / QL Gap pulses in the buffer
Red:                                     Buffer overflow:                         Buffer is full. New QL Object- / QL Gap pulses will be discarded

8.10                    System-specific ISDUs
Table 108: System-specific ISDUs - Profile characteristic
 ISDU
                                                                                  Data reposi‐                              Default
 Index                  Sub-        Name                            Data type                    Length            Access             Value/range
                                                                                  tory                                      value
 DEC        HEX         index

 13         D           -           Profile characteristic          Array         -              device specific   ro       -         -


Profile characteristic indicates which standardized profiles and functionalities the sensor supports.
The values are emitted in five 16-bit blocks.
At most, the following profiles / functionalities are supported:
1                   PID (Profile Identifier) "Smart Sensor Profile".
32768               Device Identification
                    The sensor supports enhanced identification options, see Identification section.
32769               Binary Data Channel
                    The sensor generates a switching signal from measured analog values and makes this available in a
                    specified manner (see indices 60/61 and 62/63).
32770               Process Data Variables
                    The sensor provides the measured analog value as process data.
32771               Diagnostics
                    The sensor provides standardized diagnostic information.
32772               The sensor supports teach-in methods to teach-in the sensor via the IO-Link interface.

Table 109: System-specific ISDUs - PD-Descriptor
 ISDU
                                                                                  Data reposi‐                              Default
 Index                  Sub-        Name                            Data type                    Length            Access             Value/range 1)
                                                                                  tory                                      value
 DEC        HEX         index

 14         0E          -           PDInput Descriptor              Array         -              device specific   ro       -         Octet String [2]
 15         0F          -           PDOutput Descriptor             Array         -              device specific   ro       -         Octet String [1]

1)     Description of the process data

The PDInput Descriptor (index 14) and the PDOutput Descriptor (index 15) provide information on the data structure of
the process data (input and output). The coding is described in the specification of Smart-Sensor-Profils .


58              T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                                  8022709.1ML4/2024-03-11 | SICK
                                                                                                                                                    Subject to change without notice

SERVICE DATA 8


Each part of the process data is described with 3 bytes.
Byte 1          Data type:
                0: OctetStringT
                1: Set of BoolT
                2: UIntegerT
                3: IntegerT
                4: Float32T.
Byte 2          Length of the data in bits.
Byte 3          Bit offset of the corresponding process data variables in the process data.

Table 110: System-specific ISDUs - SICK Profile Version
 ISDU
                                                                Data reposi‐                                  Default
 Index             Sub-      Name                   Data type                  Length            Access                       Value/range
                                                                tory                                          value
 DEC      HEX      index

 205      0E       -         SICK Profile Version   String      -              4 bytes           ro           -               -


SICK sensors do not just fulfill the requirements of the IO-Link specification and the IO-Link Smart Sensor profile
specification, but also the requirements of in-house profiles so as to ensure that all sensors of SICK can be
operated in a similar manner. This index indicates the version of the SICK profile used.

Table 111: System-specific ISDUs - Process Data Input
 ISDU
                                                                Data reposi‐                                  Default
 Index             Sub-      Name                   Data type                  Length            Access                       Value/range
                                                                tory                                          value
 DEC      HEX      index

 40       28       -         Process Data Input     PD in       -              device specific   ro           -               -


The current process data is made available as an index in this index.
For further information see "Process data", page 11.




8022709.1ML4/2024-03-11 | SICK                                                                    T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   59
Subject to change without notice

9 SENSOR REPLACEMENT/DATA STORAGE


9                Sensor replacement/data storage
All IO-Link Device have a backup and restore functionality - Data Storage (DS). The IO-Link Data Storage function
can be used to save previous parameters and transfer them to the replacement device, eliminating the need to
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
•    For details on using the data repository, see IO-Link Interface and System Specification, V1.1.2, section 10.4
     Data Storage (DS) at www.io-link.com, Downloads menu item.
•    Parameters that do not participate in data storage are marked in the IODD overview.


NOTE
To set the DSfunction, read the manufacturer-specific instructions for the IO-Link Master.




60       T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                        8022709.1ML4/2024-03-11 | SICK
                                                                                                   Subject to change without notice

DEVICE BACKWARD COMPATIBILITY (DBC) 10


10                 Device Backward Compatibility (DBC)
                                   IO-Link sensors typically offer extensive parameterization options to optimally adjust the
                                   device functionality to the requirements of the individual applications and to be able to
                                   operate the system reliably for many years. If such an IO-Link sensor is nevertheless
                                   defective, it is important for the replacement device to be compatible with the original
                                   device not only in terms of its sensor characteristics, but also with regard to the config‐
                                   urable IO-Link parameters and the IO-Link communication properties. This applies in
                                   particular if the defective device type is no longer available, e.g., due to a generation
                                   change, and a successor device needs to be used.
                                   IO-Link-capable sensors from SICK are generally backwards-compatible with their
                                   respective IO-Link-capable predecessor devices (if such predecessor devices exist) in
                                   terms of their communication properties and IO-Link functionality. They use the DBC
                                   mechanism (DBC = Device Backward Compatibility) standardized by the IO-Link Consor‐
                                   tium.
                                   DBC is based on the fact that an IO-Link device not only supports its current communica‐
                                   tion-related and functional IO-Link parameter set, but also the parameter set(s) of one
                                   or more predecessor devices. Each of these parameter sets is represented by its own
                                   device ID. Accordingly, a backwards-compatible IO-Link device supports multiple device
                                   IDs. Depending on the requirements, the device can be operated with its latest (default)
                                   device ID or with one of the supported predecessor device IDs.
                                   Ideally, the sensor is automatically set to the device ID required in the respective applica‐
                                   tion during start-up via DBC. Such an automatic device ID setting works if the IO-Link
                                   master supports DBC and the relevant IO-Link master ports are configured so that
                                   when IO-Link communication with the connected IO-Link device starts up, its identity
                                   is checked using the vendor and device ID (often found under the keyword “validation”).
                                   If the DBC-capable IO-Link device supports the vendor and device ID expected by the
                                   IO-Link master, the IO-Link device sets itself accordingly and starts up with this device ID
                                   requested by the master.
                                   To utilize the full potential of DBC, the data repository function (section 9) should also
                                   be used for the relevant IO-Link devices. This ensures that the respective IO-Link device
                                   automatically adopts the last active parameter settings from the predecessor device in
                                   addition to the correct device ID.
                                   Together with the data repository function, DBC thus enables plug & play device
                                   exchange even across device generations.
                                   If the requirements for automatic device ID switching via DBC are not met in an existing
                                   system, most DBC-capable IO-Link sensors from SICK allow manual switching of the
                                   device ID via index 16000 (Device ID setup), see table 23, page 18.




8022709.1ML4/2024-03-11 | SICK                                                   T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   61
Subject to change without notice

11 EVENTS


11                 Events
IO-Link events
With Events (events), an IO-Link Device reports events to the IO-Link Master without being prompted to do so by the
IO-Link Master.
Events are the only way for an IO-Link Device to report a sporadic event, information or problem. An IO-Link Master can
use events to inform about port-specific events, e.g. the disconnection of an IO-Link Device from the IO-Link Master.

NOTE
Not all IO-Link Master support the event mechanism, especially older ones. You can deactivate the generation of
events on the device page in “Notification handling (ISDU 227)”.

An event consists of:
•     Event Qualifier: Specification of information about:
      - Instance (event instance)
      - Source (event source)
      - Type (event type)
      - Mode (event mode)
•     Event Code: Details of the event content

11.1               Event Qualifier
The Event Qualifier (event qualifier) is a byte that contains some important information about the event.

           MODE                                     TYPE                     SOURCE               INSTANCE

     Bit 7                                                                                               Bit 0
Figure 12: Structure of an Event Qualifier

Instance
As a rule, all events come from the application layer.
Table 112: Instance
Value                                                                            Definition
0                                                                                Unknown
1-3                                                                              Reserved
4                                                                                Application
5-7                                                                              Reserved

Source
This bit decides whether the event comes from the IO-Link Master / Port (e.g. “No Device (communication)”) or from the
connected IO-Link Device (e.g. “Teach-in successful”).
Table 113: Source
Value                                                                            Definition
0                                                                                IO-Link Device
1                                                                                IO-Link Master / Port




62         T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                       8022709.1ML4/2024-03-11 | SICK
                                                                                                                    Subject to change without notice

EVENTS 11


Type
Type (event type) are classified as follows:
Table 114: Type
 Value                                    Definition                     Description                                 Event mode
 0                                        Reserved                       -                                           -
 1                                        Note                           For information purposes                    Event single shot
                                                                         only; the system is not
                                                                         restricted.
 2                                        Warning                        System is still functional, but             Event appears/disappears
                                                                         impaired in some way. You
                                                                         must rectify the problem as
                                                                         quickly as possible by taking
                                                                         appropriate measures.
 3                                        Error                          The system is no longer                     Event appears/disappears
                                                                         functional. Depending on the
                                                                         cause of the error, it may be
                                                                         possible to restore the func‐
                                                                         tion.

Mode
There are upcoming, outgoing and individual events (e.g. a note).
Table 115: Mode (event mode)
 Value                                                                   Definition
 0                                                                       Reserved
 1                                                                       Event single shot
 2                                                                       Event disappears
 3                                                                       Event appears


11.2               Event Code
An event outputs a 2-byte long Event Code that contains the cause for the occurrence of the event.
The information on the event source from Event Qualifier can be used to differentiate where the event comes from.

11.2.1             Device-specific events
Common Event Codes are defined in the IO-Link interface specification (Table D.1):
Table 116: Event Codes for devices2)
 Event Code ID                     Definition and recommended maintenance              DeviceStatus                  Type
                                   action                                              Value
 0x0000                            No malfunction                                      0                             Notification
 0x1000                            General malfunction – unknown error                 4                             Error
 0x1001 to                         Reserved
 0x17FF
 0x1800 to                         Vendor specific
 0x18FF
 0x1900 to                         Reserved
 0x3FF
 0x4000                            Temperature fault – Overload                        4                             Error



2)     Source: IO-Link Interface Specification V1.1.3, June 2019; Table D.1 - EventCodes for Devices

8022709.1ML4/2024-03-11 | SICK                                                           T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   63
Subject to change without notice

11 EVENTS

Event Code ID                      Definition and recommended maintenance                    DeviceStatus   Type
                                   action                                                    Value
0x4001 to                          Reserved
0x420F
0x4210                             Device temperature overrun – Clear source of heat         2              Warning
0x4211 to                          Reserved
0x421F
0x4220                             Device temperature underrun – Insulate Device             2              Warning
0x4221 to                          Reserved
0x4FFF
0x5000                             Device hardware fault – Device exchange                   4              Error
0x5001 to                          Reserved
0x500F
0x5010                             Component malfunction – Repair or exchange                4              Error
0x5011                             Non volatile memory loss – Check batteries                4              Error
0x5012                             Batteries low – Exchange batteries                        2              Warning
0x5013 to                          Reserved
0x50FF
0x5100                             General power supply fault – Check availability           4              Error
0x5101                             Fuse blown/open – Exchange fuse                           4              Error
0x5102 to                          Reserved
0x510F
0x5110                             Primary supply voltage overrun – Check tolerance          2              Warning
0x5111                             Primary supply voltage underrun – Check tolerance         2              Warning
0x5112                             Secondary supply voltage fault (Port Class B) – Check     2              Warning
                                   tolerance
0x5113 to                          Reserved
0x5FFF
0x6000                             Device software fault – Check firmware revision           4              Error
0x6001 to                          Reserved
0x631F
0x6320                             Parameter error – Check data sheet and values             4              Error
0x6321                             Parameter missing – Check data sheet                      4              Error
0x6322 to                          Reserved
0x634F
0x6350                             Reserved
0x6351 to                          Reserved
0x76FF
0x7700                             Wire break of a subordinate device – Check installation   4              Error
0x7701 to                          Wire break of subordinate device 1 …device 15 – Check     4              Error
0x770F                             installation
0x7710                             Short circuit – Check installation                        4              Error
0x7711                             Ground fault – Check installation                         4              Error
0x7712 to                          Reserved
0x8BFF
0x8C00                             Technology specific application fault – Reset Device      4              Error
0x8C01                             Simulation active – Check operational mode                3              Warning
0x8C02 to                          Reserved
0x8C0F


64       T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                            8022709.1ML4/2024-03-11 | SICK
                                                                                                                       Subject to change without notice

EVENTS 11


 Event Code ID                     Definition and recommended maintenance                  DeviceStatus                Type
                                   action                                                  Value
 0x8C10                            Process variable range overrun – Process Data uncertain 2                           Warning
 0x8C11 to                         Reserved
 0x8C1F
 0x8C20                            Measurement range exceeded – Check application          4                           Error
 0x8C21 to                         Reserved
 0x8C2F
 0x8C30                            Process variable range underrun – Process Data uncer‐   2                           Warning
                                   tain
 0x8C31 to                         Reserved
 0x8C3F
 0x8C40                            Maintenance required – Cleaning                         1                           Warning
 0x8C41                            Maintenance required – Refill                           1                           Warning
 0x8C42                            Maintenance required – Exchange wear and tear parts     1                           Warning
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
 0xFF91                            Data Storage upload request ("DS_UPLOAD_REQ") –         0                           Notification (single shot)
                                   internal, not visible to user
 0xFF92 to                         Reserved
 0xFFAF
 0xFFB0 to                         Reserved for Wireless extensions
 0xFFB7
 0xFFB8 to                         Reserved
 0xFFFF


In addition, IO-Link Devices support manufacturer-specific Event Codes, which must be described in the documenta‐
tion belonging to the IO-Link device.

Manufacturer-specific events

IO-Link communication is a IO-Link Master/IO-Link Device communication system.
With Events, an IO-Link device reports events to the IO-Link Master (without being prompted by the IO-Link Master).
Device-specific events are classified as follows:
Table 117: Device-specific events
 Notification                             For information purposes only; system is not restricted.
 Warning                                  System is still functional, but is impaired in some way. You must rectify this with suitable
                                          measures as soon as possible.
 Error                                    System is no longer functional. Depending on the cause of the error, it may be possible to
                                          restore functionality.



8022709.1ML4/2024-03-11 | SICK                                                             T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   65
Subject to change without notice

11 EVENTS

An Event issues an event code, which contains the cause of the occurrence of the Event.

NOTE
Not all IO-Link masters support the event mechanism.
In Notification Handling (Index 227), the generation of events can be deactivated on the device side.

The following events are supported:

Table 118: Events
Code
                                   Name                                    Type           Description                                                 Action
Dec            Hex
                                                                                          Triggered in the event of a short circuit on at least one
30480          0x7710              Short circuit                           Error          digital output.                                             Check device connection.
                                                                                          Overcurrent detection.
                                                                                          Triggered in the event of a short circuit on at least one
36000          0x8CA0              Short circuit on Qx                     Warning        digital output.                                             Check device connection.
                                                                                          Overcurrent detection.
                                                                                          Parameters have been amended (only when changing
36001          0x8CA1              New parameters                          Notification   the sensing range using control elements on the sen‐        None
                                                                                          sor housing or using the external teach-in via pin 2).
                                                                                                                                                      Clean the optical surfaces (sensor
36004          0x8CA4              Quality of run alarm                    Warning        Operational safety alarm
                                                                                                                                                      and reflector).
                                                                                          Teach/distance value outside the specified range (too       Readjust sensor or detection
36005          0x8CA5              Teach / value out of specified range    Notification
                                                                                          close, too far, no signal).                                 object. Teach in again.
36006          0x8CA6              Value out of specified range            Notification   Set value is outside the permissible range.                 Correct adjustment value.
                                                                                          Teach-in required
36007          0x8CA7              Teach-in necessary or teach-in error    Warning                                                                    Teach in again.
                                                                                          Teach-in error
36008          0x8CA8              Alarm upper temperature threshold       Warning        Upper temperature threshold has been exceeded.              Cool down sensor.
36009          0x8CA9              Alarm sender lifetime threshold         Warning        Alarm threshold for sender LED monitoring reached.          Prepare device exchange.
36010          0x8CAA              Alarm maintenance prediction            Warning        Alarm threshold for maintenance request reached.            Prepare on-site service.
                                                                                                                                                      Prepare on-site service or device
36011          0x8CAB              Alarm operating hours                   Warning        Alarm threshold for operating hours reached
                                                                                                                                                      exchange.
36015          0x8CAF              Alarm lower temperature threshold       Warning        Lower temperature threshold has been exceeded.              Warm up sensor.



Example of common Event Code
The SLG-2 from SICK transmits the event of an occurring "short-circuit" error:




Figure 13: Source: Logix Designer, Studio 5000 using SIG350 as IO-Link Master

Example of manufacturer-specific Event Code
The KTS from SICK sends the event "Successful teach-in":




Figure 14: Source: Logix Designer, Studio 5000 using SIG350 as IO-Link Master




66       T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                                              8022709.1ML4/2024-03-11 | SICK
                                                                                                                                                         Subject to change without notice

EVENTS 11


11.2.2             Port-specific events
Port-specific events are events that are output by the IO-Link-Master. The reason for their occurrence has something
to do with the port to which a device is connected.
Here too, a distinction is made between common Event Codes events that are specified in the IO-Link interface
specification (Table D.2) and events that are specific to the IO-Link master:
Table 119: EventCodes for ports 3)
 EventCode ID                        Definition and recommended maintenance action                                         Type
 0x0000 to                           Reserved
 0x17FF
 0x1800                              No Device (communication) Trigger: SMI_PortEvent (0x1800) by                          Error
                                     SM_PortMode (COMLOST)
 0x1801                              Startup parametrization error – check parameter                                       Error
 0x1802                              Incorrect VendorID – Inspection Level mismatch Trigger: SM_PortMode Error
                                     (COMP_FAULT)
 0x1803                              Incorrect DeviceID – Inspection Level mismatch Trigger: SM_PortMode Error
                                     (COMP_FAULT)
 0x1804                              Short circuit at C/Q – check wire connection                                          Error
 0x1805                              PHY overtemperature – check Master temperature and load                               Error
 0x1806                              Short circuit at L+ – check wire connection                                           Error
 0x1807                              Overcurrent at L+ – check power supply (e.g. L1+)                                     Error
 0x1808                              Device Event overflow                                                                 Error
 0x1809                              Backup inconsistency – memory out of range (2048 octets) Trigger:                     Error
                                     SMI_PortEvent (0x1809) by DS_Fault (SizeCheck_Fault)
 0x180A                              Backup inconsistency – identity fault Trigger: SMI_PortEvent (0x180A)                 Error
                                     by DS_Fault (Identification_Fault)
 0x180B                              Backup inconsistency – Data Storage unspecific error Trigger: SMI_Por‐ Error
                                     tEvent (0x180B) by DS_Fault (All other incidents)
 0x180C                              Backup inconsistency – upload fault                                                   Error
 0x180D                              Parameter inconsistency – download fault                                              Error
 0x180E                              P24 (Class B) missing or undervoltage                                                 Error
 0x180F                              Short circuit at P24 (Class B) – check wire connection (e.g. L2+)                     Error
 0x1810                              Short circuit at I/Q – check wiring                                                   Error
 0x1811                              Short circuit at C/Q (if digital output) – check wiring                               Error
 0x1812                              Overcurrent at I/Q – check load                                                       Error
 0x1813                              Overcurrent at C/Q (if digital output) – check load                                   Error
 0x1814 to                           Reserved
 0x1EFF
 0x1F00 to                           Vendor specific
 0x1FFF
 0x2000 to                           Safety extensions
 0x2FFF
 0x3000 to                           Wireless extensions
 0x3FFF
 0x4000 to                           Reserved
 0x5FFF
 0x6000                              Invalid cycle time Trigger: SM_PortMode (CYCTIME_FAULT)                               Error



3)     Source: IO-Link Interface Specification V1.1.3, June 2019, Table D.2 - EventCodes for Ports

8022709.1ML4/2024-03-11 | SICK                                                                 T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   67
Subject to change without notice

11 EVENTS

 EventCode ID                                   Definition and recommended maintenance action                           Type
 0x6001                                         Revision fault – incompatible protocol version Trigger: SM_PortMode     Error
                                                (REVISION_FAULT)
 0x6002                                         ISDU batch failed – parameter inconsistency?                            Error
 0x6003 to                                      Reserved
 0xFF20
 0xFF21a)                                       DL: Device plugged in ("NEW_SLAVE") – PD stop Trigger: SM_Port‐         Notification
                                                Mode (COMREADY); see Figure 71 (T10)
 0xFF22a)                                       Device communication lost ("DEV_COM_LOST") Trigger: see Figure          Notification
                                                101 (T9)
 0xFF23a)                                       Data Storage identification mismatch ("DS_IDENT_MISMATCH") Trig‐        Notification
                                                ger: see Figure 104 (T15)
 0xFF24a)                                       Data Storage buffer overflow ("DS_BUFFER_OVERFLOW") Trigger: see        Notification
                                                Figure 104 (T17)
 0xFF25a)                                       Data Storage parameter access denied ("DS_ACCESS_DENIED") Trig‐         Notification
                                                ger: see Figure 104 (T29), Figure 105 (T32), Figure 107 (T39)
 0xFF26                                         Port status changed ‒ Use "SMI_PortStatus" service for port status in   Notification
                                                detail Trigger: see Figure 101 (T12)
 0xFF27                                         Data Storage upload completed and new data object available Trigger:    Notification
                                                see Figure 104 (T26)
 0xFF28 to                                      Reserved
 0xFF30
 0xFF31a)                                       DL: Incorrect Event signalling ("EVENT") Trigger: none                  Notification
 0xFF32 to 0xFFFF                               Reserved
a)   No more required due to SMI Event concept. Not recommended for new implementations.

Example of common port-specific Event Code
SIG350 sends the port event of a disappearing 'No Device (communication)' error:




Figure 15: Source: Logix Designer, Studio 5000 using SIG350 as IO-Link Master

Technical principle of operation in detail
An IO-Link device manufacturer can choose from various Frame Types, depending on the amount of process and
service data required for the respective device.




68          T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                     8022709.1ML4/2024-03-11 | SICK
                                                                                                                                   Subject to change without notice

EVENTS 11


TYPE_0               MC            CKT
                                         OD
                                               CKS

TYPE_1_1             MC            CKT
                                         PD0   PD1
                                                      CKS

TYPE_1_2             MC            CKT
                                         OD0   OD1
                                                      CKS

TYPE_1_V             MC            CKT
                                         OD0           ODn
                                                               CKS


TYPE_2_1             MC            CKT
                                         OD
                                               PD     CKS


TYPE_2_2             MC            CKT
                                         OD
                                               PD0    PD1      CKS


TYPE_2_3             MC            CKT   PD
                                               OD
                                                      CKS


TYPE_2_4              MC           CKT   PD0   PD1
                                                       OD
                                                               CKS


TYPE_2_5              MC           CKT   PD
                                               OD
                                                      PD       CKS


TYPE_2_V              MC           CKT   PD0          PDn-1
                                                                OD0                 ODm-1
                                                                                                    PD0                          PDk-1          CKS

Figure 16: Frame Types, source: IO-Link Interface Specification V1.1.3, June 2019

The figure above shows the available Frame Types. Each block represents one byte.
What they all have in common is that the Frame begins with MC (Master-Sequence-Control), followed by CKT (Checksum /
M-Sequence-Type). In addition, all Frames end with CKS (Checksum / Status).
It is precisely this CKS byte that is decisive for the event mechanism:

  Event PD
  flag status                                            Checksum

    Bit 7                                                                                               Bit 0
Figure 17: CKS byte, source: IO-Link Interface Specification V1.1.3, June 2019



8022709.1ML4/2024-03-11 | SICK                                                T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors     69
Subject to change without notice

11 EVENTS

The CKS byte is the last part of the response message from the Device to the master. It consists of a 6-bit
checksum (to check the integrity of the response message from the device to the master), a Flag to display valid or
invalid process data and the Eventflag.
This Eventflag indicates that an event has occurred on the device side. As soon as the master recognizes the
activated Eventflag, it starts the procedure for reading the event details (Event Qualifier and Event Code).
An IO-Link-Master will then propagate the event and its content to its gateway application and thus make the event
available on its fieldbus and/or cloud interface.
How the event and its information are then processed further depends heavily on the protocol of the interface
used at the next level.
You can find some examples in section 11.3.

11.3            Event processing using the example of EtherNet/IP
                (Rockwell Logix Designer, Studio 5000)
The following example: The program (SIG350_EventExample.ACD) shows how events of a SIG350 are read using
an Ethernet/IP interface.
•    PLC: Allen Bradly, L30ER
•    IO-Link master: SIG350
•    Rockwell Logix Designer, Studio 5000




70      T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                      8022709.1ML4/2024-03-11 | SICK
                                                                                                Subject to change without notice

EVENTS 11


1.     Check whether events are pending




       The Ethernet/IP input process data of SIG350 contains an IOL status byte with the following coding.
       With bit 3, the IO-Link master reports whether events are currently pending or not.




       The first line in the main program copies the flag into a variable.




8022709.1ML4/2024-03-11 | SICK                                               T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   71
Subject to change without notice

11 EVENTS




     Source: Rockwell Logix Designer, Studio 5000
2.   Read out event details
     There is a CIP object for reading out details (Event Qualifier, Event Code) that provides access to all information.
     To receive the event details, the CIP Explicit Messaging System (CIP messaging system) must be used.




     Source: netPROXY System Development
     The easiest access is provided by attribute 22.
     The response of the explicit message is the oldest pending event on the respective port. Reading the event
     automatically deletes this event from the queue in the IO-Link master. As soon as all pending events have
     been read/deleted, the Event Flag is deleted from the Ethernet/IP process data.
     Explicit Message
     ° Service code: 0x0E
     ° Class code: 0x41
     ° Instance: 100...107
     ° Attributes: 0x16




72      T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                            8022709.1ML4/2024-03-11 | SICK
                                                                                                      Subject to change without notice

EVENTS 11




       Figure 18: Rockwell Logix Designer, Studio 5000




8022709.1ML4/2024-03-11 | SICK                           T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   73
Subject to change without notice

11 EVENTS

3.   Interpretation of the event details
     The example program shown contains an implementation of how an event could be interpreted.




     Source: Rockwell Logix Designer, Studio 5000
     The interpreted event is located in the controller tags of the example program.




     Source: Rockwell Logix Designer, Studio 5000




74      T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                8022709.1ML4/2024-03-11 | SICK
                                                                                          Subject to change without notice

TECHNICAL DATA 12


12                 Technical data
Table 120: Mechanics/Electronics
 Cable length of IO-Link master and IO-Link device   max. 20 m
 IO-Link specification                               V1.1




8022709.1ML4/2024-03-11 | SICK                                   T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   75
Subject to change without notice

13 LIST OF ABBREVIATIONS


13               List of abbreviations
Table 121: List of abbreviations
IODD           IO Device Description                                       Device description file of an IO-Link device
ISDU           Indexed Service Data Unit                                   Service data object in IO-Link
COM1                                                                       COM1 = 4.8 kbit/s
COM2           SDCI communication mode                                     COM2 = 38.4 kbit/s
COM3                                                                       COM3 = 230.4 kbit/s
SDCI           Single-drop digital interface                               Official (specification) name for IO-Link technology
SDD            SOPAS ET Device Description                                 Device description file / driver for SICK SOPAS ET software




76       T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                                                  8022709.1ML4/2024-03-11 | SICK
                                                                                                                             Subject to change without notice

INDEX 14


14                      Index
I                                                                                                     0121 Pin2 configuration.............................................................. 16
                                                                                                      0153 Temperature........................................................................ 39
ISDU                                                                                                  0154 Temperature........................................................................ 39
   0002 Standard command..................................................... 33, 37                  0155 Remaining sender lifetime................................................. 39
   0002 Standard command (job backup)...................................... 50                        0175 Quality of run...................................................................... 39
   0002 Standard command (Reset)............................................... 14                    0176 Quality of run threshold..................................................... 40
   0002 Standard command (Smart Task A71)............................. 46                             0177 Quality of alignment........................................................... 40
   0002 Standard command (WE, WEO)......................................... 31                        0178 Maintenance prediction..................................................... 40
   0002 Standard command (WL, WLA)......................................... 24                        0179 Alarm thresholds for diagnostic parameters.................... 41
   0002 Standard command (WLG)................................................ 26                     0180 Current receiver level (WL, WLA)....................................... 26
   0002 Standard command (WTB, WTS, WTL).............................. 19                             0180 Current receiver level (WLG).............................................. 31
   0012 Device access locks........................................................... 14             0180 Current receiver level (WT)................................................. 23
   0013 Profile characteristic.......................................................... 58           0181 Upper threshold (WLG)....................................................... 31
   0014 PDInput Descriptor............................................................. 58            0182 Lower threshold (WLG)....................................................... 31
   0015 PDOutput Descriptor.......................................................... 58              0190 Operating hours.................................................................. 41
   0016 Vendor Name...................................................................... 13          0204 Find me............................................................................... 14
   0018 Product Name..................................................................... 13          0205 SICK profile version............................................................ 59
   0019 Product ID........................................................................... 13      0219 Article No............................................................................. 13
   0020 Product Text........................................................................ 13       0226 Quality of run alarm output................................................ 42
   0021 Serial Number..................................................................... 13         0227 Notification Handling.......................................................... 17
   0022 Hardware version................................................................ 14           0229 Abstand zum Objekt.................................................... 23, 37
   0023 Firmware version................................................................ 14           0234 Display settings................................................................... 17
   0024 Application Specific Tag..................................................... 13              0235 Eco mode............................................................................ 18
   0036 Device Status...................................................................... 38        1000 Counter version (Smart Task A71).................................... 47
   0037 Detailed Device Status....................................................... 38              1001 Counter mode (Smart Task A71)....................................... 47
   0040 Process Data Input............................................................. 59            1002 Preset mode (Smart Task A71)......................................... 47
   0058 Teach-in channel................................................................. 33          1003 Preset value (Smart Task A71).......................................... 47
   0058 Teach-in channel (WE, WEO).............................................. 32                   1004 Comparator value low (Smart Task A71).......................... 47
   0058 Teach-in channel (WL, WLA).............................................. 24                   1005 Comparator value low (Smart Task A71).......................... 47
   0058 Teach-in channel (WLG)..................................................... 27                1006 Counter value (Smart Task A71)....................................... 47
   0058 Teach-in channel (WTB, WTS, WTL)................................... 19                        1016 Time measurement version (Smart Task A70)................. 45
   0059 Teach................................................................................... 34   1017 Time base (Smart Task A70)............................................. 45
   0059 Teach (WE, WEO)................................................................ 32            1018 Measuring mode (Smart Task A70).................................. 45
   0059 Teach (WL, WLA)................................................................. 24           1019 Comparator value low (Smart Task A70).......................... 45
   0059 Teach (WLG)........................................................................ 27        1020 Comparator value high (Smart Task A70)......................... 45
   0059 Teach (WTB, WTS, WTL)..................................................... 19                 1032 Debounce version (Smart Task A70)................................ 46
   0060 Qint.1 SP1 / SP2 (WE, WEO).............................................. 32                   1032 Debounce version (Smart Task A71)................................ 48
   0060 Qint.1 SP1 / SP2 (WL, WLA) ............................................. 25                   1033 Debounce time 1 (Smart Task A70).................................. 46
   0060 Qint.1 SP1 / SP2 (WLG)..................................................... 28                1033 Debounce time 1 (Smart Task A71).................................. 48
   0060 Qint.1 SP1 / SP2 (WTB, WTS, WTL).................................. 20                         1034 Quality D1 (Smart Task A70)............................................. 46
   0060 Qint.1 SP1 / SP2 (WTT)..................................................... 34                1034 Quality D1 (Smart Tasks A71)........................................... 48
   0061 Qint.1 configuration (WE, WEO)......................................... 32                    1035 Debounce time 2 (Smart Tasks A71)................................ 48
   0061 Qint.1 configuration (WL, WLA)......................................... 25                    1036 Quality D2 (Smart Tasks A71)........................................... 48
   0061 Qint.1 configuration (WLG)................................................ 28                 1080 SLTI Version (Smart Tasks 00)........................................... 42
   0061 Qint.1 configuration (WTB, WTS, WTL).............................. 20                         1081 Input Selector 1 (Smart Task 00)...................................... 51
   0061 Qint.1 configuration (WTT)................................................. 34                1083 Logic 1 (Smart Tasks 00)................................................... 43
   0062 Qint.2 SP1 / SP2 (WE, WEO).............................................. 33                   1084 Logic 2 (Smart Tasks 00)................................................... 43
   0062 Qint.2 SP1 / SP2 (WL, WLA).............................................. 25                   1085 Timer 1 mode (Smart Task 00).......................................... 43
   0062 Qint.2 SP1 / SP2 (WLG)..................................................... 28                1086 Timer 2 mode (Smart Task 00).......................................... 43
   0062 Qint.2 SP1 / SP2 (WTB, WTF, WTL, WTS)......................... 20                             1087 Time 1 setup (Smart Task 00)........................................... 43
   0062 Qint.2 SP1 / SP2 (WTT)..................................................... 34                1088 Time 2 setup (Smart Task 00)........................................... 43
   0063 Qint.2 configuration (WE, WEO)......................................... 33                    1089 Inverter 1 (Smart Tasks 00)............................................... 44
   0063 Qint.2 configuration (WL, WLA)......................................... 25                    1090 Inverter 2 (Smart Tasks 00)............................................... 44
   0063 Qint.2 configuration (WLG)................................................ 28                 1091 Time 1.1 setup (Smart Task 00)........................................ 43
   0063 Qint.2 configuration (WTB WTF, WTL, WTS)...................... 21                             1092 Time 2.1 setup (Smart Task 00)........................................ 43
   0063 Qint.2 configuration (WTT)................................................. 34                1093 Inverter ext. input (Smart Task A72)................................. 51
   0064 Device Specific Name........................................................ 13               1093 Inverter external input........................................................ 18
   0083 Detection mode (WLG)....................................................... 29                1096 Speed and Length Measurement version (Smart Task A72)
   0083 Detection mode (WT)................................................... 21, 22                                                                                                       ...... 51
   0089 Measurement averaging.................................................... 36                  1097 Measurement mode (Smart Task A72)............................. 52
   0090 Teach-in offset............................................................. 23, 37           1098 Distance between measuring points [in 100 µm] (Smart
   0092 Physical input/output type configuration pin 2................ 15                                                                                                  Task A72)...... 52
   0097 Sender configuration.......................................................... 15             1099 Pulses per 100 millimeter (Smart Task A72)................... 53
   0112 AutoAdapt (WLG)................................................................. 29           1100 Measurement threshold 1................................................. 53
   0113 Threshold presetting.......................................................... 30             1101 Measurement threshold 2................................................. 53
   0114 Quality of teach............................................................ 38, 38           1102 Switching mode.................................................................. 53
   0115 Oscillation frequency at output.......................................... 15                  1103 Time setup impulse width.................................................. 53
   0120 Process data select............................................................ 16            1104 Time setup impulse shift.................................................... 53


8022709.1ML4/2024-03-11 | SICK                                                                                      T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors             77
Subject to change without notice

14 INDEX

     1105 Object speed for reference run.......................................... 54
     1106 Length measurement value............................................... 55
     1107 Speed measurement value................................................ 55
     1109 Smart Task operating state................................................ 55
     1112 Object + Gap Monitor version............................................ 57
     1113 Measurement threshold 1 - object.................................... 57
     1114 Measurement threshold 2 - object.................................... 57
     1115 Switching mode object....................................................... 57
     1116 Time setup impulse width object....................................... 57
     1117 Time setup impulse shift object........................................ 57
     1118 Measurement threshold 1 - gap........................................ 57
     1119 Measurement threshold 2 - gap........................................ 57
     1120 Switching mode gap........................................................... 57
     1121 Time setup impulse width gap........................................... 57
     1122 Time setup impulse shift gap............................................ 57
     1123 Impulse buffer state........................................................... 58
     1123 Impulse buffer state (Smart Task A72)............................. 56
     16000 Device ID setup................................................................ 18
     16384 Qint.3 SP1 / SP2 (WTT)................................................... 34
     16385 Qint.3 configuration (WTT).............................................. 34
     16386 Qint.4 SP1 / SP2 (WTT)................................................... 35
     16387 Qint.4 configuration (WTT).............................................. 35
     16388 Qint.5 SP1 / SP2 (WTT)................................................... 35
     16389 Qint.5 configuration (WTT)........................................ 35, 35
     16390 Qint.6 SP1 / SP2 (WTT)................................................... 35
     16392 Qint.7 SP1 / SP2 (WTT)................................................... 35
     16393 Qint.7 configuration (WTT).............................................. 35
     16394 Qint.8 SP1 / SP2 (WTT)................................................... 35
     16395 Qint.8 configuration (WTT).............................................. 36




78            T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors                   8022709.1ML4/2024-03-11 | SICK
                                                                                                   Subject to change without notice

INDEX 14




8022709.1ML4/2024-03-11 | SICK     T E C H N I C A L I N F O R M A T I O N | Photoelectric sensors   79
Subject to change without notice

8022709.1ML4/2024-03-11/en
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