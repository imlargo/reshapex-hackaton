TECHNICAL INFORMATION


PSS
SICK Smart Sensors/IO-Link

Device configuration – Advanced operating instructions

Product described
PSS

Manufacturer
SICK AG
Erwin-Sick-Str. 1
79183 Waldkirch
Germany

Legal information
This work is protected by copyright. Any rights derived from the copyright shall be reserved for SICK AG. Reproduc‐
tion of this document or parts of this document is only permissible within the limits of the legal determination of
Copyright Law. Any modification, abridgment or translation of this document is prohibited without the express writ‐
ten permission of SICK AG.
The trademarks stated in this document are the property of their respective owner.
© SICK AG. All rights reserved.

Original document
This document is an original document of SICK AG.




2       T E C H N I C A L I N F O R M A T I O N | PSS                                             8023268/2018-06-27 | SICK
                                                                                                Subject to change without notice

CONTENTS


Contents
                                   1   About this document........................................................................                             5
                                       1.1     Purpose of this document........................................................................                 5
                                       1.2     Intended use.............................................................................................        5
                                       1.3     Symbols.....................................................................................................     5

                                   2   Description of IO-Link.......................................................................                           6

                                   3   Accessories for visualization, configuration, and integration.....                                                      7

                                   4   Data repository..................................................................................                       8

                                   5   Physical layer.....................................................................................                     9

                                   6   Process data...................................................................................... 10
                                       6.1     Quality of print...........................................................................................     10
                                       6.2     Q1 valid.....................................................................................................   10

                                   7   Service data....................................................................................... 11
                                       7.1     Device identification.................................................................................          11
                                               7.1.1     Device identification................................................................                 11
                                               7.1.2     Product text and serial number..............................................                          11
                                               7.1.3     Definable names.....................................................................                  11
                                               7.1.4     Hardware and firmware version..............................................                           12
                                               7.1.5     Find me.....................................................................................          12
                                       7.2     General device settings............................................................................             12
                                               7.2.1     Pin 2 configuration..................................................................                 12
                                               7.2.2     Key lock....................................................................................          13
                                               7.2.3     Display orientation...................................................................                13
                                               7.2.4     Disable sender light source....................................................                       13
                                               7.2.5     Restore factory settings/reset................................................                        14
                                               7.2.6     (De)activate events..................................................................                 14
                                       7.3     Teach-in / detection settings...................................................................                14
                                               7.3.1     Configuration Q1 / inversion...................................................                       14
                                               7.3.2      Switching output inversion......................................................                     14
                                               7.3.3      Switch-on and switch-off delay/impulse generator...............                                      15
                                               7.3.4      Trigger input delay....................................................................              16
                                               7.3.5      Teach-in....................................................................................         16
                                               7.3.6      Teach-in status.........................................................................             18
                                               7.3.7      Switching threshold position...................................................                      18
                                               7.3.8      Background evaluation...........................................................                     18
                                               7.3.9      Job assurance..........................................................................              19
                                               7.3.10 Reference pattern....................................................................                    20
                                               7.3.11 Last read pattern.....................................................................                   20
                                       7.4     Installation / Diagnostics.........................................................................             21
                                               7.4.1      Device state.............................................................................            21

8023268/2018-06-27 | SICK                                                                                      T E C H N I C A L I N F O R M A T I O N | PSS    3
Subject to change without notice

CONTENTS


                                                              7.4.2    Device temperature.................................................................                21
                                                              7.4.3    Teach-in quality........................................................................           21
                                                     7.5      System-specific ISDUs..............................................................................         22
                                                              7.5.1    Teach-in channel......................................................................             22
                                                              7.5.2    Process data as ISDU..............................................................                 22

                                     8               Events.................................................................................................. 23

                                     9               Use cases............................................................................................ 24
                                                     9.1      Configuring job assurance.......................................................................            24
                                                     9.2      Teach-in via IO-Link...................................................................................     26
                                                     9.3      Teach-in via IO-Link...................................................................................     27
                                                     9.4      Control reading window via IO-Link.........................................................                 28

                                     10              List of abbreviations.......................................................................... 29

                                     11              Index.................................................................................................... 30




4    T E C H N I C A L I N F O R M A T I O N | PSS                                                                                               8023268/2018-06-27 | SICK
                                                                                                                                               Subject to change without notice

ABOUT THIS DOCUMENT 1


1                     About this document
1.1                   Purpose of this document
The ISDU descriptions in this document apply to IO-Link-enabled photoelectric sensors (Smart Sensors) with the
following principle of operation: PSS.
In some cases, functions may be described in this document which are not supported by individual sensors. The
functions in question are marked accordingly (see "Symbols", page 5).
The specific functional scope of an individual sensor is described in full in the Supplement to operating instructions on
the relevant product page under www.sick.com.


1.2                   Intended use
Use IO-Link only as described in this documentation.

1.3                   Symbols

NOTICE
This symbol indicates important information.


NOTE
This symbol provides additional information, e.g., dependencies / interactions between the described function and
other functions, or when individual functions are not supported by every sensor.




8023268/2018-06-27 | SICK                                                             T E C H N I C A L I N F O R M A T I O N | PSS   5
Subject to change without notice

2 DESCRIPTION OF IO-LINK


2                Description of IO-Link
IO-Link and control integration
IO-Link is a non-proprietary internationally standardized communication technology, which makes it possible to
communicate with sensors and actuators in industrial environments (IEC 61131-9).
IO-Link devices communicate with higher-level control systems via an IO-Link master. The IO-Link devices (slaves)
are connected to these via a point-to-point connection.
Different variants of IO-Link master are available. In most cases, they are remote fieldbus gateways or input cards
for the backplane bus of the control used.
To make it possible for an IO-Link sensor to communicate with the control, both the IO-Link master and the
IO-Link sensor must be integrated in the hardware configuration in the control manufacturer’s Engineering Tool.
To simplify the integration process, SICK provides sensor-specific device description files (IODD = IO-Link Device
Description) for IO-Link devices.
You can download these device description files free of charge: www.sick.com/[device-part number].
Not all control system manufacturers support the use of IODDs. If third-party IO-Link masters are used, it is possi‐
ble to integrate the IO-Link sensor by manually entering the relevant sensor parameters directly during the hard‐
ware configuration.
To ensure that the IO-Link sensor can be easily integrated into the control program, SICK also provides function
blocks for many control systems. These function blocks make it easier to read and write the individual
sensor parameters, for example, and provide support when it comes to interpreting the process data supplied by
the IO-Link sensor. You can also download them free of charge from the homepage: www.sick.com/[device-part
number].
On SICK’s YouTube channel, you can find some tutorials, which will help you to integrate SICK IO-Link masters:
www.youtube.com/SICKSensors.
If you have any questions, SICK’s Technical Support is available to help all over the world.




6        T E C H N I C A L I N F O R M A T I O N | PSS                                             8023268/2018-06-27 | SICK
                                                                                                 Subject to change without notice

