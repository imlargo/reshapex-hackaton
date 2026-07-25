OPERATING INSTRUCTIONS



nanoScan3 I/O
Safety laser scanners

Described product
                    nanoScan3 I/O

                    Manufacturer
                    SICK AG
                    Erwin-Sick-Str. 1
                    79183 Waldkirch
                    Germany

                    Legal information
                    This work is protected by copyright. Any rights derived from the copyright shall be
                    reserved for SICK AG. Reproduction of this document or parts of this document is
                    only permissible within the limits of the legal determination of Copyright Law. Any mod-
                    ification, abridgment or translation of this document is prohibited without the express
                    written permission of SICK AG.
                    The trademarks stated in this document are the property of their respective owner.
                    © SICK AG. All rights reserved.

                    Original document
                    This document is an original document of SICK AG.




2   nanoScan3 I/O                                                                    8024596/1W27/2026-05-26 | SICK
                                                                                SUBJECT TO CHANGE WITHOUT NOTICE

CONTENTS

Contents
                              1    About this document..............................................................................                                       8
                                   1.1      Scope.......................................................................................................................   8
                                   1.2      Target groups of these operating instructions.............................................                                     8
                                   1.3      Further information...............................................................................................             8
                                   1.4      Related applicable documents.........................................................................                           9
                                   1.5      Symbols and document conventions.............................................................                                   9

                              2    Safety information...................................................................................                                   10
                                   2.1      General safety notes............................................................................................               10
                                   2.2      Intended use..........................................................................................................         11
                                   2.3      Improper use..........................................................................................................         11
                                   2.4      Qualification of personnel..................................................................................                   11

                              3    Cybersecurity...........................................................................................                                12
                                   3.1      Comprehensive cybersecurity concept.........................................................                                   12
                                   3.2      Software from trustworthy sources..................................................................                            12
                                   3.3      Logging....................................................................................................................    12

                              4    Product description................................................................................                                     14
                                   4.1      Product identification via the SICK product ID.............................................                                    14
                                   4.2      Device overview....................................................................................................            14
                                   4.3      Structure and function.........................................................................................                15
                                   4.4      Product characteristics.......................................................................................                 16
                                            4.4.1             Variants.................................................................................................    16
                                            4.4.2             System plug........................................................................................          17
                                            4.4.3             Field types...........................................................................................       17
                                   4.5      Example applications..........................................................................................                 18

                              5    Project planning.......................................................................................                                 21
                                   5.1      Manufacturer of the machine............................................................................                        21
                                   5.2      Operating entity of the machine.......................................................................                         21
                                   5.3      Design......................................................................................................................   21
                                            5.3.1             Protection from interference..........................................................                       22
                                            5.3.2             Preventing unprotected areas.......................................................                          23
                                            5.3.3             Reference contour monitoring......................................................                           24
                                            5.3.4             Monitoring case switching time....................................................                           26
                                            5.3.5             Minimum distance for stationary applications..........................                                       27
                                            5.3.6             Supplement ZR for reflection-based measurement errors...                                                     28
                                            5.3.7             Hazardous area protection.............................................................                       28
                                            5.3.8             Hazardous point protection............................................................                       32
                                            5.3.9             Access protection.............................................................................               34
                                            5.3.10            Mobile hazardous area protection................................................                             36
                                   5.4      Integration in the electrical control system...................................................                                41
                                            5.4.1             Electromagnetic compatibility......................................................                          41
                                            5.4.2             Voltage supply....................................................................................           42


8024596/1W27/2026-05-26 | SICK                                                                                                                  nanoScan3 I/O              3
SUBJECT TO CHANGE WITHOUT NOTICE

CONTENTS

                                  5.4.3             USB connection.................................................................................                42
                                  5.4.4             OSSDs...................................................................................................       42
                                  5.4.5             Control inputs.....................................................................................            43
                                  5.4.6             Universal inputs, universal outputs, universal I/Os..................                                          46
                                  5.4.7             Restart interlock.................................................................................             46
                                  5.4.8             External device monitoring (EDM)................................................                               49
                         5.5      Integration into the network...............................................................................                      49
                         5.6      Testing plan............................................................................................................         49
                                  5.6.1             Planning the thorough check during commissioning and in
                                                    certain situations...............................................................................              50
                                  5.6.2             Planning the regular thorough check..........................................                                  50
                                  5.6.3             Notes on the tests.............................................................................                51

                     6   Mounting.................................................................................................... 54
                         6.1      Safety........................................................................................................................   54
                         6.2      Unpacking...............................................................................................................         54
                         6.3      Fitting the system plug........................................................................................                  54
                         6.4      Mounting the device............................................................................................                  55

                     7   Electrical installation.............................................................................. 56
                         7.1      Safety........................................................................................................................   56
                         7.2      Connecting.............................................................................................................          56
                                  7.2.1             Connecting cable with M12 plug connector, 8-pin..................                                              56
                                  7.2.2             Connecting cable with M12 plug connector, 17-pin.................                                              57
                                  7.2.3             Connecting cable with flying leads, 17-wire...............................                                     58
                                  7.2.4             Network connection.........................................................................                    60

                     8   Configuration............................................................................................                                 61
                         8.1      Delivery state.........................................................................................................          61
                         8.2      Safety Designer configuration software.........................................................                                  61
                                  8.2.1             Installing Safety Designer...............................................................                      61
                                  8.2.2             Projects................................................................................................       61
                                  8.2.3             User interface.....................................................................................            62
                                  8.2.4             User groups.........................................................................................           62
                                  8.2.5             Settings................................................................................................       64
                                  8.2.6             Configuration......................................................................................            64
                                  8.2.7             Networking..........................................................................................           66
                         8.3      Overview..................................................................................................................       67
                         8.4      Hardware.................................................................................................................        68
                         8.5      Network settings...................................................................................................              69
                                  8.5.1             Ethernet................................................................................................       69
                         8.6      Time synchronization...........................................................................................                  69
                         8.7      Reading configuration.........................................................................................                   69
                         8.8      Identification...........................................................................................................        70
                         8.9      Application..............................................................................................................        70
                         8.10     Monitoring plane...................................................................................................              71



4    nanoScan3 I/O                                                                                                         8024596/1W27/2026-05-26 | SICK
                                                                                                                      SUBJECT TO CHANGE WITHOUT NOTICE

CONTENTS

                                   8.11    Contour as Reference field................................................................................                       73
                                   8.12    Fields........................................................................................................................    75
                                           8.12.1            Drawing in points that cannot be monitored.............................                                        78
                                           8.12.2            Enable propose field........................................................................                    79
                                           8.12.3            Object transformation......................................................................                     79
                                           8.12.4            Editing fields using coordinates....................................................                           80
                                           8.12.5            Background image............................................................................                    81
                                           8.12.6            Device Settings..................................................................................               81
                                           8.12.7            Defining global geometry................................................................                       82
                                           8.12.8            Grid Settings.......................................................................................           82
                                           8.12.9            Creating field set templates...........................................................                        82
                                           8.12.10           Importing and exporting field sets and fields............................                                      83
                                           8.12.11           Virtual group........................................................................................          83
                                   8.13    Inputs and outputs, local....................................................................................                    84
                                           8.13.1            Outputs.................................................................................................       85
                                           8.13.2            Inputs....................................................................................................     85
                                           8.13.3            Further settings for some signals.................................................                             86
                                   8.14    Monitoring cases..................................................................................................               88
                                           8.14.1            Settings for monitoring case tables.............................................                               88
                                           8.14.2            Several monitoring case tables.....................................................                            90
                                           8.14.3            Settings for monitoring cases........................................................                          90
                                           8.14.4            Input condition...................................................................................             90
                                           8.14.5            Cut-off paths.......................................................................................            91
                                           8.14.6            Assigning field sets...........................................................................                 91
                                           8.14.7            Assigning a defined cut-off behavior...........................................                                92
                                   8.15    Simulation...............................................................................................................        93
                                   8.16    Data output.............................................................................................................         94
                                   8.17    Transferring a configuration...............................................................................                      95
                                           8.17.1            Verify configuration...........................................................................                96
                                           8.17.2            Transferring a verified configuration............................................                              96
                                   8.18    Starting and stopping safety function.............................................................                                97
                                   8.19    Report.......................................................................................................................    98
                                   8.20    Service.....................................................................................................................     99
                                           8.20.1            Restart device.....................................................................................            99
                                           8.20.2            Resetting to factory settings..........................................................                        99
                                           8.20.3            Managing passwords.......................................................................                      100
                                           8.20.4            Access management.......................................................................                       100
                                           8.20.5            Optics cover calibration...................................................................                    101
                                           8.20.6            Compare configuration.................................................................... 102
                                           8.20.7            Import / Export...................................................................................             103

                              9    Commissioning........................................................................................ 104
                                   9.1     Safety........................................................................................................................ 104
                                   9.2     Overview.................................................................................................................. 104
                                   9.3     Alignment................................................................................................................ 104



8024596/1W27/2026-05-26 | SICK                                                                                                                  nanoScan3 I/O                5
SUBJECT TO CHANGE WITHOUT NOTICE

CONTENTS

                          9.4       Switching on........................................................................................................... 104
                          9.5       Check during commissioning and modifications........................................ 105

                     10   Operation................................................................................................... 106
                          10.1      Safety........................................................................................................................ 106
                          10.2      Regular thorough check.....................................................................................                      106
                          10.3      Status indicators...................................................................................................             106
                          10.4      Status indicator with the display....................................................................... 107

                     11   Maintenance.............................................................................................                                   111
                          11.1      Safety........................................................................................................................   111
                          11.2      Regular cleaning...................................................................................................              111
                          11.3      Replacing the optics cover................................................................................                       112
                          11.4      Replacing the safety laser scanner.................................................................                              112
                                    11.4.1            Replacing the safety laser scanner without system plug......                                                   112
                                    11.4.2            Replacing the safety laser scanner with system plug.............                                               113
                          11.5      Replacing the system plug.................................................................................                       114
                          11.6      Regular thorough check.....................................................................................                      114
                          11.7      Updating firmware................................................................................................                114

                     12   Troubleshooting....................................................................................... 118
                          12.1      Safety........................................................................................................................   118
                          12.2      Detailed diagnostics using the display...........................................................                                118
                          12.3      Error indication on the display..........................................................................                        119
                          12.4      Diagnostics using Safety Designer..................................................................                              121
                                    12.4.1            Data recorder...................................................................................... 122
                                    12.4.2            Event history.......................................................................................           123
                                    12.4.3            Message history................................................................................. 125
                                    12.4.4            Contamination measurement........................................................                              126

                     13   Decommissioning................................................................................... 127
                          13.1      Disposal...................................................................................................................      127

                     14   Technical data.......................................................................................... 128
                          14.1      Version numbers and range of functions.......................................................                                    128
                          14.2      Data sheet...............................................................................................................        129
                          14.3      Response times..................................................................................................... 133
                          14.4      Course of the OSSD test over time..................................................................                              134
                          14.5      Sensing range........................................................................................................            135
                          14.6      Scan plane..............................................................................................................         137
                          14.7      Light spot size........................................................................................................          137
                          14.8      Measurement data details.................................................................................                        138
                          14.9      Network services and protocols.......................................................................                            138
                          14.10 Dimensional drawings.........................................................................................                        139

                     15   Ordering information.............................................................................. 141
                          15.1      Scope of delivery..................................................................................................              141



6    nanoScan3 I/O                                                                                                           8024596/1W27/2026-05-26 | SICK
                                                                                                                        SUBJECT TO CHANGE WITHOUT NOTICE

CONTENTS

                                   15.2     Ordering information............................................................................................      141

                              16   Spare parts................................................................................................ 142
                                   16.1     Additional spare parts.........................................................................................      142

                              17   Accessories.............................................................................................. 143
                                   17.1     System plug............................................................................................................ 143
                                   17.2     Additional accessories........................................................................................ 143

                              18   Glossary..................................................................................................... 144

                              19   Annex.......................................................................................................... 149
                                   19.1     Conformities and certificates............................................................................            149
                                   19.2     Note on standards................................................................................................    149
                                   19.3     Open source software.........................................................................................        149
                                   19.4     Checklist for initial commissioning and commissioning...........................                                     149

                              20   List of figures............................................................................................ 151

                              21   List of tables.............................................................................................. 153




8024596/1W27/2026-05-26 | SICK                                                                                                         nanoScan3 I/O                7
SUBJECT TO CHANGE WITHOUT NOTICE

1 ABOUT THIS DOCUMENT

1           About this document
1.1         Scope
                      Product
                      This document applies to the following products:
                      O    Product code: nanoScan3 I/O
                      O    “Operating instructions” type label entry: 8024594

                      Document identification
                      Document part number:
                      O   This document: 8024596
                      O    Available language versions of this document: 8024594
                      You can find the current version of all documents at www.sick.com.


1.2         Target groups of these operating instructions
                      Some sections of these operating instructions are intended for certain target groups.
                      However, the entire operating instructions are relevant for intended use of the product.
                      Table 1: Target groups and selected sections of these operating instructions
                      Target group                                      Sections of these operating instructions
                      Project developers (planners, developers,         "Project planning", page 21
                      designers)                                        "Configuration", page 61
                                                                        "Technical data", page 128
                                                                        "Accessories", page 143
                      Installers                                        "Mounting", page 54
                      Electricians                                      "Electrical installation", page 56
                      Safety experts (such as CE authorized repre-      "Project planning", page 21
                      sentatives, compliance officers, people who       "Configuration", page 61
                      test and approve the application)                 "Commissioning", page 104
                                                                        "Technical data", page 128
                                                                        "Checklist for initial commissioning and com-
                                                                        missioning", page 149
                      Operators                                         "Operation", page 106
                                                                        "Troubleshooting", page 118
                      Maintenance personnel                             "Maintenance", page 111
                                                                        "Troubleshooting", page 118


1.3         Further information
                      www.sick.com
                      The following information is available via the Internet:
                      O    Data sheets and application examples
                      O    CAD files and dimensional drawings
                      O    Certificates (such as the EU declaration of conformity)
                      O    Guide for Safe Machinery. Six steps to a safe machine
                      O    Safety Designer (software for configuring safety solutions made by SICK AG)




8     nanoScan3 I/O                                                                            8024596/1W27/2026-05-26 | SICK
                                                                                          SUBJECT TO CHANGE WITHOUT NOTICE

ABOUT THIS DOCUMENT 1

1.4            Related applicable documents
                              Related applicable documents from SICK
                               Document                       Title                           Source
                               Technical information          Cybersecurity – safety laser    www.sick.com/8029467
                                                              scanner


1.5            Symbols and document conventions
                              The following symbols and conventions are used in this document:

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

                              →       The arrow denotes instructions to action.

                              1.      The sequence of instructions for action is numbered.
                              2.      Follow the order in which the numbered instructions are given.
                              m       The check mark denotes the result of an instruction.

                              LED symbols
                              These symbols indicate the status of an LED:
                                   o The LED is off.
                                   Ö The LED is flashing.
                                   O The LED is illuminated continuously.




8024596/1W27/2026-05-26 | SICK                                                                         nanoScan3 I/O   9
SUBJECT TO CHANGE WITHOUT NOTICE

2 SAFETY INFORMATION

2           Safety information
2.1         General safety notes
                      Integrating the product

                      DANGER
                      The product can not offer the expected protection if it is integrated incorrectly.

                      →    Plan the integration of the product in accordance with the machine requirements
                           (project planning).
                      →    Implement the integration of the product in accordance with the project planning.


                      Laser notes

                      CAUTION
                      Optical radiation: Class 1 Laser Product
                      Caution - if any operating or calibrating equipment other than those specified here are
                      used or other methods are employed, this can lead to dangerous exposure to radiation.

                      →    Use only the tools and auxiliary equipment specified in this documentation.
                      →    Only carry out the procedures specified in this documentation.
                      →    Do not open the housing unless carrying out the mounting and maintenance oper-
                           ations provided in this documentation.




                                                LASER
                                                  1

                      Figure 1: Laser class 1


                      This device complies with the following standards:
                      O    EN 60825-1:2014 + A11:2021
                      O    IEC 60825-1:2014
                      O    21 CFR 1040.10 and 1040.11, except compliance with IEC 60825-1:2014, as descri-
                           bed in Laser Notice No. 56 dated 08.05.2019
                      The laser is eye-safe.
                      The laser marking is located on the underside of the safety laser scanner.

                      Mounting and electrical installation

                      DANGER
                      Death or severe injury due to electrical voltage and/or an unexpected startup of the
                      machine

                      →    Make sure that the machine is and remains in a de-energized state during mount-
                           ing and electrical installation.
                      →    Make sure that the dangerous state of the machine is and remains switched off.




10    nanoScan3 I/O                                                                      8024596/1W27/2026-05-26 | SICK
                                                                                    SUBJECT TO CHANGE WITHOUT NOTICE

SAFETY INFORMATION 2

                              Repairs and modifications

                              DANGER
                              Improper work on the product
                              A modified product may not offer the expected protection if it is integrated incorrectly.

                              →    Apart from the procedures described in this document, do not repair, open, manip-
                                   ulate or otherwise modify the product.


2.2            Intended use
                              The safety laser scanner is an electro-sensitive protective device (ESPE) and is suitable
                              for the following applications:
                              O    Hazardous area protection
                              O    Hazardous point protection
                              O    Access protection
                              O    Mobile hazardous area protection (protection of automated guided vehicles)
                              The product may be used in safety functions.
                              The safety laser scanner must only be used within the limits of the prescribed and
                              specified technical data and operating conditions at all times.
                              Incorrect use, improper modification or manipulation of the safety laser scanner will
                              invalidate any warranty from SICK; in addition, any responsibility and liability of SICK for
                              damage and secondary damage caused by this is excluded.


2.3            Improper use
                              Impermissible use
                              O   As a physical guard. The product works as an indirect protective measure and
                                  cannot provide protection from parts thrown from the application nor from emitted
                                  radiation.
                              O    Access control or authorization
                              O    Detection of transparent items
                              Impermissible ambient conditions
                              O   Outdoors
                              O    Underwater
                              O    In explosion-hazardous areas

2.4            Qualification of personnel
                              Any work on the product may only be carried out by personnel qualified and authorized
                              to do so.
                              Qualified personnel are able to perform tasks assigned to them and can independently
                              recognize and avoid any potential hazards. This requires, for example:
                              O    technical training
                              O    experience
                              O    knowledge of the applicable regulations and standards




8024596/1W27/2026-05-26 | SICK                                                                         nanoScan3 I/O      11
SUBJECT TO CHANGE WITHOUT NOTICE

3 CYBERSECURITY

3           Cybersecurity
3.1         Comprehensive cybersecurity concept
                      Overview
                      To protect against cybersecurity threats, the operator must have a comprehensive
                      cybersecurity concept, which must be continuously monitored and maintained. A suita-
                      ble concept consists of organizational, technical, procedural, electronic, and physical
                      levels of defense and considers suitable measures for different types of risks. The
                      measures implemented in this product can only support protection against cybersecur-
                      ity threats if the product is used as part of such a concept.
                      You will find further information at www.sick.com/psirt, e.g.:
                      O   General information on cybersecurity
                      O    Contact option for reporting vulnerabilities
                      O    Information on known vulnerabilities (security advisories)

                      Further topics
                      O    "Related applicable documents", page 9
                      O    "Improper use", page 11
                      O    "Software from trustworthy sources", page 12
                      O    "Logging", page 12
                      O    "Product identification via the SICK product ID", page 14
                      O    "User groups", page 62
                      O    "Managing passwords", page 100
                      O    "Access management", page 100
                      O    "Resetting to factory settings", page 99
                      O    "Updating firmware", page 114
                      O    "Data sheet", page 129
                      O    "Network services and protocols", page 138

3.2         Software from trustworthy sources
                      When installing software (e.g. firmware, application software), the operating entity must
                      ensure the relevant sources are known and trustworthy.
                      For information on verifying downloads from the SICK website, visit www.sick.com/ver-
                      ify-downloads.


3.3         Logging
                      Logging
                      The product captures and stores events in the following areas:
                      O   Message history
                           Events such as errors, warnings and information are stored in the message history.
                           The message history stores up to 1,000 events.
                           When the history is full, the oldest entries are automatically overwritten by new
                           entries.
                           This history cannot be deactivated.
                      O    Event history
                           The safety laser scanner stores data on important events. The event history dis-
                           plays information about the most recently stored events.
                           The event history is deleted each time the device is restarted and when transfer-
                           ring a configuration.


12    nanoScan3 I/O                                                                     8024596/1W27/2026-05-26 | SICK
                                                                                   SUBJECT TO CHANGE WITHOUT NOTICE

CYBERSECURITY 3

                                   The event history can be deactivated via an input signal.
                              O    Configuration history
                                   The configuration history contains the time stamps and checksums of the most
                                   recent configurations transferred to the device. Up to 5 configuration processes
                                   are stored.
                                   When the history is full, the oldest entries are automatically overwritten by new
                                   entries.
                                   The configuration history is contained in the Safety Designer report.
                                   This history cannot be deactivated.
                              O    Firmware history
                                   The firmware history contains the time stamps and version information of the
                                   firmware updates performed. Up to 32 installation processes are stored.
                                   When the history is full, the oldest entries are automatically overwritten by new
                                   entries.
                                   This history cannot be deactivated.

                              Further topics
                              O    "Message history", page 125
                              O    "Event history", page 123
                              O    "Inputs", page 85
                              O    "Report", page 98




8024596/1W27/2026-05-26 | SICK                                                                       nanoScan3 I/O     13
SUBJECT TO CHANGE WITHOUT NOTICE

4 PRODUCT DESCRIPTION

4           Product description
4.1         Product identification via the SICK product ID
                      SICK product ID
                      The SICK product ID uniquely identifies the product. It also serves as the address of the
                      web page with information on the product.
                      The SICK product ID comprises the host name pid.sick.com, the part number (P/N), and
                      the serial number (S/N), each separated by a forward slash.
                      For newer products, the SICK product ID is displayed as text and QR code on the type
                      label and/or on the packaging.




                      Figure 2: SICK product ID


4.2         Device overview
                      Overview

                                      1       2   3

                                                             4
                          3                                 3
                      2                                        2
                          1                                  1

                                                                                                            9
                          8
                                                       5
                                  7
                                              6
                      Figure 3: Device overview

                      1        LED ON status
                      2        LED OFF status
                      3        LED restart interlock/warning field
                      4        Optics cover
                      5        USB connection
                      6        Display
                      7        Network LED
                      8        Pushbutton
                      9        System plug


                      Complementary information
                      Position and direction information in this document:
                      O    The top is the side of the device on which the optics cover is located.
                      O       The bottom is the side of the device opposite the optics cover.




14    nanoScan3 I/O                                                                       8024596/1W27/2026-05-26 | SICK
                                                                                     SUBJECT TO CHANGE WITHOUT NOTICE

PRODUCT DESCRIPTION 4

                              O    The front is the side of the device on which the display is located. The 90° angle of
                                   the sector of a circle scanned by the device points in this direction.
                              O    The back is the side of the device opposite the display. The sector of a circle not
                                   scanned by the device lies in this direction.

                              Further topics
                              O    "Connecting", page 56
                              O    "Status indicators", page 106

4.3            Structure and function
                              The safety laser scanner is an electro-sensitive protective device (ESPE) which scans
                              its surroundings two-dimensionally using infrared laser beams.
                              The safety laser scanner forms a protective field using the invisible laser beams. This
                              protective field protects the hazardous area and enables hazardous point protection,
                              access protection or hazardous area protection. As soon as an object is situated in the
                              protective field, the safety laser scanner signals the detection by means of a signal
                              change at the safety output. The machine or its control must safely analyze the signals
                              (for example using a safe control or safety relays) and stop the dangerous state.
                              The safety laser scanner operates on the principle of optical time-of-flight measure-
                              ment. It emits light pulses in regular, very short intervals. If the light strikes an object,
                              it is reflected. The safety laser scanner receives the reflected light. The safety laser
                              scanner calculates the distance to the object based on the time interval between the
                              moment of transmission and moment of receipt (∆t).




                                                                                                     

                                                                 



                                                                                                ∆t
                                                                                  
                                                                                                                  t
                                                                                  
                                                                                                                  t

                              Figure 4: Principle of time-of-flight measurement

                              1      Transmitted light pulse
                              2      Reflected light pulse


                              A rotating mirror is situated in the safety laser scanner. The mirror deflects the light
                              pulses so that they scan a fan-shaped area.




8024596/1W27/2026-05-26 | SICK                                                                           nanoScan3 I/O        15
SUBJECT TO CHANGE WITHOUT NOTICE

4 PRODUCT DESCRIPTION


                                                                                     227,5°


                                                 -47,5°




                                                0°




                                                                                                     90°




                                    




                         Figure 5: Light pulses scan an area

                         1      Angular resolution: the angular distance (in degrees) between 2 distance measurements


                         Scan cycle time and resolution
                         The time that the mirror requires for one rotation is called the scan cycle time. The
                         number of light pulses per unit of time is constant. The scan cycle time and the number
                         of light pulses per unit of time determine the angular resolution. The scanning range
                         for a given object resolution depends on the angular resolution. The object resolution
                         indicates the minimum size that an object must be to allow it to be detected safely. The
                         scan cycle time also influences the response time.
                         The resolution in protective fields can be set to various values according to the
                         intended purpose.

                         Geometry of the scan plane
                         The laser beams emitted cover a sector of a circle, so an object can be detected in an
                         area of up to 275°.
                         The sector of a circle covered ranges from –47.5° to 227.5°, where 90° denotes the axis
                         of the safety laser scanner from the back to the front. When viewing the safety laser
                         scanner from above, the direction of rotation of the mirror and the deflected light pulses
                         is counterclockwise, see figure 5, page 16.


4.4           Product characteristics

4.4.1         Variants
                         The device is available in various variants. You will find an overview of important distin-
                         guishing features of the variants in the following.

                         Performance package
                         The Core and Pro performance packages feature a number of configurable fields and a
                         number of safety switching functions.
                         O    nanoScan3 core I/O: 8 fields, 1 OSSD pair
                         O    nanoScan3 Pro I/O: 128 fields, 2 OSSD pairs



16      nanoScan3 I/O                                                                         8024596/1W27/2026-05-26 | SICK
                                                                                         SUBJECT TO CHANGE WITHOUT NOTICE

PRODUCT DESCRIPTION 4

                               Integration into the controller
                               The device communicates with the machine controller as follows:
                               O   I/O: local inputs and outputs (incl. OSSDs)

                               Connection type
                               Some variants are available with different connection types:
                               O  Connecting cable with M12 round connector
                               O     Connecting cable with flying leads

                               Ethernet connection for configuration and data output
                               The device is available with or without Ethernet connection for configuration, diagnos-
                               tics and data output.

                               Further topics
                               O     "Ordering information", page 141

4.4.2          System plug
                               The safety laser scanner requires a system plug.
                               The safety laser scanner’s configuration memory is integrated in the system plug. The
                               system plug and all connecting cables can remain at the installation site when the
                               safety laser scanner is replaced. The system plug is detached from the defective safety
                               laser scanner and connected to the new safety laser scanner. The new safety laser
                               scanner reads the configuration from the configuration memory when switched on.

4.4.3          Field types
                               During operation, the safety laser scanner uses its laser beams to continuously check
                               whether people or objects are present in one or more areas. The areas to be checked
                               are called fields. A distinction is made between the following field types, depending on
                               the application type:
                               O     Protective field
                               O     Contour as Reference field
                               O     Contour detection field
                               O     Warning field
Table 2: Field types and their function
                           Protective field          Contour as Reference   Contour detection    Warning field
                                                     field                  field
Safe switch off (accord-   Yes (PL d)                Yes (PL d)             Yes (PL d)           No
ing to ISO 13849-1)
Maximum scanning          3.0 m                      3.0 m                  3.0 m                10 m
range of the safety laser
scanner
Purpose                    Detection and protec-     Tamper protection      Contour monitoring   Functional use (not
                           tion of people                                                        safety application)




8024596/1W27/2026-05-26 | SICK                                                                        nanoScan3 I/O    17
SUBJECT TO CHANGE WITHOUT NOTICE

4 PRODUCT DESCRIPTION

                        Protective field            Contour as Reference      Contour detection          Warning field
                                                    field                     field
Description             The protective field        The contour as refer-     The contour detection      The warning field mon-
                        is the area in which        ence field monitors a     field monitors a con-      itors larger areas than
                        the test object speci-      contour of the environ-   tour of the environ-       the protective field.
                        fied by the manu-           ment. The safety laser    ment. The electro-sen-     Simple switching func-
                        facturer is detected        scanner switches all      sitive protective device   tions can be triggered
                        by the electro-sensi-       safety outputs to the     switches the associated    with the warning field,
                        tive protective equip-      OFF state if a con-       safety outputs to the      e.g. a warning light
                        ment (ESPE). As soon        tour does not match       OFF state if a contour     or an acoustic signal
                        as the electro-sensi-       the set parameters,       does not correspond to     can be triggered if
                        tive protective device      because, for example,     the set specifications,    a person approaches,
                        detects an object in        the mounting of the       e.g. because a door or     even before the person
                        the protective field, it    safety laser scanner      flap is open.              enters the protective
                        switches the associated     has been changed.                                    field.
                        safety outputs to the
                        OFF state. This signal
                        can be passed to con-
                        trollers resulting in the
                        dangerous state com-
                        ing to an end, e.g. to
                        stop the machine or the
                        vehicle.


4.5           Example applications
                           Hazardous area protection
                           In hazardous area protection, people are detected if they stay in a defined area.
                           This type of protective device is suitable for machines, where it is possible to see a
                           hazardous area completely from the reset pushbutton. When the hazardous area is
                           entered, a stop signal is triggered and starting is prevented.




                           Figure 6: Hazardous area protection: detection of the presence of a person in the hazardous area


                           Hazardous point protection
                           In hazardous point protection, the approach is detected very close to the hazardous
                           point.




18      nanoScan3 I/O                                                                                  8024596/1W27/2026-05-26 | SICK
                                                                                                  SUBJECT TO CHANGE WITHOUT NOTICE

PRODUCT DESCRIPTION 4

                              The advantage of this type of protective device is that it is possible to have a short
                              minimum distance and the operator can work more ergonomically.




                              Figure 7: Hazardous point protection: Hand detection


                              Access protection
                              In access protection, people are detected if their whole body passes through the pro-
                              tective field.
                              This type of protective device is used for the protection of access to hazardous areas.
                              A stop signal is initiated if the hazardous area is entered. A person standing behind the
                              protective device will not be detected by the ESPE.




                              Figure 8: Access protection: detection of a person when accessing a hazardous area




8024596/1W27/2026-05-26 | SICK                                                                           nanoScan3 I/O   19
SUBJECT TO CHANGE WITHOUT NOTICE

4 PRODUCT DESCRIPTION

                     Mobile hazardous area protection
                     Mobile hazardous area protection is suitable for AGVs (automated guided vehicles) and
                     forklift trucks to protect people when vehicles are moving or docking at a fixed station.
                     The safety laser scanner monitors the area in the direction of travel and stops the
                     vehicle as soon as an object is located in the protective field.




                     Figure 9: Mobile hazardous area protection: detection of a person when a vehicle approaches




20   nanoScan3 I/O                                                                         8024596/1W27/2026-05-26 | SICK
                                                                                      SUBJECT TO CHANGE WITHOUT NOTICE

PROJECT PLANNING 5

5              Project planning
5.1            Manufacturer of the machine
                              The manufacturer of the machinery must carry out a risk assessment and apply appro-
                              priate protective measures. Further protective measures may be required in addition to
                              the product.
                              The product must not be tampered with or changed, except for the procedures descri-
                              bed in this document.
                              The product must only be repaired by the manufacturer of the product or by someone
                              authorized by the manufacturer. Improper repair can result in the product not providing
                              the expected protection.


5.2            Operating entity of the machine
                              Changes to the electrical integration of the product in the machine controller and
                              changes to the mechanical mounting of the product necessitate a new risk assessment.
                              The results of this risk assessment may require the entity operating the machine to
                              meet the obligations of a manufacturer.
                              After each change to the configuration, it is necessary to check whether the protective
                              measure provides the necessary protection. The person making the change is respon-
                              sible for ensuring that the protection measure provides the necessary protection.
                              The product must not be tampered with or changed, except for the procedures descri-
                              bed in this document.
                              The product must only be repaired by the manufacturer of the product or by someone
                              authorized by the manufacturer. Improper repair can result in the product not providing
                              the expected protection.


5.3            Design
                              Important information

                              DANGER
                              Hazard due to lack of effectiveness of the protective device
                              Persons or parts of the body to be protected may not be recognized or not recognized
                              in time in case of non-observance.

                              →    Make sure that there are no mirrors or other highly reflective objects in the protec-
                                   tive field of the safety laser scanner.
                              →    Make sure that there is no smoke in the protective field of the safety laser scanner.
                              →    Prevent interference in the optical beam path. If, for example, the device is instal-
                                   led in a paneling, the viewing slit must be sufficiently large.
                              →    Do not use an additional front screen.
                              →    Ensure that there are no small objects (e.g. cables) in the protective field of the
                                   safety laser scanner, even if they do not trigger an object detection.


                              NOTE
                              If you are not integrating the product in accordance with ISO 13855:2010, you must carry
                              out an individual impact analysis.




8024596/1W27/2026-05-26 | SICK                                                                       nanoScan3 I/O    21
SUBJECT TO CHANGE WITHOUT NOTICE

