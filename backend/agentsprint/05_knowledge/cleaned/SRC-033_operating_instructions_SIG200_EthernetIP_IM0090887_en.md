OPERATING INSTRUCTION


Sensor Integration Gateway - SIG200
EtherNet/IPTM(R)

Integration Products

Described product
                                   SIG - Sensor integration gateway
                                   SIG200 EtherNet/IP

                                   Manufacturer
                                   SICK AG
                                   Erwin-Sick-Str. 1
                                   79183 Waldkirch
                                   Germany

                                   Production location
                                   SICK PCA
                                   55438 Minneapolis, MN
                                   USA

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

                                                                                     NO

                                                                                2006/42/EC
                                                                                    SAFETY




2   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                     8016629.1MCE/2024-10-24 | SICK
                                                                                                         Subject to change without notice

CONTENTS


Contents
                                   1    About this document........................................................................                              5
                                        1.1      Information on the operating instructions..............................................                          5
                                        1.2      Further information...................................................................................           5
                                        1.3      Symbols and document conventions......................................................                           5

                                   2    Safety information............................................................................                           7
                                        2.1      General safety notes................................................................................            7
                                        2.2      Correct use................................................................................................     7
                                        2.3      Notes on UL approval...............................................................................             7
                                        2.4      Qualification of personnel........................................................................              7

                                   3    Product description...........................................................................                           8
                                        3.1      Product identification via the SICK product ID.......................................                            8
                                        3.2      Product description..................................................................................            8
                                        3.3      Operating and status indicators..............................................................                    9

                                   4    Transport and storage....................................................................... 11
                                        4.1      Transport...................................................................................................    11
                                        4.2      Transport inspection.................................................................................           11
                                        4.3      Storage......................................................................................................   11

                                   5    Mounting............................................................................................. 12

                                   6    Electrical installation........................................................................ 13
                                        6.1      Pin alignment............................................................................................       13

                                   7    SIG200 configuration....................................................................... 15
                                        7.1      SIG200 EtherNet/IP interface.................................................................                   15
                                        7.2      Operation via Webserver..........................................................................               33
                                        7.3      Operation via SOPAS ET (USB/Ethernet).................................................                          34
                                        7.4      Configuration via REST API.......................................................................               51

                                   8    Device Functions............................................................................... 93
                                        8.1      Data Storage.............................................................................................       93
                                        8.2      Logic Editor................................................................................................    93

                                   9    Troubleshooting................................................................................. 113

                                   10   Disassembly and disposal............................................................... 114

                                   11   Maintenance...................................................................................... 115

                                   12   Technical data.................................................................................... 116
                                        12.1 General technical data............................................................................. 116

                                   13   Annex.................................................................................................. 119

8016629.1MCE/2024-10-24 | SICK                                                   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200    3
Subject to change without notice

CONTENTS


                                                13.1 Conformities and certificates................................................................... 119




4    O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                          8016629.1MCE/2024-10-24 | SICK
                                                                                                                               Subject to change without notice

ABOUT THIS DOCUMENT 1


1                  About this document
1.1                Information on the operating instructions
                                   Read these operating instructions carefully before starting any work in order to familiar‐
                                   ize yourself with the product and its functions.
                                   The operating instructions are an integral part of the product and should remain acces‐
                                   sible to the personnel at all times. When handing this product over to a third party,
                                   include these operating instructions.
                                   These operating instructions do not provide information on the handling and safe
                                   operation of the machine or system in which the product is integrated. Information on
                                   this can be found in the operating instructions for the machine or system.

1.2                Further information
                                   You can find the product page with further information via the SICK Product ID:
                                   pid.sick.com/{P/N}/{S/N}
                                   (see "Product identification via the SICK product ID", page 8).
                                   The following information is available depending on the product:
                                   • This document in all available language versions
                                   • Data sheets
                                   • Other publications
                                   • CAD files and dimensional drawings
                                   • Certificates (e.g., declaration of conformity)
                                   • Software
                                   • Accessories

1.3                Symbols and document conventions
                                   Warnings and other notes

                                   DANGER
                                   Indicates a situation presenting imminent danger, which will lead to death or serious
                                   injuries if not prevented.


                                   WARNING
                                   Indicates a situation presenting possible danger, which may lead to death or serious
                                   injuries if not prevented.


                                   CAUTION
                                   Indicates a situation presenting possible danger, which may lead to moderate or minor
                                   injuries if not prevented.


                                   NOTICE
                                   Indicates a situation presenting possible danger, which may lead to property damage if
                                   not prevented.


                                   NOTE
                                   Highlights useful tips and recommendations as well as information for efficient and
                                   trouble-free operation.




8016629.1MCE/2024-10-24 | SICK                                        O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   5
Subject to change without notice

1 ABOUT THIS DOCUMENT

                                    Instructions to action
                                    ►        The arrow denotes instructions to action.
                                    1.       The sequence of instructions is numbered.
                                    2.       Follow the order in which the numbered instructions are given.
                                    ✓        The tick denotes the results of an action.




6    O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                       8016629.1MCE/2024-10-24 | SICK
                                                                                                            Subject to change without notice

SAFETY INFORMATION 2


2                  Safety information
2.1                General safety notes

2.1.1              Safety notes
                                   ■    Read the operating instructions before commissioning.
                                   ■    Connection, mounting, and setting may only be performed by trained specialists.
                                   ■    Not a safety component in accordance with the EU Machinery Directive.
                                   ■    When commissioning, protect the device from moisture and contamination.
                                   ■    These operating instructions contain information required during the life cycle of
                                        the gateway.

                                   CAUTION
                                   This equipment is not intended for use in residential environments and may not provide
                                   adequate protection to radio reception in such environments.


2.2                Correct use
                                   The SIG200 (hereinafter referred to as "module") is an IO-Link master for connecting
                                   IO-Link devices and standard input signals or output signals.
                                   Intended use requires that the device is used industrially indoors without any spe‐
                                   cific climatic and atmospheric requirements. Operation of the device according to its
                                   intended use and enclosure rating IP 67 are only guaranteed if open male and female
                                   connectors are sealed with blind plugs.
                                   If the product is used for any other purpose or modified in any way, all warranty claims
                                   against SICK AG will be void.

2.3                Notes on UL approval
                                   UL Environmental Rating: Enclosure type 1

2.4                Qualification of personnel
                                   Any work on the product may only be carried out by personnel qualified and authorized
                                   to do so.
                                   Qualified personnel are able to perform tasks assigned to them and can independently
                                   recognize and avoid any potential hazards. This requires, for example:
                                   •    technical training
                                   •    experience
                                   •    knowledge of the applicable regulations and standards




8016629.1MCE/2024-10-24 | SICK                                        O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   7
Subject to change without notice

3 PRODUCT DESCRIPTION


3             Product description
3.1           Product identification via the SICK product ID
                                     SICK product ID
                                     The SICK product ID uniquely identifies the product. It also serves as the address of the
                                     web page with information on the product.
                                     The SICK product ID comprises the host name pid.sick.com, the part number (P/N),
                                     and the serial number (S/N), each separated by a forward slash.
                                     For many products, the SICK product ID is displayed as text and QR code on the type
                                     label and/or on the packaging.




                                     Figure 1: SICK product ID


3.2           Product description
                                     The SIG200 IO-Link master is an intelligent gateway for connecting IO-Link devices
                                     and input and/or output signals for signal integration into a PLC via EtherNet/IP or
                                     into a network via the REST API. It is intended for use in industrial environments that
                                     require enclosure rating up to IP67. There are four IO-Link channels, each of which is
                                     connected to its own M12 female connector of connection type A.
                                     In addition, the SIG200 has a powerful user interface that can be accessed either via
                                     USB using the SOPAS ET software from SICK or via Ethernet and any web browser. With
                                     the integrated IODD interpreter, the SIG200 and the connected IO-Link devices can be
                                     parameterized using the IODD file(s). The user interface also has a logic editor that can
                                     be used to parameterize sensor/actuator systems based on the information provided.




8     O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                     8016629.1MCE/2024-10-24 | SICK
                                                                                                           Subject to change without notice

PRODUCT DESCRIPTION 3


3.3                Operating and status indicators
                                   ß                                                            à


                                                    POWER         CONFIG   â
                                       POWER                                        POWER
                                           MS
                                                                           1            MS
                                           NS                                            NS
                                   9                        SIG200
                                                                           á
                                          /DO               S1                     C/DI/DO
                                            DI
                                                                           2              DI
                                   8
                                          /DO                                      C/DI/DO
                                                            S2
                                            DI                                            DI
                                                                           3
                                          /DO                                      C/DI/DO
                                                            S3
                                            DI                                            DI

                                                                           4
                                          /DO                                      C/DI/DO
                                                            S4
                                            DI                                            DI

                                                                           5
                                          LINK                                        LINK
                                          ACT2
                                                            P2                        ACT2
                                                                           6
                                          LINK                                        LINK
                                          ACT1
                                                            P1                        ACT1
                                                                           7



                                   Figure 2: Dimensional drawing


                                   1       POWER IN
                                   2       IO-Link Port S1
                                   3       IO-Link Port S2
                                   4       IO-Link Port S3
                                   5       IO-Link Port S4
                                   6       Ethernet Port P2
                                   7       Ethernet Port P1
                                   8       DI: LED for pin 2
                                   9       C/DI/DO LED for pin 4
                                   ß       Mounting hole for front mounting
                                   à       Mounting hole for side mounting
                                   á       Removable user defined port labels
                                   â       USB Port (M8) for configuration with SOPAS ET

                                   LEDs on the fieldbus module


                                                                                                       LINK
                                                                                                       ACT2
                                                                                                                         P2
                                                 POWER      CONFIG

                                   1
                                   2 MS                                                                LINK
                                                                                                                         P1
                                                                                                       ACT1
                                   3 NS                  SIG200




8016629.1MCE/2024-10-24 | SICK                                                 O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   9
Subject to change without notice

3 PRODUCT DESCRIPTION

                                    Table 1: LED status indicators
                                     LED                    Display                           Meaning
                                     Supply volt‐           green                    O        Power on
                                     age
                                                            Off                      o        Power off
                                                            Flashing                 Ö        A serious error has occurred. Please contact your SICK
                                                            green                             service partner.
                                     MS (Module             dark                     o        The module has no power
                                     status)
                                                            red / green              alter‐   Self-test when switching on
                                                                                     nately
                                                                                     Ö
                                                            green                    O        Device in operation
                                                            green blink‐             Ö        Device in standby, no IP address assigned
                                                            ing
                                                            red                      O        Error (device not in operation)
                                                            red blinking             Ö        Warning (but device in operation)
                                     NS (Network dark                                o        No voltage or IP address
                                     status)
                                                 red / green                         alter‐   Self-test when switching on
                                                                                     nately
                                                                                     Ö
                                                            green                    O        Valid IP address and CIP connection
                                                            green blink‐             Ö        Valid IP address, no connection
                                                            ing
                                                            red                      O        IP address assigned to a different device
                                                            red blinking             Ö        Connection timeout
                                     LINK ACT 1 dark                                 o        No network connection on port 1
                                     (Link / Activ‐
                                                    green                            O        Network connection on port 1
                                     ity 1)
                                     LINK ACT 2 dark                                 o        No network connection on port 2
                                     (Link / Activ‐
                                                    green                            O        Network connection on port 2
                                     ity 2)

                                    IO-Link Port LEDs (Port S1-S4)

                                    9                          SIG200
                                             /DO               S1
                                               DI

                                    8

                                     Legend                                LED                            Indication              Meaning
                                     8                                     DI: LED for pin 2              amber                   Additional DI on pin 2
                                                                                                          Off                     No additional DI on
                                                                                                                                  pin 2
                                     9                                     C/DI/DO LED for pin 4 green                            Pin 4 - IO-Link commu‐
                                                                                                                                  nication active
                                                                                                          green blinking          Pin 4 - no IO-Link com‐
                                                                                                                                  munication active




10   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                              8016629.1MCE/2024-10-24 | SICK
                                                                                                                                   Subject to change without notice

TRANSPORT AND STORAGE 4


4                  Transport and storage
4.1                Transport
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


4.2                Transport inspection
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


4.3                Storage
                                   Store the device under the following conditions:
                                   ■    Recommendation: Use the original packaging.
                                   ■    Do not store outdoors.
                                   ■    Store in a dry area that is protected from dust.
                                   ■    So that any residual damp can evaporate, do not package in airtight containers.
                                   ■    Do not expose to any aggressive substances.
                                   ■    Protect from sunlight.
                                   ■    Avoid mechanical shocks.
                                   ■    Storage temperature: see "Technical data", page 116.
                                   ■    Relative humidity: see "Technical data", page 116.
                                   ■    For storage periods of longer than 3 months, check the general condition of all
                                        components and packaging on a regular basis.




8016629.1MCE/2024-10-24 | SICK                                       O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   11
Subject to change without notice

5 MOUNTING


5            Mounting
                                    The SIG200 is mounted with two screws, maximum M6, and two flat washers.
                                    Observe the maximum permissible tightening torque of 0.8 Nm.


                                                     2 x M6
                                                     < 0.8 Nm




                                    Figure 3: Mounting

                                    Scope of delivery:
                                     •       SIG200
                                     •       5 blind plugs (on Port CONFIG, S2, S3, S4, P1)
                                     •       Quickstart instruction
                                     •       20 labels for the label pocket
                                    To ensure proper ground connection to the housing, the coating on the housing around
                                    the mounting screws must be removed.

                                    NOTE
                                    There can be several SIG200 mounted side by side without observing a minimum
                                    distance between each IO-Link Master.


                                    NOTE
                                    There are no blind plugs at ports P1, S1 and Power.


                                    NOTE
                                    There are no screws inlcuded in the scope of delivery.




12   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                 8016629.1MCE/2024-10-24 | SICK
                                                                                                      Subject to change without notice

ELECTRICAL INSTALLATION 6


6                  Electrical installation
                                   The SIG200 power and IO-Link cables must be connected in a voltage-free state (UV =
                                   0 V). The following information must be observed, depending on the connection type:
                                   Even if the wiring is looped through, the total current of the module must not exceed
                                   3 A.

                                   NOTICE DAMAGE OF EQUIPMENT
                                   Equipment damage due to incorrect supply voltage! Please note the instructions for
                                   electrical installation.

                                   An incorrect supply voltage may result in damage to the equipment. Operation in
                                   short-circuit protected network max. 8 A is allowed.
                                   Only apply voltage/switch on the voltage supply (UV > 0 V) once all electrical connec‐
                                   tions have been established.
                                   Male and female connectors that are not used must be sealed with blind caps so that
                                   the enclosure rating of IP 67 is assured.
                                   Explanation of the connection diagrams:
                                   DI = Digital input
                                   DO = Digital output
                                   FE = functional ground
                                   IO-Link = IO-Link communication (C)
                                   n. c. = not connected
                                   Rx+ = Receiver +
                                   Rx- = Receiver -
                                   Tx+ = Transmitter +
                                   Tx- = Transmitter +

6.1                Pin alignment
                                   UB: 10 ... 30 V DC
                                   Table 2: Power port, M12 A-coded
                                                Pin                             Signal                                           Description
                                                 1                               + (L+)                                     +24 V DC nominal
                                                 2                                n.c.                                         Not connected
                                                 3                                  M                                                   0V
                                                 4                                n.c.                                         Not connected
                                                                        2                         1



                                                                        3                         4
                                                                               IN = 3 A

                                   Table 3: USB port (for configuration), M8
                                                Pin                             Signal                                           Description
                                                 1                               + (L+)                                      + 5 V DC nominal
                                                 2                               - Data


8016629.1MCE/2024-10-24 | SICK                                           O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   13
Subject to change without notice

6 ELECTRICAL INSTALLATION

                                                         Pin                              Signal                   Description
                                                          3                               + Data
                                                          4                                  M                 0 V (logic ground)
                                                                                      1              3



                                                                                      2              4

                                     Table 4: USB port (for configuration), M8
                                                         Pin                              Signal                   Description
                                                          1                                + (L+)              + 5 V DC nominal
                                                          2                                - Data
                                                          3                               + Data
                                                          4                                  M                 0 V (logic ground)
                                                                                      1              3



                                                                                      2              4

                                     Table 5: Ethernet/IP Port (P1/P2), M12 D-coded
                                                         Pin                              Signal                   Description
                                                          1                                 Tx+                      Sender +
                                                          2                                 Rx+                     Receiver +
                                                          3                                 Tx-                      Sender -
                                                          4                                 Rx-                     Receiver -
                                                                                      1              2



                                                                                      4              3

                                     Table 6: IO-Link ports (S1-S4) M12, A-coded, (port class A)
                                                         Pin                              Signal                   Description
                                                          1                                + (L+)              +24 V DC nominal
                                                          2                                 DI            Configurable as Digital Input
                                                          3                                  M                 0 V (logic ground)
                                                          4                           DI/DO or IO-Link   Configurable as Digital Input or
                                                                                                            Digital Output or IO-Link
                                                          5                                n. c.
                                                                                      1              2

                                                                                      5

                                                                                      4              3




14    O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                              8016629.1MCE/2024-10-24 | SICK
                                                                                                                    Subject to change without notice

SIG200 CONFIGURATION 7


7                  SIG200 configuration
                                   The SIG200 EtherNet/IP can be parameterized using the following methods:
                                   1    EtherNet/IP (fieldbus/PLC engineering tool)
                                   2    Ethernet (Webserver)
                                   3    USB (with SOPAS ET)
                                   4    Ethernet (with SOPAS ET)
                                   5    Ethernet (via REST API)
                                   Parameterization via EtherNet/IP (1) is performed using the engineering tool of the
                                   PLC manufacturer for direct access to the SIG200. Depending on which type of PLC
                                   engineering tool is used, parameterization of the SIG200 and the connected devices is
                                   done in different ways.
                                   The integrated web server (2) of the SIG200 provides direct access for parameteriza‐
                                   tion via a suitable web browser on devices connected to the same Ethernet network as
                                   the SIG200.
                                   In addition, the SIG200 can be done via USB (3) using the SOPAS engineering tool
                                   application from SICK. The required cable (M8, USB) must be ordered separately. It is
                                   also possible to connect the SIG200 to SOPAS ET via Ethernet (4) for parameterization.
                                   The SOPAS engineering tool application can be downloaded from www.sick.com.
                                   The SIG200 also has a REST API interface that provides direct access for higher-level
                                   automation operations. A REST API is a programming interface that defines functions
                                   for making requests and receiving responses via HTTP protocols such as GET and POST
                                   (REST = Representational State Transfer, API = Application Programming Interface).

7.1                SIG200 EtherNet/IP interface
                                   The SIG200 can be configured with an appropriate PLC and EtherNet/IP software tools.
                                   This includes addressing and configuration.

7.1.1              Configuration via EtherNet/IP

7.1.1.1            Parameterization
                                   The SIG200 EtherNet/IP can be integrated into EtherNet/IP control systems using
                                   various methods.

                                   NOTE
                                   All configuration information relates to controls manufactured by Rockwell Automation,
                                   which are configured and diagnosed with the RSLogix 5000 configuration tool.

                                   Integration in Ethernet/IP
                                   The SIG200 EtherNet/IP can be integrated into EtherNet/IP using the following meth‐
                                   ods:
                                   •    As a generic module:
                                        All module settings must be selected manually.


                                   •    Using an EDS file:
                                        The SIG200 module settings have been predefined.




8016629.1MCE/2024-10-24 | SICK                                       O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   15
Subject to change without notice

7 SIG200 CONFIGURATION

                                         Configuration
                                         The parameters are configured offline, then written to the SIG200 and activated
                                         on switching to online mode. The following options are available for configuring the
                                         SIG200:
                                          •       The configuration assembly
                                          •       The controller tags in the Controller Organizer

                                         Configuration options when integrating as a generic module
                                          •       If you have integrated the SIG200 as a generic module, then you can configure it
                                                  dependent on the Connection Parameters entered.
                                          •       If the configuration assembly is activated in the connection parameters, you must
                                                  perform the configuration with the configuration assembly.

                                         Configuration options when integrating using the EDS file
                                          •       If you have integrated the SIG200 with the EDS file, it can be configured depend‐
                                                  ing on the selected instances of the I/O assemblies.
                                         Table 7: Overview of connection types
                                          Connection type                       Assembly               Description             Note
                                          Exclusive owner with                  I/O assembly: 100      This connection type sends and receives proc‐
                                          config                                through 101            ess data and contains a configuration assembly
                                                                                Configuration assem‐
                                                                                bly: 102
                                          Input only without con‐ I/O assembly: 100                    This connection type sends process data and
                                          fig                     Configuration assem‐                 does not contain a configuration assembly.
                                                                  bly: –


7.1.1.2           Integration as a generic module
                                         1.       Right-click the Ethernet icon, then click on New Module....
                                         ✓        The Select Module dialog box opens.
                                         2.       In the Select Module dialog, select the By Category index card.
                                         3.       Open the Communication structure tree.
                                         4.       In the Communication structure tree, mark the ETHERNET MODULE (Generic Ethernet
                                                  Module) module. Click on OK.
                                         ✓        The Module Properties [module name] dialog box opens.

                                         Module settings
                                         1.       In the Module Properties [module name] dialog, enter a name and the IP address of
                                                  the SIG200.
                                         2.       Configure the settings for input, output and configuration as follows:
                                                  If the generic module is used, 4 bytes of user data must be added to the user data
                                                  length after see "Assembly object", page 22.
                                                  Example:
                                                   ° Input: Assembly instance: 100; length aftersee table 19, page 22: 328 bytes
                                                   ° Information stated in the generic module: 332 bytes
                                                  NOTE
                                                  When specifying the data length, pay attention to the data type selected under
                                                  Comm Format!

                                         If the generic assembly is used, the header data is now transmitted in bytes 0:3 in the
                                         SIG200 input data:
                                          •       Bit 0: Run/Idle (1 = Run mode | 0 = Idle mode)
                                          •       Bit 1: Claim Output Ownership (COO) flag

16        O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                       8016629.1MCE/2024-10-24 | SICK
                                                                                                                                 Subject to change without notice

SIG200 CONFIGURATION 7


                                   •    Bit 2 ... 3: Ready for Ownership of Outputs (ROO) flags
                                   •    Bit 4 ... 31: Reserved by CIP
                                   The actual SIG200 payload starts at byte 4.
                                   •    Output: Assembly instance: 101
                                        Select this instance if no output data is to be written. The output parameter is set
                                        to 101 (input only).
                                   •    Output: Assembly instance: 101; size: 262 bytes
                                        Select this instance if output data is to be sent.
                                   The composition of the control output data is given under section 7.1.3.3.

                                   NOTE
                                   When specifying the data length, pay attention to the data type selected under Comm
                                   Format!

                                   •    Configuration: Assembly instance: 102; size: 52
                                        Instance 102 of the assembly object is selected.

                                   NOTE
                                   The assembly object contains a configuration assembly. The configuration assembly is repre‐
                                   sented by instance 102. Before the configuration assembly can be accessed by the con‐
                                   troller, valid data must be written to it. An empty configuration assembly or a configuration
                                   assembly with invalid data can lead to a controller error.

                                   Downloading the configuration to the control
                                   1.   Load the configuration to the controller.
                                   ✓    The status displays for Run Mode, Controller OK, and I/O OK turn green.
                                   Checking communication
                                       The data received by the control from the SIG200 can be displayed in order
                                       to check that communication between the control and the SIG200 is working
                                       correctly.
                                   1. In the Controller Organizer, open the Controller Test Setup, Controller Tags folder.
                                   2. Under Controller Tags in the Name column, select the node with the name previously
                                       entered for the SIG200.

7.1.1.3            Integration using an EDS file
                                   Common configuration tools can import an EDS file for integration of the SIG200 into
                                   the EtherNet/IP™ network.
                                   The EDS file for the SIG200 can be downloaded from www.sick.com (SIG200 EDS file).
                                   Instructions on how to import the file can be found in the documentation of your
                                   configuration tool.
                                   Prerequisites
                                   • Use of an Allen Bradley controller system with “RSLogix 5000” control software
                                        V22 or newer (or another controller that allows facilitated integration with an EDS
                                        file).
                                   • The SIG200 has an IP address (see "IP address of the SIG200", page 18).
                                   • The EDS file has been integrated into the control software using the Rockwell
                                        Hardware Installation Tool.

                                   Setting up communication
                                   1.   Right-click the Ethernet icon, then click on New Module....
                                   ✓    The Select Module Type dialog box opens.
                                   2.   On the Catalog index card, select the SIG200 option.

8016629.1MCE/2024-10-24 | SICK                                          O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   17
Subject to change without notice

7 SIG200 CONFIGURATION

                                       ✓        The Module Properties [module name] dialog box opens.
                                       3.       Enter any name you want in the Name field. In the IP address field, enter the IP
                                                address for the SIG200.
                                       ✓        In the Module Definition area, the Exclusive Owner (100) default connection is dis‐
                                                played as Connection . This is instance 100 of the assembly object.
                                       Changing the instance of the assembly object
                                       1. To change the instance, click Change.......
                                       2. For example, select Exclusive Owner 101.
                                       3. Under Size, select the UINT-16 data format.
                                       Checking communication
                                           The data received by the control from the SIG200 can be displayed in order
                                           to check that communication between the control and the SIG200 is working
                                           correctly.
                                       1. In the Controller Organizer, open the Controller Test Setup, Controller Tags folder.
                                       2. Under Controller Tags in the Name column, open the node with the name previously
                                           entered for the SIG200.

