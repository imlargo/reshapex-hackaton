OPERATING INSTRUCTIONS


FlexChain

Described product
                                     FlexChain

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

                                     FlexChain Host



                                                                                                  LISTED
                                                                                                E502493
                                                                                                Prog.Cntlr.

                                                                                                                      NO

                                                                                                                  2006/42/EC
                                                                                                                   SAFETY




                                     FlexChain Adapter and Booster




                                                                                                                      NO

                                                                                                                  2006/42/EC
                                                                                                                   SAFETY




2   O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                     8023047.1Q01/2025-01-29 | SICK
                                                                                                                 Subject to change without notice

CONTENTS


Contents
                                   1   About this document........................................................................                              5
                                       1.1     Information on the operating instructions..............................................                           5
                                       1.2     Symbols and document conventions......................................................                            5
                                       1.3     Further information...................................................................................            5
                                       1.4     Customer service......................................................................................            6

                                   2   Safety information............................................................................                           7
                                       2.1     Intended use.............................................................................................        7
                                       2.2     Limitation of liability.................................................................................         8
                                       2.3     Qualification of personnel........................................................................               8
                                       2.4     Hazard warnings and operational safety.................................................                          8
                                       2.5     Repair........................................................................................................   8

                                   3   Product description...........................................................................                           9
                                       3.1     Product identification via the SICK product ID.......................................                             9
                                       3.2     Product features and functions...............................................................                     9
                                               3.2.1     Device view...............................................................................              9

                                   4   Mounting............................................................................................. 11
                                       4.1     Scope of delivery.......................................................................................         11
                                       4.2     Installation requirements.........................................................................               11
                                       4.3     Installing the system.................................................................................           11

                                   5   Electrical installation........................................................................ 12
                                       5.1     Notes on electrical installation................................................................                 12
                                       5.2     Schematic arrangement...........................................................................                 13
                                       5.3     Pin assignment of the connections.........................................................                       14
                                       5.4     Connecting the supply voltage.................................................................                   15
                                       5.5     Digital interfaces.......................................................................................        16

                                   6   Commissioning.................................................................................. 17
                                       6.1     Commissioning via the control panel......................................................                        17

                                   7   Operation............................................................................................ 20
                                       7.1     Configuring the FlexChain system...........................................................                      20
                                               7.1.1     Functions structure..................................................................                  20
                                               7.1.2     Structure of SOPAS..................................................................                   21
                                               7.1.3     Basic information on the FlexChain system...........................                                   22
                                               7.1.4     Teach & Positioning.................................................................                   23
                                               7.1.5     Zones........................................................................................          28
                                               7.1.6     Logics........................................................................................         32
                                               7.1.7     PINS..........................................................................................         34
                                               7.1.8     Process data............................................................................               36
                                               7.1.9     Settings....................................................................................           39
                                       7.2     IO-Link specific settings...........................................................................             41

8023047.1Q01/2025-01-29 | SICK                                                                          O P E R A T I N G I N S T R U C T I O N S | FlexChain    3
Subject to change without notice

CONTENTS


                                                  7.3        CANopen-specific settings.......................................................................                41
                                                             7.3.1   Overview...................................................................................             41
                                                             7.3.2   Acyclic data (service data).......................................................                      45
                                                             7.3.3   Cyclic data (process data).......................................................                       45
                                                             7.3.4   Object library............................................................................              46
                                                             7.3.5   1xxxh – Standard objects........................................................                        47
                                                             7.3.6   Standard object for defining process data............................                                   50
                                                  7.4        RS485 configuration................................................................................             55

                                      8           Diagnostics and troubleshooting.................................................... 58
                                                  8.1        General diagnostic information...............................................................                   58
                                                  8.2        Detailed diagnostic information...............................................................                  58
                                                  8.3        Troubleshooting........................................................................................         63

                                      9           Maintenance...................................................................................... 65
                                                  9.1        Servicing....................................................................................................   65
                                                  9.2        Maintenance.............................................................................................        65

                                      10          Decommissioning............................................................................. 66
                                                  10.1 Disassembly and disposal.......................................................................                       66
                                                  10.2 Returning devices.....................................................................................                66

                                      11          Technical data.................................................................................... 67
                                                  11.1 Host performance.....................................................................................                 67
                                                  11.2 Interfaces host..........................................................................................             67
                                                  11.3 Host software features.............................................................................                   68
                                                  11.4 System response time..............................................................................                    68
                                                  11.5 Mechanics/electronics/host....................................................................                        68
                                                  11.6 Technical data guests...............................................................................                  69
                                                       11.6.1 Technical data G6-C – general...............................................                                   69
                                                       11.6.2 Technical data GL6-C..............................................................                             70
                                                       11.6.3 Technical data GSE6-C............................................................                              70
                                                       11.6.4 Technical data GTB6-C............................................................                              70
                                                       11.6.5 Technical data SLG-2...............................................................                            70
                                                       11.6.6 Technical data Adapter............................................................                             73
                                                       11.6.7 Technical data Booster............................................................                             74
                                                  11.7 Dimensional drawings..............................................................................                    75
                                                  11.8 FlexChain Host control panel...................................................................                       83

                                      12          Accessories........................................................................................ 84

                                      13          Annex.................................................................................................. 85
                                                  13.1 EU declaration of conformity and certificates........................................                                 85
                                                  13.2 Licenses....................................................................................................          85




4    O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                                                     8023047.1Q01/2025-01-29 | SICK
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

1.2                Symbols and document conventions
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

                                   Instructions to action
                                   ►    The arrow denotes instructions to action.
                                   1.   The sequence of instructions is numbered.
                                   2.   Follow the order in which the numbered instructions are given.
                                   ✓    The tick denotes the results of an action.

1.3                Further information
                                   You can find the product page with further information via the SICK Product ID:
                                   pid.sick.com/{P/N}/{S/N}
                                   (see "Product identification via the SICK product ID", page 9).
                                   The following information is available depending on the product:
                                   • This document in all available language versions
                                   • Data sheets

8023047.1Q01/2025-01-29 | SICK                                                        O P E R A T I N G I N S T R U C T I O N S | FlexChain   5
Subject to change without notice

1 ABOUT THIS DOCUMENT

                                       •        Other publications
                                       •        CAD files and dimensional drawings
                                       •        Certificates (e.g., declaration of conformity)
                                       •        Software
                                       •        Accessories

1.4           Customer service
                                       If you require any technical information, our customer service department will be happy
                                       to help. To find your agency, see the final page of this document.

                                       NOTE
                                       Before calling, make a note of all type label data such as type code, serial number, etc.,
                                       to ensure faster processing.




6     O P E R A T I N G I N S T R U C T I O N S | FlexChain                                               8023047.1Q01/2025-01-29 | SICK
                                                                                                             Subject to change without notice

SAFETY INFORMATION 2


2                  Safety information
                                   This document is an original document of SICK AG. All rights reserved. Subject to
                                   change without notice.
                                   Read these safety notes and take them into account when working with the sensor. The
                                   safety notes do not describe how to use the sensor.
                                   You can find technical data and information on commissioning the sensor in the oper‐
                                   ating instructions. They can be downloaded at this Internet site: www.sick.com (enter
                                   the part number of the sensor in the search field and you will find the operating
                                   instructions under Downloads).

                                                     - Connection, mounting, and setting is only to be performed by trained
                                                     specialists.
                                       NO            - Not a safety component in accordance with the EU Machinery Direc‐
                                    2006/42/EC
                                     SAFETY
                                                     tive.

                                                     - Do not install the sensor in places exposed to direct sunlight or other
                                                     weather conditions unless this is expressly permitted in the operating
                                                     instructions.




                                   WARNING
                                   Fire
                                   Electrical connections must be made in compliance with local and national electrical
                                   regulations and standards. The sensor must be protected with a fuse suitable for the
                                   cross-circuit of the connecting cable; for details, see the operating instructions.

                                   For devices with a supply voltage > 50 V (AC), 75 V (DC):

                                   WARNING
                                   Lost of electrical safety (protection class)
                                   When commissioning, protect the device from moisture and contamination.
                                   Unless stated otherwise in the operating instructions, the sensor may only be used in
                                   an area with maximum degree of contamination 3, maximum overvoltage category II
                                   and a maximum altitude of 2,000 m above sea level.


2.1                Intended use
                                   The FlexChain is a sensor system comprising a central unit (host) and connected guests
                                   (sensors) that is used for optical and non-contact detection of objects.
                                   The FlexChain must be mounted and installed according to these operating instruc‐
                                   tions, and may only be operated according to its intended function.
                                   The FlexChain is not equipped with any direct safety devices. The system designer must
                                   provide measures to ensure the safety of persons and systems in accordance with the
                                   legal guidelines.
                                   Sick AG assumes no liability for losses or damage arising from the use of the product,
                                   either directly or indirectly. This applies in particular to use of the product that does not
                                   conform to its intended purpose and is not described in this documentation.




8023047.1Q01/2025-01-29 | SICK                                                          O P E R A T I N G I N S T R U C T I O N S | FlexChain   7
Subject to change without notice

2 SAFETY INFORMATION

2.2           Limitation of liability
                                       Applicable standards and regulations, the latest state of technological development,
                                       and our many years of knowledge and experience have all been taken into account
                                       when assembling the data and information contained in these operating instructions.
                                       The manufacturer accepts no liability for damage caused by:

                                       ■        Failure to observe the operating instructions
                                       ■        Improper use
                                       ■        Use by untrained personnel
                                       ■        Unauthorized conversions
                                       ■        Technical modifications
                                       ■        Use of unauthorized spare parts, wear and tear parts, and accessories

                                       With special variants, where optional extras have been ordered, or owing to the latest
                                       technical changes, the actual scope of delivery may vary from the features and illustra‐
                                       tions shown here.

2.3           Qualification of personnel
                                       Any work on the product may only be carried out by personnel qualified and authorized
                                       to do so.
                                       Qualified personnel are able to perform tasks assigned to them and can independently
                                       recognize and avoid any potential hazards. This requires, for example:
                                       •        technical training
                                       •        experience
                                       •        knowledge of the applicable regulations and standards

2.4           Hazard warnings and operational safety
                                       Please observe the safety notes and the warnings listed here and in other chapters
                                       of these operating instructions to reduce the possibility of risks to health and avoid
                                       dangerous situations.

2.5           Repair
                                       The product is replaced if defective. The device is not intended to be repaired. Interfer‐
                                       ence with or modifications to the device on the part of the customer will invalidate any
                                       warranty claims against SICK AG.




8     O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                8023047.1Q01/2025-01-29 | SICK
                                                                                                              Subject to change without notice

PRODUCT DESCRIPTION 3


3                  Product description
3.1                Product identification via the SICK product ID
                                   SICK product ID
                                   The SICK product ID uniquely identifies the product. It also serves as the address of the
                                   web page with information on the product.
                                   The SICK product ID comprises the host name pid.sick.com, the part number (P/N),
                                   and the serial number (S/N), each separated by a forward slash.
                                   For many products, the SICK product ID is displayed as text and QR code on the type
                                   label and/or on the packaging.




                                   Figure 1: SICK product ID


3.2                Product features and functions

3.2.1              Device view
                                                          500 (19.69)                          109.4 (4.31)                      1,500 (59.06)
                                                                  300 (11.81)            15.9 (0.63)
                                                                                                   82.6 (3.25)                 5.5 (0.22)
                                                   4                                                  6                                                      1
                                    3



                                                                         20.1   (0.79)                                        5.5 (0.22)
                                                                                                                                                             2
                                               5                                                                              24 (0.94)
                                                                  300 (11.81)                                                 35 (1.38)

                                   Figure 2: Sample view of FlexChain Host CANopen variant
                                   1      Port-A, pigtail M8, 4-pin, female
                                   2      Port B, pigtail M8, 4-pin, female
                                   3      PLC PLC, pigtail M12, 5-pin, male
                                   4      CANopen PLC, pigtail M12, 5-pin / 8-pin, male
                                   5      Micro USB
                                   6      Control panel

                                   Structure
                                   A FlexChain system comprises a host and a number of guests (sensors). As shown in
                                   the image below, the system components are connected sequentially (bus topology).
                                   A system comprises a host and at least one guest. A total of up to 60 guests can be
                                   connected to one host (the number depends on the type of sensors connected).




8023047.1Q01/2025-01-29 | SICK                                                                       O P E R A T I N G I N S T R U C T I O N S | FlexChain       9
Subject to change without notice

3 PRODUCT DESCRIPTION




                                      Figure 3: Structure of FlexChain system

                                      Function
                                      The FlexChain system operates similarly to a light grid. That is, each individual channel
                                      in the system is processed sequentially. This principle means that only one channel
                                      at a time is active. Consequently, there is no possibility of mutual interference within
                                      a system, and the guests can be installed arbitrarily close to one another without
                                      any interference occurring. Due to this sequential processing, the scan time and the
                                      response time of the system depend on the number of connected guests. The total
                                      times are short, however, because the processing interval between two channels is in
                                      the µs range (see "Technical data", page 67).
                                      With the FlexChain system and in SOPAS, the term “channel” is used to cover the varia‐
                                      tions of sensors and actuators that can be used. For example, light grids, photoelectric
                                      sensors and photoelectric retro-reflective sensors are light beams.
                                      Host:
                                      –        Supplies the guests with current.
                                      –        Collects the status of each individual channel.
                                      –        Requests diagnostic data from the individual guests.
                                      –        Processes the collected data (if desired).
                                      –        Forwards the collected and/or processed data via various interfaces.
                                      Guest:
                                      –        Guests are connected to one another via a standard M8 pigtail.
                                      –        Guests forward information to the host.
                                      –        Can be arranged differently within the system.
                                      –        Guests employing different sensor technologies can be integrated into the same
                                               system.
                                      –        Senders & receivers that belong together must be connected to separate ports.

                                      NOTE
                                      Mutual interference is managed by the host exclusively for sensors that belongs to
                                      the FlexChain system. This feature is not valid for optical sensors connected to the
                                      FlexChain Adapter, since the host only read the output status and have no control over
                                      the sender LED from the device connected to the Adapter. Therefore, it's not possible to
                                      prevent cross-talk issues with other devices/guests in this situation.




10   O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                8023047.1Q01/2025-01-29 | SICK
                                                                                                             Subject to change without notice

MOUNTING 4


4                  Mounting
4.1                Scope of delivery
                                   •    FlexChain host with 2x bus terminator
                                   •    Quickstart
                                   •    Safety notes
                                   The FlexChain guests and mounting accessories are not included in the scope of
                                   delivery and need to be purchased separately.

4.2                Installation requirements
                                   •    Typical space requirement for the device, see type-specific dimensional drawing,
                                        see "Technical data", page 67.
                                   •    Comply with technical data, such as the permitted ambient conditions for opera‐
                                        tion of the device (e.g., temperature range, EMC interference emissions, ground
                                        potential).
                                   •    To prevent condensation, avoid exposing the device to rapid changes in tempera‐
                                        ture.
                                   •    Protect the device from direct sunlight.
                                   •    Protect the device from external light sources.
                                   •    The device must only be mounted using the pairs of mounting threads/fixing holes
                                        provided for this purpose.
                                   •    Shock and vibration-free mounting.

4.3                Installing the system
                                   Installing the FlexChain host
                                                                             <0,7 Nm




                                   Figure 4: FlexChain host - installation


                                         –25°C ... +50 °C
                                         –13°F ... +122 °F



                                   Figure 5: Temperature

                                   Installing the FlexChain guest
                                   The procedure for installing a guest can vary significantly depending on the device
                                   family or device type. See the instructions supplied with the device for installation
                                   instructions.




8023047.1Q01/2025-01-29 | SICK                                                        O P E R A T I N G I N S T R U C T I O N S | FlexChain   11
Subject to change without notice

5 ELECTRICAL INSTALLATION


5             Electrical installation
5.1           Notes on electrical installation

                                       NOTICE
                                       Equipment damage due to incorrect supply voltage!
                                       An incorrect supply voltage may result in damage to the equipment.
                                       ■        Only operate the host with safety/protective extra-low voltage (SELV/PELV).
                                       ■        The host is a device of protection class III.


                                       NOTICE
                                       Equipment damage due to incorrect supply voltage!
                                       An incorrect supply voltage may result in damage to the equipment.
                                       •        Only operate the host with an LPS (limited power source) in accordance with IEC
                                                60950-1 or an NEC Class 2 power supply unit.


                                       NOTICE
                                       Equipment damage or unpredictable operation due to working with live parts!
                                       Working with live parts may result in unpredictable operation.
                                       ■        Only carry out wiring work when the power is off.
                                       ■        Only connect and disconnect electrical connections when the power is off.


                                       NOTICE
                                       Device damage due to incorrect connection!
                                       Incorrect connection may result in damage to the FlexChain system or peripheral devi‐
                                       ces.
                                       ■        If connection cables are required, use twisted pair connection cables.
                                       ■        Standard M8 4-pin connection cables can also be used in many applications.

                                       ■        The electrical installation must only be performed by electrically qualified person‐
                                                nel.
                                       ■        Standard safety requirements must be observed when working on electrical
                                                systems!
                                       ■        Only switch on the supply voltage for the device when the connection tasks have
                                                been completed and the wiring has been thoroughly checked.
                                       ■        When using extension cables with open ends, ensure that bare wire ends do not
                                                come into contact with each other (risk of short-circuit when supply voltage is
                                                switched on!). Wires must be appropriately insulated from each other.
                                       ■        Wire cross-sections in the supply cable from the user’s power system must be
                                                selected in accordance with the applicable standards.
                                       ■        Only operate the device with an LPS (limited power source) in accordance with IEC
                                                60950-1 or an NEC Class 2 power supply unit.
                                       ■        All circuits connected to the device must be designed as SELV/PELV circuits.
                                       ■        Operation in short-circuit protected network at max. 8 A.




12    O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                  8023047.1Q01/2025-01-29 | SICK
                                                                                                                Subject to change without notice

ELECTRICAL INSTALLATION 5


                                   NOTE
                                   Layout of data cables
                                   ■    Use shielded data cables with twisted-pair wires.
                                   ■    Implement the shielding design correctly and completely.
                                   ■    To avoid interference, e.g., from switching power supplies, motors, clocked drives,
                                        and contactors, always use cables and layouts that are suitable for EMC.
                                   ■    Do not lay cables over long distances in parallel with voltage supply cables and
                                        motor cables in cable channels.

                                   The IP enclosure rating for the device is only achieved under the following conditions:
                                   ■    The cables plugged into the connections are screwed tight.
                                   If these instructions are not complied with, the IP enclosure rating for the device is not
                                   guaranteed!