5 PROJECT PLANNING

                          Prerequisites
                          O    No obstacles interfere with the view in the protective field of the safety laser
                               scanner. Where there are unavoidable obstacles, additional protective measures
                               are applied.
                          O    If people can stay between the protective device and the hazardous point without
                               being detected, additional protective measures (e.g. restart interlock) are applied.
                          O    Reaching under, over and around, crawling beneath and stepping over the safety
                               laser scanner, as well as moving it, are prevented.




                          Figure 10: Prevent crawling beneath




                          Figure 11: Prevent stepping over


                          Complementary information
                          Certain optical and electromagnetic ambient conditions can affect the safety laser
                          scanner and thus reduce the availability of the machine.
                          Examples:
                          O   Condensation on the optics cover
                          O    Strong electrical fields (e.g. welding cables or induction cables)

                          Further topics
                          O    "Mounting", page 54
                          O    "Dimensional drawings", page 139

5.3.1         Protection from interference
                          Influence by laser
                          Laser sources located close to the machine can influence the safety laser scanner and
                          thus reduce the availability of the machine.

                          Measures to increase availability:
                          →  Avoid laser sources in the scan plane.
                          →  Set multiple sampling to the highest value permitted in your application, taking the
                             minimum distances into account, see "Multiple sampling", page 72.




22      nanoScan3 I/O                                                                        8024596/1W27/2026-05-26 | SICK
                                                                                        SUBJECT TO CHANGE WITHOUT NOTICE

PROJECT PLANNING 5

                              Influence by strong light sources
                              Strong external light sources in the scan plane can influence the safety laser scanner
                              and thus reduce the availability of the machine.

                              Measures to increase availability:
                              →  Avoid external light sources in the scan plane.
                              →  Avoid direct sunlight in the scan plane.
                              →  Do not position halogen lights, infrared light sources or stroboscopes directly on
                                 the scan plane.

                              Mutual interference from safety laser scanners
                              Due to the safeHDDM® scanning technology, mutual interference of multiple safety
                              laser scanners is unlikely. If many safety laser scanners are operated at the same
                              level in a stationary application, they may nevertheless interfere with one another. We
                              recommend selecting a suitable mounting method to avoid mutual interference.

                              Suitable mounting methods:
                              →    Offset mounting so that the scan planes are on different planes
                              →    Slightly inclined, tilted mounting, so that the scan planes intersect one another

5.3.2          Preventing unprotected areas
                              Overview
                              The safety laser scanner must be mounted in such a way that people cannot enter
                              unsecured areas without being detected.

                              Undetected areas
                              There may be areas behind the safety laser scanner which cannot be detected by the
                              safety laser scanner. The undetected areas become larger if the safety laser scanner is
                              mounted using a mounting kit.




                                         
                                                                              




                                   

                                                                                         




                              Figure 12: Unsecured areas

                              1        Length of the undetected area
                              2        Width of the undetected area




8024596/1W27/2026-05-26 | SICK                                                                       nanoScan3 I/O     23
SUBJECT TO CHANGE WITHOUT NOTICE

5 PROJECT PLANNING

                         Remedial measures:
                         O  Mounting of deflector plates to protect the undetected areas
                         O    Mounting the safety laser scanner in the machine or vehicle paneling

                         Near range
                         In close proximity (50 mm-wide area in front of the optics cover), the detection capabil-
                         ity of the safety laser scanner may be restricted. If required, this area must be secured
                         using an undercut or frame, for example.

5.3.3         Reference contour monitoring
                         Vertical operation
                         National and international standards require or recommend that a reference contour is
                         monitored if the angle between access direction and scan plane exceeds 30°. With the
                         reference contour field, the safety laser scanner monitors the distance to a contour of
                         the environment (e.g. a wall) in order to detect inadvertent adjustment or manipulation.

                         Configuring the reference contour field during vertical operation
                         O    In many cases, it makes sense to use the floor and lateral vertical passage boun-
                              daries (e.g. door frames) as a reference contour.
                         O    The resolution of the reference contour field specifies how large a gap in the con-
                              tour or an object in the reference contour field must be for the reference contour
                              field to detect the gap or object in any case. Smaller gaps or objects can also
                              trigger detection in some cases.
                         O    The length of the monitored contour must be greater than the set resolution of the
                              reference contour field.
                         O    The reference contour field has an adjustable tolerance band. If the safety laser
                              scanner does not detect the reference contour within the tolerance band, all safety
                              outputs switch to the OFF state. In Safety Designer, you can define the tolerance
                              band around the reference contour in both directions (near and far).
                              o    For high availability, setting both the positive tolerance band (far) and the
                                   negative tolerance band (near) to the TZ value is recommended. (TZ = toler-
                                   ance zone of the safety laser scanner, see "Data sheet", page 129.)
                              o    The tolerance band must not be too wide. The reference contour field must
                                   detect a deviation from the reference contour before access to the hazard-
                                   ous point occurs next to the protective field. Deviations may occur due to
                                   changes in position or orientation.
                              o    If the reference contour represents the edge of the protected opening, the
                                   sum of the negative and positive tolerance bands must not be greater than
                                   the resolution of the protective field.
                              o    If the reference contour does not represent the edge of the protected open-
                                   ing, the sum of the negative and positive tolerance bands must not be greater
                                   than the projection.
                         O    You can define a number of contours in the reference contour field and therefore
                              monitor various areas in the environment.

                         Protective field and reference contour field for hazardous point protection
                         The protective field must be larger than the protected opening. The required overrun (o)
                         is calculated using the following formula:
                         o ≥ (2 × TZ) – d
                         Where:
                         O  o = overrun of the protective field over the opening
                         O    TZ = tolerance zone of the safety laser scanner, see "Data sheet", page 129
                         O    d = set resolution


24      nanoScan3 I/O                                                                      8024596/1W27/2026-05-26 | SICK
                                                                                      SUBJECT TO CHANGE WITHOUT NOTICE

PROJECT PLANNING 5


                                                             3

                                                 2




                                                                                                          1




                              Figure 13: Overrun of the protective field in front of an opening

                              1      Tolerance band of the reference contour field
                              2      Distance of the protective field from the contour, to ensure availability
                              3      o = overrun of the protective field over the opening


                              Protective field and reference contour field for access protection
                              O    If the reference contour represents the edge of the protected opening, its distance
                                   from the protective field must not exceed 100 mm. A distance equal to the TZ
                                   value is recommended for high availability and sufficient protection. (TZ = toler-
                                   ance zone of the safety laser scanner, see "Data sheet", page 129.)
                              O    If the reference contour does not represent the edge of the protected opening, the
                                   protective field must be larger than the protected opening. The required overrun
                                   (o) is calculated using the same formula as for hazardous point protection.




8024596/1W27/2026-05-26 | SICK                                                                                   nanoScan3 I/O   25
SUBJECT TO CHANGE WITHOUT NOTICE

5 PROJECT PLANNING




                                                             1                            2
                          Figure 14: Tolerance band of the contour as reference field (protective field within the protected
                          opening, edge of the protected opening = reference contour)

                          1        Tolerance band of the reference contour field
                          2        Distance of the protective field from the reference contour, to ensure availability


5.3.4         Monitoring case switching time
                          Overview
                          If you switch between monitoring cases, you must specify the time at which the switch-
                          over takes place.
                          When determining the time, you must consider the following points, among others:
                          O  At the time of switchover, one person can already be in the newly activated protec-
                             tive field. The new protective field must therefore be active in good time so that
                             the device detects a person in the newly activated protective field before a hazard
                             arises there.
                          O    In some cases, the process of switching between monitoring cases takes so long
                               that the new monitoring case is not available inside the response time provided.
                               This means that it may not be possible to detect a person in the protective field in
                               time. In cases like this, you must start switching between monitoring cases earlier.
                               The following parameters influence the duration of the process:
                               o    Set input delay
                               o      Processing time for the chosen input
                          O    In addition to the parameters considered below, the switching signal’s time-of-
                               flight up to the device must also be taken into account. Depending on the commu-
                               nication protocol, these include the network cycle time and the processing time of
                               a controller, for example.

                          Procedure

                          1.   Calculate how long it takes to switch between monitoring cases:
                               tCSR = tID + tI
                               where:
                               o      tCSR = time required for switching between monitoring cases in milliseconds
                                      (ms)
                               o      tID = input delay for the control inputs in milliseconds (ms)


26      nanoScan3 I/O                                                                                 8024596/1W27/2026-05-26 | SICK
                                                                                                 SUBJECT TO CHANGE WITHOUT NOTICE

PROJECT PLANNING 5

                                   o     tI = processing time for the selected switching type in milliseconds (ms)
                                         O     Local control input: tI = 12 ms
                              2.   Calculate how much time is available in the response time for switching between
                                   monitoring cases:
                                   tCSA = (n – nCS) × tS
                                   where:
                                   o     tCSA = time available for switching between monitoring cases in milliseconds
                                         (ms)
                                   o     n = Multiple sampling setting (default: n = 2)
                                   o     nCS = multiple sampling after switching between monitoring cases (with set-
                                         ting Fast (presetting): nCS = 1, with setting Reliable: nCS = n – 1, with setting
                                         User-defined: nCS ≤ n – 1)
                                   o   tS = scan cycle time in milliseconds (ms)
                              3.   Compare whether there is enough time available for switching between monitoring
                                   cases:
                                   o     If tCSA ≥ tCSR: earlier start is not necessary.
                                   o     If tCSA < tCSR: switching between monitoring cases must start earlier. Required
                                         time advance tCSP: tCSP = tCSR – tCSA

                              Complementary information
                              O    In some cases, it is not possible to define when to switch (for example because
                                   processing times of the machine vary) or the time advance means that the moni-
                                   toring of an area finishes too early.
                                   Remedial measures:
                                   o  Allow both protective fields to partially overlap.
                                   o     Temporarily monitor both hazardous areas simultaneously.

                              Further topics
                              O    "Input delay", page 89

5.3.5          Minimum distance for stationary applications
                              Overview
                              The protective field must be designed to recognize a person, at the latest, when he or
                              she reaches the minimum distance from the hazardous point The minimum distance
                              means that the dangerous state can be ended in good time before the person reaches
                              the hazardous point.

                              Minimum distance for stationary applications
                              The calculation of the minimum distance is based on international or national standards
                              and statutory requirements applicable at the place of installation of the machine.
                              If the minimum distance is calculated according to ISO 13855:2010, then it depends
                              on the following points:
                              O     Machine stopping time (time interval between triggering the sensor function and
                                    the end of the machine’s dangerous state, if necessary including signal propaga-
                                    tion times in the network and processing time in the control)
                              O    Response time of the protective device
                              O    Reach or approach speed of the person
                              O    Resolution (detection capability) of the safety laser scanner
                              O    Type of approach: parallel for hazardous area protection, orthogonal for hazardous
                                   area protection and access protection
                              O    Switching time between monitoring cases


8024596/1W27/2026-05-26 | SICK                                                                         nanoScan3 I/O     27
SUBJECT TO CHANGE WITHOUT NOTICE

5 PROJECT PLANNING

                          O    Parameters specified based on the application
                          O    Supplements for general and, possibly, reflection-based measurement errors (only
                               for hazardous area protection)
                          O    Supplement for protection against reaching over (only for hazardous area protec-
                               tion)
                          O    Height of the scan plane (only for hazardous area protection)
                          O    Supplement to prevent reaching through (only for access protection)

                          Complementary information
                          More information is available in the ISO 13855:2010 standard and in the Guide for Safe
                          Machinery from SICK.
                          SICK offers a stopping/run-down time measurement service in many countries.

                          Further topics
                          O    "Response times", page 133

5.3.6         Supplement ZR for reflection-based measurement errors

                          If there is a retroreflector in the vicinity of the protective device (distance of the retrore-
                          flector from protective field ≤ 6 m), you must take the supplement ZR = 350 mm into
                          account.

5.3.7         Hazardous area protection
                          Overview
                          The safety laser scanner is mounted with a horizontal scan plane in a stationary appli-
                          cation. This is, for example, on a machine where the hazardous area is not completely
                          surrounded by a physical guard.
                          During hazardous area protection, the safety laser scanner detects a person’s legs. The
                          protective field is parallel to the direction of approach.




                                                                                            S
                                                                                S




                          Figure 15: Stationary application with horizontal scan plane for hazardous area protection




28      nanoScan3 I/O                                                                              8024596/1W27/2026-05-26 | SICK
                                                                                              SUBJECT TO CHANGE WITHOUT NOTICE

PROJECT PLANNING 5

                              Complementary information
                              It is recommended to mark the course of the protective field boundaries on the floor.
                              By doing this, you allow machine operators to see the protective field boundaries and
                              make it easier to thoroughly check the protective function at a later date.

5.3.7.1        Protective field
                              In hazardous area protection, the minimum distance typically defines the protective
                              field size required.
                              If you define a number of monitoring cases with different protective fields, you must
                              calculate the protective field size separately for each protective field used.
                              In many cases, a resolution of 50 mm to 70 mm is suitable for hazardous area protec-
                              tion. Resolutions coarser than 70 mm are not permitted.

5.3.7.2        Supplement CRO to protect against reaching over

                              Overview
                              Under certain circumstances, a person can reach the hazardous area by reaching over,
                              before the protective device stops the dangerous state. The supplement CRO prevents
                              this.




                                                                              CRO = 1200 mm                    HD ≈ 0 mm




                              Figure 16: Protection against reaching over with low scan plane (dimensions in mm)




8024596/1W27/2026-05-26 | SICK                                                                            nanoScan3 I/O    29
SUBJECT TO CHANGE WITHOUT NOTICE

5 PROJECT PLANNING




                                                                                                          HD = 875 mm




                                                                               CRO = 850 mm




                            Figure 17: Protection against reaching over with high scan plane (dimensions in mm)


                            The necessary supplement to the minimum distance depends on the height of the
                            protective field’s scan plane. With a low scan plane, the supplement is greater than with
                            a high scan plane.

                            Calculating the supplement CRO

                            →    If there is sufficient space in front of the hazardous area, use CRO = 1,200 mm.
                            →    If the minimum distance should be as small as possible, calculate CRO using the
                                 following formula:
                                 CRO = 1,200 mm – (0.4 × HD)
                                 where:
                                 o     HD = height of the protective field above the floor in millimeters (mm).
                            m    If the result is CRO ≥ 850 mm, then use the calculated value as supplement C.
                            m    If the result is CRO < 850 mm, then use CRO = 850 mm (this value corresponds to
                                 an arm’s length and is valid as a minimum supplement to protect against reaching
                                 over).

5.3.7.3         Calculation example for the minimum distance
                            Example calculation of the minimum distance S according to ISO 13855:2010
                            The example shows the calculation of the minimum distance S for parallel approach to
                            the protective field. A different calculation may be required, depending on the applica-
                            tion and the ambient conditions (e.g. for a protective field orthogonal to or at any angle
                            to the direction of approach or an indirect approach).
                            S = 1,600 mm/s × T + TZ + ZR + CRO

                            where:
                            O   S = minimum distance in millimeters (mm)
                            O    T = stopping/run-down time for the entire system in seconds (s)
                                 (Response time of the safety laser scanner + machine stopping time, incl.
                                 response time of the machine control system and signal propagation time)
                            O    TZ = tolerance zone of the safety laser scanner, see "Data sheet", page 129




30        nanoScan3 I/O                                                                            8024596/1W27/2026-05-26 | SICK
                                                                                              SUBJECT TO CHANGE WITHOUT NOTICE

PROJECT PLANNING 5

                              O    ZR = supplement for reflection-based measurement errors in millimeters (mm),
                                   see "Supplement ZR for reflection-based measurement errors", page 28
                              O    CRO = supplement to protect against reaching over in millimeters (mm), see "Sup-
                                   plement CRO to protect against reaching over", page 29

                              The reach/approach speed is already included in the formula.

5.3.7.4        Height of the scan plane
                              Overview
                              If you mount the safety laser scanner at a height of at least 300 mm (height of the scan
                              plane), the scan plane is at calf height and the leg is detected at a resolution of 70 mm
                              (see figure 18, page 31).
                              If the scan plane is lower than 300 mm, you must use a resolution finer than 70 mm.
                              The scan plane must not be higher than 1,000 mm.




                                                                 HD




                              Figure 18: Scan plane at calf height


                              Calculating required resolution
                              If the height of the protective field (scan plane) is predefined and is less than 300 mm,
                              you can calculate the required resolution using the following formula:
                              dr = HD / 15 +50 mm

                              where:
                              O   dr = coarsest permissible resolution of the safety laser scanner in millimeters (mm)
                              O    HD = height of the protective field above the floor in millimeters (mm)

                              The safety laser scanner’s resolution can be set to the predefined value d. If the result dr
                              does not match any of these values, you must choose a finer resolution (d ≤ dr).


5.3.7.5        Distance from walls
                              The availability may be impaired if the protective field stretches as far as a wall or a
                              different object. So, a space between the protective field and the object is required. A
                              distance of the TZ value is recommended to ensure availability. (TZ = tolerance zone of
                              the safety laser scanner, see "Data sheet", page 129.)


8024596/1W27/2026-05-26 | SICK                                                                        nanoScan3 I/O    31
SUBJECT TO CHANGE WITHOUT NOTICE

5 PROJECT PLANNING




                                                                                1




                          Figure 19: Distance of the protective field from the wall


                          1      Recommended distance of the protective field from the wall.

                          If the distance between the protective field and the wall is so large that a person can
                          stand in it, this person might not be detected. In this case, appropriate measures are
                          required to prevent it, e.g. deflector plates or a fence.

5.3.8         Hazardous point protection
                          Overview
                          The safety laser scanner is mounted with a vertical scan plane in a stationary applica-
                          tion. This is, for example, on a machine where the operator must stay close to the
                          hazardous point. A fixed barrier with a height of at least 1200 mm is located in front
                          of the hazardous point. The operator can reach over the barrier and through the scan
                          plane into the hazardous point. But the operator cannot climb over the barrier. If there is
                          no such barrier available, access protection may be required.
                          During hazardous point protection, the safety laser scanner detects a person’s hand or
                          other part of their body of at least the same size. The protective field is orthogonal to
                          the direction of approach.
                          You must monitor a reference contour to protect the safety laser scanner from acciden-
                          tal misalignment or manipulation.




32      nanoScan3 I/O                                                                           8024596/1W27/2026-05-26 | SICK
                                                                                           SUBJECT TO CHANGE WITHOUT NOTICE

PROJECT PLANNING 5




                                                 s




                              Figure 20: Stationary application in vertical operation for hazardous point protection


                              Important information

                              DANGER
                              Hazard due to lack of effectiveness of the protective device
                              If there is a retroreflector in the protective field level (distance of the retroreflector from
                              protective field ≤ 6 m), it may not be possible detect people and parts of the body that
                              are to be protected, or it may not be possible to detect them on time.

                              →    Avoid retroreflectors in the protective field level if possible.
                              →    With retroreflectors at the protective field level: Increase overrun of the protective
                                   field over the opening to be protected by supplement ZR = 350 mm.


5.3.8.1        Protective field
                              In hazardous point protection, the minimum distance typically defines the position at
                              which the safety laser scanner is mounted. Access to the hazardous point shall only be
                              possible through the protective field.
                              In many cases, a resolution of 20 mm, 30 mm or 40 mm is suitable for hazardous point
                              protection. A resolution of 40 mm or finer is required to ensure detection of the hand
                              during hazardous point protection. The safety laser scanner is not suitable for finger
                              detection, because the finest resolution is 20 mm.

                              Complementary information
                              The required minimum distance depends on the safety laser scanner’s set resolution.
                              Notes on selecting the resolution:
                              O   If you choose a fine resolution, the protective field range is smaller and the protec-
                                  tive field is only suitable for smaller hazardous points. But the required minimum
                                  distance is smaller, you can mount the safety laser scanner closer to the hazard-
                                  ous point.
                              O    If you choose a coarser resolution, the protective field range is larger and the pro-
                                   tective field is also suitable for larger hazardous points. But the required minimum
                                   distance is larger, you must mount the safety laser scanner further away from the
                                   hazardous point.


8024596/1W27/2026-05-26 | SICK                                                                               nanoScan3 I/O   33
SUBJECT TO CHANGE WITHOUT NOTICE

5 PROJECT PLANNING

5.3.8.2         Calculation example for the minimum distance
                            Example calculation of the minimum distance S according to ISO 13855:2010
                            The example shows the calculation of the minimum distance for an orthogonal
                            approach to the protective field. A different calculation may be required depending
                            on the application and the ambient conditions, e.g. for a protective field parallel to or at
                            any angle to the direction of approach or an indirect approach.

                            →    First, calculate S using the following formula:
                                 S = 2,000 mm/s × T +8 ×(d – 14 mm)
                                 where:
                                 o   S = minimum distance in millimeters (mm)
                                 o     T = stopping/run-down time for the entire system in seconds (s)
                                       (Response time of the safety laser scanner + machine stopping time, incl.
                                       response time of the machine control system and signal propagation time)
                                 o     d = resolution of the safety laser scanner in millimeters (mm)
                            m    If the result is S ≤ 100 mm, use S = 100 mm.
                            m    If the result is 100 mm < S ≤ 500 mm, use the calculated value as the minimum
                                 distance.
                            →    If the result is S > 500 mm, then recalculate S with the following formula:
                                 S = 1,600 mm/s × T +8 ×(d – 14 mm)
                            m    If the new value is S > 500 mm, then use the newly calculated value as the
                                 minimum distance.
                            m    If the new value is S ≤ 500 mm, then use S = 500 mm as the minimum distance.

                            The reach/approach speed is already included in the formula.

5.3.9           Access protection
                            Overview
                            In a stationary application, for example on a machine where the point of access to the
                            hazardous area can be physically defined, the safety laser scanner is mounted with a
                            vertical scan plane.
                            For access protection, the safety laser scanner detects an intrusion by a whole body.
                            The protective field is orthogonal to the direction of approach.
                            You must monitor a reference contour to protect the safety laser scanner from acciden-
                            tal misalignment or manipulation.




34        nanoScan3 I/O                                                                         8024596/1W27/2026-05-26 | SICK
                                                                                           SUBJECT TO CHANGE WITHOUT NOTICE

PROJECT PLANNING 5




                                                                         S




                              Figure 21: Stationary application in vertical operation for access protection


                              Important information

                              DANGER
                              Hazard due to lack of effectiveness of the protective device
                              If there is a retroreflector in the protective field level (distance of the retroreflector from
                              protective field ≤ 6 m), it may not be possible detect people and parts of the body that
                              are to be protected, or it may not be possible to detect them on time.

                              →    Avoid retroreflectors in the protective field level if possible.
                              →    With retroreflectors at the protective field level: Increase overrun of the protective
                                   field over the opening to be protected by supplement ZR = 350 mm.


5.3.9.1        Protective field
                              In access protection, the minimum distance typically defines the position at which the
                              safety laser scanner is mounted.
                              The protective field must cover a minimum area so that the safety laser scanner
                              reliably detects a moving person:
                              O    The lower edge of the protective field must not be more than 300 mm above the
                                   floor/ground according to ISO 13855:2010.
                              O    Resolution < 150 mm: The top edge of the protective field must be at least
                                   900 mm above the floor/ground according to ISO 13855:2010.
                              O    Resolution 150 mm: The top edge of the protective field must be at least 1,100 mm
                                   above the floor/ground.
                              O    Resolution 200 mm: The top edge of the protective field must be at least
                                   1,400 mm above the floor/ground.
                              The multiple sampling must be 2 or 3. Otherwise, a person could possibly walk unde-
                              tected through the protective field.




8024596/1W27/2026-05-26 | SICK                                                                                nanoScan3 I/O   35
SUBJECT TO CHANGE WITHOUT NOTICE

5 PROJECT PLANNING

5.3.9.2         Calculation example for the minimum distance
                            Example calculation of the minimum distance S according to ISO 13855:2010
                            The example shows the calculation of the minimum distance for an orthogonal
                            approach to the protective field. A different calculation may be required, depending
                            on the application and the ambient conditions (e.g. for a protective field parallel to or at
                            any angle to the direction of approach or an indirect approach).
                            S = 1,600 mm/s × T +850 mm
                            where:
                            O   S = minimum distance in millimeters (mm)
                            O    T = stopping/run-down time for the entire system in seconds (s)
                                 (Response time of the safety laser scanner + machine stopping time, incl.
                                 response time of the machine control system and signal propagation time)
                            The approach speed is already included in the formula.

5.3.10          Mobile hazardous area protection
                            The safety laser scanner is mounted with a horizontal scan plane in a mobile applica-
                            tion, like on an automated guided vehicle. In mobile hazardous area protection, the
                            safety laser scanner protects the hazardous area created by the vehicle’s movement.
                            The safety laser scanner detects a person’s legs. The protective field is parallel to the
                            direction of approach.




                                                                                S




                            Figure 22: Mobile application in horizontal operation for hazardous area protection


                            NOTE
                            O    In a mobile application, a resolution of 70 mm (leg detection) is sufficient for
                                 detecting people. By contrast with stationary hazardous point protection, this is
                                 also true for a low mounting height, as the safety laser scanner moves together
                                 with the vehicle.
                            O    In the following calculation examples, only the vehicle speed is taken into account,
                                 not the speed of a walking person. This is based on the assumption that the person
                                 recognizes the danger and stands still.




36        nanoScan3 I/O                                                                             8024596/1W27/2026-05-26 | SICK
                                                                                               SUBJECT TO CHANGE WITHOUT NOTICE

PROJECT PLANNING 5

5.3.10.1       Protective field
                              The protective field must be designed in such a way that it recognizes a person at
                              the latest when he or she is at the minimum distance from the hazardous point. The
                              minimum distance allows the vehicle to stop in time before it reaches a person or an
                              object.
                              In mobile hazardous area protection, the minimum distance typically defines the pro-
                              tective field length required. When calculating the protective field length, the impact of
                              turning must be considered separately.
                              The protective field must be wide enough to cover the width of the loaded vehicle with
                              supplements for measurement error and the lack of ground clearance. When calculat-
                              ing the protective field width, the impact of turning must be considered separately.
                              If you define a number of monitoring cases with different protective fields, you must
                              calculate the protective field size separately for each protective field used.

5.3.10.2       Supplement ZF for lack of ground clearance

                              This supplement is necessary, because, generally, a person is detected above the foot
                              and the braking process cannot take account of the length of the foot in front of the
                              point of detection. A person’s foot could be injured if a vehicle has no ground clearance.




                                                                                   SL
                                                                                                        ZF




                                                              BF



                              Figure 23: Flat-rate supplement for lack of ground clearance


                              BF     Ground clearance
                              SL     Protective field length without a supplement for lack of ground clearance
                              ZF     Supplement for lack of ground clearance

                              The lump supplement for ground clearance under 120 mm is 150 mm. This supplement
                              may be reduced further in individual cases, see figure 24, page 38.




8024596/1W27/2026-05-26 | SICK                                                                               nanoScan3 I/O   37
SUBJECT TO CHANGE WITHOUT NOTICE

5 PROJECT PLANNING

                             BF [mm]

                                  120




                                   60

                                   50



                                        0              50                 100            150     Z F [mm]

                             Figure 24: Minimum supplement for lack of ground clearance


                             BF     Ground clearance in mm
                             ZF     Supplement for lack of ground clearance in mm


5.3.10.3         Stopping distance SA

                             The stopping distance is the sum of the following distances:
                             O   Braking distance of the vehicle
                             O     Distance covered during the response time of the safety laser scanner
                             O     Distance covered during the response time of the vehicle control (incl. signal
                                   propagation time)
                             A vehicle’s braking distance does not increase linearly with increasing speed, but rather
                             in a squared relationship.
                             SA
                                                                     SA




                                                            SA + Z




                                               SL




                                                                                    v

                             Figure 25: Stopping distance as a function of the vehicle’s speed




38         nanoScan3 I/O                                                                              8024596/1W27/2026-05-26 | SICK
                                                                                                 SUBJECT TO CHANGE WITHOUT NOTICE

PROJECT PLANNING 5


                              v        Speed
                              SA       Stopping distance
                              Z        Supplements
                              SL       Protective field length for the relevant range of speeds

                              SA = SBr + SAnF + SAnS

                              where:
                              O   SA = stopping distance in millimeters (mm)
                              O    SBr = braking distance, from the vehicle documentation, in millimeters (mm)
                              O    SAnF = distance covered during the vehicle control’s response time (including
                                   signal propagation time), from the vehicle documentation, in millimeters (mm)
                              O    SAnS = distance covered during the response time of the safety laser scanner in
                                   millimeters (mm)
                                   The distance SAnS depends on the safety laser scanner’s response time and the
                                   vehicle’s speed. The distance SAnS is calculated using the following formula:
                                   SAnS = tR × Vmax
                                   where:
                                   o      tR = response time of the safety laser scanner in seconds (s)
                                   o      Vmax = maximum speed of the vehicle, from the vehicle documentation, in
                                          millimeters per second (mm/s) (If you define a number of monitoring cases
                                          with different protective fields: Vmax = maximum speed of the vehicle in the
                                          current monitoring case)

                              Further topics
                              O    "Response times", page 133

5.3.10.4       Calculation example for the protective field length
                              Calculation example for the protective field length SL

                              SL = SA + TZ + ZR + ZF + ZB

                              where:
                              O   SL = protective field length in millimeters (mm)
                              O    SA = stopping distance in millimeters (mm)
                              O    TZ = tolerance zone of the safety laser scanner, see "Data sheet", page 129
                              O    ZR = supplement for reflection-based measurement errors in millimeters (mm)
                              O    ZF = supplement for lack of ground clearance of the vehicle in millimeters (mm)
                              O    ZB = supplement for the decreasing braking force of the vehicle, from the vehicle
                                   documentation, in millimeters (mm)

5.3.10.5       Calculation example for the protective field width
                              Calculation example for the protective field width SB

                              SB = FB +2 × (TZ + ZR + ZF)

                              where:
                              O   SB = protective field width in millimeters (mm)
                              O    FB = vehicle width in millimeters (mm)
                              O    TZ = tolerance zone of the safety laser scanner, see "Data sheet", page 129
                              O    ZR = supplement for reflection-based measurement errors in millimeters (mm)
                              O    ZF = supplement for lack of ground clearance of the vehicle in millimeters (mm)



8024596/1W27/2026-05-26 | SICK                                                                         nanoScan3 I/O     39
SUBJECT TO CHANGE WITHOUT NOTICE

5 PROJECT PLANNING

5.3.10.6         Height of the scan plane
                             The scan plane must be at a maximum height of 200 mm everywhere. Otherwise,
                             persons lying horizontally may not be detected.
                             In many cases, a mounting height of 150 mm above the floor (height of the scan plane)
                             is suitable.




                                                                                 SL




                                                                        180 mm                       150 mm


                             Figure 26: Recommended fitting height




                                                                                 SL




                                                                        120 mm                       150 mm


                             Figure 27: Recommended fitting height for inverted mounting




40         nanoScan3 I/O                                                                        8024596/1W27/2026-05-26 | SICK
                                                                                           SUBJECT TO CHANGE WITHOUT NOTICE

PROJECT PLANNING 5

5.4            Integration in the electrical control system
                              Requirements for use
                              O    The control of the machine can be electrically influenced.
                              O    The connected controller and all devices responsible for safety comply with the
                                   required performance level and the required category (for example according to
                                   ISO 13849-1).
                              O    Power is supplied to all electrically connected devices in accordance with SELV/
                                   PELV (IEC 60204-1).
                              O    All devices connected to a local input or output are in the same SELV/PELV circuit
                                   as the product.
                              O    All electrically connected devices use the same earthing method.
                              O    All earthing points are connected with the same ground potential.

                              Further topics
                              O    "Electrical installation", page 56

5.4.1          Electromagnetic compatibility
                              Overview
                              Safety components switch all safety outputs to the OFF state in the event of errors in
                              order to rule out potentially dangerous situations. For example, faulty data transmission
                              must lead to a shutdown for safety-related devices, even if it can be tolerated for
                              non-safety-related devices.
                              To avoid electromagnetic interference as much as possible, a consistent earthing
                              method is required for the entire system. In particular, the functional earth must be
                              connected using suitable conductors. Cables susceptible to interference and sources
                              of interference should be routed separately.
                              Electromagnetic interference depends on the environment in which the product is
                              used. The product is tested and certified according to common standards. It is there-
                              fore reliable when used in industrial environments.

                              Shielded cables
                              For shielded cables, the shielding should be applied on both sides and over a large
                              area. Deviations are only permitted in exceptional and justified cases. Especially when
                              using motors or other inductive consumers, one-sided support of the shielding is not
                              sufficient because it does not act against inductive interferers.

                              Functional earth
                              The functional earth must be connected. The connection must be made in accordance
                              with the earthing method of the system.
                              Options for connecting the functional earth:
                              O   8-pin plug connector for voltage supply and inputs and outputs: pin 8 or thread on
                                  the M12 plug connector
                              O    17-pin plug connector for voltage supply and inputs and outputs: thread on the M12
                                   plug connector
                              O    Flying leads: Shielding of connecting cable
                              O    M5 threaded holes on the housing
                              The functional earth must be connected with low inductance, i.e. with a sufficient wire
                              cross-section and the shortest possible length of cable.




8024596/1W27/2026-05-26 | SICK                                                                      nanoScan3 I/O       41
SUBJECT TO CHANGE WITHOUT NOTICE