ACCESSORIES FOR VISUALIZATION, CONFIGURATION, AND INTEGRATION 3


3                     Accessories for visualization, configuration, and integration
Using the SiLink2-Master, you can easily connect IO-Link sensors from SICK to a PC or a laptop via USB. You can
then quickly and easily test or configure the connected sensors using the SOPAS ET program (SICK Engineering
Tool with graphic user navigation and convenient visualization).

The corresponding visualization files (SDD = SOPAS Device Description) are available for many devices so that you
can operate the IO-Link sensors using SOPAS ET.
You can download SOPAS ET and the device-specific SDDs directly and free of charge from the SICK homepage:
www.sick.com.
Various IO-Link masters are available from SICK for integrating IO-Link masters using fieldbus. For more details,
see: www.sick.com.




8023268/2018-06-27 | SICK                                                         T E C H N I C A L I N F O R M A T I O N | PSS   7
Subject to change without notice

4 DATA REPOSITORY


4               Data repository
When the current IO-Link standard V1.1 was introduced, the automatic data repository (Data Storage) was added
to IO-Link’s range of functions. The data repository allows the machine operator to replace defective IO-Link
devices with corresponding replacement devices without having to reconfigure these manually.
When the data repository is activated, the IO-Link 1.1 master always saves the last valid setting parameters of all
connected IO-Link 1.1 devices in its local memory. If you replace one of the connected IO-Link devices with
another device which is compatible with the function, the IO-Link master will transfer the last valid parameter set
of the previous sensor to the new sensor automatically.
The data repository therefore means that devices can be replaced in a plug-and-play manner within a matter of
seconds – without complex reconfiguration, special hardware or software tools, and specific specialist knowledge.

NOTE
•    To use the data repository, you must activate it in the IO-Link master.
•    When the conversion of one or several sensor parameters is initiated via the control, then the control must
     activate the Data Storage Upload Request-Flag as the final command in the sensor. Only this initiates the data
     repository.
•    Uploading / downloading sensor parameters using the data repository function can take between a few hun‐
     dred milliseconds and three seconds depending on the volume of data and the IO-Link master used (typical
     values; values can differ in practice).
•    For details on using the data repository, see IO-Link Interface and System Specification, V1.1.2, chapter 10.4
     Data Storage (DS) at www.io-link.com, Downloads menu item.




8       T E C H N I C A L I N F O R M A T I O N | PSS                                              8023268/2018-06-27 | SICK
                                                                                                 Subject to change without notice

PHYSICAL LAYER 5


5                     Physical layer
The physical layer describes the basic IO-Link device data (see table below). The device data is automatically
shared with the IO-Link master. It is important to ensure that the used IO-Link master supports this performance
data.

NOTICE
The maximum current consumption of the IO-Link sensor (including load at the outputs) must not exceed the per‐
missible output current of the relevant port on the IO-Link master.

Table 1: Physical layer – System data
 SIO mode                                                 Yes
 Min. cycle time                                          4.3 ms
 Baud rate                                                COM 2 (38.4 kbit/s)
 Process data length PD in (from device to master)        2 bytes
 IODD version                                             V1.1
 Supported IO-Link version                                V1.1
 Supports block-parametrization                           Yes




8023268/2018-06-27 | SICK                                                       T E C H N I C A L I N F O R M A T I O N | PSS   9
Subject to change without notice

6 PROCESS DATA


6                     Process data
Process data is transmitted cyclically. There is no confirmation of receipt.
The master determines the cycle time; however, this must not be less than the minimum cycle time of the sensor
("figure X").

NOTE
The service data (acyclic data) does not influence the cycle time.

Table 2: Process data structure
     Byte offset                                              Byte 1                                                        Byte 0
      Bit offset          15         14        13        12            11     10         9   8   7   6   5      4       3               2               1              0

                                                                   Quality of print                          Reserved                Q1 valid       Reserved           Q1

                                                                                                                               0 = OFF                            0 = OFF
                                                               Value range = 0 ... 100
                                                                                                                               1 = ON                             1 = ON



6.1                   Quality of print
After each reading taken by the PSS sensor, the quality of print is calculated and output. This quality indicator
reflects the degree of detection of the taught-in pattern.
 100Read pattern is identical to the taught-in pattern
   %
 50%Only half of the read pattern reflects the taught-in pattern
  0%No overlap detected between taught-in and read pattern

6.2                   Q1 valid
The bit indicates whether the current quality of print and Q1 are valid.
0       During pattern reading and while the quality calculation is being executed, the switching output is invalid
1       When the quality calculation is complete, the output values are valid




10            T E C H N I C A L I N F O R M A T I O N | PSS                                                                                       8023268/2018-06-27 | SICK
                                                                                                                                                Subject to change without notice

SERVICE DATA 7


7                     Service data
Service data is only exchanged between the control and IO-Link sensor via the IO-Link master on request by the
control (acyclically). The service data is designated as ISDUs. Using an ISDU, you can change the configuration or
read out information about the status of the sensor.
The respective counterpart confirms receipt of the data.
If the sensor does not answer within five seconds, the master reports a communication error.

7.1                   Device identification

7.1.1                 Device identification
Table 3: Device identification
 ISDU
                                                                           Data reposi‐                       Default
 Index               Sub-          Name                        Data type                  Length     Access                   Value/range
                                                                           tory                               value
 DEC        HEX      index

 16         10                     Vendor name                                            7 byte              SICK AG
                                                                                                              www.sick.co
 17         11                     Vendor text                                            64 byte
                                                                                                              m
                     -                                         String
 18         12                     Product name                                           30 byte
                                                                           -                         ro
                                                                                                              see ISDU
 19         13                     Product ID                                             13 byte
                                                                                                              219
                     0             Product ID                  Record                     7 byte
 219        DB
                     1             Product ID IO-Link device   String                     7 byte


The Product ID is also the part number of the connected IO-Link device.
For reasons of standardization, this may also contain a reference to ISDU 219. In this case, the Product ID (part
number) is filed under ISDU 219.
To make it possible to provide a family IODD for a device family, the Product ID can be found under Device identifi‐
cation (ISDU 219) for SICK IO-Link devices.
Furthermore, the part numbers for the components associated with the system are filed in sub-index 2…x for sen‐
sors.

7.1.2                 Product text and serial number
Table 4: Device identification – Product text/serial number
 ISDU
                                                                           Data reposi‐                       Default
 Index               Sub-          Name                        Data type                  Length     Access                   Value/range
                                                                           tory                               value
 DEC        HEX      index

 20         14                     Product text                                           64 bytes            “PSS”
                     -                                         String      -                         ro
 21         15                     Serial number                                          8 bytes


Format of the serial number:
YYWWnnnn (Y = year, W = week, n = sequential numbering)