5.2                Schematic arrangement
                                   The first guest is connected to the host using the pigtail. It can be connected to either
                                   port A or port B. Up to 30 sensors in total can be connected per port.
                                   All guests have an M8 4-pin male connector and an M8 4-pin female connector (pig‐
                                   tail). The pigtail can always be connected to the male connector of the next guest.
                                   The bus terminator must be connected at the end of the system. This is included in the
                                   scope of delivery of the FlexChain host.
                                   With regard to the arrangement of the guests on Port A and Port B, there is only one
                                   restriction for sender and receiver sensors: the sender and the associated receiver
                                   must not be connected to the same port.
                                   If the pigtail cable is insufficiently long, it can be extended using an M8 4-pin cable.
                                   Ensure that the total cable length of the system does not exceed 40 m when doing so.

                                   NOTE
                                   Sender-receiver assignment:
                                   The assignment of senders and receivers must be taken into account when setting up
                                   the guest chains and cannot be determined directly via the configuration parameters.
                                   This is based on the automatic assignment algorithm.
                                   Assignment algorithm:
                                   The first address (A1) is considered starting from port A. If a counterpart is needed
                                   for this, the addresses of port B are checked for suitability in ascending order, starting
                                   with B1. If an counterpart is found (e.g. B3), the next address at port A that requires an
                                   counterpart (e.g. A3) is considered.
                                   However, the search for the matching partner does not start again at B1 but after
                                   the previously found counterpart on port B (in the example, from B4). “Crossed” assign‐
                                   ments of sender-receiver pairs are not possible if the chains at ports A and B are
                                   regarded as two parallel lines. If no counterpart is found during the aforementioned
                                   iteration, the "Error: Sender Missing“ or ”Error: Receiver Missing" message is displayed
                                   via the Chain Issue (IO-Link index 300).
                                   "Error: Incompatible Sender Receiver Couple" is reported if an counterpart is present
                                   but incompatible (e.g. if the sender has more channels than the receiver).
                                   The algorithm terminates when the first error is found, since the system cannot be
                                   run in this state. In order to catch all of the aforementioned errors correctly, port B is
                                   processed after all addresses of port A have been processed.




8023047.1Q01/2025-01-29 | SICK                                                         O P E R A T I N G I N S T R U C T I O N S | FlexChain   13
Subject to change without notice

5 ELECTRICAL INSTALLATION




                                                                      FlexChain Host
                                                 Port A                                                  Port B



                                       A1                                                                            B1


                                                                                                                     B2


                                       A2                                                                            B3

                                       A3                                                                            B4




                                                                                                                     B5


                                       A4

                                       Figure 6: Schematic arrangement


5.3           Pin assignment of the connections
                                       Overview of pin assignment - FlexChain host
                                       Table 1: DC
                                         Flex‐                                                   PLC
                                         Chain
                                         Host                                                                                CANopen                                      Port-A /
                                                        Standard          Advanced                                                                  micro USB
                                                                                               RS485                                                                       Port-B
                                                         IO-Link           IO-Link                                                CAN con‐
                                                                                                              System/Q
                                                                                                                                   nector
                                             1              + (L+)             + (L+)           + (L+)             + (L+)              n.c.             +5V                CANH
                                             2             Q2 / IN1           Q2 / IN1         Q2 / IN1           Q2 / IN1             n.c.               D-               CANL
                                             3                M                  M                M                  M                 GND               D+               12Vout
                                             4             Q1 / C             Q1 / C           Q1 / C             Q1 / C              CAN1_H             n.c.              GND
                                             5             Q3 / In2           Q3/IN2             n.c.               n.c.              CAN1_L            GND                  -
                                             6                -               Q4/IN3             n.c.                -                  -                  -
                                             7                -               Q5/IN4       RS485_A                   -                  -                  -
                                             8                -               Q6/IN5       RS485_B                   -                  -                  -
                                                                  5       5              8 5              8              5                  5                         4              1
                                                       4              3                                       4               3   4             3
                                                                          6              4 6              4
                                                                          7              3 7              3
                                                                                                                                                     5 4 3 2 1
                                                       1              2   1              2 1              2   1               2   1             2                     3              2




14    O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                                                         8023047.1Q01/2025-01-29 | SICK
                                                                                                                                                       Subject to change without notice

ELECTRICAL INSTALLATION 5


                                   The system can be configured via the USB interface, SOPAS, CANopen and IO-Link. A
                                   micro USB -> USB-A adapter cable is required to connect to a computer.

                                   Overview of pin assignment - FlexChain guests
                                   Table 2: DC
                                         Guest
                                           1                                        CAN high
                                           2                                        CAN low
                                           3                                         12 Vout
                                           4                                          GND
                                                                               3                       1



                                                                               4                       2

                                   Table 3: Adapter
                                        Adapter
                                           1                                          24 V
                                           2                                            nc
                                           3                                          GND
                                           4                                  Input (Sensor output)

                                   Table 4: Booster
                                        Booster
                                           1                                          24 V
                                           2                                            nc
                                           3                                          GND
                                           4                                            nc


5.4                Connecting the supply voltage

                                   NOTICE
                                   Risk of damage to the host!
                                   The host can become damaged if it is connected to a voltage supply that is already
                                   switched on.
                                   •    Only connect the host when the supply cable is de-energized.

                                   The host must be connected to a power supply unit with the following properties:
                                   •    24 V voltage supply ± 20% or DC 19.2 V – 28.8 V (SELV/PELV as per currently
                                        applicable standards)
                                   •    The current consumption depends on the number of connected sensors and is
                                        typically 100 mA and maximum 600 mA @ 24 V
                                   To ensure protection against short-circuits/overload in the customer’s supply cables,
                                   the wire cross-sections used must be appropriately selected and protected.
                                   The Booster must be connected to a power supply unit with the following properties:
                                   24 V voltage supply ± 10% or DC 21.6 V – 26.4 V (SELV/PELV as per currently applica‐
                                   ble standards)




8023047.1Q01/2025-01-29 | SICK                                                       O P E R A T I N G I N S T R U C T I O N S | FlexChain   15
Subject to change without notice

5 ELECTRICAL INSTALLATION

5.5           Digital interfaces
                                       The digital interfaces can be configured via SOPAS, Engineering Tool or directly via the
                                       CANopen and IO-Link serial interfaces. Apart from PIN4, every digital interface can be
                                       configured as a digital input or digital output.
                                       Each digital interface can be assigned different functions (see "Operation", page 20).
                                       The signal state of each individual interface (HIGH/LOW) is shown on the FlexChain
                                       Host display.
                                       If a PIN is configured as input, the appropriate PIN must to be connected to either GND
                                       or L+.




16    O P E R A T I N G I N S T R U C T I O N S | FlexChain                                               8023047.1Q01/2025-01-29 | SICK
                                                                                                             Subject to change without notice

COMMISSIONING 6


6                  Commissioning
6.1                Commissioning via the control panel

                                   NOTE
                                   The commissioning described here is carried out via the control panel, commissioning
                                   via SOPAS ET, IO-Link, CANopen is also possible.
                                   Perform any other operation with the SOPAS ET user interface. Download at:
                                   www.sick.com

                                   1.   Connect sensors to port A and port B.
                                   2.   Connect the power supply. The Power LED lights up green.
                                   3.   Perform AutoAssign
                                        AutoAssign detects all connected guests. Automated assignment of guest posi‐
                                        tions and zones, e.g. A1 ... AN, B1 ... BM.

                                                      Menu




                                                    >2s
                                                      Menu

                                   4.   Perform teach-in
                                        Perform teach-in for sensors. Set sensors with potentiometer directly on the sen‐
                                        sor.

                                                      Menu




                                                    >2s
                                                      Menu

                                   5.   Baud rate (RS485, CANopen)
                                        Set baud rate (BDR) for FlexChain Host variant with RS485 and CANopen.




8023047.1Q01/2025-01-29 | SICK                                                       O P E R A T I N G I N S T R U C T I O N S | FlexChain   17
Subject to change without notice

6 COMMISSIONING


                                                               Menu




                                                               Menu




                                                             >2s
                                                               Menu


                                                             >2s


                                                                      kbaud
                                                RS485                 9.6, 38.4, 115.2, 230.4, 460.8
                                                CANopen               50, 125, 250, 500, 1,000




18   O P E R A T I N G I N S T R U C T I O N S | FlexChain                                             8023047.1Q01/2025-01-29 | SICK
                                                                                                          Subject to change without notice

COMMISSIONING 6


                                   6.   NodeID (CANopen)
                                        Set NodeID (NID) for FlexChain Host with CANopen. A single value or several
                                        values can be set or deleted (bit display).
                                        A power cycle is required after changing the CANopen baud rate and NodeID.

                                                      Menu




                                                      Menu




                                                   >2s
                                                      Menu


                                                   >2s




8023047.1Q01/2025-01-29 | SICK                                                     O P E R A T I N G I N S T R U C T I O N S | FlexChain   19
Subject to change without notice

7 OPERATION


7                Operation
7.1              Configuring the FlexChain system
                                          The complete configuration is possible via the USB port and SOPAS ET, via IO-Link and
                                          via CANopen.
                                          The booster has no SOPAS device description functionality.
                                          In addition, the main settings required for commissioning can be made via the display
                                          (see "Commissioning", page 17). Interface-specific settings can be found at the end of
                                          this chapter.
                                          To configure the system via SOPAS ET you will need the SOPAS software, the SOPAS
                                          Device Description (SDD), and a USB connection.

                                          NOTE
                                          The USB interface is intended only for configuring the device and must be unplugged
                                          during operation.


7.1.1            Functions structure
                                          The graphic below basically describes the functional structure and makes it easier to
                                          understand the FlexChain system.




Figure 7: Function overview




20       O P E R A T I N G I N S T R U C T I O N S | FlexChain                                              8023047.1Q01/2025-01-29 | SICK
                                                                                                               Subject to change without notice

OPERATION 7


                                   –    Guest Position:
                                        Each guest or pair of guests (for sender/receiver sensors) requires a defined posi‐
                                        tion in the FlexChain system. The process data sequence is ordered depending
                                        on the position. With suitable positioning it is also possible to define meaningfully
                                        connected zones.
                                        If a FlexChain system has been set up or the guests are connected to the host, the
                                        guests can be automatically positioned using the “Automatic Position Assignment”
                                        or “Auto Assignment” methods. Manual positioning of each individual guest is also
                                        possible.
                                   –    Guest Thresholds:
                                        The switching thresholds of the connected sensors can be set in “Guest Thresh‐
                                        olds”. This is done either via a central teach-in for all sensors or via a teach-in of a
                                        selected sensor.
                                        This function is not available for sensors installed using the FlexChain Adapter
                                        guest. In this case, the teach-in must be performed directly on the sensor con‐
                                        nected on the FlexChain Adapter.
                                   –    Channel:
                                        Once a positioning and a switching threshold setting have been carried out, the
                                        system is ready for operation. Now the states of each individual channel can be
                                        output via the process data (see also “Process Data”), and/or the sensor data can
                                        be used for further processing.
                                   –    Zones:
                                        In “Zones”, areas can be defined between two channels within which an evalua‐
                                        tion is made by selectable functions within the zone. The resulting states (Qint)
                                        can either be used for further processing or output directly via the I/Os (see “I/
                                        Os”) and/or via the process data (see “Process Data”).
                                   –    Logics:
                                        The states of the different zones can be further processed by simple logic gates.
                                        In addition, external input signals can also be integrated into the logic gates. The
                                        states of the logic gates can be output via the I/Os (see “I/Os”) and/or via the
                                        process data (see “Process Data”).
                                   –    Process Data:
                                        The information is transmitted to the control via a serial interface using the proc‐
                                        ess data. An individual configuration of the process data is possible.
                                   –    I/O:
                                        Binary data can be transferred via I/O. The I/Os are freely configurable. A configu‐
                                        ration as input for further processing (e.g. as logic input signal) is given.

7.1.2              Structure of SOPAS
                                   The SOPAS screen for FlexChain is divided into a number of tabs (orange). Every tab
                                   provides a specific set of parameterization functions. You can easily jump back and
                                   forward between the tabs.
                                   The structure of the visualization is similar in each tab:
                                   –    Important basic information is displayed on the left side of the Sopas window (1,
                                        red). This includes diagnostic information (see chapter 8) or the status of the pins.
                                   –    The channel status can be seen in the middle of the screen (2, green). If a channel
                                        is free, it is displayed in green with a continuous line. If the channel is blocked
                                        by an object, the channel is displayed with a red dashed line. In case of an error
                                        (e.g. Quality of Run Alarm), the error is directly visible in the channel status at the
                                        respective guest.
                                   –    On the right side of the Sopas window (3, blue), you can either make settings or
                                        call up individual information.




8023047.1Q01/2025-01-29 | SICK                                                         O P E R A T I N G I N S T R U C T I O N S | FlexChain   21
Subject to change without notice

7 OPERATION




                                                        1                        2                               3
                                           Figure 8: Structure of SOPAS – home


7.1.3             Basic information on the FlexChain system

7.1.3.1           SOPAS
                                           The Home tab does not contain any settings. The purpose of this tab is to provide you
                                           with information and status details for the connected FlexChain system. This includes
                                           information such as performance values of the system, higher-level diagnostic informa‐
                                           tion and states of the individual switching outputs.
                                           In addition, detailed information on the selected guest can be called up by selecting a
                                           specific guest.




                                           Figure 9: Guest Information


                                           NOTE
                                           Detailed information can be found in the IO-Link supplement (8023651) and/or the
                                           EDS description (8024673).


22        O P E R A T I N G I N S T R U C T I O N S | FlexChain                                              8023047.1Q01/2025-01-29 | SICK
                                                                                                                Subject to change without notice

OPERATION 7


                                   Table 5: Basic information IO-Link & CANopen index
                                   Object name                  Description                                                     IO-Link           CAN-
                                                                                                                                Index             Open
                                                                                                                                                  Index
                                   System Properties            Retrieval of various system information such                    301               0x212D
                                                                as response time, number of connected
                                                                guests, etc.
                                   Guest Address Selector       Selection of a specific guest                                   302               0x212E
                                   Guest Info                   Retrieval of detailed guest information of the                  303               0x212F
                                                                selected guest
                                   Channel Status               Information about the status of each individual 480                               0x21E0
                                                                channel (object there or not). This information
                                                                is the raw data from the FlexChain system and
                                                                can be used for further processing.
                                   PIN status                   Specifies the pin status (high/low status at the 483                              0x21E3
                                                                individual pin) via a byte. The bits used depend
                                                                on the hardware variant of the FlexChain Host.
                                   System status                Contains general diagnostic information such                    100               0x2064
                                                                as error and/or warning message such as
                                                                quality of run alarm, hardware error, etc.
                                   Guest Teach-In Status        Indicates whether a teach-in is recommended                     307               0x2133
                                                                by the system or whether there is an error.


7.1.4              Teach & Positioning
                                   The Teach & Positioning tab can be used to teach in the switching threshold of individ‐
                                   ual guests or all guests at once. The guest position can also be set automatically
                                   (automated position assignment) or changed manually.




                                   Figure 10: Teach & Positioning

                                   Automated positioning
                                   The “Automated position assignment” method is used to automatically assigned a
                                   position to every guest in the FlexChain system. Positions are assigned based on the
                                   following rules:




8023047.1Q01/2025-01-29 | SICK                                                            O P E R A T I N G I N S T R U C T I O N S | FlexChain           23
Subject to change without notice

7 OPERATION

                                      1        The first position is the first guest connected to port A. Further positions are then
                                               assigned in increasing numerical order for the guests hanging off port A.
                                      2        All guests on port B are then numbered according to the same principle as in step
                                               1.
                                      3        Sender/receiver sensors are always jointly assigned a position. The receiver
                                               serves as the reference during positioning.
                                      The transmitted process data word also varies according to the position of the guest.
                                      For example, the first channel of the guest at position 1 is represented by the first bit
                                      in the process data word. This means that the sequence within the process data word
                                      depends directly on the guest positions.
                                      Note when changing the number of guests: if a guest is removed or a new guest con‐
                                      nected, this guest is not taken into consideration when using the “Automated position
                                      assignment” positioning method. If there is a changed arrangement, the system reports
                                      a “Chain Issue Error” “Confirm Chain Changed” after a reboot and refuses operation.
                                      You need to either use the “Confirm chain change” method beforehand, or perform the
                                      “Auto assignment” method (see below).

                                      NOTE
                                      “Automatic Assignment” also changes the position and zone settings if necessary. (see
                                      "Automated assignment", page 26)

                                      Manual positioning
                                      The position of the guest can be individually adapted via the IO-Link, CANopen and/or
                                      via SOPAS. This option was implemented because the automated positioning may not
                                      always represent the actual physical position in the application. The manual positioning
                                      option was therefore created for simpler organization or easier interpretation of the
                                      process data.
                                      A comparison of the addressing, the automated positioning, and the desired positioning
                                      is shown in figure 11.




                                      Figure 11: Manual positioning of guests

                                      Using SOPAS, the position of a guest can be easily changed via drag & drop (figure 11).
                                      Note that the sequence number in the process data word also changes depending on
                                      the positioning.




24   O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                    8023047.1Q01/2025-01-29 | SICK
                                                                                                                 Subject to change without notice

OPERATION 7




                                   Figure 12: Manual positioning of guests

                                   To ensure the correct guest has been selected, detailed information about the selected
                                   guest is shown on the right hand side. There is also a “Find Me” function for easily
                                   locating a guest. After selecting a specific guest and pressing the Find Me button, both
                                   LEDs on the selected guest flash with 1 Hz.

                                   NOTE
                                   1    Find Me can also be activated during process data operation (PD = valid). Note,
                                        however, that this will have a periodic effect (500 ms) on the cycle time.
                                   2    The Find Me function is automatically deactivated by the device for certain com‐
                                        mands/configurations (Factory reset, Teach-in, Confirm chain change, Automated
                                        assignment, Automated position assignment, Change position, or Teach-in posi‐
                                        tion).




                                   Figure 13: Manual positioning settings


7.1.4.1            Confirm chain change
                                   The total number of connected guests and their respective threshold values are stored
                                   in the host. If the number of guests changes at a later time, a warning message is
                                   displayed. Confirm chain change is used to confirm the new total guest count and store
                                   it in the host. The warning message is no longer displayed.




8023047.1Q01/2025-01-29 | SICK                                                       O P E R A T I N G I N S T R U C T I O N S | FlexChain   25
Subject to change without notice