5 PROJECT PLANNING

                          Complementary information
                          For more information, see the “Background knowledge on EMC” technical information
                          (part number 8027030).

5.4.2         Voltage supply
                          Prerequisites
                          O    The power supply unit is able to jumper a brief power failure of 20 ms as specified
                               in IEC 60204-1.
                          O    The power supply unit provides safe isolation according to IEC 61140 (SELV/PELV
                               as per IEC 60204-1).
                          O    The electrical power supply has an appropriate electrical fuse.

                          Further topics
                          O    "Data sheet", page 129

5.4.3         USB connection
                          The device has a USB connection for configuration and diagnostics. The USB port
                          complies with the USB 2.0 Micro-B standard (socket). The USB port may only be used
                          temporarily and only for configuration, diagnostics and installation of firmware.

                          Further topics
                          O    "Configuration", page 61
                          O    "Troubleshooting", page 118

5.4.4         OSSDs
                          Overview
                          When the protective field is clear, the OSSDs signal the ON state and the signal level is
                          HIGH (non-isolated). If there are objects in the protective field or there is a device error,
                          the OSSDs signal the OFF state with the LOW signal level.
                          Downstream control elements must evaluate the output signals of the protective device
                          in such a way that the dangerous state of the machine is safely ended. Depending on
                          the safety concept, the signal is analyzed by safety relays or a safety controller, for
                          example.
                          The OSSDs are short-circuit proof against 24 VDC and 0 V.

                          Prerequisites
                          O    The machine switches to the safe state if, at any time, at least one OSSD in an
                               OSSD pair switches to the OFF state.
                          O    When using a safety controller: The safety controller detects different signal levels
                               of the two OSSDs of an OSSD pair (depending on national regulations or required
                               reliability of the safety function). The maximum discrepancy time tolerated by the
                               control is selected according to the application.
                          O    The output signals from an OSSD pair are not connected to each other.
                          O    The machine controller processes both signals of an OSSD pair separately.




42      nanoScan3 I/O                                                                          8024596/1W27/2026-05-26 | SICK
                                                                                          SUBJECT TO CHANGE WITHOUT NOTICE

PROJECT PLANNING 5




                                               OSSD A   OSSD B                                       OSSD A    OSSD B




                                   Figure 28: Dual-channel and isolated connection of an OSSD pair

                              O    No potential difference can occur between the load and the protective device. The
                                   0 V connections of the load and those of the associated protective device are
                                   connected individually and directly to the same 0 V terminal strip. In the event of
                                   an error, this is the only way to ensure that there can be no potential difference
                                   between the 0 V connections of the loads and those of the corresponding protec-
                                   tive device. This is particularly important for loads that switch even if they are
                                   activated with negative voltage (e.g. electromechanical contactor without reverse
                                   polarity protection diode).




                                                                 OSSD A   OSSD B                                        OSSD A   OSSD B




                                   Figure 29: No potential difference between load and protective device



5.4.5          Control inputs
                              Overview
                              Local control inputs accept signals for switching between different monitoring
                              cases:
                              O   Static control inputs are used for information about machine status.
                              O    Dynamic control inputs are usually used for information about the speed of a
                                   vehicle.

                              Prerequisites
                              O    The safety-related parts of the controller that switch the active protective field
                                   provide the same safety level as the safety function. In many cases, this is PL d as
                                   per ISO 13849-1 or SIL 2 as per IEC 62061.
                              O    Position-dependent switching is carried out by 2 independently wired signal sour-
                                   ces, such as 2 independent position switches.




8024596/1W27/2026-05-26 | SICK                                                                                nanoScan3 I/O               43
SUBJECT TO CHANGE WITHOUT NOTICE

5 PROJECT PLANNING

                             O    Speed-dependent switching is carried out by two independently wired signal sour-
                                  ces, such as two independent incremental encoders.
                             O    Manual switching that depends on the operating mode is carried out using a
                                  suitable manual control switch.

                             Further topics
                             O    "Data sheet", page 129
                             O    "Electrical installation", page 56
                             O    "Inputs and outputs, local", page 84

5.4.5.1         Static control inputs
                             Overview
                             The static control inputs support the following evaluation methods:
                             O   Complementary evaluation
                             O    1-out-of-n evaluation (only devices with several static control inputs)

                             Complementary evaluation
                             A static control input consists of 2 channels in the case of complementary sampling.
                             The channels of a static control input are switched inversely. The following table shows
                             which status the static control input’s channels must have to define logical input condi-
                             tion 1 and 0 at the relevant control input.
                             Table 3: Status of the channels of the control inputs with complementary evaluation
                             A1                        A2                       Logical input status (input A)
                             1                         0                        0
                             0                         1                        1
                             1                         1                        Error
                             0                         0                        Error

                             1-of-n evaluation
                             With the 1-out-of-n evaluation, each channel of a control input is considered individu-
                             ally. At any time, exactly one channel must have logic value 1.
                             Table 4: True vales with 1-off-n-evaluation with 2 input pairs (example)
                             A1           A2           B1           B2          Result (e.g. monitoring case no.)
                             1            0            0            0           1
                             0            1            0            0           2
                             0            0            1            0           3
                             0            0            0            1           4
                             Other input conditions                             Error




44        nanoScan3 I/O                                                                                8024596/1W27/2026-05-26 | SICK
                                                                                                  SUBJECT TO CHANGE WITHOUT NOTICE

PROJECT PLANNING 5

                              Complementary information
                              O    When the input signal is changed, the previous monitoring case remains active for
                                   the duration of the set switch-on delay. If no valid input signal is present after the
                                   switch-on delay has elapsed, the behavior depends on the sequence monitoring:
                                   o     If monitoring of the switching sequence (sequence monitoring) is not acti-
                                         vated, the OSSDs switch to the OFF state after the switch-on delay has
                                         elapsed. If a valid input signal is present within another second, the safety
                                         laser scanner activates the new monitoring case. If no valid input signal is
                                         present within this time, the OSSDs remain in the OFF state and the safety
                                         laser scanner displays an error and must be restarted.
                                   o     If monitoring of the switching sequence (sequence monitoring) is activated,
                                         the OSSDs switch to the OFF state after the switch-on delay has elapsed and
                                         the safety laser scanner displays an error and must be restarted.
                              O    A short-circuit or cross-circuit on one or more channels of the static control inputs
                                   can cause the wrong monitoring case to be activated.
                                   o     Some safety controllers detect the short-circuit or cross-circuit and switch off
                                         the outputs concerned or all their outputs.
                                   o     Due to the short-circuit or cross-circuit, one or more input channels of the
                                         safety laser scanner can still deliver the HIGH signal level. This may result in a
                                         valid input signal so that a monitoring case is activated.
                                   o     For this reason, laying the cables for the input signals in a protected manner
                                         is recommended. Otherwise, setting the switch-on delay to 0 s and activating
                                         sequence monitoring is recommended. Carrying out regular thorough check
                                         at short intervals is also recommended.

                              Further topics
                              O    "Settings for monitoring case tables", page 88
                              O    "Configure switching sequence", page 89

5.4.5.2        Dynamic control inputs
                              Overview
                              A dynamic control input receives speed information from an incremental encoder.

                              Important information

                              WARNING
                              Failure of both encoders due to a common cause
                              If both encoders fail at the same time, the device will receive no speed information.
                              Therefore, the device switches to the monitoring case defined for standstill, although
                              the vehicle may be moving.

                              →    Exclude errors with a common cause in the encoders.


                              Prerequisites
                              O    Defects of an incremental encoder are detected. Therefore, 2 incremental encod-
                                   ers are used which function independently of one another and transmit their sig-
                                   nals on separate pathways.
                              O    Only a single safety laser scanner is connected to each incremental encoder.
                              O    Each incremental encoder (with one wire each for 0° and 90°) is connected to only
                                   one control input.
                              O    Each incremental encoder is supplied with voltage via its own supply line.




8024596/1W27/2026-05-26 | SICK                                                                         nanoScan3 I/O     45
SUBJECT TO CHANGE WITHOUT NOTICE

5 PROJECT PLANNING

                           O      Errors with a common cause on both encoders are excluded.
                                  Possible measures:
                                  o   Each encoder has its own electrical power supply and its own supply line in
                                      its own sheathed cable.
                                  o    Both encoders and the device have a common electrical power supply at a
                                       protected location (e.g. in the control cabinet). Each encoder and device has
                                       its own supply line in its own sheathed cable.

                           Incremental encoder
                           Each incremental encoder must have a 0° output and a 90° output so that the direction
                           of travel can be detected.
                           Requirements for incremental encoders:
                           O   Dual-channel encoder with 90° phase separation
                           O      Outputs: push-pull
                           O      Shielded cable
                           O      Max pulse rate: 100 kHz
                           O      Minimum number of pulses: 100 pulses per cm
                           Suitable incremental encoders are available from SICK. Additional information can be
                           obtained from your SICK subsidiary.

5.4.6         Universal inputs, universal outputs, universal I/Os
                           Universal I/O can be configured as universal input or as universal output. In addition,
                           certain universal I/Os can be used in pairs as OSSD pairs, depending on the device.
                           Depending on the device, a universal input can be used for resetting, external device
                           monitoring (EDM), sleep mode, or restarting the protective device, for example. If sleep
                           mode is activated by a universal input, the sleep mode must not be used for safety
                           applications. Certain universal inputs can also be used in pairs as a static control input.
                           The function of a universal output is configurable. Which functions are available
                           depends on the device. Possible signals are, for example: reset required, contamination
                           warning.
                           A universal output must not be used for safety functions.

                           Further topics
                           O      "Electrical installation", page 56
                           O      "Technical data", page 128

5.4.7         Restart interlock
                           Overview
                           Depending on the regulations which apply at the place of installation, a restart interlock
                           may be required.
                           The restart interlock prevents the machine from automatically starting up, for example
                           after a protective device has responded while the machine is operating or after chang-
                           ing the machine’s operating mode.
                           First, the operator must press a reset pushbutton to return the protective device to
                           monitoring status. Then, in a second step, the operator can restart the machine.




46      nanoScan3 I/O                                                                         8024596/1W27/2026-05-26 | SICK
                                                                                         SUBJECT TO CHANGE WITHOUT NOTICE

PROJECT PLANNING 5

                              Prerequisites
                              O    The control switch for resetting the restart interlock (reset pushbutton) is mounted
                                   outside the hazardous area.
                              O    Persons within the hazardous area cannot operate the reset pushbutton.
                              O    Any person operating the control switch can view the entire hazardous area.

                              Internal restart interlock
                              Each safety output of the safety laser scanner is equipped with a configurable internal
                              restart interlock.
                              When the internal restart interlock is used, the following sequence is the result for
                              the machine operator:
                              1    A safety output of the safety laser scanner switches to the OFF state, if there is an
                                   interruption in the protective field.
                              2    The safety output remains in the OFF state when there is no longer an object in the
                                   protective field.
                              3    The safety output only switches back to the ON state when the operator presses
                                   the reset pushbutton, which is outside the hazardous area. If there is an object in
                                   the protective field when the reset pushbutton is pressed, the safety output stays
                                   in the OFF state.
                              4    After the reset, the operator can restart the machine in a second step.




                              Figure 30: How the restart interlock works (1): no one in protective field, machine operates




8024596/1W27/2026-05-26 | SICK                                                                               nanoScan3 I/O   47
SUBJECT TO CHANGE WITHOUT NOTICE

5 PROJECT PLANNING




                     Figure 31: How the restart interlock works (2): person detected in protective field, safety output in
                     OFF state




                     Figure 32: How the restart interlock works (3): person in hazardous area, no detection in protective
                     field, safety output still in OFF state




48   nanoScan3 I/O                                                                              8024596/1W27/2026-05-26 | SICK
                                                                                           SUBJECT TO CHANGE WITHOUT NOTICE

PROJECT PLANNING 5




                              Figure 33: How the restart interlock works (4): the reset pushbutton must be pressed before
                              restarting the machine.


5.4.8          External device monitoring (EDM)
                              Overview
                              The external switching elements (external device monitoring, EDM) must be inspected
                              in line with the regulations which apply at the place of installation or the required
                              reliability of the safety function.
                              The external device monitoring (EDM) monitors the status of downstream contactors.

                              Prerequisites
                              O    Positively guided contactors are used for shutting down the machine.
                                   If the auxiliary contacts of the positively guided contactors are connected to the
                                   external device monitoring, the external device monitoring checks whether the
                                   contactors switch correctly when the OSSDs are switched off.

5.5            Integration into the network

5.6            Testing plan
                              The manufacturer of the machine and the operating entity must define all required
                              thorough checks. The definition must be based on the application conditions and the
                              risk assessment and must be documented in a traceable manner.
                              The following tests must be planned:
                              O    Before commissioning the machine and after making changes, you must check
                                   whether the safety functions are fulfilling their planned purpose and whether per-
                                   sons are being adequately protected.
                              O    The thorough checks of the safety laser scanner must fulfill certain minimum
                                   requirements.
                              A test object is required for some thorough checks. An optically opaque cylinder with
                              a black surface can be used as a suitable test object. The diameter must match the
                              configured resolution.




8024596/1W27/2026-05-26 | SICK                                                                             nanoScan3 I/O    49
SUBJECT TO CHANGE WITHOUT NOTICE

5 PROJECT PLANNING

5.6.1         Planning the thorough check during commissioning and in certain situations
                          Minimum requirements
                          The protective device and its application must be thoroughly checked in the follow-
                          ing situations:
                          O    Before commissioning
                          O    After changes to the configuration or the safety function
                          O    After changes to the mounting, the alignment, or the electrical connection
                          O    After exceptional events, such as after manipulation has been detected, after
                               modification of the machine, or after replacing components
                          The thorough check ensures the following:
                          O    All relevant regulations are complied with and the protective device is active for all
                               of the machine’s operating modes. This includes the following points:
                               o     compliance with standards
                               o     correct use of the protective device
                               o     suitable configuration and safety function
                               o     correct alignment
                          O    The documentation accurately reflects the state/condition of the machine, includ-
                               ing the protective device.
                          O    The verified configuration report matches the desired project planning (see "Verify
                               configuration", page 96).
                          The thorough checks must be carried out by qualified safety personnel or specially
                          qualified and authorized personnel, and must be documented in a traceable manner.

                          Recommended thorough checks
                          In many cases, it makes sense to carry out the following thorough checks during
                          commissioning and in certain situations:
                          O   Test of the relevant points on the checklist, see "Checklist for initial commissioning
                              and commissioning", page 149
                          O    "Visual check of the machine and the protective device", page 53
                          O    "Thorough check of the principal function of the protective device", page 51
                          O    "Thorough check of the area to be protected", page 52
                          O    "Test of the contour detection field", page 52
                          O    Instruction of the operators in the function of the protective device

5.6.2         Planning the regular thorough check
                          Overview
                          The purpose of regular tests is to detect defects due to changes or external influences
                          (e.g. damage or manipulation) and to ensure that the protective measure provides the
                          necessary protection.

                          Important information

                          WARNING
                          Hazard due to lack of effectiveness of the protective device
                          Persons and parts of the body to be protected may not be recognized in case of
                          non-observance.

                          →    Carry out tests at least once a year.
                          →    Assign competent persons to carry out the tests or persons specifically authorized
                               for this purpose.
                          →    Document tests in a traceable manner.



50      nanoScan3 I/O                                                                         8024596/1W27/2026-05-26 | SICK
                                                                                         SUBJECT TO CHANGE WITHOUT NOTICE

PROJECT PLANNING 5

                              Minimum requirements for the regular thorough check
                              The following thorough checks must be carried out at least once a year:
                              O    "Thorough check of the principal function of the protective device", page 51
                              O    Test of the detection capability (resolution), see "Thorough check of the area to be
                                   protected", page 52

                              Recommendations for further thorough checks
                              In many cases, depending on the application conditions, the risk assessment of the
                              machine determines that further thorough checks are required or that some thorough
                              checks must take place more frequently.
                              In many cases, it makes sense to carry out the following thorough checks together
                              with the regular thorough check:
                              O    "Visual check of the machine and the protective device", page 53
                              O    "Test of the contour detection field", page 52
                              O    Test of the relevant points on the checklist, see "Checklist for initial commissioning
                                   and commissioning", page 149
                              In many cases, it makes sense to carry out the following thorough checks daily:
                              O   "Visual check of the machine and the protective device", page 53
                              O    "Thorough check of the principal function of the protective device", page 51

                              Complementary information
                              If the thorough check reveals an error, the machine should be shut down immediately.
                              In this case, the mounting and electrical installation of the device must be checked by
                              appropriately qualified safety personnel.

5.6.3          Notes on the tests
                              Thorough check of the principal function of the protective device

                              Recommended approach:
                              →   Observe display and status LEDs. An error has occurred if at least one LED does
                                  not light up permanently when the machine is switched on.
                              →   Test the function of the protective device. To do this, trigger the protective function
                                  once and observe the safety output’s reaction using the reaction of the machine,
                                  for example.
                                   o    All applications: During the thorough check, observe whether the safety laser
                                        scanner displays the interruption of the protective field using the LEDs and/or
                                        the display.
                                   o    Stationary application (hazardous area protection, access protection, hazard-
                                        ous point protection):
                                        O    Interrupt the protective field with the intended test object and observe
                                             whether the machine stops.
                                   o    Mobile application (mobile hazardous area protection):
                                        O    Place the supplied test object in the path of the vehicle and observe
                                             whether the vehicle stops.
                                             OR
                                        O    Activate a protective field, which is interrupted by at least one test object
                                             and check the expected reaction (for example by an automatic test in
                                             the safety controller).
                              If the thorough check reveals an error, the machine should be shut down immediately.
                              In this case, the mounting and electrical installation of the device must be checked by
                              appropriately qualified safety personnel.




8024596/1W27/2026-05-26 | SICK                                                                        nanoScan3 I/O     51
SUBJECT TO CHANGE WITHOUT NOTICE

5 PROJECT PLANNING

                     Thorough check of the area to be protected
                     The area to be protected and the detection capability are checked during this thorough
                     check.
                     The thorough check covers the following points:
                     O    Changes in the detection capability (thorough check of all configured fields)
                     O    Modifications, tampering and damage to the protective device or the machine,
                          which lead to changes in the area to be protected or the position of the protective
                          field
                     Recommended approach for hazardous area protection:
                     →   Position the supplied test object at a number of points at the edges of the area to
                         be protected. The safety laser scanner must detect the test object at each position
                         and indicate the detection. How it is indicated depends on the configuration. The
                         number and position of sites where the thorough check is carried out must be
                         chosen so that undetected access to the hazardous area is impossible.
                     →   If a number of protective fields are used (in different monitoring cases for exam-
                         ple), check the edges of all protective fields.

                     Recommended approach for access protection and hazardous point protection:
                     →   Move the supplied test object along the edges of the area to be protected. The
                         safety laser scanner must detect the test object at each position and indicate the
                         detection. How it is indicated depends on the configuration. The protective field
                         must be dimensioned such that reaching around or going around it is impossible.
                     →   If a number of protective fields are used (in different monitoring cases for exam-
                         ple), check the edges of all protective fields.
                     →   If the reference contour monitoring feature is used, check the areas with the refer-
                         ence contour:
                          o    Move the test object along the inner edge of the tolerance band of the refer-
                               ence contour. The safety laser scanner must detect the test object at each
                               position and indicate the detection.
                          o    If several reference contours are used, test all reference contours.
                     Recommended approach for mobile hazardous area protection:
                     →   Place the supplied test object in the path of the vehicle and check whether the
                         vehicle comes to a stop in time.
                     →   If a number of protective fields are used (in different monitoring cases for exam-
                         ple), check whether the vehicle comes to a stop in time in all of the protective
                         fields.
                     →   If necessary, change the position of the test object so that a thorough check is
                         carried out for each monitoring case to determine whether the protective field is
                         active over the whole of the required width.
                     →   Check the height of the scan plane. The scan plane must be at a height of at least
                         200 mm so that people lying down can be reliably detected. For this purpose,
                         position the supplied test object at a number of points at the edges of the largest
                         protective field. The safety laser scanner must detect the test object at each posi-
                         tion and indicate the detection. How it is indicated depends on the configuration.

                     If the thorough check reveals an error, the machine should be shut down immediately.
                     In this case, the mounting and electrical installation of the device must be checked by
                     appropriately qualified safety personnel.

                     Test of the contour detection field
                     If you use contour detection fields, you must test whether each contour detection field
                     fulfills the intended function.




52   nanoScan3 I/O                                                                     8024596/1W27/2026-05-26 | SICK
                                                                                  SUBJECT TO CHANGE WITHOUT NOTICE

PROJECT PLANNING 5

                              Notes on planning the test
                              O   Which contour should be detected at which position? What is the desired result?
                              O    What is the desired result if the contour is not at the position?
                              O    What is the desired result if only one part of the contour is at the position?
                              O    Is it possible for there to be another object at the intended position instead of
                                   the expected object, so that the device still recognizes the contour? What is the
                                   desired result?
                              If the thorough check reveals an error, the machine should be shut down immediately.
                              In this case, the mounting and electrical installation of the device must be checked by
                              appropriately qualified safety personnel.

                              Visual check of the machine and the protective device

                              Recommended approach:
                              →   Check whether the machine or the protective device has been modified or manip-
                                  ulated so that the effectiveness of the protective device may be impaired.
                              →   In particular, check the following points:
                                   o    Has the machine been retrofitted?
                                   o    Have machine parts been removed?
                                   o    Have modifications been made to the surroundings of the machine?
                                   o    Are there any defective cables or open cable ends?
                                   o    Have the protective device or its parts been dismantled?
                                   o    Is the protective device damaged?
                                   o    Is the protective device severely contaminated?
                                   o    Is the optical cover contaminated, scratched or destroyed?
                                   o    Has the protective device’s alignment been changed?
                                   o    Are there any objects (e.g. cables, reflective surfaces) in the protective field?
                              If one of the points applies, the machine should be shut down immediately. In this case,
                              the machine and the protective device must be checked by appropriately qualified
                              safety personnel.




8024596/1W27/2026-05-26 | SICK                                                                         nanoScan3 I/O   53
SUBJECT TO CHANGE WITHOUT NOTICE

6 MOUNTING

6           Mounting
6.1         Safety
                      Important information

                      DANGER
                      Death or severe injury due to electrical voltage and/or an unexpected startup of the
                      machine

                      →    Make sure that the machine is and remains in a de-energized state during mount-
                           ing and electrical installation.
                      →    Make sure that the dangerous state of the machine is and remains switched off.


                      NOTICE
                      The optics cover of the safety laser scanner is an optical component.

                      →    Do not contaminate or scratch the optics cover during unpacking and mounting.
                      →    Prevent fingerprints on the optics cover.


6.2         Unpacking
                      Procedure

                      →    Check the components for completeness and the integrity of all parts.
                      →    In the event of complaints, contact the responsible SICK subsidiary.

                      Further topics
                      O    "Ordering information", page 141

6.3         Fitting the system plug
                      Prerequisites
                      Tool required:
                      O    TX10 key

                      Procedure




                      1.   Carefully insert the system plug into the safety laser scanner.
                      2.   Screw in the system plug using the captive screws. Tightening torque: 1.3 Nm.




54    nanoScan3 I/O                                                                    8024596/1W27/2026-05-26 | SICK
                                                                                  SUBJECT TO CHANGE WITHOUT NOTICE

MOUNTING 6

6.4            Mounting the device
                              Prerequisites
                              O    Project planning has been completed.
                              O    Mount according to project planning.
                              O    Installation location provides protection against moisture, dirt and damage.
                              O    Status indicators are easily visible after mounting.

                              Procedure




                                                                                1




                                                                                                                    1
                              Figure 34: Mounting safety laser scanner

                              1      Side M5 threaded hole


                              →    Use all four sides of M5 threaded holes for direct mounting, so the values given in
                                   the data sheet for vibration and shock resistance are achieved.
                              →    Maximum depth of thread engagement: 7.5 mm.
                              →    Tightening torque: 4.5 Nm … 5.0 Nm.
                              →    In case of strong vibrations, use screw locking devices to secure the fixing screws.

                              Further topics
                              O    "Project planning", page 21
                              O    "Dimensional drawings", page 139




8024596/1W27/2026-05-26 | SICK                                                                      nanoScan3 I/O       55
SUBJECT TO CHANGE WITHOUT NOTICE

7 ELECTRICAL INSTALLATION

7             Electrical installation
7.1           Safety
                          Important information

                          DANGER
                          Death or severe injury due to electrical voltage and/or an unexpected startup of the
                          machine

                          →    Make sure that the machine is and remains in a de-energized state during mount-
                               ing and electrical installation.
                          →    Make sure that the dangerous state of the machine is and remains switched off.


7.2           Connecting
                          Overview
                          Depending on the system plug used, the connection is made via M12 plug connectors
                          or flying leads.

                          Prerequisites
                          O    Project planning has been completed.
                          O    Mounting is complete.
                          O    Electrical installation according to project planning.
                          O    Electrical installation according to the requirements of section 5.4, "Integration in
                               the electrical control system", page 41.
                          O    Functional earth is connected correctly.

                          Further topics
                          O    "Project planning", page 21
                          O    "Mounting", page 54

7.2.1         Connecting cable with M12 plug connector, 8-pin
                          Voltage supply and local inputs and outputs
                          O    Male connector
                          O    M12
                          O    8-pin
                          O    A-coded
                          2                1
                                           8
                          3                7
                          4
                          5                6

                          Figure 35: Connecting cable (male connector, M12, 8-pin, A-coded)




56      nanoScan3 I/O                                                                          8024596/1W27/2026-05-26 | SICK
                                                                                          SUBJECT TO CHANGE WITHOUT NOTICE

ELECTRICAL INSTALLATION 7

                              Table 5: Pin assignment of the connecting cable with 8-pin M12 plug connector
                               Pin                     Designation   Function
                               1                       24 V DC       Supply voltage (+24 V DC)
                               2                       OSSD 1.A      OSSD pair 1, OSSD A
                               3                       0 V DC        Supply voltage (0 V DC)
                               4                       OSSD 1.B      OSSD pair 1, OSSD B
                               5                       Uni-I/O 01    Universal I/O 1, configurable:
                                                                     O  Universal input: resetting, EDM (external device moni-
                                                                        toring), standby, restarting the device
                                                                     O  Universal output: contamination, error, reset required,
                                                                        monitoring result
                               6                       Uni-I/O 02    Universal I/O 2, configurable:
                                                                     O  Static control input A1 (together with pin 7)
                                                                     O  Universal input: resetting, EDM (external device moni-
                                                                        toring), standby, restarting the device
                                                                     O  Universal output: contamination, error, reset required,
                                                                        monitoring result
                               7                       Uni-I/O 03    Universal I/O 3, configurable:
                                                                     O  Static control input A2 (together with pin 6)
                                                                     O  Universal input: resetting, EDM (external device moni-
                                                                        toring), standby, restarting the device
                                                                     O  Universal output: contamination, error, reset required,
                                                                        monitoring result
                               8                       FE            Functional earth/shield
                               Thread                  FE            Functional earth/shield


7.2.2          Connecting cable with M12 plug connector, 17-pin
                              Voltage supply and local inputs and outputs
                              O    Male connector
                              O      M12
                              O      17-pin
                              O      A-coded
                              12  2           1   11
                              3                   10
                              13                  16
                              4                    9
                              17                   8
                              5 14 6          7   15

                              Figure 36: Connecting cable (male connector, M12, 17-pin, A-coded)


                              Table 6: Pin assignment of the connecting cable with M12 plug connector, 17-pin
                               Pin                     Designation   Function
                               1                       +24 V DC      Supply voltage (+24 V DC)
                               2                       0 V DC        Supply voltage (0 V DC)
                               3                       OSSD 1.A      OSSD pair 1, OSSD A
                               4                       OSSD 1.B      OSSD pair 1, OSSD B
                               5                       Uni-I/O 01    Universal I/O 1, configurable:
                                                                     O  Static control input B1
                                                                     O  Universal input: sleep mode, restarting the device
                                                                     O  Universal output: contamination, error, reset required
                                                                        (OSSD pair 1), monitoring result




8024596/1W27/2026-05-26 | SICK                                                                            nanoScan3 I/O      57
SUBJECT TO CHANGE WITHOUT NOTICE

7 ELECTRICAL INSTALLATION

                           Pin              Designation     Function
                           6                Uni-I/O 02      Universal I/O 2, configurable:
                                                            O  OSSD pair 2, OSSD A (OSSD 2.A)
                                                            O  Static control input A1
                                                            O  Universal input: sleep mode, restarting the device
                                                            O  Universal output: contamination, error, monitoring
                                                               result
                           7                Uni-I/O 03      Universal I/O 3, configurable:
                                                            O  OSSD pair 2, OSSD B (OSSD 2.B)
                                                            O  Static control input A2
                                                            O  Universal input: sleep mode, restarting the device
                                                            O  Universal output: contamination, error, monitoring
                                                               result
                           8                Uni-I/O 04      Universal I/O 4, configurable:
                                                            O  Static control input B2
                                                            O  Universal input: sleep mode, restarting the device
                                                            O  Universal output: contamination, error, reset required
                                                               (OSSD pair 2), monitoring result
                           9                Uni-I 01        Universal input 1, configurable:
                                                            O  Static control input C1
                                                            O  Dynamic control input 1a (0°)
                                                            O  Universal input: sleep mode, restarting the device
                           10               Uni-I 02        Universal input 2, configurable:
                                                            O  Static control input C2
                                                            O  Dynamic control input 1b (90°)
                                                            O  Universal input: sleep mode, restarting the device
                           11               Uni-I 03        Universal input 3, configurable:
                                                            O  Static control input D1
                                                            O  Dynamic control input 2a (0°)
                                                            O  Universal input: sleep mode, restarting the device
                           12               Uni-I 04        Universal input 4, configurable:
                                                            O  Static control input D2
                                                            O  Dynamic control input 2b (90°)
                                                            O  Universal input: sleep mode, restarting the device
                           13               Uni-I 05        Universal input 5, configurable:
                                                            O  Static control input E1
                                                            O  Universal input: resetting, (OSSD pair 1), sleep mode,
                                                               restarting the device
                           14               Uni-I 06        Universal input 6, configurable:
                                                            O  Static control input E2
                                                            O  Universal input: EDM (external device monitoring,
                                                               OSSD pair 1), sleep mode, restarting the device
                           15               Uni-I 07        Universal input 7, configurable:
                                                            O  Static control input F1
                                                            O  Universal input: resetting, (OSSD pair 2), sleep mode,
                                                               restarting the device
                           16               Uni-I 08        Universal input 8, configurable:
                                                            O  Static control input F2
                                                            O  Universal input: EDM (external device monitoring,
                                                               OSSD pair 2), sleep mode, restarting the device
                           17               nc              Not connected
                           Thread           FE              Functional earth/shield


7.2.3         Connecting cable with flying leads, 17-wire
                           Voltage supply and local inputs and outputs
                           O    Flying leads
                           O     17-wire




58      nanoScan3 I/O                                                                       8024596/1W27/2026-05-26 | SICK
                                                                                       SUBJECT TO CHANGE WITHOUT NOTICE

ELECTRICAL INSTALLATION 7




                              Table 7: Pin assignment of the connecting cable with flying leads, 17-wire
                               Wire color         Designation          Function
                               Brown              24 V DC              Supply voltage (+24 V DC)
                               Blue               0 V DC               Supply voltage (0 V DC)
                               White              OSSD 1.A             OSSD pair 1, OSSD A
                               Green              OSSD 1.B             OSSD pair 1, OSSD B
                               Pink               Uni-I/O 01           Universal I/O 1, configurable:
                                                                       O  Static control input B1
                                                                       O  Universal input: sleep mode, restarting the device
                                                                       O  Universal output: contamination, error, reset required
                                                                          (OSSD pair 1), monitoring result
                               Yellow             Uni-I/O 02           Universal I/O 2, configurable:
                                                                       O  OSSD pair 2, OSSD A (OSSD 2.A)
                                                                       O  Static control input A1
                                                                       O  Universal input: sleep mode, restarting the device
                                                                       O  Universal output: contamination, error, monitoring
                                                                          result
                               Black              Uni-I/O 03           Universal I/O 3, configurable:
                                                                       O  OSSD pair 2, OSSD B (OSSD 2.B)
                                                                       O  Static control input A2
                                                                       O  Universal input: sleep mode, restarting the device
                                                                       O  Universal output: contamination, error, monitoring
                                                                          result
                               Gray               Uni-I/O 04           Universal I/O 4, configurable:
                                                                       O  Static control input B2
                                                                       O  Universal input: sleep mode, restarting the device
                                                                       O  Universal output: contamination, error, reset required
                                                                          (OSSD pair 2), monitoring result
                               Red                Uni-I 01             Universal input 1, configurable:
                                                                       O  Static control input C1
                                                                       O  Dynamic control input 1a (0°)
                                                                       O  Universal input: sleep mode, restarting the device
                               Violet             Uni-I 02             Universal input 2, configurable:
                                                                       O  Static control input C2
                                                                       O  Dynamic control input 1b (90°)
                                                                       O  Universal input: sleep mode, restarting the device
                               Grey/Pink          Uni-I 03             Universal input 3, configurable:
                                                                       O  Static control input D1
                                                                       O  Dynamic control input 2a (0°)
                                                                       O  Universal input: sleep mode, restarting the device
                               Red/Blue           Uni-I 04             Universal input 4, configurable:
                                                                       O  Static control input D2
                                                                       O  Dynamic control input 2b (90°)
                                                                       O  Universal input: sleep mode, restarting the device
                               White/Green        Uni-I 05             Universal input 5, configurable:
                                                                       O  Static control input E1
                                                                       O  Universal input: resetting, (OSSD pair 1), sleep mode,
                                                                          restarting the device
                               Brown/Green        Uni-I 06             Universal input 6, configurable:
                                                                       O  Static control input E2
                                                                       O  Universal input: EDM (external device monitoring,
                                                                          OSSD pair 1), sleep mode, restarting the device




8024596/1W27/2026-05-26 | SICK                                                                               nanoScan3 I/O     59
SUBJECT TO CHANGE WITHOUT NOTICE

7 ELECTRICAL INSTALLATION

                         Wire color            Designation            Function
                         White/Yellow          Uni-I 07               Universal input 7, configurable:
                                                                      O  Static control input F1
                                                                      O  Universal input: resetting, (OSSD pair 2), sleep mode,
                                                                         restarting the device
                         Yellow/Brown          Uni-I 08               Universal input 8, configurable:
                                                                      O  Static control input F2
                                                                      O  Universal input: EDM (external device monitoring,
                                                                         OSSD pair 2), sleep mode, restarting the device
                         White/Gray            nc                     Not connected
                         – (shielding)         FE                     Functional earth


7.2.4         Network connection
                         Network connection
                         O   Female connector
                         O     M12
                         O     4-pin
                         O     D-coded
                         O     Pin assignment according to IEC 61918, Appendix H
                         1                2



                         4                3

                         Figure 37: Network pin assignment (M12 female connector, 4-pin, D-coding)


                         Table 8: Network pin assignment
                         Pin             Designation Function
                         1               TX+              Send data +
                         2               RX+              Receive data +
                         3               TX–              Send data -
                         4               RX–              Receive data -
                         Thread          SH               Shielding




60      nanoScan3 I/O                                                                                 8024596/1W27/2026-05-26 | SICK
                                                                                                 SUBJECT TO CHANGE WITHOUT NOTICE

CONFIGURATION 8

8                  Configuration
8.1                Delivery state
                                     The device is not configured in the delivery state.


8.2                Safety Designer configuration software
                                     The safety laser scanner is configured using the Safety Designer.
                                     For information on the Safety Designer, see the operating instructions for the Safety
                                     Designer item no. 8018178.

8.2.1              Installing Safety Designer
                                     Prerequisites
                                     O     Your Windows user account has rights for installing software.

                                     Procedure

                                     1.    Call up the download web page and enter Safety Designer in the search field on
                                           www.sick.com.
                                     2.    Take note of the system requirements on the download page.
                                     3.    Download the installation file from the download page. Extract it and run it.
                                     4.    Follow the notes from the setup assistant.

8.2.2              Projects
                                     Using Safety Designer, you can configure one or more devices in a project. You can save
                                     the configuration data in a project file on the computer.

                                     Creating a project

                                     →     Click on Create new project.
                                     m     This creates and opens an empty project.

                                     Configuring a device online (device connected to computer)
                                     The following interfaces are suitable for configuration:
                                     O     USB 1)
                                     O     Ethernet
                                     If a device is connected to the computer, Safety Designer can establish a connection to
                                     the device. 2)
                                     You will then configure the device online. In this case, you can transfer the configuration
                                     to the devices directly and use diagnostic functions.

                                     →     Click on Search.
                                     m     Safety Designer searches for connected devices, with which it can establish a
                                           connection.

                                     Configuring a device offline (device not connected to computer)
                                     If the device is not connected to the computer, select it from the device catalog.
                                     You will then configure the device offline. Diagnostics functions are not available.