7.1.2           IP address of the SIG200
                                       The SIG200 is shipped from the factory without a preset IP address. The default setting
                                       for IP address assignment is made via the BOOTP protocol.

                                       Assigning the IP address via BOOTP or DHCP
                                       If your control has a BOOTP or DHCP server, you can assign an IP address to the
                                       SIG200 via this server.
                                       1.       Start the BOOTP/DHCP server (usually from the start menu of your computer
                                                under Rockwell Software, BOOTP-DHCP server, BOOTP-DHCP server).
                                       ✓        The SIG200 is displayed as a node in the program window of the BOOTP/DHCP
                                                server; its MAC address is also displayed, but not its assigned IP address.
                                       2.       Open the SIG200 by double-clicking in the BOOTP/DHCP server.
                                       3.       Enter a valid and free IP address in the IP Address field. Click on OK.
                                       4.       Click Clear History.
                                       ✓        After a while, the SIG200 is displayed with the entered IP address under Request
                                                History, as well as under Relation List.

                                       Freezing the assigned IP address

                                       NOTE
                                       The procedure described below can be used to ensure that the address assigned via
                                       BOOTP/DHCP is retained even after a restart:

                                       1.       Deactivate the DHCP function in the SIG200 by setting attribute 3 of the TCP/IP
                                                interface object to 0. To do this, click Disable BOOTP/DHCP on the Rockwell BOOTP/
                                                DHCP server, for example.
                                       ✓        After a restart, the SIG200 starts up with the IP address that was previously
                                                assigned and backed up in the non-volatile memory.
                                                The RSLinx Classic tool can be used to check again whether the controller recog‐
                                                nizes the specified IP address.
                                       2.       Start the RSLinx Classic (usually from your computer Start menu under Rockwell
                                                Software, RSLinx, RSLinx Classic).
                                       3.       Click on RSWho in the program.
                                       4.       Then open the AB_ETHIP1,Ethernet path.
                                       ✓        The SIG200 can be seen below its IP address.




18      O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                            8016629.1MCE/2024-10-24 | SICK
                                                                                                                    Subject to change without notice

SIG200 CONFIGURATION 7


7.1.3              Operation via EtherNet/IP
                                   The SIG200 can exchange process data (I/O) and (explicit) parameters via EtherNet/IP.
                                   For this purpose, the IO-Link master must be connected to a suitable programmable
                                   logic controller (PLC).
                                   The EtherNet/IP interface of the SIG200 has the following features:
                                   Properties                                Values
                                   Transmission rate                         10 or 100 Mbit/s
                                   Maximum distance between nodes            100 m
                                   Process data (implicit connection)        Depending on selected assemblies
                                                                             Minimum cycle time: 2 ms
                                   Max. process input data                   328 byte
                                   Max. process output data                  262 byte
                                   Asynchronous data (explicit connec‐       Manufacturer-specific classes per module
                                   tion)
                                   Observed standard                         IEEE802.3u (100Base-Tx)
                                   Max. number of connections                8
                                   Ethernet ports                            2
                                   CIP services                              DLR, QoS
                                   EDS file                                  Available at www.sick.com


7.1.3.1            Supported classes
                                   The SIG200 supports the following classes:
                                   Table 8: Supported standard classes
                                   Class code       Class               Description                        Services                              Instances
                                   0x01             Identity object     Contains all device-               Get_Attribute_Single                  1
                                                                        specific data (e.g., ID,           Get_Attribute_All
                                                                        device type, device                Reset
                                                                        status, etc.)
                                   0x02             Message router      Contains all supported -                                                 1
                                                    object              class codes for the
                                                                        device and the maxi‐
                                                                        mum number of con‐
                                                                        nections
                                   0x04             Assembly object     Groups together the                Get_Attribute_Single                  5
                                                                        data for several                   Set_Attribute_Single
                                                                        objects into a single
                                                                        object
                                   0x06             Connection man‐     Contains connection-               Get_Attribute_Single                  1
                                                    ager object         specific attributes for
                                                                        triggering, transport,
                                                                        connection type, etc.
                                   0x47             Device level ring   Contains the status                Get_Attribute_Single                  1
                                                    (DLR) object        and configuration                  Get_Attribute_All
                                                                        attributes of the DLR
                                                                        protocol
                                   0x48             Quality of service Contains mechanisms Get_Attribute_Single                                  1
                                                    (QoS) object       for processing data       Set_Attribute_Single
                                                                       flows with different pri‐
                                                                       orities




8016629.1MCE/2024-10-24 | SICK                                             O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200     19
Subject to change without notice

7 SIG200 CONFIGURATION

                                          Class code             Class                        Description              Services                     Instances
                                          0xF5                   TCP/IP interface             Contains the attrib‐     Get_Attribute_Single         1
                                                                 object                       utes for TCP/IP, such    Set_Attribute_Single
                                                                                              as IP address, subnet    Get_Attribute_All
                                                                                              mask, and gateway or
                                                                                              reference for the IP
                                                                                              address via DHCP
                                          0xF6                   Ethernet link                Contains connection-     Get_Attribute_Single         2
                                                                 object                       specific attributes,     Set_Attribute_Single
                                                                                              such as transmission     Get_Attribute_All
                                                                                              speed, interface sta‐    Get_and_Clear
                                                                                              tus, and MAC address

                                         NOTE
                                         The minimum RPI time is 2 ms.

                                         Table 9: Supported manufacturer classes
                                          Class code             Class                        Description              Services                     Instances
                                          0x96                   IO-Link device               Enables access to      Custom Service                 1 ... 4
                                                                                              ISDUs, Data Storage    0x32: ISDU
                                                                                              objects, process data, 0x33: Backup
                                                                                              port configuration,    0x34: PDAccess
                                                                                              port status and mas‐   0x35: PortConfig
                                                                                              ter information        0x36: PortStatus
                                                                                                                     0x37: MasterInfo


7.1.3.2           Identity Object
                                         Table 10: Class services of the identity object
                                          Service code Service                                          Description
                                          0x01                   Get_Attribute_All                      Returns the values of all attributes
                                          0x0E                   Get_Attribute_Single                   Returns the values of an attribute

                                         Table 11: Class attributes of the identity object
                                          Attribute ID           Access                   Description                                               Data type
                                          1                      Get                      Object revision index                                     UINT
                                          2                      Get                      Highest instance number in this class                     UINT
                                          6                      Get                      Highest class attribute ID that appears                   UINT
                                          7                      Get                      Highest instance attribute implemented                    UINT

                                         Table 12: Instance services of the identity object
                                          Service code Service                                Description
                                          0x01                   Get_Attribute_All            Returns the values of all attributes
                                          0x0E                   Get_Attrib‐                  Returns the values of an attribute
                                                                 ute_Single
                                          0x05                   Reset                        Resets the device:
                                                                                              0 = The device is reinitialized (power on)
                                                                                              1 = The device is reinitialized (power on) and reset to factory
                                                                                              settings.




20        O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                              8016629.1MCE/2024-10-24 | SICK
                                                                                                                                        Subject to change without notice