7 OPERATION

7.1.4.2           Automated assignment
                                           Automated assignment performs the three methods “Confirm Chain Change”, “Auto‐
                                           mated Position Assignment”, and “Automatic Zone Assignment” (see also the Zone
                                           tabs).

7.1.4.3           Teach
                                           There are a number of different teach modes available.
                                           –        Teach all guests
                                                    Sets the switching threshold value for all centralized and teachable guests
                                           –        Teach guest
                                                    Sets the switching threshold value for the selected guest.
                                           –        Auto TeachIn
                                                    If AutoTeach is activated, a teach-in is carried out automatically after:
                                                     ° Restart
                                                     ° “Automatic Assignment”
                                                     ° “Confirm Chain Change”
                                                     ° IO-Link Datastorage Download
                                           There are sensors (e.g. the photoelectric proximity sensor GTB6) where the switching
                                           threshold value can only be set manually directly on the sensor. A teach in via the host
                                           is not possible in this case.
                                           The teach-in status should be queried after a teach-in. This returns a response for each
                                           individual guest position.


7.1.4.4           Performance Options
                                           Performance options are available for a few guests. These are guest-specific setting
                                           options. The respective performance option can be found directly in the Teach menu
                                           (see figure 13).
                                           Cross beam:
                                           With the SLG-2 light grids, the “Cross beam” performance option can be selected
                                           to improve the resolution. The function is suitable for the detection of very flat and
                                           wide objects such as metal plates. This function enables the following resolution to be
                                           achieved between sender and receiver in the middle detection zone (average 50% of
                                           the total distance between sender and receiver):
                                           Resolution = beam separation / 2 +4 mm




26        O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                  8023047.1Q01/2025-01-29 | SICK
                                                                                                                    Subject to change without notice

OPERATION 7


                                        3     4                                                                                                           1
                                              5
                                              6
                                              7
                                              8
                                              9
                                              10
                                              11
                                              12
                                              13
                                              14
                                              15
                                              16
                                              17
                                              18
                                              19
                                              20
                                              21
                                              22
                                              23


                                               25%                             50%                                            25%
                                   Figure 14: Cross beam, to improve the resolution in the middle 50%


7.1.4.5            Teach & Positioning IO-Link & CANopen Index

                                   NOTE
                                   Detailed information can be found in the IO-Link supplement (8023651) and/or the
                                   EDS description (8024673).

                                   Table 6: Teach & Positioning IO-Link & CANopen Index
                                   Object name                  Description                                                     IO-Link           CAN-
                                                                                                                                Index             Open
                                                                                                                                                  Index
                                   Standard Command/Auto‐       Performs automatic positioning of the guest                     2                 0x2,00
                                   matic Guest Position         positions                                                                         2
                                   Assignment
                                   Standard Command/Auto‐       Performs the Automatic Guest Position Assign‐ 2                                   0x2,00
                                   matic Assignment             ment, Confirm Chain Change and Automatic                                          2
                                                                Zone Assignment methods
                                   Standard Command/Con‐        Confirms/accepts and saves the new/existing                     2                 0x2,00
                                   firm Chain Change            number of guests in the host                                                      2
                                   Standard Command/            Performs a teach-in across all sensors                          2                 0x2,00
                                   Teach-In                                                                                                       2
                                   Guest Teach-In Status        Indicates whether a teach-in is recommended                     307               0x2,13
                                                                by the system.                                                                    3



8023047.1Q01/2025-01-29 | SICK                                                            O P E R A T I N G I N S T R U C T I O N S | FlexChain           27
Subject to change without notice

7 OPERATION

                                          Object name                   Description                                             IO-Link       CAN-
                                                                                                                                Index         Open
                                                                                                                                              Index
                                          Guest positions               For manual positioning of the guests. Value    304                    0x2,13
                                                                        range 1 – 32 for the guests with the addresses                        0
                                                                        A1 – A32 (port A) and 101 – 132 for the
                                                                        guests with the addresses B1 – B32 (port B).
                                                                        Warning: senders should not be assigned a
                                                                        position, as senders do not have a channel.
                                          Guest Performance             Adjustability of guest-specific options (e.g.           305           0x2,13
                                          Options                       cross beam)                                                           1
                                          Guest Teach-In Position       Teach-in of all guests or a selected specific           306           0x2,13
                                                                        guest                                                                 2
                                          FindMe                        During running, the guest(s) at the selected            204           0x20CC
                                                                        position flash at 1 Hz

                                         IOLink TeachInStatus has the following values:
                                         –        Teach-in necessary (0)
                                                  This is set if the guest at the relevant position has been replaced (serial number
                                                  has changed), provided the guest is actually teachable, a teach-in has not already
                                                  been carried out at that position, an Automatic assignment, Confirm chain change,
                                                  Factory reset or DataStorage download has been performed.
                                         –        OK (1) (the last teach-in was successful)
                                         –        Fail (2) (the last teach-in failed, e.g. bad alignment)
                                                  This is an immediate teach-in response. It is also retained after a restart, and does
                                                  not become a “Teach-in Necessary”.
                                         –        Local Adjustment at Device (optional) (3) (e.g., GTB with built-in potentiometer)
                                         –        Not Available (4) (guest does not have a teach-in function, for example a sender, or
                                                  is completely masked (user mask))

7.1.5           Zones




                                         Figure 15: Zones

                                         The Zones tab can be used to define multiple areas or zones. Up to 16 zones can be
                                         defined.




28      O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                           8023047.1Q01/2025-01-29 | SICK
                                                                                                                           Subject to change without notice

OPERATION 7


                                   The zones are displayed, on the one hand, in a table on the right hand side. You can
                                   configure the zones there. The zones are also shown in the system schematic (on the
                                   left).
                                   Specific measurement functions can be defined within each zone. The result is passed
                                   on as an internal output state, which in turn can be used as input for further functions,
                                   or directly outputted via an output. The measurement results of a zone can also be
                                   output via the serial interface (see "Process data", page 36).

7.1.5.1            Zone definition
                                   Automated zone assignment
                                   This function is performed by “Automatic Zone Assignment” or by “Auto Assignment”.
                                   Starting with zone 2, running causes every guest in a zone to be assigned the NCB>=1
                                   function (number of channels blocked greater than or equal to 1).
                                   NCB>=1 means that if at least one channel in the zone is blocked, the internal output
                                   state is set to “High”.
                                   The exception to this is zone 1. It is initially defined as the first channel to the last
                                   channel.

                                   Manual zone assignment
                                   You can individually select each zone in the right hand area of the screen, and config‐
                                   ure the zone in the bottom area. The “Status” column shows whether the internal
                                   output state Qint is active or not.




                                   Figure 16: Overview of the settings for each zone




                                   Figure 17: Zone configuration options




8023047.1Q01/2025-01-29 | SICK                                                           O P E R A T I N G I N S T R U C T I O N S | FlexChain   29
Subject to change without notice

7 OPERATION

                                      The zone range can be set in the parameterization area (e.g., from Channel 3 – Channel
                                      6). It is also possible to define different measurement functions within each zone.
                                      These include:
                                      1        NCB: Number of channels blocked; object detection or width classification
                                               Example 1: NCB>=1 for object detection (Qint active if at least 1 channel blocked)
                                               Example 2: NCB=2 for width classification (Qint active if exactly 2 channels in a
                                               zone are blocked)




                                               Figure 18: Width measurement with NCB




30   O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                 8023047.1Q01/2025-01-29 | SICK
                                                                                                              Subject to change without notice

OPERATION 7


                                   2    FCB/LCB: First channel blocked/last channel blocked:
                                        Mainly used for height measurement, height classification or position determina‐
                                        tion.
                                        - FCB: Channel number of the first blocked channel of a zone.
                                        - LCB: Channel number of the last blocked channel of a zone.

                                        Example of height classification with FCB/LCB: Crates of the same size or larger
                                        than shown in the figure should be detected:
                                        - FCB <= 5: if the first channel blocked in zone 1 is channel 5 or lower, the internal
                                        output state Qint1 is activated (figure on left).
                                        - LCB >=2: if the last channel blocked in zone 1 is channel 2 or higher, the internal
                                        output state Qint1 is activated (figure on right).




                                        Figure 19: Height measurement FCB/LCB


7.1.5.2            Zones QInts IO-Link & CANopen Index

                                   NOTE
                                   Detailed information can be found in the IO-Link supplement (8023651) and/or the
                                   EDS description (8024673).

                                   Table 7: Zones QInts IO-Link & CANopen Index
                                   Object name                 Description                                                   IO-Link           CAN-
                                                                                                                             Index             Open
                                                                                                                                               Index
                                   Standard Command/Auto‐      Performs an automatic zone definition and                     2                 0x2002
                                   matic Zone Assignment       assigns the function NCB ≥ 1 to each zone
                                   Standard Command/Auto‐      Performs the Automatic Guest Position Assign‐ 2                                 0x2002
                                   matic Assignment            ment, Confirm Chain Change and Automatic
                                                               Zone Assignment methods




8023047.1Q01/2025-01-29 | SICK                                                         O P E R A T I N G I N S T R U C T I O N S | FlexChain           31
Subject to change without notice

7 OPERATION

                                            Object name                  Description                                         IO-Link       CAN-
                                                                                                                             Index         Open
                                                                                                                                           Index
                                            Qint Zone Definition 1-16    Zone definition with a start channel and an         "Index = "Index =
                                                                         end channel                                         351 +     0x215F
                                                                                                                             x*2;      + x*2;
                                                                                                                             x=
                                                                                                                             0,1,2,... x=0,1,2
                                                                                                                             15"       ,...F"
                                            Qint Advanced Settings       A measurement function with operator and            " Index "Index =
                                            1-16                         constant can be defined. The result (Qint) is       = 352 + 0x2160
                                                                         a boolean value                                     x*2;      + x*2;
                                                                                                                             x=        x=
                                                                                                                             0,1,2,... 0,1,2,...
                                                                                                                             15"       F"


7.1.6             Logics

7.1.6.1           Logics tab
                                           The Logic tab can be used to further process the individual Qint internal output states
                                           or external signals using logic functions (AND, OR,…). A total of 8 logics are available,
                                           whereby Logix (n-x) (x>=1 and x<n) can also be used as an input signal for Logic n. The
                                           logic state can be outputted via the switching output or via the serial interface.




                                           Figure 20: Logics tab with two logics

                                           If all logic inputs of a gate are “Not Used”, the result will differ depending on the logic
                                           function selected. This fact can also be used to produce a constant 0 or 1.
                                           Table 8: Logic functions
                                            Logic function                                   Result
                                            AND                                              1
                                            OR                                               0
                                            XOR                                              0
                                            NAND                                             0
                                            NOR                                              1
                                            XNOR                                             1


32        O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                      8023047.1Q01/2025-01-29 | SICK
                                                                                                                        Subject to change without notice

OPERATION 7


                                   An input that is “Not Used” is not actually removed but instead replaced with a value
                                   that does not change the result, i.e. 1 for AND and NAND, otherwise 0.
                                   The XOR and XNOR function is not generally defined for more than two inputs.
                                   The following definitions were selected for the FlexChain implementation:
                                   Table 9: Inputs/outputs
                                                             Inputs                                                       Outputs
                                         a0             a1             a2              a3                      XOR                        XNOR
                                         0               0             0               0                         0                               1
                                         0               0             0               1                         1                               0
                                         0               0             1               0                         1                               0
                                         0               0             1               1                         0                               1
                                         0               1             0               0                         1                               0
                                         0               1             0               1                         0                               1
                                         0               1             1               0                         0                               1
                                         0               1             1               1                         1                               0
                                         1               0             0               0                         1                               0
                                         1               0             0               1                         0                               1
                                         1               0             1               0                         0                               1
                                         1               0             1               1                         1                               0
                                         1               1             0               0                         0                               1
                                         1               1             0               1                         1                               0
                                         1               1             1               0                         1                               0
                                         1               1             1               1                         0                               1


7.1.6.2            Logics IO-Link & CANopen Index

                                   NOTE
                                   Detailed information can be found in the IO-Link supplement (8023651) and/or the
                                   EDS description (8024673).

                                   Table 10: Logics IO-Link & CANopen Index
                                   Object name                 Description                                                     IO-Link           CAN-
                                                                                                                               Index             Open
                                                                                                                                                 Index
                                   Logic 1-8                   Configuration of logic gates 1 – 8. Selection of                421,42 0x21A5
                                                               the operator and the logic inputs                               2,423  ,
                                                                                                                               … 428 0x21A6
                                                                                                                                      ,
                                                                                                                                      0x21A7
                                                                                                                                      , …,
                                                                                                                                      0x21AC




8023047.1Q01/2025-01-29 | SICK                                                           O P E R A T I N G I N S T R U C T I O N S | FlexChain           33
Subject to change without notice

7 OPERATION

7.1.7             PINS

7.1.7.1           PINS tab




                                           Figure 21: Pins

                                           The PINS tab can be used to configure which information is assigned to, or should be
                                           output for a pin.
                                           Possible output signals
                                           1   Qint
                                               Issues the Qint status of the zones
                                           2   Logic
                                               Issues the configured logics
                                           3   Masked System Status
                                               One system status byte. You can configure when, and for which warnings and error
                                               messages this signal should be high.
                                           input
                                           1    Teach-In Trigger
                                                For performing an external teach-in.
                                           2    Logic-In
                                                The input signal can be used for the logics.
                                           3    Blocked Channel Hold
                                                If the input signal is 0 (“LOW”), the “Blocked Channel Hold” function is set. Chan‐
                                                nels that have been blocked once remain set or are held. Thus only a channel
                                                status from 0 to 1 is possible. If the input signal is 1 (“HIGH”), the “Block Channel
                                                Hold” function is inactive and the channel status indicates the currently measured
                                                values.
                                           4    RS-485 Trigger
                                                Sends data as soon as a signal is HIGH.
                                           5    Sender Off
                                                Test function for simulating object detection: The sender LEDs can be deactivated
                                                via the input. This can be used to test whether the associated receiver LED
                                                responds.
                                           Furthermore, the temporal behavior of the PIN can be controlled via the “Output Delay
                                           Mode” and a possibility of signal inversion is available. A value range between 1 ms
                                           and 30,000 ms is available for the “Output Delay Mode” function.



34        O P E R A T I N G I N S T R U C T I O N S | FlexChain                                               8023047.1Q01/2025-01-29 | SICK
                                                                                                                 Subject to change without notice

OPERATION 7


                                   Input signal


                                   DEACTIVATED
                                   Output signal
                                   T-ON DELAY                  t                      t                      t       t
                                   Output signal
                                   T-OFF DELAY                            t               t                      t                       t
                                   Output signal
                                   T-ON / T-OFF DELAY          t          t          t                       t       t                   t
                                   Output signal
                                   IMPULSE (one shot)          t                     t                       t
                                   Output signal

                                   Figure 22: Output delay modes


7.1.7.2            PINS IO-Link & CANopen Index

                                   NOTE
                                   Detailed information can be found in the IO-Link supplement (8023651) and/or the
                                   EDS description (8024673).

                                   Table 11: PINS IO-Link & CANopen Index
                                   Object name                     Description                                                      IO-Link           CAN-
                                                                                                                                    Index             Open
                                                                                                                                                      Index
                                   PIN 2 Configuration             Assign a boolean value like Qint 1 – 16, Logic                   121               0x2,07
                                                                   1 – 8, Teach-In Trigger…                                                           9
                                   PIN 4 configuration             Assign a boolean value like Qint 1 – 16, Logic                   441               0x21B9
                                                                   1 – 8, Teach-In Trigger…
                                   PIN 5 configuration             Assign a boolean value like Qint 1 – 16, Logic                   122               -
                                                                   1 – 8, Teach-In Trigger…
                                   PIN 6 configuration             Assign a boolean value like Qint 1 – 16, Logic                   442               -
                                                                   1 – 8, Teach-In Trigger…
                                   PIN 7 configuration             Assign a boolean value like Qint 1 – 16, Logic                   443               -
                                                                   1 – 8, Teach-In Trigger…
                                   PIN 8 configuration             Assign a boolean value like Qint 1 – 16, Logic                   444               -
                                                                   1 – 8, Teach-In Trigger…
                                   Output Delay Mode Pin2/         T-On Delay, T-Off Delay, …                                       213/21 0x20D5
                                   Pin4                                                                                             2      /
                                                                                                                                           0x20D4
                                   Output Delay Mode               T-On Delay, T-Off Delay, …                                       463/46 -
                                   Pin5 / Pin6 / Pin7 / Pin8                                                                        5/467/
                                                                                                                                    469
                                   Output Delay Time               Time value for the delay modes                                   215/21 0x20D7
                                   Pin2 / Pin4                                                                                      4      /
                                                                                                                                           0x20D6
                                   Output Delay Time               Time value for the delay modes                                   464/46 -
                                   Pin5 / Pin6 / Pin7 / Pin8                                                                        6/468/
                                                                                                                                    470
                                   Pin2 / Pin4 Inversion           Inverting the signal                                             455/45 0x21C7
                                                                                                                                    6      /
                                                                                                                                           0x21C8




8023047.1Q01/2025-01-29 | SICK                                                                O P E R A T I N G I N S T R U C T I O N S | FlexChain           35
Subject to change without notice

7 OPERATION

                                            Object name                 Description                                        IO-Link       CAN-
                                                                                                                           Index         Open
                                                                                                                                         Index
                                            Pin5 / Pin6 / Pin7 / Pin8   Inverting the signal                               457/45 -
                                            Inversion                                                                      8/459/
                                                                                                                           460
                                            Pin2 / Pin4 System Status   Boolean value: ORring of different diagnostic      447/44 0x21BF
                                            Mask                        information                                        8      / 0x21
                                                                                                                                  C0
                                            Pin5 / Pin6 / Pin7 / Pin8   Boolean value: ORring of different diagnostic      449/45 -
                                            System Status Mask          information                                        0/451/
                                                                                                                           452


7.1.8             Process data

7.1.8.1           Process Data Tab
                                           For the IO-Link and CANopen interfaces, the FlexChain process data word has a length
                                           of 32 bytes. Each of these bytes can be individually populated with the desired data.




                                           Figure 23: Overview of process data

                                           Loading process data via profiles
                                           A number of pre-defined process data profiles are available that can be selected to
                                           populate the process data word.




36        O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                    8023047.1Q01/2025-01-29 | SICK
                                                                                                                      Subject to change without notice