7.1.3                 Definable names
Table 5: Device identification – Specific tag / name
 ISDU
                                                                           Data reposi‐
 Index               Sub-          Name                        Data type                  Length     Access   Default value          Value/range
                                                                           tory
 DEC        HEX      index

 24         18       -             Application-specific tag                yes                                *******
                                                               String                     32 byte    rw
 64         40       -             Device-specific name                    No                                 *******


In Application-specific tag, you can store any text with a maximum of 32 characters. This can be useful for describing
the exact position or task of the sensor in the overall machine. The Application-specific tag is saved via the Data repos‐
itory.


8023268/2018-06-27 | SICK                                                                                          T E C H N I C A L I N F O R M A T I O N | PSS   11
Subject to change without notice

7 SERVICE DATA

In Device-specific name, you can also store any text with a maximum of 32 characters. This name is NOT saved via
the Data repository and is therefore available for information which is valid temporarily or for information which is
only applicable to this sensor.


7.1.4              Hardware and firmware version
Table 6: Device identification – Version
ISDU
                                                                           Data reposi‐                      Default
Index              Sub-        Name                            Data type                  Length    Access                  Value/range
                                                                           tory                              value
DEC       HEX      index

22        16                   Hardware version                                           4 byte             xxxx
                   -                                           String      -                        ro
23        17                   Firmware version                                           12 byte            Vxxx.xxx.xxx


This ISDU indicates the hardware and software versions.

7.1.5              Find me
Table 7: Device identification – Find me
ISDU
                                                                           Data reposi‐                      Default
Index              Sub-        Name                            Data type                  Length    Access                  Value/range
                                                                           tory                              value
DEC       HEX      index

                                                                                                                            0 = Find me deactivated
                                                                                                                            1 = Find me activated, yellow LED flashes at
204       CC       -           Find me                         UInt        no             8 bit     rw       0              1 Hz
                                                                                                                            16 = Find me activated, yellow LED + Q1 (pin
                                                                                                                            2) flashes at 1 Hz


The sensor can be uniquely identified using Find me. For machines with several identical sensors, it is therefore
possible to uniquely identify the device with which communication is currently taking place.
When Find me is activated, the yellow indicator LED of the sensor flashes at 1 Hz.

To identify the switching output (pin 2) in the control cabinet, you can also activate or deactivate the digital output
at pin 2 by writing the value 16.

NOTICE
Observe the effect of the output activation and deactivation on the connected system.


7.2                General device settings

7.2.1              Pin 2 configuration
Table 8: General device settings – Pin 2 configuration
ISDU
                                                                           Data reposi‐                      Default
Index              Sub-        Name                            Data type                  Length    Access                  Value/range
                                                                           tory                              value
DEC       HEX      index

                                                                                                                            0 = Deactivated
121       79       -           Pin2 configuration              UInt        yes            1 byte    rw       32             17 = External teach-in
                                                                                                                            32 = Switching output Q


Assignment options for pin 2 of the PSS:
0       Deactivated                                        Pin 2 in high-impedance state.
17      External teach-in                                  Pin 2 functions as a digital input for teaching-in the sensor.
32      Switching output Q                                 Pin 2 functions as an additional digital switching output (Q1). There is no option
                                                           to teach-in a separate switching threshold. (Function not available or pin 5) Par‐
                                                           ticularly with constant IO-Link communication via pin 4, it is advisable to config‐
                                                           ure the quick switching output (50 kHz) to pin 2 in order to continue to benefit
                                                           from the quick switching frequency.




12         T E C H N I C A L I N F O R M A T I O N | PSS                                                                                    8023268/2018-06-27 | SICK
                                                                                                                                          Subject to change without notice

SERVICE DATA 7


7.2.2                 Key lock
Table 9: General device settings – Device access locks
 ISDU
                                                                             Data reposi‐                     Default
 Index               Sub-          Name                          Data type                  Length   Access                  Value/range
                                                                             tory                             value
 DEC        HEX      index

                                                                                                                             Bit no.
                                                                                                                             0                    Not available
                                                                                                                                                  0 = Data Storage released
                                                                                                                             1
                                                                                                                                                  1 = Data Storage locked

                                   Device access locks (key                                                                                       0 = Keys released
 12         0C       -                                           Record      yes            2 byte   rw       -              2                    1 = Key lock (can only be
                                   lock)
                                                                                                                                                  reset via IO-Link)
                                                                                                                                                  0 = Keys released
                                                                                                                             3                    1 = Key lock (can be reset
                                                                                                                                                  via display keys)
                                                                                                                             4 – 15               Not available


With Device access locks, you can lock or unlock various sensor functions.
The functionality has been recorded in the IO-Link interface specification.
Bit 1        Data Storage                                You can lock the Data Storage functionality using bit 1.
                                                         When the bit is set, the sensor rejects Data Storage write requests from the IO-Link
                                                         master with an error message.
Bit 2        Key lock                                    You can completely lock the controls on the sensor using bit 2 (key lock).
             Local                                       When the bit is set, all keys are locked.
             parameterization                            The lock can only be reset via IO-Link.
Bit 3        Key lock                                    You can completely lock the controls on the sensor using bit 3 (key lock).
             Local user                                  When the bit is set, all keys are locked.
             interface                                   In this case, you can deactivate the lock by pressing the ± key for 10 seconds.

7.2.3                 Display orientation
Table 10: General device settings – Display orientation
 ISDU
                                                                             Data reposi‐                     Default
 Index               Sub-          Name                          Data type                  Length   Access                  Value/range
                                                                             tory                             value
 DEC        HEX      index

                                                                                                                             0 = Standard
 117        75       -             Display orientation           UInt        yes            8 bit    rw       0
                                                                                                                             1 = Upside down


If the installation position of the device makes it difficult to read from the segment display, the display can be
rotated by 180°.

7.2.4                 Disable sender light source
Table 11: General device settings – Sender light source
 ISDU
                                                                             Data reposi‐                     Default
 Index               Sub-          Name                          Data type                  Length   Access                  Value/range
                                                                             tory                             value
 DEC        HEX      index

                                                                                                                             0 = Sender active
 97         61       -             Disable sender light source   UInt        -              8 bit    rw       0
                                                                                                                             1 = Sender inactive


The sender LED can be switched off using this ISDU.

NOTICE
When the sender LED is switched off, the process data and switching output will not function.




8023268/2018-06-27 | SICK                                                                                          T E C H N I C A L I N F O R M A T I O N | PSS         13
Subject to change without notice

7 SERVICE DATA

7.2.5             Restore factory settings/reset
Table 12: General device settings – Restore factory settings
ISDU
                                                                          Data reposi‐                      Default
Index             Sub-        Name                            Data type                  Length    Access             Value/range
                                                                          tory                              value
DEC     HEX       index

                                                                                                                      128 = Device reset
2       02        -           Standard command                UInt        -              8 bit     ro
                                                                                                                      130 = Restore factory settings