SIG200 CONFIGURATION 7


                                   NOTE
                                   If you reset to factory settings, you will lose all data that has already been configured.
                                   •     The factory settings are restored as soon as 1 is written.
                                   •     The SIG200 will be reset too. Therefore, the control reports, where necessary, an
                                         error that the SIG200 is no longer available.

                                   Table 13: Instance attributes of the identity object
                                   Attribute ID        Access        Data type                 Name                          Default value
                                   0x01                R             UINT                      Manufacturer ID               0x0328 corresponds to
                                                                                                                             the SICK vendor ID
                                   0x02                R             UINT                      Device type                   0x000C
                                   0x03                R             UINT                      Product Code                  0x4100
                                   0x04                R             STRUCT                    Revision                      Contains the firmware
                                                                                                                             revision number
                                                                                                                             UINT 0x0001
                                                                                                                             UINT 0x0001
                                   0x05                R             WORD                      Status                        see table 14
                                   0x06                R             UDINT                     Serial Number                 yywwnnnn
                                   0x07                R             Short_String              Product name                  SIG200
                                   0x08                R             USINT                     State                         Current device status
                                                                                                                             0 = Non-existent
                                                                                                                             1 = Self-test
                                                                                                                             2 = Standby
                                                                                                                             3 = Operation
                                                                                                                             4 = Serious remediable
                                                                                                                             error
                                                                                                                             5 = Serious non-remedia‐
                                                                                                                             ble error
                                                                                                                             255 = Default value

                                   Table 14: Bits of the status instance attribute
                                   Bit             Name                               Description                                          Default value
                                   0               Owned                              0 = no connection with the mas‐ 0
                                                                                      ter
                                                                                      1 = connection established with
                                                                                      the master
                                   1               -                                  Reserved                                             0
                                   2               Configured                         0 = device with standard config‐ 0
                                                                                      uration
                                                                                      1 = no standard configuration
                                   3               -                                  Reserved                                             0
                                   4…7             Extended device status             Manufacturer-specific status                         see table 15
                                                   field                              bits
                                   8               Minor recoverable status           0 = no error                                         0
                                                                                      1 = error that can be reset
                                                                                      (device not in error status)
                                   9               Minor unrecoverable status 0 = no error                                                 0
                                                                              1 = error that cannot be reset
                                                                              (device not in error status)
                                   10              Major recoverable status           0 = no major error                                   0
                                                                                      1 = major error that can be
                                                                                      reset (device in error status



8016629.1MCE/2024-10-24 | SICK                                              O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   21
Subject to change without notice

7 SIG200 CONFIGURATION

                                          Bit                    Name                                   Description                          Default value
                                          11                     Major unrecoverable status 0 = no major error                               0
                                                                                            1 = major error that cannot be
                                                                                            reset (device in error status)
                                          12 … 15                -                                      Reserved                             0000

                                         Table 15: Bits 4 to 7 of the status instance attribute
                                          Possible combina‐                     Description
                                          tions Bits 4 … 7
                                          0000                                  Device in self-test
                                          0001                                  Firmware update in progress
                                          0010                                  At least one connection error
                                          0011                                  No I/O connection established
                                          0100                                  Configuration in non-volatile memory (EEPROM) failed
                                          0101                                  Major error, bit 10 or bit 11 = 1
                                          0110                                  At least one connection in Run operating mode
                                          0111                                  At least one connection present, all in Idling operating mode
                                          1,000 … 1,111                         Reserved


7.1.3.3           Assembly object
                                         Class code 0x04
                                         The Assembly object allows the grouping of data objects from different objects into a
                                         single object. The SIG200 supports only static groupings of objects where the number
                                         of instances is fixed.
                                         Table 16: Class services of the Assembly object
                                          Service code Service                                          Description
                                          0x0E                   Get_Attribute_Single                   Returns the values of an attribute

                                         Table 17: Class attributes of the Assembly object
                                          Attribute ID           Access                   Description                                               Data type
                                          1                      Get                      Object revision index                                     UINT

                                         Table 18: Instance services of the Assembly object
                                          Service code Service                                          Description
                                          0x0E                   Get_Attribute_Single                   Returns the values of an attribute
                                          0x10                   Set_Attribute_Single                   Sets the value of an attribute

                                         Table 19: Instance attributes of the Assembly object
                                          Instance               Attribute ID                 Access              Description                Default value
                                          100                    3                            Get                 Assembly input
                                                                 4                            Get                 Size 16                    0x148
                                          101                    3                            Get/Set             Assembly output
                                                                 4                            Get                 Size 16                    0x106
                                          102                    3                            Get                 Configuration Assembly
                                                                 4                            Get                 Size 16                    0x34




22        O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                              8016629.1MCE/2024-10-24 | SICK
                                                                                                                                        Subject to change without notice

SIG200 CONFIGURATION 7


                                   I/O assemblies with process data
                                   Table 20: Assembly input - instance 100
                                   Byte              Designa‐                         Data           Data           Description
                                                     tion                             length         Type
                                   0                 Inputs                           1 byte         UINT8          See bit description for input
                                                                                                                    data
                                   1...7             Reserved                         7 byte         ARRAY          -
                                   8...39            Port S1    IOLink input          32 byte ARRAY                 See documentation for con‐
                                                                data                                                nected device
                                   40                           IOL Status            1 byte         UINT8          See bit description for IOL
                                                                                                                    status
                                   41                           IOL Error             1 byte         UINT8          See bit description for IOL
                                                                                                                    error
                                   42...43                      Manufacturer          2 byte         UINT16 See documentation for con‐
                                                                ID                                          nected device
                                   44...46                      Device ID             3 byte         ARRAY          See documentation for con‐
                                                                                                                    nected device
                                   47                           IOL Event Error       1 byte         UINT8          See documentation for con‐
                                                                                                                    nected device
                                   48...49                      IOL Event Addi‐       2 byte         UINT16 See documentation for con‐
                                                                tional Code                                 nected device
                                   50                           IOL Event Error       1 byte         UINT8          See documentation for con‐
                                                                                                                    nected device
                                   51...52                      IOL Event Addi‐       2 byte         UINT16 See documentation for con‐
                                                                tional Code                                 nected device
                                   53                           IOL Event Error       1 byte         UINT8          See documentation for con‐
                                                                                                                    nected device
                                   54...55                      IO Event Addi‐        2 byte         UINT16 See documentation for con‐
                                                                tional Code                                 nected device
                                   56...87           Port S2    IOLink input          32 byte ARRAY                 See documentation for con‐
                                                                data                                                nected device
                                   88                           IOL Status            1 byte         UINT8          See bit description for IOL
                                                                                                                    status
                                   89                           IOL Error             1 byte         UINT8          See bit description for IOL
                                                                                                                    error
                                   90...91                      Manufacturer          2 byte         UINT16 See documentation for con‐
                                                                ID                                          nected device
                                   92...94                      Device ID             3 byte         ARRAY          See documentation for con‐
                                                                                                                    nected device
                                   95                           IOL Event Error       1 byte         UINT8          See documentation for con‐
                                                                                                                    nected device
                                   96...97                      IOL Event Addi‐       2 byte         UINT16 See documentation for con‐
                                                                tional Code                                 nected device
                                   98                           IOL Event Error       1 byte         UINT8          See documentation for con‐
                                                                                                                    nected device
                                   99...100                     IOL Event Addi‐       2 byte         UINT16 See documentation for con‐
                                                                tional Code                                 nected device
                                   101                          IOL Event Error       1 byte         UNIT8          See documentation for con‐
                                                                                                                    nected device
                                   102...103                    IOL Event Addi‐       2 byte         UINT16 See documentation for con‐
                                                                tional Code                                 nected device



8016629.1MCE/2024-10-24 | SICK                                          O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   23
Subject to change without notice

7 SIG200 CONFIGURATION

                                     Byte                       Designa‐                               Data     Data    Description
                                                                tion                                   length   Type
                                     104...135                  Port S3              IOLink input      32 byte ARRAY    See documentation for con‐
                                                                                     data                               nected device
                                     136                                             IOL Status        1 byte   UINT8   See bit description for IOL
                                                                                                                        status
                                     137                                             IOL Error         1 byte   UINT8   See bit description for IOL
                                                                                                                        error
                                     138...139                                       Manufacturer      2 byte   UINT16 See documentation for con‐
                                                                                     ID                                nected device
                                     140...142                                       Device ID         3 byte   ARRAY   See documentation for con‐
                                                                                                                        nected device
                                     143                                             IOL Event Error   1 byte   UINT8   See documentation for con‐
                                                                                                                        nected device
                                     144...145                                       IOL Event Addi‐   2 byte   UINT16 See documentation for con‐
                                                                                     tional Code                       nected device
                                     146                                             IOL Event Error   1 byte   UINT8   See documentation for con‐
                                                                                                                        nected device
                                     147...148                                       IOL Event Addi‐   2 byte   UINT16 See documentation for con‐
                                                                                     tional Code                       nected device
                                     149                                             IOL Event Error   1 byte   UINT8   See documentation for con‐
                                                                                                                        nected device
                                     150...151                                       IOL Event Addi‐   2 byte   UNIT16 See documentation for con‐
                                                                                     tional Code                       nected device
                                     152...183                  Port S4              IOLink input      32 byte ARRAY    See documentation for con‐
                                                                                     data                               nected device
                                     184                                             IOL Status        1 byte   UINT8   See bit description for IOL
                                                                                                                        status
                                     185                                             IOL Error         1 byte   UINT8   See bit description for IOL
                                                                                                                        error
                                     186...187                                       Manufacturer      2 byte   UINT16 See documentation for con‐
                                                                                     ID                                nected device
                                     188...190                                       Device ID         3 byte   ARRAY   See documentation for con‐
                                                                                                                        nected device
                                     191                                             IOL Event Error   1 byte   UINT8   See documentation for con‐
                                                                                                                        nected device
                                     192...193                                       IOL Event Addi‐   2 byte   INT16   See documentation for con‐
                                                                                     tional Code                        nected device
                                     194                                             IOL Event Error   1 byte   UNIT8   See documentation for con‐
                                                                                                                        nected device
                                     195...196                                       IOL Event Addi‐   2 byte   UINT16 See documentation for con‐
                                                                                     tional Code                       nected device
                                     197...198                                       IOL Event Error   1 byte   UINT8   See documentation for con‐
                                                                                                                        nected device
                                     199                                             IOL Event Addi‐   2 byte   UINT16 See documentation for con‐
                                                                                     tional Code                       nected device
                                     200...327                  Logic Editor input data                128      ARRAY   Depending on the logic editor
                                                                                                       byte             configuration




24   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                            8016629.1MCE/2024-10-24 | SICK
                                                                                                                                 Subject to change without notice

SIG200 CONFIGURATION 7


                                   Table 21: Assembly output - instance 101
                                   Byte                 Designa‐                           Data           Data           Description
                                                        tion                               length         Type
                                   0...5                Reserved                           6 byte         ARRAY          -
                                   6                    Port S1       IO-Link output       1 byte         ARRAY          See documentation of the
                                                                      data/DO pin                                        connected device/bit 0, sets
                                                                                                                         the output.
                                   7...37                             IOLink output        31 byte ARRAY                 See documentation of the
                                                                      data                                               connected device
                                   38                   Port S2       IO-Link output       1 byte         ARRAY          See documentation of the
                                                                      data/DO pin                                        connected device/bit 0, sets
                                                                                                                         the output.
                                   39...69                            IOLink output        31 byte ARRAY                 See documentation of the
                                                                      data                                               connected device
                                   70                   Port S3       IO-Link output       1 byte         ARRAY          See documentation of the
                                                                      data/DO pin                                        connected device/bit 0, sets
                                                                                                                         the output.
                                   71...101                           IOLink output        31 byte ARRAY                 See documentation of the
                                                                      data                                               connected device
                                   102                  Port S4       IO-Link output       1 byte         ARRAY          See documentation of the
                                                                      data/DO pin                                        connected device/bit 0, sets
                                                                                                                         the output.
                                   103...133                          IOLink output        31 byte ARRAY                 See documentation of the
                                                                      data                                               connected device
                                   134...261            Logic Editor output data           128            ARRAY          Depending on the logic editor
                                                                                           byte                          configuration

                                   Table 22: Bit description for input data
                                   Bit 7        Bit 6         Bit 5          Bit 4            Bit 3              Bit 2              Bit 1              Bit 0
                                   DI S4        DI S4         DI S3          DI S3            DI S2              DI S2              DI S1              DI S1
                                   Pin 2        Pin 4         Pin 2          Pin 4            Pin 2              Pin 4              Pin 2              Pin 4

                                   Table 23: Bit description for IOL status
                                   Bit 7        Bit 6         Bit 5          Bit 4            Bit 3              Bit 2              Bit 1              Bit 0
                                   0            0             0              0                0                  0                  Device    Port in IOL
                                                                                                                                    connected mode

                                   Table 24: Bit description for IOL error
                                   Bit 7        Bit 6         Bit 5          Bit 4            Bit 3              Bit 2              Bit 1              Bit 0
                                   0            0             0              0                0                  Validation Data stor‐                 Process
                                                                                                                 failed     age vali‐                  data inva‐
                                                                                                                            dation                     lid
                                                                                                                            failed

                                   Configuration assemblies
                                   Table 25: Assembly output - instance 102
                                   Byte                 Designa‐                           Data           Data           Description
                                                        tion                               length         Type
                                   0...11               Port S1       IOLink Configu‐      12 byte ARRAY                 see table 26, page 26
                                                                      ration
                                   12...23              Port S2       IOLink Configu‐      12 byte ARRAY                 see table 26, page 26
                                                                      ration
                                   24...35              Port S3       IOLink Configu‐      12-byte ARRAY                 see table 26, page 26
                                                                      ration


8016629.1MCE/2024-10-24 | SICK                                               O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200      25
Subject to change without notice

7 SIG200 CONFIGURATION

                                     Byte                       Designa‐                                Data       Data      Description
                                                                tion                                    length     Type
                                     36...47                    Port S4              IOLink Configu‐    12-byte ARRAY        see table 26, page 26
                                                                                     ration
                                     48                         Logic Editor output data                1 byte     ARRAY     see table 27

                                    Table 26: IOLink Port Configuration Description
                                     Byte                       Description                         Data         Data Type    Mini‐        Maxi‐        Default
                                                                                                    length                    mum          mum
                                     0                          Port Mode                           1 byte       UINT8        0            4            0
                                     1...2                      Cycle Time                          2 byte       INT16        0            8            0
                                     3                          Validation and backup 1 byte                     UINT8        0            4            0
                                     5...8                      Manufacturer ID                     4 byte       UINT32       0            65535        0
                                     9...12                     Device ID                           4 byte       UINT32       0            16777        0
                                                                                                                                           216

                                    Table 27: Logic editor configuration
                                     Byte                       Description                         Data         Data Type    Mini‐        Maxi‐        Default
                                                                                                    length                    mum          mum
                                     0                          Logic Editor byte size              1 byte       UINT8        0            21           21
                                                                for inut and output
                                                                process data

                                    Table 28: Logic editor configuration
                                     Value                                           Description
                                     0                                               None
                                     1                                               2 In / 0 Out
                                     2                                               0 In / 2 Out
                                     3                                               2 In / 2 Out
                                     4                                               4 In / 0 Out
                                     5                                               0 In / 4 Out
                                     6                                               4 In / 4 Out
                                     7                                               8 In / 0 Out
                                     8                                               0 In / 8 Out
                                     9                                               8 In / 8 Out
                                     10                                              16 In / 0 Out
                                     11                                              0 In / 16 Out
                                     12                                              16 In / 16 Out
                                     13                                              32 In / 0 Out
                                     14                                              0 In / 32 Out
                                     15                                              32 In / 32 Out
                                     16                                              64 In / 0 Out
                                     17                                              0 In / 64 Out
                                     18                                              64 In / 64 Out
                                     19                                              128 In / 0 Out
                                     20                                              0 In / 128 Out
                                     21                                              128 In / 128 Out




26   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                                8016629.1MCE/2024-10-24 | SICK
                                                                                                                                     Subject to change without notice

SIG200 CONFIGURATION 7


                                   Table 29: Port Mode
                                   Value                        Description
                                   0                            IOL AutoConfig
                                   1                            IOL Manual
                                   2                            Reserved
                                   3                            Digital In (Pin 4)
                                   4                            Digital Out (Pin 4)

                                   Table 30: Cycle Time
                                   Value                        Description
                                   0                            Fast as possible
                                   16                           1.6 ms
                                   32                           3.2 ms
                                   48                           4.8 ms
                                   68                           8.0 ms
                                   100                          20.8 ms
                                   133                          40 ms
                                   158                          80 ms
                                   183                          120 ms

                                   Table 31: Data Storage Validation and Backup
                                   Value                        Description
                                   0                            No device check
                                   1                            Type compatible device (V1.0)
                                   2                            Type compatible device (V1.1)
                                   3                            V1.1 with backup and restore
                                   4                            V1.1 with Restore

                                   NOTE
                                   Port Mode must be set to IOL Manual to configure the Cycle Time and Valid Backup options
                                   of the port.


                                   NOTE
                                   Port Mode must be set to Digital Out to configure the outputs via the output assembly.


7.1.3.4            Manufacturer-specific classes
                                   Table 32: Nomenclature for access and data types
                                   Abbreviation       Meaning
                                   R                  Read only access
                                   R/W                Read/write access
                                   STRG               String = a chain of characters of varying length
                                   BOOL               Boolean = logical value 0 or 1
                                   ENUM               Freely selectable values within a limited value range (e.g. BLACK, RED,
                                                      BLUE, YELLOW)
                                   INT                Signed Integer = Signed integer value (e.g. INT-32 = -2,147,483,648 ...
                                                      2,147,483,647)
                                   UINT               Unsigned integer = Integer value (e.g. UINT-32 = 0 ... 4,294,967,295)



8016629.1MCE/2024-10-24 | SICK                                           O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   27
Subject to change without notice

7 SIG200 CONFIGURATION

                                        Abbreviation                  Meaning
                                        ARRAY                         Data sequence of a data type (e.g. Array UINT-8 = Character string of the
                                                                      data type UINT-8)
                                        RECORD                        Data sequence with different data types (e.g. UINT-8, UINT-32, UINT-32,
                                                                      UINT-16)
                                        STRUCT                        Data sequence with different data types (e.g. UINT-8, UINT-32, UINT-32,
                                                                      UINT-16)

                                       NOTE
                                       A string in EtherNet/IP consists of 2 bytes of length information followed by a byte
                                       container of the specified length.


7.1.3.4.1                  Class 150 IO-Link Device
                                       Supported Services
                                       Table 33: Supported Services
                                        Serv‐ Name                 Attribute Instance Data             Command specific          Common error codes
                                        ice ID                                        Length           errors
                                        0x32        ISDU           0: Read          PortID   Depend 0xB500: Read Access
                                        (50)                       1: Write         1: S1    s on   State Conflict
                                                                                    2: S2    record
                                                                                    3: S3    length
                                                                                    4: S4
                                        0x33        Backup 0: Read                  PortID   Depend                              0xA000: Read Appli‐
                                        (51)               1: Write                 1: S1    s on                                cation Error
                                                                                    2: S2    record
                                                                                    3: S3    length
                                                                                    4: S4
                                        0x34        PDAc‐          0: Read          PortID   Depend                              0xB300: Read Access
                                        (52)        cess           1: Write         1: S1    s on PD                             Type Conflict
                                                                                    2: S2    Length
                                                                                    3: S3
                                                                                    4: S4
                                        0x35        Port‐          0: Read          PortID   18        0xA800: Version Con‐
                                        (53)        Config         1: Write         1: S1              flict
                                                                                    2: S2              0xC300: Resource
                                                                                    3: S3              unavailable
                                                                                    4: S4              0xA100: Write Applica‐
                                                                                                       tion Error
                                        0x36        PortSta‐ 0: Read                PortID   25        0xB600: Access error
                                        (54)        tus                             1: S1
                                                                                    2: S2
                                                                                    3: S3
                                                                                    4: S4
                                        0x37        Master‐ 0: Read                 1        7         0xB600: Access error
                                        (55)        Info

                                       ISDU access (Service ID 0x32)
                                       ISDUs are read in 2 steps using Service ID 0x32, where the port is addressed via the
                                       instance. First, the required data must be written to the device. For this purpose, the
                                       attribute is set to 1 and the data is entered according to the table. Note that the control
                                       byte is set to 3 and the data length must be at least 8 bytes.
                                       To read the ISDU response, read access via attribute 0 now follows. The structure of the
                                       ISDU response can be found in the table.


28      O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                           8016629.1MCE/2024-10-24 | SICK
                                                                                                                                   Subject to change without notice

SIG200 CONFIGURATION 7


                                   When writing ISDUs, the attribute is set to 1 and the control byte is set to 2. The user
                                   data is forwarded directly to the IO-Link device according to index and subindex.

                                   Data layout of ISDU request
                                   Table 34: Data layout of ISDU request
                                   Byte      Name                            Description
                                   0         Control                         0: Cancel pending request
                                                                             1: nothing to do
                                                                             2: write request
                                                                             3: read request
                                   1         Index (MSB)
                                   2         Index (LSB)
                                   3         Subindex
                                   4         Playload                        Used only on write

                                   ISDU Response Data Layout
                                   Table 35: ISDU Response Data Layout
                                   Byte      Name                            Description
                                   0         Function                        Always 0x08
                                   1         PortID                          1: S1
                                                                             2: S2
                                                                             3: S3
                                                                             4: S4
                                   2 ... 3   Function Index                  Always 0xFE4A
                                   4         Status                          0x00: successful
                                                                             0x80: error
                                   5         Index (MSB)
                                   6         Index (LSB)
                                   7         Subindex
                                   8         Playload

                                   Read MasterInfo response data layout
                                   Table 36: Read MasterInfo response data layout
                                   Byte      Name                            Description
                                   0         Block type                      0x01
                                   1         Block version                   0x00
                                   2 ... 3   Reserved                        0x0000
                                   4         Port Count                      0x04
                                   5 ... 6   Client Access Point             0xB400

                                   Read PortStatus response data layout
                                   Table 37: Read PortStatus response data layout
                                   Byte      Name                            Description
                                   0         Block type                      0x01
                                             Block version                   0x00
                                   2 ... 3   Reserved                        0x0000




8016629.1MCE/2024-10-24 | SICK                                             O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   29
Subject to change without notice

7 SIG200 CONFIGURATION

                                     Byte           Name                             Description
                                     4              PortID                           1: S1
                                                                                     2: S2
                                                                                     3: S3
                                                                                     4: S4
                                     5              Status Info                      0: Running
                                                                                     1: Input
                                                                                     2: Output
                                                                                     3: Deactivated
                                                                                     4: No Device
                                                                                     5: Wrong Device
                                                                                     6: Fault
                                                                                     255: Unavailable
                                     6              Port Qualifier                   Bit 7: Valid
                                                                                     Bit 6: Device Error
                                                                                     Bit 5: Communication Error
                                                                                     Bit 4: Port Active
                                                                                     Bit 3: Substitute Device
                                                                                     Bit 2: New Parameter
                                     7              Port status flags                Bit 0: Process input data valid
                                                                                     Bit 1: Process output data valid
                                     8              Reserved                         Reserved
                                     9              Revision ID                      0: Unknown
                                                                                     0x10: V1.0
                                                                                     0x11: V1.1
                                     10             Transmission Rate                0: No communication
                                                                                     1: COM1
                                                                                     2: COM2
                                                                                     3: COM3
                                     11             Cycle Time                       0: Fast as possible
                                                                                     16: 1.6 ms
                                                                                     32: 3.2 ms
                                                                                     48: 4.8 ms
                                                                                     68: 8.0 ms
                                                                                     100: 20.8 ms
                                                                                     133: 40 ms
                                                                                     158: 80 ms
                                                                                     183: 120 ms
                                     12 ... 1       Manufacturer ID                  big endian
                                     3
                                     14 ... 1       Device ID                        big endian
                                     6
                                     17             Reserved                         0x00
                                     18             Reserved                         0x01
                                     19 ... 2       Reserved                         0x000000
                                     1
                                     22             Reserved                         0x01
                                     23 ...         Reserved                         0x0000
                                     24

                                    Read PortConfig response data layout
                                    Table 38: Read PortConfig response data layout
                                     Byte           Name                             Description
                                     0              Block type                       0x01



30   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                      8016629.1MCE/2024-10-24 | SICK
                                                                                                                           Subject to change without notice

SIG200 CONFIGURATION 7


                                   Byte       Name                          Description
                                   1          Block version                 0x00
                                   2 ... 3    Reserved                      0x0000
                                   4          Port Mode                     0: IOL AutoConfig
                                                                            1: IOL Manual
                                                                            2: Reserved
                                                                            3: Digital input (pin 4)
                                                                            4: Digital output (pin 4)
                                   5          Cycle Time                    0: Fast as possible
                                                                            16: 1.6 ms
                                                                            32: 3.2 ms
                                                                            48: 4.8 ms
                                                                            68: 8.0 ms
                                                                            100: 20.8 ms
                                                                            133: 40 ms
                                                                            158: 80 ms
                                                                            183: 120 ms
                                   6          Reserved                      0x00
                                   7          Valid Backup                  0: No device check
                                                                            1: Type compatible device (V1.0)
                                                                            2: Type compatible device (V1.1)
                                                                            3: V1.1 with Backup+Restore
                                                                            4: 1.1 with Restore
                                   8 ... 9    Manufacturer ID               little endian
                                   10 ... 1   Reserved                      0x0000
                                   1
                                   12 ... 1   Device ID                     little endian
                                   4
                                   15         Reserved                      0x00

                                   Write PortConfig request data layout
                                   Table 39: Write PortConfig request data layout
                                   Byte       Name                          Description
                                   0          Block type                    0x01
                                   1          Block version                 0x00
                                   2 ... 3    Reserved                      0x0000
                                              Port Mode                     0: IOL AutoConfig
                                                                            1: IOL Manual
                                                                            2: Reserved
                                                                            3: Digital input (pin 4)
                                                                            4: Digital output (pin 4)
                                   5          Cycle Time                    0: Fast as possible
                                                                            16: 1.6 ms
                                                                            32: 3.2 ms
                                                                            48: 4.8 ms
                                                                            68: 8.0 ms
                                                                            100: 20.8 ms
                                                                            133: 40 ms
                                                                            158: 80 ms
                                                                            183: 120 ms
                                   6          Reserved                      0x00




8016629.1MCE/2024-10-24 | SICK                                            O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   31
Subject to change without notice

7 SIG200 CONFIGURATION

                                     Byte           Name                             Description
                                     7              Valid Backup                     0: No device check
                                                                                     1: Type compatible device (V1.0)
                                                                                     2: Type compatible device (V1.1)
                                                                                     3: V1.1 with Backup+Restore
                                                                                     4: 1.1 with Restore
                                     8 ... 9        Manufacturer ID                  little endian
                                     10 ...         Reserved                         0x0000
                                     11
                                     12 ...         Device ID                        little endian
                                     14
                                     15             Reserved                         0x0000

                                    NOTE
                                    Port Mode must be set to IOL Manual to configure the Cycle Time and Valid Backup options
                                    of the port.

                                    Read Process Data Access Response Layout
                                    Table 40: Read Process Data Access Response Layout
                                     Byte           Name                             Description
                                     0              Block type                       0x01
                                     1              Block version                    0x00
                                     2 ... 3        Reserved                         0x0000
                                     4              Input length                     For EIP this value is always 33 or 0
                                     5 ... 37       Process input data and PQI For the PQI definition see see , page 33 (none exists for
                                                    byte at the end            length 0)
                                     38 (9 if       Output Data Length               For EIP this value is always 32 or 0
                                     input
                                     data
                                     length
                                     is 0)
                                     39 ... 7       Process output data
                                     0

                                    Layout for writing process data access request
                                    Table 41: Layout for writing process data access request
                                     Byte           Name                             Description
                                     0              Block type                       0x01
                                     1              Block version                    0x00
                                     2 ... 3        Reserved                         0x0000
                                     4              Input length                     For EIP this value is always 33 or 0
                                     5 ... 37       Process input data and PQI For the PQI definition see see , page 33 (none exists for
                                                    byte at the end            length 0)
                                     38 (5 if       Output Data Length               For EIP this value is always 32 or 0
                                     the
                                     input
                                     length
                                     is 0)
                                     39 ...         Process output data
                                     70



32   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                      8016629.1MCE/2024-10-24 | SICK
                                                                                                                           Subject to change without notice

SIG200 CONFIGURATION 7


                                   PQI description
                                   In IO-Link mode, each IO-Link port always has a status byte of input data (Port Qualifier
                                   Information, PQI). It contains the following data:
                                   Table 42: PQI description
                                   Bit                    Description
                                   Bit 7                  Validity of device process data (PQ)
                                                          0 = Invalid IO process data from device
                                                          1 = Valid IO process data from device
                                   Bit 6                  Display of a port/device error (DevErr)
                                                          0 = No error/no warning
                                                          1 = Error/warning for device or port
                                   Bit 5                  Device communication (DevCom)
                                                          0 = No device available
                                                          1 = Device detected and in PREOPERATE or OPERATE state
                                   Bit 4                  Port activation (PortActive)
                                                          0 = Port deactivated via port function
                                                          1 = Port activated
                                   Bit 3                  Substitute device detection (SubstDev)
                                                          0 = No substitute device detected (identical serial number)
                                                          1 = Substitute device detected (different serial number)
                                   Bit 2                  New parameter (NewPar)
                                                          0 = No change of device parameter detected
                                                          1 = Change of device parameter detected: Master has performed a data
                                                          memory upload and a new IOLD backup object (0xB904) is available

                                   Backup Response Data Layout
                                   Table 43: Backup Response Data Layout
                                   Byte        Name                           Description
                                   0           Block type                     type of record (1)
                                   1           Block version                  Data set version (0)
                                   2 ... 3     Reserved
                                   4           Data Storage Record


7.2                Operation via Webserver
                                   The SIG200 can be accessed via the integrated web server. To do so, an IP address
                                   must be set for the SIG200. The SIG200 is shipped from the factory without a preset IP
                                   address. The default setting for IP address assignment is made via the BOOTP protocol.
                                   The following web browsers are supported:
                                   •       Microsoft Internet Explorer (version 11 or higher)
                                   •       Google Chrome (version 50 or higher)
                                   •       Firefox (version 30 or higher)
                                   •       Safari (version 9 or higher)
                                   To access the integrated SIG200 web server, start the browser on your device and enter
                                   the IP address of the SIG200.




8016629.1MCE/2024-10-24 | SICK                                              O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   33
Subject to change without notice

7 SIG200 CONFIGURATION


                                       NOTE
                                       When using the web server and EtherNet/IP communication and user configuration at
                                       the same time, the response time increases.


                                       NOTE
                                       SIG200 only supports HTTP, the HTTPS protocol is not supported.

                                       The layout and functionality of the integrated webserver as accessed by a browser
                                       corresponds to the operation via SOPAS ET (using USB or Ethernet connection), see
                                       "Operation via SOPAS ET (USB/Ethernet)", page 34.

7.3             Operation via SOPAS ET (USB/Ethernet)
                                       With the aid of the SOPAS engineering tool application, the SIG200 can be parameter‐
                                       ized on a computer running Microsoft Windows.
                                       SIG200 configuration with SOPAS ET allows not only to configure the four ports of the
                                       IO-Link Master but also to configure the connected IO-Link devices via an embedded
                                       IODD interpreter.
                                       Additionally, via the Logic Editor (which is a graphical configuration environment) logic
                                       functions across multiple devices which are connected to SIG200 can be created.
                                       The physical connection between SOPAS ET (computer) and the SIG200 can be estab‐
                                       lished via USB or Ethernet.

                                       NOTE
                                       Basically, connecting the SIG200 to the computer via Ethernet is recommended. When
                                       using the USB interface, long waiting/loading times may occur for large amounts of
                                       data, as the data transmission rate on the USB interface is limited. Especially when
                                       saving large data flows in the logic editor, there may be connection problems between
                                       SOPAS and the device, meaning that the logic cannot be saved completely via USB.


7.3.1           Opening new project in SOPAS
                                       Connect the SIG200 to your computer and start SOPAS ET. When the program is
                                       started, the Ethernet and USB interfaces are always scanned for connected devices
                                       and devices found are automatically displayed as a new project icon.
                                       If the connected SIG200 does not automatically appear as a new project, check that
                                       the SIG200 is correctly connected to the computer and add the device to the project
                                       manually. To do so, run the device search again. Then select the desired SIG200 in the
                                       search results. Add to the project via drag and drop or double-click. Devices that are
                                       already in the project are grayed out in the search results.

                                       NOTE
                                       Also, make sure you are using the device family search (→ click Search settings . Select
                                       the Device family oriented search and “SIG200” options).

                                       If a SIG200 is inserted into a SOPAS project for the first time, then the corresponding
                                       device driver must be installed. In the project icon, click on the Install device driver button
                                       and either download the required SDD from the SICK homepage www.sick.com or
                                       upload it directly from the device. The uploaded device driver now appears in the device
                                       catalog.




34      O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                         8016629.1MCE/2024-10-24 | SICK
                                                                                                                 Subject to change without notice

SIG200 CONFIGURATION 7




                                   NOTE
                                   Make sure that the device driver available in the device catalog matches the firmware
                                   version of the SIG200 used. If these do not match, uninstall the SDD by right-clicking on
                                   the corresponding entry in the device catalog. Then upload the device driver again as
                                   described above.

                                   If the device status is signaled with OFFLINE in the project icon, then the SIG200
                                   must first be switched online. To do this, click the offline button and synchronize the
                                   parameter values in the project and on the device.
                                   Special user levels can be selected via the REGISTER button. For the standard configura‐
                                   tion of the SIG200, a special login is not required, since the required user levels Run
                                   and Maintenance are already stored in the device (for details see see "User login and
                                   editing mode", page 40).
                                   To parameterize the SIG200, double-click on any point on the project icon.
                                   The device window opens, in which all device parameters are displayed. Here the
                                   parameterization can be carried out, parameters can be loaded into or from the device
                                   or parameter values can be observed.

                                   NOTE
                                   Other functions are available in the context menu of the project icon. To do this, click
                                   on the button with the three dots at the upper right edge of the device tile to open the
                                   context menu.


7.3.2              SOPAS ET overview and standard functions on each page
                                   SIG200 pages have the following common layout:




8016629.1MCE/2024-10-24 | SICK                                        O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   35
Subject to change without notice

7 SIG200 CONFIGURATION

                                            56                                                                     7 1        2         3             8
                                    4

                                    ß
                                                                                                                                         9




                                     àá

                                    Figure 4: SOPAS ET layout


                                    1           Process data
                                    2           FIND ME function (not available for EtherNet/IP variant)
                                    3           RESTORE FACTORY SETTINGS: Reset to factory settings
                                    4           Menu
                                    5           Home
                                    6           STATUS
                                    7           Refresh page
                                    8           Edit mode
                                    9           Page contents
                                    ß           Page selection
                                    à           Notifications
                                    á           User mode

                                    The buttons located in the upper right portion of the interface provide global device
                                    configuration. These buttons will be present on every configuration page.

                                    Table 44: Functions
                                     EDIT                          The EDIT button allows the settings on a given configuration page to be
                                                                   changed.
                                                                   The EDIT button will be highlighted light blue when pressed. Pages that can
                                                                   be configured will be gray until the EDIT mode is activated.

                                                                   NOTE
                                                                   1.       Click on the Edit button (top right)
                                                                   2.       Click the RUN button (bottom left).
                                                                   3.       Change the operating mode from RUN to MAINTENANCE.
                                                                   4.       Insert the password "main"
                                                                   5.       Now the device parameterization can be changed.


                                                                   NOTE
                                                                   For the sake of device cybersecurity, changing the default password is
                                                                   strongly recommended.




36   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                     8016629.1MCE/2024-10-24 | SICK
                                                                                                                          Subject to change without notice

SIG200 CONFIGURATION 7


                                   Process data   The process data button provides the process data of the connected IO-Link
                                                  devices.




8016629.1MCE/2024-10-24 | SICK                                     O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   37
Subject to change without notice

7 SIG200 CONFIGURATION

                                     FIND ME function When this button is clicked, the MS LED next to the SIG200 POWER voltage
                                                      supply connection flashes at a frequency of 1 Hz until the button is clicked
                                                      again. This function can be used to identify devices that have already been
                                                      mounted.

                                                                   NOTE
                                                                   If the FIND ME function is active, no further interface navigation can take
                                                                   place until the STOP button has been clicked in the dialog.




                                     RESTORE FAC‐                  Clicking on this button the SIG200 will reset all settings to the factory
                                     TORY SETTINGS                 defaults. As a factory default, all ports are configured as digital inputs.
                                                                   Selection of the RESTORE FACTORY SETTINGS option must be confirmed again
                                                                   in the Confirm Action field.
                                                                   If you click Yes, all settings currently stored in the device are overwritten.
                                                                   After clicking OK, a Success dialog is displayed to confirm the successful
                                                                   reset of the connected SIG200 to the factory settings.

                                                                   NOTE
                                                                   While both of the dialogues boxes are active, no other interface navigation is
                                                                   possible.


                                                                   NOTE
                                                                   The Restore Factory Settings button works from any of the configuration
                                                                   pages.


                                                                   NOTE
                                                                   After resetting to factory settings with Restore Factory Settings, the IP address
                                                                   of the device is set to the default value.




38   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                         8016629.1MCE/2024-10-24 | SICK
                                                                                                                              Subject to change without notice

SIG200 CONFIGURATION 7


                                   HELP               The HELP button can be used to access a help page that is displayed on
                                                      each parameterization page on the right side of the user interface. Here
                                                      you will find additional information about the SIG200 relating to the current
                                                      page.
                                                      Please use for more detailed information always the operating manual. The
                                                      help texts does not include all information from the operating manual.

                                                      NOTE
                                                      The HELP screen remains open when you switch the parameterization page
                                                      via the tree view with parameterization pages.




                                   Menu               Click this button to show/hide the Page selection menu to make it easier to
                                                      navigate on smaller screens.

                                                      NOTE
                                                      The button is highlighted light blue when the device tree is hidden.

                                   Home               Click the Start button at any time to return to the STATUS device page.




                                   Refresh page       Clicking on this button the page contents are refreshed.



                                   Device informa‐    This area on the top left side of the page shows the product name, user-
                                   tion               defined location, firmware version, and serial number.




                                   Page contents      This area shows the selected page.
                                   SETTINGS           On the SETTINGS page, you can change the language and password.
                                   Device notifica‐   SIG200 device notifications will appear on the bottom of the screen. These
                                   tions              are informational only for configuration exchanges and errors. Each notifica‐
                                                      tion can be acknowledged by clicking on the entry.




8016629.1MCE/2024-10-24 | SICK                                          O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   39
Subject to change without notice

7 SIG200 CONFIGURATION

                                          RUN                           Click the RUN button to change the user access level from RUN (read-only)
                                                                        to MAINTENANCE. The default password is “main”. The device settings on
                                                                        the CONFIGURATION (parameterization), LOGIC EDITOR and SETTINGS pages can
                                                                        only be adjusted in MAINTENANCE mode.

                                                                        NOTE
                                                                        The device settings on the other pages are grayed out and cannot be
                                                                        adjusted until MAINTENANCE mode is activated.
                                                                        Please ensure that you have clicked on the Edit button on the top right
                                                                        corner as well if you would like to do any configurations.


7.3.2.1           User login and editing mode
                                         To change SIG200 settings, you must log in at the Maintenance user level (read and write
                                         access). By default, you are logged in at the Run (read-only) user level, where you can
                                         only view data and parameterization. If you want to change the user, click on the user
                                         icon at the bottom left of the page. Select the desired user name in the dialog. If a user
                                         other than “Run” is selected, the corresponding password must also be entered.
                                         If the Keep me logged in option is activated, the last user remains saved even if the
                                         parameterization tool (SOPAS ET or web browser) is closed.

                                         NOTE
                                         Saving the user in a web browser may depend on the cookie settings.

                                         The following table shows the available users and their initial password:
                                         Table 45: User / Passwords
                                          User                                            Initial password           Role
                                          Run                                             (none)                     Read configuration
                                          Maintenance                                     main                       Read and write configuration

                                         Please see "Settings", page 49 for details on changing passwords.

                                         NOTE
                                         As of firmware version 1.2.0, you are automatically prompted to change the password
                                         for the “Maintenance” user when logging in for the first time. Please remember this
                                         password. If you have changed and forgotten the password, contact SICK Service.

                                         If you click Login, you can also change the password of the logged-in user.

                                         NOTE
                                         In terms of cybersecurity of the device, changing the default password of the “Mainte‐
                                         nance” user is strongly recommended.


7.3.3             STATUS page




                                         The STATUS page is the home page for the SIG200. It provides an overview of the
                                         current module status and device function.




40        O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                      8016629.1MCE/2024-10-24 | SICK
                                                                                                                                Subject to change without notice

SIG200 CONFIGURATION 7




                                   Figure 5: Status page

                                   The page displays the parameterization of pin 2 (DI) and pin 4 (C/DI/DO) for each port.
                                   The LEDs in the SIG200 figure change their state depending on the current state of the
                                   connected device. The ports correspond to the IO link, input or output settings defined
                                   on the CONFIGURATION (parameterization) page. The port designations correspond to the
                                   user-defined port designations defined on the CONFIGURATION (parameterization) page.
                                   The POWER LED shown in the figure on the left is normally always green to indicate that
                                   the SIG200 is switched on.
                                   The Module Status (MS) and Network Status (NS) LED displays signal the EtherNet/IP
                                   status of the device.
                                   ACT/LINK1 + 2 indicate if there is Ethernet network connection on either port.

                                   NOTE
                                   Note that the LED displays do not work in real time. When the SIG200 is started for the
                                   first time, the device has an initialization time after switching on of approx. 70 seconds


7.3.4              IDENTIFICATION page




                                   The IDENTIFICATION page provides detailed information about the connected SIG200.
                                   These include the product name, serial number and firmware version.




8016629.1MCE/2024-10-24 | SICK                                        O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   41
Subject to change without notice

7 SIG200 CONFIGURATION

7.3.5             CONFIGURATION page (parameterization)




                                         Four tabs are displayed on the configuration page: Gateway, EtherNet/IP Settings, IO-Link
                                         Ports and IO-Link Devices.
                                         On the Gateway tab, the Ethernet settings such as the IP address or the subnet mask
                                         can be changed. In addition, EtherNet/IP identification data is displayed.
                                         The EtherNet/IP settings define the size and structure of the EtherNet/IP I/O data for
                                         the logic editor.
                                         On the IO-Link Ports tab, the port parameterization for ports S1 to S4 can be changed.
                                         In addition, an IODD file can be uploaded from your computer and assigned to one of
                                         the SIG200 ports (S1 to S4). Therefore, the IODD XML file and the referenced device
                                         image must be packed into a ZIP archive. This follows the same convention used by
                                         the IO-Link community (IODD Finder) and is the preferred method for retrieving the
                                         corresponding device IODDs. In addition, the single IODD can be uploaded as XML file.
                                         Other settings such as the minimum cycle time or the assignment of port designations
                                         can also be made on this page.
                                         On the IO-Link Devices tab there is a page for each IO-Link port (S1-S4). This tab
                                         displays the IODD view, device info and parameter data for each IO-Link device. The
                                         page visualization when an IODD was already uploaded to the user interface is different
                                         to the visualization of the IO-Link device without uploaded IODD file. For a more conven‐
                                         ient use it is recommended to upload the relevant IODD file for the IO-Link devices.




                                         Figure 6: CONFIGURATION page (parameterization)


7.3.5.1           Gateway
                                         The Ethernet settings can be configured on the Gateway tab.




42        O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                      8016629.1MCE/2024-10-24 | SICK
                                                                                                                Subject to change without notice

SIG200 CONFIGURATION 7




                                   Figure 7: CONFIGURATION page, gateway


                                   NOTE
                                   If the Ethernet settings are changed, device communication may be interrupted.


                                   NOTE
                                   A device power cycle is necessary to activate the ethernet parameter changes.


7.3.5.2            EtherNet/IP settings
                                   This tab provides several possibilities to configure the structure and size of I/O data to
                                   be exchanged between the PLC and the Logic Editor.
                                   The expected input and output size matches the Logic Editor process data size defined
                                   by the configuration assembly. In order to guarantee correct process data transfer, the
                                   expected size should correspond to the selection.
                                   The structure of the process data can be adjusted according to the application and
                                   logic by changing the Input and Output Data Configuration. This is important in terms of
                                   handling differnet data types in the logic editor.
                                   The input and output data can be labled individually to achieve a clearer wiring in the
                                   Logic Editor.




8016629.1MCE/2024-10-24 | SICK                                         O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   43
Subject to change without notice

7 SIG200 CONFIGURATION




                                         Figure 8: EtherNet/IP configuration




                                         Figure 9: Logic Editor


7.3.5.3           IO-Link ports
                                         On the IO-Link Ports tab, settings of the IO-Link ports that can be used in IO-Link or
                                         standard input/output mode can be configured.
                                         An IODD file can be uploaded here for easy parameterization of the connected IO-Link
                                         device. First upload an IODD file using the Upload IODD button. This IODD is then stored
                                         in the SIG200 Repository .
                                         The disk usage shows how much storage capability on SIG200 is available.
                                         After the correct IODD file has been uploaded, it can be assigned to the port to which
                                         the corresponding device is connected (e.g. port S1). To do this, select the IODD file on
                                         the right side of the table using the drop-down menu. All IODDs already in the Repository
                                         are displayed and the correct one can be selected. If an IODD is to be deleted from the
                                         device, select the desired IODD and click DELETE.
                                         After the desired IODD is selected, confirm by clicking the Apply button. The information
                                         from the IODD is now displayed on the IO-Link Devices tab.



44        O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                       8016629.1MCE/2024-10-24 | SICK
                                                                                                                 Subject to change without notice

SIG200 CONFIGURATION 7


                                   NOTE
                                   The upload of one IODD file takes a few minutes. Depending on the size of the specific
                                   IODD file the upload is faster or slower. It is not unusual in case the IODD upload needs
                                   1-5 minutes or longer untill the IODD is fully visualized in the user interface.




                                   Figure 10: CONFIGURATION page, IO-Link ports

                                   The port owner determines who can write process data outputs. This can be set to
                                   either fieldbus, REST or logic editor. When this setting is set to REST, no available
                                   process data outputs are displayed on the LOGIC EDITOR page.
                                   If the fieldbus is the port owner, the minimum process cycle time is as short as possible
                                   and cannot be changed because the port parameterization comes from the PLC.
                                   The Data Storage function can be configured for Restore or Backup + Restore according to
                                   the desired use case. If data storage is to be used, Expected Device ID and Expected Vendor
                                   ID must be set.

                                   NOTE
                                   If an IO-Link port has been configured, click Apply to change the parameterization.
                                   Otherwise, the parameterization will not be sent to the device.


                                   NOTE
                                   If Fieldbus (fieldbus) has been configured as the port owner, the parameterization is set
                                   by the PLC and cannot be changed via the user interface. The corresponding control
                                   surfaces are also grayed out in the Maintenance user level.


                                   NOTE
                                   The state of pin 2 is only mapped to the fieldbus processing data when the port owner
                                   is set to Fieldbus.


7.3.5.4            IO-Link devices
                                   IODD view
                                   The SIG200 user interface is manufacturer-independent and can be used to connect
                                   and visualize IO-Link devices with connection class A from any manufacturer.

8016629.1MCE/2024-10-24 | SICK                                          O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   45
Subject to change without notice

7 SIG200 CONFIGURATION

                                    The IO-Link devices tab displays the connected IO-Link devices on each port. Make sure
                                    that the correct port (S1 to S4) is selected at the top of the page and that the correct
                                    IODD has been uploaded and assigned to the port.
                                    The page is divided into three parts: Identification (left side), Process data (center) and
                                    Service data (right side).
                                    So this page allows the parametrization of the IO-Link device in an easy way in case a
                                    corresponding IODD file was uploaded before.

                                    NOTE
                                    This page needs some time for loading all IO-Link device data. There is no "loading"
                                    information appearing. It can happen that the visualization needs ~20 s or more untill
                                    all parameters are visualized.

                                    The following figure shows the view in case a corresponding IODD file for an IO-Link
                                    device was uploaded:




                                    Figure 11: CONFIGURATION page, IO-Link devices


                                    NOTE
                                    The correct IODD file must be uploaded and provided in the device configuration for this
                                    section to be displayed.

                                    The following figure shows the view if no IODD file is supplied; default IO-Link parame‐
                                    ters are visualized:




46   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                         8016629.1MCE/2024-10-24 | SICK
                                                                                                              Subject to change without notice

SIG200 CONFIGURATION 7




                                   Device Info
                                   Provides a device overview of any attached IO-Link device. This section will display the
                                   details of any attached IO-Link sensor regardless of port configuration.

                                   Parameter Data
                                   Use this section to issue individual IO-Link commands to the attached device.

                                   Data Storage
                                   Use the commands in this section for advanced management of an IO-Link devices
                                   data storage.
                                   Upload:
                                   If the IO-Link device is parameterized to Backup/Restore, this button is used to upload
                                   the device parameterization to the local data storage container of the SIG200. If the
                                   IO-Link device is parameterized to Restore, this button deletes the contents of the port
                                   data storage container and reinitializes the port.




8016629.1MCE/2024-10-24 | SICK                                        O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   47
Subject to change without notice

7 SIG200 CONFIGURATION


                                       NOTE
                                       Be aware that the current configuration is deleted and replaced with the new configura‐
                                       tion from the IO-Link device.

                                       Download / Import / Export:
                                       Export and Import allow you to copy the contents of a port data storage container from
                                       one SIG200 to a second SIG200. Once the contents of the data memory have been
                                       imported into the second SIG200, they can be downloaded to the connected IO-Link
                                       device.

                                       NOTE
                                       If the individual underside for the ports remains empty, then either no IO-Link device is
                                       physically connected to the SIG200 or the connected device is not an IO-Link device.


7.3.6           LOGIC EDITOR page (logic editor)




                                       Figure 12: LOGIC EDITOR page (logic editor)

                                       The LOGIC EDITOR page of SIG200 allows you to apply user-defined logic functions to the
                                       available input signals and transmit the results to various output signals by dragging
                                       and dropping logic blocks and connection cables.
                                       The left side of the screen lists all configured inputs. The upper middle bar contains the
                                       available logic gates that can be dragged down into the workspace. And listed on the
                                       right side are the configured outputs.
                                       Before setting up any logic, it is required to upload the relevant IODD files. This ensures
                                       that the correct inputs and outputs of every connected IO-Link device are displayed
                                       correctly.

                                       NOTE
                                       Note that the screen is grayed out until you change to editing mode (see "User login and
                                       editing mode", page 40).

                                       Creating a logic system
                                       1.       To select the desired logic blocks, click and drag them to the working range.

48      O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                        8016629.1MCE/2024-10-24 | SICK
                                                                                                                Subject to change without notice

SIG200 CONFIGURATION 7


                                        NOTE
                                        If a logic block has been selected incorrectly, or needs to be removed, click on it
                                        and drag it back up to the selection bar. A garbage bin will appear to remove the
                                        selected logic gate from the workspace.

                                   2.   Making connections from the inputs to the logic gates: Click on the desired input,
                                        click again and mark the arrow. A connecting line is then created. Note that you
                                        can drag the line to a desired logic gate input.
                                        As you approach, the logic gate inputs expand to accommodate the connection
                                        cable. As soon as the connection is made, the bends (if there are bends along the
                                        connection), the position of the logic gate and the window size can be adjusted.
                                        The connection is scaled automatically. An incorrect connection can be deleted by
                                        clicking and holding the connecting line. A wastebasket icon is displayed at the top
                                        center of the user interface.
                                        Some logic blocks require at least two input signals.
                                        Note that the inputs must always be assigned from top to bottom (e.g. for two
                                        inputs A+B and not A+D).
                                        The inputs are outlined in red when connections are made to indicate that a
                                        connection is still required in this area. The two inputs C and D are only active in
                                        the logical truth table if a connection has been made.
                                        NOTE
                                        Green input arrows and green text: a connection is possible
                                        If a connection is not possible, the text will have red color and it is not possible to
                                        drag a connection to the input.


                                        NOTE
                                        Some inputs and logic gates have a small gear indicating that some additional set‐
                                        tings are possible. Clicking on the gear will open the additional settings dialogue
                                        box and allow for additional configuration (e. g. delay time).

                                   3.   Clomplete the setup by using the Transfer and Execute Flow button: the new logic
                                        configuration is transfered to the connected SIG200.



                                        NOTE
                                        An error will appear if there are any improper or missing connections. The notifica‐
                                        tion area will indicate a successful transfer.




7.3.7              Settings




                                   The following settings are possible:
                                   Setting                                              Possible values
                                   Language                                             english / german




8016629.1MCE/2024-10-24 | SICK                                         O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   49
Subject to change without notice

7 SIG200 CONFIGURATION




                                    Figure 13: Settings

                                    The language of the user interface can be selected on the SETTINGS page (German or
                                    English).
                                    Also, if logged in as any user except “Run” (see "User login and editing mode", page 40),
                                    it is possible to change the password for the logged in user.




                                    For security reasons, changing the original default password is strongly recommended.
                                    As of firmware version 1.2.0, you are automatically prompted to change the password
                                    for the “Maintenance” user when logging in for the first time.
                                    If you have changed and forgotten the password please contact SICK service for sup‐
                                    port.

50   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                    8016629.1MCE/2024-10-24 | SICK
                                                                                                         Subject to change without notice

SIG200 CONFIGURATION 7


7.4                Configuration via REST API
                                   The SIG200 provides a REST API with JSON data format for accessing the data of the
                                   connected devices.

                                   NOTE
                                   Since firmware version 1.3, the SIG200 has also featured the JSON REST interface
                                   defined by the IO-Link community in addition to the SICK-specific REST API interface.
                                   This is specified in the document “JSON Integration for IO-Link” in version 1.0.0 (Mar
                                   2020 Order No: 10.222).

                                   These operating instructions provide an overview of the available device functions and
                                   the access mechanisms.

7.4.1              General Interface description
                                   The REST API is a client – server interface and enables the client to request data from
                                   the server through a defined set of resources. The REST API is stateless which means
                                   that no information about the state of connection and no information about the server
                                   or client are required.
                                   The operation is based on HTTP methods. Common HTTP methods are GET, POST, PUT
                                   and DELETE. JSON, or JavaScript Object Notation, is a minimal, visually readable format
                                   for structuring data. It is mainly used to transmit data between a server and a web
                                   application as an alternative to XML.
                                   Table 46: Overview
                                   Interface                                          see "Interface", page 63
                                   GET/apiversion                                     see "GET/apiversion", page 63
                                   GET/openapi                                        see "GET/openapi", page 63
                                   gateway                                            see "gateway", page 64
                                   GET/gateway/identification                         see "GET/gateway/identification", page 64
                                   GET/gateway/capabilities                           see "GET/gateway/capabilities", page 64
                                   GET/gateway/configuration                          see "GET/gateway/configuration", page 64
                                   POST/gateway/configuration                         see "POST/gateway/configuration", page 64
                                   GET/gateway/events                                 see "GET/gateway/events", page 65
                                   POST/gateway/reboot                                see "POST/gateway/reboot", page 66
                                   POST/gateway/reset                                 see "POST/gateway/reset", page 66
                                   IODDs                                              see "IODDs", page 67
                                   GET/iodds                                          see "GET/iodds", page 67
                                   GET/iodds/file                                     see "GET/iodds/file", page 67
                                   POST/iodds/file                                    see "POST/iodds/file", page 68
                                   DELETE/iodds                                       see "DELETE/iodds", page 68
                                   Masters                                            see "Masters", page 68
                                   GET/masters                                        see "GET/masters", page 68
                                   GET/masters / 1/capabilities                       see "GET/masters / 1/capabilities", page 68
                                   GET/masters / 1/identification                     see "GET/masters / 1/identification",
                                                                                      page 69
                                   POST/masters / 1/identification                    see "POST/masters / 1/identification",
                                                                                      page 69
                                   Ports                                              see "Ports", page 69
                                   GET/masters / 1/ports                              see "GET/masters / 1/ports", page 69


8016629.1MCE/2024-10-24 | SICK                                       O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   51
Subject to change without notice

7 SIG200 CONFIGURATION

                                     GET/masters / 1/ports/{portNumber}/capabil‐ see "GET/masters / 1/ports/{portNum‐
                                     ities                                       ber}/capabilities", page 70
                                     GET/masters / 1/ports/{portNumber}/status       see "GET/masters / 1/ports/{portNum‐
                                                                                     ber}/status", page 70
                                     GET/masters / 1/ports/{portNumber}/configu‐ see "GET/masters / 1/ports/{portNum‐
                                     ration                                      ber}/configuration", page 71
                                     POST/masters / 1/ports/{portNumber}/config‐ see "POST/masters / 1/ports/{portNum‐
                                     uration                                     ber}/configuration", page 71
                                     GET/masters / 1/ports/{portNumber}/data‐        see "GET/masters / 1/ports/{portNum‐
                                     storage                                         ber}/datastorage", page 72
                                     POST/masters / 1/ports/{portNumber}/data‐       see "POST/masters / 1/ports/{portNum‐
                                     storage                                         ber}/datastorage", page 72
                                     Devices                                         see "Devices", page 72
                                     GET/devices                                     see "GET/devices", page 72
                                     GET/devices/{deviceAlias}/capabilities          see "GET/devices/{deviceAlias}/capabilities",
                                                                                     page 73
                                     GET/devices/{deviceAlias}/identification        see "GET/devices/{deviceAlias}/identification",
                                                                                     page 73
                                     POST/devices/{deviceAlias}/identification       see "POST/devices/{deviceAlias}/identifica‐
                                                                                     tion", page 73
                                     GET/devices/{deviceAlias}/events                see "GET/devices/{deviceAlias}/events",
                                                                                     page 74
                                     GET/devices/{deviceAlias}/processdata/value     see "GET/devices/{deviceAlias}/process‐
                                                                                     data/value", page 74
                                     GET/devices/{deviceAlias}/processdata/get‐      see "Devices"
                                     data/value
                                     GET/devices/{deviceAlias}/processdata/set‐      see "GET/devices/{deviceAlias}/process‐
                                     data/value                                      data/setdata/value", page 75
                                     POST/devices/{deviceAlias}/process‐             see "POST/devices/{deviceAlias}/process‐
                                     data/value                                      data/value", page 77
                                     GET/devices/{deviceAlias}/parame‐               see "GET/devices/{deviceAlias}/parame‐
                                     ters/{index}/value                              ters/{index}/value", page 77
                                     POST/devices/{deviceAlias}/parame‐              see "POST/devices/{deviceAlias}/parame‐
                                     ters/{index}/value                              ters/{index}/value", page 77
                                     GET/devices/{deviceAlias}/parame‐               see "GET/devices/{deviceAlias}/parame‐
                                     ters/{index}/subindices                         ters/{index}/subindices", page 77
                                     GET/devices/{deviceAlias}/parame‐               see "GET/devices/{deviceAlias}/parame‐
                                     ters/{index}/subindices/{subindex}/value        ters/{index}/subindices/{subindex}/value",
                                                                                     page 77
                                     POST/devices/{deviceAlias}/parame‐              see "POST/devices/{deviceAlias}/parame‐
                                     ters/{index}/subindices/{subindex}/value        ters/{index}/subindices/{subindex}/value",
                                                                                     page 77
                                     GET/devices/{deviceAlias}/parameters            see "GET/devices/{deviceAlias}/parameters",
                                                                                     page 78
                                     GET/devices/{deviceAlias}/parame‐               see "GET/devices/{deviceAlias}/parame‐
                                     ters/{parameterName}/value                      ters/{parameterName}/value", page 79
                                     POST/devices/{deviceAlias}/parame‐              see "POST/devices/{deviceAlias}/parame‐
                                     ters/{parameterName}/value                      ters/{parameterName}/value", page 79
                                     GET/devices/{deviceAlias}/parame‐               see "GET/devices/{deviceAlias}/parame‐
                                     ters/{parameterName}/subindices                 ters/{parameterName}/subindices", page 79