OPERATION 7




                                   Figure 24: Loading process data via a profile

                                   Manually customizing the process data
                                   Each individual byte of the process data can be customized. After clicking on a byte, a
                                   drop-down list of information that can be assigned to the byte is displayed. The length
                                   of each “information block” is limited to one byte (8 bits). A single byte can therefore be
                                   used, for example, to transmit 8 channel states.
                                   The available information is shown in figure 14. NCB, FCB and LCB are the actual
                                   measured values. For example, NCB transmits how many channels in the zone are
                                   blocked. The following assignment is defined for the issue of the outputs (PIN status):
                                   Table 12: Assignment of the PIN status in the process data
                                   PIN       4-2-5-6-7-8
                                   BIT       0-1-2-3-4-5

                                   Table 13: Description of availbale process data values
                                   Value     Description
                                   System    Diagnosis Byte. Every bit contains a specific diagnostic information. (See chapter 8.2)
                                   Status
                                   PIN Sta‐ HIGH/LOW Status of each Input or Output PIN. (See assignment table 10)
                                   tus
                                   Qint      Internal bninary status of selected zones. (See chapter 7.1.5)
                                   Logic     Result of each Logic (1-8). (See chapter 7.1.6)
                                   Chan‐     High low status of the selected channel or beam (channel blocked or made)
                                   nel
                                   NCB of    Number of channel blocked (how many channels) of selected zone (see chapter 7.1.5)
                                   zone
                                   LCB of    Last channel blocked of selected Zone (see chapter 7.1.5)
                                   zone
                                   FCB of    First channel blocked of selected zone (see chapter 7.1.5)
                                   zone




8023047.1Q01/2025-01-29 | SICK                                                              O P E R A T I N G I N S T R U C T I O N S | FlexChain   37
Subject to change without notice

7 OPERATION




                                           Figure 25: Process data word selection


7.1.8.2           Process Data IO-Link & CANopen Index

                                           NOTE
                                           Detailed information can be found in the IO-Link supplement (8023651) and/or the
                                           EDS description (8024673).

                                           Table 14: Process Data IO-Link & CANopen Index
                                            Object name                 Description                                       IO-Link       CAN-
                                                                                                                          Index         Open
                                                                                                                                        Index
                                            Process Data Definition     Configuration of the process data. Each proc‐     67            "Cyclic
                                                                        ess data slot with a size of 8 bits can be                      data
                                                                        assigned a process data function                                (proc‐
                                                                                                                                        ess
                                                                                                                                        data)",
                                                                                                                                        page 45




38        O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                   8023047.1Q01/2025-01-29 | SICK
                                                                                                                     Subject to change without notice

OPERATION 7


7.1.9              Settings

7.1.9.1            Settings tab




                                   Figure 26: Settings tab

                                   The following settings can be configured in the Settings tab:
                                   1    Local interface lock: Locks the buttons on the display
                                   2    Crosstalk Offset Time: If two identical FlexChain systems are operated in close
                                        proximity to one another, there is a possibility of mutual interference. The Cross‐
                                        talk Offset Time changes the cycle time of the FlexChain system. The two systems
                                        can then no longer interfere with one another due to the different cycle time and
                                        the standard 2-bit processing.
                                        Suitable crosstalk offset time values are 300 µs and 500 µs.
                                        If these values do not work, a suitable value must be determined together with
                                        your technical contact.
                                   3    “Notification handling” can be used to activate or deactivate events. Various
                                        events such as overtemperature, overvoltage, etc. can be selected. PDinvalid
                                        means invalid process data.
                                   4    Test functions: Deactivates the sender LED. This is used to check whether the
                                        receiver is responding.
                                   5    Factory reset: Restores all settings to the factory defaults. If there are guests con‐
                                        nected to the system, these need to be reassigned using “Automated assignment”,
                                        and then taught in again using “Teach all devices”.
                                   6    Blanked channels: The “blank all currently made/blocked channels” functions can
                                        be used to hide all free or currently blocked beams. This function is useful if
                                        there is a static object in the light path (e.g., light grid). The channels can also be
                                        individually hidden using Ctrl & left mouse button. Channels that are hidden are
                                        no longer included in the process data.
                                   7    Quality of Run Alarm Time Filter: The filter can be used to select the time from
                                        which the “Quality of run alarm” signal becomes active. If the time is set very
                                        short, activation is possible if an object is in the light path. Since the signal is
                                        mainly used to detect contamination, a time filter of several minutes is usually
                                        sufficient.




8023047.1Q01/2025-01-29 | SICK                                                         O P E R A T I N G I N S T R U C T I O N S | FlexChain   39
Subject to change without notice

7 OPERATION