Device reset                                              The sensor performs a restart.
Restore factory settings                                  The sensor is reset to factory settings.

7.2.6             (De)activate events
Table 13: General device settings – Notification handling
ISDU
                                                                          Data reposi‐                      Default
Index             Sub-        Name                            Data type                  Length    Access             Value/range
                                                                          tory                              value
DEC     HEX       index

                                                                                                                      0 = All enabled
227     E3        -           Notification handling           UInt        -              8 bit     rw       0
                                                                                                                      1 = All disabled


With this ISDU, you can switch off the generation of sensor IO-Link events.

7.3               Teach-in / detection settings

7.3.1             Configuration Q1 / inversion
Table 14: Teach-in/detection – Switchpoint
ISDU
                                                                          Data reposi‐                      Default
Index             Sub-        Name                            Data type                  Length    Access             Value/range
                                                                          tory                              value
DEC     HEX       index

                  -           Configuration Qint 1            Record                     4 bytes
                                                                                                                      0 = Q1 active on match
                  1           Switchpoint logic/inversion     Bit (0)                    8 bit              128
61      3D                                                                yes                      rw                 1 = Q1 active on mismatch

                  2           Switchpoint mode                Bit (8)                    8 bit              1         1 = single point mode
                  3           Switchpoint hysteresis          Bit (16)                   16 bit             0         0 = Vendor-specific default (not editable)


Switchpoint logic                      The switching output logic (inversion) can be configured so that the switching output is
                                       activated following successful detection of the pattern (positive detection) or so that it is
                                       activated when the pattern is not detected (negative detection). This inversion of the
                                       switching logic takes place upstream of the integrated timer module.
Switchpoint mode                       The switchpoint mode indicates the current work mode of the sensor. There is no option
                                       to edit this information.
Switchpoint hysteresis                 Switchpoint hysteresis is preset at the factory and cannot be changed.

7.3.2             Switching output inversion
Table 15: Smart Tasks – Inverter
ISDU
                                                                          Data reposi‐                      Default
Index             Sub-        Name                            Data type                  Length    Access             Value/range
                                                                          tory                              value
DEC     HEX       index

                                                                                                                      0 = Not inverted
1089    441       -           Inverter Q1                     UInt        yes            8 bytes   rw       0
                                                                                                                      1 = Inverted


Inverter for digital switching output. This inverter is positioned downstream of the timer.




14        T E C H N I C A L I N F O R M A T I O N | PSS                                                                               8023268/2018-06-27 | SICK
                                                                                                                                    Subject to change without notice

SERVICE DATA 7


7.3.3                    Switch-on and switch-off delay/impulse generator
Table 16: Teach-in/detection – Timer 1 mode
 ISDU
                                                                                          Data reposi‐                     Default
 Index                   Sub-          Name                               Data type                      Length   Access                  Value/range
                                                                                          tory                             value
 DEC          HEX        index

                                                                                                                                          0 = Inactive
                                                                                                                                          1 = ON delay
 1085         43D        -             Timer 1 mode                       UInt            yes            8 bit    rw       0              2 = OFF delay
                                                                                                                                          3 = ON&OFF delay
                                                                                                                                          4 = Impulse


The PSS has a switch-on and switch-off delay (Delay) and an impulse generator.
Impulse is set by default.
You can individually select the different delays using this ISDU.

Output delay


                                 12345


Trigger
Output delay
deactivated

Ton delay

Toff delay *

Ton + Toff delay *

Impulse
* Depending on the length and the speed, Toff delay can be used to ignore a few „ wrong prints“.

Figure 1: Ein- und Ausschaltverzögerung

NOTE
The selected delay affects the Q1 bit in the IO-Link process data.


NOTE
Dependency: You must set the duration of the selected delay in Timer 1 setup (ISDU 1087).

Table 17: Teach-in / detection – Timer 1 setup
 ISDU
                                                                                          Data reposi‐                     Default
 Index                   Sub-          Name                               Data type                      Length   Access                  Value/range
                                                                                          tory                             value
 DEC          HEX        index

 1087         43F        -             Timer 1 setup                      UInt            yes            16 bit   rw       10             1 … 30000


The duration of the delay function defined in Timer 1 mode (ISDU 1085) is specified here in ms (milliseconds).




8023268/2018-06-27 | SICK                                                                                                       T E C H N I C A L I N F O R M A T I O N | PSS   15
Subject to change without notice

7 SERVICE DATA

7.3.4            Trigger input delay
Table 18: Trigger input teach-in/delay
ISDU
                                                                     Data reposi‐                     Default
Index            Sub-        Name                        Data type                  Length   Access             Value/range
                                                                     tory                             value
DEC     HEX      index

                                                                                                                0 = deactivated
                                                                                                                1 = Ton delay
161              -           Ton timer mode              UInt        yes            8 bit    rw       0         2 = Toff delay
                                                                                                                3 = Ton + Toff delay
                                                                                                                4 = Ton delay + impulse
162                          Ton input delay             UInt        yes            16 bit   rw       1         1...30,000 [ms]
                             Toff input delay/impulse
163                                                      UInt        yes            16 bit   rw       1         1...30,000 [ms]
                             length


Trigger input delay


                                     12345

Trigger delay
deactivated




Ton delay

Toff delay

Ton + Toff delay

Ton delay + Impulse

Figure 2: Ein- und Ausschaltverzögerung

The trigger input delay option allows you to delay (Ton delay) or extend (Toff delay) the digital input signal, or to
generate a specific length (impulse) from this signal. The switch-on delay delays the incoming trigger signal by the
duration indicated in index 162 in milliseconds (trigger is delayed). The switch-off delay extends the trigger impulse
by the duration indicated in index 163 in milliseconds. The combination of switch-on delay and impulse generator
can be used to delay a trigger signal (duration in index 162 – can also be set to 0 ms) and to assign a defined
length to the signal (duration in index 163).

7.3.5            Teach-in
Table 19: Teach-in/detection – Teach command
ISDU
                                                                     Data reposi‐                     Default
Index            Sub-        Name                        Data type                  Length   Access             Value/range
                                                                     tory                             value
DEC     HEX      index

                                                                                                                71 = Start teach-in (background + print)
                                                                                                                73 = Start teach (print only)
                             Standard command –
2       02       -                                       UInt        -              8 bit    ro                 79 = Abort teach sequence
                             Teach command
                                                                                                                226 = Trigger window start
                                                                                                                227 = Trigger window stop




16       T E C H N I C A L I N F O R M A T I O N | PSS                                                                          8023268/2018-06-27 | SICK
                                                                                                                              Subject to change without notice

SERVICE DATA 7