52   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                            8016629.1MCE/2024-10-24 | SICK
                                                                                                                 Subject to change without notice

SIG200 CONFIGURATION 7


                                   GET/devices/{deviceAlias}/parame‐                   see "GET/devices/{devi‐
                                   ters/{parameterName}/subindices/{subPara‐           ceAlias}/parameters/{parameterName}/subin‐
                                   meterName}/value                                    dices/{subParameterName}/value", page 80
                                   POST/devices/{deviceAlias}/parame‐                  see "POST/devices/{devi‐
                                   ters/{parameterName}/subindices/{subPara‐           ceAlias}/parameters/{parameterName}/subin‐
                                   meterName}/value                                    dices/{subParameterName}/value", page 80


7.4.2              API basics
                                   The API itself is accessible under the following address:
                                   http://[Host Name]/[Namespace]/[Variable | Method]?[QueryParameter]
                                   Host Name: IP or hostname of the device
                                   Namespace: Namespace ID for the function
                                    The namespace to access the standard JSON REST is done via "iolink/v1/{domain}".
                                   The version of the interface to be used is already included there. Another component
                                   of the namespace is the {domain}. This allows access to certain parameter groups, see
                                   "Description of JSON REST", page 57.
                                   The SICK-specific namespace is “api” or “iolink/sickv1/”.
                                   Variable: Name of the variable to be read or set
                                   Method: Name of the method to be called
                                   QueryParameter: Name or combination of names to parameterize the query (e.g. filtering
                                   of return data).
                                   http://[Host Name]/api/[Namespace Name]/[Variable | Method]

                                   NOTE
                                   The available variables, methods, and namespaces are listed below.


7.4.3              Requests
                                   The SIG200 supports request types GET and POST.
                                   GET is used to read variables (without parameters).
                                   POST is used to read and write variables and call methods.
                                   All API calls are executed synchronously. This means that every request is followed by a
                                   response. This contains the requested data and additional status information.
                                   Type: GET | POST
                                   URL http://device/api/variable
                                   MIME-Type: application/json
                                   Payload: <empty> | variable | parameter
                                   The type of request depends on the use case, as described in the following table:
                                   Table 47: Request types
                                   Use case                                            Request type
                                   Read data                                           GET
                                   Write data                                          POST
                                   Method call                                         POST
                                   Login                                               POST
                                   Data deletion                                       DELETE




8016629.1MCE/2024-10-24 | SICK                                        O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   53
Subject to change without notice

7 SIG200 CONFIGURATION

                                    Values or method parameters must be included in a data object and passed as a JSON
                                    string within the POST request user data as follows:
                                    {
                                           "data":
                                           {
                                              "name": value
                                           }
                                    }
                                    The exact format of the variables and parameters is described in section Data Types.

                                    NOTE
                                    Please make sure to use application/json as the mime-type.


                                    NOTE
                                    The HTTP request user data should be empty if a method has no parameters.

                                    Get variable
                                    The variable named "angle" shall be read:
                                    Type: GET
                                    URL http://device/api/angle
                                    Payload: <empty>

                                    Set variable
                                    The variable named "angle" shall be set to 42:
                                    Type: POST
                                    URL: http://device/api/angle
                                    MIME-Type: application/json
                                    Payload:
                                    {
                                           "data":
                                           {
                                              "angle": 42
                                           }
                                    }

                                    Call method
                                    The setDeviceState(state) method is to be called with a parameter value of 42:
                                    Type: POST
                                    URL: http://device/api/setDeviceState
                                    MIME-Type: application/json
                                    Payload:
                                    {
                                           "data":
                                           {
                                              "state": 42
                                           }
                                    }


54   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                     8016629.1MCE/2024-10-24 | SICK
                                                                                                          Subject to change without notice

SIG200 CONFIGURATION 7


7.4.4              Response
                                   The device responds to each request with either status information and data or only
                                   status information if no data is available. In case of an error, it returns a non-zero status
                                   code and an optional error description. These return values are transmitted within the
                                   user data of the HTTP response.
                                   {
                                          "header":
                                          {
                                             "status": status code,
                                             "message": status code description
                                          },
                                          "data":
                                          {
                                             "name" : value
                                          }
                                   }

                                   NOTE
                                   If a method has no return value there will be no data inside the payload of the HTTP
                                   Response.

                                   The status codes and error messages depend on the corresponding REST API and are
                                   described in detail in see "Description of JSON REST", page 57 and see table 57,
                                   page 80.

                                   NOTE
                                   No specific response time is guaranteed, as HTTP requests are based on a standard
                                   TCP mechanism. When using the web UI or SOPAS ET at the same time, the response
                                   time increases.


7.4.5              Data Types
                                   In this chapter each supported Data Type will be discussed. Please note that each
                                   example is nested inside a JSON object. The first value, wrapped in double quotes,
                                   represents the name and the second one the actual value.
                                   Boolean
                                   {
                                          "booleanName": true | false
                                   }
                                   Numbers
                                   A number is very much like a C or Java number, except that the octal and hexadecimal
                                   formats are not used.
                                   {
                                          "numberName": 32
                                   }
                                   The following table describes the ranges of each numeric type which this API supports:
                                   Table 48: Numeric types
                                   Name of Type       Range                                            Description
                                   SInt               -128 … 127                                       8 bit signed
                                   Int                -32768 … 32767                                   16 bit signed



8016629.1MCE/2024-10-24 | SICK                                         O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   55
Subject to change without notice

7 SIG200 CONFIGURATION

                                     Name of Type                  Range                       Description
                                     Dint                          - 2147483648 … 2147483647   32 bit signed
                                     USInt                         0 … 255                     8 bit unsigned
                                     UInt                          0 … 65535                   16 bit unsigned
                                     UDInt                         0… 4294967295               32 bit unsigned
                                     Real                          IEEE Standard 754 single    By default only 9 digits behind the
                                                                                               comma will be transmitted
                                     LReal                         IEEE Standard 754 double    By default only 18 digits behind the
                                                                                               comma will be transmitted

                                    Boolean
                                    Boolean values can assume two states. Either true or false.
                                    {
                                            "ioddSupported": true
                                    }
                                    String
                                    A string is a sequence of zero or more Unicode characters, wrapped in double quotes,
                                    using backslash escapes. A character is represented as a single character string.
                                    {
                                            "stringName": "value"
                                    }
                                    value = any UNICODE character except " , \ , or control character. Escaped unicode
                                    characters are not supported.
                                    Enum
                                    Enums are numerical types which define a number of values. All other values are not
                                    permitted and will be excluded.
                                    {
                                            "enumName": ordinal number
                                    }
                                    ordinal number = USInt | UInt
                                    Array
                                    An array is an ordered collection of values. An array begins with [ (left bracket) and
                                    ends with ] (right bracket). Values are separated by , (comma).
                                    {
                                            "arrayName": [value, value, …, value]
                                    }
                                    value = boolean | number | string | array | struct | enum
                                    An Array with a length of 0 will be transmitted as an empty Array:
                                    {
                                            "arrayName": []
                                    }
                                    Struct
                                    A struct is an unordered set of name/value pairs. An object begins with { (left brace)
                                    and ends with } (right brace). Each name is followed by : (colon) and the name/value
                                    pairs are separated by , (comma).
                                    {
                                            "structName":


56   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                             8016629.1MCE/2024-10-24 | SICK
                                                                                                                  Subject to change without notice

SIG200 CONFIGURATION 7


                                       {
                                            "memberOneName": value,
                                            "memberOneName": value
                                       }
                                   }
                                   value = boolean | number | string | array | struct | enum

                                   NOTE
                                   It is possible to partially write a struct. That means it's possible to write for example only
                                   one member of a struct by just transmitting only this one value and omitting the other
                                   struct members.


                                   NOTE
                                   The order in which the members are transmitted doesn't matter.


7.4.6              Description of JSON REST
                                   The description of the API can also be read out directly from the device, see GET/
                                   openapi. The output is an OpenAPI description in JSON format and maps the interface
                                   implemented in the device. This should be the preferred method, as it ensures compati‐
                                   bility with the device and is also in machine-readable format.

7.4.6.1            Error messages
                                   Table 49: JSON REST general error messages
                                   HTTP        Message        Description
                                   code
                                   500         Internal       {
                                               Server Error       "code": 101,
                                                                  "message": "Internal server error"
                                                              }

                                                              NOTE
                                                              This error can occur with any request.

                                                              {
                                                                  "code": 102,
                                                                  "message": "Internal communication error"
                                                              }
                                   404         Not Found      {
                                                                  "code": 103,
                                                                  "message": "Operation not supported"
                                                              }

                                                              NOTE
                                                              This error is returned if the requested function does not exist.

                                   400         Bad Request {
                                                                  "code": 104,
                                                                  "message": "Action locked by another client"
                                                              }

                                                              NOTE
                                                              Fieldbus controller or another participant blocks access




8016629.1MCE/2024-10-24 | SICK                                           O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   57
Subject to change without notice

7 SIG200 CONFIGURATION

                                     HTTP              Message                Description
                                     code
                                     501               Not imple‐             {
                                                       mented                        "code": 105,
                                                                                     "message": "IODD feature not supported"
                                                                              }
                                                                              {
                                                                                     "code": 106,
                                                                                     "message": "MQTT feature not supported"
                                                                              }
                                     403               Forbidden              {
                                                                                     "code": 150,
                                                                                     "message": "Permission denied"
                                                                              }

                                                                              NOTE
                                                                              Access is not allowed. Check access rights and Port Owner in configu‐
                                                                              ration. This error can occur with any request.




58   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                          8016629.1MCE/2024-10-24 | SICK
                                                                                                                               Subject to change without notice

SIG200 CONFIGURATION 7


                                   Table 50: JSON parsing error messages
                                   HTTP       Message       Description
                                   code
                                   400        Bad Request {
                                                                "code": 201,
                                                                "message": "JSON parsing failed"
                                                            }

                                                            NOTE
                                                            The sent JSON object could not be interpreted correctly. Check the
                                                            JSON object in the Payload data.

                                                            {
                                                                "code": 202,
                                                                "message": "JSON data value invalid"
                                                            }

                                                            NOTE
                                                            The data in the sent JSON object is not correct (for example: format
                                                            of the IP address).

                                                            {
                                                                "code": 203,
                                                                "message": "JSON data type invalid"
                                                            }

                                                            NOTE
                                                            The data type in the sent JSON object is not correct (for example:
                                                            String instead of Integer).

                                                            {
                                                                "code": 204,
                                                                "message": "Enumeration value unknown"
                                                            }
                                                            {
                                                                "code": 205,
                                                                "message": "JSON data value out of range"
                                                            }

                                                            NOTE
                                                            The parameter is out of the valid value range. Check the correspond‐
                                                            ing default.

                                                            {
                                                                "code": 206,
                                                                "message": "JSON data value out of bounds"
                                                            }

                                                            NOTE
                                                            The maximum array/string length is exceeded.

                                                            {
                                                                "code": 207,
                                                                "message": "deviceAlias is not unique"
                                                            }
                                                            {
                                                                "code": 208,
                                                                "message": "POST request without content"
                                                            }

8016629.1MCE/2024-10-24 | SICK                                         O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   59
Subject to change without notice

7 SIG200 CONFIGURATION

                                    Table 51: Access error
                                     HTTP              Message                Description
                                     code
                                     404               Not Found              {
                                                                                     "code": 301,
                                                                                     "message": "Resource not found"
                                                                              }

                                                                              NOTE
                                                                              This error can occur with any request that contains parameters in the
                                                                              URL.

                                                                              {
                                                                                     "code": 302,
                                                                                     "message": "masterNumber not found"
                                                                              }
                                                                              {
                                                                                     "code": 303,
                                                                                     "message": "portNumber not found"
                                                                              }
                                                                              {
                                                                                     "code": 304,
                                                                                     "message": "deviceAlias not found"
                                                                              }
                                                                              {
                                                                                     "code": 305,
                                                                                     "message": "Query parameter name invalid"
                                                                              }
                                                                              {
                                                                                     "code": 306,
                                                                                     "message": "Query parameter value invalid"
                                                                              }
                                                                              {
                                                                                     "code": 307,
                                                                                     "message": "Port is not configured to IO-Link"
                                                                              }
                                                                              {
                                                                                     "code": 308,
                                                                                     "message": "IO-Link Device is not accessible"
                                                                              }
                                                                              {
                                                                                     "code": 309,
                                                                                     "message": "IO-Link parameter not found"
                                                                              }
                                                                              {
                                                                                     "code": 310,
                                                                                     "message": "IO-Link parameter access not
                                                                                     supported by the Device"
                                                                              }
                                                                              {
                                                                                     "code": 311,
                                                                                     "message": "IO-Link parameter access error"
                                                                              }
                                                                              {
                                                                                     "code": 312,
                                                                                     "message": "IO-Link parameter name is not
                                                                                     unique"
                                                                              }