1)      The USB port may only be used temporarily and only for configuration, diagnostics and installation of firmware.
2)      If the device is only connected via the network and has no network address, Safety Designer can find the device but cannot establish a
        connection to it. You first need to assign the device a valid network address.



8024596/1W27/2026-05-26 | SICK                                                                                               nanoScan3 I/O       61
SUBJECT TO CHANGE WITHOUT NOTICE

8 CONFIGURATION

                                  You can connect the computer to the device later, assign a device to the device tile, and
                                  transfer the configuration to the device.

8.2.2.1             Saving verified configuration
                                  When you save a project, information is saved for each device as to whether the con-
                                  figuration is verified. When you open a project file, each device tile and the Overview
                                  dialog box of the device window show whether the configuration is verified.
                                  You can transfer a verified configuration to the same or an identical device again.

8.2.3               User interface




Figure 38: Software controls

1         Menu bar
2         Toolbar
3         Main navigation
4         Working range
5         Device catalog
6         Task list and notes


8.2.4               User groups
                                  Overview
                                  The devices contain a hierarchy of user groups that regulate access to the devices.



62          nanoScan3 I/O                                                                           8024596/1W27/2026-05-26 | SICK
                                                                                               SUBJECT TO CHANGE WITHOUT NOTICE

CONFIGURATION 8

                              For certain actions (e.g., transferring a configuration to the device), you are requested to
                              log onto the device with the respective user group.

                              Important information

                              NOTICE
                              When you log into a device, the configuration software stores the password so that you
                              do not need to re-enter it for other configuration steps.
                              If you do not change any other settings in the login dialog, the password is deleted as
                              soon as you exit the configuration software, or log out in the main window or Device
                              window.
                              If you enable the Temporarily store password for login on additional devices. func-
                              tion, the password will be retained even if you log out in the device window only.
                              If you leave the computer unattended, you must log off to prevent unwanted access to
                              the device.


                              User groups
                              Table 9: User groups
                               User group            Password                               Authorization
                                   Machine opera-    No password required. Anyone can       O   May read configuration from the
                                   tor               log on as a machine operator.              device.
                                   Maintenance       Deactivated ex-works, i.e. it is not   O   May read configuration from the
                                                     initially possible to log on as a          device.
                                                     maintenance technician. The user       O   May transmit verified configura-
                                                     group can be activated by the user         tion to the device.
                                                     group administrator and provided       O   Change own password allowed.
                                                     with a password.
                                   Authorized client Deactivated ex-works, i.e. it is not   O   May read configuration from the
                                                     initially possible to log on as            device.
                                                     an authorized customer. The user       O   May transmit verified and
                                                     group can be activated by the user         unverified configuration to the
                                                     group administrator and provided           device.
                                                     with a password.                       O   May verify configuration.
                                                                                            O   Resetting the safety function
                                                                                                and communication settings to
                                                                                                factory defaults is allowed.
                                                                                            O   Change own password allowed.
                                                                                            O   Changing the password of the
                                                                                                Maintenance user group is
                                                                                                allowed.
                                   Administrator     The password SICKSAFE is created       O   May read configuration from the
                                                     at the factory.                            device.
                                                                                            O   May transmit verified and
                                                     → Change this password to protect          unverified configuration to the
                                                         the device against unauthorized        device.
                                                         access.                            O   May verify configuration.
                                                                                            O   Resetting whole device to fac-
                                                                                                tory settings allowed.
                                                                                            O   Activating and deactivating
                                                                                                device functions is allowed.
                                                                                            O   Activating and deactivating the
                                                                                                Maintenance, Authorized cli-
                                                                                                ent and SICK-service user
                                                                                                groups is allowed.
                                                                                            O   Change own password allowed.
                                                                                            O   Changing the passwords of the
                                                                                                Maintenance and Authorized
                                                                                                client user groups is allowed.




8024596/1W27/2026-05-26 | SICK                                                                              nanoScan3 I/O     63
SUBJECT TO CHANGE WITHOUT NOTICE

8 CONFIGURATION

                          User group            Password                               Authorization
                               SICK-service     The user group SICK-service is intended exclusively for cases whose
                                                access is required by SICK as the manufacturer. It is used for error analy-
                                                sis, diagnostics and carrying out service or repair work on the device.
                                                This user group is deactivated by default.
                                                Activation can only be performed by the user group Administrator.

                                                → Only activate this user group if it is required for support from SICK.
                                                → After completing the work, deactivate the user group again to prevent
                                                   unauthorized access to the device.


                          Complementary information
                          The administrator is permitted to install firmware.
                          The configuration of the device is saved in the system plug. Therefore, the passwords
                          are retained when the device is replaced if the system plug is still used.

8.2.5         Settings
                          Information on the functionality and basic operation of the software and on the settings
                          in the main window can be found in the operating instructions of the Safety Designer
                          (part number 8018178).

8.2.6         Configuration
                          You collect the devices of a project in the Configuration area. The available devices
                          can be found in the Device Catalog. The devices are displayed as Device tiles in the
                          working range.




64      nanoScan3 I/O                                                                            8024596/1W27/2026-05-26 | SICK
                                                                                            SUBJECT TO CHANGE WITHOUT NOTICE

CONFIGURATION 8




Figure 39: Configuration

1         Device management
2         Device tile


8.2.6.1          Device Catalog
                              Overview
                              Device Management contains all available devices:
                              O   The Catalog tab contains the devices installed in Safety Designer.
                              O    The Search tab contains the devices found during a search.

                              Procedure

                              The devices from the device catalog can be added to a project in the workspace:
                              →   Drag a device into the working area using drag and drop.
                                  Or:
                              →   Double-click on a device in the device catalog.
                              m   The device is shown as a tile in the working area.

                              Complementary information
                              When a device is configured offline for the first time, the device selection wizard opens
                              for devices with multiple variants (device types). This is where you select the exact type
                              of device to be configured.




8024596/1W27/2026-05-26 | SICK                                                                       nanoScan3 I/O    65
SUBJECT TO CHANGE WITHOUT NOTICE

8 CONFIGURATION

8.2.6.2          Open the device window – configure devices
                               Overview
                               To configure the device, perform diagnostics or create reports, open a device window.

                               Procedure

                               You have the following options:
                               →    Double-click on the Device tile.
                                    Or:
                               →    Open the tile menu and choose Configure.
                               m    The device window opens.

                               Complementary information
                               When a device is configured offline for the first time, the device selection wizard opens
                               for devices with multiple variants (device types). This is where you select the exact type
                               of device to be configured.

8.2.6.3          Type code in Safety Designer
                               The Safety Designer displays a separate type code for the device with system plug,
                               which differs from the type code for the device without system plug.
Table 10: Type code in Safety Designer
Device                                           System plug                                      Device with system plug
Performance pack-          Type code             Connections               Type code              Type code
age
Core I/O                   NANS3-AAAZ30AN1       O   Cable with plug con- NANSX-AAABZZZZ1         NANS3-AAAZ30AN1P01
                                                     nector
                                                 O   Cable with plug con- NANSX-AAABAEZZ1         NANS3-AAAZ30AN1P02
                                                     nector
                                                 O   Cable with M12 net-
                                                     work connection
Pro I/O                    NANS3-CAAZ30AN1       O   Cable with plug con- NANSX-AAACZZZZ1         NANS3-CAAZ30AN1P01
                                                     nector
                                                 O   Cable with plug con- NANSX-AAACAEZZ1         NANS3-CAAZ30AN1P02
                                                     nector
                                                 O   Cable with M12 net-
                                                     work connection
                                                 O   Flying leads          NANSX-AACCZZZZ1S01     NANS3-CAAZ30AN1P03
                                                     (880 mm)
                                                 O   Flying leads (2 m)    NANSX-AACCZZZZ1
                                                 O   Flying leads          NANSX-AACCAEZZ1S01     NANS3-CAAZ30AN1P04
                                                     (880 mm)
                                                 O   Cable with M12 net-
                                                     work connection
                                                 O   Flying leads (2 m)    NANSX-AACCAEZZ1
                                                 O   Cable with M12 net-
                                                     work connection


8.2.7            Networking
Information on the functionality and basic operation of the software and on the settings in the main window can be
found in the operating instructions of the Safety Designer (part number 8018178).




66         nanoScan3 I/O                                                                          8024596/1W27/2026-05-26 | SICK
                                                                                             SUBJECT TO CHANGE WITHOUT NOTICE

CONFIGURATION 8

8.3            Overview




Figure 40: Overview

1      Device information
2      Current measurement data
3      Display with device status


                              The Overview dialog box contains information about the safety laser scanner.

                              Project
                              O     Project name:
                                    This name should be chosen the same for all devices in the project.
                              O     Application name:
                                    This name can be the same for a number of devices in the project. It highlights
                                    that these devices realize an application together, by responding to one another
                                    for example.
                              O     User name

                              Device information
                              O     Name:
                                    Name for identification of the individual device.
                              O     Type code:
                              O     Functional scope of the configuration in the project:
                              O     Functional scope of the configuration in the device:


8024596/1W27/2026-05-26 | SICK                                                                      nanoScan3 I/O      67
SUBJECT TO CHANGE WITHOUT NOTICE

8 CONFIGURATION

                       O    Serial number:
                       O    Functional scope of the device:
                       O    Part number:
                       O    Hardware version:

                       Connection
                       O    Connection status:
                       O    Type:

                       Checksums
                       A checksum is used as a unique identification for a configuration. Using the checksum,
                       it is possible to work out whether a setup was changed or whether two devices have the
                       same configuration.
                       The checksum of the configuration in the project may not match the checksum in the
                       device, for example if a field geometry has been modified, but not yet transmitted to the
                       device.

                       System status
                       O    Application status:
                       O    Last message:
                       O    Device configuration date:
                       O    Synchronization:
                            Shows whether the configuration in Safety Designer and the configuration in the
                            device are identical.
                       O    Verification state project:
                       O    Verification state device:

                       Time synchronization
                       O    Configured value in the project
                       O    Configured values in the device

                       Measured data
                       Shows the measurement data when a device is connected.

                       Indicator
                       Shows the status of the display and LEDs when a device is connected.

                       Establishing connection
                       If the safety laser scanner is correctly connected, you can establish the connection to
                       the safety laser scanner by clicking Connect.


8.4         Hardware
                       Overview
                       On the Hardware page, you can view details of the safety laser scanner and the system
                       plug.
                       If several functionally identical products with different part numbers exist, you can
                       select your product. The selected product is shown in the report under Bill of materi-
                       als. The selection does not affect anything else.




68    nanoScan3 I/O                                                                      8024596/1W27/2026-05-26 | SICK
                                                                                    SUBJECT TO CHANGE WITHOUT NOTICE

CONFIGURATION 8

8.5            Network settings

8.5.1          Ethernet
                              IP address:
                              If you want to address the device via TCP/IP or output data, make the IP settings here.

                              Reading and transmitting values
                              If the values in the project and the values in the device differ, you can read the values
                              out from the device and adopt them in the project. Alternatively, you can transmit values
                              from the project to the device.


8.6            Time synchronization
                              Time synchronization
                              You can synchronize the time and date of the devices in the network. This is important,
                              amongst other things, for ensuring that diagnostics and reports have synchronized and
                              correct time stamps.
                              You can configure the time synchronization in the main window of the Safety Designer
                              or in the device window.
                              Information on the functionality and basic operation of the software and on the settings
                              in the main window can be found in the operating instructions of the Safety Designer
                              (part number 8018178).


8.7            Reading configuration
                              Overview
                              At the left, you see the values configured in the project for the device. If the device is
                              connected, you see the values saved in the device at the right.
                              If the values in the project and the values in the device differ, you can read the values
                              out from the device and adopt them in the project.

                              Procedure

                              1.   Click on Read from device.
                              m    The values are read from the device and adopted in the project.

                              Complementary information
                              Configuration:
                              O   Name
                                   If a number of devices are used in an application or in a project, a unique device
                                   name helps to tell the individual devices apart.
                              O    Checksums
                                   A checksum is used as a unique identification for a configuration. Using the check-
                                   sum, it is possible to work out whether a setup was changed or whether two
                                   devices have the same configuration.
                                   The checksum of the configuration in the project may not match the checksum
                                   in the device, for example if a field geometry has been modified, but not yet
                                   transmitted to the device.




8024596/1W27/2026-05-26 | SICK                                                                          nanoScan3 I/O      69
SUBJECT TO CHANGE WITHOUT NOTICE

8 CONFIGURATION

8.8         Identification
                       Overview
                       On the Identification page, you can optionally enter attributes for the device. The
                       attributes are used to identify the device or to distinguish between different devices.
                       The attributes appear in reports and in the diagnostic data.

                       Device name
                       If a number of devices are used in an application or in a project, a unique device name
                       helps to tell the individual devices apart.

                       Project name
                       The project name is used to identify an entire project. The same project name should be
                       chosen for all devices in the project.

                       Application name
                       The application name can be the same for a number of devices in the project.

                       User name
                       The optional user name helps later users to find a contact for the application.

                       Application image
                       An image helps to identify the application more quickly. The Safety Designer supports
                       the following file formats: BMP, GIF, JPG, PNG, TIF.

                       Description
                       A description makes it easier to understand an application’s context more quickly.


8.9         Application
                       Application type
                       The type of application depends on the application of the safety laser scanner:
                       O    Mobile
                             Mobile hazardous area protection is suitable for AGVs (automated guided vehi-
                             cles), cranes, and forklifts to protect people when vehicles are moving or docking.
                             The safety laser scanner monitors the area in the direction of travel and stops the
                             vehicle as soon as an object is located in the protective field.
                       O     Stationary
                             The position of the safety laser scanner is fixed. The safety laser scanner is
                             mounted horizontally (for hazardous area protection) or vertically (for hazardous
                             point protection and access protection).

                       Display language
                       The display of the safety laser scanner outputs notifications and states. Multiple lan-
                       guages are available for the display.

                       Display alignment
                       If you mount the safety laser scanner with the optics cover downward, you can rotate
                       the orientation of the display through 180°. The preview shows the selected orientation
                       of the display.




70    nanoScan3 I/O                                                                       8024596/1W27/2026-05-26 | SICK
                                                                                     SUBJECT TO CHANGE WITHOUT NOTICE

CONFIGURATION 8

8.10           Monitoring plane
                              Overview
                              Here you configure general parameters for the monitoring level.
                              At first, the object resolution and multiple sampling configured for the monitoring plane
                              apply for all fields. If necessary, you can make changes to each individually at a later
                              date.
                              Resulting values are displayed in the area on the right. A graphic shows how the config-
                              uration affects the available ranges.

                              Name
                              You can use the name to identify the monitoring levels in the reports.

                              Safety task
                              People approach the monitoring plane parallel or orthogonally, depending on the orien-
                              tation of the protective field in your application.
                              O    Hazardous area protection (Horizontal)
                                   Typically, for a horizontal approach, the requirement is to detect the leg. The typi-
                                   cal object resolution is leg (70 mm).
                              O    Access protection (Vertical)
                                   Typically, for access protection, the requirement is to detect a person. The typical
                                   object resolution is body (200 mm).
                              O    Hazardous point protection (Vertical)
                                   Typically, for hazardous point protection, the requirement is to detect a hand. The
                                   typical object resolution is hand (40 mm).

                              Reference contour monitoring
                              If the monitoring plane has a vertical alignment, a contour (such as the floor, a part of
                              the machine bed, or an access threshold) must typically be defined and monitored as a
                              reference contour. The reference contour field is used for this purpose.
                              If reference contour monitoring is activated, the Reference contour field point is dis-
                              played in the navigation. Here you can configure the reference contour field required for
                              your application.

                              Object resolution
                              The object resolution defines the size that an object must be to allow it to be reliably
                              detected. The following object resolutions are available:
                              O    20 mm = hand detection
                              O    30 mm = hand detection
                              O    40 mm = hand detection
                              O    50 mm = leg detection/arm detection
                              O    60 mm = leg detection/arm detection
                              O    70 mm = leg detection/arm detection
                              O    150 mm = body detection
                              O    200 mm = body detection




8024596/1W27/2026-05-26 | SICK                                                                         nanoScan3 I/O     71
SUBJECT TO CHANGE WITHOUT NOTICE

8 CONFIGURATION

                     Multiple sampling
                     Multiple sampling indicates how often an object has to be scanned before the safety
                     laser scanner responds. A higher multiple sampling reduces the possibility that insects,
                     weld sparks or other particles will cause the machine to be shut down. You will increase
                     the machine’s availability.
                     A multiple sampling of 2 is the minimum setting.
                     A higher multiple sampling increases the response time and influences the minimum
                     distance.
                     Table 11: Recommended multiple sampling
                     Application                                       Recommended multiple sampling
                     Stationary application: such as horizontal haz-   2×
                     ardous area protection or vertical hazardous
                     point protection under clean ambient condi-
                     tions
                     Stationary application: such as vertical access   2×
                     protection
                     Only 2-time or 3-time multiple sampling may
                     be used for vertical access protection.
                     Mobile application                                4×
                     Stationary application: such as horizontal haz-   8×
                     ardous area protection under dusty ambient
                     conditions

                     Multiple sampling after monitoring case switching
                     When switching between monitoring cases, it is possible that a person may already be
                     in the newly activated protective field when switching takes place. In order to ensure
                     that the person is detected quickly and the dangerous state is brought to an end swiftly,
                     you can adjust the settings for multiple sampling immediately after switching between
                     monitoring cases – regardless of any other multiple sampling in place.
                     For persons and body parts to be reliably detected, each monitoring case must be
                     active for at least as long as the safety laser scanner requires for detection (set multiple
                     sampling after switching between monitoring cases multiplied by the scan cycle time).
                     O    Fast (1 scan) (preset)
                          Multiple sampling after switching between monitoring cases nCS = 1. An object
                          needs to be scanned once before the safety laser scanner responds. Fastest
                          response and safest behavior of the safety laser scanner.
                     O    Robust (multiple sampling - 1)
                          Multiple sampling after switching between monitoring cases nCS = n - 1. Multiple
                          sampling after switching between monitoring cases is one scan fewer than any
                          other multiple sampling in place. This reduces the possibility that insects, weld
                          sparks, or other particles cause the machine to be switched off. This increases
                          machine availability. The standard response time applies from the outset in the
                          new field.
                     O    User-defined (please consult manual)
                          You can adjust the settings for multiple sampling after switching between moni-
                          toring cases in line with your requirements for the response time and reliability.
                          Regardless of the exact settings here, multiple sampling after switching between
                          monitoring cases is always at least one scan fewer than any other multiple sam-
                          pling in place: nCS ≤ n – 1




72   nanoScan3 I/O                                                                       8024596/1W27/2026-05-26 | SICK
                                                                                    SUBJECT TO CHANGE WITHOUT NOTICE

CONFIGURATION 8

                              Multiple sampling after object detection
                              The set multiple sampling also applies by default if a field becomes free again after an
                              object detection. That means, when the field is free again, the free field is scanned the
                              same number of times until the safety outputs switch back to the ON state.
                              If you activate the Activate different multiple sampling rate after object detection
                              option, you can specify deviating values for the monitoring level or for individual fields.
                              This may cause the outputs to switch back to the ON state faster or slower after a field
                              has become free again.
                              The following case is only relevant if multiple sampling or different multiple sampling
                              rate after object detection is set to a value n < 6: Regardless of whether a different
                              multiple sampling rate after object detection is set, the multiple sampling after object
                              detection will in some circumstances be increased to a value up to n = 6. This case
                              arises if an object detection lasts for a longer period, i.e. if it takes a long time until the
                              field is clear again.


8.11           Contour as Reference field
                              Overview




Figure 41: Contour as Reference field

1      Tool for drawing reference contour fields
2      Drawn contour with tolerance band
3      Contour as Reference field
4      Configure the field




8024596/1W27/2026-05-26 | SICK                                                                            nanoScan3 I/O     73
SUBJECT TO CHANGE WITHOUT NOTICE

8 CONFIGURATION

                     If you have activated the Reference contour monitoring option for a monitoring plane,
                     the Reference contour field dialog box is displayed.
                     The contour as reference field monitors a contour of the environment. The safety laser
                     scanner switches all safety outputs to the OFF state if a contour does not match the set
                     parameters, because, for example, the mounting of the safety laser scanner has been
                     changed.

                     Drawing a reference contour field

                     1.   Select the tool for drawing reference contour fields.
                     2.   First, use the mouse to click the desired contour.
                     3.   Click to add the corners of the contour.
                     4.   Finally, double-click the contour.
                     m    The reference contour field is displayed.

                     Multiple sampling and Object resolution
                     At first, the object resolution and multiple sampling configured for the monitoring plane
                     apply for all fields. If necessary, you can make changes to each individually at a later
                     date.

                     Tolerance band
                     A contour has a positive and a negative tolerance band. If the safety laser scanner does
                     not detect the contour within the tolerance band, the field switches to the OFF state.
                     O    Positive tolerance (far): The tolerance away from the safety laser scanner
                     O    Negative tolerance (near): The tolerance toward the safety laser scanner




74   nanoScan3 I/O                                                                     8024596/1W27/2026-05-26 | SICK
                                                                                  SUBJECT TO CHANGE WITHOUT NOTICE

CONFIGURATION 8

8.12             Fields
                                 Overview




Figure 42: Field editor

1      Toolbar
2      Visible spatial contour
3      Protective field (red) and warning field (yellow) created
4      Create, copy, delete field set and fields
5      Define field type, name field, configure field


                                 Using the field editor, you can configure the field sets of the safety laser scanner. The
                                 number of configurable fields depends on the safety laser scanner variant.
                                 In the Fields area, you draw the fields in a field set using the tools in the toolbar. In
                                 the Field set area, you create the field sets and fields. In the area below, you configure
                                 details for the selected field set or field.
                                 The edge length or the diameter of each field must be at least as large as the selected
                                 object resolution.
                                 You can change the sequence of the fields in the Field set area using drag and drop.
                                 The fields of a field set are displayed in the monitoring case table in the same sequence
                                 in which you create them here.




8024596/1W27/2026-05-26 | SICK                                                                           nanoScan3 I/O       75
SUBJECT TO CHANGE WITHOUT NOTICE

8 CONFIGURATION

                     Toolbar
                     Using the tools in the field editor, you can draw the fields in a field set or masked areas
                     inside the fields.
                     Table 12: Buttons on the toolbar
                                         Arrow tool, for marking objects


                                         Hand tool, for moving the work space


                                         Measuring tool for measuring distances in the Fields area

                                         Draw reference contour field or contour detection field


                                         Draw field using points


                                         Draw rectangle


                                         Draw circle


                                         Draw circle segment


                                         Mask areas. Clicking this button shows the buttons for drawing fields with a
                                         hatched display. You can then draw in areas that cannot be monitored.



                                         Enable propose field


                                         Delete selected object


                                         Object transformation. Move, rotate or mirror one or more objects in the
                                         Fields area.
                                         Editing a field using coordinates


                                         Push the object into the foreground or background


                                         Selecting the color scheme for fields
                                         If a device is selected in the field editor: Select pattern for fields
                                         Zoom in


                                         Zoom out


                                         Zoom to area


                                         Zoom to work space


                                         Show snapshot of the spatial contour. Clicking again clears the spatial con-
                                         tour shown.
                                         For a virtual group, individual devices or all devices can be selected.
                                         Show live spatial contour
                                         For a virtual group, individual devices or all devices can be selected.
                                         Selecting a color for the displayed room contour
                                         For a virtual group, the color can be selected individually for each device.
                                         Insert background image


                                         Calculate field




76   nanoScan3 I/O                                                                               8024596/1W27/2026-05-26 | SICK
                                                                                            SUBJECT TO CHANGE WITHOUT NOTICE

CONFIGURATION 8

                                                   Open the device settings


                                                   Editing grid settings



                              Field display
                              Safety Designer displays the field types in different colors.
                              Table 13: Colors of the field types
                               Protective field                     Warning field                Reference contour field and
                                                                                                 contour detection field




                               Red                                  Yellow                       Turquoise

                              Create fields and field sets
                              Table 14: Buttons for field sets
                                                   Add field set


                                                   Add field to field set


                                                   Duplicate field set


                                                   Delete field or field set


                                                   Hide or show field sets and fields


                                                   Manage field set templates


                                                   Importing field sets and fields


                                                   Exporting field sets and fields


                                                   Synchronize selection and visibility
                                                   If a field or a field set is selected or hidden or shown for the current device
                                                   and a field set of the same name exists in another device of the virtual group,
                                                   the status is transferred to the other device.

                              Name
                              You can assign a unique name for each field set.

                              Name and Field type
                              You can assign a unique name and select a field type for each field.

                              Multiple sampling and Object resolution
                              At first, the object resolution and multiple sampling configured for the monitoring plane
                              apply for all fields. If necessary, you can make changes to each individually at a later
                              date.




8024596/1W27/2026-05-26 | SICK                                                                               nanoScan3 I/O      77
SUBJECT TO CHANGE WITHOUT NOTICE

8 CONFIGURATION

                           Tolerance band
                           A contour has a positive and a negative tolerance band. If the safety laser scanner does
                           not detect the contour within the tolerance band, the field switches to the OFF state.
                           O    Positive tolerance (far): The tolerance away from the safety laser scanner
                           O    Negative tolerance (near): The tolerance toward the safety laser scanner

8.12.1         Drawing in points that cannot be monitored
                           Overview




                           Figure 43: Area that cannot be monitored

                           1      Protective field
                           2      Marked column
                           3      Area that cannot be monitored


                           The area to be monitored is scanned radially 1. For this reason, shadows 3 are formed
                           by objects in the room 2 (support columns, separator grids, etc.). The safety laser
                           scanner cannot monitor these areas.
                           You draw objects that limit the field of view of the safety laser scanner as masked areas.
                           Table 15: Mask areas
                                               Mask areas


                                               Hatched drawing tools



                           Procedure

                           1.   Click on the Mask areas tool.
                           m    The tools you can use to draw fields are shown crosshatched.
                           2.   Choose a drawing tool.
                           3.   Draw the masked area.
                           m    The masked area is shown in gray.
                           m    The field editor shows the shadowing of the masked area.




78       nanoScan3 I/O                                                                       8024596/1W27/2026-05-26 | SICK
                                                                                        SUBJECT TO CHANGE WITHOUT NOTICE

CONFIGURATION 8

8.12.2         Enable propose field
                              Overview
                              You can have a protective field or warning field suggested by Safety Designer.
                              For this purpose, the safety laser scanner scans the visible surrounding contour several
                              times. Based on the data obtained, the Safety Designer suggests the contour and size
                              of the field.
                              Table 16: Propose field
                                                  Suggest field


                              If you propose a protective field, the proposal does not replace calculation of the
                              minimum distance. You must calculate the minimum distance and check whether the
                              size of the proposed protective field is sufficient. You must also take into account the
                              measurement tolerances of the safety laser scanner.

                              Existing field geometries
                              O    Delete existing shapes: The field is redrawn according to the surrounding con-
                                   tour.
                              O    Refine existing shapes: The existing field is adapted to the surrounding contour.

                              Measurement method
                              O    Use every single distance value: Each scan of the surrounding contour is used
                                   individually to draw the field.
                              O    Use median of distance values: The median of the last 25 scans is used to draw
                                   the field.

                              Type of teach-in
                              O    Only allow reduction: The shortest measured distance is used at each angle. If
                                   you walk along the borders of the imaginary field and, for example, hold a board or
                                   cardboard into the laser beam, this restricts the surrounding contour.
                              O    Allow expansion: The surrounding contour is used as it is measured.

                              Automatic reduction
                              You can specify that the proposed field is drawn smaller than the measured surround-
                              ing contour so that the field will be at a distance from walls. The default value corre-
                              sponds to the TZ value (tolerance zone of the safety laser scanner).

                              Smoothing by point reduction
                              The proposed contour may initially be uneven and consist of very many points. With
                              the Smoothing by point reduction option, you can reduce the number of points and
                              simplify the lines.

                              Further topics
                              O    "Distance from walls", page 31

8.12.3         Object transformation
                              Overview
                              Table 17: Object transformation

                                                  Object transformation




8024596/1W27/2026-05-26 | SICK                                                                       nanoScan3 I/O       79
SUBJECT TO CHANGE WITHOUT NOTICE

8 CONFIGURATION

                           Procedure

                           1.   In the area on the left, select the objects to be transformed.
                           2.   In the area on the right, select the transformation to be performed (Shifting ,
                                Rotation or Mirroring ) and enter values for the transformation.
                           3.   In the area on the right, click on Apply to selected objects .
                           m    The configured transformation is performed in the Fields area.

8.12.4         Editing fields using coordinates
                           You can use coordinates to edit fields. Depending on the form on which a field is
                           based, the appropriate input fields are displayed. The example shows a dialog box for a
                           rectangle.




                           Figure 44: Editing fields using coordinates




80       nanoScan3 I/O                                                                       8024596/1W27/2026-05-26 | SICK
                                                                                        SUBJECT TO CHANGE WITHOUT NOTICE

CONFIGURATION 8

                              The reference points for the X and Y values are as follows:
                              O    Rectangle: top left corner
                              O    Circle: center point
                              O    Circle sector: center point
                              O    Polygon: each point individually
                              O    Contour line: each point individually

8.12.5         Background image
                              Overview
                              You can select a background image for the field editor. For example, the plan view of the
                              machine to be protected can be used as a sample.
                              The background image is saved in the project file on the computer. It is not transmitted
                              to the device.
                              Table 18: Background image
                                                  Edit background image


                              The Safety Designer supports the following file formats: BMP, JPG, PNG.

                              Procedure

                              1.   Click on Edit background image in the toolbar.
                              m    The Background image dialog box opens.
                              2.   Click on Browse ....
                              3.   Select the file for the background image.
                              m    Safety Designer displays the background image.
                              4.   If necessary, use the pipette icon to select a color of the image to make this color
                                   transparent.
                              5.   Adjust the size of the image with the scaling tool or by directly entering the dimen-
                                   sions. Use the scaling tool to move the tips of the blue arrow to two known points
                                   and then enter the distance between the points in the field.
                              6.   Enter X-Position, Y-Position and Rotation in the coordinate system of the field
                                   editor.
                                   You can then freely move or rotate the background image in the field editor.
                              7.   If necessary, click on the Lock position of the image option.
                              m    It is no longer possible to change the background image in the field editor.