Start teach-in                 When the value 71 is written to index 2, the teach-in process for the pattern to be detected
(background +                  begins. In this case, the background must be taught-in first, followed by the pattern to be
print)                         detected. For teach-in to begin, the PSS sensor must be triggered via the trigger input (pin 5) or
                               by writing the system commands “Trigger window start” and “Trigger window stop”. For details,
                               see diagram:




                                         1                  4
                               ET

                               Trigger

                                         2a 3 a 2b 3b
                               1 Start teach (background + print) with standard command 71.
                               2 Trigger window start with standard command 226 or trigger signal via pin 5.
                               3 Trigger window stop with standard command 227 or trigger signal via pin 5.
                               4 Teach-in ends automatically at the end of the second trigger window

Start teach (print             When the value 73 is written to index 2, the teach-in process for the pattern to be detected
only)                          begins. This teach-in process is only suitable for patterns with a homogeneous background, as
                               this process only teaches in the pattern and not the background. For teach-in to begin, the PSS
                               sensor must be triggered via the trigger input (pin 5) or by writing the system commands “Trig‐
                               ger window start” and “Trigger window stop”.
                               For details, see diagram:




                                                1           4
                               ET

                               Trigger

                                                    2     3
                               1 Start teach (print only) with standard command 73.
                               2 Trigger window start with standard command 226 or trigger signal via pin 5.
                               3 Trigger window stop with standard command 227 or trigger signal via pin 5.
                               4 Teach-in ends automatically at the end of the trigger window.

Abort teach-in                 Writing the value 79 aborts the ongoing teach-in process.
sequence



8023268/2018-06-27 | SICK                                                                     T E C H N I C A L I N F O R M A T I O N | PSS   17
Subject to change without notice

7 SERVICE DATA

7.3.6                      Teach-in status
Table 20: Teach-in/detection – Teach-in status
 ISDU
                                                                      Data reposi‐                                             Default
 Index                     Sub-       Name            Data type                        Length                       Access                   Value/range
                                                                      tory                                                     value
 DEC          HEX          index

                                                                                       8 bit                        ro         -             Bit no.
                                                                                                                                             7         6        5        4        3      2      1      0
                                                                                                                                             SP2 1)             SP1               Teach state
                                                                                                                                             TP2       TP1      TP2      TP1      2)


                                                                                                                                                                                  4 = Device is waiting for
                                                                                                                                                                                  background trigger win‐
                                      Teach-in sta‐                                                                                                                               dow
 59           3B           -                          UInt            -
                                      tus                                                                                                                                         5 = Device is recording
                                                                                                                                                                                  background
                                                                                                                                             0 = TP x failed                      7 = Teach error
                                                                                                                                             1 = TP x success                     52 = Device is waiting for
                                                                                                                                                                                  reference pattern window
                                                                                                                                                                                  53 = Device is recording
                                                                                                                                                                                  reference pattern
                                                                                                                                                                                  240 = Device is in run
                                                                                                                                                                                  mode

1)     SP = Switchpoint
2)     TP = Teach point

You can retrieve the current status of the teach-in process at any time via the teach-in status.
The interpretation of the status bytes can be taken from the table.

7.3.7                      Switching threshold position
Table 21: Teach-in/detection – Threshold settings
 ISDU
                                                                                       Data reposi‐                                          Default
 Index                     Sub-       Name                                Data type                       Length                   Access                    Value/range
                                                                                       tory                                                  value
 DEC          HEX          index

                           -          Threshold setting Qint 1            Record                          2 bytes
                                      Setpoint SP1 in % between
 60           3C           1                                              Bit (0)      -                                           rw        50              10 ... 90
                                      mark and background                                                 8 bit
                           2          Setpoint SP2 in %                   Bit (8)                                                                            not editable


In this ISDU, the switching threshold is described depending on the selected sensor mode.
The switching threshold of the PSS is indicated as a quality of print percentage (see "Q1 valid", page 10). If the
calculated quality of print exceeds the threshold, the output Q1 is activated.
If the ambient conditions are not ideal, e.g., in the event of:
–        Material variations
–        Variations in the exact pattern printing location on the background
–        Variations in printing intensity
–        Where changes to the pattern to be detected are not taught-in separately, we recommend setting the switch‐
         ing threshold significantly below 90%.
If the sensor is used for quality control, the interference factors listed above must be eliminated.

7.3.8                      Background evaluation
Table 22: Configuring the outputs
 ISDU                                                                       Data
                                                               Data         repo               Acce   Default
 Index             Sub-        Name                                                 Length                           Value/range
                                                               type         sitor              ss     value
 DEC     HEX       index                                                    y

                               Background teach evalua‐                                                              0 = Background teach disabled
 164     A4                                                    UInt         yes     16 bit     rw     0
                               tion                                                                                  1 = Background teach enabled


This ISDU can be used to switch background evaluation on or off.




18             T E C H N I C A L I N F O R M A T I O N | PSS                                                                                                                   8023268/2018-06-27 | SICK
                                                                                                                                                                             Subject to change without notice

SERVICE DATA 7


External teach-in              Background teach enabled Two trigger windows for (1.) Background and (2.) Patterns are nec‐
                                                         essary.
                               Background teach disabled Only one trigger window is necessary for the pattern.

Display                        Background teach enabled Teach-in of background and pattern possible via display.
                               Background teach disabled Only pattern teach-in possible.

Assessment                     Background teach enabled The available background pattern is evaluated (even if only one
                                                         pattern without a background has been taught-in previously. In
                                                         such cases, the most recently taught-in background pattern is
                                                         used).
                               Background teach disabled Only the taught-in pattern is evaluated (any previously taught-in
                                                         background pattern is ignored).

7.3.9                 Job assurance
Table 23: Teach-in/detection – Job assurance
 ISDU
                                                                      Data reposi‐                          Default
 Index               Sub-          Name                   Data type                  Length        Access                  Value/range
                                                                      tory                                  value
 DEC        HEX      index

 222        EN                     Job assurance Part 1
 223        DF                     Job assurance Part 2
                     -                                    Array       no             232 bytes     rw                      Unsigned Integer8 [232]
 224        EO                     Job assurance Part 3
 225        E1                     Job assurance Part 4


Parameter sets (jobs) make it possible to read out and save (in the PLC) specific application parameters (e.g.,
switching threshold) for certain applications, formats, or patterns so that you can use them flexibly later.
Compared to IO-Link Data Storage, only the application-specific data is saved.
In other words, a job can be duplicated from one sensor to another easily without the need to overwrite the local
sensor-related settings (e.g., configuration of the pins).
This means that you can quickly change the sensor parameters in the event of a format change or quickly install
the saved job data on a new device.
Furthermore, the teach-in values (such as measured value on mark, measured value on background) saved in the
job assurance can be used for visualization.

NOTE
To load and write job data, two standard commands (Execute Job Assurance (Restore), value 208 and Show Present Job
(Read Job), value 209) ) must be used.