60   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                         8016629.1MCE/2024-10-24 | SICK
                                                                                                                              Subject to change without notice

SIG200 CONFIGURATION 7


                                   Table 52: Data storage error
                                   HTTP        Message       Description
                                   code
                                   400         Bad Request {
                                                                  "code": 401,
                                                                  "message": "Data storage mismatch"
                                                             }

                                                             NOTE
                                                             The Data Storage object is not compatible with the connected IO-Link
                                                             device.

                                   Table 53: Process data error
                                   HTTP        Message       Description
                                   code
                                   400         Bad Request {
                                                                  "code": 501,
                                                                  "message": "I/Q is not configured as
                                                                  DIGITAL_OUTPUT"
                                                             }
                                                             {
                                                                  "code": 502,
                                                                  "message": "C/Q is not configured as
                                                                  DIGITAL_OUTPUT"
                                                             }
                                                             {
                                                                  "code": 503,
                                                                  "message": "IO-Link device has no output
                                                                  process data"
                                                             }




8016629.1MCE/2024-10-24 | SICK                                         O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   61
Subject to change without notice

7 SIG200 CONFIGURATION

                                    Table 54: IODD error
                                     HTTP              Message                Description
                                     code
                                     400               Bad Request {
                                                                                     "code": 601,
                                                                                     "message": "IODD (representation) is not
                                                                                     available"
                                                                              }

                                                                              NOTE
                                                                              No compatible IODD found. Upload a suitable IODD.

                                                                              {
                                                                                     "code": 603,
                                                                                     "message": "IODD upload failed: IODD XML
                                                                                     invalid"
                                                                              }

                                                                              NOTE
                                                                              The uploaded IODD contains XML errors. Upload only suitable IODD
                                                                              files.

                                                                              {
                                                                                     "code": 604,
                                                                                     "message": "IODD upload failed: CRC error"
                                                                              }
                                                                              {
                                                                                     "code": 605,
                                                                                     "message": "IODD upload failed: parsing error"
                                                                              }
                                     500               Internal               {
                                                       Server Error                  "code": 602,
                                                                                     "message": "IODD upload failed: not enough
                                                                                     memory"
                                                                              }




62   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                       8016629.1MCE/2024-10-24 | SICK
                                                                                                                            Subject to change without notice

SIG200 CONFIGURATION 7


                                   Table 55: Data error
                                   HTTP        Message       Description
                                   code
                                   400         Bad Request {
                                                                 "code": 701,
                                                                 "message": "Data set incomplete"
                                                             }
                                                             {
                                                                 "code": 702,
                                                                 "message": "Data set not applicable"
                                                             }

                                                             NOTE
                                                             The complete sent data set is discarded.

                                                             {
                                                                 "code": 703,
                                                                 "message": "Data set combination incompatible"
                                                             }

                                                             NOTE
                                                             The complete sent data set is discarded.


                                   NOTE
                                   Only the first error is returned if a request contains multiple errors.


7.4.6.2            Interface
                                   GET/apiversion
                                   Readout of API version.
                                   Sample response:
                                   {
                                         "version": "V1.0.0"
                                   }

                                   GET/openapi
                                   Reading of interface in OpenAPI JSON format.
                                   Sample response:
                                   {
                                         "openapi": "3.0.1",
                                         "info": {
                                            "description": "This is the description of the SIG200 IO-
                                            Link Master REST API server….",
                                            "version": "1.0.0",
                                            "title": "SIG200 IO-Link Master",
                                            "contact": {
                                                "email": "info@sick.de"
                                   },
                                         "license": {
                                            "name": "Apache 2.0",
                                            "url": "http://www.apache.org/licenses/LICENSE-2.0.html"
                                         }
                                   }
                                   ...



8016629.1MCE/2024-10-24 | SICK                                         O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   63
Subject to change without notice

7 SIG200 CONFIGURATION

7.4.6.3           gateway
                                         GET/gateway/identification
                                         Readout of identification information.
                                         Sample response:
                                          {
                                                  "macAddress": "00:06:77:00:00:00",
                                                  "serialNumber": "12345678",
                                                  "productId": "1234567",
                                                  "vendorName": "SICK AG",
                                                  "productName": "SIG200-0A0G12200",
                                                  "hardwareRevision": "V1.0.0",
                                                  "firmwareRevision": "1.3.0.0B"
                                          }

                                         GET/gateway/capabilities
                                         Information about device function.
                                          JSON parameters Type                            Description
                                          ioddSupporte Boolean                            Describes the general support for IODD files. This
                                          d                                               includes uploading IODDs and allows parameter access
                                                                                          via variable names. In addition, it offers the advantage
                                                                                          that values are output directly in the appropriate format.
                                          mqttSupporte Boolean                            Describes the general support of MQTT.
                                          d

                                         Sample response:
                                          {
                                                  "ioddSupported": true,
                                                  "mqttSupported": false
                                          }

                                         GET/gateway/configuration

                                         POST/gateway/configuration
                                         Reading and writing the device configuration or Ethernet settings.
                                          JSON parameters Type                            Description
                                          ipConfigurat Enum                               Describes the general support for IODD files. This
                                          ion          [“DHCP”/ “MAN‐                     includes uploading IODDs and allows parameter access
                                                       UAL”]                              via variable names. In addition, it offers the advantage
                                                                                          that values are output directly in the appropriate format.

                                         Sample request:




64        O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                     8016629.1MCE/2024-10-24 | SICK
                                                                                                                               Subject to change without notice

SIG200 CONFIGURATION 7


                                   {
                                         "ethIpv4": [
                                         {
                                            "ipConfiguration": "DHCP",
                                            "ipAddress": "192.168.0.50",
                                            "subnetMask": "255.255.255.0",
                                            "standardGateway": "0.0.0.0"
                                                "email": "info@sick.de"
                                   },
                                         "license": {
                                            "name": "Apache 2.0",
                                            "url": "http://www.apache.org/licenses/LICENSE-2.0.html"
                                            }
                                         ]
                                   }

                                   GET/gateway/events
                                   Readout of events that have occurred.
                                   Query parame‐      Type              Description
                                   ters
                                   origin             String            ALL: Output of all events.
                                                                        GATEWAY: Only outputs gateway events.
                                                                        PORTS: Only outputs port events. Requires specification
                                                                        of partNumber.
                                                                        DEVICES: Only outputs device events. Requires specifica‐
                                                                        tion of deviceAlias.
                                   portNumber         Integer           Only events of the specified port are output.
                                   deviceAlias        String            Only events of the device with the specified deviceAlias
                                                                        are displayed.
                                   top                Integer           Filter to output only the first events after switching on
                                                                        the supply voltage.
                                   bottom             Integer           Filter to output only the most recent events in time.

                                   Example of namespace with query parameters
                                   http://192.168.2.1/iolink/v1/gateway/events?
                                   origin=DEVICES&deviceAlias=master1port1
                                   http://192.168.2.1/iolink/v1/gateway/events?origin=ALL&bottom=1
                                   http://192.168.2.1/iolink/v1/gateway/events?
                                   origin=PORTS&portNumber=1&top=5

                                   JSON parameters Type                 Description
                                   time               Time              Time of the occurred event since switching on the supply
                                                                        voltage in the format [dd:hh:mm:ss.ms].
                                   severity           Enum [“EMER‐     Category of the event.
                                                      GENCY” /”ALERT”
                                                      /”CRITI‐
                                                      CAL” /”ERROR” /
                                                      “WARN‐
                                                      ING” /”NOTICE” /
                                                      ”INFO” /”DEBUG”
                                                      ]

                                   Sample response:




8016629.1MCE/2024-10-24 | SICK                                        O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   65
Subject to change without notice

7 SIG200 CONFIGURATION

                                     [
                                             {
                                                "time": "00:02:41:51.417",
                                                "severity": "NOTICE",
                                                "message": {
                                                    "code": 65319,
                                                    "mode": "SINGLESHOT",
                                                    "text": "Data Storage upload completed and new data
                                                    object available"
                                                },
                                             "origin": {
                                                "portNumber": 1,
                                                "masterNumber": 1
                                                }
                                             },
                                             {
                                                "ti
                                                me"
                                                :
                                                "00
                                                :02
                                                :41
                                                :51
                                                .44
                                                3",
                                                "se
                                                ver
                                                ity
                                                ":
                                                "NO
                                                TIC
                                                E",
                                                "me
                                                ssa
                                                ge"
                                                : {
                                                    "code": 65313,
                                                    "mode": "SINGLESHOT",
                                                    "text": "Device plugged in"
                                                },
                                                "or
                                                igi
                                                n":
                                                {
                                                    "portNumber": 1,
                                                    "masterNumber": 1
                                                }
                                             }
                                     ]

                                    POST/gateway/reboot
                                    This command restarts the device and is only acknowledged by the HTTP code "204".

                                    POST/gateway/reset
                                    The device is set to the delivery state.

                                    NOTE
                                    By executing the device reset, all settings are lost or replaced by the default values.




66   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                      8016629.1MCE/2024-10-24 | SICK
                                                                                                           Subject to change without notice

SIG200 CONFIGURATION 7


7.4.6.4            IODDs
                                   GET/iodds
                                   Readout of all IODDs located on the device.
                                   Query parame‐      Type               Description
                                   ters
                                   vendorId           Integer            Output of the IODDs available on the device with the
                                                                         specified vendor ID.
                                   deviceId           Integer            Output of the IODDs available on the device with the
                                                                         specified device ID.
                                   revision           Enum               Output of the IODDs available on the device with the
                                                      [“1.0”/ “1.1”]     specified revision.

                                   Namespace example with query parameters
                                   http://192.168.2.1/iolink/v1/iodds?vendorId=26&deviceId=8389227
                                   http://192.168.2.1/iolink/v1/iodds?revision=1.1

                                   Sample response:
                                   [
                                        {
                                             "vendorId": 26,
                                             "deviceId": 8389010,
                                             "version": "V1.04",
                                             "releaseDate": "2018-07-17",
                                             "iolinkRevision": "1.1"
                                        },
                                        {
                                             "vendorId": 26,
                                             "deviceId": 8389238,
                                             "version": "V0.1",
                                             "releaseDate": "2020-11-19",
                                             "iolinkRevision": "1.1"
                                        },
                                   ]

                                   GET/iodds/file
                                   Read out the IODD file specified by the query parameters. Vendor and Device ID are
                                   required here.
                                   Namespace example with query parameters:
                                   http://192.168.2.1/iolink/v1/iodds/file?
                                   vendorId=26&deviceId=8389010

                                   Sample response:




8016629.1MCE/2024-10-24 | SICK                                         O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   67
Subject to change without notice

7 SIG200 CONFIGURATION

                                          <?xml version="1.0" encoding="UTF-8"?>
                                          <!-- edited with SICK IODD editor 3.0.0.1170R -->
                                          <IODevice
                                              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                              xmlns="http://www.io-link.com/IODD/2010/10"
                                                 xsi:schemaLocation="http://www.io-link.com/IODD/2010/10
                                                 IODD1.1.xsd">
                                              <DocumentInfo copyright="Copyright 2017, SICK AG"
                                                 releaseDate="2018-07-17"
                                                 version="V1.04"/>
                                              <ProfileHeader>
                                                 <ProfileIdentification>IO Device Profile</
                                                 ProfileIdentification>
                                                 <ProfileRevision>1.1</ProfileRevision>
                                                 <ProfileName>Device Profile for IO Devices</ProfileName>
                                                 <ProfileSource>IO-Link Consortium</ProfileSource>
                                                 <ProfileSource>IO-Link Consortium</ProfileSource>
                                                 <ProfileClassID>Device</ProfileClassID>
                                                 <ISO15745Reference>
                                                     <ISO15745Part>1</ISO15745Part>
                                                     <ISO15745Edition>1</ISO15745Edition>
                                                     <ProfileTechnology>IODD</ProfileTechnology>
                                                 </ISO15745Reference>
                                              </ProfileHeader>
                                          ... <ProfileBody>

                                         POST/iodds/file
                                         Upload and save an IODD file to the device. The file must conform to the IODD schema
                                         and be in XML format.

                                         DELETE/iodds
                                         Delete all IODD files or an IODD file specified by the query parameters.
                                         Namespace example with query parameters:
                                          http://192.168.2.1/iolink/v1/iodds
                                          http://192.168.2.1/iolink/v1/iodds?deviceId=8389010


7.4.6.5           Masters

                                         NOTE
                                         Since this device is not a multimaster, the masterNumber is always 1. This also applies to
                                         the namespace ports.

                                         GET/masters
                                         Readout of general IO-Link master information.
                                         Sample response:
                                          [
                                                  {
                                                         "masterNumber": 1,
                                                         "serialNumber": "20020010",
                                                         "locationTag": "*******"
                                                  }
                                          ]

                                         GET/masters / 1/capabilities
                                         Readout of number of ports and the maximum current of all ports.


68        O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                     8016629.1MCE/2024-10-24 | SICK
                                                                                                               Subject to change without notice

SIG200 CONFIGURATION 7


                                   Sample response:
                                   {
                                        "numberOfPorts": 4,
                                        "maxPowerSupply": {
                                           "value": 2.0,
                                           "unit": "A"
                                        }
                                   }

                                   GET/masters / 1/identification
                                   Reading out specific IO-Link master information.
                                   Sample response:
                                   {
                                        "vendorName": "SICK AG",
                                        "vendorId": 26,
                                        "masterId": 1,
                                        "masterType": "Master acc. V1.1",
                                        "serialNumber": "20020010",
                                        "productId": "1089794",
                                        "productName": "SIG200-0A0412200",
                                        "hardwareRevision": "V1.0.0",
                                        "firmwareRevision": "1.3.1.2293B",
                                        "vendorUrl": "https://www.sick.com",
                                        "manualUrl": "https://www.sick.com/SIG200",
                                        "locationTag": "*******"
                                   }

                                   POST/masters / 1/identification
                                   Writing the identification parameters.
                                   JSON parameters Type                 Description
                                   locationTag        String            The user can assign a name here that describes the
                                                                        placement of the device in the system.


7.4.6.6            Ports
                                   GET/masters / 1/ports
                                   Readout of available ports with status information and device pseudonym (deviceA‐
                                   lias). The portNumber is used to access the individual ports. The deviceAlias is used to
                                   access the connected IO-Link devices and can be changed via /masters/1/ports/
                                   portNumber/configuration.
                                   Sample response:




8016629.1MCE/2024-10-24 | SICK                                        O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   69
Subject to change without notice

7 SIG200 CONFIGURATION

                                     [
                                             {
                                                    "portNumber": 1,
                                                    "statusInfo": "DIGITAL_INPUT_C/Q",
                                                    "deviceAlias": "master1port1"
                                             },
                                             {
                                                    "portNumber": 2,
                                                    "statusInfo": "DEVICE_ONLINE",
                                                    "deviceAlias": "master1port2"
                                             },
                                             {
                                                    "portNumber": 3,
                                                    "statusInfo": "COMMUNICATION_LOST",
                                                    "deviceAlias": "master1port3"
                                             },
                                             {
                                                    "portNumber": 4,
                                                    "statusInfo": "COMMUNICATION_LOST",
                                                    "deviceAlias": "master1port4"
                                             },
                                     ]

                                    GET/masters / 1/ports/{portNumber}/capabilities
                                    Readout of performance characteristics of the port.
                                    Sample response:
                                     {
                                             "maxPowerSupply": {
                                                "value": 0.5,
                                                "unit": "A"
                                             },
                                                "portType": "CLASS A"
                                     }

                                    GET/masters / 1/ports/{portNumber}/status
                                    Readout of port status.
                                     JSON parameters Type                            Description
                                     statusInfo                    Enum             Information about the state of the port.
                                                                   [“DEACTIVATED”/
                                                                   “INCOR‐
                                                                   RECT_DEVICE”/
                                                                   “DEVICE_START‐
                                                                   ING”/
                                                                   “DEVICE_ONLINE
                                                                   ”/ “COMMUNICA-
                                                                   TION_LOST”/
                                                                   “DIGI‐
                                                                   TAL_INPUT_C/Q”
                                                                   / “DIGI-TAL_OUT‐
                                                                   PUT_C/Q”/
                                                                   “NOT_AVAILA‐
                                                                   BLE”]

                                    Sample response:




70   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                    8016629.1MCE/2024-10-24 | SICK
                                                                                                                         Subject to change without notice

SIG200 CONFIGURATION 7


                                   {
                                        "statusInfo": "DEVICE_ONLINE",
                                        "iolinkRevision": "1.1",
                                        "transmissionRate": "COM3",
                                        "masterCycleTime": {
                                           "value": 3.2,
                                           "unit": "ms"
                                        }
                                   }

                                   GET/masters / 1/ports/{portNumber}/configuration

                                   POST/masters / 1/ports/{portNumber}/configuration
                                   Read and write the port configuration.
                                   JSON parameters Type                Description
                                   mode              Enum            Configuration options:
                                                     [“DEACTIVATED”/
                                                     “IOLINK_MAN‐    • Manual mode: Required if cycle time, device check or
                                                                        data storage is to be used
                                                     UAL”/
                                                     “IOLINK_AUTOS‐  •  Auto: IO-Link devices are detected automatically.
                                                                        Cycle time is set to fastest possible.
                                                     TART”/ “DIGI‐
                                                     TAL_INPUT”/     • Digital input: Pin 4 is switched as input.
                                                     “DIGITAL_OUT‐   • Digital output: Pin 4 is switched as output.
                                                     PUT” ]
                                   validationAn Enum            Configuration options:
                                   dBackup
                                                [“NO_DEVICE_CH •
                                                                   No check: Any IO-Link devices are detected and proc‐
                                                                   ess data is transmitted
                                                ECK”/
                                                “TYPE_COMPATI‐  •  Revision Check: This setting activates a check of the
                                                                   IO-Link revision and a connection is only established
                                                BLE_DEVICE_V1.
                                                                   for devices with the corresponding version.
                                                0”/ “TYPE_COM‐
                                                PATIBLE_DEVICE_ •  Data Storage: This parameter is used to set Data Stor‐
                                                                   age in "Restore" or "Backup&Restore" mode for the
                                                V1.1”/
                                                                   corresponding port.
                                                “TYPE_COMPATI‐
                                                BLE_DEVICE_V1.
                                                1_BACKUP_AND_
                                                RESTORE”/
                                                “TYPE_COMPATI‐
                                                BLE_DEVICE_V1.
                                                1_RESTORE” ]

                                   Example:




8016629.1MCE/2024-10-24 | SICK                                       O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   71
Subject to change without notice

7 SIG200 CONFIGURATION

                                          {
                                                  "mode": "IOLINK_MANUAL",
                                                  "validationAndBackup": "TYPE_COMPATIBLE_DEVICE_V1.1",
                                                  "iqConfiguration": "DIGITAL_INPUT",
                                                  "cycleTime": {
                                                      "value": 0.0,
                                                      "unit": "ms"
                                                  },
                                                  "ve
                                                  ndo
                                                  rId
                                                  ":
                                                  26,
                                                  "de
                                                  vic
                                                  eId
                                                  ":
                                                  838
                                                  901
                                                  1,
                                                  "de
                                                  vic
                                                  eAl
                                                  ias
                                                  ":
                                                  "ma
                                                  ste
                                                  r1p
                                                  ort
                                                  1"
                                          }

                                         GET/masters / 1/ports/{portNumber}/datastorage

                                         POST/masters / 1/ports/{portNumber}/datastorage
                                         Read and write the Data Storage objectin base64 coding.
                                         Example:
                                          {
                                                  "header": {
                                                      "vendorId": 26,
                                                      "deviceId": 8389010,
                                                      "iolinkRevision": "1.1"
                                                  },
                                                  "co
                                                  nte
                                                  nt"
                                                  :
                                                  "DAAAAgAAGAAAAzAxMkAAAAcqKioqKioqWwAAAQBcAAABAHgAAAGB4wAAAQDmAA
                                                  ABAOcAADEAMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwM
                                                  DAwMDAwMDAw6AAABwAwMDAAAAClDwACAACnDwDkUEsDBBQACAAIAMkIIeAAAAAA
                                                  AAAAAAAAAAAAAAAAAAAAAAAAAAACqDwDkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                                                  AAAAAAAAAAAAAAAAAgAAtA8AAgAAtQ8AAgAAtg8AAgAAtw8AAgAAuA8AAgAAuQ8
                                                  AAgAAug8AAgAA"
                                          }


7.4.6.7           Devices
                                         GET/devices
                                         Overview of ports and device aliases (deviceAlias).


72        O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200            8016629.1MCE/2024-10-24 | SICK
                                                                                                      Subject to change without notice

SIG200 CONFIGURATION 7


                                   Sample response:
                                   [
                                        {
                                             "deviceAlias": "master1port1",
                                             "masterNumber": 1,
                                             "portNumber": 1
                                        },
                                        {
                                             "deviceAlias": "master1port2",
                                             "masterNumber": 1,
                                             "portNumber": 2
                                        },
                                        {
                                             "deviceAlias": "master1port3",
                                             "masterNumber": 1,
                                             "deviceAlias": "portNumber": 3
                                        },
                                        {
                                             "deviceAlias": "master1port4",
                                             "masterNumber": 1,
                                             "deviceAlias": "portNumber": 4
                                        },
                                   ]

                                   GET/devices/{deviceAlias}/capabilities
                                   Reading the device properties and supported profiles.
                                   Sample response:
                                   {
                                        "minimumCycleTime": {
                                           "value": 5.1000000000000009,
                                           "unit": "ms"
                                           "portNumber": 1
                                        },
                                        "supportedProfiles": [
                                           1,
                                           32768,
                                           32769,
                                           32770
                                        }
                                   }

                                   GET/devices/{deviceAlias}/identification

                                   POST/devices/{deviceAlias}/identification
                                   Reading and writing the IO-Link device identification data.
                                   JSON parameters Type                 Description
                                   applicationS String                  The user can assign a name with this parameter, which
                                   pecificTag                           describes the application of the device in the system.
                                                                        Refer to the data sheet of the connected IO-Link device
                                                                        to see whether the parameter is available.
                                   locationTag        String            The user can assign a name with this parameter, which
                                                                        describes the placement of the device in the system.
                                                                        Refer to the data sheet of the connected IO-Link device
                                                                        to see whether the parameter is available.




8016629.1MCE/2024-10-24 | SICK                                        O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   73
Subject to change without notice

7 SIG200 CONFIGURATION

                                     JSON parameters Type                            Description
                                     functionTag                   String            The user can assign a name with this parameter, which
                                                                                     describes the function of the device in the system. Refer
                                                                                     to the data sheet of the connected IO-Link device to see
                                                                                     whether the parameter is available.

                                    Sample response:
                                     {
                                             "vendorId": 26,
                                             "deviceId": 8389010,
                                             "iolinkRevision": "1.1",
                                             "vendorName": "SICK AG",
                                             "vendorText": "www.sick.com",
                                             "productName": "SIG100",
                                             "productId": "1089792",
                                             "productText": "IO-Link Sensor Hub",
                                             "serialNumber": "18301211",
                                             "hardwareRevision": "1.0",
                                             "firmwareRevision": "1.1.2.R",
                                             "applicationSpecificTag": "Test device"
                                     }

                                    Sample request:
                                     {
                                             "applicationSpecificTag": "Test device"
                                     }

                                    GET/devices/{deviceAlias}/events
                                    Reading the events of the IO-Link device.
                                     Query parame‐                 Type              Description
                                     ters
                                     top                           Integer           Filter to output only the first events after switching on
                                                                                     the supply voltage.
                                     bottom                        Integer           Filter to output only the most recent events in time.

                                    Sample response:
                                     [
                                             {
                                                    "time": "00:23:21:37.897",
                                                    "severity": "ERROR",
                                                    "message": {
                                                       "code": 4096,
                                                       "mode": "APPEARS",
                                                       "text": "General malfunction - Unknown error"
                                                    },
                                                    "origin": {
                                                       "deviceAlias": "master1port1",
                                                       "portNumber": 1,
                                                       "masterNumber": 1
                                                    }
                                             }
                                     ]

                                    GET/devices/{deviceAlias}/processdata/value

                                    GET/devices/{deviceAlias}/processdata/getdata/value



74   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                      8016629.1MCE/2024-10-24 | SICK
                                                                                                                           Subject to change without notice

SIG200 CONFIGURATION 7


                                   GET/devices/{deviceAlias}/processdata/setdata/value
                                   Reading the input and/or output process data, where the length of the process data
                                   depends on the connected device.
                                   Query parame‐      Type              Description
                                   ters
                                   format             Enum              Selection of the process data structure. Either as a byte
                                                      [“byteArray”/     array (default) or according to the data structure and
                                                      “iodd”]           typing stored in the IODD. Requires prior upload of the
                                                                        correct IODD.

                                   http://192.168.2.1/iolink/v1/devices/master1port1/processdata/value
                                   http://192.168.2.1/iolink/v1/devices/master1port1/processdata/
                                   setdata/value?format=iodd

                                   JSON parameters Type                 Description
                                   getData            Object            Input process data of the connected device.
                                   setData            Object            Output process data of the connected device.
                                   valid              Boolean           Describes the validity of the process data.
                                   iqValue            Boolean           Output state pin 2.
                                   cqValue            Boolean           Output state pin 4.

                                   Sample response:




8016629.1MCE/2024-10-24 | SICK                                        O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   75
Subject to change without notice

7 SIG200 CONFIGURATION

                                    Table 56: ]
                                     {
                                             "ge
                                             tDa
                                             ta"
                                             : {
                                                    "io
                                                    lin
                                                    k":
                                                    {
                                                           "va
                                                           lid
                                                           ":
                                                           tru
                                                           e,
                                                           "va
                                                           lue
                                                           ":
                                                           [
                                                                   0,
                                                                   0,
                                                                   0,
                                                                   0,
                                                                   0,
                                                                   0,
                                                                   0,
                                                                   0
                                                           ]
                                                    },
                                                    "iq
                                                    Val
                                                    ue"
                                                    :
                                                    fal
                                                    se
                                             },
                                             "se
                                             tDa
                                             ta"
                                             : {
                                                    "io
                                                    lin
                                                    k":
                                                    {
                                                           "va
                                                           lid
                                                           ":
                                                           fal
                                                           se,
                                                           "va
                                                           lue
                                                           ":
                                                           [
                                                                   0,
                                                           ]
                                                    }
                                             }
                                     }