7.1.9.2           Settings IO-Link & CANopen Index

                                           NOTE
                                           Detailed information can be found in the IO-Link supplement (8023651) and/or the
                                           EDS description (8024673).

                                           Table 15: Settings IO-Link & CANopen Index
                                            Object name                  Description                                          IO-Link       CAN-
                                                                                                                              Index         Open
                                                                                                                                            Index
                                            Local Interface Lock         Locks the operating pushbuttons of the Flex‐         4             0x200C
                                                                         Chain Host
                                            CrossTalkOffsetTime          If two identical FlexChain systems are oper‐    499                0x21F3
                                                                         ated directly next to each other, crosstalk may
                                                                         occur under certain circumstances. Two scans
                                                                         are always made for greater robustness. Cross‐
                                                                         talk can be avoided if one system has a dif‐
                                                                         ferent ScanTime than another system. This is
                                                                         ensured by the offset time.
                                            Notification Handling        Activate/deactivate IO-Link events and the           227           -
                                                                         ProcessStatus bits (event codes on the last
                                                                         page of the IO-Link supplement)
                                            SenderOff                    Test function: Deactivates the senders to simu‐ 97                 0x2,06
                                                                         late an blocking of the channels                                   1
                                            Factory Reset                Resets the host to factory settings                  2             0x2,00
                                                                                                                                            2
                                            Blank All Currently Made     Blanks out all non-blocked channels. The             2             0x2,00
                                            Channels                     blanked channels will not be taken into                            2
                                                                         account in the evaluation.
                                            Blank All Currently Blocked Blanks out all blocked channels. The blanked          2             0x2,00
                                            Channels                    channels will not be taken into account in the                      2
                                                                        evaluation.
                                            Channel Mask                 Individual blanking of individual channels.          72            0x2,04
                                                                         The blanked channels will not be taken into                        8
                                                                         account in the evaluation.
                                            Quality Of Run Alarm On      Setting a warning after a critical signal            311           0x2,13
                                            Time Filter                  strength is detected at the sensor for the                         7
                                                                         defined duration
                                            Quality Of Run Alarm Off     Resetting a warning after an uncritical signal       312           0x2,13
                                            Time Filter                  strength is detected at the sensor for the                         8
                                                                         defined duration
                                            Hardware Variant             Reading the connected hardware variant of the 440                  -
                                                                         FlexChain Host
                                            CANopen Node ID              Setting the Node ID                                  475           "Node
                                                                                                                                            ID and
                                                                                                                                            baud
                                                                                                                                            rate",
                                                                                                                                            page 43
                                            CANopen Bit Rate             Setting the transmission rate                        440           "Node
                                                                                                                                            ID and
                                                                                                                                            baud
                                                                                                                                            rate",
                                                                                                                                            page 43
                                            RS-485 configuration         Parameterization of the RS-485 interface             473           -
                                                                         (baud rate, transmission format, …



40        O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                       8023047.1Q01/2025-01-29 | SICK
                                                                                                                         Subject to change without notice

OPERATION 7


7.2                IO-Link specific settings
                                   The FlexChain Host variants have an IO-Link interface. The process data can be
                                   retrieved via the interface and the system can be configured with the same range
                                   of functions as in Sopas using the service data.

                                   Configuration via acyclic service data
                                   Functions such as zone definition, teach-in or positioning can be carried out using the
                                   service data. The indices of the service data can be found in the IO-Link supplement.
                                   The IO-Link supplement for the respective product number can be found online. Various
                                   diagnostic information can be transferred via the process date.

                                   NOTE
                                   Detailed information can be found in the IO-Link supplement (8023651) and/or the
                                   EDS description (8024673).

                                   Data Storage
                                   All relevant parameters of the FlexChain Host can be saved in an IO-Link master using
                                   the data storage IO-Link function. If the device is replaced, these parameters can be
                                   written to the new device, or they can be distributed to multiple FlexChain Hosts with
                                   the same application.

                                   NOTE
                                   The device replacement via the IO-Link function data storage is only possible with a
                                   FlexChain Host with the same part number.


                                   NOTE
                                   After a DataStorage download, a changed number of guests and guest arrangement is
                                   automatically accepted. In addition, the teach-in status is reset at all guest positions.
                                   This means that a teach-in is necessary (if a teach-in is supported by the host at the
                                   corresponding guest). If an auto teach-in is set, the teach-in is carried out automatically
                                   on restart.

                                   Issue of process data of the FlexChain Host
                                   Transmission data
                                   –    Minimum cycle time IO-Link: 2.3 ms
                                   –    Baud rate: COM3 (230.4 kbaud)
                                   –    Process data length: 32 bytes
                                   –    IO-Link version: 1.1.0

7.3                CANopen-specific settings

7.3.1              Overview
                                   Communication profile
                                   The CANopen communication profile (documented in CiA DS-301) regulates how the
                                   devices in a CANopen network exchange data.

                                   CANopen in the OSI model
                                   The CANopen protocol is a standardized Layer 7 protocol for the CAN bus. This layer is
                                   based on the CAN Application Layer (CAL).




8023047.1Q01/2025-01-29 | SICK                                                         O P E R A T I N G I N S T R U C T I O N S | FlexChain   41
Subject to change without notice

7 OPERATION


                                             7
                                             6
                                             5
                                             4
                                             3
                                             2
                                             1
                                      Figure 27: CANopen in the OSI model
                                      7           CAN application layer
                                      2           Data link layer
                                      1           Physical layer


                                      NOTE
                                      Layers 3 to 6 are not used in CANopen.

                                      Architecture
                                      CANopen is an asynchronous, serial fieldbus. As a rule, all subscribers are connected in
                                      a line (line topology). Signals lines and star-shaped placement are permissible but this
                                      is not always possible.
                                      The fieldbus needs to be terminated at the beginning and at the end of the business
                                      field. A passive 120 Ω bus terminating resistor is sufficient for this. The simplest type of
                                      bus termination are male cable connectors with terminators (SICK part no. 6021167).
                                      A T-connector (SICK part no.: 6030664) is required to integrate the FlexChain in a
                                      CANopen network (except as end device).
                                      The fieldbus can be expanded with bridges and repeaters.
                                      The optional voltage supply to pin 2 is not supported.

                                      Communication channels and status
                                      CANopen features various communication channels (SDO, PDO, Emergency Messages).
                                      These channels are formed with the help of the communication object identifier (COB
                                      ID). The COB IDs are based on the node IDs of the individual devices on the CANopen
                                      bus.
                                      As soon as the FlexChain Host possesses a node ID, it can be addressed via the
                                      network management services (NMT) and its CANopen state machine can be switched
                                      to the necessary status (Pre-Operational, Operational, or Stopped) by the master.

                                      Network management
                                      Network management (NMT) initializes the nodes in a CANopen network. It also adds
                                      the nodes to the network, as well as stopping and monitoring them.
                                      The following statuses can be identified:




42   O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                8023047.1Q01/2025-01-29 | SICK
                                                                                                             Subject to change without notice

OPERATION 7


                                   Table 16: Status of the CANopen state machine
                                   Status                Description
                                   Initializing          Initialization commences. Both the device application and device com‐
                                                         munication are initialized. After this, the node automatically switches to
                                                         Pre-Operational status.
                                   Pre-Operational       The FlexChain Host is ready for configuration; acyclic communication
                                                         can take place via SDO. However, the FlexChain is not yet able to
                                                         commence PDO communication and is not sending out any emergency
                                                         messages.
                                   Operational           In this state, the FlexChain is fully ready for operation and can transmit
                                                         messages autonomously (PDOs, emergency messages).
                                   Stopped               In this state, the FlexChain is not actively communicating (although
                                                         communication is still being actively monitored via node guarding).


7.3.1.1            Node ID and baud rate
                                   Node ID
                                   There can be a maximum of 128 devices on a CANopen network: one master and
                                   up to 127 slaves. Every device has a unique node ID (node address). The COB IDs
                                   (communication object identifiers) of the communication channels are derived from
                                   this ID.
                                   A correct node ID must be set for the FlexChain on the display or membrane keyboard
                                   for communication with the master. The following are correct:
                                   •    A node ID which is free in the CANopen network
                                   •    A node ID which the master expects
                                   Node ID 6 is set in the FlexChain at the factory.
                                   Node IDs 1 to 127 can be set (0 is typically allocated to the master).

                                   Baud rate
                                   The same baud rate must be set on the FlexChain as in the master.
                                   The higher the baud rate used in the CANopen network is, the lower the bus load. The
                                   longer the lengths of cable used are, the lower the possible baud rate.
                                   Baud rate 125 kbit/s is set at the factory.
                                   The following baud rates can be assigned to the FlexChain: 10 kbit/s, 20 kbit/s,
                                   50 kbit/s, 125 kbit/s, 250 kbit/s, 500 kbit/s, 800 kbit/s, 1,000 kbit/s.

                                   Maximum length of cable
                                   The max. length of the cable within a business field depends on the baud rate. The
                                   table below shows the sensing range per business field without the use of repeaters.
                                   Table 17: Maximum length of cable
                                   Baud rate                             125 kbit/s     250 kbit/s             500 kbit/s              1,000 kbit/s
                                   Length of cable                       500 m          250 m                  100 m                   30 m


7.3.1.2            Setting of node ID and baud rate
                                   Set the node ID and the baud rate as follows:
                                   •    Using the display or membrane keypad
                                   •    Via SOPAS ET
                                   •    Via layer setting services (LSS)




8023047.1Q01/2025-01-29 | SICK                                                           O P E R A T I N G I N S T R U C T I O N S | FlexChain   43
Subject to change without notice

7 OPERATION


                                           NOTE
                                           The voltage supply of the FlexChain must be switched off then back on to activate the
                                           baud rate.
                                           A device reset (command 81) is sufficient to activate a changed node ID.

                                           SOPAS ET
                                           The node ID and the baud rate of the FlexChain can also be set via SOPAS ET.
                                           In the address configuration area, you can enter the address in CAN and select the baud
                                           rate. You can enter address 1 to 127 for the FlexChain.




                                           Figure 28: Node ID and baud rate in SOPAS ET

                                           Access via layer setting services
                                           Layer setting services are supported in order to set the node ID and the baud rate of
                                           the FlexChain.
                                           The LSS slave is accessed via its LSS address (identity object), which is stored in object
                                           1018h. The LSS address comprises:
                                           •        Vendor- ID
                                           •        Product-Code
                                           •        Revision number
                                           •        Serial number
                                           The master uses the LSS services to request the individual services which are then
                                           executed by the FlexChain. The LSS telegrams facilitate communication between LSS
                                           master and LSS slave. An LSS telegram is always 8 bytes long. Byte 0 contains the
                                           command specifier (CS), followed by 7 bytes for the data. All bytes that are not in use
                                           must be set to zero.
                                           The following COB IDs are used:
                                           •        07E4h = LSS slave to LSS master
                                           •        07E5h = LSS master to LSS slave

7.3.1.3           Configuration using an EDS file
                                           An EDS file is available for easy connection of the FlexChain to a CANopen master.
                                           Among other things, this file contains the default parameters of the FlexChain and the
                                           default configuration for the process data.
                                           You can download the EDS file at www.sick.com:
                                           1.       Enter the seven-digit part number of your FlexChain directly into the Search field on
                                                    the homepage.
                                           2.       Click on the relevant search result.
                                           ✓        This will take you to all the information and files for your device.
                                           3.       Download the EDS file.
                                           4.       Integrate the EDS file into the engineering tool of your control.

                                           When the FlexChain is integrated into the CANopen development environment, the
                                           object values can be read out and set using the engineering tool.


44        O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                   8023047.1Q01/2025-01-29 | SICK
                                                                                                                     Subject to change without notice

OPERATION 7


7.3.2              Acyclic data (service data)
                                   The service data forms the communication channel through which device parameters
                                   (e.g. configuration of the beam numbering) are transmitted. It is used for status quer‐
                                   ies.
                                   Service data is always transmitted with confirmation, i.e. the receipt of every message
                                   is acknowledged by the receiver.
                                   The FlexChain has a Transmit service data channel and a Receive service data channel,
                                   to which two CAN identifiers are assigned.
                                   The service data communication corresponds to the client-server model. The FlexChain
                                   functions as an SDO server. In its request, the SDO client (e.g., the PLC) specifies the
                                   parameter, the access method (read/write), and the value, if applicable. The FlexChain
                                   executes read/write access and responds to the request.
                                   The maximum data length of a CAN telegram of 8 bytes is assigned as follows:
                                   Table 18: Service data format
                                   COB-ID          CCD        Index                    Subindex Specifications
                                        600 h +     Byte 0      Byte 1      Byte 2      Byte 3       Byte 4         Byte 5          Byte 6           Byte 7
                                        node ID

                                   The command code (CCD) identifies whether read or write access is required. In the
                                   event of an error, the data range will contain a 4-byte error code which provides
                                   information about the cause of the error.

                                   NOTE
                                   All parameters are automatically saved immediately after writing. Only the mapping of
                                   the PDOs is not saved and must be reinitialized after every device restart.


7.3.3              Cyclic data (process data)
                                   Process data is used for rapid and efficient exchange of real-time data (e.g., I/O data,
                                   setpoint values or actual values).
                                   8 databytes are available for the transmission of process data. Process data is trans‐
                                   mitted without confirmation.
                                   Table 19: Process data format
                                   COB-ID                Specifications
                                       0,180 h + node    Byte 0    Byte 1     Byte 2     Byte 3      Byte 4         Byte 5          Byte 6           Byte 7
                                             ID

                                   The FlexChain supports 6 Transmit PDOs and 1 Receive PDOs.
                                   Data from the FlexChain is sent to the master with the Transmit PDOs.
                                   The Transmit PDOs are defined by the following objects:
                                   •      Objects 1,800 h to 1,805 h contain the communication parameters.
                                   •      Objects 1A00 h to 1A05 h contain the object mapping.
                                   The format of the Transmit PDO between the master and the FlexChain must be agreed
                                   through PDO mapping.
                                   The process data can be arranged at will. The address (i.e. index and subindex) and the
                                   size (number of bits) from the entry in the object directory are entered in the mapping
                                   object for this purpose.




8023047.1Q01/2025-01-29 | SICK                                                               O P E R A T I N G I N S T R U C T I O N S | FlexChain        45
Subject to change without notice

7 OPERATION

                                         Bus load
                                         •        The more process data and the more frequently it is sent, the higher the bus load
                                                  in the CANopen network.
                                         •        The higher the baud rate used in the CANopen network is, the lower the bus load.
                                         •        The longer the lengths of cable used are, the lower the possible baud rate.
                                         A compromise must therefore be found between all three named factors for optimal
                                         communication.

                                         NOTE
                                         If a Transmit PDO is not used, it should be deactivated. To do so, set bit 31 to 1 in
                                         subindex 01h of the respective object 180xh.


7.3.4           Object library
                                         Table 20: Nomenclature for access and data types
                                          Abbreviation             Meaning
                                          R                        Read only access
                                          R/W                      Read/write access
                                          STRG                     String = a chain of characters of varying length
                                          BOOL                     Boolean = logical value 0 or 1
                                          ENUM                     Freely selectable values with a limited value range
                                                                   (e.g. BLACK, RED, BLUE, YELLOW)
                                          UINT                     Unsigned Integer = whole number value
                                                                   (e.g. UINT-32 = 0 … 4.294.967.295)
                                          ARRAY                    Data sequence of a data type
                                                                   (e.g. Array UINT-8 = character string of the data type UINT-8)
                                          RECORD                   Sequence of data containing different data types
                                                                   (e.g. UINT-8, UINT-32, UINT-32, UINT-16)
                                          STRUCT                   Sequence of data containing different data types
                                                                   (e.g. UINT-8, UINT-32, UINT-32, UINT-16)

                                         Table 21: Standard objects
                                          Object                   Access    Data type      Name
                                          1,000 h                  R         UINT-32        Device type
                                          1,001 h                  R         UINT-8         Error Register
                                          1,005 h                  R/W       UINT-32        COB-ID SYNC message
                                          1,008 h                  R         STRG           Device name
                                          1,009 h                  R         STRG           Hardware version number
                                          100 Ah                   R         STRG           Software version number
                                          100 Ch                   R/W       UINT-16        Node guarding – Guard time
                                          100 Dh                   R/W       UINT-8         Node guarding – Life time factor
                                          1,014 h                  R/W       UINT-32        COB-ID emergency message
                                          1,015 h                  R/W       UINT-16        Emcy inhibition time
                                          1,016 h                  R/W       UINT-32        Consumer heartbeat time
                                          1,017 h                  R/W       UINT-16        Producer heartbeat time
                                          1,018 h                  R         RECORD         Identity Object
                                          1,400 h … 1,401 h        R/W       RECORD         Receive PDO – Communication
                                          1,600 h … 1,601 h        R/W       RECORD         Receive PDO – Mapping
                                          1,800 h … 1,805 h        R/W       RECORD         Transmit PDOs – Communication


46      O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                         8023047.1Q01/2025-01-29 | SICK
                                                                                                                         Subject to change without notice

OPERATION 7


                                    Object                     Access     Data type      Name
                                    1A00 h … 1A05 h            R          RECORD         Transmit PDOs – Mapping


7.3.5              1xxxh – Standard objects
                                    CANopen standard objects are implemented in the FlexChain.

7.3.5.1            Device type
                                    1,000 h - Device type
                                    Table 22: 1000h – Device type
                                    Object                     Access     Data type      Description
                                    1000h                      R          UINT-32        The object contains the device type.
                                                                                         The value is always 0, as no device profile
                                                                                         is defined for the measuring automation light
                                                                                         grid.


7.3.5.2            Error register
                                    1001h – Error register
                                    Table 23: 1001h – Error register
                                    Object                     Access     Data type      Description
                                    1001h                      R          UINT-8         The object contains the error register.

                                    The error register is stored in 8 bit:
                                    Table 24: Error register – Stored in 8 bit
                                    Bit 7         Bit 6        Bit 5        Bit 4        Bit 3            Bit 2              Bit 1                Bit 0
                                    Manufac‐      Reserved     Device       Commu‐       Tempera‐ Voltage                    Current              Generic
                                    turer-spe‐                 profile-     nication     ture error error                    error                error
                                    cific error                related      error
                                                               error


7.3.5.3            SYNC message
                                    1,005 h – COB-ID SYNC message
                                    Table 25: 1,005 h – COB-ID SYNC message
                                    Object          Access Data type       Description
                                    1,005 h         R/W      UINT-32       Determines whether the device generates the SYNC mes‐
                                                                           sage and if it does, which bit width is used.

                                    Table 26: 1,005 h – Details
                                            Bit     Description                                                     Data values
                                            31      Reserved                                                        0
                                            30      Determines whether the device generates the                     0 Device does not generate a
                                                    SYNC message.                                                   SYNC message.
                                                                                                                    1 Not supported
                                            29      Determines which bit width is used.                             0 11 bit
                                                                                                                    1 Not supported
                                       28 … 0       29 bit wide CAN-ID                                              0
                                       11 … 0       11 bit wide CAN-ID                                              80 h




8023047.1Q01/2025-01-29 | SICK                                                                   O P E R A T I N G I N S T R U C T I O N S | FlexChain      47
Subject to change without notice

7 OPERATION

7.3.5.4           Type code
                                           1,008 h – Device name
                                           Table 27: 1,008 h – Device name
                                            Object                            Access    Data type     Description
                                            1,008 h                           R         STRG          The object contains the type code.


7.3.5.5           Hardware version
                                           1,009 h – Hardware version number
                                           Table 28: 1,009 h – Hardware version number
                                            Object                            Access    Data type     Description
                                            1,009 h                           R         STRG          This object contains the revision status of the
                                                                                                      hardware.


7.3.5.6           firmware version
                                           100 Ah – Software version number
                                           Table 29: 100 Ah – Software version number
                                            Object                            Access    Data type     Description
                                            100 Ah                            R         STRG          This object contains the version of the firm‐
                                                                                                      ware.

                                           The version of firmware in its delivery state can be found on the type label.

7.3.5.7           Node guarding
                                           The node guarding telegram is sent to poll the status of the FlexChain at regular
                                           intervals. The monitoring time multiplied by the life time factor results in the cycle in
                                           which the FlexChain is monitored.

                                           100 Ch – Guard time
                                           Table 30: 100 Ch - Node guarding – Guard time
                                            Object                      Access         Data type        Description
                                            100 Ch                      R/W            UINT-16          Configured monitoring time in ms

                                           100 Dh – Life time factor
                                           Table 31: 100 Dh - Node guarding – Life time factor
                                            Object                      Access         Data type        Description
                                            100 Dh                      R/W            UINT-8           Factor for multiplication of the monitoring
                                                                                                        time


7.3.5.8           COB-ID of the emergency message
                                           1,014 h – COB-ID emergency message
                                           Table 32: 1,014 h – COB-ID emergency message
                                            Object                Access Data type      Description
                                            1,014 h               R/W     UINT-32       Communication object identifier of the emergency message
                                                                                        The value is calculated from 00000080 h + node ID
                                                                                        1 … 127.
                                                                                        Example: the FlexChain with factory-set node ID = 6 trans‐
                                                                                        mitted with COB-ID 00000086 h.

                                           If the FlexChain detects an internal error, it sends an emergency message.


48        O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                               8023047.1Q01/2025-01-29 | SICK
                                                                                                                                 Subject to change without notice

OPERATION 7


                                   The FlexChain supports the following emergency messages:
                                   Table 33: Emergency messages
                                   Error code of Error regis‐      Manufacturer-specific    Description
                                   object        ter of object     code
                                   1,003 h       1,001 h
                                                                   1        2   3   4   5
                                   0,000 h         00 h            0        0   0   0   0   No error or reset error
                                   6,180 h         11 h            0        0   0   0   0   The PDO mapping specified in the FBMD
                                                                                            file is faulty or there are not enough PDO
                                                                                            services available. All PDOs of this direc‐
                                                                                            tion are locked.
                                   6,380 h         11 h            0        0   0   0   0   A CANopen object has been mapped in
                                                                                            several Receive PDOs. No process data
                                                                                            is sent to the application controller.
                                   8,110 h         11 h            1        0   0   0   0   CAN overrun
                                                                                            The receipt buffer in the CAN controller is
                                                                                            full. New messages cannot be saved and
                                                                                            are lost.
                                   8,110 h         11 h            2        0   0   0   0   CAN overrun
                                                                                            The sender buffer in the CAN controller
                                                                                            is full. New messages cannot be sent.
                                                                                            The FlexChain CANopen tries to send an
                                                                                            emergency message when the cause is
                                                                                            not a busoff or ERROR PASSIVE.
                                   8,120 h         11 h            0        0   0   0   0   The CAN controller switches to ERROR
                                                                                            PASSIVE status.
                                   8,130 h         11 h            ID1      0   0   0   0   The heartbeat or node guarding of a
                                                                                            CANopen device to be monitored has
                                                                                            failed.
                                   8,140 h         11 h            0        0   0   0   0   It was possible to restart the CANopen
                                                                                            communication after a busoff. Data can
                                                                                            be lost.
                                   8,210 h         11 h            No.2 0       0   0   0   PDO too short
                                                                                0           The Receive PDO contains too little data.
                                                                                            The data is ignored.
                                   8,220 h         11 h            No.      0   0   0   0   PDO too long
                                                                   2
                                                                                            The Receive PDO contains too much
                                                                                            data. The redundant data is ignored.
                                   1   Node ID of the failed device.
                                   2   Object number of the affected PDO.


7.3.5.9            Inhibition time for emergency message
                                   1,015 h – Emergency inhibition time
                                   Table 34: 1,015 h – Emergency inhibition time
                                   Object              Access          Data type        Description
                                   1,015 h             R/W             UINT-16          The configured inhibition time for the emer‐
                                                                                        gency message in ms.
                                                                                        The inhibition time becomes inactive with
                                                                                        value 0.


7.3.5.10           Heartbeat
                                   The FlexChain can be monitored with the heartbeat protocol or monitor other bus
                                   nodes.


8023047.1Q01/2025-01-29 | SICK                                                              O P E R A T I N G I N S T R U C T I O N S | FlexChain   49
Subject to change without notice

7 OPERATION

                                            1,016 h – Consumer heartbeat time
                                            Table 35: 1,016 h – Consumer heartbeat time
                                             Object                Access         Data type       Description
                                             Subindex
                                             1,016 h               R/W            UINT-16         Cycle time of the heartbeat in ms. The heart‐
                                                                                                  beat becomes inactive with value 0.
                                             00 h                  R/W            UINT-8          Number of entries
                                             01 h                  R/W            UINT-32         Node ID and heart beat time of the moni‐
                                                                                                  tored bus node (see table 36)

                                            Table 36: 1,016 h – Details
                                                           Bit       Description
                                                      31 … 24        Reserved
                                                      23 … 16        Node ID of the monitored bus node
                                                       15 … 0        Heartbeat time of the monitored bus node (typically multiplied by a factor
                                                                     of 1.5)

                                            1,017 h – Producer heartbeat time
                                            Table 37: 1,017 h – Producer heartbeat time
                                             Object                Access         Data type       Description
                                             1,017 h               R/W            UINT-16         Cycle time of the heartbeat in ms. The heart‐
                                                                                                  beat becomes inactive with value 0.


7.3.5.11           Identification values of the FlexChain
                                            1,018 h – Identity object
                                            Table 38: 1,018 h – Identity object
                                             Object                      Access    Data type    Description
                                             1,018 h                     R         RECORD       You use this object to read the following values
                                                                                                from the FlexChain:
                                                                                                Subindex 01 h = Vendor ID (SICK AG)
                                                                                                Subindex 02 h = Product Code
                                                                                                Subindex 03 h = Revision Number (firmware
                                                                                                version)
                                                                                                Subindex 04 h = Serial Number (serial num‐
                                                                                                ber)


7.3.6              Standard object for defining process data
                                            The FlexChain supports 6 Transmit PDOs and 1 Receive PDOs. Each Process Data
                                            Object (PDO) has one communication object and one mapping object.
                                            Communication objects specify which COB IDs are used and which transmission type is
                                            selected for this.
                                            The mapping objects specify which objects are sent as process data.
                                            The Transmit PDOs are defined by the following objects:
                                            •        Objects 1,800 h to 1,805 h contain the communication parameters.
                                            •        Objects 1A00 h to 1A05 h contain the object mapping.
                                            The Receive PDOs are defined by the following objects:
                                            •        The object 1,400 h contains the communication parameters.
                                            •        The object 1,600 h contains the object mapping.
                                            While parameters are being changed, no process data is available.

50         O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                        8023047.1Q01/2025-01-29 | SICK
                                                                                                                           Subject to change without notice

OPERATION 7


                                   Transmission types
                                   The “Transmission type” parameter (subindex 02 h of all PDOs) contains information on
                                   when a Transmit PDO is sent or how Receive PDOs received are handled.
                                   Table 39: Transmission types
                                   Transmission                               Transmission type
                                   Type
                                                                                                         Asynchro‐
                                                      Cyclic      Acyclical     Synchronous                                            RTR
                                                                                                           nous
                                   0                    –             X              X                          –                        –
                                   1–240                X            –               X                          –                        –
                                   241–251                                        Reserved
                                   252                  –            –               X                          –                        X
                                   253                  –            –               –                          X                        X
                                   254 +255             –            –               –                          X                        –

                                   Transmission type 0: Acyclical and synchronous data transmission
                                   During acyclical and synchronous data transmission, only one Transmit PDO is sent if
                                   the FlexChain receives a SYNC message and the beam status of the FlexChain has
                                   changed.
                                   For an Receive PDO, this transmission type means that the data received is evaluated
                                   only after receiving the next SYNC message.

                                   Transmission type 1 to 240: Cyclical and synchronous data transmission
                                   With synchronous and cyclical data transmission, a Transmit PDO is not sent until after
                                   a certain number of SYNC message have been received. This number may be between
                                   1 and 240. A Receive PDO is processed after the reception of the next SYNC message.

                                   Transmission type 252 and 253: RTR data transmission

                                   NOTE
                                   Transmission types 252 and 253 are only permissible for Transmit PDOs.

                                   Some bus module manufacturers do not support RTR data transmission. For this
                                   reason, we do not recommend using transmission types 252 and 253.
                                   RTR stands for “Remote Transmission Request”. With RTR data transmission, data is
                                   only transferred after an RTR frame has been received.
                                   With synchronous RTR data transmission (transmission type 252), the process data is
                                   redetermined every time a SYNC message is received. A Transmit PDO is not transmit‐
                                   ted until the RTR frame has been received.
                                   With asynchronous RTR data transmission (transmission type 253), the current values
                                   are constantly determined. A Transmit PDO is not transmitted until the RTR frame has
                                   been received.

                                   Transmission type 254 + 255: Asynchronous data transmission
                                   In asynchronous data transmission, Transmit PDOs are transmitted in an event-con‐
                                   trolled process. This means transmission occurs every time the beam status of the
                                   FlexChain changes.
                                   A Receive PDO is evaluated immediately after it is received.
                                   This transmission type can be linked with the event timer.




8023047.1Q01/2025-01-29 | SICK                                                           O P E R A T I N G I N S T R U C T I O N S | FlexChain   51
Subject to change without notice

7 OPERATION

                                           Dynamic PDO mapping
                                           Mapping objects are used to define which parameters and data are to be used. In the
                                           mapping object, links are created to objects from the object directory. Objects linked in
                                           the mapping object are sent in Process Data Objects (PDOs).
                                           Subindex 00 h for a mapping object specifies the number of linked objects. If a new
                                           object is linked, the device tests the validity of the link. If the linked object is not
                                           available or cannot be linked, an error message will be triggered.

                                           NOTE
                                           The dynamic PDO mapping is permanently saved in the FlexChain.


7.3.6.1           Communication parameter of the Receive PDO
                                           1,400 h – Communication parameter of the Receive PDO
                                           Table 40: 1,400 h
                                            Object                Access Data type   Description
                                            Subindex
                                            1,400 h               R/W    RECORD      Communication parameter of the Receive PDOs
                                            00 h                  R      UINT-8      Number of
                                                                                     entries
                                            01 h                  R/W    UINT-32     Bit            Description
                                                                                     31             0: PDO is being used
                                                                                                    1: PDO is not being used
                                                                                     30             0: reacts to RTR
                                                                                                    1: does not react to RTR
                                                                                     29             0: 11 bit identifier (CAN 2.0A)
                                                                                                    1: 29 bit identifier (CAN 2.0B)
                                                                                     28 … 0         COB-ID = 0200h + node ID
                                            02 h                  R/W    UINT-8      Transmis‐      Description
                                                                                     sion Type
                                                                                     0              Data is synchronized, but not cyclically sent
                                                                                     1 … 240        Cyclic transmission Clocked with the SYNC
                                                                                                    messages
                                                                                     252            Query by the RTR telegram (synchronous trans‐
                                                                                                    mission)
                                                                                     253            Query by the RTR telegram (asynchronous
                                                                                                    transmission)
                                                                                     254 +255       Event-controlled transmission when beam sta‐
                                                                                                    tus changes
                                            03 h                  R/W    UINT-16     Inhibition time = Idle time between two transmissions
                                                                                     (× 0.1 ms)
                                            04 h                  –      –           Reserved
                                            05h                   R/W    UINT-16     Event timer = Timer for application-specific triggering (× 1 ms)


7.3.6.2           Mapping parameter of the Receive PDO
                                           1,600 h – Mapping parameter for the PDO
                                           Table 41: 1,600 h – mapping configured at the factory
                                            Object                Access Data type   Description
                                            Subindex
                                            1,600 h               R/W    RECORD      Mapping parameter of the first Receive PDO


52        O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                             8023047.1Q01/2025-01-29 | SICK
                                                                                                                               Subject to change without notice

OPERATION 7


                                   Object      Access Data type    Description
                                   Subindex
                                   00 h        R/W      UINT-8     Number of entries = 0 = PDO is deactivated

                                   In the subindexes, the index, the subindex and the width of the affected Receive PDO
                                   sub-area are specified as follows:
                                   Table 42: Mapping
                                   Bits 31 … 16                   Bits 15 … 8                           Bits 7 … 0
                                   Index of the mapped object     Subindex of the mapped                Length in bits
                                                                  object


7.3.6.3            Communication parameter of the Transmit PDOs
                                   The first two Transmit PDOs are activated at the factory using objects 1,800 h and
                                   1,801 h. The remaining Transmit PDOs are deactivated using objects 1,802 h to
                                   1,805 h.

                                   1,800 h … 1,805 h – Communication parameter for Transmit PDOs
                                   Table 43: 1,800 h to 1,805 h
                                   Object      Access Data type    Description
                                   Subindex
                                   1,800 h … R/W        RECORD     Communication parameter of the Transmit PDOs
                                   1,805 h
                                   00 h        R        UINT-8     Number of
                                                                   entries
                                   01 h        R/W      UINT-32    Bit            Description
                                                                   31             0: PDO is being used
                                                                                  1: PDO is not being used
                                                                   30             0: reacts to RTR
                                                                                  1: does not react to RTR
                                                                   29             0: 11 bit identifier (CAN 2.0A)
                                                                                  1: 29 bit identifier (CAN 2.0B)
                                                                   28 … 0         COB-ID = 0,200 h + node ID
                                   02 h        R/W      UINT-8     Transmis‐      Description
                                                                   sion Type
                                                                   0              Data is synchronized, but not cyclically sent
                                                                   1 … 240        Cyclic transmission Clocked with the SYNC
                                                                                  messages
                                                                   252            Query by the RTR telegram (synchronous trans‐
                                                                                  mission)
                                                                   253            Query by the RTR telegram (asynchronous
                                                                                  transmission)
                                                                   254 +255       Event-controlled transmission when process
                                                                                  data changes
                                   03 h        R/W      UINT-16    Inhibition time = Idle time between two transmissions
                                                                   (× 0.1 ms)
                                   04 h        –        –          Reserved
                                   05 h        R/W      UINT-16    Event timer = Timer for application-specific triggering (× 1 ms)




8023047.1Q01/2025-01-29 | SICK                                                          O P E R A T I N G I N S T R U C T I O N S | FlexChain   53
Subject to change without notice

7 OPERATION

                                           Inhibition time
                                           The inhibition time (configured in objects 1,800.03 h to 1,805.03 h) in principle limits
                                           the communication of a device on the CANopen bus.
                                           The inhibition time does not influence the triggering by RTR telegrams.
                                           The inhibition time (transmit delay time) specifies the minimum waiting time in ms
                                           between the transmission of two identical Transmit PDOs. It always has higher priority
                                           than the event timer, the CoS events and triggering with SYNC messages. If, for exam‐
                                           ple, the event timer is set to 100 ms and the inhibition time to 1 s, the respective PDO
                                           is only sent every second.

                                           NOTE
                                           Some bus module manufacturers do not support use of inhibition time. We recommend
                                           using synchronous communication if you want to control the bus load.

                                           Event Timer
                                           Subindex 05 h of the Transmit PDOs contains an event timer. It runs in the background
                                           and triggers an event when it expires. This means if no event occurs in the purely
                                           asynchronous transmission type (beam status change), a Transmit PDO will be sent
                                           when the set event time (in 1 ms increments) expires. No event timer can be set for the
                                           Receive PDO of the FlexChain.

7.3.6.4           Mapping parameter of the Transmit PDOs
                                           Mappings are preconfigured at the factory for the 1A00 h and 1A01 h objects. No
                                           objects are mapped at the factory in the subindexes of the 1A02 h to 1A05 h objects.

                                           1A00 h – Mapping parameter for the 1st Transmit PDO
                                           Table 44: 1A00 h – mapping configured at the factory
                                            Object                Access Data type   Description
                                            Subindex
                                            1A00 h                R/W    RECORD      Mapping parameter of the first Transmit PDO
                                            00 h                  R/W    UINT-8      Number of entries
                                            2,064.0 h             R/W    UINT-32     System status
                                            21E1.1 h              R/W    UINT-32     Qint 1...8
                                            21E0.1 h              R/W    UINT-32     channel 1...8
                                            21E0.2 h              R/R    UINT-32     channel 9...16
                                            21E0.3 h              R/R    UINT-32     channel 17...24
                                            21E0.4 h              R/R    UINT-32     channel 25...32
                                            21E0.5 h              R/R    UINT-32     channel 33...40
                                            21E0.6 h              R/R    UINT-32     channel 40...48

                                           1A01 h – Mapping parameter for the 2nd Transmit PDO
                                           Table 45: 1A01 h – mapping configured at the factory
                                            Object                Access Data type   Description
                                            Subindex
                                            1A01 h                R/W    RECORD      Mapping parameter of the second Transmit PDO
                                            00 h                  R/W    UINT-8      Number of entries
                                            01 h                  R/W    UINT-32     2,200.0 Ch – IDI
                                            02 h                  R/W    UINT-32     21E0.7 h channel 49...56



54        O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                          8023047.1Q01/2025-01-29 | SICK
                                                                                                                            Subject to change without notice

OPERATION 7


                                   Object       Access Data type      Description
                                   Subindex
                                   03 h         R/W     UINT-32       21E0.8 h channel 57...64

                                   1A02 … 1A05 h – Mapping Parameter for Transmit PDOs
                                   Table 46: 1A02 to 1A09 h – Mapping configured at the factory
                                   Object       Access Data type      Description
                                   Subindex
                                   1A02 h …     R/W     RECORD        Mapping parameter of the remaining Transmit PDOs
                                   1A05 h
                                   00 h         R/W     UINT-8        Number of entries = 0 = PDOs are deactivated

                                   How to change the content of the mapping objects:

                                   NOTE
                                   Parameter changes to the PDO mapping objects are only made in Pre-operational
                                   status.

                                   1.     First, set bit 31 to 1 in corresponding object 180xh in subindex 01 h.
                                   2.     Set subindex 00 h to 0 in object 1A0xh.
                                   3.     Configure the objects to be mapped in subindexes 01 h to n of object 1A0xh.
                                   4.     Set subindex 00 h of object 1A0xh to the number of mapped objects.
                                   5.     Then set bit 31 back to 0 in corresponding object 180xh in subindex 01 h.

                                   In the subindexes, the index, the subindex and the width of the affected Receive PDO
                                   sub-area are specified as follows:
                                   Table 47: Mapping
                                   Bits 31 … 16                    Bits 15 … 8                           Bits 7 … 0
                                   Index of the mapped object      Subindex of the mapped                Length in bits
                                                                   object


7.4                RS485 configuration

                                   NOTE
                                   Compared to IO-Link and CANopen, for example, the RS-485 is a pure process data
                                   interface. Service data can be transmitted, but not changed.

                                   RS-485 Framing
                                   An RS-485 frame always consists of an <STX>, process data (ASCII hex or binary),
                                   <ETX>. Transmission in hexadecimal ASCII is the standard.
                                   The maximum process data length is 32 bytes. The process data length is 10 bytes
                                   ex-works. The following process data is transmitted by default.
                                   Table 48: RS485 Framing
                                   Byte                    Function
                                   Byte 1                  System status
                                   Byte 2                  Qint 1 – 8
                                   Byte 3                  Channel 1 – 8
                                   Byte 4                  Channel 9 – 16
                                   Byte 5                  Channel 17 – 24
                                   Byte 6                  Channel 25 – 32


8023047.1Q01/2025-01-29 | SICK                                                           O P E R A T I N G I N S T R U C T I O N S | FlexChain   55
Subject to change without notice

7 OPERATION

                                       Byte                    Function
                                       Byte 7                  Channel 33 – 40
                                       Byte 8                  Channel 41 – 48
                                       Byte 9                  Channel 49 – 56
                                       Byte 10                 Channel 57 – 64

                                      The process data can be individually adapted via the USB interface and Sopas or via
                                      the IO-Link interface. (see configuration Sopas or configuration IO-Link)

                                      Settings of the RS-485 interface
                                      Trigger (index 473, subindex 1, 8 bit):
                                      These settings cannot be made via RS-485, but they affect the RS-485 interface.
                                      Table 49: Trigger (index 473, subindex 1, 8 bit)
                                       Value                   Name
                                       0                       Deactivated
                                       1                       On Process Data Change with Heartbeat
                                       2                       Time Interval
                                       3                       Command Byte Reception <STX><CMD<ETX>
                                       4                       Input Pin Level

                                      On Change with Heartbeat:
                                      –   Interval Time in ms = 0; only in case of change
                                      –   Interval Time in ms > 0; in case of change, and time interval
                                      Time Interval:
                                      –   Interval Time in ms = 0; continuous, the issue is synchronized with the internal
                                          process data cycle
                                      –   Interval Time in ms > 0; time Interval
                                      Command Byte:
                                      –  <STX><CMD><ETX> / <0x02><0x54><0x03>
                                      –  0x54 = ’T’ = Trigger, Blocked Channel Hold Off, see "Commands", page 57
                                      Input Pin:
                                      –    Issue as long as input = 1, the cycle time is identical to the current cycle time of
                                           the system, if the baud rate setting permits this.

                                      Format (index 473, subindex 2, 8 bit):
                                      Process data ASCII hexadecimal or binary.
                                      Table 50: Process data ASCII hexadecimal or binary
                                       Value                   Name
                                       0                       Hexadecimal ASCII
                                       1                       Binary

                                      Baud rate (index 473, subindex 3, 8 bit):
                                      Discrete values 9k6, 38k4, 230k4, 460k8.
                                      Table 51: Discrete values 9k6, 38k4, 230k4, 460k8
                                       Value                   Name
                                       0                       9,600 bits/s
                                       1                       38,400 bits/s
                                       2                       115,200 bits/s
                                       3                       230,400 bits/s


56   O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                 8023047.1Q01/2025-01-29 | SICK
                                                                                                              Subject to change without notice

OPERATION 7


                                   Value                   Name
                                   4                       460,800 bits/s

                                   Parity (index 473, subindex 4, 8 bit):
                                   none oder even
                                   Table 52: none oder even
                                   Value                   Name
                                   0                       No Parity
                                   1                       Even Parity

                                   IntervalTime (index 473, subindex 5, 16 bit):
                                   Table 53: Heartbeat off/Sync with Cycle Time
                                   Value                   Name
                                   0                       Heartbeat off/Sync with Cycle Time
                                   1 – 60,000

                                   Commands
                                   The commands can only be sent if the trigger is set in mode 3 = Command Byte
                                   Reception.
                                   The following commands can be transmitted via the RS-485 to FlexChain. Each com‐
                                   mand starts with <STX> and ends with <ETX>.
                                   –    <STX><’C’><ETX>
                                        Teach-in. Recommendation: Include system status in process date to be able to
                                        poll busy flag active bit.
                                   –    <STX><’H’><ETX>
                                        Blocked Channels Hold on.
                                   –    <STX><’T’><ETX>
                                        Trigger to send process data, Blocked Channel Hold Off.
                                   –    <STX><’o’><ETX>
                                        Sender off.
                                   –    <STX><’s’><ETX>
                                        Sender on
                                   If a command is transferred to FlexChain which FlexChain does not know, FlexChain
                                   answers with
                                   –    <STX><’?’><ETX>
                                        Negative response, unknown command.
                                   –    <STX><’N’><ETX>
                                        Negative response, not available, (Teach-in).

                                   RS-485 LED
                                   –    The LED flashes green for 20 ms with each frame transmitted, if the sequence is
                                        faster, the LED lights up constantly.
                                   –    In case of an unknown command, the LED flashes red once for 0.1 s.
                                   –    With ’Sender off’ the LED flashes red once for 0.5 s.
                                   –    With ’Teach-In’ the LED flashes red once for 1.0 s.




8023047.1Q01/2025-01-29 | SICK                                                          O P E R A T I N G I N S T R U C T I O N S | FlexChain   57
Subject to change without notice

8 DIAGNOSTICS AND TROUBLESHOOTING


8             Diagnostics and troubleshooting
8.1           General diagnostic information
                                       The Device Status object provides general diagnostic information about IO-Link and
                                       CANopen. A Device Status Information (e.g. Maintenance Required) can have several
                                       causes (e.g. Quality of Run Alarm or Teach-In Error) (see table). The Device Status can
                                       be retrieved via index 36 (IO-Link) or index 0x2024 (CANopen).
                                       Table 54: General Diagnostic Information IO-Link & CANopen index
                                        Object name                   Description                                       IO-Link       CAN‐
                                                                                                                        Index         Open
                                                                                                                                      Index
                                        Device status                 Provides information about the general status     36            0x2,02
                                                                      of the FlexChain system                                         4

                                       Detailed information can be found in the IO-Link supplement and/or the ESD descrip‐
                                       tion.
                                       Table 55: Value range of the Device Status
                                        Value = highest is highest pri‐ Definition                      Incident (System Status)
                                        ority
                                                              0         Device is operating properly    -
                                                              1         Maintenance Required            QualityOfRunAlarm OR TeachIn
                                                                                                        error
                                                              2         Out-of-Specification            PinShortCircuitWarning
                                                              3         Functional-Check                InvalidProcessData (caused by
                                                                                                        Busy = Configuration)
                                                              4         Failure                         HardwareError OR Chain Issue -
                                                                                                        Error

                                       In addition to the Device Status, the IO-Link interface offers events for error diagnosis.
                                       Detailed information can be found in the IO-Link supplement. The following information
                                       is available as events:
                                       Table 56: Events
                                        Event Name                                       Type
                                        Device Hardware Fault                            Error
                                        Short Circuit on Output Pin                      Warning
                                        New Parameters                                   Notification
                                        Quality of Run Alarm                             Warning
                                        Teach-In Error                                   Warning
                                        Chain Issue Error                                Error


8.2           Detailed diagnostic information
                                       Detailed diagnostic information can be transmitted via the RS-485, CANopen and
                                       IO-Link serial interfaces and, to a limited extent, via the binary interface (switching
                                       outputs). In addition, SOPAS ET offers a user-friendly display of diagnostic information.




58    O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                     8023047.1Q01/2025-01-29 | SICK
                                                                                                                   Subject to change without notice

DIAGNOSTICS AND TROUBLESHOOTING 8


                                   SOPAS




                                                                    Figure 30: Troubleshooting host




                                   Figure 29: General status
                                   Table 57: Diagnostic symbols
                                   Icons              Description
                                                      Note
                                                      e.g. TeachIn recommended after running an AutoAssignment




                                                      Error
                                                      e.g. errors in the arrangement of the guests. A guest was disconnected
                                                      during operation.




                                                      Note
                                                      e.g. TeachIn can only be carried out directly on the guest.




                                                      Warning
                                                      e.g. Quality of Run Alarm




                                   In Sopas, the diagnosis status is displayed in the System Status field in traffic light
                                   colors. The following definition applies:
                                   –    Green: Device OK
                                   –    Yellow: Warning
                                   –    Red: Error
                                   More detailed diagnostic information can be displayed by clicking the “System Status”
                                   field. In addition, the relevant guest is marked with an icon in the system field. More
                                   detailed information can be obtained via a mouse-over.




8023047.1Q01/2025-01-29 | SICK                                                            O P E R A T I N G I N S T R U C T I O N S | FlexChain   59
Subject to change without notice

8 DIAGNOSTICS AND TROUBLESHOOTING

                                      Via IO-Link, CAN and RS-485
                                      Errors, warnings and messages are output by three main diagnostic objects. These are:
                                      System Status, Chain Issue and Quality of Run Alarm.
                                      Only a limited diagnostic functionality is available for the RS-485 interface with the
                                      System Status. The System Status can be transferred via this interface, but cannot be
                                      parameterized.
                                      The complete diagnostic information is available for the CANopen and IO-Link interfa‐
                                      ces.
                                      Table 58: Diagnostic Information IO-Link & CANopen Index
                                       Object name                        Description                                            IO-Link       CAN-
                                                                                                                                 Index         Open
                                                                                                                                               Index
                                       System status                      Information about the status of the FlexChain          100           0x2,06
                                                                          system. Can be transmitted via the process                           4
                                                                          data.
                                       Chain Issue                        Information on the structure and communica‐            300           0x212C
                                                                          tion of the FlexChain system
                                       Quality of Run Alarm               Warning if the received signal falls below a           309           0x2,13
                                                                          stable value.                                                        5
                                       System Status Mask                 Configuration for ORring the SystemStatus as           447,          0x21BF
                                                                          binary signal via the PINs.                            448,          0x21C0
                                                                                                                                 449,          0x21C1
                                                                                                                                 450,          0x21C2
                                                                                                                                 451,          0x21C3
                                                                                                                                 452           0x21C4

                                      A special feature to be emphasized is the System Status. This can be transmitted
                                      cyclically via all serial interfaces via the process data and as “Masked System Status”
                                      via the PINs. It gives an overview of the status of the system. The following information
                                      is available in the System Status.
                                      Table 59: Bit assignment of the System Status transmitted via Process Data
                                       Bit Su Incident                              Description
                                           bIn
                                           de
                                           x
                                       Bit 1           Pin Short Circuit Warning    Bit is set in case of a short circuit on at least one Output
                                       0
                                       Bit 2           Invalid Process Data         Bit is set in case of Invalid Process Data
                                       1
                                       Bit 3           Reserved                     Not used
                                       2
                                       Bit 4           Busy                         Bit is set during ongoing configuration (e.g. Teach-In)
                                       3
                                       Bit 5           Quality of Run Alarm         Bit is set in case of a Quality of Run Alarm (critical signal
                                       4                                            received)
                                       Bit 6           Hardware Error               Bit is set in case of an Hardware Error
                                       5
                                       Bit 7           Teach-in Error               Bit is set in case the teach-in hasn't been excecuted
                                       6                                            successfully
                                       Bit 8           Chain Issue                  Bit is set in case of a chain issue (e.g. not correct wiring).
                                       7                                            See chapter 5.2 and index 300




60   O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                               8023047.1Q01/2025-01-29 | SICK
                                                                                                                            Subject to change without notice

DIAGNOSTICS AND TROUBLESHOOTING 8




                                   Figure 31: Configuration of PIN 4 / Masked System Status

                                   Detailed information on the communication of the FlexChain system can be queried
                                   using the “Chain Issue” object. As with the Quality of Run Alarm, it is possible to localize
                                   the sensor via the object. The Chain Issue can be queried via the CANopen and IO-Link
                                   interfaces.




8023047.1Q01/2025-01-29 | SICK                                                          O P E R A T I N G I N S T R U C T I O N S | FlexChain   61
Subject to change without notice

8 DIAGNOSTICS AND TROUBLESHOOTING

                                      Diagnostic information via the display LEDs
                                      Table 60: Diagnostics via display LEDs


                                       Function                        FlexChain Guest                  Host                     Host
                                                                                                 only system traf‐          only PIN LEDs
                                                                  Sender           Receiver
                                                                                                      fic light
                                       Supply                green perma‐      green perma‐      green perma‐           -
                                                             nently on         nently on         nently on
                                       IO-Link Communi‐ -                      -                 green 1 Hz             -
                                       cation
                                       No channel         -                    yellow on         Depending on the -
                                       blocked                                                   PIN configuration.
                                       Receiver sees sig‐                                        Always displays
                                       nal                                                       the signal of the
                                                                                                 respective PIN.
                                       Status of switch‐     -                 -                 -                      Status of the
                                       ing output/input                                                                 switching output
                                                                                                                        or switching input
                                       Quality of Run        -                 yellow 8 Hz       yellow 8 Hz            -
                                       Alarm
                                       Teach-in active       yellow 1 Hz       yellow 1 Hz       yellow 1 Hz            -
                                                             min 3x flash      min 3x flash      min 3x flash
                                       FindMe                green + yellow    green + yellow    green + yellow +       Q-LEDs 1 Hz
                                                             1 Hz              1 Hz              red 1 Hz
                                       Chain Issue -         -                 -                 red 8 Hz               PIN2 LED AA 8 Hz
                                       Error
                                       Chain Issue -         -                 -                 yellow 3 Hz            PIN2 LED AA 3 Hz
                                       Warning
                                       Hardware fault        yellow perma‐     yellow perma‐     red permanently        -
                                                             nently on         nently on         on
                                                             green off         green off         green off
                                       Short circuit of a    -                 -                 red permanently        -
                                       Q                                                         on
                                       TeachIn Error         -                 yellow 8 Hz, poor yellow 8 Hz            PIN4 LED TCH
                                                                               alignment or an                          8 Hz
                                                                               object in the
                                                                               beam path during
                                                                               the teach-in proc‐
                                                                               ess.
                                       Local (control    -                     -                 yellow 8 Hz            -
                                       panel) activation                                         red 8 Hz
                                       of the pushbutton
                                       lock
                                       Activating/deacti‐ -                    -                 -                      300 ms Inversion
                                       vating pushbut‐                                                                  of the current sta‐
                                       ton lock                                                                         tus of all
                                                                                                                        menu/PIN LEDs
                                       Local (control    -                     -                 -                      All menu LEDs
                                       panel) performing                                                                flash 3x 1 Hz
                                       a factory reset




62   O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                      8023047.1Q01/2025-01-29 | SICK
                                                                                                                   Subject to change without notice

DIAGNOSTICS AND TROUBLESHOOTING 8


                                   Diagnostic information Booster LEDs
                                   Table 61: LED Booster
                                   Function                                         Booster
                                   Supply via FCin                                  Yellow permanently on
                                   Supply via Power input                           Green permanently on

                                   Diagnostic information Adapter LEDs
                                   Table 62: LED Adapter
                                   Function                                         Adapter
                                   Supply via FCin                                  Grün permanently on
                                   Guest switching output Q1 HIGH                   Yellow on
                                   Guest switching output Q1 LOW                    Yellow off
                                   FindMe                                           Green + Yellow 1 Hz


8.3                Troubleshooting
                                   FlexChain host
                                   Table 63: FlexChain Host troubleshooting
                                   LED/fault pattern             Cause                                  Measures
                                   red error LED lights up       Short-circuit                          Check connections
                                   Yellow TCH LED flashes (8     Teach-in faulty                        Check the alignment of all
                                   Hz)                                                                  guests
                                   yellow presence LED                                                  Perform teach-in
                                   flashes (8 Hz)
                                   Yellow LED AA flashes (8      Position or zones inconsistent.        Read out ChainIssue code (via
                                   Hz)                           Maximum number of guests               IO-Link index 300, CANopen
                                   Red LED Error flashes (8      exceeded.                              index 0x212C or Sopas) to
                                   Hz)                           Communication error.                   restrict the error
                                                                 Connection sequence changed.           Check connection of all guests
                                                                 supply voltage for booster not         and alignment of the sensors
                                                                 connected / supply voltage for         Perform AutoAssign
                                                                 booster polarity reversed              Perform teach-in

                                   FlexChain Guests GL6-C
                                   Table 64: FlexChain GL6-C troubleshooting
                                   LED/fault pattern             Cause                                  Measures
                                   yellow LED of the GL6-C      Sensor not aligned correctly            Check application
                                   does not light up, no object with the reflector or not taught        Align the sensor with the reflec‐
                                   in the beam path             in.                                     tor and teach in.
                                                                Distance between sensor and
                                                                reflector is too large
                                   Yellow LED of the GL6-        Object is too small or the beam        Check application, if applicable
                                   C lights up, although an      is being reflected and diverted        remove reflection
                                   object is in the beam path.   away from it.




8023047.1Q01/2025-01-29 | SICK                                                            O P E R A T I N G I N S T R U C T I O N S | FlexChain   63
Subject to change without notice

8 DIAGNOSTICS AND TROUBLESHOOTING

                                      FlexChain Guests GTB6-C
                                      Table 65: FlexChain GTB6-C troubleshooting
                                       LED/fault pattern             Cause                             Measures
                                       yellow LED of the GTB6-C      The sensing range distance is     Check application
                                       lights up, no object in the   too large                         Reduce the sensing range
                                       beam path                     Background influence is too
                                                                     great.
                                       Yellow LED does not light     Object too small.                 Check application
                                       up, an object is in the       Remission capability of the       Increase the sensing range
                                       beam path                     object is insufficient
                                                                     Distance between the sensor
                                                                     and the object is too long or
                                                                     sensing range is set too short

                                      FlexChain Guests GSE6-C and SLG-2
                                      Table 66: FlexChain GSE6-C and SLG-2 troubleshooting
                                       LED/fault pattern             Cause                             Measures
                                       Yellow LED of the GE6-C      Distance between sender and        Check application
                                       does not light up, no object receiver is too large:             Align the sender with the
                                       in the path of the beam.     Sender not aligned correctly       receiver and teach in.
                                                                    with receiver.
                                       Yellow LED of the GE6-C       Object is too small or the beam   Check application
                                       lights up, no object in the   is being reflected and diverted   Where applicable, remove the
                                       path of the beam.             away from it.                     cause of the reflection

                                      FlexChain Guests Adapter
                                      Table 67: Troubleshooting FlexChain Adapter
                                       LED/fault pattern             Cause                             Measures
                                       yellow LED lights up          Hardware error                    Substitute the device
                                       Green LED does not light
                                       up




64   O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                     8023047.1Q01/2025-01-29 | SICK
                                                                                                                  Subject to change without notice

MAINTENANCE 9


9                  Maintenance
9.1                Servicing
                                   The deviceis maintenance-free. Depending on the ambient conditions, regular cleaning
                                   is required.
                                   Depending on the ambient conditions of the device, the front screens must be cleaned
                                   regularly and in the event of contamination. Static charges can cause dust particles to
                                   be attracted to the front screen.

                                   NOTE
                                   ►    Do not use aggressive cleaning agents.
                                   ►    Do not use abrasive cleaning agents.
                                   ►    Do not use cleaning agents that contain alcohol, e.g., window cleaner.

                                   We recommend anti-static cleaning agents.
                                   We recommend the use of anti-static plastic cleaner (SICK part number 5600006) and
                                   the SICK lens cloth (SICK part number 4003353).
                                   How to clean the front screen:
                                   ►    Use a clean, soft brush to remove dust from the front screen.
                                   ►    Then wipe the front screen with a clean, damp cloth.
                                   ►    Check the position of the sender and receiver after cleaning.
                                   ►    Perform the teach-in process on the MLG-2 again. To do this, press the Teach
                                        pushbutton.

9.2                Maintenance
                                   During operation, the device works maintenance-free.

                                   Depending on the assignment location, the following preventive maintenance tasks
                                   may be required for the device at regular intervals:
                                   Table 68: Maintenance schedule
                                   Maintenance work                   Interval                                               Implementation
                                   Clean housing and front screen     Cleaning interval depends on ambi‐                     Specialist
                                                                      ent conditions and climate
                                   Check screw connections and plug   Every 6 months                                         Specialist
                                   connectors




8023047.1Q01/2025-01-29 | SICK                                                         O P E R A T I N G I N S T R U C T I O N S | FlexChain   65
Subject to change without notice

10 DECOMMISSIONING


10             Decommissioning
10.1           Disassembly and disposal
                                        Disassembling the device
                                        1.       Switch off the supply voltage to the device.
                                        2.       Detach all connecting cables from the device.
                                        3.       If the device is being replaced, mark its position and alignment on the bracket or
                                                 surroundings.
                                        4.       Detach the device from the bracket.

                                        Disposing of the device
                                        Any device which can no longer be used must be disposed off in an environmentally
                                        friendly manner in accordance with the applicable country-specific waste disposal regu‐
                                        lations.

                                        NOTE
                                        Disposal of batteries, electric and electronic devices
                                        • According to international directives, batteries, accumulators and electrical or
                                            electronic devices must not be disposed of in general waste.
                                        • The owner is obliged by law to return this devices at the end of their life to the
                                            respective public collection points.
                                        •


                                                          This symbol on the product, its package or in this document, indicates
                                                 that a product is subject to these regulations.


10.2           Returning devices
                                        ►        Do not dispatch devices to the SICK Service department without consultation.

                                        NOTE
                                        To enable efficient processing and allow us to determine the cause quickly, please
                                        include the following when making a return:
                                        ■        Details of the contact person
                                        ■        Description of the application
                                        ■        Description of the fault that occurred




66     O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                  8023047.1Q01/2025-01-29 | SICK
                                                                                                                 Subject to change without notice

TECHNICAL DATA 11


11                 Technical data
11.1               Host performance
Table 69: Host performance
 Attribute                                                              Value
 Number of connectable guests                                           max. 60 (max. 30 / port)1)
 Number of channels                                                     max. 255
 Max. total cable length                                                40 m/port2)
 Max. sensor to sensor or sensor to host cable length                   30 m