Table 24: Job assurance teach data (ISDU 82dec)
                                           Byte offset     Length                Part            ISDU            Value range
 Version                                   0               2 bytes               1               222
 Background teach data                     4               12 bytes              1               222
 Teach pattern                             16              216 bytes             1               222
                                           0               232 bytes             2               223             Teach pattern consists of 696 bytes
                                                                                                                 in total
                                           0               232 bytes             3               224
                                           0               16 bytes              4               225
 Ton input delay                           20              2 bytes               4               225             1 to 30,000 ms
 Toff input delay/impulse                  22              2 bytes               4               225             1 to 30,000 ms
 Input timer mode                          24              1 byte                4               225             0 = deactivated
                                                                                                                 1 = Ton delay
                                                                                                                 2 = Toff delay
                                                                                                                 3 = Ton + Toff delay
                                                                                                                 4 = Ton delay + impulse



8023268/2018-06-27 | SICK                                                                                        T E C H N I C A L I N F O R M A T I O N | PSS   19
Subject to change without notice

7 SERVICE DATA

                                               Byte offset             Length                  Part                   ISDU                   Value range
Q1 setpoint SP1: sensitiv‐                     25                      1 byte                  4                      225                    10 to 90: Steps of 10 percent
ity
Q1 configuration: switch‐                      26                      1 byte                  4                      225                    0 = Q1 active on match
point logic                                                                                                                                  1 = Q1 active on mismatch
Q1 configuration: switch‐                      27                      1 byte                  4                      225                    1 = single point mode
point mode
Background teach                               28                      1 byte                  4                      225                    0 = background teach disabled
enabled                                                                                                                                      1 = background teach enabled

Table 25: Teach-in/detection – Job assurance
ISDU
                                                                                  Data reposi‐                                          Default
Index                     Sub-       Name                             Data type                      Length                 Access                 Value/range
                                                                                  tory                                                  value
DEC          HEX          index

                                     Standard command – Job                                                                                        208 = Execute job assurance (restore)
2            02           -                                           UInt        -                  8 bit                  ro
                                     assurance                                                                                                     209 = Show present job (read out)


Execute job assurance                     After a new job is written to job assurance (ISDUs 222 to 225 – a job is always comprised of
                                          all four ISDUs), it must be activated via the system command Execute job assurance. Without
                                          activation, the loaded job will not be adopted.
Show present job (read                    To ensure that the job data in Job assurance (ISDUs 222 to 225) contains up-to-date, consis‐
job)                                      tent values, this system command must be executed before reading the job data. The sen‐
                                          sor then provides the data in ISDU 222-225. To read out an entire PSS job, all four ISDUs
                                          222 to 225 must be read out and saved.

7.3.10                    Reference pattern
Table 26: System-specific ISDUs – Reference pattern
ISDU
                                                                                  Data reposi‐                                          Default
Index                     Sub-       Name                             Data type                      Length                 Access                 Value/range
                                                                                  tory                                                  value
DEC          HEX          index

82           52                      Reference pattern – Part 1
83           53                      Reference pattern – Part 2
84           54           -          Reference pattern – Part 3       Array       yes                232 bytes              rw                     Unsigned Integer32 [58]

                                     Background pattern and
85           55
                                     teach meta data


In these ISDUs, the information collected during the teach-in (e.g., the recorded contrast pattern) is saved. These
ISDUs exist solely for the purposes of the IO-Link data storage mechanism. It can also be used to visualize the
reference pattern. You can also find the same information in job assurance (ISDUs 222 to 225). For recipe man‐
agement, we recommend using ISDUs 222 to 225.

NOTE
The reference pattern is part of Job assurance. This ISDU is only relevant for data maintenance and visualization.
The exact breakdown of the arrays can be found in the Job assurance chapter.


7.3.11                    Last read pattern
Table 27: System-specific ISDUs – Reference pattern
ISDU                                                                   Data
                                                              Data     repo             Acce     Default
Index             Sub-        Name                                             Length                         Value/range
                                                              type     sitor            ss       value
DEC     HEX       index                                                y

165     A5        -           Last print pattern – Part 1              yes                       0
                                                                               232 by
166     A6        -           Last print pattern – Part 2     Array                     ro                    Unsigned Integer32 [58]
                                                                               tes
167     A7        -           Last print pattern – Part 3




20            T E C H N I C A L I N F O R M A T I O N | PSS                                                                                                        8023268/2018-06-27 | SICK
                                                                                                                                                                 Subject to change without notice

SERVICE DATA 7


ISDUs 165 to 167 can be used to read out the last patten read by the sensor. This is particularly helpful for visual‐
ization and diagnostics purposes. As the process, and therefore the reading sequence of the sensor, is often faster
than the read-out process via IO-Link, the pattern must always be read out following the ascending sequence of
the ISDUs (165 before 166 and then 167). If the pattern is read out in this sequence, the PSS ensures that the
data is consistent and that it comes from the same reading sequence.

7.4                   Installation / Diagnostics

7.4.1                 Device state
Table 28: Installation/diagnostics – Device status
 ISDU
                                                                     Data reposi‐                     Default
 Index               Sub-          Name                  Data type                  Length   Access                  Value/range
                                                                     tory                             value
 DEC        HEX      index

                                                                                                                     0 = Device is OK
                                                                                                                     1 = Maintenance required
                                                                                                                     2 = Out of specification
 36         24       -             Device status         UInt        -              8 bit    ro       -
                                                                                                                     3 = Functional check
                                                                                                                     4 = Failure
                                                                                                                     5 to 255 = Reserved



7.4.2                 Device temperature
Table 29: Installation / Diagnostics – Temperature
 ISDU
                                                                     Data reposi‐                     Default
 Index               Sub-          Name                  Data type                  Length   Access                  Value/range
                                                                     tory                             value
 DEC        HEX      index

 153        99       -             Temperature           Int         -              16 bit   ro                      Internal device temperature in °


Read out the operating temperature of the sensor.

7.4.3                 Teach-in quality
Table 30: Installation/diagnostics – Quality of teach-in
 ISDU
                                                                     Data reposi‐                     Default
 Index               Sub-          Name                  Data type                  Length   Access                  Value/range
                                                                     tory                             value
 DEC        HEX      index

 114        72       -             Quality of teach-in   UInt        -              8 bit    ro                      0 … 100 = Quality level in %


Quality of teach-in contains the teach-in quality of the taught-in material.
Values:
•        ERR < 10: low information content in printed image
•        50: adequate information content for printed image
•        100: optimum information content for printed image
The PSS also reliably detects printed images with sufficient information content.

NOTE
Recommendation:
In the event of poor teach-in quality, avoid external influences such as contamination or significant material varia‐
tion. In such cases, we also recommend that the system is used only for presence monitoring and not for quality
tests.




8023268/2018-06-27 | SICK                                                                                  T E C H N I C A L I N F O R M A T I O N | PSS   21
Subject to change without notice

7 SERVICE DATA

7.5                  System-specific ISDUs