8.12.6         Device Settings
                              Overview
                              Table 19: Device Settings

                                                  Device Settings


                              Field calculation
                              You specify whether the fields are calculated manually or automatically after drawing.
                              If you select the Manual option, first draw the areas to be monitored. Then click on
                              Calculate field sets so that the Safety Designer calculates the field that the safety laser
                              scanner actually monitors.
                              If you select the Automatic option, the drawn areas are immediately converted into
                              fields.




8024596/1W27/2026-05-26 | SICK                                                                       nanoScan3 I/O     81
SUBJECT TO CHANGE WITHOUT NOTICE

8 CONFIGURATION

                           Use global geometry
                           You specify whether global geometries are used.

                           Display reference contour field
                           You determine whether the reference contour field is displayed.

8.12.7         Defining global geometry
                           Overview
                           You draw field geometries and non-monitored areas as global geometry. The global
                           geometry affects all protective fields and warning fields.

                           Procedure

                           1.    Click on the Device Settings tool.
                           2.    Activate the Use global geometry checkbox.
                           3.    In the Field set area, select > Global Geometry.
                           4.    Draw a global field geometry.
                           5.    If applicable, draw non-monitored areas with the Mask areas tool.

8.12.8         Grid Settings
                           Overview
                           Table 20: Settings for the field editor

                                                Grid Settings


                           Drawing surface
                           You can use a Cartesian or a polar coordinates system and select the colors for the grid,
                           the labels, and the drawing area.

8.12.9         Creating field set templates
                           Overview
                           If you require the same combination of fields a number of times, you can create a field
                           set template.
                           Table 21: Manage field set templates

                                                Manage field set templates


                           Procedure

                           1.    Click on Add field set template .
                           2.    Enter the name for the template.
                           3.    Define the number of fields.
                           m     A selection field is shown for each field.
                           4.    Select the Field types for the fields.
                           5.    Enter the Field names.
                           6.    Click on Apply.
                           m     The field set template is saved.




82       nanoScan3 I/O                                                                      8024596/1W27/2026-05-26 | SICK
                                                                                       SUBJECT TO CHANGE WITHOUT NOTICE

CONFIGURATION 8

8.12.10        Importing and exporting field sets and fields
                              Overview
                              If you need identical field sets or fields across different projects, you can export entire
                              field sets or individual fields out of one project and import them into another project.

                              Importing field sets and fields

                              1.   Click on Import fields and field sets.
                              2.   Select exported file with field set information.
                              m    A preview of the field sets and fields saved in the file will be shown.
                              3.   Select the required field sets and fields.
                              4.   Start the import.
                              m    The field sets and fields will be imported.

                              Exporting field sets and fields

                              1.   Click on Export fields and field sets.
                              2.   Select the relevant folder and enter a file name for storing the field set information.
                              3.   Select the required field sets and fields.
                              4.   Start the export.
                              m    The field sets and fields will be exported.

8.12.11        Virtual group
                              Overview
                              If you are configuring several safety laser scanners in a project, you can combine these
                              safety laser scanners into a virtual group. You can then edit the fields for these safety
                              laser scanners in a single field editor. A virtual group can be useful if the safety laser
                              scanners have been mounted on the same level and are arranged in a common world
                              coordinate system.
                              You need a license to use this function.
                              Table 22: Virtual group
                                                  Manage devices


                                                  Show/hide device and field decomposition


                                                  Change to device window



                              Creating a virtual group

                              1.   Click on Manage devices.
                              2.   Activate the devices to be included in the virtual group.
                              3.   Click OK to confirm.
                              m    The devices in the virtual group are displayed at the bottom of the field editor.

                              Editing devices and associated fields in the field editor

                              1.   Click on the desired device at the bottom of the field editor.
                              2.   Edit the device and the associated fields in the field editor as usual.

                              Hiding or showing devices and associated fields in the field editor

                              1.   Click on Show/hide device and field decomposition next to the desired device.
                              m    If the device was previously visible in the field editor, it will be hidden.
                              m    If the device was previously hidden in the field editor, it will now be shown.



8024596/1W27/2026-05-26 | SICK                                                                         nanoScan3 I/O    83
SUBJECT TO CHANGE WITHOUT NOTICE

8 CONFIGURATION

                              Switching to another device window in the virtual group

                              1.       Click on Change to device window next to the desired device.
                              m        The device window of the desired device opens in the foreground.

                              Complementary information
                              For information on licenses, see the Safety Designer operating instructions.


8.13           Inputs and outputs, local
                              Overview




Figure 45: Inputs and outputs, local

1      Overview: Plug connectors of the safety laser scanner
2      Pin assignment
3      Available signals
4      Remove signal from connection
5      Further settings for some signals


                              Assign the required signals to the safety laser scanner connection in the Inputs and
                              outputs, local dialog box.

                              Connection overview
                              Safety Designer shows the safety laser scanner’s plug connectors and flying leads in
                              the center of the dialog box.



84       nanoScan3 I/O                                                                           8024596/1W27/2026-05-26 | SICK
                                                                                            SUBJECT TO CHANGE WITHOUT NOTICE

CONFIGURATION 8

                              Pin assignment
                              The Safety Designer shows the plug connectors with the individual pins and the individ-
                              ual wires of the flying leads.

                              Signals
                              Safety Designer shows the available signals on the right under Signals.
                              You can assign the desired signals to the individual pins or wires via drag-and-drop.
                              You can cancel the assignment by dragging a signal from a pin or wire onto the trash
                              can icon.

                              Properties
                              Under Properties, you will find further adjustment options depending on the signals
                              used.

8.13.1         Outputs
                              OSSD
                              Dual-channel, safety switching output which is used to switch off the dangerous state.

                              Contamination
                              Signals that the optics cover is contaminated.

                              Error
                              Signals an error.

                              Reset required
                              Signals that a reset is possible. A connected lamp lights up if the restart interlock has
                              been triggered and the protective field is then clear again.

                              Monitoring result
                              Indicates the status of the active field. A connected lamp lights up if an object is
                              detected in the field.

                              Reset required (flashing)
                              Signals that a reset is possible. A connected lamp flashes if the restart interlock has
                              been triggered and the protective field is then clear again.

8.13.2         Inputs
                              Static control input
                              Signal of the machine controller for switching between monitoring cases.

                              Dynamic control input
                              For connecting an incremental encoder for speed-dependent switching between moni-
                              toring cases.

                              External device monitoring (EDM)
                              Signal from the auxiliary contacts of the positively guided contactors for external device
                              monitoring (EDM).




8024596/1W27/2026-05-26 | SICK                                                                        nanoScan3 I/O     85
SUBJECT TO CHANGE WITHOUT NOTICE

8 CONFIGURATION

                           Reset
                           Signal from the reset pushbutton to manually reset the internal restart interlock.

                           Sleep mode
                           Signal from a pushbutton to activate sleep mode.

                           Restart device
                           Signal from a pushbutton to completely restart the device.

                           Pause event recording
                           Signal of a pushbutton to stop the event history.

                           Further topics
                           O    "Static control inputs", page 44

8.13.3         Further settings for some signals
                           Safety Designer shows the setting options for some signals under Properties at the
                           bottom right.

                           Restart interlock for the OSSD pair
                           The safety laser scanner has the following options for the restart interlock behavior
                           for the OSSDs:
                           O     Immediate restart without restart interlock: If there is no longer an object in the
                                 protective field, the safety laser scanner switches the OSSDs to the ON state.
                           O    Restart interlock, reset required by input signal: If the operator activates the
                                restart or reset control switch, the safety laser scanner switches the OSSDs to the
                                ON state.
                           O    Automatic restart after:: If there is no longer an object in the protective field,
                                the safety laser scanner switches the OSSDs to the ON state after the configured
                                delay.

                           Activate external device monitoring (EDM)
                           An input must be configured for external device monitoring (EDM). This input must be
                           correctly connected to the electric control (see "External device monitoring (EDM)",
                           page 49).
                           If external device monitoring is activated, the safety laser scanner checks whether
                           voltage is applied at the external device monitoring (EDM) input after the OSSDs have
                           been switched off.
                           If no voltage is applied at the input after the OSSDs have been switched off, the safety
                           laser scanner changes to the locking state and does not switch the OSSDs back to the
                           ON state.

                           Signal level
                           For some non-safe output signals, you can select whether the signal is output with
                           HIGH or with LOW:
                           O    Setting Hi: The output is normally in LOW state. If the signal is active, the output
                                switches to HIGH state.
                           O    Setting Lo: The output is normally in HIGH state. If the signal is active, the output
                                switches to LOW state.




86       nanoScan3 I/O                                                                         8024596/1W27/2026-05-26 | SICK
                                                                                          SUBJECT TO CHANGE WITHOUT NOTICE

CONFIGURATION 8

                              Error
                              O    Device error setting: Device errors are serious errors where all safety outputs
                                   switch to the OFF state and the device switches to the locking state. Once the
                                   cause of the error has been rectified, the device must be completely restarted.
                              O    Application error setting: In the event of an application error, all safety outputs
                                   switch to the OFF state. Once the cause of the error has been rectified, the safety
                                   function must be restarted.

                              Contamination
                              O    Switch when Contamination Warning is present. Device is in ON state, but
                                   partial contamination on the optics cover is detected. setting: The optics cover
                                   should be cleaned soon.
                              O    Switch when Contamination Error is present. Device is in OFF state due to
                                   contamination of the optics cover. setting: All safety outputs in the OFF state. The
                                   optics cover is severely contaminated and must be cleaned immediately.

                              Speed
                              For dynamic inputs, you must specify for each incremental encoder how many pulses it
                              outputs per distance traveled.
                              For dynamic inputs, you must also specify the tolerance by which the measured speeds
                              of the two incremental encoders are allowed to deviate from one another, e.g., when
                              cornering. The value is given as a percentage of the higher of the two speeds (whether
                              forwards or backwards). In case of differences, the speed with the higher value is always
                              used. The tolerance is allowed to be exceeded for a certain period of time. The safety
                              laser scanner then switches the safety outputs to the OFF state.
                              The period of time depends on the vehicle speed:
                              O   Vehicle speed -10 cm/s … +10 cm/s: No shut-off, no matter how large the deviation
                                  between the measured speeds is.
                              O    Vehicle speed -30 cm/s … -10 cm/s or +10 cm/s … +30 cm/s: The tolerance is
                                   allowed to be exceeded for a maximum of 60 seconds.
                              O    Vehicle speed ≤ -30 cm/s or ≥ +30 cm/s: The tolerance is allowed to be exceeded
                                   for a maximum of 20 seconds.
                              O    Vehicle speed in the range ≤ -10 cm/s or ≥ +10 cm/s: Different directions of
                                   rotation of the incremental encoders are tolerated for a maximum of 0.4 s.




8024596/1W27/2026-05-26 | SICK                                                                      nanoScan3 I/O    87
SUBJECT TO CHANGE WITHOUT NOTICE

8 CONFIGURATION

8.14             Monitoring cases
                                 Overview




Figure 46: Monitoring cases

1        Add monitoring case table
2        Settings for the whole monitoring case table
3        Settings for the individual monitoring case
4        Input conditions for a monitoring case
5        Field set in the monitoring case and in the cut-off path
6        Cut-off paths
7        Configured field sets
8        Areas for defined cut-off behavior
9        Remove field set from a monitoring case


                                 In the monitoring case editor, you can also define the monitoring cases with input
                                 conditions and assign the field sets.

8.14.1           Settings for monitoring case tables
                                 Name
                                 In the Name field, you can enter a meaningful name for the monitoring case table.




88         nanoScan3 I/O                                                                          8024596/1W27/2026-05-26 | SICK
                                                                                             SUBJECT TO CHANGE WITHOUT NOTICE

CONFIGURATION 8

                              Inputs used
                              You choose the inputs that you would like to use for switching between monitoring
                              cases in the monitoring case table.

                              Input delay
                              In the Input delay field, you can select a delay for the inputs.
                              If your control device, which you use to switch the static control inputs, cannot switch
                              to the appropriate input condition within 12 ms (for example because of the switch’s
                              bounce times), you must configure an input delay. The selected input delay must be
                              large enough to allow your control device to switch to the new input condition within this
                              time.
                              Table 23: Empirical values for the required input delay
                               Switchover method                                                    Required input delay
                               Electronic switching via control, complementary electronic outputs   12 ms
                               with 0 ms to 12 ms bounce time
                               Tactile controls (relays)                                            30 ms to 150 ms
                               Control via independent sensors                                      130 ms to 480 ms

                              Use speed
                              If you want to use the speed for monitoring case switching or as an additional condition,
                              activate this option.

                              Importing and exporting monitoring case tables
                              If you need identical monitoring case tables across different projects, you can export
                              monitoring case tables out of one project and import them into another project.

                              Further topics
                              O     "Monitoring case switching time", page 26
                              O     "Static control inputs", page 44

8.14.1.1       Configure switching sequence
                              Overview
                              You can specify the order in which the monitoring cases can be called.
                              You can specify one or two subsequent monitoring cases for each monitoring event.
                              If you do not specify a subsequent monitoring case for a monitoring case, then any
                              monitoring case may follow.
                              If input conditions are present that do not call up any of the defined subsequent moni-
                              toring cases, the safety laser scanner switches all safety outputs to the OFF state.
                              You can specify the order of the monitoring cases as a process or in individual steps.

                              Process
                              You define one or more sequences. You can use a sequence to map the sequence of
                              work steps for your machine.
                              In all sequences, you can define a maximum of two subsequent monitoring cases for
                              each monitoring case.
                              If you do not specify a subsequent monitoring case for a monitoring case, then any
                              monitoring case may follow.




8024596/1W27/2026-05-26 | SICK                                                                              nanoScan3 I/O   89
SUBJECT TO CHANGE WITHOUT NOTICE

8 CONFIGURATION

                           Individual steps
                           You define individually for each monitoring case which one or two monitoring cases
                           may follow.
                           If you do not specify a subsequent monitoring case for a monitoring case, then any
                           monitoring case may follow.

                           Complementary information
                           You can use the changeover order as an additional check of your control unit. For exam-
                           ple, deviations of a vehicle from the route or a plant from the prescribed production
                           process can be detected.

8.14.2         Several monitoring case tables
                           Certain variants of the safety laser scanner support multiple simultaneous monitoring
                           case tables. For example, you can use a monitoring case table to switch between differ-
                           ent monitoring cases with different field sets. At the same time, you can use another
                           monitoring case table to keep a monitoring case always active with a particular field set.
                           Even if you use several monitoring case tables, each shutdown path is assigned to only
                           one monitoring case table.
                           If you use several monitoring case tables, one monitoring case must be active in each
                           monitoring case table at all times. As long as no monitoring case is active in a monitor-
                           ing case table after the start, all outputs remain in the OFF state and the device displays
                           Waiting for inputs. If no monitoring case is active in a monitoring case table during
                           operation, all outputs switch to the OFF state and the device displays an error.

8.14.3         Settings for monitoring cases
                           Name
                           In the Name field, you can enter a meaningful name for the monitoring case. If you
                           create a lot of monitoring cases, you should consider a naming concept that makes
                           it possible to identify the monitoring cases easily (for example right cornering, left
                           cornering).

                           Sleep mode
                           If you activate this option, the safety laser scanner changes to the sleep mode as soon
                           as the input conditions for this monitoring case exist.

8.14.4         Input condition
                           For each monitoring case, you choose the input conditions for which the monitoring
                           case will be activated. The relevant monitoring case is activated for exactly this combi-
                           nation.
                           Combinations which are invalid or already assigned are marked.

                           Speed
                           O     Range: The monitoring case is activated if the speed is within the specified range.
                                 You can use static control inputs as additional input conditions.
                           O     Limit: The monitoring case is activated via the static control inputs. The safety
                                 laser scanner monitors the speed. If the speed is outside the specified range, the
                                 safety laser scanner switches the safety outputs to the OFF state.
                                 In this mode, the safety laser scanner ignores different speeds of the two incre-
                                 mental encoders for 60 seconds, even if the difference is greater than the config-
                                 ured tolerance.



90       nanoScan3 I/O                                                                        8024596/1W27/2026-05-26 | SICK
                                                                                         SUBJECT TO CHANGE WITHOUT NOTICE

CONFIGURATION 8

                              Complementary information
                              The Generate input conditions from case numbers function allows you to automati-
                              cally assign input conditions to monitoring cases.

8.14.5         Cut-off paths
                              Overview
                              You can create cut-off paths and define the outputs switched by the cut-off paths.
                              You need a cut-off path for every field in a field set. If the field sets have different sizes,
                              use the field set with the most fields as a guide.

                              Cut-off path
                              You can enter a meaningful name for each shutdown path.

                              Outputs
                              A cut-off path can switch safety outputs and non-safety outputs.
                              You select the outputs that the cut-off path should switch:
                              O    OSSDs
                              O    Universal outputs

8.14.6         Assigning field sets
                              Overview
                              The field sets that have been created are listed in the Field sets area.

                              Procedure

                              Assign a field set to a monitoring case
                              →   Assign a field set to a monitoring case using drag and drop.
                              m   The fields in a field set are arranged as they were drawn in the field editor.

                              Splitting a field set into a monitoring case
                              1.   Assign a field set to a monitoring case using drag and drop.
                              2.   Right click on the assigned field set and select Split fieldset.
                              3.   Assign the individual fields to one or various monitoring cases.

                              Assigning a field to a monitoring case
                              1.  Click on De-/activate single-drag of fields in the toolbar.
                              m   Every field in the field sets is highlighted with a frame.
                              2.  Click on either a field set or an individual field and assign it to a monitoring case
                                  using drag and drop.

                              Removing assignment
                              →  Drag a field set or field from a monitoring case onto the trash can icon.




8024596/1W27/2026-05-26 | SICK                                                                            nanoScan3 I/O     91
SUBJECT TO CHANGE WITHOUT NOTICE

8 CONFIGURATION

8.14.7           Assigning a defined cut-off behavior
                              Overview
                              In a monitoring case, you can assign a defined cut-off behavior to a cut-off path
                              instead of a field:
                              O    Always OFF: If the monitoring case becomes active, the cut-off path is always in
                                   the OFF state.
                              O    Always ON (NON-safe): If the monitoring case becomes active, a safety output in
                                   the cut-off path is always in the OFF state. A non-safety output is always in the ON
                                   state.
                              O    Always ON (safe): If the monitoring case becomes active, the cut-off path is in the
                                   ON state.

                              Procedure

                              Assigning a defined cut-off behavior
                              →   Assign a cut-off behavior to a cut-off path in a monitoring case using drag-and-
                                  drop.

                              Complementary information
                              If you have not assigned fields to certain cells in a monitoring case table, Safety
                              Designer automatically assigns the Always OFF function to these cells.

8.14.7.1         Configuring the default settings for defined cut-off behavior
                              Overview
                              With this function, you can define specified cut-off behaviors per cut-off path as default
                              settings for monitoring cases.
                              Table 24: Show/hide preset for specified cutoff behavior
                                                  Show/hide preset for specified cutoff behavior



                              Procedure

                              1.   Select Show/hide preset for specified cutoff behavior.
                              m    Safety Designer displays an additional line in the monitoring case table.
                              2.   Assign a cut-off behavior to a cut-off path in the Preset for specified cutoff
                                   behavior cell using drag and drop.
                              m    Safety Designer applies the default settings when you add a new monitoring case.




92         nanoScan3 I/O                                                                                8024596/1W27/2026-05-26 | SICK
                                                                                                   SUBJECT TO CHANGE WITHOUT NOTICE

CONFIGURATION 8

8.15           Simulation
                              Overview




Figure 47: Simulation

1      Show or hide field types
2      Simulation tools
3      Select input conditions
4      Display the cut-off paths


                              You can visualize the result of the set configuration in the simulation.

                              Simulation components and options
                              O    Display the status of the cut-off paths
                              O    Feedback about which monitoring case is active for the selected input sample
                              O    You can switch inputs, monitoring cases, etc. virtually using symbols and observe
                                   the result.
                              O    You can simulate an object detection in a field and check the result.
                              O    You can move fields to the foreground or to the background using the context
                                   menu (right mouse button).




8024596/1W27/2026-05-26 | SICK                                                                           nanoScan3 I/O   93
SUBJECT TO CHANGE WITHOUT NOTICE

8 CONFIGURATION

8.16           Data output
                             Overview




Figure 48: Data output

1      Data output channel
2      Send mode
3      Data content
4      Angular range


                             Data output can be used for general monitoring and control tasks. This data is used
                             in particular for providing navigation support for AGVs (automated guided vehicles).
                             This data is not intended for use in safety-related applications. If the data output is to
                             be used in safety functions, the user must define and implement additional required
                             measures.

                             Data output channel
                             Every data output channel has independent settings.




94       nanoScan3 I/O                                                                           8024596/1W27/2026-05-26 | SICK
                                                                                            SUBJECT TO CHANGE WITHOUT NOTICE

CONFIGURATION 8

                              Send Mode
                              O    Deactivated: No data output
                              O    On request: Data is output when there is an explicit request from a host computer
                                   via TCP/IP using CoLa 2
                              O    On request and also continuously to a target computer (router settings made
                                   via “Network settings”): Data is output continuously via UDP to a defined target
                                   address and also when there is an explicit request from a host computer via
                                   TCP/IP using CoLa 2

                              Selection data content
                              O    Block "Device Status": Information on the status of the safety laser scanner (e.g.,
                                   cut-off paths, errors)
                              O    Block "Configuration of Data Output": Information on the actual angle range used
                                   (due to technical conditions, data may be output from a slightly larger angle range
                                   than the set angle range)
                              O    Block "Measurement Data" *: Distance data with reflector detection and RSSI
                              O    Block "Object detection" *: Data on the beams in the fields of the active monitor-
                                   ing case in which an object was detected
                              O    Block "Application Data": State of the inputs and outputs used in the monitoring
                                   case table
                              O    Block "Local I/Os": State of the local inputs and outputs

                              Angular range
                              You define in which range measurement data and data on detections in fields are
                              output.

                              Complementary information
                              For more information on data output, see the technical information “microScan3, out-
                              doorScan3, nanoScan3: Data output via UDP and TCP/IP” (part number 8022706).


8.17           Transferring a configuration
                              Overview
                              A configuration is first saved in your Safety Designer project as a configuration file. You
                              transfer the configuration to the connected device.
                              At the left, you see the values configured in the project for the device. If the device is
                              connected, you see the values saved in the device at the right.
                              The compatibility of the configuration is checked during transmission. An existing con-
                              figuration on the device is overwritten.

                              Procedure

                              1.   Check the configuration carefully before transmission.
                              2.   Click on Identify the device to ensure that the desired device is connected.
                              m    The display of the connected device flashes blue.
                              3.   If the checksums on the computer and the device differ, click on Transfer to
                                   device.
                              m    The transmission process is shown in Safety Designer and on the device.
                              m    Safety Designer will notify you as soon as the transfer process is complete.

                              Further topics
                              O    "Verify configuration", page 96




8024596/1W27/2026-05-26 | SICK                                                                          nanoScan3 I/O      95
SUBJECT TO CHANGE WITHOUT NOTICE

8 CONFIGURATION

8.17.1         Verify configuration
                            Overview
                            By verifying the configuration, you can confirm that the configuration complies with the
                            planned safety function and fulfills the requirements in the risk assessment.
                            During verification, Safety Designer reads back the configuration transferred to the
                            device. It compares the configuration with the configuration saved in Safety Designer. If
                            both configurations are identical, Safety Designer displays the verification report. If the
                            user confirms that this is correct, the system is considered to be verified.

                            Important information

                            DANGER
                            Hazard due to lack of effectiveness of the protective device
                            Errors can occur when transferring the configuration to the device, e.g., due to environ-
                            mental influences or faulty cables. The verification report always contains exactly the
                            settings that are stored in the device.

                            →    Before confirming, check the verification report carefully.


                            Prerequisites
                            O    The configuration corresponds to the planned safety function and meets the
                                 requirements of the risk assessment.
                            O    The configuration has been transferred to the device.

                            Procedure

                            1.   Click on Verify.
                            m    Safety Designer displays the verification report.
                            2.   Thoroughly review the verification report.
                                 →     If the verification report does not match the planned safety function, click on
                                       Cancel, correct the configuration and start again from step 1.
                                 →    If the verification report matches the planned safety function, click on OK.
                            m    Device configuration is shown as verified.

                            Complementary information
                            If the configuration is verified, the device automatically starts the safety function after
                            switching on the voltage supply.
                            If the configuration is not verified, the device may not be operated as a protective
                            device. You can start the safety function manually to test the device and the configura-
                            tion. The test operation has a time limit.

                            Further topics
                            O    "Starting and stopping safety function", page 97

8.17.2         Transferring a verified configuration
                            Overview
                            No additional verification in Safety Designer is required after transferring a verified
                            configuration. The thorough check during commissioning, however, still needs to be
                            performed as in all other cases.

                            Procedure

                            1.   Click on Identify the device to ensure that the desired device is connected.


96       nanoScan3 I/O                                                                           8024596/1W27/2026-05-26 | SICK
                                                                                            SUBJECT TO CHANGE WITHOUT NOTICE

CONFIGURATION 8

                              m    The display of the connected device flashes blue.
                              2.   If the checksums on the computer and the device differ, click on Transfer to
                                   device.
                              m    The transmission process is shown in Safety Designer and on the device.
                              m    Safety Designer displays the verification report.
                              3.   Click on OK.
                              m    Device configuration is shown as verified.


8.18           Starting and stopping safety function
                              Overview
                              In some situations, for example tests during commissioning, you can start or stop the
                              safety function manually.

                              Procedure

                              Start safety function
                              →
                                   Click on the     button.

                              Stop the safety function
                              →
                                  Click on the     button.




8024596/1W27/2026-05-26 | SICK                                                                     nanoScan3 I/O      97
SUBJECT TO CHANGE WITHOUT NOTICE

8 CONFIGURATION

8.19           Report
                                Overview




Figure 49: Report

1      Contents of the report
2      Composition of the report


                                A report shows the settings and data of a device. You have the option of saving and
                                archiving these data as a PDF.

                                Report
                                When you open the Report dialog box, the Safety Designer creates a report. If you
                                click on Update after making changes to the configuration, you will receive an updated
                                report.

                                Composition of the report
                                You can assemble the contents of the report as required.

                                Complementary information
                                National and international standards promote or recommend specific data and the
                                person responsible for it. The required data are included in the report.




98       nanoScan3 I/O                                                                           8024596/1W27/2026-05-26 | SICK
                                                                                            SUBJECT TO CHANGE WITHOUT NOTICE

CONFIGURATION 8

8.20           Service

8.20.1         Restart device
                              If you have problems with the device, you can restart the device or subsections of the
                              device (safety function, connections, additional functions).

                              Restarting safety function
                              O    The fastest type of restart
                              O    Serious errors remain, even if the cause has been rectified (for example a locking
                                   state because of a supply voltage which is too low).
                              O    Communication with the device remains intact (connections for configuration,
                                   safety function and data not relating to safety).
                              O    Communication beyond the device is not impaired.

                              Restarting safety function and connections
                              O    The device’s function is also re-established after serious errors if the cause has
                                   been rectified.
                              O    Communication with the device is interrupted (connections for configuration,
                                   safety function and data not relating to safety). The device sets up communication
                                   again automatically after restarting.
                              O    Communication beyond the device is not impaired.

                              Restarting device completely
                              O    The device behaves exactly as it does when the voltage supply is switched off and
                                   back on again.
                              O    The device’s function is also re-established after serious errors if the cause has
                                   been rectified.
                              O    Communication with the device is interrupted (connections for configuration,
                                   safety function and data not relating to safety).
                              O    Communication beyond the device is interrupted. This may also affect devices
                                   which communicate beyond the device.

8.20.2         Resetting to factory settings
                              Overview
                              Before reconfiguring the device, you can reset all settings to factory settings.

                              Resetting safety function to factory settings
                              O    The configuration for the safety function is reset to factory settings.
                              O    Communication beyond the device is not impaired.

                              Resetting safety function and communication settings to factory settings
                              O    The configuration for the safety function is reset to factory settings.
                              O    The configuration of device communication is reset to factory settings (connec-
                                   tions for configuration, safety function and data not relating to safety).

                              Resetting complete settings to factory settings
                              O    The configuration for the safety function is reset to factory settings.
                              O    The configuration of device communication is reset to factory settings (connec-
                                   tions for configuration, safety function and data not relating to safety).




8024596/1W27/2026-05-26 | SICK                                                                         nanoScan3 I/O    99
SUBJECT TO CHANGE WITHOUT NOTICE

8 CONFIGURATION

                         O    The Maintenance, Authorized client and SICK-service user groups are deacti-
                              vated.
                         O    The password of the Administrator user group is reset to the factory settings.

8.20.3         Managing passwords
                         Assigning or changing passwords

                         1.   Establish connection to the device.
                         2.   In the device window under Service, select the User password entry.
                         3.   In the User password dialog box, select the user group.
                         4.   Enter the new password twice and confirm with Transfer to device.
                         5.   When you are prompted to log on, select your user group and enter the corre-
                              sponding password.
                         m    The new password is valid for the user group immediately.

                         Reset password
                         If you have forgotten the password of the Administrator user group, you can reset it
                         with the assistance of SICK.

                         1.   Request the form for resetting your password from SICK support.
                         2.   Connect to the device in Safety Designer.
                         3.   In the device window under Service, select the User password entry.
                         4.   In the User password dialog box, select the Start process for resetting the
                              password option.
                         5.   Send the information displayed on the form to SICK support.
                         m    You will then receive an activation code.
                         6.   If the device is connected via network: On the display of the device in the relevant
                              menu, allow the resetting of the password by pressing the OK pushbutton.
                         7.   Enter and confirm the activation code in the field provided in Safety Designer.
                         m    The password of the Administrator user group is reset to factory settings
                              (SICKSAFE). The Maintenance and Authorized client user groups are deactivated.
                              The configuration is not changed.

8.20.4         Access management
                         Overview
                         You can activate or deactivate interfaces and selected functions as needed.
                         In the Projected device area, you can see the settings in the project.
                         When a device is connected, you can see in the Physical device area the configuration
                         in the device and the status describing the actual behavior of the device.
                         Older devices may not support all settings.

                         Functions and settings
                         You can activate, deactivate or select the default setting for each function displayed.
                         The default setting depends on the device and its range of functions.
                         Safety Designer displays the minimum functionality that the device must have to sup-
                         port the setting.

                         Behavior if the "deactivated" setting is not supported by the device or replacement
                         device:
                         It may happen that settings are stored in the system plug that the device cannot evalu-
                         ate, e.g., because a device has been replaced by an older device. You can set how the
                         device should behave in this case.



100      nanoScan3 I/O                                                                     8024596/1W27/2026-05-26 | SICK
                                                                                      SUBJECT TO CHANGE WITHOUT NOTICE

CONFIGURATION 8

                                 Older devices ignore all settings in this window. Safety Designer shows up to which
                                 functional range the settings are ignored.

8.20.4.1       Functions and settings
                                 Device restart (without network) via device display
                                 You can specify whether the device can be restarted using the pushbuttons on the
                                 display.

                                 Ethernet (generic): Port 1 3)
                                 You can activate or deactivate the network connection.

                                 Configuration and diagnostic service: Ethernet (generic)
                                 The CoLa 2 interface enables device configuration and diagnostics with Safety
                                 Designer via network. For information on further functions of the CoLa 2 interface, refer
                                 to the technical information “microScan3, outdoorScan3, nanoScan3: Data output via
                                 UDP and TCP/IP” (part number 8022706).
                                 As soon as the interface is deactivated, no new connections can be established. An
                                 existing connection remains open until it is closed or the timeout expires.

8.20.5         Optics cover calibration
                                 Overview
                                 After replacing an optics cover, the measurement system of the safety laser scanner
                                 must be calibrated to the new optics cover. During optics cover calibration, the refer-
                                 ence for the contamination measurement of the optics cover is defined (status = not
                                 contaminated).

                                 Important information

                                 WARNING
                                 Poor calibration of the measurement system for the optical properties of the optics
                                 cover
                                 The measurement system of the safety laser scanner must be calibrated for the specific
                                 optics cover. If optics cover calibration is not done correctly, persons and parts of the
                                 body to be protected may not be detected.

                                 →     Carry out an optics cover calibration with the Safety Designer every time the optics
                                       cover is replaced.
                                 →     Carry out the optics cover calibration at room temperature (10 °C to 30 °C).
                                 →     Only carry out the optics cover calibration using a new optics cover.
                                 →     Before the optics cover calibration switch on the device for a few minutes to warm
                                       up the internal components.
                                 →     Make sure that the entire system is clear of contamination when the adjustment is
                                       carried out.


                                 Procedure

                                 1.    Before the optics cover calibration, switch on the device for a few minutes to warm
                                       up the internal components.
                                 2.    In the Exchange column, click on Yes.
                                 3.    Check that the optics cover is clean.
                                 4.    In the Check cleanliness column, click on OK.

3)   The network connection is available for certain system plugs.