1)   Number depends on the type of connected sensors
2)   For > 25 guests/port: Total length plus additional extension cables ≤ 10 m/port


11.2               Interfaces host
Table 70: Interfaces host
 Attribute                                                Standard IO-     Advanced IO-                    CANopen                           RS485
                                                          Link             Link
                                                                                            System/Q                CAN connec‐
                                                                                                                    tor
 No. of IOs (push-pull switching mode)                    1xQ 2xI/O        1xQ 5xI/O        1xQ 1xI/O               -                        1xQ 1xI/O
 Serial process data interface                            IO-Link          IO-Link          IO-Link                 CANopen                  IO-Link
                                                                                                                                             RS485
 Parameterization interface                               Control panel Control panel Control panel                                          Control panel
                                                          IO-Link       IO-Link       IO-Link                                                IO-Link
                                                          USB           USB           USB                                                    USB
                                                                                      CANopen
 Data transmission rate                                        COM3 (230.4 kbit/s)          COM3          50 kbit/s,                         COM3
                                                                                            (230.4 kbit/s 125 kbit/s,                        (230.4 kbit/s
                                                                                            )             250 kbit/s,                        )
                                                                                                          500 kbit/s,                        9.6 kbit/s，
                                                                                                          1 Mbit/s                           38.4 kbit/s，
                                                                                                                                             11.52 kbit/
                                                                                                                                             s，
                                                                                                                                             230.4 kbit/
                                                                                                                                             s，
                                                                                                                                             460.8 kbit/s
 Connection type (control)                          PIN M12, 5-pin,        M12, 8-pin,      M12, 5-pin,             M12, 5 pole, M12, 8-pin,
 Pigtail length 0.5 m (except CANopen)                  male               male             male                    male           male
                                                                                                                    Pigtail length
                                                                                                                    0.3 m
                                                    1     L+ (BN)          L+ (BN)          L+ (BN)                 n.c. (BN)                L+ (BN)
                                                    2     Q2 / IN1         Q2 / IN1         Q2 / IN1                n.c. (WH)                Q2 / IN1
                                                          (WH)             (WH)             (WH)                                             (WH)
                                                    3     M (BU)           M (BU)           M (BU)                  GND (BU)                 M (BU)
                                                    4     Q1 / C (BK)      Q1 / C (BK)      Q1 / C (BK)             CAN1_H (VT) Q1 / C (BK)
                                                    5     Q3 / IN2 (GY) Q3 / IN2 (GY) n.c. (GY)                     CAN1_L (OG) n.c. (GY)
                                                    6     -                Q4 / IN3 (PK) -                          -                        n.c. (PK)
                                                    7     -                Q5 / IN4 (VT) -                          -                        RS485_A
                                                                                                                                             (VT)
                                                    8     -                Q6 / IN5         -                       -                        RS485_B
                                                                           (OG)                                                              (OG)
 Connection type (USB)                                                              Pigtail length 0.3 m micro USB