76   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   8016629.1MCE/2024-10-24 | SICK
                                                                                        Subject to change without notice

SIG200 CONFIGURATION 7


                                   POST/devices/{deviceAlias}/processdata/value
                                   Writing the output process data, where the length of the process data depends on the
                                   connected device. As with reading, access can be as a byte array or in IODD format.

                                   NOTE
                                   To write the output process data, the port owner must be set to REST.

                                   Example of byte array:
                                   {
                                        "iolink": {
                                           "value": [
                                               0,
                                               2
                                           ]
                                        }
                                   }

                                   Example of IODD format:
                                   {
                                        "iolink": {
                                           "value": [
                                               "Analog value": {
                                                  "value": 2
                                               }
                                           }
                                        }
                                   }

                                   GET/devices/{deviceAlias}/parameters/{index}/value

                                   POST/devices/{deviceAlias}/parameters/{index}/value
                                   Reading and writing the IO-Link device parameters (ISDU).
                                   http://192.168.2.1/iolink/v1/devices/master1port1/parameters/24/
                                   value
                                   {
                                        "value": [
                                           31,
                                           32,
                                           33,
                                           34,
                                           35
                                        ]
                                   }

                                   GET/devices/{deviceAlias}/parameters/{index}/subindices

                                   GET/devices/{deviceAlias}/parameters/{index}/subindices/{subindex}/value

                                   POST/devices/{deviceAlias}/parameters/{index}/subindices/{subindex}/value
                                   When reading or writing to subindices, it is necessary to upload a matching IODD.




8016629.1MCE/2024-10-24 | SICK                                       O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   77
Subject to change without notice

7 SIG200 CONFIGURATION

                                     http://192.168.2.1/iolink/v1/devices/master1port1/parameters/13/
                                     subindices
                                     [
                                             {
                                                    "subIndex": 1,
                                                    "subParameterName": "element_1"
                                             },
                                             {
                                                    "subIndex": 2,
                                                    "subParameterName": "element_2"
                                             },
                                             {
                                                    "subIndex": 3,
                                                    "subParameterName": "element_3"
                                             },
                                             {
                                                    "subIndex": 4,
                                                    "subParameterName": "element_4"
                                        },
                                     ]
                                     http://192.168.2.1/iolink/v1/devices/master1port1/parameters/13/
                                     subindices/1/value
                                     {
                                        "va
                                        lue
                                        ":
                                        [
                                            0,
                                            1
                                        ]
                                     }

                                    GET/devices/{deviceAlias}/parameters
                                    Output of a list with all parameters contained in the IODD and their names.
                                     JSON parameters Type                            Description
                                     index                         Integer           Parameter index via which the corresponding ISDU can
                                                                                     be accessed.
                                     parameterNam String                             Name of the parameter from IODD.
                                     e
                                     parameterNam String                             Name of the parameter without spaces. This name is
                                     eURI                                            also used to access individual parameters.

                                    Sample response:




78   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                  8016629.1MCE/2024-10-24 | SICK
                                                                                                                       Subject to change without notice

SIG200 CONFIGURATION 7


                                   [
                                       {
                                             "index": 0,
                                             "parameterName": "Direct Parameters 1",
                                             "parameterNameURI": "Direct_Parameters_1"
                                       },
                                       {
                                             "index": 1,
                                             "parameterName": "Direct Parameters 2",
                                             "parameterNameURI": "Direct_Parameters_2"
                                       },
                                       {
                                             "index": 2,
                                             "parameterName": "Standard Command",
                                             "parameterNameURI": "Standard_Command"
                                       },
                                       {
                                             "index": 12,
                                             "parameterName": "Device Access Locks",
                                             "parameterNameURI": "Device_Access_Locks"
                                       },
                                       {
                                             "index": 13,
                                             "parameterName": "Profile Characteristic",
                                             "parameterNameURI": "Profile_Characteristic"
                                       },
                                       {
                                             "index": 14,
                                             "parameterName": "PDInput Descriptor",
                                             "parameterNameURI": "PDInput_Descriptor"
                                       },
                                       {
                                             "index": 15,
                                             "parameterName": "PDOutput Descriptor",
                                             "parameterNameURI": "PDOutput_Descriptor"
                                       },
                                       {
                                             "index": 16,
                                             "parameterName": "Vendor Name",
                                             "parameterNameURI": "Vendor_Name"
                                       },
                                       {
                                             "index": 17,
                                             "parameterName": "Vendor Text",
                                             "parameterNameURI": "Vendor_Text"
                                       },
                                       {
                                             "index": 18,
                                             "parameterName": "Product Name",
                                             "parameterNameURI": "Product_Name"
                                       }
                                       ...
                                   ]

                                   GET/devices/{deviceAlias}/parameters/{parameterName}/value

                                   POST/devices/{deviceAlias}/parameters/{parameterName}/value

                                   GET/devices/{deviceAlias}/parameters/{parameterName}/subindices




8016629.1MCE/2024-10-24 | SICK                                   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   79
Subject to change without notice

7 SIG200 CONFIGURATION

                                         GET/devices/{deviceAlias}/parameters/{parameterName}/subindices/{subParame‐
                                         terName}/value

                                         POST/devices/{deviceAlias}/parameters/{parameterName}/subindices/{subParame‐
                                         terName}/value
                                         Reading and writing individual IO-Link device parameters via the parameter name.
                                         Requires correct IODD for the connected device.
                                          Query parame‐                 Type                   Description
                                          ters
                                          format                        Enum                   Selection of the parameter data structure. Either as byte
                                                                        [“byteArray”/          array (default) or according to the data structure and
                                                                        “iodd”]                typing stored in the IODD. Requires prior upload of the
                                                                                               correct IODD.


7.4.7             SICK-specific REST API (deprecated)

7.4.7.1           Error messages
                                         The table below contains all defined status codes, messages and a detailed descrip‐
                                         tion:
                                         Table 57: Status codes/messages of SICK-specific REST API (deprecated)
                                          Code           Message                Description
                                          0              Ok                     The request was processed successfully.
                                          1              Parsing        Error when analyzing the incoming JSON object.
                                                         failed (analy‐
                                                         sis failed)
                                          2              Invalid data           Data specified for variable is invalid
                                          3              Internal               General error message issued when an unexpected condition has
                                                         Server Error           occurred and no more specific message is suitable. Note: The Message
                                                                                property may contain more details about the error condition.
                                          4              Access                 The request was valid, but the server refuses to respond due to an
                                                         denied                 access violation. In the event of a variable access, it is possible that
                                                                                the variable is defined as read-only.
                                          5              Not found              Variable or method could not be found.
                                          6              Out of range The value does not fit into the value field or is too large, e.g. a value
                                                                      that exceeds or falls below the permitted minimum or maximum value
                                                                      for this variable.
                                          7              Out of                 An array was accessed whose maximum length was exceeded.
                                                         bounds (out
                                                         of the per‐
                                                         missible
                                                         range)
                                          9              Illegal value          A data condition was violated or the enum value passed was out of
                                                                                range.
                                          10             Invalid chal‐          The challenge used has expired or is unknown.
                                                         lenge
                                          11             Port not               The desired IO-Link port cannot be accessed:
                                                         available
                                                                                 • Incorrect parameterization
                                                                                 • Missing IO-Link device
                                          12             Communica‐ The desired IO-Link port does not provide a communication channel:
                                                         tion error
                                                                    • Read incoming/outgoing process data if not available


80        O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                           8016629.1MCE/2024-10-24 | SICK
                                                                                                                                     Subject to change without notice

SIG200 CONFIGURATION 7