8024596/1W27/2026-05-26 | SICK                                                                          nanoScan3 I/O   101
SUBJECT TO CHANGE WITHOUT NOTICE

8 CONFIGURATION

                          5.   In the Optical cover calibration column, click on Start.
                          m    The calibration process starts. Typically, this process can take up to a minute. A
                               progress bar shows the progress.
                          6.   Do not switch off the safety laser scanner and do not disrupt the connection
                               between the computer and the safety laser scanner during the adjustment.
                          m    The end of the calibration is shown.

8.20.6         Compare configuration
                          Overview
                          You can use this function to compare the current configuration in the project with a
                          previously exported configuration or the configuration in the device.
                          Exported configurations are stored in their own format: “.sdsc”. You can export a con-
                          figuration under Service > Compare configurations in the Current configuration of
                          project area in the project.
                          Table 25: Buttons
                           Button                     Description
                                                      Current configuration of project area:
                                                      Exports the current configuration in the “.sdsc” format for another
                                                      comparison
                                                      Comparison data area:
                                                      Exports the comparison configuration in the “.sdsc” format
                                                      Via the comparison table:
                                                      Exports the comparison result
                                                      Imports the configuration file in the “.sdsc” format


                                                      Identifying the device


                                                      Reads the configuration from the device


                                                      Updates the configuration comparison



                          Prerequisites
                          O    The configuration export contains only one device.
                          O    Type code of the device is identical in both configurations.
                          O    Version number of the range of functions in the project is equal to or higher than
                               the configuration to be compared with.

                          Procedure

                          1.   In the navigation menu of the device window, navigate to Service > Compare
                               configurations.
                          m    The Safety Designer shows the current device configuration at the top left of the
                               workspace.
                          2.   Reading in comparison data:
                               o     Reading a configuration from the device: Open the drop-down menu next to
                                     the device symbol and select Read from Device.
                               o     Importing a configuration file: Select and import a previously exported config-
                                     uration file using Import data.
                               o     Use the current configuration in the project: Select Use comparison data.
                          m    The Safety Designer starts the configuration comparison and displays the results
                               in a table in the workspace.




102      nanoScan3 I/O                                                                           8024596/1W27/2026-05-26 | SICK
                                                                                            SUBJECT TO CHANGE WITHOUT NOTICE

CONFIGURATION 8

                              3.   If necessary, export the comparison result as a .csv file using Export result via the
                                   comparison table.

                              Importing comparison data
                              You can use the Import button to apply all settings of the comparison data to the
                              current configuration if the version number of the range of functions is identical in both
                              configurations.
                              You need a license to use this function.
                              For information on licenses, see the Safety Designer operating instructions.

8.20.7         Import / Export
                              Overview
                              You can use this function to export the current configuration in the project or import a
                              previously exported configuration.
                              Exported configurations are stored in their own format: “.sgexml”.
                              When importing using Import, you can select in detail which parts of the configuration
                              to import.
                              When exporting using Export, you can select in detail which parts of the configuration
                              to export.




8024596/1W27/2026-05-26 | SICK                                                                        nanoScan3 I/O   103
SUBJECT TO CHANGE WITHOUT NOTICE

9 COMMISSIONING

9           Commissioning
9.1         Safety
                        Important information

                        WARNING
                        Dangerous state of the machine
                        The machine or the protective measure may not yet behave as you have planned
                        When changes are made to the machine, the effectiveness of the protective measure
                        may be affected unintentionally.

                        →    Before commissioning the machine, make sure that the machine is first checked
                             and released by qualified safety personnel.
                        →    Only operate the machine with a perfectly functioning protective device.
                        →    Check the effectiveness of the protective measure after each change to the
                             machine, the integration or the operating and boundary conditions of the safety
                             laser scanner. Perform commissioning again.


9.2         Overview
                        Prerequisites
                        O    Project planning has been completed.
                        O    Mounting is complete.
                        O    Electrical installation is completed.
                        O    Configuration is completed.
                        O    No-one is in the hazardous area during commissioning.

                        Further topics
                        O    "Project planning", page 21
                        O    "Mounting", page 54
                        O    "Electrical installation", page 56
                        O    "Configuration", page 61

9.3         Alignment
                        Overview
                        Various options are available for precisely aligning the safety laser scanner depending
                        on the mounting kit that is used.

                        Procedure

                        1.   Align the safety laser scanner.
                        2.   Tighten the screws to the specified tightening torque.
                        3.   Check alignment.


9.4         Switching on
                        After switching on, the safety laser scanner performs various internal tests. The OFF
                        LED illuminates continually. The ON LED is off.
                        When the start procedure is complete, the status LEDs and the display show the current
                        operational status of the safety laser scanner.




104   nanoScan3 I/O                                                                        8024596/1W27/2026-05-26 | SICK
                                                                                      SUBJECT TO CHANGE WITHOUT NOTICE

COMMISSIONING 9

                              Further topics
                              O    "Troubleshooting", page 118

9.5            Check during commissioning and modifications
                              The thorough check is intended to ensure that the safety functions are fulfilling their
                              planned purpose and whether persons are being adequately protected.

                              →    Carry out the checks specified in the test plan of the manufacturer of the machine
                                   and the operating entity.




8024596/1W27/2026-05-26 | SICK                                                                       nanoScan3 I/O      105
SUBJECT TO CHANGE WITHOUT NOTICE

10 OPERATION

10           Operation
10.1         Safety

                       NOTE
                       This document does not provide instructions for operating the machine in which the
                       safety laser scanner is integrated.


10.2         Regular thorough check
                       The thorough check is intended to ensure that the safety functions are fulfilling their
                       planned purpose and whether persons are being adequately protected.

                       →       Carry out the checks specified in the test plan of the manufacturer of the machine
                               and the operating entity.


10.3         Status indicators




                                                    1 23



                           6

                                                              54


                       Figure 50: Display elements

                       1        LED ON status
                       2        LED OFF status
                       3        LED restart interlock/warning field
                       4        Display
                       5        Network LED
                       6        Button


                       Table 26: Status LEDs
                        Number               Function            Color         Meaning
                        1                    ON state            Green         Lights up green when at least one
                                                                               safety output is in the ON state.
                        2                    OFF state           Red           Lights up red when at least one safety
                                                                               output is in OFF state due to an inter-
                                                                               rupted field.
                                                                               Flashes red when a safety output is in
                                                                               the OFF state due to an error.




106    nanoScan3 I/O                                                                       8024596/1W27/2026-05-26 | SICK
                                                                                      SUBJECT TO CHANGE WITHOUT NOTICE

OPERATION 10

                               Number             Function               Color              Meaning
                               3                  Restart interlock/     Yellow             Setup with reset: Flashes if the restart
                                                  warning field                             interlock has been triggered.
                                                                                            Configuration with automated restart
                                                                                            after a time: Lights up while the con-
                                                                                            figured time to restart expires.
                                                                                            Warning field: Lights up yellow if at
                                                                                            least one warning field is interrupted.
                               4                  Display                Red/yellow/green Information about the status of the
                                                                                          safety laser scanner
                               5                  Network LED            Yellow/green       O   Lights up green: Ethernet connec-
                                                                                                tion established.
                                                                                            O   Flashes yellow: Data are being
                                                                                                transmitted.
                               6                  Button                 Operation of the display

                              The the ON state, OFF state and restart interlock/warning field LEDs are arranged in
                              three sets on the base of the optics cover so that they are clearly visible from all
                              directions.

                              Complementary information
                              The display elements are only used for diagnostic purposes and are not safety-relevant.
                              The safety function of the device is not impaired even if the status indicators are incor-
                              rectly displayed or fail.


10.4           Status indicator with the display
                              Overview
                              The display shows current information about the status of the safety laser scanner. The
                              display switches off after approx. 60 s if all fields are clear and no other notification is
                              displayed.

                              Procedure

                              →    If the display is switched off, press any button briefly to activate the display.
                              →    Press the button briefly to obtain more details about the displayed status informa-
                                   tion.
                              →    If there are a number of pages with detailed information, this is shown in the top
                                   right of the display. Press the button briefly to change between a number of pages
                                   with detailed information.

                              Status indicator
                              Table 27: Overview of status information
                               Display                 Device or configura-       Meaning
                                                       tion
                                                       All devices and config- All fields clear, safety outputs in ON state.
                                                       urations                The number at bottom right indicates the active
                                                                               monitoring case.


                                                       Devices and configu-       Protective field interrupted, safety output in
                                                       rations with a config-     OFF state.
                                                       ured safety output




8024596/1W27/2026-05-26 | SICK                                                                                 nanoScan3 I/O       107
SUBJECT TO CHANGE WITHOUT NOTICE

10 OPERATION

                      Display           Device or configura-     Meaning
                                        tion
                                        Devices and configu-     For the cut-off paths of both safety outputs,
                                        rations with 2 config-   the following applies: the protective field is
                                        ured safety outputs      interrupted or there is a warning field in the
                                                                 active monitoring case. Safety outputs in the
                                                                 OFF state.
                                                                 Each column stands for a safety output.
                                        Devices and configu-     The protective field in the cut-off path of safety
                                        rations with 2 config-   output 1 is interrupted or there is a warning field
                                        ured safety outputs      in the active monitoring case. The safety output
                                                                 is in the OFF state.
                                                                 Safety outputs for which no field is interrupted
                                                                 and which are in the ON state are marked with
                                                                 their number.
                                        Devices with 2 safety    The protective field in the cut-off path of safety
                                        outputs if only safety   output 2 is interrupted or there is a warning field
                                        output 2 is configured   in the active monitoring case. The safety output
                                                                 is in the OFF state.
                                                                 Safety outputs that are not configured are not
                                                                 marked.
                                        Configuration with       Protective field is clear, reset can take place.
                                        restart interlock




                                        Configuration with       Reset button pressed. Safety output in the OFF
                                        restart interlock        state.




                                        Configuration with       Reset button pressed. Safety output in the ON
                                        restart interlock        state.




                                        Configuration with       Protective field is clear, configured time to
                                        automated restart        restart expires.
                                        after a time


                                        Configuration with at   Warning field interrupted (left column: num-
                                        least one warning field ber of interrupted warning fields, right col-
                                                                umn: number of warning fields in the current
                                                                monitoring case).

                                        All devices and config- Error. All safety outputs in the OFF state.
                                        urations




                      Display flashes
                                        All devices and config- Contamination warning.
                                        urations
                                                                → Check the optics cover for damage.
                                                                 → Clean the optics cover.


                      Display flashes




108   nanoScan3 I/O                                                                     8024596/1W27/2026-05-26 | SICK
                                                                                   SUBJECT TO CHANGE WITHOUT NOTICE

OPERATION 10

                               Display           Device or configura-      Meaning
                                                 tion
                                                 All devices and config- Contamination error. All safety outputs in the
                                                 urations                OFF state.

                                                                           → Check the optics cover for damage.
                                                                           → Clean the optics cover.

                               Display flashes
                                                 All devices and config- Dazzle warning. Check whether the safety laser
                                                 urations                scanner is being dazzled by an external light
                                                                         source in the scan plane, e.g., sun, halogen
                                                                         light, infrared light source. Remove or cover the
                                                                         light source.

                               Display flashes
                                                 All devices and config- Dazzle error. The associated safety outputs are
                                                 urations                in the OFF state. Check whether the safety laser
                                                                         scanner is being dazzled by an external light
                                                                         source in the scan plane, e.g., sun, halogen
                                                                         light, infrared light source. Remove or cover the
                                                                         light source.
                               Display flashes
                                                 Configuration with        Error in the external device monitoring (EDM).
                                                 external device moni-     OSSD pair in OFF state.
                                                 toring (EDM)




                               Display flashes
                                                 Configuration with ref-   Manipulation protection. The safety laser scan-
                                                 erence contour field      ner does not detect any contour within the con-
                                                                           figured tolerance band of the reference contour
                                                                           field. All safety outputs in the OFF state.


                               Display flashes
                                                 All devices and config- Manipulation protection. The safety laser scan-
                                                 urations                ner measures no values within the distance
                                                                         measurement range in an area of at least 90°.
                                                                         All safety outputs in the OFF state.


                               Display flashes
                                                 All devices and config- Safety function stopped. All safety outputs in
                                                 urations                the OFF state. Restart the device using the key-
                                                                         pad or Safety Designer.


                                                 All devices and config- A valid input signal is not yet applied at the con-
                                                 urations                trol inputs. All safety outputs in the OFF state.
                                                                         After switching on, the safety laser scanner
                                                                         waits for a valid input signal. During this time,
                                                                         an invalid input signal does not result in an
                                                                         error.
                                                 All devices               The device is not configured. The device is in
                                                                           the as-delivered state or has been reset to fac-
                                                                           tory settings. All safety outputs in the OFF state.




8024596/1W27/2026-05-26 | SICK                                                                          nanoScan3 I/O     109
SUBJECT TO CHANGE WITHOUT NOTICE

10 OPERATION

                      Display   Device or configura-    Meaning
                                tion
                                All devices and config- Passive state. All safety outputs in the OFF
                                urations                state. Press the button to obtain more informa-
                                                        tion.




110   nanoScan3 I/O                                                           8024596/1W27/2026-05-26 | SICK
                                                                         SUBJECT TO CHANGE WITHOUT NOTICE

MAINTENANCE 11

11             Maintenance
11.1           Safety

                              DANGER
                              Improper work on the product
                              A modified product may not offer the expected protection if it is integrated incorrectly.

                              →    Apart from the procedures described in this document, do not repair, open, manip-
                                   ulate or otherwise modify the product.


11.2           Regular cleaning
                              Overview
                              Depending on the ambient conditions, the optical cover must be cleaned regularly and
                              in the event of contamination. For example, static charges can cause dust particles to
                              be attracted to the optical cover.

                              Important information

                              WARNING
                              Contamination or damage to the optics cover
                              If the optical properties of the optics cover are impaired, persons or body parts might
                              not be detected or not detected in time.

                              →    Remove any contamination (e.g., droplets, condensation, frost, ice formation).
                                   Restart the safety laser scanner.
                              →    Replace damaged optics covers.
                              →    Keep the optics cover free of substances containing oil and grease.


                              NOTICE
                              →    Do not use aggressive or abrasive cleaning agents.
                              →    Recommendation: Use lens cleaner and lens cloths from SICK.


                              Procedure

                              Cleaning the optics cover
                              1.  Make sure that the dangerous state of the machine is and remains switched off
                                  during the cleaning.
                              2.  Remove dust from the optics cover using a soft, clean brush.
                              3.  Moisten a clean, soft cloth with lens cleaner and use it to wipe the optics cover.
                              4.  Check the effectiveness of the protective device.

                              Complementary information
                              If the display shows a contamination warning, the optics cover is dirty and must be
                              cleaned soon.
                              If the display shows a contamination error, the optics cover is very dirty and the safety
                              laser scanner has switched to the OFF state for safety reasons.

                              Further topics
                              O    "Thorough check of the principal function of the protective device", page 51




8024596/1W27/2026-05-26 | SICK                                                                        nanoScan3 I/O     111
SUBJECT TO CHANGE WITHOUT NOTICE

11 MAINTENANCE

11.3           Replacing the optics cover
                           Overview
                           If the optics cover is scratched or damaged, it must be replaced.
                           You can order the replacement optics cover from SICK.

                           Important information

                           NOTICE
                           SICK offers a variety of optics covers as a spare part.

                           →    Only use, as a spare part, the optics cover that is suitable for the product, if
                                applicable with mounted accessories.


                           Complementary information
                           For instructions on replacing the optics cover and additional information, see the
                           mounting instructions for the respective optics cover.

                           Further topics
                           O    "Spare parts", page 142

11.4           Replacing the safety laser scanner
                           Important information

                           DANGER
                           Hazard due to lack of effectiveness of the protective device
                           If an unsuitable configuration is saved in the system plug, it may cause the dangerous
                           state to not end in time.

                           →    After replacement, make sure the same system plug is used or the configuration is
                                restored.
                           →    Make sure that the safety laser scanner is aligned correctly after the replacement.


                           NOTICE
                           Enclosure rating IP65 only applies if the optics cover and the system plug are mounted
                           and the USB connection is closed with the protective cover.


                           NOTICE
                           If the system plug is mounted with excessive force, the contacts can break or bend.

                           →    Plug in the system plug carefully.
                           →    Do not force it.


11.4.1         Replacing the safety laser scanner without system plug
                           Overview




                           In many cases, you can reuse the existing bracket and the existing system plug. When
                           the new safety laser scanner is switched on for the first time, it reads the configuration
                           from the system plug and can be used without having to be reconfigured.



112      nanoScan3 I/O                                                                         8024596/1W27/2026-05-26 | SICK
                                                                                          SUBJECT TO CHANGE WITHOUT NOTICE

MAINTENANCE 11

                              Prerequisites
                              Tool required:
                              O    TX10 key

                              Procedure

                              1.   Make sure that the environment is clean and clear of fog, moisture, and dust.
                              2.   Unscrew the fixing screws and remove the defective safety laser scanner.
                              3.   Unscrew screws in the system plug and remove the system plug from the defective
                                   safety laser scanner.
                              4.   Mount the system plug on the new safety laser scanner.
                              5.   Mount the new safety laser scanner.
                              6.   Check the effectiveness of the protective device.
                                   o    Generally, the protective device is checked exactly as during commissioning.
                                   o    If during the project planning the possible tolerances of the devices have
                                        been considered and it is ensured that the configuration, wiring, or alignment
                                        of the safety laser scanner have not been changed, a function check-out is
                                        sufficient.

                              Complementary information

                              In certain cases (in the event of dust, high air humidity), it may make sense not to
                              disconnect the system plug and the safety laser scanner at first:
                              1.   Disconnect the connecting cables to the system plug.
                              2.   Unscrew screws from the bracket and remove the defective safety laser scanner
                                   from the bracket.
                              3.   Move the safety laser scanner with the system plug to a clean location (e.g. office,
                                   maintenance areas).
                              4.   Unscrew screws in the system plug and remove the system plug from the defective
                                   safety laser scanner.
                              5.   See above for further steps.

                              Further topics
                              O    "Replacing the system plug", page 114
                              O    "Mounting the device", page 55

11.4.2         Replacing the safety laser scanner with system plug




                              Procedure

                              1.   Disconnect the connecting cables to the system plug.
                              2.   Unscrew the fixing screws and remove the defective safety laser scanner.
                              3.   Mount the new safety laser scanner.
                              4.   Reconnect the connecting cables to the system plug.
                              5.   Configure the safety laser scanner.
                              6.   Perform commissioning again, taking particular care to conduct all of the thorough
                                   checks described.


                              Further topics
                              O    "Mounting the device", page 55




8024596/1W27/2026-05-26 | SICK                                                                     nanoScan3 I/O   113
SUBJECT TO CHANGE WITHOUT NOTICE

11 MAINTENANCE

11.5         Replacing the system plug




                       Important information

                       NOTICE
                       Enclosure rating IP65 only applies if the optics cover and the system plug are mounted
                       and the USB connection is closed with the protective cover.


                       NOTICE
                       If the system plug is mounted with excessive force, the contacts can break or bend.

                       →    Plug in the system plug carefully.
                       →    Do not force it.


                       Prerequisites
                       Tool required:
                       O    TX10 key

                       Procedure

                       1.   Make sure that the environment is clean and clear of fog, moisture, and dust.
                       2.   Disconnect the connecting cables to the system plug.
                       3.   Unscrew the screws in the defective system plug and remove the system plug from
                            the safety laser scanner.
                       4.   Make sure that the seal is seated correctly.
                       5.   Carefully push the new system plug into the safety laser scanner.
                       6.   Screw in the system plug using the captive screws. Tightening torque: 1.3 Nm.
                       7.   Reconnect the connecting cables to the system plug.
                       8.   Configure the safety laser scanner.
                       9.   Perform commissioning again, taking particular care to conduct all of the thorough
                            checks described.

                       Further topics
                       O    "Mounting the device", page 55

11.6         Regular thorough check
                       The thorough check is intended to ensure that the safety functions are fulfilling their
                       planned purpose and whether persons are being adequately protected.

                       →    Carry out the checks specified in the test plan of the manufacturer of the machine
                            and the operating entity.


11.7         Updating firmware
                       Overview
                       SICK provides new firmware versions at irregular intervals. New firmware improves, for
                       example, the device behavior or introduces new functions.
                       When SICK provides a new firmware for the product, you can download and install the
                       new firmware using Sentio Creator. The firmware may only be downloaded and installed
                       via Sentio Creator. You can download Sentio Creator by clicking on www.sick.com and




114    nanoScan3 I/O                                                                      8024596/1W27/2026-05-26 | SICK
                                                                                     SUBJECT TO CHANGE WITHOUT NOTICE

MAINTENANCE 11

                                 entering Sentio Creator in the search field. Additional information on Sentio Creator
                                 and on installing firmware can be found in the operating instructions included with
                                 Sentio Creator.
                                 The changes that a new firmware brings are described in the release notes. You can
                                 find the current release notes for the firmware at www.sick.com/8028488.
                                 You can find the version number of the currently installed firmware on the display of the
                                 device, in Safety Designer, and in the Deployment Manager extension of Sentio Creator.
                                 The following interfaces are suitable for firmware installation:
                                 O    USB 4)
                                 O     Ethernet

                                 Important information

                                 DANGER
                                 Death or serious injury due to unexpected startup of the machine

                                 →     Make sure that the dangerous state of the machine is (and remains) switched off
                                       during the firmware installation.


                                 NOTICE
                                 Damage to the device

                                 →     After starting the installation of a firmware, do not interrupt the power supply
                                       before the installation has successfully completed.
                                 →     After starting the installation of a firmware, do not restart the device before the
                                       installation of the firmware has successfully completed.


                                 NOTE
                                 When a new firmware is installed, the previously installed firmware cannot be restored.


                                 NOTE
                                 With new firmware, the product may receive new functions that are not described
                                 in older versions of these operating instructions. You will find the current operating
                                 instructions under www.sick.com/8024594.

                                 →     Use the latest version of the operating instructions.


                                 Prerequisites
                                 O     Firmware version R01.64 or higher is installed on the device.
                                 O     If firmware with a version lower than R01.94 is installed on the device, the firmware
                                       with version R01.94 must be installed first. Only then can a firmware with a higher
                                       version be installed.
                                 O     The version number of the firmware on the device is lower than the version number
                                       of the firmware to be installed.
                                 O     A compatible system plug is correctly mounted on the device.
                                 O     The device is not connected to Safety Designer.
                                 O     The device is not displaying an error.
                                 O     Firmware may only be installed by qualified and authorized personnel.

                                 Before installation

                                 1.    Read the firmware release notes carefully.

4)   The USB port may only be used temporarily and only for configuration, diagnostics and installation of firmware.



8024596/1W27/2026-05-26 | SICK                                                                                          nanoScan3 I/O   115
SUBJECT TO CHANGE WITHOUT NOTICE

11 MAINTENANCE

                           Changes introduced in an earlier firmware version are also included in later firm-
                           ware versions. You must therefore consider all release notes after the currently
                           installed firmware version and up to the intended version.
                      2.   Analyze the effects of the firmware update on the safety function.
                      3.   Perform a risk assessment for the identified effects of the firmware update and
                           determine any additional measures required, in particular tests that must be per-
                           formed.
                      4.   Implement the measures from step 3..
                      5.   Analyze the effects of the firmware update on other functions.
                      6.   Create and save a backup copy of the entire configuration of the device.
                      7.   Make sure that the dangerous state of the machine is and remains switched off.
                      8.   Ensure that there are no other communication connections to the device during
                           installation, e.g., a connection to Safety Designer.

                      Installation

                      1.   When installing, observe any additional instructions in the firmware release notes.
                      2.   Follow the operating instructions of the Sentio Creator.
                      3.   In the Deployment Manager extension of Sentio Creator, use the Identify the
                           device function to check whether the correct device is selected.
                      4.   In the Deployment Manager extension of Sentio Creator, check whether the
                           expected firmware is installed on the device.
                      5.   Log in to the device with the Administrator user group and the corresponding
                           password.
                      m    The progress of the installation is displayed in Sentio Creator.
                      m    During the installation of the firmware, the display shows Ready for firmware
                           update. The display may go dark for a certain period of time.
                      m    The device is restarted at least once.
                      m    Installing the firmware can take several minutes.
                      m    The display shows the initial status again.
                      m    The firmware installation is complete.

                      In the event of problems during installation

                      →    If Sentio Creator displays an error message, take this message into account and
                           rectify the cause.
                      →    If the device can no longer be reached via the network due to an error and the
                           display shows a corresponding message, then connect the device via USB.
                      →    For all other problems, restart the installation but do not restart the device.

                      After installation

                      1.   In the Deployment Manager extension of Sentio Creator, check whether the
                           expected firmware is installed on the device.
                      2.   Implement the measures from "Before installation", page 115, step 3. and, if neces-
                           sary, further necessary checks.
                      3.   If additional checks are described in the firmware release notes, then carry out
                           these additional checks.
                      4.   Do not switch the dangerous state of the machine back on until the firmware has
                           been successfully installed, all measures have been implemented, and all checks
                           have been completed.




116   nanoScan3 I/O                                                                    8024596/1W27/2026-05-26 | SICK
                                                                                  SUBJECT TO CHANGE WITHOUT NOTICE

MAINTENANCE 11

                              Complementary information
                              O    Installing new firmware does not change the configuration of the device. If the
                                   configuration is not compatible with the new firmware, the device will display an
                                   error and must be reconfigured.
                              O    A new firmware version can result in a new functional scope. In this case, the
                                   version number of the functional scope on the type label is no longer correct.
                                   The version number of the functional scope is shown correctly on the display and
                                   in Safety Designer. Information on the new functional scope can be found in the
                                   firmware release notes.
                              O    The device version remains unchanged when a new firmware version is installed.
                                   This also applies if the new firmware version contains functions that are associated
                                   with a new version for new devices. Information on new functions can be found in
                                   the firmware release notes.

                              Further topics
                              O    "Version numbers and range of functions", page 128




8024596/1W27/2026-05-26 | SICK                                                                      nanoScan3 I/O      117
SUBJECT TO CHANGE WITHOUT NOTICE

12 TROUBLESHOOTING

12           Troubleshooting
12.1         Safety

                       DANGER
                       Improper work on the product
                       A modified product may not offer the expected protection if it is integrated incorrectly.

                       →    Apart from the procedures described in this document, do not repair, open, manip-
                            ulate or otherwise modify the product.


                       DANGER
                       Hazard due to unexpected starting of the machine

                       →    When any work is taking place, use the protective device to secure the machine or
                            to ensure that the machine is not switched on unintentionally.


                       NOTE
                       Additional information on troubleshooting is available from your SICK subsidiary.


                       Further topics
                       O    "Status indicators", page 106
                       O    "Status indicator with the display", page 107

12.2         Detailed diagnostics using the display
                       Overview
                       Use the button to call up the menu.
                       The menu provides access to the following areas:
                       O   Hardware
                       O    Configuration
                       O    Access management
                       O    Data output
                       O    Service
                       O    Device restart

                       Procedure

                       →    Press and hold to call up the menu.
                       →    Press the button briefly to switch to the desired menu item.
                       →    Press and hold the button to confirm the desired menu item.
                       →    Press the button briefly to navigate through the selected submenu.
                       →    Press the button repeatedly and briefly to return to the main menu.
                       →    Do not press the button for some time so that the display returns to the status
                            display.

                       Complementary information
                       The display language is set using Safety Designer during configuration. The display
                       language and the configuration cannot be changed using the button on the display.




118    nanoScan3 I/O                                                                      8024596/1W27/2026-05-26 | SICK
                                                                                     SUBJECT TO CHANGE WITHOUT NOTICE

TROUBLESHOOTING 12

12.3           Error indication on the display
                               Overview
                               If there is an error, the display shows a warning symbol, a type of error and an error code
                               on a red flashing background.




                               Figure 51: Error indication


                               O    The two-character error type will help you during troubleshooting.
                               O    The eight-character error code in the bottom line helps SICK support during the
                                    detailed error analysis.
                               O    Pressing the button briefly shows you more information about the error for trouble-
                                    shooting.
                               O    You will find detailed information in Safety Designer’s message history about the
                                    individual errors and information about events not shown by the display.

                               Error indication on the display
Table 28: Error types (selection)
Error type                 Brief description          Cause                                  Troubleshooting
C1                         Faulty configuration       The configuration is faulty.           → Reconfigure the device.
C2                         Incompatible configura- The configuration in the system plug      → Check device variant.
                           tion                    does not match the device’s func-         → Replace or reconfigure the
                                                   tionality.
                                                                                                device.
C3                         Incompatible firmware      The configuration in the system plug   → Check the firmware version of the
                                                      does not match the device’s firm-         device.
                                                      ware version.
                                                                                             → If necessary, update the device
                                                                                                firmware.
                                                                                             → Replace or reconfigure the
                                                                                                device.
D1                         Speed tolerance            The deviation between the meas-        → Check the configuration with
                           exceeded                   ured speeds of the two incremen-         Safety Designer.
                                                      tal encoders has exceeded the toler-
                                                                                             → Check the working process of the
                                                      ance permitted for the current travel
                                                      situation for longer than permissible.   machine.
                                                                                             → Check speed source.
D2                         Direction of rotation dif- The direction of rotation output by    → Check the configuration with
                           ferent                     the incremental encoders is differ-       Safety Designer.
                                                      ent. The allowed tolerance time has
                                                                                             → Check the working process of the
                                                      been exceeded.
                                                                                                machine.
                                                                                             → Check speed source.
D3                         Wiring error at dynamic    O   Cross-circuit between 0° and 90° → Check wiring.
                           control inputs             O   Cross-circuit between incremen-
                                                          tal encoder 1 and incremental
                                                          encoder 2
                                                      O   Connection cable of the incre-
                                                          mental encoders not correctly
                                                          connected




8024596/1W27/2026-05-26 | SICK                                                                               nanoScan3 I/O    119
SUBJECT TO CHANGE WITHOUT NOTICE

12 TROUBLESHOOTING

Error type              Brief description           Cause                                    Troubleshooting
D4                      Maximum speed               The maximum speed or the maxi-           → Check the configuration with
                        or input frequency          mum input frequency (pulses per             Safety Designer.
                        exceeded                    second) was exceeded at a dynamic
                                                                                             → Check the working process of the
                                                    control input.
                                                                                                machine.
                                                                                             → Check speed source.
D5                      Speed limit exceeded        The speed is outside the configured      → Check the configuration with
                                                    speed range. The signal is applied          Safety Designer.
                                                    for longer than 1 s.
                                                                                             → Check the working process of the
                                                                                                machine.
                                                                                             → Check speed source.
E1                      Error in the safety laser   The safety laser scanner has an          → Perform a device restart using
                        scanner                     internal error.                             the display or Safety Designer or
                                                                                                interrupt the voltage supply for at
                                                                                                least two seconds.
                                                                                             → Replace the safety laser scanner
                                                                                                and send it to the manufacturer
                                                                                                for repair.
E2                      Error in the safety laser   The safety laser scanner has an          → Perform a device restart using
                        scanner                     internal error.                             the display or Safety Designer or
                                                                                                interrupt the voltage supply for at
                                                                                                least two seconds.
                                                                                             → Replace the safety laser scanner
                                                                                                and send it to the manufacturer
                                                                                                for repair.
E3                      Error in the system plug The system plug has an internal             → Perform a device restart using
                                                 error.                                         the display or Safety Designer or
                                                                                                interrupt the voltage supply for at
                                                                                                least two seconds.
                                                                                             → Replace the system plug.
E4                      Incompatible system         The system plug is unsuitable for the → Check part number or type code.
                        plug                        safety laser scanner.                 → Replace the system plug.
E5                      Dazzle error                Strong external light source, e.g.,      → Remove or cover the light source.
                                                    sun, halogen headlamps, infrared         → Perform a device restart using
                                                    light source, stroboscope.
                                                                                                the display or Safety Designer or
                                                                                                interrupt the voltage supply for at
                                                                                                least two seconds.
F1                      Current too high at an      The current is too high at an OSSD.  → Check connected switching ele-
                        OSSD                        The limit has been exceeded for cur-   ment.
                                                    rent allowed short-term or perma-
                                                    nently.
F2                      OSSD short-circuit to       There is a short-circuit to 24 V at an   → Check wiring.
                        24 V                        OSSD.
F3                      OSSD short-circuit to       There is a short-circuit to 0 V at an    → Check wiring.
                        0V                          OSSD.
F4                      Short-circuit between 2     There is a short-circuit between 2       → Check wiring.
                        OSSDs                       OSSDs.
F5                      Short-circuit between       There is a short-circuit between         → Check wiring.
                        OSSD and universal          an OSSD and a universal input or
                        input or universal I/O      between an OSSD and a universal
                                                    I/O.
F9                      General OSSD error          At least one OSSD is showing unex-       → Check the wiring of the OSSDs.
                                                    pected behavior.




120     nanoScan3 I/O                                                                                   8024596/1W27/2026-05-26 | SICK
                                                                                                   SUBJECT TO CHANGE WITHOUT NOTICE

TROUBLESHOOTING 12

Error type                 Brief description          Cause                                     Troubleshooting
L2                         Invalid configuration of   The configuration of the external         → Check whether the external
                           the external device        device monitoring (EDM) is invalid.          device monitoring is connected
                           monitoring (EDM)           The configuration is unsuitable for
                                                                                                   correctly.
                                                      the wiring.
                                                                                                → Check the configuration with
                                                                                                   Safety Designer.