7.5.1                Teach-in channel
Table 31: System-specific ISDUs – Teach-in channel
 ISDU
                                                                         Data reposi‐                     Default
 Index               Sub-        Name                        Data type                  Length   Access             Value/range
                                                                         tory                             value
 DEC        HEX      index

 58         3A       -           Teach-in channel            UInt        yes            8 bit    rw       0         0 = Qint 1


The PSS only has one teach-in channel for the teach-in process. Only the preset teach-in channel can be used.

7.5.2                Process data as ISDU
Table 32: System-specific ISDUs – Process data input
 ISDU
                                                                         Data reposi‐                     Default
 Index               Sub-        Name                        Data type                  Length   Access             Value/range
                                                                         tory                             value
 DEC        HEX      index

 40         28       -           Process data input 1)       PD in       yes            2 byte   ro

1)     Refers to process data

In this ISDU, the current process data is provided as an ISDU. For more information: see "Process data".




22           T E C H N I C A L I N F O R M A T I O N | PSS                                                                          8023268/2018-06-27 | SICK
                                                                                                                                  Subject to change without notice

EVENTS 8


8                     Events
IO-Link communication is a master-slave communication system.
With “Events”, an IO-Link device reports events to the master (without being prompted by the master). Device-spe‐
cific events are classified as follows:
Table 33: Device-specific events
 Notification                              For information purposes only; system is not restricted.
 Warning                                   System is still functional, but is impaired in some way. You must rectify this with suitable mea‐
                                           sures as soon as possible.
 Error                                     System is no longer functional. Depending on the cause of the error, it may be possible to
                                           restore functionality.

An event issues an event code, which contains the cause of the occurrence of the event.

NOTE
Not all IO-Link masters support the event mechanism.
You can deactivate the generation of events on the device side in ISDU 227 Notification handling.

The following events are supported:

NOTE
Not all IO-Link masters support the event mechanism.
You can deactivate the generation of events on the device side in ISDU 227 Notification handling.

Table 34: Events
 Code                          Name                  Type         Comment                              Action
 Dec            Hex
 6144           1800           Teach-in failure      Error        Triggered after a failed teach-in.   Realign the PSS and perform a new
                                                                  The contrast was too low during      teach-in.
                                                                  teach-in.
 6145           1801           Teach-in back‐    Notification     Triggered after a successful         No action required.
                               ground successful                  teach-in.
 6146           1802           Teach-in print suc‐ Notification   Triggered after a successful         No action required.
                               cessful                            teach-in.
 6147           1803           Hardware error        Error        Sensor is defective.                 Replace the sensor.
 16912          4210           Device tempera‐       Warning      Triggered if the critical tempera‐   Check the sensor environment and
                               ture over-run                      ture is exceeded in the device.      remove the heat source.
 3600           8CA0           Output is shortcir‐   Warning      Triggered in the event of a short-   Check the cabling.
                               cuited                             circuit on at least one switching
                                                                  output.
                                                                  Overcurrent detection.




8023268/2018-06-27 | SICK                                                                              T E C H N I C A L I N F O R M A T I O N | PSS   23
Subject to change without notice

9 USE CASES


9                Use cases
9.1              Configuring job assurance
Store a job from sensor in PLC




Figure 3: Store a job from sensor in PLC

Job 1 = Text field on yellow background
Job 2 = Text field on green background
1a and 1b text field teach-in = Perform teach-in as described in operating instructions
2 Preparation: Write value 209 to index 2
3 Read out job and save in PLC, read indexes 222 to 225 and save in PLC




24       T E C H N I C A L I N F O R M A T I O N | PSS                                      8023268/2018-06-27 | SICK
                                                                                          Subject to change without notice

USE CASES 9


Write job to sensor




Figure 4: Write job to sensor

1 Format change
2 Write new job from database to sensor: Write the selected job to indexes 222 to 225
3 Activation: Write value 208 to index 2 to activate the job.
4 End




8023268/2018-06-27 | SICK                                                      T E C H N I C A L I N F O R M A T I O N | PSS   25
Subject to change without notice

9 USE CASES

9.2              Teach-in via IO-Link
Teach-in – Teach-in background & printed image
For a non-homogeneous background, we recommend teaching in the background during the teach-in process to
improve the detection results.




Figure 5: Application example – Teach-in – Background & printed image

1 Start teach-in process. Write 71 to index 2
2 Query teach-in status. Read index 59 4 = wait for background teach-in
3 Start background teach-in. Write 226 to index 2
4 Query teach-in status. Read index 59 5 = teach-in background
5 End teach-in background. Write 227 to index 2
6 Query teach-in status. Read index 59 52 = wait for text field
7 Start text field teach-in. Write 79 to index 2
8 Query teach-in status. Read index 59 53 = teach-in text field
9 Complete teach-in. Write 227 to index 2
ß Query teach-in status. Read index 59 240 = in run mode
à Query teach quality. Read index 114 100 = best teach-in quality
End

26       T E C H N I C A L I N F O R M A T I O N | PSS                                    8023268/2018-06-27 | SICK
                                                                                        Subject to change without notice

USE CASES 9


9.3                   Teach-in via IO-Link
Teach-in – Teach-in printed image only without background
For a consistent, homogeneous background, the background does not need to be included in the teach-in process.
A shortened form of the teach-in process can be executed.




Figure 6: Anwendungsbeispiel – Teach-in – nur Druckbild

1 Start teach-in process. Write 73 to index 2
2 Query teach-in status. Read index 59 52 = wait for text field
3 Start text field teach-in. Write 79 to index 2
4 Query teach-in status. Read index 59 53 = teach-in text field
5 Complete teach-in. Write 227 to index 2
6 Query teach-in status. Read index 59 240 = in run mode
7 Query teach quality. Read index 114 100 = best teach-in quality
End




8023268/2018-06-27 | SICK                                                    T E C H N I C A L I N F O R M A T I O N | PSS   27
Subject to change without notice

9 USE CASES

9.4              Control reading window via IO-Link
Control the reading window via the IO-Link rather than the trigger input
The PSS must be controlled via a reading window when detecting the printed image. This can be executed using
the trigger input or via IO-Link commands.




Figure 7: Application example – Reading window via IO-Link

1 Start trigger window
2 End trigger window
3 Read out process data




28       T E C H N I C A L I N F O R M A T I O N | PSS                                        8023268/2018-06-27 | SICK
                                                                                            Subject to change without notice

LIST OF ABBREVIATIONS 10


10                    List of abbreviations
Table 35: List of abbreviations
 IODD              IO Device Description           Device description file of an IO-Link device
 ISDU              Indexed Service Data Unit       Service data object in IO-Link
                                                   1 = 4.8 kbit/s
 COM 1 – 3 SDCI communication mode                 2 = 38.4 kbit/s
                                                   3 = 230.4 kbit/s
 SDCI              Single-drop digital interface   Official (specification) name for IO-Link technology
 SDD               SOPAS ET Device Description     Device description file / driver for SICK SOPAS ET software