8023047.1Q01/2025-01-29 | SICK                                                                  O P E R A T I N G I N S T R U C T I O N S | FlexChain    67
Subject to change without notice

11 TECHNICAL DATA

 Attribute                                                           Standard IO-   Advanced IO-            CANopen                     RS485
                                                                     Link           Link
                                                                                                   System/Q         CAN connec‐
                                                                                                                    tor
 Connection type (guests)                                                                        Port A and port B
                                                                                             Pigtail length each 1.5 m
                                                                                             Pigtail M8, 4 pole, female
1    For > 25 guests/port: Total length plus additional extension cables ≤ 10 m/port


11.3                 Host software features
Table 71: Host software features
 Attribute                                                                      Value
 Host software features                                                         Guest parameterization
                                                                                Zone definition
                                                                                Measurement functions, logic gates
                                                                                Interface parameterization
                                                                                Service data


11.4                 System response time
Table 72: System response time
 Attribute                                                                      Value
 Scan time (reproducibility) Tscan                6)




                                                                                Minimum scan time = 1 ms
                                                                                TFC_GTB6 = 185 µs
                                                                                TFC_GL6 = 185 µs
                                                                                TFC_GSE6 = 210 µs
                                                                                TFC_SLG2_A2) = 248µs + N1) x 46µs
                                                                                TFC_SLG2_B3) = 280µs + N1) x 78µs
                                                                                TFC_A = 150 μs7)
 Maximum minimum dwell time                                                     2x Tscan4)
 Maximum response time                                                          3x Tscan +500 µs5)
1)   N = number of beams/channels
2)   SLG-2 with operating sensing range of 4 m (type A) or 1.7 m (type C)
3)   SLG-2 with operating sensing range of 6.5 m (type B) or 3 m (type D)
4)   With light grid sensing range type B; minimum dwell time = 4 x Tscan
5)   With light grid sensing range type B; response time = 5 x Tscan +500 µs
6)   SLG2: If cross beam is activated, the scanning time of the individual light grid doubles.
7)   Response time does not consider the scanning time / update rate of the device connected on the Adapter.


11.5                 Mechanics/electronics/host
Table 73: Mechanics/electronics/host
 Attribute                                                                      Value
 Supply voltage VS                                                              24 V ±20%1)




68           O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                        8023047.1Q01/2025-01-29 | SICK
                                                                                                                             Subject to change without notice

TECHNICAL DATA 11


 Attribute                                                   Value
 Maximum current consumption (at maximum number of           600 mA @ 24 V2)
 guests)
 Output current                                              Max. 100 mA
 Logic level                                                 Active 15 V … 30 V
                                                             Inactive 0 V … 5 V
 Capacitive output load                                      max. 100 nF
 Inductive output load                                       max. 1 H
 Dimensions in mm                                            118 x 35 x 25 (without cables)
 Housing material                                            Plastic, ABS
 Enclosure rating                                            IP65 / IP67
 Electrical protection class                                 III
 Circuit protection                                          UV connections, reverse polarity protected
                                                             Output Q short-circuit protected
                                                             Interference-pulse suppression
 Storage temperature                                         -25° C to 70° C
 Operating temperature                                       Host -25° C - 50° C
 Vibration/shock resistance of host                          Single Shock:
                                                             30 g, 11 ms, 6 each axis
                                                             DIN EN 60068-2-27
                                                             Continuous Shock:
                                                             25 g, 6 ms, 1000 each axis
                                                             DIN EN 60068-2-27
                                                             Vibration:
                                                             10 grms 20 Hz…2,000 Hz, 2 h each axis
                                                             IEC 60068-2-64
 Electromagnetic compatibility                               61000-6-2 immunity / 61000-6-3 emission
 MTBF                                                        > 50,000 h
 Weight of host                                              5-pin IO-Link: 154 g
                                                             8-pin IO-Link, RS485: 161 g
                                                             CANopen: 170 g
 Initialization time                                         <3s
 Synchronization of port A/port B                            Cable
1)   Operation in short-circuit protected network max. 8 A
2)   Without load on the outputs


11.6               Technical data guests

11.6.1             Technical data G6-C – general
Table 74: General data GL6-C
 Attribute                                                   Value
 Enclosure rating                                            IP67
 Protection class                                            III
 Circuit protection                                          A, D1)
 Ambient temperature, operation                              -25 °C – 55 °C




8023047.1Q01/2025-01-29 | SICK                                                     O P E R A T I N G I N S T R U C T I O N S | FlexChain   69
Subject to change without notice

11 TECHNICAL DATA

 Attribute                                                           Value
 Vibration/shock resistance of G6 guest                              Single Shock:
                                                                     30 g, 11 ms, 6 each axis
                                                                     DIN EN 60068-2-27
                                                                     Continuous Shock:
                                                                     25 g, 6 ms, 1,000 each axis
                                                                     DIN EN 60068-2-27
                                                                     Vibration:
                                                                     10 grms 20 Hz…2,000 Hz, 2 h each axis
                                                                     IEC 60068-2-64
 Weight of G6 guests                                                 23 g (GTB, GL, GS, GE)
1)   A = UB connections reverse polarity protected
     C = interference suppression
     D = outputs overcurrent and short-circuit protected


11.6.2               Technical data GL6-C
Table 75: General data GL6-C
 Attribute                                                           Value
 Sensing range RW max. (with PL80A reflector)                        0.03 ... 6.0 m
 Light spot size / distance                                          8 mm / 350 mm


11.6.3               Technical data GSE6-C
Table 76: General data GSE6-C
 Attribute                                                           Value
 Sensing range RW max. (with PL80A reflector)                        0 ... 15 m
 Light spot size / distance                                          375 mm / 12 m


11.6.4               Technical data GTB6-C
Table 77: General data GTB6-C
 Attribute                                                           Value
 Sensing range RW max (with 90% remission)                           5 ... 250 mm
 Light spot size / distance                                          6 mm / 100 mm