L3                         Error in the exter-        A faulty signal is applied at the exter- → Check whether the contactors
                           nal device monitoring      nal device monitoring (EDM). The           are wired correctly and operating
                           (EDM)                      allowed tolerance time has been
                                                                                                 correctly.
                                                      exceeded.
L8                         Error in the reset input   An invalid signal is applied at a reset   → Check the reset pushbutton, the
                                                      input. The reset signal is applied for       wiring, and any other compo-
                                                      too long.
                                                                                                   nents affected.
L9                         Short-circuit at the       Exactly the same signal is applied at     → Check wiring for cross-connec-
                           reset input                a reset input as at another input, an        tions.
                                                      OSSD or an output. There may be a
                                                      short-circuit.
M1                         Incompatible configura- The data output is configured in a   → Reconfigure the data output.
                           tion of the data output way that the device does not support
                                                   (e.g., invalid start angle).
M2                         Data output: Data pack- The data output could not transmit           → Configure the data output so that
                           ets lost                all data packets (for example, buffer           less data is transmitted.
                                                   memory full).
M3                         Configuration not veri-    The configuration is not verified.        → Verify the configuration.
                           fied
N1                         Invalid input signal       The signal applied at the control         → Check the configuration with
                                                      inputs is not assigned to a monitor-         Safety Designer.
                                                      ing case. The signal is applied for
                                                                                                → Check the working process of the
                                                      longer than the set input delay +1 s.
                                                                                                   machine.
N2                         Incorrect switching        The configured switching sequence         → Check the working process of the
                           sequence                   was interrupted by the new monitor-          machine.
                                                      ing case.
                                                                                                → Change configured switching
                                                                                                   order.
N3                         Invalid input signal       The signal applied at the static con-     → Check activation of the control
                                                      trol inputs does not match the com-          inputs.
                                                      plementary condition. The signal is
                                                      applied for longer than 1 s.
T1                         Temperature error          The operating temperature of the          → Check whether the safety laser
                                                      safety laser scanner has exceeded            scanner is being operated in
                                                      or fallen below the permitted range.
                                                                                                   accordance with the permissible
                                                                                                   ambient conditions.
W1                         Warnings exceed toler-     The combination of multiple warn-         → Use Safety Designer to check
                           ance time                  ings has resulted in an error. The           what warnings exist.
                                                      tolerance time of 1 s has been
                                                      exceeded as there are multiple
                                                      warnings.


12.4           Diagnostics using Safety Designer
                               Diagnostic tools
                               The following diagnostics tools are available in the device window:
                               O    Data recorder
                               O     Event history
                               O     Message history
                               O     Contamination measurement




8024596/1W27/2026-05-26 | SICK                                                                                   nanoScan3 I/O      121
SUBJECT TO CHANGE WITHOUT NOTICE

12 TROUBLESHOOTING

                                  Interfaces
                                  The following interfaces are suitable for diagnostics:
                                  O    USB 5)
                                  O     Ethernet

12.4.1          Data recorder
                                  Overview




Figure 52: Data recorder


                                  You can use the data recorder to record the device’s signals. Depending on the inter-
                                  face and the load on the interface, the measurement data may not be transmitted and
                                  shown for every scan cycle.
                                  The data is saved in a data recorder diagnostics file.
                                  You can play the data recorder diagnostic file in the data recorder.
                                  You can adjust the settings in the Safety Designer main window.
                                  Table 29: Data recorder

                                              Start recording


                                              Stop recording




5)    The USB port may only be used temporarily and only for configuration, diagnostics and installation of firmware.



122       nanoScan3 I/O                                                                                              8024596/1W27/2026-05-26 | SICK
                                                                                                                SUBJECT TO CHANGE WITHOUT NOTICE

TROUBLESHOOTING 12


                                       Selecting the displayed data and setting the display sequence


                                       Full screen mode


                              Prerequisites
                              O    Existing connection between Safety Designer and device
                              O    Configuration in the project and configuration in the device are synchronized.

                              Typical applications
                              O    Check spatial geometry
                              O    Check where a person can stay or when a person is detected
                              O    Check input information about the current monitoring case
                              O    Check why safety outputs have switched

12.4.2          Event history
                              Overview




Figure 53: Event history

1        Data source
2        Available views
3        Navigation




8024596/1W27/2026-05-26 | SICK                                                                         nanoScan3 I/O   123
SUBJECT TO CHANGE WITHOUT NOTICE

12 TROUBLESHOOTING

                      The safety laser scanner stores data on important events. The event history displays
                      information about the most recently stored events.

                      Event memory in the safety laser scanner
                      The safety laser scanner stores data on the following events:
                      O   Safety output switches to the OFF state.
                      O    An object is detected in a safety-related field.
                      For each object detection where a safety output switches to the OFF state, the safety
                      laser scanner stores the data from 10 scans. When the internal memory of the safety
                      laser scanner is full, the scan data of the oldest object detection is overwritten to store
                      a new object detection. The position and time of the object detection are retained.
                      The internal memory of the safety laser scanner is cleared during a restart and when
                      transferring a configuration.

                      Data source
                      O    Read from device: Only available when a device is connected. The data stored in
                           the device will be read.
                      O    Load file: You can open a file that stores events that were previously read from a
                           device.
                      O    Store data: You can save the events read from a device to a file for later analysis.

                      Events
                      The Events view shows a graphical overview of the object detections in safety-related
                      fields that have led to a safety output switching to the OFF state.
                      O    Navigation: You can select the event whose measurement data is displayed in the
                           right area.
                      O    Overview of events: The position of each recorded object detection relative to the
                           safety laser scanner is displayed. If you hold the mouse pointer on a position, the
                           set multiple sampling is displayed. When you click on a position, the correspond-
                           ing measurement data is displayed in the right-hand area.
                      O    Measurement data for the selected event: The measurement data of the selected
                           object detection is displayed. If multiple scans are stored for the selected object
                           detection, you can view the individual scans one by one by clicking on the icons
                           next to Scan.

                      Event table
                      The event table shows detailed information about the events which have led to a safety
                      output switching to the OFF state.
                      Based on the measurement data, a probable cause is assigned to each event:
                      O   Object: An object was probably detected in the protective field.
                      O    Contour: A reference contour field or a contour identification field detects a devia-
                           tion of the monitored contour.
                      O    Contamination: The shutdown was triggered by a contamination of the optics
                           cover in the area of the protective field. The displayed distance relates to an object
                           that was detected despite the contamination. This value is not reliable due to the
                           contamination.
                      O    Dazzle: The shutdown was triggered by an external light source in the scan plane
                           in the area of the protective field, e.g., sun, halogen light, infrared light source,
                           stroboscope.
                      O    Close to field edge or particle in field: Object detection in the protective field was
                           probably triggered at the edge or by particles.




124   nanoScan3 I/O                                                                       8024596/1W27/2026-05-26 | SICK
                                                                                     SUBJECT TO CHANGE WITHOUT NOTICE

TROUBLESHOOTING 12

                              Multiple sampling
                              The Multiple sampling view shows how often object detections with different durations
                              occurred. All object detections in safety-related fields are taken into account. There-
                              fore, the number of entries in this view may deviate from the other views.
                              The duration is specified as the number of consecutive scans in which an object is
                              detected in the field. For each duration, the diagram shows the corresponding number
                              of object detections.

                              Meta data
                              The Meta data view shows additional information.
                              You can add to a comment. When you save the event history, the comment is saved as
                              well.

12.4.3           Message history
                              Overview




Figure 54: Message history

1        Message history
2        Display filter
3        Details about the selected message


                              Events such as errors, warnings and information are stored in the message history.




8024596/1W27/2026-05-26 | SICK                                                                    nanoScan3 I/O    125
SUBJECT TO CHANGE WITHOUT NOTICE

12 TROUBLESHOOTING

                         By right-clicking on the table header, you can select the columns displayed in the
                         message history.
                         Safety Designer shows details about the events in the bottom part of the window, ways
                         to solve them are also shown.
                         Table 30: Message history
                                            Start automatic update


                                            Stop automatic update


                                            Mark all entries as viewed


                                            Delete all entries
                                            Deleted entries are hidden for the current user group and for user groups
                                            with lower permissions. They are still visible to user groups with higher per-
                                            missions.
                                            Print message history


                                            Save message history as a PDF


                                            Save message history as CSV



12.4.4         Contamination measurement
                         Safety Designer displays information on the measured contamination of the optics
                         cover.
                         A contamination of 100% means that the safety laser scanner is reporting a contamina-
                         tion error and is switching all safety outputs to the OFF state.




126      nanoScan3 I/O                                                                           8024596/1W27/2026-05-26 | SICK
                                                                                            SUBJECT TO CHANGE WITHOUT NOTICE

DECOMMISSIONING 13

13             Decommissioning
13.1           Disposal
                              Procedure

                              →    Always dispose of unusable devices in accordance with national waste disposal
                                   regulations.




                              Complementary information
                              SICK will be glad to help you dispose of these devices on request.




8024596/1W27/2026-05-26 | SICK                                                                     nanoScan3 I/O   127
SUBJECT TO CHANGE WITHOUT NOTICE

14 TECHNICAL DATA

14                Technical data
14.1              Version numbers and range of functions
                                   Functional scope
                                   Older devices might not support the full functional scope of the latest Safety Designer.
                                   To identify the different levels of the functionality, we use a three-digit version number.
                                   The range of functions of the device is found at the following locations:
                                   O    Type label, Version field 6)
                                   O      Display, entry in the Hardware menu
                                   O      Safety Designer, Overview dialog box (only with connected device)
                                   O      Safety Designer, report
                                   Table 31: Functional scope
                                    Type code                    Version number               Amendments and new functions
                                    NANS3-AAAZ30AN1              V 1.0.0                      O   First released version
                                                                 V 1.1.0                      O   Deviating multiple sampling after object
                                                                                                  detection can be configured
                                                                                              O   Interfaces and selected functions can be
                                                                                                  activated or deactivated
                                                                                              O   New Always ON (NON-safe) function in
                                                                                                  monitoring case tables
                                    NANS3-CAAZ30AN1              V 1.0.0                      O   First released version
                                                                 V 1.1.0                      O   Deviating multiple sampling after object
                                                                                                  detection can be configured
                                                                                              O   Interfaces and selected functions can be
                                                                                                  activated or deactivated
                                                                                              O   New Always ON (NON-safe) function in
                                                                                                  monitoring case tables

                                   Version
                                   To identify the different revision levels of the devices, we use a three-digit version
                                   number. The revision level of the device is indicated on the type label in the Revision
                                   field.
                                   Table 32: Version
                                    Type code                    Version number               Amendments and new functions
                                    NANS3-AAAZ30AN1              Rev 1.0.0                    O   First released version
                                                                 Rev 1.1.0                    O   Data output: Accuracy of angle specification
                                                                                                  improved
                                                                 Rev 1.2.0                    O   Transmission of the measurement data to
                                                                                                  Safety Designer optimized, improved live
                                                                                                  display of the spatial contour
                                                                 Rev 1.3.0                    O   Adaptation of detection behavior for opti-
                                                                                                  mized safety and availability
                                                                 Rev 1.3.1                    O   Internal change to components, no change
                                                                                                  in function




6)     A new firmware version can result in a new functional scope. In this case, the version number of the functional scope on the type label is no
       longer correct. The version number of the functional scope is shown correctly on the display and in Safety Designer.



128        nanoScan3 I/O                                                                                               8024596/1W27/2026-05-26 | SICK
                                                                                                                  SUBJECT TO CHANGE WITHOUT NOTICE

TECHNICAL DATA 14

                               Type code                Version number            Amendments and new functions
                               NANS3-CAAZ30AN1          Rev 1.0.0                 O   First released version
                                                        Rev 1.1.0                 O   Data output: Accuracy of angle specification
                                                                                      improved
                                                        Rev 1.2.0                 O   Transmission of the measurement data to
                                                                                      Safety Designer optimized, improved live
                                                                                      display of the spatial contour
                                                                                  O   Encoder evaluation: General stability
                                                                                      improvement
                                                        Rev 1.3.0                 O   Adaptation of detection behavior for opti-
                                                                                      mized safety and availability
                                                        Rev 1.3.1                 O   Internal change to components, no change
                                                                                      in function

                              The device version remains unchanged when a new firmware version is installed. This
                              also applies if the new firmware version contains functions that are associated with a
                              new version for new devices. Information on new functions can be found in the firmware
                              release notes.


14.2           Data sheet
                              Table 33: Features
                                                                nanoScan3 Core I/O                 nanoScan3 Pro I/O
                               Protective field range           ≤ 3.0 m, details: see "Sensing range", page 135
                               Scanning range of the refer-     Like protective field range, see "Sensing range", page 135
                               ence contour field
                               Scanning range of the con-       Like protective field range, see "Sensing range", page 135
                               tour detection field
                               Warning field range              ≤ 10 m
                               Fields                           ≤8                                 ≤ 128
                               Simultaneously monitored         ≤4                                 ≤8
                               fields
                               Field sets                       ≤8                                 ≤ 128
                               Monitoring case tables           1                                  2
                               Monitoring cases                 ≤2                                 ≤ 128
                               Scanning angle                   275° (–47.5° to 227.5°)
                               Protective field resolution      20 mm, 30 mm, 40 mm, 50 mm, 60 mm, 70 mm, 150 mm,
                                                                200 mm
                               Response time                    ≥ 70 ms, details: see "Response times", page 133
                               Scan cycle time                  30 ms
                               Generally necessary protec-      65 mm
                               tive field supplement (TZ =
                               tolerance zone of the safety
                               laser scanner)
                               Additional supplement ZR for 350 mm
                               reflection-based measure-
                               ment errors
                               Multiple sampling                2 … 16

                              Table 34: Safety-related parameters
                                                                nanoScan3 Core I/O                 nanoScan3 Pro I/O
                               Type (IEC 61496)                 Type 3
                               Safety integrity level           SIL 2
                               (IEC 61508)
                               Safety integrity level           SIL 2
                               (IEC 62061)
                               Category (ISO 13849)             Category 3



8024596/1W27/2026-05-26 | SICK                                                                                 nanoScan3 I/O   129
SUBJECT TO CHANGE WITHOUT NOTICE

14 TECHNICAL DATA

                                                                         nanoScan3 Core I/O               nanoScan3 Pro I/O
                                   Performance level                     PL d
                                   (ISO 13849)
                                   PFH (average frequency of a           8 × 10–8 h–1
                                   dangerous failure)
                                   TM (mission time) (ISO 13849) 20 years
                                   Safe status when an error             At least one OSSD is in the OFF state.
                                   occurs

                                  Table 35: Interfaces
                                                                         nanoScan3 Core I/O               nanoScan3 Pro I/O
                                   OSSD pairs                            1                                ≤2
                                   Automated restart of OSSDs            2 s to 60 s (configurable)
                                   after
                                   Length of cable                       ≤ 30 m                           ≤ 20 m
                                   USB
                                       Connection type                   USB 2.0 Micro-B (female connector)
                                       Transmission rate                 ≤ 12 Mbit/s (Full Speed)         ≤ 12 Mbit/s (Full Speed)
                                       Length of cable                   ≤3m
                                   Ethernet 1)
                                       Connection type                   M12 female connector, 4-pin, D-coded
                                       Port properties                   O   100BASE-TX
                                                                         O   Auto-negotiation
                                                                         O   Auto-crossover (MDIX)
                                                                         O   Auto-polarity
                                       Transmission rate                 ≤ 100 Mbit/s
                                       Length of cable                   ≤ 100 m
                                       Services                          O   Configuration and diagnostics using Safety Designer
                                                                         O   Data output
                                                                         O   SNTP (client)
                                   Physical interfaces                   O   Power supply, local inputs and outputs
                                                                         O   Network (Ethernet for data output, configuration and diag-
                                                                             nostics) 7)
                                                                         O   USB
                                                                         O   Display and pushbutton

                                  1)    The network connection is available for certain system plugs.


                                  Table 36: Electrical data
                                                                         nanoScan3 Core I/O               nanoScan3 Pro I/O
                                   Operating data
                                       Protection class                  III (IEC 61140)
                                       Supply voltage VS                 24 V DC (16.8 V to 30 V DC) (SELV/PELV) 1)
                                       Residual ripple                   ± 5% 2)
                                       Start-up current at 24 V          ≤ 1.3 A
                                       Current consumption at 24 V
                                                       No output load Typ. 0.16 A
                                         With maximum output load Typ. 0.66 A
                                                          Sleep mode Typ. 0.13 A
                                       Power consumption
                                                       No output load Typ. 3.9 W
                                         With maximum output load Typ. 15.9 W
                                                          Sleep mode Typ. 3.2 W
                                       Total output current              ≤ 500 mA

7)    The network connection is available for certain system plugs.



130       nanoScan3 I/O                                                                                         8024596/1W27/2026-05-26 | SICK
                                                                                                           SUBJECT TO CHANGE WITHOUT NOTICE

TECHNICAL DATA 14

                                                                   nanoScan3 Core I/O               nanoScan3 Pro I/O
                                   Power-up delay                  ≤ 12 s
                               Safety outputs (OSSD)
                                   Type of output                  2 PNP semiconductors for         2 PNP semiconductors for
                                                                   each OSSD pair, short-circuit    each OSSD pair, short-circuit
                                                                   protected, cross-circuit moni-   protected, cross-circuit moni-
                                                                   tored                            tored
                                   Output voltage for ON state     (UV – 2 V) … UV                  (UV – 2 V) … UV
                                   (HIGH)
                                   Output voltage for OFF state    0V…2V
                                   (LOW)
                                   Output current for ON state     0.5 mA … 250 mA per OSSD 3)
                                   (HIGH)
                                   Leakage current                 ≤ 250 µA
                                   Load inductance                 ≤ 2.2 H
                                   Load capacity                   ≤ 1 µF in series with 50 Ω
                                   Permissible resistivity         ≤4Ω
                                   between load and device
                                   Test pulse width                ≤ 300 µs (typ. 230 µs)
                                   Test pulse interval             Typ. 8 × scan cycle time
                                   Duration of OFF state           ≥ 80 ms
                                   Discrepancy time (time offset ≤ 10 ms
                                   between switching OSSDs of
                                   an OSSD pair)
                               Universal output, universal I/O (configured as output)
                                   Output voltage HIGH             (UV – 2 V) … UV
                                   Output voltage LOW              0V…2V
                                   Output current HIGH             0.5 mA … 200 mA 3)
                                   Leakage current                 ≤ 250 µA
                                   Switch-on delay time            30 ms
                                   Switch off delay                30 ms
                               Static control input, universal input, universal I/O (configured as input)
                                   Input voltage HIGH              24 V (11 V … 30 V)
                                   Input voltage LOW               0 V (-30 V … 5 V)
                                   Input current HIGH              2 mA … 3 mA
                                   Input current LOW               0 mA … 2 mA
                                   Input capacitance               Typ. 10 nF
                                   Input frequency (max. switch- ≤ 20 Hz
                                   ing sequence when used as
                                   control input)
                                   Sampling time                   4 ms
                                   Response time at EDM after      300 ms
                                   switching on OSSDs (when
                                   used as EDM input)
                                   Actuating duration of control   60 ms to 30 s
                                   switch for reset (when used
                                   as reset input)
                                   Actuating duration of switch    ≥ 120 ms
                                   for sleep mode (when used
                                   as sleep mode input)
                               Dynamic control input
                                   Input voltage HIGH              -                                24 V (11 V … 30 V)
                                   Input voltage LOW               -                                0 V (-30 V … 5 V)
                                   Input current HIGH              -                                2 mA … 3 mA
                                   Input current LOW               -                                0 mA … 2 mA




8024596/1W27/2026-05-26 | SICK                                                                                  nanoScan3 I/O   131
SUBJECT TO CHANGE WITHOUT NOTICE

14 TECHNICAL DATA

                                                               nanoScan3 Core I/O                     nanoScan3 Pro I/O
                           Input capacitance                   -                                      Typ. 1 nF
                           Input frequency                     -                                      ≤ 100 kHz
                           Duty cycle (Ti/T)                   -                                      0.5
                           Incremental encoders that can be evaluated
                                                       Type -                                         Dual-channel, 90° phase sepa-
                                                                                                      ration
                                   Outputs required on the -                                          Push-pull
                                    incremental encoders
                             Number of pulses per path -                                              ≥ 100 pulses per cm
                              Length of cable (shielded) -                                            ≤ 20 m

                      1)    The supply voltage must be within the specified range at all times. It must not fall below the lower limit, even
                            for a brief period.
                            The power supply unit must be able to bridge a brief power failure of 20 ms as specified in IEC 60204-1.
                            Suitable power supply units are available as accessories from SICK.
                      2)    The voltage level must not fall below the specified minimum voltage.
                      3)    Total output current of all outputs ≤ 500 mA.


                      Table 37: Mechanical data
                                                               nanoScan3 Core I/O                     nanoScan3 Pro I/O
                       Dimensions (incl. system                106.6 mm × 80.2 mm × 117.5 mm
                       plug, W × H × D)
                       Weight (including system                0.67 kg
                       plug)
                       Housing material                        Aluminum
                       Housing color                           RAL 9005 (black) and RAL 1021 (rape yellow)
                       Optics cover material                   Polycarbonate
                       Optics cover surface                    Outside with scratch-resistant coating

                      Table 38: Ambient data
                                                               nanoScan3 Core I/O                     nanoScan3 Pro I/O
                       Enclosure rating 1)                     IP65 (IEC 60529)
                       Ambient light immunity                  ≤ 40 klx 2)
                       Ambient operating tempera-              -10 °C … 50 °C
                       ture
                       Storage temperature                     -25 °C … 70 °C
                       Air humidity                            ≤ 95%, non-condensing 3)               ≤ 95%, non-condensing 4)
                       Height above sea level dur-             ≤ 2,300 m
                       ing operation
                       Vibration resistance 5)
                           Standards                           O   IEC 60068-2-6
                                                               O   IEC 60068-2-64
                                                               O   IEC 60721-3-5
                                                               O   IEC TR 60721-4-5
                                                               O   IEC 61496-3
                           Class                               O   5M1 (IEC 60721-3-5)
                           Sinusoidal vibrations               O   0.35 mm, 50 m/s², 10 Hz … 150 Hz
                                                               O   1.5 mm, 1 Hz … 9 Hz
                                                               O   50 m/s², 9 Hz … 200 Hz
                                                               O   10 m/s², 10 Hz … 1,000 Hz
                           Noise vibrations                    O   0.3 m²/s³, 10 Hz … 200 Hz
                                                               O   0.1 m²/s³, 200 Hz … 500 Hz
                                                               O   50 m/s², 10 Hz … 500 Hz
                       Shock resistance 5)




132   nanoScan3 I/O                                                                                         8024596/1W27/2026-05-26 | SICK
                                                                                                       SUBJECT TO CHANGE WITHOUT NOTICE

TECHNICAL DATA 14

                                                                       nanoScan3 Core I/O                     nanoScan3 Pro I/O
                                   Standards                           O      IEC 60068-2-27
                                                                       O      IEC 60721-3-5
                                                                       O      IEC TR 60721-4-5
                                                                       O      IEC 61496-3
                                   Class                               O      5M1 (IEC 60721-3-5)
                                   Single shock                        150 m/s², 11 ms
                                   Continuous shock                    O      50 m/s², 11 ms
                                                                       O      100 m/s², 16 ms
                               EMC                                     In accordance with IEC 61496-1, IEC 61000-6-2, and
                                                                       IEC 61000-6-3

                              1)    The specified enclosure rating only applies if the optics cover and the system plug are mounted and the USB
                                    connection is closed with the protective cover.
                              2)    For ambient light sources directly in the scan plane in accordance with IEC 61496-3: ≤ 3 klx
                              3)    IEC 61496-1, no. 4.3.1 and no. 5.4.2, IEC 61496-3, no. 4.3.1 and no. 5.4.2. Condensation has an influence on
                                    normal operation.
                              4)    IEC 61496-1, no. 4.3.1 and no. 5.4.2, IEC 61496-3, no. 4.3.1 and no. 5.4.2. Condensation has an influence on
                                    normal operation.
                              5)    In direct mounting.


                              Table 39: Miscellaneous data
                                                                       nanoScan3 Core I/O                     nanoScan3 Pro I/O
                               Type of light                           Pulsed laser diode
                               Wavelength                              905 nm
                               Detectable remission                    1.8% to several 1,000%
                               Maximum uniform contami-                30%
                               nation of the optics cover
                               without reducing the detec-
                               tion capability 1)
                               Area where detection capa-              ≤ 50 mm 2)
                               bility is restricted
                               Pulse duration                          Typ. 4 ns
                               Average output power                    12.8 mW
                               Laser class                             1 3)

                              1)    In the event of heavy contamination, the safety laser scanner displays a contamination error and switches all
                                    safety outputs to the OFF state. This status is displayed in Safety Designer as 100% contamination.
                              2)    In close proximity (50 mm-wide area in front of the optics cover), the detection capability of the safety laser
                                    scanner may be restricted. If required, this area must be secured using an undercut or frame, for example.
                              3)    This laser product has laser class 1 according to IEC 60825-1:2014. In some cases, evaluation is required
                                    according to the older IEC 60825-1:2007 standard, e.g. by employers in the EU according to Directive
                                    2006/25/EC. According to the older IEC 60825-1:2007 standard, laser class 1M must be used as the basis.


14.3           Response times
                              Overview
                              The protective device’s response time is the maximum time between the occurrence
                              of the event leading to the sensor’s response and supply of the switch-off signal to the
                              protective device’s interface (for example OFF state of the OSSD pair).
                              In addition to the protective device’s response time, further signal transmission and
                              processing also influence the time up until the end of the dangerous state. This
                              includes a control’s processing time and the response times of downstream contactors,
                              for example.




8024596/1W27/2026-05-26 | SICK                                                                                              nanoScan3 I/O      133
SUBJECT TO CHANGE WITHOUT NOTICE

14 TECHNICAL DATA

                       Response time
                       The safety laser scanner’s response time depends on the set multiple sampling.
                       You can calculate the response time using the following formula:
                       tR = n × 30 ms +10 ms

                       The following rules apply:
                       O    tR = response time
                       O     n = set multiple sampling (default: n = 2)

14.4         Course of the OSSD test over time
                       The safety laser scanner tests the OSSDs at regular intervals. To do this, the safety laser
                       scanner switches each OSSD briefly to the OFF state and checks whether this channel
                       is voltage-free during this time.
                       Make sure that the machine’s control does not react to these test pulses and the
                       machine does not switch off.
                               tS         tS         tS      tS        tS        tS        tS         tS         tS
                       V


                                       OSSD 1.A
                                                                                                                             t

                       V


                                       OSSD 1.B
                                                                                                                             t

                       V


                                       OSSD 2.A
                                                                                                                             t

                       V


                                       OSSD 2.B
                                                                                                                             t


                       Figure 55: Switch-off tests


                       tS     Scan cycle time tS = 30 ms

                                                                  4 × tS

                            ≤ 300 µs                                                                              ≤ 300 µs
                       V


                                       OSSD 1.A
                                                                                                                             t

                       V


                                       OSSD 1.B
                                                                                                                             t


                       Figure 56: Duration and time offset for the switch-off tests in an OSSD pair



134    nanoScan3 I/O                                                                             8024596/1W27/2026-05-26 | SICK
                                                                                            SUBJECT TO CHANGE WITHOUT NOTICE

TECHNICAL DATA 14


                              tS     Scan cycle time tS = 30 ms


14.5           Sensing range
                              Protective field range
                              The effective protective field range depends on the object resolution that has been set.
                              Table 40: Protective field range
                               Resolution                   Protective field range
                               ≥ 70 mm                      3.00 m
                               60 mm                        2.60 m
                               50 mm                        2.15 m
                               40 mm                        1.60 m
                               30 mm                        1.25 m
                               20 mm                        1.25 m

                              Scanning range of the reference contour field
                              The effective scanning range of the reference contour field is the same as the protec-
                              tive field range.

                              Scanning range of the contour detection field
                              The effective scanning range of the contour detection field is the same as the protective
                              field range.

                              Warning field range and distance measurement range
                              For non-safety applications (warning fields, measurement data output), the safety laser
                              scanner has a larger scanning range than the maximum protective field range. The
                              requirements for size and remission factor of objects to be detected are illustrated
                              in the following graphs as a function of the desired scanning range. Under good condi-
                              tions, in many cases a smaller object size or a lower remission factor is sufficient to
                              achieve the desired scanning range.
                              The range is limited to 10 m for warning fields.




8024596/1W27/2026-05-26 | SICK                                                                     nanoScan3 I/O   135
SUBJECT TO CHANGE WITHOUT NOTICE

14 TECHNICAL DATA

                      d [mm]
                          1000


                           500



                           200


                           100


                            50



                            20


                            10
                                                 5          10          20          50       D [m]
                      Figure 57: Range and object size for measured data output


                      d          Required minimum size of the object in mm
                      D          Scanning range in m

                      R [%]

                       500         6


                       200


                       100         5
                                   4
                          50



                          20       3

                          10


                           5       2


                           2       1


                           1
                                                     5        10         20          50         D [m]
                      Figure 58: Range and required remission for measured data output




136   nanoScan3 I/O                                                                           8024596/1W27/2026-05-26 | SICK
                                                                                         SUBJECT TO CHANGE WITHOUT NOTICE

TECHNICAL DATA 14


                                  R         Required minimum remission in %
                                  D         Scanning range in m
                                  1         Black shoe leather
                                  2         Matt black paint
                                  3         Gray cardboard
                                  4         Writing paper
                                  5         White plaster
                                  6         Reflectors > 2,000%, reflective tapes > 300% 8)


14.6             Scan plane
                                  Overview
                                  In practice, the scan plane is slightly conical and tilted.

                                  Scan plane
                                  Table 41: Scan plane
                                                                             nanoScan3
                                   Conical error 1) 2)                       O   ≤ ± 75 mm at a distance of 3 m
                                                                             O   ≤ ± 500 mm at a distance of 20 m
                                   Tilt error 1) 3)                          O   ≤ 2°
                                                                             O   ≤ ± 105 mm at a distance of 3 m
                                                                             O   ≤ ± 700 mm at a distance of 20 m
                                   Deviation from the ideal scan             O   ≤ ± 180 mm at a distance of 3 m
                                   plane taking into account the             O   ≤ ± 1200 mm at a distance of 20 m
                                   conical error and the tilt error 1)

                                  1)   The specified values are valid at an ambient temperature of 20 °C. Deviations can occur at other tempera-
                                       tures.
                                  2)   The conical error was described in earlier operating instructions as the deviation from the ideal scan field
                                       flatness, or a similar description.
                                  3)   The values for tilt error apply for the M5 threaded holes on the sides.
                                       Additional deviations can be caused by brackets, for example.


                                  Complementary information
                                  The scan plane details are relative to the midpoint of the light spot. Depending on the
                                  specific application, it may also be necessary to consider the light spot size.

                                  Further topics
                                  O      "Dimensional drawings", page 139
                                  O      "Light spot size", page 137

14.7             Light spot size
                                  Overview
                                  The light spot has an elongated shape. The orientation of the light spot varies with the
                                  angle at which the light beam emerges from the device.
                                  The light spot has at its edges a transition area in which significantly less light hits the
                                  object than in the central area. In the following, the light spot size is specified as the
                                  area of the light spot that triggers a detection under normal conditions.



8)     The measured values are less accurate for reflectors or reflective surfaces because the distance measurement is designed for lower
       remission values.



8024596/1W27/2026-05-26 | SICK                                                                                               nanoScan3 I/O       137
SUBJECT TO CHANGE WITHOUT NOTICE

14 TECHNICAL DATA

                               Light spot size
                               Table 42: Light spot size 1)
                                                                      nanoScan3
                                At a distance of 3 m                  15 mm × 2 mm
                                At a distance of 5 m                  6 mm × 25 mm
                                At a distance of 10.0 m               20 mm × 50 mm
                                At a distance of 20.0 m               40 mm × 100 mm

                               1)   Effective light spot size (W × H) when the light beam exits the device at a 90° forward angle.


14.8           Measurement data details
                               Table 43: Measurement data
                                                                      nanoScan3
                                Data output channels                  2
                                Distance measurement range 1)
                                    For remission factor = 10%        ≤ 8.7 m
                                    For remission factor = 100%       ≤ 27.4 m
                                Scan rate                             33 Hz
                                Angular resolution (physical) 2)      < 0.01°
                                Angular resolution                    0.17° (1,651 safeHDDM® measured values)
                                (safeHDDM®) 2)
                                Measurement uncertainty 3)
                                Systematic error                      ± 10 mm
                                Total measurement error (statistical and systematic)
                                    At 1 σ                            ± 13 mm
                                    At 2 σ                            ± 16 mm
                                    At 3 σ                            ± 19 mm
                                    At 4 σ                            ± 22 mm
                                    At 5 σ                            ± 25 mm

                               1)   Warm-up time ≥ 30 min. Light spot fully on the target object.
                               2)   safeHDDM® filters the physical measured values and provides very precise and reproducible measured
                                    values. Only safeHDDM® measured values are available via data output.
                               3)   Typical values at 20 °C and remission factor - 1.8%, distance = protective field range.
                                    The measured values are less accurate for reflectors or reflective surfaces because the distance measure-
                                    ment is designed for lower remission values.


14.9           Network services and protocols
                               The network connection is available for certain system plugs.