8023268/2018-06-27 | SICK                                                           T E C H N I C A L I N F O R M A T I O N | PSS   29
Subject to change without notice

11 INDEX


11                     Index
I
ISDE
   0017 Vendor text.......................................................................... 11
ISDU
   0002 Job assurance..................................................................... 20
   0002 Standard command (Restore)........................................... 14
   0002 Standard command (teach command)............................. 16
   0012 Device access locks (key lock).......................................... 13
   0016 Vendor name...................................................................... 11
   0018 Product name..................................................................... 11
   0019 Product ID........................................................................... 11
   0020 Product text......................................................................... 11
   0021 Serial number..................................................................... 11
   0022 Hardware version................................................................ 12
   0023 Firmware version................................................................ 12
   0024 Application-specific tag...................................................... 11
   0036 Device status...................................................................... 21
   0040 Process data input............................................................. 22
   0058 SICK profile version............................................................ 22
   0059 Teach-in status.................................................................... 18
   0060 Setpoint SP1 in % between mark and background.......... 18
   0061 Switchpoint......................................................................... 14
   0064Device-specific name.......................................................... 11
   0082 Reference pattern – Part 1................................................ 20
   0083 Reference pattern – Part 2................................................ 20
   0084 Reference pattern – Part 3................................................ 20
   0085 Background pattern and teach meta data....................... 20
   0097 Disable sender light source............................................... 13
   0114 Quality of teach-in............................................................... 21
   0117 Display orientation.............................................................. 13
   0121 Pin2 configuration.............................................................. 12
   0153 Temperature........................................................................ 21
   0161 Ton timer mode................................................................... 16
   0162 Ton input delay.................................................................... 16
   0163 Toff input delay/impulse length......................................... 16
   0164 Background teach evaluation............................................ 18
   0165 Last print pattern – Part 1................................................. 20
   0166 Last print pattern – Part 2................................................. 20
   0167 Last print pattern – Part 3................................................. 20
   0204 Find me............................................................................... 12
   0219 Product ID........................................................................... 11
   0222 Job assurance Part 1......................................................... 19
   0223 Job assurance Part 2......................................................... 19
   0224 Job assurance Part 3......................................................... 19
   0225 Job assurance Part 4......................................................... 19
   0227 Notification handling.......................................................... 14
   1085 Timer 1 mode..................................................................... 15
   1087 Timer 1 setup...................................................................... 15
   1089 Inverter 1 (Smart Tasks 00)............................................... 14
   16912 Device temperature over-run........................................... 23
   3600 Output is shortcircuited...................................................... 23
   6144 Teach-in failure................................................................... 23
   6145 Teach-in background successful....................................... 23
   6146 Teach-in print successful................................................... 23
   6147 Hardware error.................................................................... 23




30             T E C H N I C A L I N F O R M A T I O N | PSS                                          8023268/2018-06-27 | SICK
                                                                                                    Subject to change without notice

INDEX 11




8023268/2018-06-27 | SICK          T E C H N I C A L I N F O R M A T I O N | PSS   31
Subject to change without notice

8023268/2018-06-27/en
                        Australia                         Israel                             South Korea
                        Phone +61 3 9457 0600             Phone +972 4 6881000               Phone +82 2 786 6321
                               1800 334 802 – tollfree    E-Mail info@sick-sensors.com       E-Mail info@sickkorea.net
                        E-Mail sales@sick.com.au          Italy                              Spain
                        Austria                           Phone +39 02 274341                Phone +34 93 480 31 00
                        Phone +43 22 36 62 28 8-0         E-Mail info@sick.it                E-Mail info@sick.es
                        E-Mail office@sick.at             Japan                              Sweden
                        Belgium/Luxembourg                Phone +81 3 5309 2112              Phone +46 10 110 10 00
                        Phone +32 2 466 55 66             E-Mail support@sick.jp             E-Mail info@sick.se
                        E-Mail info@sick.be               Malaysia                           Switzerland
                        Brazil                            Phone +6 03 8080 7425              Phone +41 41 619 29 39
                        Phone +55 11 3215-4900            E-Mail enquiry.my@sick.com         E-Mail contact@sick.ch
                        E-Mail marketing@sick.com.br      Mexico                             Taiwan
                        Canada                            Phone +52 (472) 748 9451           Phone +886 2 2375-6288
                        Phone +1 905 771 14 44            E-Mail mario.garcia@sick.com       E-Mail sales@sick.com.tw
                        E-Mail information@sick.com       Netherlands                        Thailand
                        Czech Republic                    Phone +31 30 2044 000              Phone +66 2645 0009
                        Phone +420 2 57 91 18 50          E-Mail info@sick.nl                E-Mail Ronnie.Lim@sick.com
                        E-Mail sick@sick.cz               New Zealand                        Turkey
                        Chile                             Phone +64 9 415 0459               Phone +90 216 528 50 00
                        Phone +56 2 2274 7430                    0800 222 278 – tollfree     E-Mail info@sick.com.tr
                        E-Mail info@schadler.com          E-Mail sales@sick.co.nz            United Arab Emirates
                        China                             Norway                             Phone +971 4 88 65 878
                        Phone +86 20 2882 3600            Phone +47 67 81 50 00              E-Mail info@sick.ae
                        E-Mail info.china@sick.net.cn     E-Mail sick@sick.no                United Kingdom
                        Denmark                           Poland                             Phone +44 1727 831121
                        Phone +45 45 82 64 00             Phone +48 22 539 41 00             E-Mail info@sick.co.uk
                        E-Mail sick@sick.dk               E-Mail info@sick.pl                USA
                        Finland                           Romania                            Phone +1 800 325 7425
                        Phone +358-9-2515 800             Phone +40 356 171 120              E-Mail info@sick.com
                        E-Mail sick@sick.fi               E-Mail office@sick.ro              Vietnam
                        France                            Russia                             Phone +84 945452999
                        Phone +33 1 64 62 35 00           Phone +7 495 775 05 30             E-Mail Ngo.Duy.Linh@sick.com
                        E-Mail info@sick.fr               E-Mail info@sick.ru
                        Germany                           Singapore
                        Phone +49 211 5301-301            Phone +65 6744 3732
                        E-Mail info@sick.de               E-Mail sales.gsg@sick.com
                        Hong Kong                         Slovakia
                        Phone +852 2153 6300              Phone +421 482 901201
                        E-Mail ghk@sick.com.hk            E-Mail mail@sick-sk.sk
                        Hungary                           Slovenia
                        Phone +36 1 371 2680              Phone +386 591 788 49
                        E-Mail office@sick.hu             E-Mail office@sick.si
                        India                             South Africa
                        Phone +91 22 6119 8900            Phone +27 11 472 3733
                        E-Mail info@sick-india.com        E-Mail info@sickautomation.co.za   Further locations at www.sick.com




                        SICK AG | Waldkirch | Germany | www.sick.com