7.4.8              Gateway Configuration
The following table shows all available REST commands (variables or methods) for SIG200. The commands are
shown without the base URL. The response is indicated without the header (see above).
Table 58: REST commands
 Command                           HTTP       JSON request part                     Response JSON body                               Function
                                   method
 api/DeviceIdent                   GET        -                                     {                                                Product name
                                                                                    "header": {                                      and firmware ver‐
                                                                                    "status": 0,                                     sion
                                                                                    "message": "Ok"
                                                                                    },
                                                                                    "data": {
                                                                                    "DeviceIdent": {
                                                                                    "Name": "SIG200",
                                                                                    "Version": "1.0.0.0A"
                                                                                    }
                                                                                    }
 api/LocationName                  GET (read) -                                     {                                                User-defined
                                                                                    "header": {                                      location name of
                                                                                    "status": 0,                                     product
                                                                                    "message": "Ok"
                                                                                    },
                                                                                    "data": {
                                                                                    "LocationName": "abc"
                                                                                    }
                                   POST       {                                     -
                                   (write)    "data": {
                                              "LocationName": "abc"
                                              }
                                              }
 api/FirmwareVersion               GET        -                                     {                                                Firmware version
                                                                                    "header": {                                      of product
                                                                                    "status": 0,
                                                                                    "message": "Ok"
                                                                                    },
                                                                                    "data": {
                                                                                    "FirmwareVersion": "1.0.0.0"
                                                                                    }
 api/ApplicationVersion            GET        -                                     {                                                Application ver‐
                                                                                    "header": {                                      sion of product
                                                                                    "status": 0,
                                                                                    "message": "Ok"
                                                                                    },
                                                                                    "data": {
                                                                                    "ApplicationVersion": "1.0"
                                                                                    }
 api/AppEngineVersion              GET        -                                     {                                                AppEngine ver‐
                                                                                    "header": {                                      sion of product
                                                                                    "status": 0,
                                                                                    "message": "Ok"
                                                                                    },
                                                                                    "data": {
                                                                                    "AppEngineVersion": "2.6.1"
                                                                                    }




8016629.1MCE/2024-10-24 | SICK                                        O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200     81
Subject to change without notice

7 SIG200 CONFIGURATION

Command                                    HTTP                JSON request part        Response JSON body              Function
                                           method
api/OrderNumber                            GET                 -                        {                               Order number of
                                                                                        "header": {                     product
                                                                                        "status": 0,
                                                                                        "message": "Ok"
                                                                                        },
                                                                                        "data": {
                                                                                        "OrderNumber": "1234567"
                                                                                        }
api/SerialNumber                           GET                 -                        {                               Serial number of
                                                                                        "header": {                     product
                                                                                        "status": 0,
                                                                                        "message": "Ok"
                                                                                        },
                                                                                        "data": {
                                                                                        "SerialNumber": "12345678"
                                                                                        }
api/Manufacturer                           GET                 -                        {                               Manufacturer
                                                                                        "header": {                     name of product
                                                                                        "status": 0,
                                                                                        "message": "Ok"
                                                                                        },
                                                                                        "data": {
                                                                                        "Manufacturer": "SICK AG"
                                                                                        }
api/PowerOnCnt                             GET                 -                        {                               Number of power
                                                                                        "header": {                     cycles of product
                                                                                        "status": 0,
                                                                                        "message": "Ok"
                                                                                        },
                                                                                        "data": {
                                                                                        "PowerOnCnt": 16
                                                                                        }
api/OpHours                                GET                 -                        {                               Number of oper‐
                                                                                        "header": {                     ating hours of
                                                                                        "status": 0,                    product
                                                                                        "message": "Ok"
                                                                                        },
                                                                                        "data": {
                                                                                        "OpHours": 1526
                                                                                        }
api/DailyOpHours                           GET                 -                        {                               Hours since last
                                                                                        "header": {                     start-up of prod‐
                                                                                        "status": 0,                    uct
                                                                                        "message": "Ok"
                                                                                        },
                                                                                        "data": {
                                                                                        "DailyOpHours":
                                                                                        53.687633514
                                                                                        }




82      O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                           8016629.1MCE/2024-10-24 | SICK
                                                                                                                   Subject to change without notice

SIG200 CONFIGURATION 7


 Command                           HTTP     JSON request part                 Response JSON body                               Function
                                   method
 api/EtherIPAddress                GET      -                                 {                                                IP address of
                                                                              "header": {                                      product
                                                                              "status": 0,
                                                                              "message": "Ok"
                                                                              },
                                                                              "data": {
                                                                              "EtherIPAddress": [
                                                                              192,
                                                                              168,
                                                                              0,
                                                                              1
                                                                              ]
                                                                              }
 api/EtherIPMask                   GET      -                                 {                                                Subnet mask of
                                                                              "header": {                                      product
                                                                              "status": 0,
                                                                              "message": "Ok"
                                                                              },
                                                                              "data": {
                                                                              "EtherIPMask": [
                                                                              255,
                                                                              255,
                                                                              255,
                                                                              0
                                                                              ]
                                                                              }
 api/EtherIPGateAddress            GET      -                                 {                                                Gateway address
                                                                              "header": {                                      of product
                                                                              "status": 0,
                                                                              "message": "Ok"
                                                                              },
                                                                              "data": {
                                                                              "EtherIPGateAddress": [
                                                                              0,
                                                                              0,
                                                                              0,
                                                                              0
                                                                              ]
                                                                              }
 api/EtherMACAddress               GET      -                                 {                                                MAC address of
                                                                              "header": {                                      product
                                                                              "status": 0,
                                                                              "message": "Ok"
                                                                              },
                                                                              "data": {
                                                                              "EtherMACAddress": [
                                                                              0,
                                                                              6,
                                                                              119,
                                                                              0,
                                                                              0,
                                                                              0
                                                                              ]
                                                                              }
                                                                              }



8016629.1MCE/2024-10-24 | SICK                                  O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   83
Subject to change without notice

7 SIG200 CONFIGURATION

Command                                    HTTP                JSON request part             Response JSON body                Function
                                           method
api/Port1IODDFileName,                     GET                 -                             {                        Returns name of
api/Port2IODDFileName,                                                                       "header": {              IODD file
api/Port3IODDFileName,                                                                       "status": 0,             assigned to IO-
api/Port4IODDFileName                                                                        "message": "Ok"          Link port
                                                                                             },
                                                                                             "data": {
                                                                                             "Port1IODDFileName":
                                                                                             "SICK-WTB12C-3_A00-20160513-IODD1.1.zip"
                                                                                             }
api/Port1Pin4Configuration,                GET                 -                             {                                 Reads/writes the
api/Port2Pin4Configuration,                                                                  "header": {                       IOLink configura‐
api/Port3Pin4Configuration,                                                                  "status": 0,                      tion for port 1. 0
api/Port4Pin4Configuration                                                                   "message": "Ok"                   = input, 1 = out‐
                                                                                             },                                put, 2 = iolink, 3
                                                                                             "data": {                         = disabled
                                                                                             "Port1Pin4Configuration": 2
                                                                                             }
                                           POST                {                             -
                                           (write)             "data": {
                                                               "Port1Pin4Configuration": 2
                                                               }
                                                               }
api/LabelPort1Pin2,                        GET                 -                             {                                 Reads/writes the
api/LabelPort1Pin4,                                                                          "header": {                       electronic label
api/LabelPort2Pin2,                                                                          "status": 0,                      for each port pin.
api/LabelPort2Pin4,                                                                          "message": "Ok"                   The maximum
api/LabelPort3Pin2,                                                                          },                                length for a label
api/LabelPort3Pin4,                                                                          "data": {                         is 8 characters.
api/LabelPort4Pin2,                                                                          "LabelPort1Pin2": "abc"
api/LabelPort4Pin4
                                                                                             }
                                           POST                {                             -
                                           (write)             "data": {
                                                               "LabelPort1Pin2": "abc"
                                                               }
                                                               }
api/PortOwner1_Fieldbus,                   GET                 -                             {                                 Reads/writes the
api/PortOwner2_Fieldbus,                                                                     "header": {                       Port owner con‐
api/PortOwner3_Fieldbus,                                                                     "status": 0,                      figuration for
api/PortOwner4_Fieldbus                                                                      "message": "Ok"                   each port:
                                                                                             },                                0 = Fieldbus, 1=
                                                                                             "data": {                         REST, 2= Logic
                                                                                             "PortOwner1_Fieldbus": 1          Editor
                                                                                             }
                                           POST                {                             -
                                           (write)             "data": {
                                                               "PortOwner1_Fieldbus": 1
                                                               }
                                                               }




84      O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                  8016629.1MCE/2024-10-24 | SICK
                                                                                                                          Subject to change without notice

SIG200 CONFIGURATION 7


 Command                           HTTP      JSON request part                     Response JSON body                               Function
                                   method
 api/Port1CycleTime,               GET       -                                     {                                                Cycle time for
 api/Port2CycleTime,                                                               "header": {                                      port 1. 0 = Fast
 api/Port3CycleTime,                                                               "status": 0,                                     as possible, 1 =
 api/Port4CycleTime                                                                "message": "Ok"                                  1.6ms, 2 =
                                                                                   },                                               3.2ms, 3 =
                                                                                   "data": {                                        4.8ms, 4 = 8ms,
                                                                                   "Port1CycleTime": 0                              5 = 20.8ms, 6 =
                                                                                                                                    40ms,7 =
                                                                                   }
                                                                                                                                    80ms,8 =
                                   POST      {                                     -                                                120ms
                                   (write)   "data": {
                                             "Port1CycleTime": 1
                                             }
                                             }
 api/Port1BackupLevel,             GET       -                                     {                                                Data storage
 api/Port2BackupLevel,                                                             "header": {                                      backup level for
 api/Port3BackupLevel,                                                             "status": 0,                                     port 1. 1 =
 api/Port4BackupLevel                                                              "message": "Ok"                                  RESTORE,2 =
                                                                                   },                                               BACKUP/
                                                                                   "data": {                                        RESTORE, 3 =
                                                                                   "Port1BackupLevel": 1                            Disabled
                                                                                   }
                                   POST      {                                     -
                                   (write)   "data": {
                                             "Port1BackupLevel": 1
                                             }
                                             }
 api/crown/ac/GetDiskUsage         POST      -                                     {                                                Returns how
                                   (read)                                          "header": {                                      many bytes of
                                                                                   "status": 0,                                     the device’s fil‐
                                                                                   "message": "Ok"                                  eystem is being
                                                                                   },                                               used. The
                                                                                   "data": {"BytesUsed":                            SIG200 has
                                                                                   0.000000,"Capacity":                             3.2GB of availa‐
                                                                                   2469606195.000000}                               ble disk space.

 api/crown/ac/GetLinkStatus        POST      { "data": {"Port":1}}                 {                                                Returns the link
                                   (read)                                          "header": {                                      status of Ether‐
                                                                                   "status": 0,                                     net ports (“Port”
                                                                                   "message": "Ok"                                  =1 or 2)
                                                                                   },
                                                                                   "data": {
                                                                                   "Status": "100MB-Full Duplex"
                                                                                   }
 api/crown/ac/GetPortStatus        POST      { "data": {"Port":1}}                 {                                                Returns the sig‐
                                   (read)                                          "header": {                                      nal status and
                                                                                   "status": 0,                                     name of con‐
                                                                                   "message": "Ok"                                  nected device on
                                                                                   },                                               an IO-Link port
                                                                                   "data": {                                        (“Port”=1, 2, 3,
                                                                                   "Status": "OK",                                  or 4)
                                                                                   "Pin4Value": false,
                                                                                   "Pin2Value": false,
                                                                                   "ConnectedDevice":
                                                                                   "PAC50-BCD"
                                                                                   }}



8016629.1MCE/2024-10-24 | SICK                                       O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200     85
Subject to change without notice

7 SIG200 CONFIGURATION

Command                                    HTTP                JSON request part         Response JSON body                Function
                                           method
api/crown/ac/SetPortOutput                 POST                {                         {                                 Sets pin 4 to high
                                           (write)             "data":                   "header": {                       (true) or low
                                                               {                         "status": 0,                      (false) according
                                                               "Port“:1,                 "message": "Ok"                   to the value and
                                                               „Value“: true             },                                port defined in
                                                               }                         "data": {                         the request part.
                                                               }                         "Status": "Ok"
                                                                                         }                                 NOTE
                                                                                         }                                 The port owner
                                                                                                                           needs to be con‐
                                                                                                                           figured as REST
                                                                                                                           in order to
                                                                                                                           change the state
                                                                                                                           of the digital out‐
                                                                                                                           put.

api/crown/ac/                              POST                { "data": {"Port":1}}     {                                 Returns the full
GetPortConfiguration                       (read)                                        "header": {                       port configura‐
                                                                                         "status": 0,                      tion of an IO-Link
                                                                                         "message": "Ok"                   port (“Port”=1, 2,
                                                                                         },                                3, or 4)
                                                                                         "data": {
                                                                                         "Status": "OK",
                                                                                         "Pin4Configuration": "IOLink",
                                                                                         "PortOwner": "Logic Editor",
                                                                                         "CycleTime":
                                                                                         "as fast as possible",
                                                                                         "IODDFileName": "none",
                                                                                         "DataStorageLevel":
                                                                                         "Disabled",
                                                                                         "VendorID": "0",
                                                                                         "DeviceID": "0"
                                                                                         }
api/crown/ac/                              POST                {                         {                                 Returns data
ReadDataStorage                            (read)              "data":                   "header": {                       storage object as
                                                               {                         "status": 0,                      a Base64 coded
                                                               "Port": 1                 "message": "Ok"                   string of an IO-
                                                               }                         },                                Link port
                                                               }                         "data": {                         (“Port”=1, 2, 3,
                                                                                         }                                 or 4).
                                                                                         }
api/crown/ac/                              POST                {                         {                                 Writes and
WriteDataStorage                           (write)             "data":                   "header": {                       applies data stor‐
                                                               {                         "status": 0,                      age object as a
                                                               "Port": 1                 "message": "Ok"                   Base64 coded
                                                               "DS_Data":                },                                string of an IO-
                                                               "eHCAIRoA1gGAAAAADAAAA‐   "data": {                         Link port
                                                               gAAGAAAB3QAdGVzdCB‐       "ErrorInfo": "OK"                 (“Port”=1, 2, 3,
                                                               CAAABAkMAAAQAAAACRAAA‐                                      or 4). Ensure that
                                                                                         }
                                                               BAAAAMhRAAAEAAAQA‐                                          the data storage
                                                                                         }
                                                               FIAAAQBAAAAVQAAAQA="                                        object is compat‐
                                                               }                                                           ible to the con‐
                                                                                                                           nected device.
                                                               }




86      O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                              8016629.1MCE/2024-10-24 | SICK
                                                                                                                      Subject to change without notice

SIG200 CONFIGURATION 7


 Command                             HTTP       JSON request part                         Response JSON body                               Function
                                     method
 api/crown/ac/                       POST       { "data": {"Port":1}}                     {                                                Starts IO-Link
 TriggerDataStorage                  (write)                                              "header": {                                      “Data Storage”
                                                                                          "status": 0,                                     as configured for
                                                                                          "message": "Ok"                                  an IO-Link port
                                                                                          },                                               (“Port”=1, 2, 3,
                                                                                          "data": {                                        or 4)
                                                                                          "Status": "No Error"
                                                                                          }
 api/crown/ac/FindMe                 POST       { "data": {"Start":true}}                 -
                                     (write)
 api/crown/ac/                       POST       -                                         {                                                Returns the
 GetRestDataInLength                 (read)                                               "header": {                                      amount of data
                                                                                          "status": 0,                                     values available
                                                                                          "message": "Ok"                                  for accessing
                                                                                          },                                               Logic Editor
                                                                                          "data": {"Value": 3}                             inputs

 api/crown/ac/                       POST       -                                         {                                                Returns the
 GetRestDataOutLength                (read)                                               "header": {                                      amount of data
                                                                                          "status": 0,                                     values available
                                                                                          "message": "Ok"                                  for accessing
                                                                                          },                                               Logic Editor out‐
                                                                                          "data": {"Value": 4}                             puts

 api/crown/ac/SetRestDataIn          POST       {                                         -                                                Sets a data value
                                     (write)    "data": {"Offset":2,                                                                       as Logic Editor
                                                "Value": 1024}                                                                             input (“Offset”
                                                }                                                                                          selects data
                                                                                                                                           value; “Value”
                                                                                                                                           defines the
                                                                                                                                           value)
 api/crown/ac/GetRestDataIn          POST       {                                         {                                                Returns a data
                                     (read)     "data": {"Offset":0}                      "header": {                                      value that was
                                                }                                         "status": 0,                                     set as Logic Edi‐
                                                                                          "message": "Ok"                                  tor input (“Off‐
                                                                                          },                                               set” selects data
                                                                                          "data": {"Value": 1024}                          value)

 api/crown/ac/GetRestDataOut POST               {                                         {                                                Returns a data
                             (read)             "data": {"Offset":0}                      "header": {                                      value that is a
                                                }                                         "status": 0,                                     Logic Editor out‐
                                                                                          "message": "Ok"                                  put (“Offset”
                                                                                          },                                               selects data
                                                                                          "data": {"Value": 1024}                          value)


7.4.9              IO-Link device communication
                                   Access to connected IO-Link devices is also possible via the REST API.
                                   The namespace for accessing IO-Link devices in REST is "iolink/sickv1/".

                                   NOTE
                                   The namespace does not include the default name "api".

                                   Access is different depending on whether an IODD has been assigned to a port. The
                                   table below lists the use cases:




8016629.1MCE/2024-10-24 | SICK                                              O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   87
Subject to change without notice

7 SIG200 CONFIGURATION

                                    Table 59: Application scenarios
                                     IODD assigned                 Correct IO-Link device connected                REST access
                                     No                            Any                                             Raw data access
                                     Yes                           According to IODD                               Access by name or raw data access
                                     Yes                           Other than according to IODD                    None

                                    "Raw data access" means that implicit knowledge of the data is required for any access
                                    to the connected IO-Link device:
                                     •       Process data is returned as a byte array without details of the data structure.
                                     •       ISDU access is done by providing the index number and the data is available as a
                                             byte array.

                                    NOTE
                                    The available process data, index numbers and data format are usually specified by the
                                    manufacturer of the IO-Link device in the device data sheet.

                                    Table 60: API version
                                     Command                       HTTP                    JSON request part       JSON response         Function
                                                                   method                                          part
                                     iolink/sickv1/                GET                     -                       1 (no JSON nota‐      Returns the ver‐
                                     apiversion                                                                    tion)                 sion of the IO-
                                                                                                                                         Link API.

                                    The table below lists the access functions in REST for "raw data access":
                                    Table 61: Functions in REST for “raw data access”
                                     Command                                         HTTP           JSON request       JSON response            Function
                                                                                     method         part               part
                                     iolink/sickv1/apiversion                        GET            -                  1 (no JSON nota‐         Returns the
                                                                                                                       tion)                    version of
                                                                                                                                                the IO-Link
                                                                                                                                                API.




88   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                               8016629.1MCE/2024-10-24 | SICK
                                                                                                                                    Subject to change without notice

SIG200 CONFIGURATION 7


                                   Command                     HTTP               JSON request                  JSON response                 Function
                                                               method             part                          part
                                   iolink/sickv1 / readPort    POST               {                             {                  Returns the
                                   (process data)                                 "header": {                   "header": {        content of
                                                                                  "portNumber": 0               "status": 0,       the raw proc‐
                                                                                  },                            "message": "Ok" ess data of a
                                                                                  "data": {                     },                 connected
                                                                                  "processData":                "data": {          IO-Link
                                                                                  "in"                          "processDataIn": [ device.
                                                                                  }                             1,                 portNumber:
                                                                                  }                                                0 = Port 1, 1
                                                                                                                80,
                                                                                                                                   = Port 2, 2 =
                                                                                                                0,
                                                                                                                                   Port 3, 3 =
                                                                                                                0                  Port 4
                                                                                                                ],                 process‐
                                                                                                                "isValid": true    Data: In =
                                                                                                                }                  Incoming
                                                                                                                }                  process
                                                                                                                                   data, out =
                                                                                                                                   Outgoing
                                                                                                                                   process data
                                                                                                                                   processDa‐
                                                                                                                                   taIn/proc‐
                                                                                                                                   essDataOut:
                                                                                                                                   Byte array of
                                                                                                                                   the process
                                                                                                                                   data
                                                                                                                                   isValid: true/
                                                                                                                                   false
                                   iolink/sickv1 / writePort   POST               {                             {                             Sets the
                                   (process data)                                 "header":                     "header": {                   content of
                                                                                  {                             "status": 0,                  the raw proc‐
                                                                                  "portNumber":0                "message": "Ok"               ess data
                                                                                  }                             }                             (outgoing) of
                                                                                  ,"data":                      }                             a connected
                                                                                  {                                                           IO-Link
                                                                                                                                              device.
                                                                                  "processData‐
                                                                                  Out":[0,55]                                                 portNumber:
                                                                                                                                              0 = Port 1, 1
                                                                                  }
                                                                                                                                              = Port 2, 2 =
                                                                                  }
                                                                                                                                              Port 3, 3 =
                                                                                                                                              Port 4
                                                                                                                                              processDa‐
                                                                                                                                              taOut: Byte
                                                                                                                                              array of the
                                                                                                                                              process data




8016629.1MCE/2024-10-24 | SICK                                          O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200    89
Subject to change without notice

7 SIG200 CONFIGURATION

                                     Command                                         HTTP     JSON request      JSON response          Function
                                                                                     method   part              part
                                     iolink/sickv1 / readPort                        POST     {                 {                      Returns the
                                     (ISDU data)                                              "header": {       "header": {            raw parame‐
                                                                                              "portNumber": 0   "status": 0,           ter data of a
                                                                                              },                "message": "Ok"        connected
                                                                                              "data": {         },                     IO-Link
                                                                                              "index":24        "data": {              device.
                                                                                              }                 "24": [                portNumber:
                                                                                              }                 42,                    0 = Port 1, 1
                                                                                                                                       = Port 2, 2 =
                                                                                                                42,
                                                                                                                                       Port 3, 3 =
                                                                                                                42,
                                                                                                                                       Port 4
                                                                                                                42,
                                                                                                                                       index: ISDU
                                                                                                                42,                    number
                                                                                                                42                     data: Byte
                                                                                                                ]                      array of the
                                                                                                                }                      parameter
                                                                                                                }                      data
                                     iolink/sickv1 / writePort                       POST     {                 {                      Sets the raw
                                     (ISDU data)                                              "header": {       "header": {            parameter
                                                                                              "portNumber": 0   "status": 0,           data of a
                                                                                              },                "message": "Ok"        connected
                                                                                              "data": {         }                      IO-Link
                                                                                              "24": [           }                      device.
                                                                                              49,                                      portNumber:
                                                                                              50,                                      0 = Port 1, 1
                                                                                                                                       = Port 2, 2 =
                                                                                              51,
                                                                                                                                       Port 3, 3 =
                                                                                              52
                                                                                                                                       Port 4
                                                                                              ]
                                                                                                                                       data: Empty
                                                                                              }                                        member for
                                                                                              }                                        ISDU num‐
                                                                                                                                       ber, followed
                                                                                                                                       by the byte
                                                                                                                                       array of the
                                                                                                                                       parameter
                                                                                                                                       data

                                    NOTE
                                    “Raw data access" is also available when an IODD is assigned.

                                    "Access by name" means that data access to the connected IO-Link device is extended
                                    by metadata:
                                     •       Process data is returned segmented and displayed according to the definition in
                                             the IODD file.
                                     •       ISDU access is performed by variable ID and the data is represented according to
                                             the definition in the IODD file.
                                    Below is an example from the SIG100 IODD:
                                    <Datatype
                                    </Variable>




90   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                      8016629.1MCE/2024-10-24 | SICK
                                                                                                                           Subject to change without notice

SIG200 CONFIGURATION 7


                                   Command                     HTTP               JSON request                  JSON response                 Function
                                                               method             part                          part
                                   iolink/sickv1/readDevice    POST               {                             {                  Returns the
                                   (process data)                                 "header": {                   "header": {        segmented
                                                                                  "portNumber": 0               "status": 0,       and ana‐
                                                                                  },                            "message": "Ok" lyzed con‐
                                                                                  "data": {                     },                 tent of the
                                                                                  "processData":                "data": {          process data
                                                                                  "in"                          "processDataIn": { of a con‐
                                                                                  }                                                nected IO-
                                                                                                                "1": false,
                                                                                                                                   Link device.
                                                                                  }                             "2": false,
                                                                                                                                   portNumber:
                                                                                                                "3": false,
                                                                                                                                   0 = Port 1, 1
                                                                                                                "4": false,        = Port 2, 2 =
                                                                                                                "5": false,        Port 3, 3 =
                                                                                                                "6": false,        Port 4
                                                                                                                "7": false,        process‐
                                                                                                                "8": false,        Data: In =
                                                                                                                "9": false,        Incoming
                                                                                                                "10": false,       process
                                                                                                                "11": 0,           data, out =
                                                                                                                "12": 726          Outgoing
                                                                                                                },                 process data
                                                                                                                "isValid": true    processDa‐
                                                                                                                }                  taIn/proc‐
                                                                                                                }                  essDataOut:
                                                                                                                                   Structure of
                                                                                                                                   the process
                                                                                                                                   data accord‐
                                                                                                                                   ing to IODD
                                                                                                                                   isValid: true/
                                                                                                                                   false
                                   iolink/sickv1/writeDevice   POST               {                             {                             Sets the
                                   (process data)                                 "header":                     "header": {                   content of
                                                                                  {                             "status": 0,                  the raw proc‐
                                                                                  "portNumber":0                "message": "Ok"               ess data
                                                                                  }                             }                             (outgoing) of
                                                                                  ,"data":                      }                             a connected
                                                                                  {                                                           IO-Link
                                                                                                                                              device.
                                                                                  "processData‐
                                                                                  Out":[0,55]                                                 portNumber:
                                                                                                                                              0 = Port 1, 1
                                                                                  }
                                                                                                                                              = Port 2, 2 =
                                                                                  }
                                                                                                                                              Port 3, 3 =
                                                                                                                                              Port 4
                                                                                                                                              processDa‐
                                                                                                                                              taOut: Struc‐
                                                                                                                                              ture of the
                                                                                                                                              process data
                                                                                                                                              according to
                                                                                                                                              IODD




8016629.1MCE/2024-10-24 | SICK                                          O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200    91
Subject to change without notice

7 SIG200 CONFIGURATION

                                     Command                                         HTTP     JSON request       JSON response          Function
                                                                                     method   part               part
                                     iolink/sickv1/readDevice                        POST     {                  {                      Returns the
                                     (ISDU data)                                              "header": {        "header": {            analyzed
                                                                                              "portNumber": 0    "status": 0,           parameter
                                                                                              },                 "message": "Ok"        data of a
                                                                                              "data": {          },                     connected
                                                                                              "variable":        "data": {              IO-Link
                                                                                              "V_ApplicationS‐   "V_ApplicationS‐       device.
                                                                                              pecificTag"        pecificTag":           portNumber:
                                                                                              }                  "*******"              0 = Port 1, 1
                                                                                              }                  }                      = Port 2, 2 =
                                                                                                                                        Port 3, 3 =
                                                                                                                 }
                                                                                                                                        Port 4
                                                                                                                                        variable:
                                                                                                                                        ISDU name
                                                                                                                                        specified in
                                                                                                                                        the IODD
                                                                                                                                        data: Struc‐
                                                                                                                                        tured param‐
                                                                                                                                        eter data
                                     iolink/sickv1/writeDevice                       POST     {                  {                      Sets the
                                     (ISDU data)                                              "header": {        "header": {            analyzed
                                                                                              "portNumber": 1    "status": 0,           parameter
                                                                                              },                 "message": "Ok"        data of a
                                                                                              "data": {          }                      connected
                                                                                              }                  }                      IO-Link
                                                                                                                                        device.
                                                                                              }
                                                                                                                                        portNumber:
                                                                                                                                        0 = Port 1, 1
                                                                                                                                        = Port 2, 2 =
                                                                                                                                        Port 3, 3 =
                                                                                                                                        Port 4




92   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                       8016629.1MCE/2024-10-24 | SICK
                                                                                                                            Subject to change without notice

DEVICE FUNCTIONS 8


8                  Device Functions
8.1                Data Storage
                                   The Data Storage feature brings major advantages when it comes to easy replacement
                                   of IO-Link devices due to defects. This means that the whole parameter set of the
                                   device, e.g. switching point, additional logic or teach-in settings, are stored centralized
                                   in the SIG200. In case a connection with a compatible device is established, this stored
                                   parameter set is written to the device and it behaves like the device to be replaced.
                                   There are two different use cases how to utilize this mechanism:
                                   Use Case Backup + Restore:
                                   Parameters are read and written in both directions, from the IO-Link master to the
                                   device and vice versa. This mode is mostly used for commissioning meaning changes in
                                   the device configuration for example triggered by a teach-in are automatically uploaded
                                   and stored in the data storage object within the SIG200. It supports also device
                                   replacement, e.g. the configuration will be automatically copied to the new device, if
                                   one needs to be exchanged.
                                   Use Case Restore:
                                   In this mode the configuration of the connected IO-Link device will be stored and frozen.
                                   It cannot be changed by the device, e.g. a teach-in directly at the device will be ignored.
                                   Replacement of broken devices is also possible.
                                   However, this function only works if the devices are compatible with each other. For this
                                   reason, the Expected Device ID and Expected Vendor ID must also be specified.

8.1.1              Example Usage
                                   The SIG200 IO-Link Master Data Storage functionality allows straightforward replace‐
                                   ment of failed IO-Link sensors. The following step-by-step example shows how the
                                   SIG200 can be used to commission a new IO-Link device so that a replacement device
                                   will be automatically reconfigured to match the original device.
                                   1.   Configure the IO-Link port of the SIG200 with an IODD file and with the Data
                                        Storage set to Disabled.




                                   2.   Configure the IO-Link device. The IO-Link device can now be configured using the
                                        IODD View in the Configuration window IO-Link Devices tab or other configuration
                                        mechanism such as with the IO-Link device’s teach button.
                                   3.   Change the Data Storage mode from Disabled to Restore. The SIG200 automati‐
                                        cally uploads the new configuration.




                                   4.   Replace the original IO-Link device with a second device of the same type. The
                                        configuration parameters from the first device are automatically loaded into the
                                        second IO-Link device.

8.2                Logic Editor
                                   The logic Editor of SIG200 is a key function allowing you to realize dedicated applica‐
                                   tions within the device by utilizing connected sensors or actuators.



8016629.1MCE/2024-10-24 | SICK                                        O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   93
Subject to change without notice

8 DEVICE FUNCTIONS


                                    NOTE
                                    The drag & drop Logic Editor configuration is not accessible via the fieldbus or the REST
                                    API. There, only process data can be used as input or output values for the Logic Editor.

                                    The Logic Editor can use all available signal inputs as sources for the logic application.
                                    In SIG200 this includes:
                                     •       All IO-Link port pins configured as “Digital Input”
                                     •       IO-Link Process Data In from all SX port pins 4 configured to IO-Link mode (Port
                                             S1-S4)
                                     •       Fieldbus Input Process Data
                                     •       REST API Input values

                                    NOTE
                                    It is necessary to upload and assign the IODDs of the devices to be used in the Logic
                                    Editor.
                                    Removing IODDs of devices which has been connected in the Logic Editor could lead to
                                    incompatibilities. This is indicated by the following notification:




                                    Editing Mode




                                    Figure 14: Editing Mode

                                    1.       To start your configuration change the operating mode from Run to Maintenance
                                             because the Run mode is a read only mode.
                                    2.       Click on Run on the bottom left side and select Maintenance in the drop-down menu.
                                    3.       The login password for the maintenance mode is: main
                                    4.       Click on Login to select the Maintenance Mode.




94   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                        8016629.1MCE/2024-10-24 | SICK
                                                                                                             Subject to change without notice

DEVICE FUNCTIONS 8




                                   Figure 15: Editing Mode

                                   5.
                                        To start with a new configuration, click on                    EDIT in the upper right corner.

                                   Overview




                                   Figure 16: Logic editor screen


                                   •    orange: logic blocks
                                   •    green: inputs
                                   •    red: outputs
                                   •    blue: workspace




8016629.1MCE/2024-10-24 | SICK                                        O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   95
Subject to change without notice

8 DEVICE FUNCTIONS




                                    Figure 17: Detailed information

                                    Within the logic function in the top bar there are some functions mentioned twice. One
                                    time with red triangles (integer) and one time with orange triangles (float). So, the logic
                                    function is the same, but the data types which can be used are different.
                                    Example:




                                    Move your mouse over individual logic blocks to get more detailed information about
                                    their function.




                                    Figure 18: Logic blocks


                                     •       Use drag & drop to select the desired logic block and put it into the workspace.
                                     •       To delete logic blocks put them back in the upper area via drag & drop.
                                     •       The maximum amount of logic blocks which can be used in the logic editor in
                                             parallel is 20 blocks.


96   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                        8016629.1MCE/2024-10-24 | SICK
                                                                                                             Subject to change without notice

DEVICE FUNCTIONS 8


                                   NOTE
                                   The input and output blocks can be moved to the workspace to achieve a better routing
                                   and overview.




                                   Figure 19: Connections


                                   •    Connect your logic blocks with drag & drop with the inputs and outputs. First click
                                        on the triangle on the input, hold the line and connect it to a triangle of the logic
                                        block.
                                   •    Please note to use always the upper inputs first, starting at A, then B, then C. In
                                        case you use only two inputs please use always the top two inputs A+B and not e.
                                        g. B+D.
                                   •    Please note whether the values are Integer or Boolean it is only possible to
                                        connect Integer with Integer and Boolean with Boolean. Boolean values have a
                                        black triangle. Integer values are easily identifiable by a red triangle.




                                   Figure 20: Possible connections

                                   By clicking on logic block you get information about the possible connections to this
                                   individual block.



8016629.1MCE/2024-10-24 | SICK                                        O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   97
Subject to change without notice

8 DEVICE FUNCTIONS




                                    Figure 21: Several inputs and outputs

                                    It is possible to connect several inputs and outputs with logic blocks.
                                     •       A combination of logic blocks is possible as well.
                                     •       Pay attention to inputs and outputs (Integer/Boolean).




                                     •
                                             Click on Settings      (=gear) to configure parameters and values of the logic
                                             block or input/output variable.
                                     •       Please note that only integer values are allowed (0-65535).
                                             NOTE
                                             Not all logic blocks are adjustable.




98   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                        8016629.1MCE/2024-10-24 | SICK
                                                                                                             Subject to change without notice

DEVICE FUNCTIONS 8




                                   Figure 22: Configuration of digital inputs


                                   •    A configuration of your digital inputs is also possible.
                                   •    For configuration click on the selected port first and on the gear second to set
                                        Logic and DebounceValue.
                                   •    Use your mouse to get more information about Logic or DebounceValue.




                                   Figure 23: Delete connections

                                   To remove a connection click on your desired connection and put it in into the garbage
                                   bin on the upper area via drag & drop.




8016629.1MCE/2024-10-24 | SICK                                            O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   99
Subject to change without notice

8 DEVICE FUNCTIONS

                                        Download new Logic to the Device




                                        Figure 24: Transfer and execute flow

                                        Press Tansfer and Execute Flow to synchronize your workflow with your device. All changes
                                        you made without pressing this button will be lost and are not downloaded to your
                                        SIG200 device.

8.2.1            Deleting the Logic from the Device




                                        Press CLEAR FLOW to delete the complete logic from the configuration window. Note
                                        that you need to press TRANSFER AND EXECUTE FLOW to also delete the logic from the
                                        actual device.

8.2.2            Explanation of Inputs, Outputs and Logic Blocks
IO-Link Ports
The logic editor visualizes, in case an IODD for the device has been uploaded, the process data as they are defined
within the IODD of the IO-Link device. Inputs are displayed on the left side, outputs are visualized on the right side
of the logic editor workspace. So, the logic editor view is depending on the connected IO-Link devices.
Example: If you connect e.g. an inductive proximity sensor IMC on port S1 of SIG200, the input side looks like this:




With a red triangle, an integer value is symbolized. With a black triangle, a boolean variable is identified.

NOTE
Last valid process data value is provided in case of a IO-Link connection loss to the connected device.




100      O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                     8016629.1MCE/2024-10-24 | SICK
                                                                                                              Subject to change without notice

DEVICE FUNCTIONS 8


NOTE
Processing of the process data in the logic editor is not permanently clocked. That is why, depending on the load of
the device, e.g. due to increased network load, there may be a delay in the output process data.


NOTE
If IO-Link pin 4 changes from SIO mode to IO-Link mode the signal output shall be deactivated (and vice versa).

Inputs
Digital:
The pin 2 of Ports S1-S4 can be individually used. All pin 2 boxes are visualized by default in the logic editor. In
case a port has been configured as “Digital Input” meaning pin 4, it will be shown on the left side as an input.




Analog:
The constant number block can be set to a fixed value to be used for further processing.




Rest:
It is possible to set an input value via REST to be processed by the logic configuration of the SIG200. This input will
be visualized with "Rest In" on the logic editor page.




Outputs
Digital:
Pin 4 can be configured as “Digital outputs” to be addressed by the logic.




8016629.1MCE/2024-10-24 | SICK                                  O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   101
Subject to change without notice

8 DEVICE FUNCTIONS


NOTE
It is not possible to connect a digital output on pin 2.

Rest:
Through the “Rest Out” block, data from the logic can be sent via REST interface to an upper system (e. g. HTTP
Client).




Logics:
Table 62: Logic blocks
                                   Description                                            Addition of the two input values.
                                   Number of inputs                                       2
                                   Input data type                                        Integer
                                   Input description                                      num1: first input value
                                                                                          num2: second input value
                                   Number of outputs                                      1
                                   Output data type                                       Output 1 (“+“): Identical to input data type
                                   Output description                                     result: result after addition of the two input values
                                   Settings                                               no settings available




102       O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                           8016629.1MCE/2024-10-24 | SICK
                                                                                                                                     Subject to change without notice

DEVICE FUNCTIONS 8


                                   Description          Event counter for digital signals.
                                                        Maximum switching frequency (e. g. for a NOT gate): 35 Hz
                                                        Maximum switching frequency for the Counter: 90 Hz
                                   Number of inputs     4
                                   Input data type      Input 1 ("Up"): 1-bit
                                                        Input 2 ("Down"): 1-bit
                                                        Input 3 ("Reset to 0"): 1-bit
                                                        Input 4 ("Set to start value"): 1-bit
                                   Input description    increment: value will be counted up
                                                        decrement: value will be counted down
                                                        setZero: set counter to zero
                                                        setValue: set counter to StartValue
                                   Number of outputs    3
                                   Output data type     Output 1 ("Overflow"): 1-bit
                                                        Output 2 ("Counter value"): 32-bit
                                                        Output 3 ("Underflow"): 1-bit
                                   Output description   overflowFlag: Bit is set if the counter value exceeds the over‐
                                                        flow value
                                                        counterValue: Current counter value. Counter values are NOT
                                                        stored by a power cycle.
                                                        underflowFlag: Bit is set if the value is below the overflow
                                                        value. The default overflow value is 4,294,967,295.
                                   Settings             StartValue: Counter value that is set when “setValue” is trig‐
                                                        gered (default: 0)
                                                        OverflowValue: Maximum value of the counter output
                                                        (default: 4,294,967,295)
                                                        OverflowMode: Behavior of the counter value in the event of
                                                        an underflow or overflow
                                                        AUTO: After reaching the overflow value, the counter is auto‐
                                                        matically reset to the defined start value.
                                                        MANU: After reaching the overflow value, the counter value
                                                        can only be reset manually by the "setZero" or "setValue"
                                                        signal.
                                                        Additional information: When the maximum counter value
                                                        (overflow value) is reached, the overflow output is set to
                                                        "High". However, there is a difference between the automatic
                                                        and manual modes.
                                                        The automatic mode the value will be set to 0 on next rising
                                                        edge of the increment input and of course the counter value
                                                        can be changed by the setZero or setValue input.
                                                        In the manual mode, the countervalue will stay on the over‐
                                                        flowvalue until a rigsing edge on the decrement, setZero or
                                                        setValue input is detected.
                                                        The default value for the counter start is 0, but it can be set to
                                                        any value within the range (32 bits).
                                   Description          Division between the two input values.
                                   Number of inputs     2
                                   Input data type      Integer
                                   Input description    num1: first input value
                                                        num2: second input value
                                   Number of outputs    2
                                   Output data type     Output 1 ("/"): Identical to input data type
                                                        Output 2 ("/0"): 1-bit
                                   Output description   result: Result after dividing the two input values
                                                        divByZero: When dividing by 0 (not possible) this output is set
                                   Settings             No settings available


8016629.1MCE/2024-10-24 | SICK                              O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   103
Subject to change without notice

8 DEVICE FUNCTIONS

                               Description                                            Modulo operation between the two input values.
                               Number of inputs                                       2
                               Input data type                                        Integer
                               Input description                                      num1: first input value
                                                                                      num2: second input value
                               Number of outputs                                      2
                               Output data type                                       Output 1 ("/"): Identical to input data type
                                                                                      Output 2 ("/0"): 1-bit
                               Output description                                     result: Result with rest after dividing the two input values
                                                                                      divByZero: When dividing by 0 (not possible) this output is set
                               Settings                                               No settings available
                               Description                                            Multiplication between the two input values.
                               Number of inputs                                       2
                               Input data type                                        Integer
                               Input description                                      num1: first input value
                                                                                      num2: second input value
                               Number of outputs                                      1
                               Output data type                                       Output 1 ("x"): Identical to input data type
                               Output description                                     result: Result after multiplying the two input values
                               Settings                                               No settings available
                               Description                                            Negation of the input value either one´s or two´s comple‐
                                                                                      ment depending on the configuration.
                               Number of inputs                                       1
                               Input data type                                        Signed Integer
                               Input description                                      input: analog input value
                               Number of outputs                                      1
                               Output data type                                       Output 1 ("-"): Identical to input data type
                               Output description                                     result: The one's or two's complement of the input value. (So
                                                                                      the analog output value is the opposite of the input value).
                               Settings                                               Selection of the one's or two's complement (Default Two's
                                                                                      Complement)
                               Description                                            Subtraction of the two input values.
                               Number of inputs                                       2
                               Input data type                                        Integer
                               Input description                                      num1: first input value
                                                                                      num2: second input value
                               Number of outputs                                      1
                               Output data type                                       Output 1 ("-"): Identical to input data type
                               Output description                                     result: Result after subtraction of the two input values
                               Settings                                               No settings available




104   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                            8016629.1MCE/2024-10-24 | SICK
                                                                                                                                  Subject to change without notice

DEVICE FUNCTIONS 8


                                   Description          Compares the two analog input values: It is set when input 1
                                                        less than input 2. Ieq is set when input 1 less than or equal
                                                        input 2. Eq us set when input 1 equal input 2. Geq is set
                                                        when input 1 greater than or equal input 2. Gt is set when
                                                        input 1 greater than input 2.
                                   Number of inputs     2
                                   Input data type      Integer
                                   Input description    num1: first input value
                                                        num2: second input value
                                   Number of outputs    1 ... 5
                                   Output data type     Output 1 ("<"): 1-bit
                                                        Output 2 ("≤"): 1-bit
                                                        Output 3 (":"): 1-bit
                                                        Output 4 ("≥"): 1-bit
                                                        Output 5 (">"): 1-bit
                                   Output description   lt: < input is less than input 2
                                                        leq: ≤ input 1 is less or equal to input 2
                                                        eq: = input 1 is equal to input 2
                                                        geq: ≥ input 1 is greater or equal to input 2
                                                        gt: > input 1 is greater than input 2
                                   Settings             No settings available
                                   Description          Selection between two analog input values depending on the
                                                        boolean input.
                                   Number of inputs     3
                                   Input data type      Integer & Boolean
                                                        Input 1 ("If"): 1-bit
                                                        Input 2 ("Then"): Any
                                                        Input 3 ("Else"): Any
                                   Input description    num1: Boolean input
                                                        num2: Analog input 1
                                                        num3: Analog input 2
                                   Number of outputs    1
                                   Output data type     Integer
                                   Output description   result: If num1 is 1, then num2 is forwarded to the result. If
                                                        num1 is 0, then num3 is forwarded to the result (false means
                                                        0).
                                   Settings             No settings available
                                   Description          Clocked (rising edge) D-Flip Flop.
                                   Number of inputs     2
                                   Input data type      Input 1 ("data"): 1-bit
                                                        Input 2 ("clock"): 1-bit
                                   Input description    data: State of this input to be transferred to output on rising
                                                        edge.
                                                        clock: Rising edge of this input triggers the capture of the
                                                        data input.
                                   Number of outputs    2
                                   Output data type     Output 1 ("Q"): 1-bit
                                                        Output 2 ("notQ"): 1-bit
                                   Output description   Q: Set when data input is high and a rising egde occurs on the
                                                        clock input. Reset when data input is low and a rising edge
                                                        occurs on the clock input.
                                                        notQ: Inverted signal of output Q.
                                   Settings             No settings available


8016629.1MCE/2024-10-24 | SICK                              O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   105
Subject to change without notice

8 DEVICE FUNCTIONS

                               Description                                            Basic RS-Flip Flop functionality.
                                                                                      if (set == false and reset == false) then Q = Keeps it's last
                                                                                      value
                                                                                      elseif (set == false and reset == true) then Q = false
                                                                                      elseif (set == true and reset == false) then Q = true
                                                                                      elseif (set == true and reset == true) then Q = false
                                                                                      end
                               Number of inputs                                       2
                               Input data type                                        Input 1 ("Set"): 1-bit
                                                                                      Input 2 ("Reset"): 1-bit
                               Input description                                      set: See above truth table description
                                                                                      reset: See above truth table description
                               Number of outputs                                      2
                               Output data type                                       Output 1 ("Q"): 1-bit
                                                                                      Output 2 ("/Q"): 1-bit
                               Output description                                     Q: See above in description
                                                                                      notQ: Always equals Q inverted
                               Settings                                               No settings available
                               Description                                            Conversion of a float input to an analog output.
                               Number of input                                        1
                               Input data type                                        Float
                               Input description                                      in1: Float value to be converted
                               Number of outputs                                      2
                               Output data type                                       analogValue: Integer
                                                                                      overflow: 1-bit
                               Output description                                     analogValue: Converted integer value
                                                                                      overflow: This output is set in case the floating input value
                                                                                      exceeds the limitation of integer.
                               Settings                                               RoundModes: To select if a number should be rounded to
                                                                                      zero or to one.
                               Description                                            Conversion of an analog input to a float output.
                               Number of input                                        1
                               Input data type                                        Integer
                               Input description                                      in1: Analog value to be converted
                               Number of output                                       1
                               Output data type                                       Float
                               Output description                                     floatValue: Converted float value




106   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                           8016629.1MCE/2024-10-24 | SICK
                                                                                                                                 Subject to change without notice

DEVICE FUNCTIONS 8


                                   Description          Conversion of an analog input to four digital outputs.
                                   Number of inputs     1
                                   Input data type      Integer
                                   Input description    analogValue: Analog input value
                                   Number of outputs    4
                                   Output data type     Output 1 ... 16: 1-bit
                                   Output description   out1: first digital output
                                                        out2: second digital output
                                                        out4: third digital output
                                                        out8: fourth digital output
                                   Settings             To select which half byte should be connected to the output
                                                        (Default First half byte)
                                                        If First half byte selected send lowest 4 bits (bits marked with
                                                        x)
                                                        ----|----|----|xxxx
                                                        If Second half byte selected send bits marked with x
                                                        ----|----|xxxx|----
                                                        If Third half byte selected send bits marked with x
                                                        ----|xxxx|----|----
                                                         If Fourth half byte selected send bits marked with x
                                                        xxxx|----|----|----
                                   Description          Conversion of four digital inputs to an analog half byte value.
                                   Number of inputs     4
                                   Input data type      Input 1 ... 16: 1-bit
                                   Input description    in1: first digital input
                                                        in2: second digital input
                                                        in4: third digital input
                                                        in8: fourth digital input
                                   Number of outputs    1
                                   Output data type     Output 1: Integer or UInteger, 8 or 16 bits
                                   Output description   analogValue: analog half byte output value
                                   Settings             To select which half byte should be connected to the output
                                                        (Default First half byte)
                                                        If First half byte selected send lowest 4 bits (bits marked with
                                                        x)
                                                        ----|----|----|xxxx
                                                        If Second half byte selected send bits marked with x
                                                        ----|----|xxxx|----
                                                        If third half byte selected send bits marked with x
                                                        ----|xxxx|----|----
                                                        If Fourth half byte selected send bits marked with x
                                                        xxxx|----|----|----




8016629.1MCE/2024-10-24 | SICK                              O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   107
Subject to change without notice

8 DEVICE FUNCTIONS

                               Description                                            The input signal is delayed by the configured time.
                               Number of inputs                                       1
                               Input data type                                        1-bit
                               Input description                                      input: input value
                               Number of outputs                                      1
                               Output data type                                       1-bit
                               Output description                                     output: when the input becomes true, the output becomes
                                                                                      true after a preset time delay. The output remains true as long
                                                                                      as the input is true. When the input is false or becomes false,
                                                                                      the output becomes false with no delay.
                               Settings                                               OnDelay: Set delay for a rising edge transmitted to the output
                                                                                      (Default 1 ms)
                                                                                      OffDelay: Set delay for a falling edge transmitted to the output
                                                                                      (Default 1 ms)
                                                                                      The may. delay value for one delay is: 65535 ms
                                                                                      The falling edge is configured with the OffDelay setting.
                               Description                                            Measures the pulse time of the digital input signal triggered
                                                                                      by the rising or falling edge depending on the configuration.
                                                                                      Information: There is no reset. Once it reaches the High Limit
                                                                                      it stops.
                               Number of inputs                                       2
                               Input data type                                        Input 1 ("Activate"): 1-bit
                                                                                      Input 2 ("Reset"): 1-bit
                               Input description                                      input: input signal
                                                                                      Reset: Sets the timer to 0 at rising edge
                               Number of outputs                                      3
                               Output data type                                       Output 1 ("High"): 1-bit
                                                                                      Output 2 ("Time"): UInteger 32
                                                                                      Output 3 ("Low"): 1-bit
                               Output description                                     low: This output is active when the time output is lower than
                                                                                      LowLimit (Information: The 1 ms option is not available).
                                                                                      time: This value increments once per TimeBase whenever
                                                                                      input is active.
                                                                                      high: This output is active when the time output is higher than
                                                                                      the HighLimit.
                               Settings                                               EnableMode: To activate the mode to specify which time is to
                                                                                      be measured. Selection between rising and falling edge of the
                                                                                      input signal or between falling and rising edge (default: rising
                                                                                      edge).
                                                                                      TimeBase: To select the time base for the time measurement
                                                                                      (default: 100 ms)
                                                                                      TimerMode (available from FW 1.3): If in StopWatch mode,
                                                                                      the input is deactivated, the timer pauses at the current
                                                                                      value. The timer can be restarted by activating the input. In
                                                                                      timer mode, the value is reset to 0 when the input signal
                                                                                      becomes active.
                                                                                      HighLimit: Defines an upper value for the Boolean output
                                                                                      signal that is set when the timer value exceeds the defined
                                                                                      upper limit (default: 0).
                                                                                      LowLimit: Defines a lower value for the Boolean output signal
                                                                                      that is set when the timer value falls below the defined lower
                                                                                      limit (default: 0).




108   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                          8016629.1MCE/2024-10-24 | SICK
                                                                                                                                Subject to change without notice

DEVICE FUNCTIONS 8


                                   Description          Monitors the state of the inputs and detects if they are not
                                                        changing as expected within the heartbeat time.
                                   Number of inputs     2
                                   Input data type      Input 1 ... 2: 1-bit
                                   Input description    levelA: first input to be monitored
                                                        levelB: second input to be monitored
                                                        levelC: third input to be monitored
                                                        levelD: fourth input to be monitored
                                   Number of outputs    2
                                   Output data type     Output 1 ... 2: 1-bit
                                   Output description   ok: As long as the input signals are changing, this output will
                                                        be high.
                                                        error: This output will be high in case the input signals are not
                                                        changing within the defined heartbeat time.
                                   Settings             InputCombination: (Any / All) When Any is selected, the ok
                                                        output will stay high as long as at least one input signal
                                                        switches in the heartbeat time.
                                                        If "Input combination" = All, the ok output will only stay high as
                                                        long as all input signals switch within the heartbeat time.
                                                        OutputReset: (Off / Single / Dynamic) If "Output reset" = Off,
                                                        an Err = high (and OK = low) output will stay this way until one
                                                        of the inputs switches again.
                                                        If "Output reset" = Single, Err = high (and OK = low) will
                                                        revert automatically after the "Output duration" has elapsed
                                                        and keep this state until a change in the inputs retrigger the
                                                        heartbeat timer.
                                                        If "Output reset" = Dynamic, Err = high (and OK = low) will
                                                        revert automatically after the "Output duration" has elapsed.
                                                        In this case Err and OK will not revert due to any input
                                                        switching. However, any input switching during this period will
                                                        retrigger the heartbeat time.
                                                        HeartbeatTime: 0...65535 ms Setting of the heartbeat time
                                                        within the input(s) must change.
                                                        OutputDurationTime: 0...65535 ms Setting of the time the
                                                        output signal stays high after a "no input change" condition
                                                        has been detected.




8016629.1MCE/2024-10-24 | SICK                              O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   109
Subject to change without notice

8 DEVICE FUNCTIONS

                                  Description                                            Invert the input signal with a logical NOT.
                                  Number of inputs                                       1
                                  Input data type                                        1-bit (future extension: or n-bit)
                                  Input description                                      levelA: first input value
                                  Number of outputs                                      1
                                  Output data type                                       Identical to input data type
                                  Output description                                     level: the input signal will be inverted with a logical not. Exam‐
                                                                                         ple: a high signal gets converted into a low signal.
                                  Settings                                               No settings available
                                  Description                                            Combine the input signals with a logical AND.
                                  Number of inputs                                       4
                                  Input data type                                        1-bit (future extension: n-bit)
                                  Input description                                      levelA: first input
                                                                                         levelB: second input
AND                                                                                      levelC: third input
                                                                                         levelD: fourth input
                                                                                         Maximum 4 inputs can be linked together. If you want to link
                                                                                         more signals, you can work with several AND blocks.
                                  Number of outputs                                      1
                                  Output data type                                       Identical to input data type
Table 63: Thruth table            Output description                                     level: the output depends on the various inputs. For more
 Input   Input      Out‐                                                                 information see truth table
 A       B          put           Settings                                               No settings available
 1       1          1
 1       0          0
 0       1          0
 0       0          0
                                  Description                                            Combine the input signals with a logical OR.
                                  Number of inputs                                       4
                                  Input data type                                        1-bit (future extension: n-bit)
                                  Input description                                      levelA: first input
                                                                                         levelB: second input
OR                                                                                       levelC: third input
                                                                                         levelD: fourth input
                                                                                         Maximum 4 inputs can be linked together. If you want to link
                                                                                         more signals, you can work with several OR blocks.
                                  Number of outputs                                      1
                                  Output data type                                       Identical to input data type
Table 64: Thruth table            Output description                                     level: the output depends on the various inputs. For more
 Input   Input      Out‐                                                                 information see truth table
 A       B          put           Settings                                               No settings available
 1       1          1
 1       0          1
 0       1          1
 0       0          0




110      O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                            8016629.1MCE/2024-10-24 | SICK
                                                                                                                                     Subject to change without notice

DEVICE FUNCTIONS 8


                                   Description          Combine the input signals with a logical XOR.
                                   Number of inputs     2
                                   Input data type      1-bit (future extension: or n-bit)
 XOR
                                   Input description    levelA: first input
                                                        levelB: second input
                                                        Maximum 2 inputs can be linked together. If you want to link
                                                        more signals, you can work with several XOR blocks.
                                   Number of outputs    1
                                   Output data type     Identical to input data type
 Table 65: Thruth table
                                   Output description   level: the output depends on the various inputs. For more
  Input     Input     Out‐                              information see truth table
  A         B         put
                                   Settings             No settings available
  1         1         0
  1         0         1
  0         1         1
  0         0         0
                                   Description          Combine the input signals with a logical NAND.
                                   Number of inputs     4
                                   Input data type      1-bit (future extension: or n-bit)
                                   Input description    levelA: first input
                                                        levelB: second input
 NAND                                                   levelC: third input
                                                        levelD: fourth input
                                                        Maximum 4 inputs can be linked together. If you want to link
                                                        more signals, you can work with several NAND blocks.
                                   Number of outputs    1
                                   Output data type     Identical to input data type
 Table 66: Thruth table            Output description   level: the output depends on the various inputs. For more
  Input     Input     Out‐                              information see truth table
  A         B         put          Settings             No settings available
  1         1         0
  1         0         1
  0         1         1
  0         0         1




8016629.1MCE/2024-10-24 | SICK                              O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   111
Subject to change without notice

8 DEVICE FUNCTIONS

                                  Description                                            Combine the input signals with a logical NOR.
                                  Number of inputs                                       4
                                  Input data type                                        1-bit (future extension: or n-bit)
                                  Input description                                      levelA: first input
                                                                                         levelB: second input
NOR                                                                                      levelC: third input
                                                                                         levelD: fourth input
                                                                                         Maximum 4 inputs can be linked together. If you want to link
                                                                                         more signals, you can work with several NOR blocks.
                                  Number of outputs                                      1
                                  Output data type                                       Identical to input data type
Table 67: Thruth table            Output description                                     level: the output depends on the various inputs. For more
 Input   Input      Out‐                                                                 information see truth table
 A       B          put           Settings                                               No settings available
 1       1          0
 1       0          0
 0       1          0
 0       0          1
                                  Description                                            Combine the input signals with a logical XNOR.
                                  Number of inputs                                       2
                                  Input data type                                        1-bit (future extension: or n-bit)
XNOR
                                  Input description                                      levelA: first input
                                                                                         levelB: second input
                                                                                         levelC: third input
                                                                                         levelD: fourth input
                                                                                         Maximum 4 inputs can be linked together. If you want to link
                                                                                         more signals, you can work with several XNOR blocks.
Table 68: Thruth table            Number of outputs                                      1
 Input   Input      Out‐          Output data type                                       Identical to input data type
 A       B          put           Output description                                     level: the output depends on the various inputs. For more
 1       1          1                                                                    information see truth table
 1       0          0             Settings                                               No settings available
 0       1          0
 0       0          1


NOTE
Please be aware that the Integer values have a value range from 0....65.535. There is no overflow or underflow
indication.


NOTE
The logic editor does only support integers (e. g. 2) and no decimal numbers (e. g. 2,345). In case, the calculated
result would be a decimal number, the logic editor will round up or down.




112      O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                         8016629.1MCE/2024-10-24 | SICK
                                                                                                                                  Subject to change without notice

TROUBLESHOOTING 9


9                  Troubleshooting
                                   The Troubleshooting table indicates measures to be taken if the sensor stops working.


Troubleshooting/LEDs
                                   Table 69: LED status indicators
                                   LED            Display                    Meaning
                                   Supply volt‐   green          O           Power on
                                   age
                                                  Off            o           Power off
                                                  Flashing       Ö           A serious error has occurred. Please contact your SICK
                                                  green                      service partner.
                                   MS (Module     dark           o           The module has no power
                                   status)
                                                  red / green    alter‐      Self-test when switching on
                                                                 nately
                                                                 Ö
                                                  green          O           Device in operation
                                                  green blink‐   Ö           Device in standby, no IP address assigned
                                                  ing
                                                  red            O           Error (device not in operation)
                                                  red blinking   Ö           Warning (but device in operation)
                                   NS (Network dark              o           No voltage or IP address
                                   status)
                                               red / green       alter‐      Self-test when switching on
                                                                 nately
                                                                 Ö
                                                  green          O           Valid IP address and CIP connection
                                                  green blink‐   Ö           Valid IP address, no connection
                                                  ing
                                                  red            O           IP address assigned to a different device
                                                  red blinking   Ö           Connection timeout
                                   LINK ACT 1 dark               o           No network connection on port 1
                                   (Link / Activ‐
                                                  green          O           Network connection on port 1
                                   ity 1)
                                   LINK ACT 2 dark               o           No network connection on port 2
                                   (Link / Activ‐
                                                  green          O           Network connection on port 2
                                   ity 2)

                                   LED                               Indication                     Meaning
                                   DI: LED for pin 2                 amber                          Additional DI on pin 2
                                                                     off                            No additional DI on pin 2
                                   C/DI/DO LED for pin 4             green                          Pin 4 - IO-Link communication active
                                                                     green blinking                 Pin 4 - no IO-Link communication active




8016629.1MCE/2024-10-24 | SICK                                             O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   113
Subject to change without notice

10 DISASSEMBLY AND DISPOSAL


10            Disassembly and disposal
                                     The SIG200 must be disposed of according to the applicable country-specific regula‐
                                     tions. Efforts should be made during the disposal process to recycle the constituent
                                     materials (particularly precious metals).

                                     NOTE
                                     Disposal of batteries, electric and electronic devices
                                     • According to international directives, batteries, accumulators and electrical or
                                         electronic devices must not be disposed of in general waste.
                                     • The owner is obliged by law to return this devices at the end of their life to the
                                         respective public collection points.
                                      •


                                                       This symbol on the product, its package or in this document, indicates
                                              that a product is subject to these regulations.




114   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                        8016629.1MCE/2024-10-24 | SICK
                                                                                                              Subject to change without notice

MAINTENANCE 11


11                 Maintenance
                                   SICK sensor integration gateways are maintenance-free.
                                   We recommend doing the following regularly:
                                   •    Clean the device
                                   •    Check the screwed and plugged connections
                                   No modifications may be made to devices.
                                   Subject to change without notice. Specified product properties and technical data are
                                   not written guarantees.




8016629.1MCE/2024-10-24 | SICK                                       O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   115
Subject to change without notice

12 TECHNICAL DATA


12             Technical data
12.1           General technical data
                                      Mechanical data
                                                                                                                                                     57 (2.24)                         38.3 (1.51)
                                                                                                                                                   30 (1.28)                           9 (0.35)




                                                                   IO-Link 1: L+            POWER
                                                                                                         CONFIG
                                                        1: TX+
                                                                                                                                                    POWER        CONFIG



                                                                                                                1: +VDC
                                                                                                1 1: L+
                                                                                                                                          POWER                                          POWER


                                                                 1        2 2: DI          2
                                                                                                                                             MS                                               MS
                                                                                                                                             NS

                                                        2: RX+
                                                                                                                                                                                              NS
                                                                                                                                                            SIG200
                                                                                  2


                                                                                                   2: NC        2: –DATA
                                                                                                                                            /DO             S1                          C/DI/DO
                                                                                                                                              DI                                               DI



                                                        3: TX– 5
                                                                             3: 0V                                                          /DO                                         C/DI/DO


                                                                                                   3: 0V        3: 0V
                                                                                                                                                            S2
                                                                                                                                              DI                                               DI

                                              3       4          3         4                     3
                                                                                          4
                                                                                                                           213.9 (8.42)
                                                                             4: C/DI1/DO1
                                                        4: RX–
                                                                                                                                            /DO                                         C/DI/DO


                                                                                                                4: +DATA
                                                                                                                                                            S3

                                                                                                   4: NC
                                                                                                                                              DI                                               DI
                                                                                                                           198.5 (7.81)

                                               P1 - P2 5: NC       S1 - S4 5: NC
                                                              2
                                                                                                                                            /DO                                         C/DI/DO

                                               EhterNET I/P
                                                                                                                                                            S4
                                                              1                                                                               DI                                               DI

                                                                     IO-Link 5


                                                                                                                                            LINK                                             LINK
                                                                                                                                                            P2
                                                     SIG200-0A0512200                                                                       ACT2                                             ACT2
                                                     1089796
                                                     10-30 VDC
                                                     OUT <100 mA                                                                            LINK                                             LINK
                                                                                                                                                            P1
                                                     Assembles in USA IND. CONT.87LL
                                                                                                                                            ACT1                                             ACT1
                                                                                  EQ
                                                     LN {YYWW}:       Type 1 Enc.




                                                                                                                                                                                       28 (1.1)
                                                                                                                                                                                       36 (1.42)

                                      Figure 25: Dimensional drawing


                                       Housing material                                                                                                                   Zinc
                                       Enclosure rating per IEC 60529                                                                                                     IP 67 (only when plugged-in and threaded-in)1
                                       Dimensions (W x H x D)                                                                                                             213.9 x 38.3 x 57 mm
                                       Mounting type                                                                                                                      Mounting slots front and side
                                       Weight                                                                                                                             520 g
                                      1     If cables are not plugged in the connector caps supplied with the device must be tightened to 0.35 Nm

                                      Operating conditions
                                       Operating temperature                                                                                                              -40 °C ... +55°C
                                       Storage temperature                                                                                                                -40 °C ... +75°C




116    O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                                                                                                 8016629.1MCE/2024-10-24 | SICK
                                                                                                                                                                                                        Subject to change without notice

TECHNICAL DATA 12


                                   EMC                                                         - EN 61000-6-2
                                   - Immunity                                                  - EN 61000-6-4
                                   - Emission
                                                                                               CAUTION
                                                                                               This equipment is not intended for use in resi‐
                                                                                               dential environments and may not provide ade‐
                                                                                               quate protection to radio reception in such
                                                                                               environments.

                                   Shock / shaking                                             EN 60068-2-6, EN 60068-2-27

                                   Electrical data
                                   Power supply          10 ... 30 V DC
                                   Power Supply IO-      18 ... 30 V DC
                                   Link
                                   Voltage ripple        <1%
                                   Device (Power         Max. device current (without con‐                    ≤ 175 mA @ 24 V
                                   Port)                 nected sensors)
                                                         Max. device current1                                 ≤ 3,000 mA
                                   Port (S1-S4)          Pin 1 max. supply current       2
                                                                                                              500 mA
                                                         Pin 4 max. output supply current           3
                                                                                                              200 mA
                                                         Pin 4 output characteristics                         VH ≥ VUS - 3 V
                                                         Pin 2 input characteristics                          Type 3 IEC 61131-2
                                                         Pin 4 input characteristics                          Type 1 IEC 61131-2
                                   1   The sum of all ports including digital outputs must not exceed the maximum device current. Current
                                       needs to be limited.
                                   2   Max. port current includes both the digital current output (Pin 4) and the connected device's current
                                       consumption (Pin 1).
                                   3   Pin 4 configured as digital output. Maximum output supply current is independent of Pin 1.

                                   EtherNet/IP
                                   Properties                                   Values
                                   Transmission rate                            10 or 100 Mbit/s
                                   Maximum distance between nodes               100 m
                                   Process data (implicit connection)           Depending on selected assemblies
                                                                                Minimum cycle time: 2 ms
                                   Max. process input data                      328 byte
                                   Max. process output data                     262 byte
                                   Asynchronous data (explicit connec‐          Manufacturer-specific classes per module
                                   tion)
                                   Observed standard                            IEEE802.3u (100Base-Tx)
                                   Max. number of connections                   8
                                   Ethernet ports                               2
                                   CIP services                                 DLR, QoS
                                   EDS file                                     Available at www.sick.com

                                   Ethernet
                                   Ethernet interface                                          2x100 Base-Tx (switched)
                                   Cable type acc. to IEEE 802.3                               Min. STP CAT 5 / ST CAT 5e
                                   Data transmission rate                                      100 Mbits/s


8016629.1MCE/2024-10-24 | SICK                                                O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   117
Subject to change without notice

12 TECHNICAL DATA

                                      Max. distance between nodes                             100 m
                                      Flow control                                            Half Duplex / Full Duplex (IEEE 802.33x
                                                                                              Pause)
                                      Used Ethernet protocols                                 ICMP, TCP, UDP
                                      Open TCP ports                                          80 (HTTP), 2111/2113/2122 (SOPAS)
                                      Open UDP ports                                          1900 (UPNP)

                                     Further information:
                                      Initialization time after switch on:                    70 s, if no iodd file installed
                                                                                              80 s maximum, if iodd is installed on each port
                                      IODD upload time                                        40 s for USB connection and 20 s for Ethernet
                                                                                              connection (typical time for 150 kB file size)
                                      Max. number of I/Os which can be connected:             52 I/Os (together with 4 SIG100)
                                      Max. number of IO-Link signals which can be             4
                                      connected:
                                      Ethernet Ports:                                         2
                                      Max. Output frequency:                                  35 Hz12
                                     1     With basic logic, not gate logic
                                     2     Max. frequency will vary depending on logic configuration

                                     IO-Link:
                                      Specification:                                          V1.1.
                                      Port Class:                                             A
                                      Transfer rate:                                          COM1 / COM2 / COM3
                                      Min. IO-Link cycle time                                 1 ms
                                      Input specification:                                    IO-Link specification EN61131-2, type 1
                                      Transfer rate recognition:                              automatic

                                     Product safety
                                     Table 70: Product safety data
                                      Protection class                                        3
                                      Short-circuit protection                                in accordance with VDE 0160




118   O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200                                  8016629.1MCE/2024-10-24 | SICK
                                                                                                                        Subject to change without notice

ANNEX 13


13                 Annex
13.1               Conformities and certificates
                                   You can obtain declarations of conformity, certificates and the current documentation
                                   for the product at www.sick.com. To do so, enter the product part number in the search
                                   field (part number: see the entry in the “P/N” or “Ident. no.” field on the type label).




8016629.1MCE/2024-10-24 | SICK                                       O P E R A T I N G I N S T R U C T I O N | Sensor Integration Gateway - SIG200   119
Subject to change without notice

8016629.1MCE/2024-10-24/en
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