Table 44: Network services and protocols
Service and Purpose           Communica- Direction               Interface         TCP or UDP Port (prod-          Port (part-       Factory
protocol                      tion partner                                                    uct)                 ner)              setting
DHCP          Automatic       DHCP server       Bidirec-         Network           UDP              68             67                Activated
              assignment                        tional           connection
              of network
              settings
SNTP          Time syn-    NTP server           Bidirec-         Network           UDP              123            123               Deactivated
              chronization                      tional           connection
CoLa 2        SICK devel-     CoLa 2 client, Bidirec-            Network           TCP              2122           Selected by       Activated
              oped proto-     e.g., com-     tional              connection                                        the client
              col: configu-   puter with
              ration and      Safety
              diagnostics     Designer



138      nanoScan3 I/O                                                                                              8024596/1W27/2026-05-26 | SICK
                                                                                                               SUBJECT TO CHANGE WITHOUT NOTICE

TECHNICAL DATA 14

Service and Purpose          Communica- Direction                   Interface            TCP or UDP Port (prod-       Port (part-   Factory
protocol                     tion partner                                                           uct)              ner)          setting
CoLa 2         SICK devel- Computer               Bidirec-          Network              UDP           30718          30,718 …      Activated
               oped proto- with Safety            tional            connection                                        30,738
               col: device  Designer
               search,
               device iden-
               tification,
               configura-
               tion of net-
               work set-
               tings
Data output    Continuous Target com-             Outgoing          Network              UDP           Randomly       Configura-    Deactivated
               data output, puter                                   connection                         selected       ble
               e.g. output
               of measure-
               ment data

                              The list of network services and protocols of the product is to the best of our knowledge
                              complete. No network service or protocol has been deliberately left out.


14.10          Dimensional drawings
                                                 106,6                                             a
                                                  ø 86                                  1
                                                                                                       2          b




                                                                      19 31,5 29,7
                                                                                                             3
                                   80,2
                                                                                                                  c                             50,5


                                                                                     26,3 24
                                                       65                                         M5 × 7,5
                                                                                            44




                               117,5
                                                -45°         225°




                                                                     102,5
                                                       90°




                                                 100,6



                              Figure 59: Dimensional drawing

                                          All dimensions in mm.
                              1           Mirror rotational axis
                              2           Scan plane
                              3           Required viewing slit

                                          •     a: Length of the viewing slit
                                          •     b: Minimum height above the scan plane
                                          •     c: Minimum height below the scan plane




8024596/1W27/2026-05-26 | SICK                                                                                              nanoScan3 I/O     139
SUBJECT TO CHANGE WITHOUT NOTICE

14 TECHNICAL DATA

                      Required viewing slit
                      If the device is installed in paneling, for example, you must ensure that the laser beam
                      can exit unhindered. The reflected laser beam must also reach the device unhindered.
                      That means the viewing slit must be large enough.
                      The required minimum height and width of the viewing slit depends on the following
                      parameters, among others:
                      O    Conical error
                      O    Alignment of the safety laser scanner (with compensation of the tilt error)
                      O    Light spot size at the end of the viewing slit. The reflected light beam has a
                           significantly larger light spot. This size must be taken into account.
                      O    Vibrations that affect the scan plane or the geometry of the viewing slit
                      The following information applies at an ambient temperature of 20 °C. Deviations may
                      occur at other temperatures.
                      Dimensioning of a viewing slit with length a ≤ 200 mm
                      O   b, c ≥ 14 mm
                      O    d ≥ 16 mm
                      Dimensioning of a viewing slit with length a > 200 mm
                           The individual tilt error of the safety laser scanner must be compensated for by
                           suitable alignment during installation. The cone error cannot be compensated and
                           is taken into account in the formula.
                      O    b, c ≥ 0.024536 × a + 9.8 mm, additional condition: b, c ≥ 14 mm
                      O    d ≥ 16 mm
                      Where:
                      O  a = length of the viewing slit from the mirror rotation axis
                      O    b = minimum height above the scan plane
                      O    c = minimum height below the scan plane
                      O    d = minimum lateral distance between the protective field and the boundary of the
                           viewing slit




140   nanoScan3 I/O                                                                      8024596/1W27/2026-05-26 | SICK
                                                                                    SUBJECT TO CHANGE WITHOUT NOTICE

ORDERING INFORMATION 15

15             Ordering information
15.1           Scope of delivery
                              O    Safety laser scanner without system plug
                              O    Safety note
                              O    Mounting instructions
                              O    Operating instructions for download: www.sick.com

15.2           Ordering information
                              Table 45: Ordering information
                               Designation                                 Type code                 Part number
                               nanoScan3 Core I/O                          NANS3-AAAZ30AN1           1100333
                               nanoScan3 Pro I/O                           NANS3-CAAZ30AN1           1100334

                              A system plug is required to operate the safety laser scanner, see "System plug",
                              page 143.




8024596/1W27/2026-05-26 | SICK                                                                     nanoScan3 I/O   141
SUBJECT TO CHANGE WITHOUT NOTICE

16 SPARE PARTS

16           Spare parts
16.1         Additional spare parts
                       Table 46: Additional spare parts
                       Part                                               Part number
                       Optics cover (with seal and screws)                2111696




142    nanoScan3 I/O                                              8024596/1W27/2026-05-26 | SICK
                                                             SUBJECT TO CHANGE WITHOUT NOTICE

ACCESSORIES 17

17                Accessories
17.1              System plug
Table 47: System plug
 Accessories for                                        Connection type                          Type code               Part number
 Device                         Part number
 nanoScan3 Core I/O             1100333                 O   Cable with plug connec-              NANSX-AAABZZZZ1         2105106
                                                            tor for voltage supply and
                                                            inputs and outputs, length:
                                                            300 mm 1)
                                1100333                 O   Cable with plug connec-              NANSX-AAABAEZZ1         2104949
                                                            tor for voltage supply and
                                                            inputs and outputs, length:
                                                            300 mm 1)
                                                        O   Cable with plug connec-
                                                            tor for network connection,
                                                            length: 250 mm 2)
 nanoScan3 Pro I/O              1100334                 O   Cable with plug connec-              NANSX-AAACZZZZ1         2105107
                                                            tor for voltage supply and
                                                            inputs and outputs, length:
                                                            300 mm 3)
                                1100334                 O   Cable with plug connec-              NANSX-AAACAEZZ1         2104860
                                                            tor for voltage supply and
                                                            inputs and outputs, length:
                                                            300 mm 3)
                                                        O   Cable with plug connec-
                                                            tor for network connection,
                                                            length: 250 mm 2)
                                1100334                 O   Cable with flying leads              NANSX-AACCZZZZ1S01      2128781
                                                            for voltage supply and
                                                            inputs and outputs, length:
                                                            880 mm 3)
                                1100334                 O   Cable with flying leads for          NANSX-AACCZZZZ1         2105109
                                                            voltage supply and inputs
                                                            and outputs, length: 2 m 3)
                                1100334                 O   Cable with flying leads              NANSX-AACCAEZZ1S01      2128780
                                                            for voltage supply and
                                                            inputs and outputs, length:
                                                            880 mm 3)
                                                        O   Cable with plug connec-
                                                            tor for network connection,
                                                            length: 250 mm 2)
                                1100334                 O   Cable with flying leads for          NANSX-AACCAEZZ1         2105108
                                                            voltage supply and inputs
                                                            and outputs, length: 2 m 3)
                                                        O   Cable with plug connec-
                                                            tor for network connection,
                                                            length: 250 mm 2)

1)   Bend radius (with fixed installation) ≥ 30 mm , bend radius (with flexible installation) ≥ 56 mm
2)   Bend radius (with fixed installation) ≥ 26 mm , bend radius (with flexible installation) ≥ 51 mm
3)   Bend radius (with fixed installation) ≥ 46 mm , bend radius (with flexible installation) ≥ 92 mm


17.2              Additional accessories
                                    Suitable accessories are available at www.sick.com. Enter the product part number in
                                    the search field (part number: see the type label entry in the “Ident. no.” field or in the
                                    “P/N” field). All suitable accessories are listed on the Accessories tab of the product
                                    page.




8024596/1W27/2026-05-26 | SICK                                                                                         nanoScan3 I/O   143
SUBJECT TO CHANGE WITHOUT NOTICE

18 GLOSSARY

18          Glossary
                       AGV                         Automatic Guided Vehicle: driverless vehicle used for transport.
                       CoLa 2                      CoLa 2 (Command Language 2) is a protocol from SICK, with which
                                                   a client (control, computer, etc.) can access suitable SICK sensors
                                                   via a network (TCP/IP) or USB.
                       Conical error               In practice, the area scanned by a scan plane is not precisely
                                                   flat but rather slightly conical. The conical error indicates how pro-
                                                   nounced the conicity is, i.e. how strongly the scanned area deviates
                                                   from the ideal plane.

                                                   The conical error of a particular device is invariable. It can only be
                                                   compensated for by measures during mounting.
                       Contour detection field     The contour detection field monitors a contour of the environment.
                                                   The electro-sensitive protective device switches the associated
                                                   safety outputs to the OFF state if a contour does not correspond
                                                   to the set specifications, e.g. because a door or flap is open.
                       Control input               A control input receives signals, e.g. from the machine or from
                                                   the control. Use of control inputs is how the protective device
                                                   receives information about the conditions at the machine, e.g., if
                                                   there is a change of operating mode. If the protective device is
                                                   configured appropriately, it will activate a different monitoring case
                                                   after receiving a new control input.

                                                   The control input information must be transmitted reliably. Gener-
                                                   ally, at least 2 separate channels are used to do this.

                                                   Depending on the device, a control input can be realized as a static
                                                   control input or a dynamic control input.
                       Dangerous state             A dangerous state is a status of the machine or facility, where
                                                   people may be injured. Protective devices prevent this risk if the
                                                   machine is operated within its intended use.

                                                   The figures in this document always show the dangerous state of
                                                   the machine as movement of a machine part. In practice, there are
                                                   different dangerous states, such as:
                                                   O   Machine movements
                                                   O   Electrical parts
                                                   O   Visible and invisible beam
                                                   O   A combination of multiple hazards
                       Dynamic control input       A dynamic control input is a single-channel control input that eval-
                                                   uates a number of pulses per time. An incremental encoder can
                                                   be connected to a dynamic control input. The incremental encoder
                                                   reports, for example, the speed of an AGV. In conjunction with a
                                                   second control input, a dynamic control input is used to switch
                                                   between different monitoring cases depending on the speed.
                       EDM                         External device monitoring
                       Electro-sensitive protec-   An electro-sensitive protective device is a device or system of devi-
                       tive device                 ces for safety-related detection of people or parts of the body.

                                                   It is used to protect people from machines and facilities that pose a
                                                   risk of injury. It triggers the machine or facility to adopt a safe state
                                                   before a person is exposed to a hazardous situation.

                                                   Examples: Safety light curtain, safety laser scanner.
                       ESPE                        Electro-sensitive protective device




144   nanoScan3 I/O                                                                             8024596/1W27/2026-05-26 | SICK
                                                                                           SUBJECT TO CHANGE WITHOUT NOTICE

GLOSSARY 18

                               External device monitor-   The external device monitoring (EDM) monitors the status of down-
                               ing                        stream contactors.

                                                          In order to use external device monitoring, positively guided con-
                                                          tactors must be used to switch off the machine. If the auxiliary
                                                          contacts of the positively guided contactors are connected to
                                                          the external device monitoring, the external device monitoring
                                                          checks whether the contactors switch correctly when the OSSDs
                                                          are switched off.
                               Field set                  A field set consists of one or more fields. The fields in a field set are
                                                          monitored simultaneously.

                                                          A field set can contain different field types, e.g., a protective field
                                                          and a warning field.
                               Hazardous area             Hazardous area is any space within and/or around machinery in
                                                          which a person can be exposed to a hazard. (ISO 12100)
                               Incremental encoder        An incremental encoder generates electrical pulses proportional to
                                                          a movement. Various physical quantities can be derived from these
                                                          pulses, e.g. speed and distance covered.
                               Light spot                 The light spot is the projection of the light beam on a plane perpen-
                                                          dicular to the light beam.

                                                          The light beam size depends on the distance between the light
                                                          source and the surface on which the light beam strikes.
                               Localization               Position determination or localization is the determination of the
                                                          position of an object. For vehicles, localization is a prerequisite for
                                                          navigation.
                               Monitoring case            A monitoring case indicates the machine status to the sensor. Gen-
                                                          erally, one field set is assigned to each monitoring case.

                                                          The sensor receives a defined signal for the current machine sta-
                                                          tus. When a signal change occurs, the sensor activates the moni-
                                                          toring case and thereby the field set that is associated with the new
                                                          machine status.
                               Navigation                 Navigation is the determination and continuous adaptation of the
                                                          route of a vehicle. This requires precise knowledge of the position
                                                          of the vehicle and the nature of the environment in which the vehi-
                                                          cle is moving.
                               Navigation                 Navigation is a central element of a website or software interface
                                                          that enables the user to always have an overview of the structure
                                                          of the website or software and to navigate as directly as possible to
                                                          any page of the website or software that is considered important.
                               OFF state                  The OFF state is the status of the outputs of the protective device,
                                                          where the controlled machine is triggered to quit its dangerous
                                                          state and the start-up of the machine is prevented (e.g., the voltage
                                                          at the OSSDs is LOW, so that the machine is switched off and
                                                          remains still).
                               ON state                   The ON state is the status of the outputs of the ESPE, where the
                                                          controlled machine is permitted to operate (e.g., the voltage at the
                                                          OSSDs is HIGH so that the machine can run).




8024596/1W27/2026-05-26 | SICK                                                                                nanoScan3 I/O     145
SUBJECT TO CHANGE WITHOUT NOTICE

18 GLOSSARY

                      OSSD                      Output signal switching device: signal output for the protective
                                                device, which is used for stopping the dangerous movement.

                                                An OSSD is a safety switching output. The functionality of each
                                                OSSD is tested periodically. OSSDs are always connected in pairs
                                                and must undergo dual-channel analysis for safety reasons. An
                                                OSSD pair is formed from 2 OSSDs that are connected and ana-
                                                lyzed together.
                      PFH                       Average frequency of a dangerous failure per hour.

                                                More information: IEC 61508, IEC 62061, ISO 13849.
                      PL                        Performance level (ISO 13849)
                      Position determination    Position determination or localization is the determination of the
                                                position of an object. For vehicles, localization is a prerequisite for
                                                navigation.
                      Protective field          The protective field is the area in which the test object specified
                                                by the manufacturer is detected by the electro-sensitive protec-
                                                tive equipment (ESPE). As soon as the electro-sensitive protective
                                                device detects an object in the protective field, it switches the
                                                associated safety outputs to the OFF state. This signal can be
                                                passed to controllers resulting in the dangerous state coming to
                                                an end, e.g. to stop the machine or the vehicle.
                      Reference contour field   The contour as reference field monitors a contour of the environ-
                                                ment. The safety laser scanner switches all safety outputs to the
                                                OFF state if a contour does not match the set parameters, because,
                                                for example, the mounting of the safety laser scanner has been
                                                changed.

                                                National and international standards require or recommend that a
                                                reference contour is monitored, if the safety laser scanner is used
                                                in vertical operation for hazardous point protection or for access
                                                protection.
                      Reset                     When a protective device has sent a stop command, the stopped
                                                state must be maintained until a reset device is activated and the
                                                machine can be restarted in a second step.

                                                The reset brings the protective device back to the monitoring state
                                                after it has sent a stop command. The reset also quits the start-up
                                                or restart interlock of a protective device, so that the machine can
                                                be restarted in a second step.

                                                The reset must only be possible, when all safety functions and
                                                protective devices are functional.

                                                The reset of the protective device must not introduce any move-
                                                ment or dangerous situations itself. The machine is only permitted
                                                to start after the reset once a separate start command has been
                                                sent.
                                                O   Manual resets are performed using a separate, manually oper-
                                                    ated device, such as a reset pushbutton.
                                                O   Automatic resets by the protective device are only permitted in
                                                    special cases, if one of the following conditions is met:
                                                    o  It must not be possible for people to be in the hazardous
                                                       area without triggering the protective device.
                                                    o  It must be ensured that no people are in the hazardous area
                                                       during or after the reset.




146   nanoScan3 I/O                                                                         8024596/1W27/2026-05-26 | SICK
                                                                                       SUBJECT TO CHANGE WITHOUT NOTICE

GLOSSARY 18

                               Resolution             The resolution of an active opto-electronic protective device (also
                                                      known as the sensor detection capability) is the minimum size of an
                                                      object for it to be reliably detected.
                               Response time          The protective device’s response time is the maximum time
                                                      between the occurrence of the event leading to the sensor’s
                                                      response and supply of the switch-off signal to the protective devi-
                                                      ce’s interface (for example OFF state of the OSSD pair).
                               Restart interlock      The restart interlock prevents the machine from automatically
                                                      starting up, for example after a protective device has responded
                                                      while the machine is operating or after changing the machine’s
                                                      operating mode.

                                                      The restart interlock can be implemented in the protective device
                                                      or in the safety controller.

                                                      A command to reset the protective device must be given, for exam-
                                                      ple using a reset pushbutton, before the machine can be restarted.
                               Retroreflector         A retroreflector reflects light back toward the light source largely
                                                      independently of the alignment of the retroreflector.
                               RSSI                   Received Signal Strength Indicator (RSSI): Indicator of the strength
                                                      of the received signal. A higher value corresponds to a better
                                                      reception. There is no universal relationship between a physical
                                                      quantity and a specified RSSI.
                               Safety function        Function of a machine whose failure can result in an immediate
                                                      increase of the risk(s). (ISO 12100)
                               Safety output          A safety output provides safety-related information.

                                                      Safety outputs are OSSDs, for example, or safety-related informa-
                                                      tion on a safety-related network.
                               Scan cycle time        The scan cycle time is the time the sensor needs for a complete
                                                      scan of its detection area.

                                                      Example: Time required by the mirror of a safety laser scanner for
                                                      one rotation.
                               Scan plane             The scan plane is the geometric plane in which the 2D laser scan-
                                                      ner captures its environment. A scan layer is created by deflecting
                                                      a laser beam using a rotating mirror. In practice, the area scanned
                                                      is not precisely flat.

                                                      Deviations from the ideal plane are specified as a conical error.
                                                      Deviations from the ideal alignment are specified as a tilt error.
                               SIL                    Safety integrity level
                               Static control input   A static control input is a dual-channel control input, which evalu-
                                                      ates the status of every channel as the value 0 or 1. The signal
                                                      states of one or more static control inputs give a unique signal
                                                      pattern. This signal pattern activates a monitoring case.
                               Tilt error             The tilt error indicates how strongly tilted the scan plane is to the
                                                      ideal alignment within the specific device. The tilt error can be
                                                      compensated for in many cases by mounting the sensor at a com-
                                                      pensating inclination.
                               Universal I/O          Universal I/O can be configured as universal input or as universal
                                                      output.




8024596/1W27/2026-05-26 | SICK                                                                          nanoScan3 I/O      147
SUBJECT TO CHANGE WITHOUT NOTICE

18 GLOSSARY

                      Universal input    Depending on the device, a universal input can be used for reset-
                                         ting, external device monitoring (EDM), sleep mode, or restarting
                                         the protective device, for example. If sleep mode is activated by a
                                         universal input, the sleep mode must not be used for safety appli-
                                         cations. Certain universal inputs can also be used in pairs as a
                                         static control input.
                      Universal output   The function of a universal output is configurable. Which functions
                                         are available depends on the device. Possible signals are, for
                                         example: reset required, contamination warning.
                      Warning field      The warning field monitors larger areas than the protective field.
                                         Simple switching functions can be triggered with the warning field,
                                         e.g. a warning light or an acoustic signal can be triggered if a per-
                                         son approaches, even before the person enters the protective field.

                                         The warning field must not be used for safety applications.




148   nanoScan3 I/O                                                                  8024596/1W27/2026-05-26 | SICK
                                                                                SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 19

19             Annex
19.1           Conformities and certificates
                              You can obtain declarations of conformity, certificates, and the current operating
                              instructions for the product at www.sick.com. To do so, enter the product part number
                              in the search field (part number: see the entry in the “P/N” or “Ident. no.” field on the type
                              label). On the page found, the conformity declarations and certificates are available for
                              downloading under "Downloads" > "Certificates".


19.2           Note on standards
                              Standards are specified in the information provided by SICK. The table shows regional
                              standards with similar or identical contents. Not every standard applies to all products.
                              Table 48: Note on standards
                               Standard                 Standard (regional)
                                                        China
                               IEC 60068-2-6            GB/T 2423.10
                               IEC 60068-2-27           GB/T 2423.5
                               IEC 60204-1              GB/T 5226.1
                               IEC 60529                GB/T 4208
                               IEC 60825-1              GB 7247.1
                               IEC 61131-2              GB/T 15969.2
                               IEC 61140                GB/T 17045
                               IEC 61496-1              GB/T 19436.1
                               IEC 61496-2              GB/T 19436.2
                               IEC 61496-3              GB 19436.3
                               IEC 61508                GB/T 20438
                               IEC 62061                GB 28526
                               ISO 13849-1              GB/T 16855.1
                               ISO 13855                GB/T 19876


19.3           Open source software
                              This product may contain open source software components. The use of such compo-
                              nents is subject to the terms of the respective open source licenses.
                              For additional information visit www.sick.com/licensetexts.


19.4           Checklist for initial commissioning and commissioning
                              Checklist for manufacturers or installers for installing electro-sensitive protective
                              device (ESPE)
                              The details relating to the items listed below must be available no later than when the
                              system is commissioned for the first time. However, these depend on the specific appli-
                              cation (the requirements of which must be reviewed by the manufacturer or installer).
                              This checklist should be retained and kept with the machine documentation to serve as
                              reference during recurring tests.
                              This checklist does not replace the initial commissioning, nor the regular inspection by
                              qualified safety personnel.
                               Have the safety rules and regulations been observed in compliance with the           Yes ⃞ No ⃞
                               directives and standards applicable to the machine?
                               Are the applied directives and standards listed in the declaration of conformity?    Yes ⃞ No ⃞



8024596/1W27/2026-05-26 | SICK                                                                               nanoScan3 I/O   149
SUBJECT TO CHANGE WITHOUT NOTICE

19 ANNEX

                      Does the protective device correspond to the required PL/SIL and PFH in accord- Yes ⃞ No ⃞
                      ance with ISO 13849-1/IEC 62061 and the required type in accordance with
                      IEC 61496-1?
                      Is access to the hazardous area or hazardous point only possible through the           Yes ⃞ No ⃞
                      protective field of the ESPE?
                      Have appropriate measures been taken to protect (mechanical protection) or             Yes ⃞ No ⃞
                      monitor (protective devices) any persons or objects in the hazardous area when
                      protecting a hazardous area or hazardous point, and have these devices been
                      secured or locked to prevent their removal?
                      Are additional mechanical protective measures fitted and secured against               Yes ⃞ No ⃞
                      manipulation which prevent reaching below, above or around the ESPE?
                      Has the maximum shutdown and/or stopping time of the machine been meas-                Yes ⃞ No ⃞
                      ured, specified and documented (at the machine and/or in the machine docu-
                      mentation)?
                      Has the ESPE been mounted such that the required separation distance from the          Yes ⃞ No ⃞
                      nearest hazardous point has been achieved?
                      Are the ESPE devices properly mounted and secured against manipulation after           Yes ⃞ No ⃞
                      alignment?
                      Are the required protective measures against electric shock in effect (protection      Yes ⃞ No ⃞
                      class)?
                      Is the control switch for resetting the protective devices (ESPE) or restarting the    Yes ⃞ No ⃞
                      machine present and correctly installed?
                      Are the outputs of the ESPE (OSSDs or safety outputs via the network) integrated       Yes ⃞ No ⃞
                      according to the required PL/SIL in accordance with ISO 13849-1 / IEC 62061 and
                      does the integration correspond to the circuit diagrams?
                      Has the protective function been checked in compliance with the test notes of          Yes ⃞ No ⃞
                      this documentation?
                      Are the specified protective functions effective at every operating mode that can      Yes ⃞ No ⃞
                      be set?
                      Are the switching elements activated by the ESPE, e.g. contactors, valves, moni-       Yes ⃞ No ⃞
                      tored?
                      Is the ESPE effective over the entire period of the dangerous state?                   Yes ⃞ No ⃞
                      Once initiated, will a dangerous state be stopped when switching the ESPE on           Yes ⃞ No ⃞
                      or off and when changing the operating mode, or when switching to another
                      protective device?




150   nanoScan3 I/O                                                                             8024596/1W27/2026-05-26 | SICK
                                                                                           SUBJECT TO CHANGE WITHOUT NOTICE

LIST OF FIGURES 20

20             List of figures
                              1.  Laser class 1................................................................................................................................. 10
                              2.  SICK product ID...........................................................................................................................14
                              3.  Device overview.......................................................................................................................... 14
                              4.  Principle of time-of-flight measurement..............................................................................15
                              5.  Light pulses scan an area.........................................................................................................16
                              6.  Hazardous area protection: detection of the presence of a person in the hazardous
                                  area................................................................................................................................................. 18
                              7.  Hazardous point protection: Hand detection......................................................................19
                              8.  Access protection: detection of a person when accessing a hazardous area..........19
                              9.  Mobile hazardous area protection: detection of a person when a vehicle
                                  approaches................................................................................................................................. 20
                              10. Prevent crawling beneath........................................................................................................22
                              11. Prevent stepping over.............................................................................................................. 22
                              12. Unsecured areas........................................................................................................................23
                              13. Overrun of the protective field in front of an opening......................................................25
                              14. Tolerance band of the contour as reference field (protective field within the pro-
                                  tected opening, edge of the protected opening = reference contour)...................... 26
                              15. Stationary application with horizontal scan plane for hazardous area protection..28
                              16. Protection against reaching over with low scan plane (dimensions in mm)............. 29
                              17. Protection against reaching over with high scan plane (dimensions in mm)........... 30
                              18. Scan plane at calf height.......................................................................................................... 31
                              19. Distance of the protective field from the wall.................................................................... 32
                              20. Stationary application in vertical operation for hazardous point protection.............33
                              21. Stationary application in vertical operation for access protection..............................35
                              22. Mobile application in horizontal operation for hazardous area protection............... 36
                              23. Flat-rate supplement for lack of ground clearance..........................................................37
                              24. Minimum supplement for lack of ground clearance........................................................38
                              25. Stopping distance as a function of the vehicle’s speed................................................. 38
                              26. Recommended fitting height................................................................................................. 40
                              27. Recommended fitting height for inverted mounting.......................................................40
                              28. Dual-channel and isolated connection of an OSSD pair................................................43
                              29. No potential difference between load and protective device.......................................43
                              30. How the restart interlock works (1): no one in protective field, machine operates.. 47
                              31. How the restart interlock works (2): person detected in protective field, safety out-
                                  put in OFF state.......................................................................................................................... 48
                              32. How the restart interlock works (3): person in hazardous area, no detection in pro-
                                  tective field, safety output still in OFF state....................................................................... 48
                              33. How the restart interlock works (4): the reset pushbutton must be pressed before
                                  restarting the machine............................................................................................................. 49
                              34. Mounting safety laser scanner...............................................................................................55
                              35. Connecting cable (male connector, M12, 8-pin, A-coded)............................................ 56
                              36. Connecting cable (male connector, M12, 17-pin, A-coded)............................................57
                              37. Network pin assignment (M12 female connector, 4-pin, D-coding)............................60
                              38. Software controls....................................................................................................................... 62
                              39. Configuration...............................................................................................................................65
                              40. Overview....................................................................................................................................... 67
                              41. Contour as Reference field......................................................................................................73
                              42. Field editor................................................................................................................................... 75
                              43. Area that cannot be monitored.............................................................................................. 78
                              44. Editing fields using coordinates............................................................................................80
                              45. Inputs and outputs, local......................................................................................................... 84
                              46. Monitoring cases....................................................................................................................... 88
                              47. Simulation.................................................................................................................................... 93
                              48. Data output.................................................................................................................................. 94
                              49. Report............................................................................................................................................98
                              50. Display elements......................................................................................................................106
                              51. Error indication...........................................................................................................................119
                              52. Data recorder.............................................................................................................................122


8024596/1W27/2026-05-26 | SICK                                                                                                                          nanoScan3 I/O              151
SUBJECT TO CHANGE WITHOUT NOTICE

20 LIST OF FIGURES

                      53.   Event history.............................................................................................................................. 123
                      54.   Message history........................................................................................................................125
                      55.   Switch-off tests.........................................................................................................................134
                      56.   Duration and time offset for the switch-off tests in an OSSD pair..............................134
                      57.   Range and object size for measured data output........................................................... 136
                      58.   Range and required remission for measured data output............................................136
                      59.   Dimensional drawing...............................................................................................................139




152   nanoScan3 I/O                                                                                                            8024596/1W27/2026-05-26 | SICK
                                                                                                                          SUBJECT TO CHANGE WITHOUT NOTICE

LIST OF TABLES 21

21             List of tables
                              1.    Target groups and selected sections of these operating instructions......................... 8
                              2.    Field types and their function.................................................................................................. 17
                              3.    Status of the channels of the control inputs with complementary evaluation.........44
                              4.    True vales with 1-off-n-evaluation with 2 input pairs (example)....................................44
                              5.    Pin assignment of the connecting cable with 8-pin M12 plug connector..................57
                              6.    Pin assignment of the connecting cable with M12 plug connector, 17-pin................ 57
                              7.    Pin assignment of the connecting cable with flying leads, 17-wire..............................59
                              8.    Network pin assignment..........................................................................................................60
                              9.    User groups................................................................................................................................. 63
                              10.   Type code in Safety Designer.................................................................................................66
                              11.   Recommended multiple sampling....................................................................................... 72
                              12.   Buttons on the toolbar.............................................................................................................. 76
                              13.   Colors of the field types............................................................................................................77
                              14.   Buttons for field sets..................................................................................................................77
                              15.   Mask areas................................................................................................................................... 78
                              16.   Propose field............................................................................................................................... 79
                              17.   Object transformation...............................................................................................................79
                              18.   Background image..................................................................................................................... 81
                              19.   Device Settings........................................................................................................................... 81
                              20.   Settings for the field editor..................................................................................................... 82
                              21.   Manage field set templates.................................................................................................... 82
                              22.   Virtual group................................................................................................................................83
                              23.   Empirical values for the required input delay.................................................................... 89
                              24.   Show/hide preset for specified cutoff behavior................................................................92
                              25.   Buttons........................................................................................................................................ 102
                              26.   Status LEDs................................................................................................................................106
                              27.   Overview of status information.............................................................................................107
                              28.   Error types (selection).............................................................................................................. 119
                              29.   Data recorder.............................................................................................................................122
                              30.   Message history........................................................................................................................126
                              31.   Functional scope......................................................................................................................128
                              32.   Version.........................................................................................................................................128
                              33.   Features...................................................................................................................................... 129
                              34.   Safety-related parameters.....................................................................................................129
                              35.   Interfaces....................................................................................................................................130
                              36.   Electrical data........................................................................................................................... 130
                              37.   Mechanical data....................................................................................................................... 132
                              38.   Ambient data............................................................................................................................. 132
                              39.   Miscellaneous data..................................................................................................................133
                              40.   Protective field range.............................................................................................................. 135
                              41.   Scan plane..................................................................................................................................137
                              42.   Light spot size .......................................................................................................................... 138
                              43.   Measurement data...................................................................................................................138
                              44.   Network services and protocols.......................................................................................... 138
                              45.   Ordering information................................................................................................................ 141
                              46.   Additional spare parts.............................................................................................................142
                              47.   System plug............................................................................................................................... 143
                              48.   Note on standards....................................................................................................................149




8024596/1W27/2026-05-26 | SICK                                                                                                                       nanoScan3 I/O             153
SUBJECT TO CHANGE WITHOUT NOTICE

21 LIST OF TABLES




154   nanoScan3 I/O        8024596/1W27/2026-05-26 | SICK
                      SUBJECT TO CHANGE WITHOUT NOTICE

LIST OF TABLES 21




8024596/1W27/2026-05-26 | SICK       nanoScan3 I/O   155
SUBJECT TO CHANGE WITHOUT NOTICE

SICK AG
                         WALDKIRCH   SICK AT
                                     A GLANCE
                         GERMANY
                         SICK.COM



                                     SICK is a leading global technology company for intelligent sensors
                                     and integrated solutions in industrial automation. Our technologies
                                     set benchmarks, making your industrial processes more efficient,
                                     safer and more sustainable – both in logistics and manufacturing
                                     operations.


                                     SICK combines sensor intelligence with industry expertise and certi-
                                     fied consulting services. We provide the ideal foundation for scalable
                                     as well as tailor-made automation solutions and create added value
                                     along the entire value chain. Our close partnership with our custom-
                                     ers is more than just a promise: Together, we optimize productivity,
                                     elevate quality, protect health and safety, and sustain the future. All
                                     with empathy and trust.




8024596/1W27/2026-05-26/en
                                     Since 1946, we have been developing innovative technologies with
                                     passion and a pioneering spirit. With a global network in around
                                     40 countries, SICK has a global presence and is always close by.
                                     The company’s headquarters are located in Waldkirch near Freiburg,
                                     Germany. Our customers benefit from our understanding of both local
                                     and global requirements, which enables us to deliver tailor-made sol-
                                     utions.