11.6.5               Technical data SLG-2
Table 78: SLG-2 features
 Features
 Technology                                                          Sender/receiver
 Beam separation                                                     10/25/50 mm
 MDO1) parallel beam                                                 15/30/55 mm
 MDO cross beam (detection only)
       1)
                                                                     9/16.5/29 mm – in the range (0.25 to 0.75) x sender-
                                                                     receiver distance
 Parameterization                                                    via FlexChain Host
1)   MDO = Minimum Detectable Object.




70           O P E R A T I N G I N S T R U C T I O N S | FlexChain                                       8023047.1Q01/2025-01-29 | SICK
                                                                                                            Subject to change without notice

TECHNICAL DATA 11


Table 79: Performance SLG-2
 Performance
 Operating range                                           Type A: 4 m
                                                           Type B: 6.5 m
                                                           Type C: 1.7 m
                                                           Type D: 3 m
 Maximum sensing range                                     Type A: 6 m
                                                           Type B: 9.1 m
                                                           Type C: 2.4 m
                                                           Type D: 4.2 m
 Minimum distance                                          0m
 Minimum distance                                          5 x beam separation
 Cross-beam function active

Table 80: Mechanics/electronics
 Mechanics/electronics
 Wavelength                                                850 nm
 Protection class                                          III
 Dimensions                                                12x24 mm2)
 Housing material                                          PMMA, aluminum
 Enclosure rating                                          IP65 / IP67
 Longitudinal cascading without blind zones                Depending on the required MDO and the device lengths, there
                                                           are different specifications for the installation of the light grid
                                                           as well as the permissible temperature range in the applica‐
                                                           tion. (see under Cascading several light grids)
2)   Customer-specific cable lengths can be implemented.

Table 81: Ambient data
 Ambient data
 Protection class                                          Protection class III according to EN61140
 EMC                                                       61000-6-2, 61000-6-4
 Ambient light immunity                                    Type A, B:
                                                           50.000 lx, indirect
                                                           Type C, D:
                                                           100.000 lx, direct
                                                           150.000 lx, indirect
 Ambient temperature                                       -25 °C to +55 °C
 Storage temperature                                       -25 °C – 70 °C
 Vibration resistance                                      0.5 mm, 10 Hz ... 55 Hz
 Impact load                                               10 g 16 ms -> DIN EN 60068-2-27
 Certificates                                              UL, RoHS, CE, CCC, ACMA, EAC, WEEE




8023047.1Q01/2025-01-29 | SICK                                                    O P E R A T I N G I N S T R U C T I O N S | FlexChain   71
Subject to change without notice

11 TECHNICAL DATA

                                                                 1 Distance housing edge to mounting bracket ≤ 10 cm
                                                                 2 Distance mounting bracket to mounting bracket ≤ 75 cm
                                                                   (in an application with high mechanical loads (vibration,
                                                                   shock) ≤ 40 cm)




              1



              2



              1




Figure 32: Mounting bracket and mounting dis‐
tance

Mounting distance dm between cascading light grids taking into consideration temperature fluctuations.




Figure 33: Cascading several light grids




72       O P E R A T I N G I N S T R U C T I O N S | FlexChain                                           8023047.1Q01/2025-01-29 | SICK
                                                                                                            Subject to change without notice

TECHNICAL DATA 11


Table 82: Mounting distance dm between cascading light grids taking into consideration temperature fluctuations.
                                                    I1 + I2
                                                                                                        dm2)                            MDOk1)
                 1,600 mm             2,000 mm                2,400 mm           2,800 mm
                    ±9K                  ±7K                    ±6K                ±5K              0.55 mm                         dc 3)+5 mm
                   ± 16 K               ± 13 K                 ± 11 K              ±9K              1.05 mm                         dc3) +6 mm
     ΔT
                   ± 24 K               ± 19 K                 ± 16 K             ± 14 K            1.55 mm                           dc3) 7 mm
                   ± 48 K               ± 38 K                 ± 32 K             ± 27 K            3.05 mm                        dc3) + 10 mm
1)   MDOk = Smallest detectable object between two cascades.
2)   Mounting distance dm between cascading SLGs
3)   Beam separation dc


11.6.6             Technical data Adapter
Table 83: Features Adapter
 Attribute                                                               Value
 Device version                                                          FlexChain Guest
 Principle                                                               Adapter to connect 24V PNP/NPN(1)/PushPull sensor to Flex‐
                                                                         Chain System1)
1)   for NPN sensors it's necessary to apply an pull-up resistor.

Table 84: Mechanics Adapter
 Attribute                                                               Value
 Housing material                                                        ABS
 Connection type Sensor                                                  M12 4 pin, female
 Cable length to Sensor                                                  500 mm
 Cable length to next FlexChain Guest                                    500 mm
 Dimensions                                                              60,4 mm x 37,4 mm x 13 mm
 Weight                                                                  42 g
 Protection class                                                        III
 tightening torque                                                       0,5 Nm

Table 85: Electronics Adapter
 Attribute                                                               Value
 Supply voltage                                                          12 V, via FlexChain (host)
 Maximum power consumption connected sensor                              65 mA 24V ± 10 %
 Digital Input
 Number                                                                  1
 Type                                                                    Digital Input, 200 µA max input current, 10 pF capacitance
 Signal Voltage HIGH                                                     > 12.5 V
 Signal Voltage LOW                                                      <9V

Table 86: Ambient Data Adapter
 Attribute                                                               Value
 Enclosure rating                                                        IP54
 Shock resistance                                                        30 g, 11 ms; 12 shocks / axis
 Vibration resistance                                                    10…2000 Hz, 10 grms, 120 min.
 EMC                                                                     IEC 61000-6-2 immunity / 61000-6-3 emission
 Ambient operating temperature                                           -25°C …+55°C


8023047.1Q01/2025-01-29 | SICK                                                                O P E R A T I N G I N S T R U C T I O N S | FlexChain   73
Subject to change without notice

11 TECHNICAL DATA

 Attribute                                                              Value
 Ambient storage temperature                                            -25°C …+70°C
 Adpter reproducebility for FlexChain Manual                            150 µs


11.6.7               Technical data Booster
Table 87: Features Booster
 Attribute                                                              Value
 Device version                                                         FlexChain Booster
 Principle                                                              Booster (max. 1A) to power the FlexChain with extra external
                                                                        power supply to be able to enlarge the number of FlexChain
                                                                        guests

Table 88: Mechanics Booster
 Attribute                                                              Value
 Housing material                                                       ABS
 Connection type Sensor                                                 M12 4 pin, male
 Cable length to Sensor                                                 500 mm
 Cable length to next FlexChain Guest                                   500 mm
 Dimensions                                                             60,4 mm x 37,4 mm x 13 mm
 Weight                                                                 42 g
 Protection class                                                       III
 tightening torque                                                      0,5 Nm

Table 89: Electronics Booster
 Attribute                                                              Value
 Supply voltage                                                         24 V ±10%
 Maximum power consumption connected sensor                             600 mA @ 24 V
 Protection                                                             Reverse-Polarity Protected

Table 90: Ambient Data Booster
 Attribute                                                              Value
 Enclosure rating                                                       IP54
 Shock resistance                                                       30 g, 11 ms; 12 shocks / axis
 Vibration resistance                                                   10…2000 Hz, 10 grms, 120 min.
 EMC1)                                                                  IEC 61000-6-2 immunity / 61000-6-4 emission
 Ambient operating temperature                                          -25°C …+50°C
 Ambient storage temperature                                            -25°C....70°C
1)   In a residential environment, this product may cause radio inteference, in which case the user may be required to take adequate measures.




74           O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                8023047.1Q01/2025-01-29 | SICK
                                                                                                                     Subject to change without notice

TECHNICAL DATA 11


11.7               Dimensional drawings
FlexChain Host
                                   500 (19.69)                          109.4 (4.31)         1,500 (59.06)
                                                                  15.9 (0.63)
                                                                            82.6 (3.25)    5.5 (0.22)

                                                                               5                                                1
 3



                                                  20.1   (0.79)                           5.5 (0.22)
                                                                                                                                2
                  4                                                                       24 (0.94)
                                           300 (11.81)                                    35 (1.38)

Figure 34: Dimensional drawing – FlexChain Host Standard
1        Port-A, pigtail M8, 4-pin, female
2        Port B, pigtail M8, 4-pin, female
3        PLC, pigtail M12, 5-pin / 8-pin, male
4        Micro USB
5        Control panel




8023047.1Q01/2025-01-29 | SICK                                                                   O P E R A T I N G I N S T R U C T I O N S | FlexChain   75
Subject to change without notice

11 TECHNICAL DATA

FlexChain Host CANopen
                                       500 (19.69)                                              109.4 (4.31)         1,500 (59.06)
                                               300 (11.81)                                15.9 (0.63)
                                                                                                    82.6 (3.25)    5.5 (0.22)
                            4                                                                          6                               1
 3



                                                          20.1   (0.79)                                           5.5 (0.22)
                                                                                                                                       2
                        5                                                                                         24 (0.94)
                                               300 (11.81)                                                        35 (1.38)

Figure 35: Dimensional drawing - FlexChain Host CANopen
1      Port-A, pigtail M8, 4-pin, female
2      Port B, pigtail M8, 4-pin, female
3      PLC PLC, pigtail M12, 5-pin, male
4      CANopen PLC, pigtail M12, 5-pin / 8-pin, male
5      Micro USB
6      Control panel

FlexChain GL6-C
                              0.5
                            (0.02)       21 (0.83)
                                                                          3
                                                                                                 4 5
                        0.5   (0.02)

                                                                 25.4 (1.0)
                        2                                        28.5 (1.12)
         7.6   (0.3)
                                                                 31.5 (1.24)
                        1
         9.7   (0.38)



                                                                          11.4   (0.45)


                                                             3 (0.12)                           12 (0.47)
                                                            9.7 (0.38)
                                           18.3 (0.72)




Figure 36: Dimensional drawing - FlexChain GL6-C
1      Center of optical axis, sender
2      Center of optical axis, receiver
3      M3 threaded mounting hole
4      Green LED
5      Yellow LED




76       O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                                       8023047.1Q01/2025-01-29 | SICK
                                                                                                                                        Subject to change without notice

TECHNICAL DATA 11


FlexChain GSE6-C
                                                       0.5
                                                   (0.02)       21 (0.83)
                                                                                  3
                                                                                                    4 5
                                                 0.5   (0.02)

                                                                               25.4 (1.0)
                                                 2                             28.5 (1.12)


                                   17.3 (0.68)
                                                                               31.5 (1.24)
                            1
             9.7   (0.38)



                                                                                    11.4   (0.45)


                                                                                3 (0.12)            12 (0.47)
                                                                               9.7 (0.38)
                                                                 18.3 (0.72)




Figure 37: Dimensional drawing - FlexChain GSE6-C
1        Center of optical axis, sender
2        Center of optical axis, sender
3        M3 threaded mounting hole
4        Green LED
5        Yellow LED




8023047.1Q01/2025-01-29 | SICK                                                                                  O P E R A T I N G I N S T R U C T I O N S | FlexChain   77
Subject to change without notice

11 TECHNICAL DATA

FlexChain GTB6-C
                              0.5
                            (0.02)     21 (0.83)
                                                                 3
                                                                                  4 5
                        0.5   (0.02)
         2.8   (0.11)
                                                             25.4 (1.0)
                        2                                    28.5 (1.12)
         7.6   (0.3)
                                                             31.5 (1.24)
                        1
         9.7   (0.38)



                                                                  11.4   (0.45)


                                                             3 (0.12)             12 (0.47)
                                                            9.7 (0.38)
                                        18.3 (0.72)

                6




Figure 38: Dimensional drawing - FlexChain GSE6-C
1      Center of optical axis, sender
2      Center of optical axis, receiver
3      M3 threaded mounting hole
4      Green LED
5      Yellow LED
6      Potentiometer: adjusting the sensing range




78       O P E R A T I N G I N S T R U C T I O N S | FlexChain                                8023047.1Q01/2025-01-29 | SICK
                                                                                                 Subject to change without notice

TECHNICAL DATA 11


FlexChain Adapter
                                 37.4 (1.47)

                                 31.4 (1.24)



                                                  11.9 (0.47)
                                    25.2                                      13 (0.51)
                                   (0.99)
                                  1

3.2
               (0.
                  13


                                                                60.4 (2.38)
                       )



                     2



 19.5 (0.77)
                                                  10.5 (0.41)




                                                                                  155.9 (6.14)




 42.8 (1.69)                                      36 (1.42)



                             3              4
Figure 39: Dimensional drawing - FlexChain Adapter
1                          Male connector, M8, 4-pin
2                          Fixing hole Ø 3,2 mm
3                          Cable with M12 female connector
4                          Cable with M8 female connector




8023047.1Q01/2025-01-29 | SICK                                                                   O P E R A T I N G I N S T R U C T I O N S | FlexChain   79
Subject to change without notice

11 TECHNICAL DATA

FlexChain Booster
                                  37.4 (1.47)

                                  31.4 (1.24)



                                                              11.9 (0.47)
                                      25.2                                                13 (0.51)
                                      (0.99)
                                     1

3.2
               (0.
                  13


                                                                            60.4 (2.38)
                       )



                     2



 19.5 (0.77)
                                                              10.5 (0.41)




                                                                                              155.9 (6.14)




 46 (1.81)
                                                              36 (1.42)



                             3                   4
Figure 40: Dimensional drawing - FlexChain Booster
1                          Male connector, M8, 4-pin
2                          Fixing hole Ø 3,2 mm
3                          Cable with M12 male connector
4                          Cable with M8 female connector

SLG-2




80                           O P E R A T I N G I N S T R U C T I O N S | FlexChain                           8023047.1Q01/2025-01-29 | SICK
                                                                                                                Subject to change without notice

TECHNICAL DATA 11


   Sender                                   Receiver                Sender




                                                         6
                                                                             C



                                                         2
                                   RM   3                                    B



                 A                                                                        D            4



                                                                             4.6 (0.18)
                                                         1



                   11.7 (0.46)

                                                         5                   169 (6.65)



                                                         9 (0.35)



                                                                                          3.8 (0.15)       24.1 (0.95)
                                                       5.6 (0.22)
                                                                             1 (0.04)




                                                                         11.8 (0.47)

Figure 41: SLG-2 Flat




8023047.1Q01/2025-01-29 | SICK                                                                                           O P E R A T I N G I N S T R U C T I O N S | FlexChain   81
Subject to change without notice

11 TECHNICAL DATA

Sender                                               Receiver                 Sender




                                                                    6
                                                                                          C



                                                                    2
                                                                                          B
                                   RM            3


                   A                                                                                         D          4



                                                                                            4.6 (0.18)
                                                                   1



                     11.7 (0.46)

                                                                                            169 (6.65)
                                                                   5


                                                                                       3.8 (0.15)



                                   11.8 (0.47)
                                                                                       1 (0.04)




                                                                                            5.6 (0.22)
                                                                                                             9 (0.35)
                                                                24.1 (0.95)

Figure 42: SLG-2 Slim

Table 91: Length aluminum profile/housing length
                                                                                                         A                        D
                  SLGxxx-010xxxxxxxx                                                       77 mm                                99,2
                  SLGxxx-020xxxxxxxx                                                      178 mm                               199,2
                  SLGxxx-030xxxxxxxx                                                      276 mm                               299,2
                  SLGxxx-040xxxxxxxx                                                      376 mm                               399,2
                  SLGxxx-050xxxxxxxx                                                      475 mm                               499,2
                  SLGxxx-060xxxxxxxx                                                      576 mm                               599,2
                  SLGxxx-070xxxxxxxx                                                      676 mm                               699,2
                  SLGxxx-080xxxxxxxx                                                      776 mm                               799,2
                  SLGxxx-100xxxxxxxx                                                      975 mm                               999,2
                  SLGxxx-120xxxxxxxx                                                     1,175 mm                            1,199,2
                  SLGxxx-140xxxxxxxx                                                     1,374 mm                            1,399.2


82       O P E R A T I N G I N S T R U C T I O N S | FlexChain                                                              8023047.1Q01/2025-01-29 | SICK
                                                                                                                               Subject to change without notice

TECHNICAL DATA 11


Table 92: Distance from upper edge to last beam
                                                                                                          B
 SLG10x-xxxxxxxxxxx                                                                                 4.6 mm1)
 SLG25x-xxxxxxxxxxx                                                                                19.6 mm1)
 SLG50x-xxxxxxxxxxx                                                                                44.6 mm1)
1)   For a detection height < 700 mm, the measured value can vary by up to 1 mm from the measurements specified here.

Table 93: Length of cable
                                                                                                          C
 SLGxxx-xxxxxxAxxxx                                                                                 514 mm
 SLGxxx-xxxxxxBxxxx                                                                                1,514 mm
1)   For a detection height < 700 mm, the measured value can vary by up to 1 mm from the measurements specified here.


11.8               FlexChain Host control panel




                                   Figure 43: FlexChain Host IO-Link Standard control panel




                                   Figure 44: FlexChain Host IO-Link Advanced control panel




                                   Figure 45: FlexChain Host RS485 control panel




                                   Figure 46: FlexChain Host CANopen control panel




8023047.1Q01/2025-01-29 | SICK                                                             O P E R A T I N G I N S T R U C T I O N S | FlexChain   83
Subject to change without notice

12 ACCESSORIES


12           Accessories

                                      NOTE
                                      Accessories can be found on the online product page at:
                                      ►        www.sick.com/FlexChain




84   O P E R A T I N G I N S T R U C T I O N S | FlexChain                                      8023047.1Q01/2025-01-29 | SICK
                                                                                                   Subject to change without notice

ANNEX 13


13                 Annex
13.1               EU declaration of conformity and certificates
                                   The EU declaration of conformity and other certificates can be downloaded from the
                                   Internet at:
                                   ►    www.sick.com/FlexChain

13.2               Licenses
                                   SICK uses open-source software. This software is licensed by the rights holders using
                                   the following licenses among others: the free licenses GNU General Public License
                                   (GPL Version2, GPL Version3) and GNU Lesser General Public License (LGPL), the MIT
                                   license, zLib license, and the licenses derived from the BSD license.
                                   This program is provided for general use, but WITHOUT ANY WARRANTY OF ANY KIND.
                                   This warranty disclaimer also extends to the implicit assurance of marketability or
                                   suitability of the program for a particular purpose.
                                   More details can be found in the GNU General Public License. For complete license
                                   texts, see www.sick.com/licensetexts. Printed copies of the license texts are also
                                   available on request.




8023047.1Q01/2025-01-29 | SICK                                                      O P E R A T I N G I N S T R U C T I O N S | FlexChain   85
Subject to change without notice

8023047.1Q01/2025-01-29/en
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