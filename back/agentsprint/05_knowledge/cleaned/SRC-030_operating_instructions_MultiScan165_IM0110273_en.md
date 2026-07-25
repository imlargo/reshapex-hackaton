OPERATING INSTRUCTIONS



multiScan165
3D LiDAR sensor

Described product
                   multiScan165

                   NOTE
                   The functional scope of the multiScan depends on the selected configuration. Certain
                   functions are supported or not supported, depending on the configured variant. The
                   operating instructions describe the full functional scope of the multiScan.


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




2   multiScan165                                                                     8028981/1X1R/2026-06-10 | SICK
                                                                               SUBJECT TO CHANGE WITHOUT NOTICE

CONTENTS

Contents
                              1    About this document..............................................................................                                         6
                                   1.1      Information on the operating instructions.....................................................                                    6
                                   1.2      Explanation of symbols.......................................................................................                     6
                                   1.3      Further information...............................................................................................                7

                              2    Safety information...................................................................................                                     8
                                   2.1      Intended use..........................................................................................................            8
                                   2.2      Improper use..........................................................................................................            8
                                   2.3      Cybersecurity.........................................................................................................            8
                                   2.4      Limitation of liability.............................................................................................              9
                                   2.5      Modifications and conversions.........................................................................                            9
                                   2.6      Requirements for skilled persons and operating personnel....................                                                      9
                                   2.7      Operational safety and specific hazards........................................................                                  10

                              3    Product description................................................................................                                       11
                                   3.1      Scope of delivery..................................................................................................              11
                                   3.2      Status indicators...................................................................................................             11
                                   3.3      Type label................................................................................................................       12
                                   3.4      Principle of operation..........................................................................................                 14
                                            3.4.1             Measurement principle...................................................................                       14
                                            3.4.2             Distance measurement...................................................................                        17
                                            3.4.3             Multi-echo analysis...........................................................................                 18
                                            3.4.4             Direction measurement...................................................................                       18
                                            3.4.5             Multi-layer technology.....................................................................                    20
                                            3.4.6             Coordinate system............................................................................                  21
                                            3.4.7             Filter......................................................................................................   23
                                                              3.4.7.1           Fog filter............................................................................       23
                                                              3.4.7.2           Echo filter.........................................................................         24
                                                              3.4.7.3           Particle filter....................................................................          24
                                                              3.4.7.4           Moving average filter....................................................                    25
                                                              3.4.7.5           Data reduction filter.......................................................                 26
                                                              3.4.7.6           Range filter.......................................................................          27
                                            3.4.8             Measurement data output..............................................................                          27
                                                              3.4.8.1           Data formats....................................................................             27
                                                              3.4.8.2           Scan layer address........................................................                   27
                                                              3.4.8.3           Segmented data output...............................................                         28
                                                              3.4.8.4           Data preparation............................................................                 29
                                                              3.4.8.5           ROS driver........................................................................           30
                                            3.4.9             Interlaced mode................................................................................                30
                                            3.4.10            Object sizes.........................................................................................          31
                                            3.4.11            Impact of object surfaces on the measurement......................                                             32
                                            3.4.12            Scanning range..................................................................................               34
                                            3.4.13            RSSI values..........................................................................................          35
                                            3.4.14            Inertial measuring unit (IMU)..........................................................                        36


8028981/1X1R/2026-06-10 | SICK                                                                                                                      multiScan165             3
SUBJECT TO CHANGE WITHOUT NOTICE

CONTENTS

                                 3.4.15            Contamination indication................................................................                     36
                                 3.4.16            Field evaluation..................................................................................           37
                                                   3.4.16.1          Delay time of field evaluation.....................................                        38

                    4   Transport and storage............................................................................ 39
                        4.1      Transport.................................................................................................................     39
                        4.2      Unpacking...............................................................................................................       39
                        4.3      Transport inspection............................................................................................               39
                        4.4      Storage....................................................................................................................    39

                    5   Mounting.................................................................................................... 40
                        5.1      Mounting instructions..........................................................................................                40
                                 5.1.1             Ventilation element...........................................................................               40
                        5.2      Mounting the system plug on the device.......................................................                                  41
                        5.3      Mounting the device............................................................................................                42
                        5.4      Mounting multiple devices.................................................................................                     42

                    6   Electrical installation.............................................................................. 43
                        6.1      Wiring instructions................................................................................................            43
                        6.2      Prerequisites for safe operation of the device..............................................                                   44
                        6.3      Calculation rule.....................................................................................................          47
                        6.4      Cable reserve on system plug...........................................................................                        48
                        6.5      Pinouts.....................................................................................................................   48
                        6.6      Connecting the device electrically..................................................................                           50

                    7   Commissioning........................................................................................                                   51
                        7.1      Operation using SOPASair.................................................................................                      51
                                 7.1.1             Opening the web server user interface (SOPASair).................                                            51
                                 7.1.2             Overview..............................................................................................       51
                                 7.1.3             Navigating in the live image...........................................................                      52
                                 7.1.4             User levels...........................................................................................       52
                                 7.1.5             Changing the password...................................................................                     53
                                 7.1.6             Resetting the password...................................................................                    53
                                 7.1.7             Displaying live data...........................................................................              53
                                                   7.1.7.1           Activating/deactivating filters.....................................                       54
                                 7.1.8             Configuring interfaces.....................................................................                  54
                        7.2      Operation in SOPAS ET.......................................................................................                   54
                                 7.2.1             Operation with SOPAS ET...............................................................                       55

                    8   Maintenance.............................................................................................                                57
                        8.1      Maintenance plan.................................................................................................              57
                        8.2      Cleaning..................................................................................................................     57

                    9   Troubleshooting....................................................................................... 58
                        9.1      General faults, warnings, and errors................................................................                           58
                        9.2      Repairs.....................................................................................................................   58
                        9.3      Returns.....................................................................................................................   58



4    multiScan165                                                                                                         8028981/1X1R/2026-06-10 | SICK
                                                                                                                    SUBJECT TO CHANGE WITHOUT NOTICE

CONTENTS

                                   9.4      Disposal...................................................................................................................   59

                              10   Technical data.......................................................................................... 60
                                   10.1     Features...................................................................................................................   60
                                   10.2     Mechanics/Electronics.......................................................................................                  62
                                   10.3     Dimensional drawing...........................................................................................                64
                                   10.4     Performance...........................................................................................................        64
                                   10.5     Interfaces................................................................................................................    65
                                   10.6     Ambient data..........................................................................................................        65
                                            10.6.1            Mission time........................................................................................        66

                              11   Accessories..............................................................................................                              67

                              12   Annex.......................................................................................................... 68
                                   12.1     Declarations of conformity and certificates..................................................                                 68
                                   12.2     Licenses..................................................................................................................    68
                                   12.3     Communication interfaces.................................................................................                     68
                                   12.4     Data format description (EN).............................................................................                     68
                                                              12.4.1.1          Glossary............................................................................      69
                                                              12.4.1.2          General information on the transmission of
                                                                                measurement data........................................................                  70
                                                              12.4.1.3          MSPACK format..............................................................               70
                                                              12.4.1.4          Compact format.............................................................               77
                                                              12.4.1.5          General measurement data definitions...................                                   89
                                                              12.4.1.6          Behavior of serialization for data reduction............                                  92
                                   12.5     Telegram listing (EN)............................................................................................             94
                                                              12.5.1.1          About this document.....................................................                  97
                                                              12.5.1.2          Communication format................................................                      98
                                                              12.5.1.3          Workflows.........................................................................        101
                                                              12.5.1.4          Telegrams......................................................................... 103
                                                              12.5.1.5          Diagnostics......................................................................         213




8028981/1X1R/2026-06-10 | SICK                                                                                                                   multiScan165              5
SUBJECT TO CHANGE WITHOUT NOTICE

1 ABOUT THIS DOCUMENT

1           About this document
1.1         Information on the operating instructions
                      These operating instructions provide important information on how to use devices from
                      SICK AG.
                      Prerequisites for safe work are:
                      O    Compliance with all safety notes and handling instructions supplied.
                      O    Compliance with local work safety regulations and general safety regulations for
                           device applications
                      The operating instructions are intended to be used by qualified personnel and electrical
                      specialists.

                      NOTE
                      Read these operating instructions carefully to familiarize yourself with the device and its
                      functions before commencing any work.

                      The operating instructions are an integral part of the product. Store the instructions
                      in the immediate vicinity of the device so they remain accessible to staff at all times.
                      Should the device be passed on to a third party, these operating instructions should be
                      handed over with it.
                      These operating instructions do not provide information on the handling and safe oper-
                      ation of the machine or system in which the device is integrated. Information on this can
                      be found in the operating instructions for the machine or system.


1.2         Explanation of symbols
                      Warnings and important information in this document are labeled with symbols. Sig-
                      nal words introduce the instructions and indicate the extent of the hazard. To avoid
                      accidents, damage, and personal injury, always comply with the instructions and act
                      carefully.

                      DANGER
                      … indicates a situation of imminent danger, which will lead to a fatality or serious injuries
                      if not prevented.


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




6     multiScan165                                                                         8028981/1X1R/2026-06-10 | SICK
                                                                                     SUBJECT TO CHANGE WITHOUT NOTICE

ABOUT THIS DOCUMENT 1

1.3            Further information
                              More information can be found on the product page. The product page can be
                              accessed via the SICK Product ID: pid.sick.com/{P/N}/{S/N}
                              {P/N} corresponds to the part number of the product (see type label).
                              {S/N} corresponds to the serial number of the product (see type label).
                              The following information is available depending on the product:
                              O    Data sheets
                              O    This document in all available language versions
                              O    CAD files and dimensional drawings
                              O    Certificates (e.g., declaration of conformity)
                              O    Other publications
                              O    Software
                              O    Accessories




8028981/1X1R/2026-06-10 | SICK                                                                        multiScan165   7
SUBJECT TO CHANGE WITHOUT NOTICE

2 SAFETY INFORMATION

2           Safety information
2.1         Intended use
                     The multiScan 3D LiDAR sensor is an intelligent sensor for invisibly detecting objects
                     in areas to be monitored. It has been designed for indoor or outdoor and mobile or
                     stationary use in stand-alone operation.
                     Typical application areas are, for example, anti-collision monitoring and rear area moni-
                     toring in industrial (autonomous) vehicles, person counts at access gates, monitoring of
                     land and buildings, volume monitoring, automated guided vehicle systems for outdoors,
                     robot area, traffic and park management systems.

                     NOTE
                     The functional scope of the multiScan depends on the selected configuration. Certain
                     functions are supported or not supported, depending on the configured variant. The
                     operating instructions describe the full functional scope of the multiScan.

                     SICK AG assumes no liability for losses or damage arising from the use of the product,
                     either directly or indirectly. This applies in particular to use of the product that does not
                     conform to its intended purpose and is not described in this documentation.


2.2         Improper use
                     Any use outside of the stated areas, in particular use outside of the technical specifica-
                     tions and the requirements for intended use, will be deemed to be incorrect use.
                     O      The device does not constitute a safety component in accordance with the
                            respective applicable safety standards for machines.
                     O      The device must not be used in explosion-hazardous areas, in corrosive environ-
                            ments or under extreme environmental conditions.
                     O      Any use of accessories not specifically approved by SICK AG is at your own risk.

                     WARNING
                     Danger due to improper use!
                     Any improper use can result in dangerous situations.
                     Therefore, observe the following information:
                     O      Product should be used only in accordance with its intended use.
                     O      All information in the documentation must be strictly observed.
                     O      Shut down the product immediately in case of damage.


2.3         Cybersecurity
                     Overview
                     To protect against cybersecurity threats, the operator must have a comprehensive
                     cybersecurity concept, which must be continuously monitored and maintained. A suita-
                     ble concept consists of organizational, technical, procedural, electronic, and physical
                     levels of defense and considers suitable measures for different types of risks. The
                     measures implemented in this product can only support protection against cybersecur-
                     ity threats if the product is used as part of such a concept.
                     You will find further information at www.sick.com/psirt, e.g.:
                     O   General information on cybersecurity
                     O      Contact option for reporting vulnerabilities
                     O      Information on known vulnerabilities (security advisories)



8     multiScan165                                                                         8028981/1X1R/2026-06-10 | SICK
                                                                                     SUBJECT TO CHANGE WITHOUT NOTICE

SAFETY INFORMATION 2

2.4            Limitation of liability
                              Relevant standards and regulations, the latest technological developments, and our
                              many years of knowledge and experience have all been taken into account when
                              compiling the data and information contained in these operating instructions. The man-
                              ufacturer accepts no liability for damage caused by:

                              O     Non-adherence to the product documentation (e.g., operating instructions)
                              O     Incorrect use
                              O     Use of untrained staff
                              O     Unauthorized conversions or repair
                              O     Technical modifications
                              O     Use of unauthorized spare parts, consumables, and accessories

2.5            Modifications and conversions

                              NOTICE
                              Modifications and conversions to the device may result in unforeseeable dangers.

                              Interrupting or modifying the device or SICK software will invalidate any warranty claims
                              against SICK AG. This applies in particular to opening the housing, even as part of
                              mounting and electrical installation.


2.6            Requirements for skilled persons and operating personnel

                              WARNING
                              Risk of injury due to insufficient training.
                              Improper handling of the device may result in considerable personal injury and material
                              damage.
                              O     All work must only ever be carried out by the stipulated persons.


                              The following qualifications are required for various activities:
                              Table 1: Activities and technical requirements
                               Activities                    Qualification
                               Mounting, maintenance         O   Basic practical technical training
                                                             O   Knowledge of the current safety regulations in the workplace
                               Electrical installation,      O   Practical electrical training
                               device replacement            O   Knowledge of current electrical safety regulations
                                                             O   Knowledge of the operation and control of the devices in their
                                                                 particular application
                               Commissioning, configura-     O   Basic knowledge of the computer operating system used
                               tion                          O   Basic knowledge of the design and setup of the described con-
                                                                 nections and interfaces
                                                             O   Basic knowledge of data transmission
                               Operation of the device for   O   Knowledge of the operation and control of the devices in their
                               the particular application        particular application
                                                             O   Knowledge of the software and hardware environment for the
                                                                 particular application




8028981/1X1R/2026-06-10 | SICK                                                                                multiScan165        9
SUBJECT TO CHANGE WITHOUT NOTICE

2 SAFETY INFORMATION

2.7         Operational safety and specific hazards

                      CAUTION
                      Optical radiation: Class 1 Laser Product
                      The accessible radiation does not pose a danger when viewed directly for up to 100
                      seconds. It may pose a danger to the eyes and skin in the event of incorrect use.
                      O    Do not open the housing. Opening the housing may increase the level of risk.
                      O    Current national regulations regarding laser protection must be observed.


                      WARNING
                      Electrical voltage!
                      Electrical voltage can cause severe injury or death.
                      O    Work on electrical systems must only be performed by qualified electricians.
                      O    The power supply must be disconnected when attaching and detaching electrical
                           connections.
                      O    The product must only be connected to a voltage supply as set out in the require-
                           ments in the operating instructions.
                      O    National and regional regulations must be complied with.
                      O    Safety requirements relating to work on electrical systems must be complied with.


                      WARNING
                      Risk of injury and damage caused by potential equalization currents!
                      Improper grounding can lead to dangerous equipotential bonding currents, which may
                      in turn lead to dangerous voltages on metallic surfaces, such as the housing. Electrical
                      voltage can cause severe injury or death.
                      O    Work on electrical systems must only be performed by qualified electricians.
                      O    Follow the notes in the operating instructions.
                      O    Install the grounding for the product and the system in accordance with national
                           and regional regulations.




10    multiScan165                                                                      8028981/1X1R/2026-06-10 | SICK
                                                                                  SUBJECT TO CHANGE WITHOUT NOTICE

PRODUCT DESCRIPTION 3

3              Product description
3.1            Scope of delivery
                              Depending on the chosen device version, the scope of delivery of a device will include
                              the following components:
                              Table 2: Scope of delivery
                               No. of     Component                          Note
                               units
                               1          Device in the ordered ver-         Complete device:
                                          sion (complete device or basic     O Components are mounted at the factory (housing
                                          device).                             and system plug).
                                          The functional scope of the
                                          device depends on the ordered      Basic device:
                                          configuration.                     O  To mount the housing and system plug yourself,
                                                                                see "Mounting the system plug on the device",
                                                                                page 41.

                                                                             All devices:
                                                                             O   Without holders and connecting cables
                               1          Printed safety notes, multilingual Brief information and general safety notes

                              The actual scope of delivery may differ for special designs, additional orders or due to
                              the latest technical changes.


3.2            Status indicators




                              Figure 1: Position of the four status LEDs, front and top view

                              1         LED1
                              2         LED2
                              3         LED3
                              4         LED4




8028981/1X1R/2026-06-10 | SICK                                                                                multiScan165       11
SUBJECT TO CHANGE WITHOUT NOTICE

3 PRODUCT DESCRIPTION

                             LED1/LED3 (color)               LED2/LED4 (color)       Description
                                    O (Red)                        O (Red)           Start up, parameterization, firmware
                                                                                     update
                                       -                              -              Off
                                  Ö Fast (red)                  Ö Fast (red)         Fatal error
                                Ö Slow (red)                    Ö Slow (red)         Recoverable error
                                   O (Green)                      O (Green)          No object detection in configured
                                                                                     fields/ready for operation
                                       –                          O (Green)          No fields configured/ready for opera-
                                                                                     tion
                                    O (Red)                       O (Yellow)         Standby / energy saving
                                   O (Green)                     Ö (Yellow)          Warning
                                   O (Yellow)                    Ö (Green)           Restart after time; input
                                   O (Green)                     Ö (Yellow)          Contamination warning
                                   Ö (Red)                       Ö (Yellow)          Contamination error
                                  Ö (Green)                       Ö (Red)            Alignment mode
                            O (Green) O (Yellow) O          O (Green) O (Yellow) O   Identifying the device
                                    (Red)                           (Red)
                                    O (Red)                  Ö (Red) Ö (Yellow)      Teach-in environment
                                   O (Yellow)                     O (Green)          Object detected

                            O = illuminated; Ö = flashing


                         NOTE
                         The LEDs are only used for additional visualization, which can provide information about
                         the device status. When the LEDs are switched off, this additional visualization is no
                         longer available, but this has no effect on the diagnostic interface (Ethernet or digital
                         I/Os).


3.3         Type label
                         Device
                         Information for identifying the sensor can be found on the bottom of the device.




12    multiScan165                                                                                8028981/1X1R/2026-06-10 | SICK
                                                                                            SUBJECT TO CHANGE WITHOUT NOTICE

PRODUCT DESCRIPTION 3




                                                                                              multiScan136

                                       á        Product ID: pid.sick.com/1099656/22221234
                                                           MULS1AA-112211 1
                                                  à        P/N 1131164   2
                                                           S/N 2221234    3                                    5
                                                           January 2022  4
                                   ß            MAC: 00:80:41:ae:fd:7e
                                       9        DC 9V ... 30V
                                                Ptyp. 10W max. 35W
                                   8
                                       7        SICK AG, 79183 Waldkirch, Germany           Made in Germany    6




                              Figure 2: multiScan type label (example)

                              1            Type code
                              2            Part number
                              3            Serial number
                              4            Production date
                              5            Conformity mark/certification mark, protection class, symbol: Observe the operating
                                           instructions!
                              6            Production site
                              7            Manufacturer
                              8            Typical power, max. power
                              9            Voltage supply
                              ß            MAC address
                              à            Data Matrix code with product data and link to product page
                              á            Web address of product page


                              Male connector
                              Information for identifying the male connector is located on the connector.




8028981/1X1R/2026-06-10 | SICK                                                                                        multiScan165   13
SUBJECT TO CHANGE WITHOUT NOTICE

3 PRODUCT DESCRIPTION


                                                                                                   1
                         7                                                                         2


                         6
                                                                                                   3



                                                                                                    4


                                                                           5
                         Figure 3: Type label for system plug (example)

                         1      Type code
                         2      Product ID with part number (P/N) and serial number (S/N)
                         3      Pin assignment or wire colors
                         4      Conformity mark/certification mark
                         5      Production site
                         6      Data Matrix code with product data and link to product page
                         7      Manufacturer


3.4           Principle of operation

3.4.1         Measurement principle
                         The device is an opto-electronic LiDAR sensor that scans the outline of its surround-
                         ings with the help of laser beams without making contact. The device measures its
                         surroundings in spherical coordinates relative to its measurement origin. This is marked
                         by a circular indentation in the center of the optics cover. If a laser beam strikes an
                         object, the position of that object is determined in terms of distance and angle.




                         Figure 4: Device with 16 scan layers, side view


                         Scan layers
                         The device has 16 scan layers:
                         O   A planar scan layer at an elevation angle of 0°, which was developed for accurate
                             navigation.
                         O    15 conical scan layers (2 oriented downwards and 13 upwards).
                         The scan layers are numbered in ascending order - starting with 1 - with descending
                         elevation angle.


14      multiScan165                                                                              8028981/1X1R/2026-06-10 | SICK
                                                                                            SUBJECT TO CHANGE WITHOUT NOTICE

PRODUCT DESCRIPTION 3




                              Figure 5: Positions of the 16 scan layers, side view, in relation to the horizon

                              1       Scan layer 1
                              2       Scan layer 16




                              Figure 6: Possible shapes of a scan layer, 3D view

                              1       Scan layer with elevation angle 0°
                              2       Scan layers with an elevation angle < 0°
                              3       Scan layers with an elevation angle > 0°




8028981/1X1R/2026-06-10 | SICK                                                                                   multiScan165   15
SUBJECT TO CHANGE WITHOUT NOTICE

3 PRODUCT DESCRIPTION




                    Figure 7: Each of the 16 horizontal point lines is created by one scan layer of the device. In the
                    example, four people have been detected by the device.


                    Due to their conical shape, all scan layers except for the one with an elevation angle
                    of 0° are bent slightly upwards or downwards when they hit a flat object depending
                    on where the cone opens out. The larger the elevation angle value, the stronger the
                    curvature.




                    Figure 8: Cone-shaped scan layer as the cause for a bent scan line




16   multiScan165                                                                               8028981/1X1R/2026-06-10 | SICK
                                                                                          SUBJECT TO CHANGE WITHOUT NOTICE

PRODUCT DESCRIPTION 3




                              Figure 9: Visualization of a scanned wall as an example of the effect of the cone-shaped scan layer


3.4.2          Distance measurement
                              The device emits beams pulsed by a laser diode. If the laser beam is reflected by an
                              object, the reflected beam is received by the sensor.
                              The distance to the object is calculated on the basis of the time that the pulsed light
                              beam requires to be reflected and received by the sensor.
                              The device uses an in-house technology from SICK. With this measurement process,
                              a measured value is formed statistical evaluation of multiple single pulses. The multi-
                              echo concept evaluates up to 691200 measured values per second. The measured
                              value consists not only of a single time-of-flight measurement, but includes evaluated
                              information from numerous pulses. This ensures a significantly more stable time and
                              distance measurement.




                                       t

                                   1       2
                              1        Emitted pulse
                              2        Receive pulse




8028981/1X1R/2026-06-10 | SICK                                                                               multiScan165     17
SUBJECT TO CHANGE WITHOUT NOTICE

3 PRODUCT DESCRIPTION

3.4.3         Multi-echo analysis
                          The distance between the device and an object is calculated via the time-of-flight of
                          the emitted pulse. The device can evaluate up to three echo signals per emitted meas-
                          uring beam to deliver reliable measurement results even under unfavorable ambient
                          conditions.




                          Figure 10: Multi-echo analysis: example industrial application for building management.

                          1       Fog
                          2       Rain
                          3       Measuring object


3.4.4         Direction measurement
                          The laser beams are emitted using internally rotating sender-receiver units (SRUs) and
                          scan the surroundings orbitally. The received measured values are assigned to the
                          associated angular cut and thus to the direction.
                          The scan layers send a set of 24 pulses over an angular range of 0.125° every 0.5°. A
                          measured value is then derived from the received signals for these pulses. This results
                          in an angular resolution of 0.5°.

                                  1°

                          1 24x 24x 24x 24x 24x 24x 24x 24x
                          Figure 11: Schematic representation of the sequence of events based on the example of a scan
                          plane

                          1       Scan plane


                          Two sender/receiver units (SRU) are installed in the device, which are offset from each
                          other by 180°. Each of these modules has eight scan layers. The two modules have
                          a different vertical tilt, depending on the device variant. The eight laser diodes of a
                          module are arranged in a circle. This arrangement results in a sensor-specific mode of
                          operation. The light beams from the laser diodes are emitted in a cone with an aperture
                          angle of 30° in both the vertical and horizontal directions.
                          The following figure shows the circular arrangement of the light beams. Due to the verti-
                          cal tilting of the two SRUs, a vertical aperture angle of up to 65° is achieved, depending
                          on the variant, with a 5° separation between the two beam fans.




18      multiScan165                                                                              8028981/1X1R/2026-06-10 | SICK
                                                                                            SUBJECT TO CHANGE WITHOUT NOTICE

PRODUCT DESCRIPTION 3




                                          1




                              Figure 12: Illustration of the circular arrangement of the laser diodes of a sender in the device

                              1      Aperture openings for eight laser diodes arranged in a circle



                                                                1                                            2




                                                        3
                                                                                                                           4




                              Figure 13: Illustrative example of the eight emitted beams of a sender in the device

                              1      Side view
                              2      Top view
                              3      Front view
                              4      Oblique view




8028981/1X1R/2026-06-10 | SICK                                                                                  multiScan165      19
SUBJECT TO CHANGE WITHOUT NOTICE

3 PRODUCT DESCRIPTION

                          The origin of each of the 16 laser beams does not lie exactly in the single origin defined
                          for the sensor see "Dimensional drawing", page 64. This applies to all three spatial
                          directions. The factory calibration of the distance, vertical and horizontal angle com-
                          pensates for this deviation from the defined origin in the best possible way. Based on
                          the characteristics of the SRUs described above, the real emitted beams deviate from
                          the respective layer origin. The calibration optimizes the angular accuracy for greater
                          distances, as the absolute error, measured in millimeters, can be minimized over all
                          distances. In the near range, however, this calibration leads to a small offset between
                          the real and the ideal beam path. This causes a greater calculated angular deviation in
                          the vertical and horizontal direction, but remains within the specified distance measure-
                          ment accuracy.
                                                                                                                à          8
                                         1
                                                                                   á                                       9
                                                                                                  7               ß
                                             4
                                                                 6
                                       5
                                                                     2                                                       3


                          Figure 14: Example sketch to illustrate the effects of the deviation between the real and defined
                          origin for the vertical direction (not to scale)

                          1       Rotation axis
                          2       Near range target
                          3       Far range target
                          4       Real origin
                          5       Defined origin
                          6       Angular deviation for near range
                          7       Angular deviation for far range
                          8       Real point of impact
                          9       Suggested point of impact
                          ß       Defined beam path
                          à       Real beam path
                          á       Guide lines


                          The vertical angle of the two light beams is identical, but there is an offset between the
                          light beams. The offset is constant over the distance. If this offset is converted into an
                          angle, there is a large angular deviation in the near range and a small deviation in the far
                          range. All deviations described are systematic.

3.4.5         Multi-layer technology
                          The multi-layer technology of the device uses 16 scan layers at different vertical angles
                          to compensate for pitch angle, for example when the device is attached to a vehicle.
                          This enables the device to reliably detect an object even, for example, when the vehicle
                          accelerates or brakes.




20      multiScan165                                                                                8028981/1X1R/2026-06-10 | SICK
                                                                                              SUBJECT TO CHANGE WITHOUT NOTICE

PRODUCT DESCRIPTION 3




                              Figure 15: Multi-plane technology

                              1      LiDAR sensor
                              2      Scan layers
                              3      Object


3.4.6          Coordinate system
                              Device coordinate system
                              The origin of the device coordinate system (X=0, Y=0, Z=0) is a single point that serves
                              as the origin and reference for all laser beams and the distance measurement of the
                              device. When no translation is applied to the device in the world coordinate system, this
                              point coincides with the origin of the world coordinate system.
                              The azimuthal (horizontal) angle of a beam is called theta. The beam at zero azimuth
                              angle lies in the middle of the main viewing direction of the device so the scan is
                              symmetrical.




8028981/1X1R/2026-06-10 | SICK                                                                       multiScan165    21
SUBJECT TO CHANGE WITHOUT NOTICE

3 PRODUCT DESCRIPTION

                                              90°
                                               Y


                                                                  Beam


                    +180°
                                               90°

                                                          theta    0°
                     -180°
                                    +/-180°
                                                     0°

                                                                        X
                                               90°




                                              -90°

                    The elevation angle (vertical angle) of a beam is designated phi and is measured rela-
                    tive to the x-y plane:
                    O    Elevation angle < 0 is above the x-y plane, i.e., for positive z-values
                    O    Elevation angle > 0 is below the x-y plane, i.e., for negative z-values
                                              -90°
                                              Z




                                                                   0°
                                                                    X
                                                             phi

                                                                   Beam


                                              90°


                    The data is always output in the device coordinate system, not in the world coordinate
                    system.

                    World coordinate system
                    The world coordinate system is based on the DIN ISO 8855 standard. The directions
                    of rotation are based on a clockwise coordinate system. The orientation of the device
                    in the world coordinate system is specified by means of a yaw angle, pitch angle and
                    roll angle and the position using the Cartesian coordinates x, y and z. If no difference
                    between the world and device coordinate systems is defined, for example to define a
                    specific mounting position, then the origin of both coordinate systems is identical and
                    corresponds to the origin of the device.




22   multiScan165                                                                        8028981/1X1R/2026-06-10 | SICK
                                                                                   SUBJECT TO CHANGE WITHOUT NOTICE

PRODUCT DESCRIPTION 3

                              The alignment of the device is defined as follows:
                              O   The beam with the azimuthal angle (horizontal) of 0° and the elevation angle
                                  (vertical) of 0° points along the x-axis
                              O    The scan layer with an elevation angle of 0° lies on the x-y plane of the coordinate
                                   system
                              O    The origin of the device coincides with the world coordinates origin
                              O    The origin of the device coordinate system lies on the axis of rotation (center of the
                                   circular optics cover) and is referenced to the mounting points.
                              O    The top of the device is oriented towards the increasing z-values of the coordinate
                                   system
                              O    The direction of rotation towards larger theta angles corresponds to the yaw angle.
                                   phi is a combination of the pitch angle and roll angle, as only two angles are
                                   specified in the spherical coordinate system.




                              1      Roll angle
                              2      pitch angle
                              3      Yaw angle


3.4.7          Filter
                              By using digital filters to pre-process and optimize the measured distance values, the
                              device can be tailored to the specific requirements of the respective application. This
                              makes it possible to prevent virtually all faults.
                              The active filter functions affect the outputted measured values. It is not possible to
                              recalculate the original measured values from the filtered output values.

3.4.7.1        Fog filter
                              The fog filter enables the device to eliminate unwanted echoes at close range. This
                              considerably lowers the probability of false activations at close range in fog.




8028981/1X1R/2026-06-10 | SICK                                                                         multiScan165     23
SUBJECT TO CHANGE WITHOUT NOTICE

3 PRODUCT DESCRIPTION




                              Figure 16: Without the fog filter: objects are       Figure 17: Using the fog filter: objects can be
                              difficult to detect through the fog due to reflec-   detected reliably because unwanted echoes
                              tions.                                               are screened out.


3.4.7.2         Echo filter
                              The echo filter screens out unwanted measurement data and signals caused by edge
                              hits, rain, dust, snow and other ambient conditions.
                              You can set whether the first, the last, or all echoes are output. With the All echoes
                              setting, the first, the second and the last echo are output.
                              The other pulses triggered by undesirable ambient conditions are not taken into
                              account.




                                       Echo 1                                              Echo 1


                                                Echo 2                                              Echo 2


                              Figure 18: Without the echo filter: The device       Figure 19: Using the echo filter (setting: last
                              receives unwanted echoes from ambient con-           echo): the device screens out unwanted ech-
                              ditions such as rain.                                oes from ambient conditions as per the set-
                                                                                   tings chosen. Measured on white objects, two
                                                                                   echoes can be separated at a distance of 1.5 m
                                                                                   or greater.


3.4.7.3         Particle filter
                              The particle filter blanks small, irrelevant reflection pulses in dusty environments and in
                              rain or snow which are caused by dust particles, raindrops, snowflakes or the like.
                              In doing so, successive scans are continuously evaluated in order to detect static
                              objects.
                              If the distance between a measured value and its temporal spatial neighbors is greater
                              than a defined threshold value, this measured value is discarded as faulty.

                              NOTE
                              If the particle filter is activated, measurement data output or the response time of the
                              field evaluation is delayed by one scan.




24        multiScan165                                                                                      8028981/1X1R/2026-06-10 | SICK
                                                                                                      SUBJECT TO CHANGE WITHOUT NOTICE

PRODUCT DESCRIPTION 3




                                      !                                                            "




                              Figure 20: Without the particle filter: Violation          Figure 21: Using the particle filter: The
                              of the contour due to dust particles in the vicin-         response time to dust particles in the detec-
                              ity of the object.                                         tion field is delayed by one scan. Particles can
                                                                                         thereby be blanked.


3.4.7.4        Moving average filter
                              The sliding average filter smooths the distance value. It does this by calculating the
                              arithmetic mean from several scans of the same point. The number of scans can be
                              configured. Each scan layer is filtered separately.
                              Table 3: Example: Moving average filter over 4 scans
                                                                              Angle (distance values in mm)
                               Scan                      1       2        3         4          5         6       7      8        9       …
                               1                         0       0     1100       1100      1150       1150   1380   1380        0       …
                               2                         0       0    1200     1200         1190       950    1500   1500        0       …
                               3                         0       0     1150    1450        1200    1200       1450   1450        0       …
                               4                         0       0     1170       1170     1220    1220       1470   1150        0       …
                               1. Output value           0       0     1155       1230      1190       1130   1450   1370        0       …
                               (scan 1-4)
                               5                         0       0        0       1110      1150       1150   1380   1380        0       …
                               2. Output value           0       0     1173       1233      1190       1130   1450   1370        0
                               (scan 2-5)
                               6                         0       0    1200        1210      1190         0    1500   1500        0       …
                               3. Output value           0       0     1173       1235      1190       1190   1450   1370        0
                               (scan 3-6)
                               7                         0    730      1150         0      1200    1200       1450   1450        0       …
                               4. Output value           0     730     1173       1163      1190       1190   1450   1370        0
                               (4-7)
                               …                         …       …        …         …         …          …      …       …        …       …

                              Individual outliers (shown in bold in the table) influence the average value.
                              Once the measured value telegram has been confirmed, the first measured value is
                              not output until after the configured number of scans. Therefore, there is always a time
                              delay equivalent to the number of scans configured for averaging. The scan counter is
                              taken from the latest scan included in the averaging process. Invalid distance values
                              (= 0) are not included in the averaging calculation, so that in these places a smaller
                              number of scans is used in the division calculation.
                              Based on the scanning frequency of 20 Hz, a measured value is generated every
                              50 ms. The time delay for data output and thus the additional response time
                              results from this base value multiplied by the number of averaging operations (e.g.,
                              2 averaging operations = 100 ms, 10 averaging operations = 500 ms).




8028981/1X1R/2026-06-10 | SICK                                                                                        multiScan165     25
SUBJECT TO CHANGE WITHOUT NOTICE

3 PRODUCT DESCRIPTION

3.4.7.5           Data reduction filter
                                  A data reduction filter is an algorithm that selects, based on various criteria, the relevant
                                  measurement data that should be excluded from the further processing.

3.4.7.5.1                  Scan layer filter
                                  The scan layer filter can be used to hide the measurement data of individual scan
                                  layers.

3.4.7.5.2                  Angular range filter
                                  The angular range filter is used to restrict the horizontal angular range output per scan.
                                  The angular range filter is switched off by default. When it is activated, it can be set to a
                                  value between - 180° and + 180°.
                                  The range can be restricted by increasing the start angle or reducing the stop angle.
                                  Please note that the angle beam orthogonal to the front screen is defined as 0°, and the
                                  direction of rotation of the device is set to counterclockwise.
                                  If a complete range of the output data is outside the angular range, it is not output. If a
                                  range is partially within the specified angular range, it is filled with 0 values.
                                                              90°
                                                              Y

                                                                               Laser beams


                                                                                   theta
                                                                                    stop
                                                                          theta
                                                               90°


                                                                           start           0°
                                  +180°
                                   -180°
                                                    +/-180°
                                                                     0°

                                                                                            X
                                                               90°




                                                              -90°
                                  Figure 22: Definition of the thetaStart and thetaStop angle (top view)


3.4.7.5.3                  Interval filter
                                  The interval filter reduces the scan output rate by a configurable factor (reduction
                                  factor). When the reduction factor is set to three, for example, the output rate is reduced
                                  to one third. In this case only every third scan is output.
                                  By combining the moving average filter with an averaging depth d and the interval filter
                                  with a reduction factor of d, a “block average filter” can be implemented that outputs
                                  the average over the previous scans while at the same time reducing the output rate by
                                  a factor d.
                                  When the interval filter is switched on, the response time increases depending on the
                                  set interval.




26          multiScan165                                                                                     8028981/1X1R/2026-06-10 | SICK
                                                                                                       SUBJECT TO CHANGE WITHOUT NOTICE

PRODUCT DESCRIPTION 3

3.4.7.6        Range filter
                              A range filter is an algorithm that uses various criteria to select relevant measurement
                              data that are set to a distance value and RSSI value of zero for further processing. Angle
                              values are retained.

3.4.7.6.1              Cubic area filter
                              When the cubic area filter is activated, it cuts out everything except for the parts of the
                              scan within an axis parallel cuboid. Note that this filter does not reduce the data, it sets
                              the data points outside the cuboid to zero.
                              The cuboid can be adjusted by setting the minimum and maximum values [mm] for the
                              X, Y and Z axis.

3.4.7.6.2              Distance filter
                              The distance filter affects the display of a spherical area around the device by limiting
                              the minimum and maximum radial distance that is measured.
                              The distance filter does not reduce the data, but sets the data points outside the radial
                              distance to zero.
                              To cut out a spherical area, set the min range to a specific radius [mm] for a very large
                              selected max range.
                              To keep a spherical area, set the max area to a specific radius [mm] and the min area to
                              0 [mm].
                              To keep a hollow sphere, set the min area and max area to a specific radius [mm].

3.4.8          Measurement data output

3.4.8.1        Data formats
                              The device offers two data output formats: MSGPACK and Compact. Both data formats
                              allow the data to be output segment by segment via UDP.
                              Both data formats contain information such as serial number and time stamp. While
                              MSGPACK can be integrated easily using existing libraries and is easy to parse, it
                              requires more computing power and bandwidth than the compact data format due
                              to the descriptive names. Compact is more efficient and requires a lower bandwidth.
                              Compared to MSGPACK, however, the compact data format is not descriptive and may
                              require more integration effort.
                              Further information see "Data format description (EN)", page 68.

3.4.8.2        Scan layer address
                              The actual position of a scan layer can vary. The exact actual vertical angle value of
                              each scan layer can be read from the device.
                              When project planning the integration of the device into a system, a deviation of
                              ± 1° from the angles specified below can be assumed. For demanding applications,
                              a smaller deviation can also be assumed, which must be verified by reading out the
                              actual vertical angles. This is possible because the extreme values rarely cumulate. A
                              tilt of up to 0.5° must be added to the actual vertical angle values read out. If only the
                              distances between the scan layers are important, this tilting within a module can be
                              neglected as it has the same effect on all scan layers.




8028981/1X1R/2026-06-10 | SICK                                                                          multiScan165    27
SUBJECT TO CHANGE WITHOUT NOTICE

3 PRODUCT DESCRIPTION

                           Table 4: Address assignment method
                           Scan layer      Measuring module allocation          DIN ISO 8855 (data        Physical (see follow-
                                           to scan layers                       output)                   ing figure for visuali-
                                                                                                          zation)
                           1               Measuring module 0                   7.3°                      -7.3°
                           2               Measuring module 0                   2.4°                      -2.4°
                           3               Measuring module 0                   0.0°                      -0.0°
                           4               Measuring module 0                   -2.5°                     2.5°
                           5               Measuring module 1                   -5.4°                     5.4°
                           6               Measuring module 0                   -7.4°                     7.4°
                           7               Measuring module 1                   -10°                      10°
                           8               Measuring module 0                   -12.5°                    12.5°
                           9               Measuring module 1                   -14.7°                    14.7°
                           10              Measuring module 0                   -17.5°                    17.5°
                           11              Measuring module 1                   -19.6°                    19.6°
                           12              Measuring module 0                   -22.7°                    22.7°
                           13              Measuring module 1                   -24.7°                    24.7°
                           14              Measuring module 1                   -27.3°                    27.3°
                           15              Measuring module 1                   -29.9°                    29.9°
                           16              Measuring module 1                   -35.3°                    35.3°




                           Figure 23: Positions of the 16 scan layers, side view, in relation to the horizon

                           1       Scan layer 1
                           2       Scan layer 16


3.4.8.3         Segmented data output
                           The device records data over an azimuth range of 360°. The data acquired within a 360°
                           rotation for all scan layers are referred to below as a frame. For data output, a frame is
                           divided into segments each of which contain the data of all scan layers for a smaller
                           azimuth interval.
                           In this case it is important to note that a segment defines a temporally related portion of
                           the data which does not (necessarily) have to be a spatially related portion of the data,
                           i.e., the azimuth range of each scan layer in a segment may be different.




28        multiScan165                                                                                  8028981/1X1R/2026-06-10 | SICK
                                                                                                  SUBJECT TO CHANGE WITHOUT NOTICE

PRODUCT DESCRIPTION 3

                              The following figure shows 12 segments each covering a range of 30°. The segment i
                              is recorded in the time interval [t_(i-1),t_i], which means the motor rotates by 30° during
                              that time interval.




                              Figure 24: Sequence of segment output. The segment i is from the time ti-1 to ti


3.4.8.4        Data preparation
                              The yellow bars in the following figures indicate the number of measuring points
                              depending on the resolution over a range of 30°.
                              Each measuring module generates 8 scan layers. The measuring modules are offset
                              from each other spatially by 180°. In accordance with DIN ISO 8855, the individual layers
                              below the zero line are output as positive and above the zero line as negative.

                              Raw data (RAW)
                              Because the device has two measuring modules that point in opposite directions and
                              the sender/receiver units on each measuring module have an azimuth offset, the azi-
                              muth range that is recorded for each scan layer in a segment is different.




                              Figure 25: Example azimuth and elevation angles for the data recorded within a segment (RAW)

                              1      Measuring module 1
                              2      Measuring module 0




8028981/1X1R/2026-06-10 | SICK                                                                                   multiScan165   29
SUBJECT TO CHANGE WITHOUT NOTICE

3 PRODUCT DESCRIPTION

                             Rectified data (RECTIFIED)
                             The data for each scan layer recorded by a measuring module are rearranged so their
                             start angles match (apart from a small deviation that is attributable to the different
                             sending times of the transmitter elements of a measuring module). This rearrangement
                             affects the latency, however, and leads to a delay of at least one time interval.




                             Figure 26: Example azimuth and elevation angles for the data recorded within a segment (RECTI-
                             FIED)

                             1        Measuring module 1
                             2        Measuring module 0


3.4.8.5         ROS driver
                             Suitable drivers for integrating the product into the ROS (Robot Operating System) are
                             available for download on the product page.

                             The product page can be accessed via the SICK Product ID: pid.sick.com/{P/N}/{S/N}
                             {P/N} corresponds to the part number of the product, see type label.
                             {S/N} corresponds to the serial number of the product, see type label (if indicated).

3.4.9           Interlaced mode
                             With interlaced mode, a finer angular resolution of the scan data can be achieved
                             through intermediate steps. For this purpose, the measuring points are shifted by an
                             angular step of 0.125° with each scan.
                             This results in the following resolutions depending on the time:
                             O    A resolution of 0.25° can be achieved after 2 revolutions (10 Hz / 100 ms).
                             O       A resolution of 0.125° can be achieved after 4 revolutions (5 Hz / 200 ms).
                             O       This increases the angular resolution from 0.5° in standard mode to 0.25° or 0.125°
                                     in interlaced mode.
                             Interlaced mode makes it possible to use smaller scanning angles, which increases
                             the point density over time. and produces more detailed 3D data. This improves object
                             detection and tracking, especially for small objects.
                             When using interlaced mode in dynamic applications, it should be noted that the
                             increased angular resolution is generated over several scans. The time-shifted data
                             points must be taken into account during processing in order to ensure reliable object
                             detection and tracking.




30        multiScan165                                                                              8028981/1X1R/2026-06-10 | SICK
                                                                                              SUBJECT TO CHANGE WITHOUT NOTICE

PRODUCT DESCRIPTION 3

                                                              0,5°


                              T1
                                              0,125°



                              T2



                                                   ...                                  ...
                              Tn




                              T8

3.4.10         Object sizes
                              Due to the angle between two scan layers, the detection of an object depends on its
                              size and distance from the device. The device may not be able to detect the object if the
                              beams go past it rather than hit it. This applies both to the width and also the height of
                              the relevant object.
                              The transmit spot is never smaller than 13 mm (diameter of the transmitter opening/
                              lens)




                              Figure 27: Laser beams pass the object without hitting it (side view)


                              The smallest object at a desired distance that can still be reliably detected is described
                              by the size obj_szmin [mm] and is defined by the following formula.

                              The formula is only valid for objects larger than 13 mm.



8028981/1X1R/2026-06-10 | SICK                                                                         multiScan165   31
SUBJECT TO CHANGE WITHOUT NOTICE

3 PRODUCT DESCRIPTION




                           objmin Minimum object angle [°]
                           αspot      Beam spot size [°], here 0.3°
                           αmeas      Measurement interval [°], horizontal 0.125°, vertical 0°
                           αres       Angular resolution [°], see table 5, page 32

                           Table 5: Typical minimum object size [mm] as a function of distance and angular resolution
                            Angular resolu-          Horizontal 0.5°                  Vertical 2.5°         Vertical 5,0° 1)
                            tion [αres]
                            Distance [mm]
                            100                      13                               13                    13
                            200                      13                               13                    19
                            500                      13                               26                    47
                            1000                     16                               51                    95
                            2000                     32                               102                   190
                            3000                     48                               153                   285
                            5000                     81                               255                   475
                            10000                    161                              511                   950
                            15000                    242                              766                   1425
                            20000                    323                              1022                  1899
                            25000                    404                              1277                  2374
                            30000                    484                              1533                  2849

                           1)     between scan layer 1 and 2 / scan layer 15 and 16


                           NOTE
                           For reliable measurement, in particular when using the device to output measured
                           values, the laser needs to hit the object with multiple beams. An object should therefore
                           be larger than the minimum object size.



3.4.11         Impact of object surfaces on the measurement
                           Reflection
                           Most surfaces produce a diffuse reflection of the laser beam in all directions. The struc-
                           ture (smooth or rough), shape (flat or curved), and color (light or dark) of the surface
                           determine how well the laser beam is reflected.
                           On very rough surfaces, a large proportion of the energy is lost due to absorption.
                           Curved surfaces produce a higher diffusion. Dark surfaces reflect the laser beam worse
                           than light ones (brilliant white plaster reflects approx. 100% of the light, while black
                           foam rubber reflects approx. 2.4%). The aforementioned surface characteristics can
                           reduce the scanning range of the device, in particular for surfaces with low remission
                           values.




32       multiScan165                                                                                       8028981/1X1R/2026-06-10 | SICK
                                                                                                      SUBJECT TO CHANGE WITHOUT NOTICE

PRODUCT DESCRIPTION 3




                              Figure 28: Reflection of light on the surface of the object


                              Angle of reflection
                              The angle of reflection corresponds to the angle of incidence. If the laser beam hits a
                              surface at right angles, the energy is optimally reflected. If the laser beam hits a surface
                              at an oblique angle, energy and range are lost accordingly.




                              Figure 29: Angle of reflection


                              Retroreflection
                              If the reflective energy is greater than 100%, the beam is not reflected diffusely in all
                              directions; instead it is reflected in a targeted way (retroreflection). Thus a large part of
                              the emitted energy can be received by the laser distance measurer. Plastic reflectors
                              (cat’s eyes), reflective tape, and triple prisms have these properties.




                              Figure 30: Retroreflection


                              Reflective surfaces
                              The laser beam is almost completely deflected on reflective surfaces. This means that
                              an object hit by the deflected beam may be detected instead of the reflective surface.




8028981/1X1R/2026-06-10 | SICK                                                                            multiScan165    33
SUBJECT TO CHANGE WITHOUT NOTICE

3 PRODUCT DESCRIPTION




                          Figure 31: Specular surfaces


                          Small objects
                          Objects that are smaller than the diameter of the laser beam cannot reflect the laser
                          light’s full energy. The portion of the light beam that does not reach the object is lost. If
                          all of the light reflected to the sensor is insufficient, the object may not be detected.
                          The portion of the light that does not reach the front object can be reflected by a larger
                          object in the background. If all of the light reflected to the sensor is sufficient, this
                          object is detected. This can lead to a corruption of the measured value.




                          Figure 32: Object smaller than the laser beam diameter


3.4.12         Scanning range
                          The scanning range of the device depends on the remission of the object to be
                          detected. The better a surface reflects the incident beam back to the device, the
                          greater the scanning range of the device.
                          Remission factor [%] 2
                          100

                           90

                           80

                           70

                           60

                           50

                           40                                                                                                             10klx
                           30
                                                                                                                                          30klx
                           20
                                                                                                                                          100klx
                           10

                            0
                                     5       10       15       20      25       30       35      40       45       50      55       60      65       70
                                  (16.40)   (32.81) (49.21) (65.62) (82.02) (98.43) (114.83) (131.23) (147.64) (164.04) (180.45) (196.85) (213.25) (229.66)

                                                                                                                          Measuring range in m (feet) 1

                          Figure 33: Scanning range as a function of the remission factor for various ambient light influences
                          (no filter activated; no influence from fog, rain or dust)




34       multiScan165                                                                                                  8028981/1X1R/2026-06-10 | SICK
                                                                                                                 SUBJECT TO CHANGE WITHOUT NOTICE

PRODUCT DESCRIPTION 3

                              Statistical error in mm (inch) 2
                                   10
                              (0.39)


                                   8
                              (0.31)


                                   6
                              (0.24)



                                   4
                              (0.16)
                                                                                                              10klx

                                   2                                                                          30klx
                              (0.08)

                                                                                                              100klx
                                   0
                                        0     10           20         30         40          50          60              70
                                            (32.81)      (65.62)    (98.43)    (131.23)    (164.04)    (196.85)       (229.66)
                                                                                               Object distance in m (feet) 1

                              Figure 34: Statistical error (σ =1) for white objects as a function of object distance for various
                              ambient light influences


                              Statistical error in mm (inch) 2
                                   10
                              (0.39)


                                   8
                              (0.31)


                                   6
                              (0.24)



                                   4                                                                                      10klx
                              (0.16)

                                                                                                                          30klx
                                   2
                              (0.08)                                                                                      100klx


                                   0
                                        0       5           10        15          20          25         30             35           40
                                             (16.40)      (32.81)   (49.21)     (65.62)     (82.02)    (98.43)        (114.83)     (131.23)
                                                                                                         Object distance in m (feet) 1

                              Figure 35: Statistical error (σ =1) for black objects as a function of object distance for various
                              ambient light influences


3.4.13         RSSI values
                              RSSI (Received Signal Strength Indicator) is the measure of the signal strength that the
                              device receives. This value is calculated for every measurement. The device therefore
                              provides, for every echo signal, an associated RSSI value for the signal strength.
                              The value 0 (zero) means that the received energy was too low to produce a valid
                              measured value and also represents the lowest possible RSSI value. An RSSI value of
                              1 represents the highest possible measured value. A linear scaling is applied between
                              the values 0 and 1 using a resolution specific to the data format (see "Data formats",
                              page 27).



8028981/1X1R/2026-06-10 | SICK                                                                                    multiScan165         35
SUBJECT TO CHANGE WITHOUT NOTICE

3 PRODUCT DESCRIPTION

                            If the RSSI value is 0, then no distance measurement is possible. There can be two
                            reasons for this:
                            O     The target object lies outside the sensing range.
                            O    The target object has an extremely low remission.
                            Please note that white paper can have very similar values as a reflector at a short
                            distance.
                            The RSSI values are sensor-specific, relative values that can vary slightly between
                            different devices and during the service life of the device.

3.4.14         Inertial measuring unit (IMU)
                            The device is equipped with an inertial measuring unit (IMU). This can be used to
                            identify vibrations and movements of the device. The IMU can output accelerations in X,
                            Y and Z as well as the position angle in yaw, pitch and roll. The orientation of the IMU
                            data is based on the coordinate system of the device.




                            1     Roll angle
                            2     pitch angle
                            3     Yaw angle


3.4.15         Contamination indication
                            The device has an optics cover to protect it. This optics cover can get dirty. Contamina-
                            tion reduces the energy emitted and received by the laser beam. As a result, scanned
                            objects appear to have a lower remission factor than they actually have and, from a cer-
                            tain degree of contamination, it will no longer be possible to perform measurements.
                            The contamination is constantly measured by a separate system during operation. A
                            contamination warning is output first for the different degrees of contamination. If the
                            optics cover is not cleaned and contamination increases, then a contamination error is
                            output. These thresholds can be individually adjusted.
                            The device supports a contamination indication over the full 360°. 12 sectors are
                            monitored independently. When a scan configuration of, for example, -144° to +144°
                            is selected, sectors without measurement outside the configured viewing range are set
                            to deactivated status. Each sector can be individually enabled for the contamination
                            indication.



36       multiScan165                                                                          8028981/1X1R/2026-06-10 | SICK
                                                                                         SUBJECT TO CHANGE WITHOUT NOTICE

PRODUCT DESCRIPTION 3

                              You can select different settings, depending on the application in which the device is
                              used.
                              Warning/error output
                              O   All sectors contaminated: If all sectors have the same or a higher value, the
                                  device status “Contamination warning” or “Contamination error” is displayed.
                              O    One sector contaminated: At least one sector must have a level of “Warning” or
                                   “Error” for a contamination warning or contamination error to be displayed.
                              O    No output: Warning and error device status display is deactivated. The contamina-
                                   tion measurement for the individual sectors continues to be performed but has no
                                   effect on the device status.
                              Sensitivity: Low, medium, high: Threshold for triggering contamination warnings and
                              errors. The parameter makes it possible to tailor the display to the specific require-
                              ments of the application.
                              Sector selection: The 30° sectors of the sensor can be activated and deactivated
                              depending on the relevant aperture angle and mounting situation. Non-selected sec-
                              tors are ignored in the contamination indication. They therefore do not result in a warn-
                              ing or an error if contaminated.
                              Evaluation for blocked sectors: If sectors of the sensor become covered by objects in
                              the near range (a few centimeters from the optics cover), these can optionally be output
                              as “heavy contamination” (=contamination error) or not evaluated.
                              Response time: This can be used to define how quickly the contamination should result
                              in an error or warning.
                              Default setting: In the default setting, the contamination display is deactivated. The
                              monitoring of individual sectors is active and can be seen for each sector in the user
                              interface and the command interface to assist with integrating the device into the
                              application.
                              Strategy and evaluation are deactivated so no device warnings or errors are triggered.
                              All associated parameters can be permanently changed.

                              NOTE
                              O    The cleaner the application environment is, the lower you can set the contamina-
                                   tion indication sensitivity. If a high precision of the measured values is required, the
                                   contamination indication must be set to the most sensitive level.
                              O    Sectors that are not relevant should be deactivated to ensure a higher availability.

                              Contamination warnings and contamination errors are indicated on the display ele-
                              ments of the device see "Status indicators", page 11.

3.4.16         Field evaluation
                              The device uses the integrated field evaluation to evaluate the fields within its scan
                              area. You can use the field evaluation, for example, to implement systems for collision
                              protection, object protection or access monitoring.
                              Up to 48 fields can be defined. The number of allowed simultaneously active fields can
                              change depending on the configuration that has been set. For a typical configuration
                              (echo filter: last echo, no data preparation, IMU or particle filter active, web interface
                              closed), 20 fields can be active simultaneously. Under real-life ambient conditions, it
                              may also be possible to have more simultaneously active fields.




8028981/1X1R/2026-06-10 | SICK                                                                          multiScan165    37
SUBJECT TO CHANGE WITHOUT NOTICE

3 PRODUCT DESCRIPTION

                              Limitations of simultaneously active fields:
                              O    More active fields results in a greater computing effort and therefore a higher
                                   system load.
                              O    Only the measuring points located within an active field result in an additional
                                   system load.
                              O    A too high system load can lead to performance problems or system errors.
                              O    The system load can be reduced by deactivating other functions, for example GUI,
                                   filter, and measurement data output, which may allow more fields to be active at
                                   the same time.
                              O    We recommend testing the exact application requirements.




                              Figure 36: Principle of field evaluation


                              Multiple groups can be created, depending on application requirements. A group can
                              be switched to active either by switching inputs of the device, telegrams, or perma-
                              nently. A group can comprise several fields, each of which can be configured for the
                              particular situation via its own evaluation.
                              The results of the evaluation can be linked to a switching output. It is also possible to
                              link the respective evaluation to other signals using logical operands (AND, OR, XOR, …).
                              For more information, see the online help in SOPASair see "Overview", page 51.

3.4.16.1         Delay time of field evaluation
                              The delay time of the field evaluation depends on several parameters. These include
                              the location and time at which an object enters the sensor detection range in relation to
                              the laser position. An evaluation is performed after each scan cycle.
                              The delay time with which the field status is output is also influenced by:
                              O   Number of activated fields
                              O    Digital outputs
                              O    Filter
                              O    Measurement data streaming function




38         multiScan165                                                                          8028981/1X1R/2026-06-10 | SICK
                                                                                           SUBJECT TO CHANGE WITHOUT NOTICE

TRANSPORT AND STORAGE 4

4              Transport and storage
4.1            Transport

                              NOTICE
                              Damage due to improper transport!
                              O    The product must be packaged with protection against shock and damp.
                              O    Recommendation: Use the original packaging.
                              O    Note the symbols on the packaging.
                              O    Do not remove packaging until immediately before you start mounting.


4.2            Unpacking
                              O    To protect the device against condensation, allow it to equilibrate with the ambient
                                   temperature before unpacking if necessary.
                              O    Handle the device with care and protect it from mechanical damage.

4.3            Transport inspection
                              Immediately upon receipt in Goods-in, check the delivery for completeness and for any
                              damage that may have occurred in transit. In the case of transit damage that is visible
                              externally, proceed as follows:
                              O    Do not accept the delivery or only do so conditionally.
                              O    Note the scope of damage on the transport documents or on the transport compa-
                                   ny's delivery note.
                              O    File a complaint.

                              NOTE
                              Complaints regarding defects should be filed as soon as these are detected. Damage
                              claims are only valid before the applicable complaint deadlines.


4.4            Storage
                              O    Do not store outdoors.
                              O    Store in a place protected from moisture and dust.
                              O    Recommendation: Use the original packaging.
                              O    Do not expose to any aggressive substances.
                              O    Protect from sunlight.
                              O    Avoid mechanical shocks.
                              O    Storage temperature: see "Technical data", page 60.
                              O    Relative humidity: see "Technical data", page 60.
                              O    For storage periods of longer than 3 months, check the general condition of all
                                   components and packaging on a regular basis.




8028981/1X1R/2026-06-10 | SICK                                                                       multiScan165    39
SUBJECT TO CHANGE WITHOUT NOTICE

5 MOUNTING

5             Mounting
5.1           Mounting instructions
                          O    Observe the technical data.
                          O    Protect the sensor from direct sunlight.
                          O    To prevent condensation, avoid exposing the device to rapid changes in tempera-
                               ture.
                          O    The mounting site has to be designed for the weight of the device.
                          O    The device can be mounted in any position.
                          O    It should be mounted so that it is exposed to as little shock and vibration as possi-
                               ble. Optional mounting accessories are available, see "Accessories", page 67.
                          O    Regularly check the tightness of the fixing screws.
                          O    Do not mount the device on or directly in front of a bright metallic surface or other
                               reflective surface, since reflections can falsify the measurements.
                          O    Avoid having shiny or reflective surfaces in the scanning range, e.g., stainless
                               steel, aluminum, glass, reflectors, or surfaces with these types of coatings.
                          O    Protect the device from moisture, contamination, and damage.
                          O    Make sure that the status indicator is clearly visible.
                          O    Do not affix any labels or stickers to the optics cover.
                          O    Do not subject the device to excessive shock or vibrations. In systems subjected to
                               heavy vibrations, secure the fixing screws with screw-locking devices.
                          O    The ventilation element must not be sealed off during installation.
                          O    The device must be mounted in such a way that no water can pool on the ventila-
                               tion element. When using a mounting bracket, we recommend providing a drill
                               hole in the area of the ventilation element.
                          O    Ensure suitable ESD protective measures during mounting.

5.1.1         Ventilation element
                          The ventilation element ensures an improved pressure equalization and allows the
                          exchange of air and heat between the housing and surroundings.
                          The breathable membrane allows ambient air to either penetrate into the device or
                          escape again depending on the prevailing ambient conditions see "Dimensional draw-
                          ing", page 64.
                          In particular for applications with frequently changing environmental influences (e.g.,
                          large temperature fluctuations or rapid temperature changes) or with standing water,
                          the ventilation element ensures a reliable pressure equalization and thereby relieves
                          the seals and adhesive joints of the housing. This can improve the expected service life
                          of the device in the application.

                          Note the following information:
                          O   Do not affix any labels or stickers to the ventilation element.
                          O    Do not paint over the ventilation element.
                          O    Devices that have been subjected to a long period of moisture or very rapid
                               temperature changes need to first equilibrate after being switched on. In some
                               circumstances, therefore, a period of time should be allowed before measurement
                               readiness of the device because any moisture in the housing must first be taken up
                               by the air in the housing, which is heated up through the operation of the device,
                               so that it can then escape via the ventilation element. Depending on the nature of
                               the precipitated moisture, this time period might be several minutes or even up to
                               hours.




40      multiScan165                                                                            8028981/1X1R/2026-06-10 | SICK
                                                                                          SUBJECT TO CHANGE WITHOUT NOTICE

MOUNTING 5

5.2            Mounting the system plug on the device
                              Notes

                                   NOTICE
                                   Risk of damage due to electrostatic discharge
                                   Electrostatic discharge from the human body may damage the device or the sys-
                                   tem plug.
                                   O      Take the necessary ESD precautions when mounting the system plug.
                                   O      Do not touch the contact surfaces with your fingers.

                              O    Depending on the device variant ordered, the system plug is either already
                                   mounted on the device or is supplied separately.
                              O    Compliance with the technical specifications of the device is possible only when
                                   the system plug is mounted.

                              Prerequisites
                              O    The system plug, the seal on the device, and the entire connection area are free of
                                   contamination and moisture and show no signs of damage.

                              Fitting the system plug



                                                      1                                          3




                                                      2




                                                                                             4




                              1        System plug, installation at top
                              2        System plug, installation at bottom
                              3        Device - system plug not mounted
                              4        System plug




8028981/1X1R/2026-06-10 | SICK                                                                       multiScan165     41
SUBJECT TO CHANGE WITHOUT NOTICE

5 MOUNTING

                     1.   Attach the system plug at the desired installation position on the device.
                     2.   Tighten the screws (tightening torque: max. 2 Nm).


5.3         Mounting the device
                     Prerequisites
                     O    The connector is mounted on the device.

                     Procedure

                     1.   Mount the device in a suitably prepared bracket using the fixing holes provided.
                          Mounting brackets are available as accessories.
                     2.   Make the electrical connection. Attach and tighten a voltage-free cable.
                     3.   Align the vertical center line of the field of view of the device with the center of the
                          area to be monitored. The marking on the upper side of the optics cover serves as
                          a bearing alignment aid.
                     4.   Switch on the supply voltage.
                     m    After successful initialization, the two status LEDs light up green. The device is
                          ready for use.
                     5.   Perform a fine adjustment using a test target and, if necessary, use the alignment
                          aid.

                     Further topics
                     O    "Mounting the system plug on the device", page 41
                     O    "Dimensional drawing", page 64
                     O    "Accessories", page 67
                     O    "Connecting the device electrically", page 50

5.4         Mounting multiple devices

                     NOTICE RISK OF INTERFERENCE FROM OTHER DEVICES!
                     Radiation sources with a wavelength of 905 nm can cause interference if they affect the
                     device directly.

                     The device has been designed to minimize the probability of mutual interference,
                     including between different LiDAR sensors. To rule out even the slightest effects on
                     the measurement accuracy, the devices should be arranged in such a way that as few
                     laser beams as possible are received from other devices.




42    multiScan165                                                                         8028981/1X1R/2026-06-10 | SICK
                                                                                     SUBJECT TO CHANGE WITHOUT NOTICE

ELECTRICAL INSTALLATION 6

6              Electrical installation
6.1            Wiring instructions

                              NOTE
                              Pre-assembled cables can be found on the product page.
                              The product page can be accessed via the SICK Product ID: pid.sick.com/{P/N}/{S/N}
                              {P/N} corresponds to the part number of the product, see type label.
                              {S/N} corresponds to the serial number of the product, see type label (if indicated).


                              NOTICE
                              Faults during operation and defects in the device or the system
                              Incorrect wiring may result in operational faults and defects.
                              O    Follow the wiring notes precisely.


                              The electrical connection of the device is configured as an M12 round connector.
                              The enclosure rating stated in the technical data is achieved only with screwed plug
                              connectors or protective caps.
                              All circuits connected to the device must be configured as SELV or PELV circuits. SELV
                              = safety extra-low voltage, PELV = protective extra-low voltage.
                              Protect the device with an external 3 A slow-blow fuse at the beginning of the supply
                              cable.
                              Connect the connecting cables in a de-energized state. Do not switch on the supply
                              voltage until installation is complete and all connecting cables are connected to the
                              device and controller.
                              Wire cross-sections in the supply cable from the customer’s power system must be
                              implemented in accordance with the applicable standards.
                              Check the device configuration for the inputs/outputs before connecting the I/O cable.
                              Avoid tensile loads to the connecting cables.
                              Maximum cable lengths for the voltage supply, depending on the available power sup-
                              ply voltage. The maximum cable length and the permissible minimum voltage at the
                              power supply unit can be calculated with the help of the calculation rule in the following
                              sections.
                              Parallel connection of the digital outputs of several identical devices – for example in
                              PNP mode – to a common input (e.g. a PLC) is not recommended. For safe and reliable
                              signal processing, an external logic or decoupling circuit, for example with diodes,
                              should be used.




8028981/1X1R/2026-06-10 | SICK                                                                        multiScan165    43
SUBJECT TO CHANGE WITHOUT NOTICE

6 ELECTRICAL INSTALLATION




6.2         Prerequisites for safe operation of the device

                      WARNING
                      Risk of injury and damage caused by electrical current!
                      As a result of equipotential bonding currents between the device and other grounded
                      devices in the system, faulty grounding of the device can give rise to the following
                      dangers and faults:
                      O    Dangerous voltages are applied to the metal housings.
                      O    Devices will behave incorrectly or be destroyed.
                      O    Cable shielding will be damaged by overheating and cause cable fires.
                      Remedial measures
                      O    Only skilled electricians should be permitted to carry out work on the electrical
                           system.
                      O    If the cable insulation is damaged, disconnect the voltage supply immediately and
                           have the damage repaired.
                      O    Ensure that the ground potential is the same at all grounding points.
                      O    Where local conditions do not meet the requirements for a safe earthing method,
                           take appropriate measures. For example, ensure low-impedance and current-car-
                           rying equipotential bonding.


                      The device is connected to the peripheral devices (any local trigger sensor(s), system
                      controller) via shielded cables. The cable shield – for the data cable, for example – rests
                      against the metal housing of the device.
                      The device can be grounded through the cable shield or through a blind tapped hole in
                      the housing, for example.
                      If the peripheral devices have metal housings and the cable shields are also in contact
                      with their housings, it is assumed that all devices involved in the installation have the
                      same ground potential.
                      This is achieved by complying with the following conditions:
                      O    Mounting the devices on conductive metal surfaces
                      O    Correctly grounding the devices and metal surfaces in the system
                      O    If necessary: low-impedance and current-carrying equipotential bonding between
                           areas with different ground potentials




44    multiScan165                                                                         8028981/1X1R/2026-06-10 | SICK
                                                                                     SUBJECT TO CHANGE WITHOUT NOTICE

ELECTRICAL INSTALLATION 6

                                      1                                         2                                          3


                                    System                                     SICK
                                   Controller                                 Device                               Power Supply




                                                            I

                                                                                                       =8
                                                                                                       =9


                                     7          6       U            5         4

                              Figure 37: Example: Occurrence of equipotential bonding currents in the system configuration

                              1        System controller
                              2        Device
                              3        Voltage supply
                              4        Grounding point 2
                              5        Closed current loop with equalizing currents via cable shield
                              6        Ground potential difference
                              7        Grounding point 1
                              8        Metal housing
                              9        Shielded electrical cable


                              If these conditions are not fulfilled, equipotential bonding currents can flow along the
                              cable shielding between the devices due to differing ground potentials and cause the
                              hazards specified. This is, for example, possible in cases where there are devices within
                              a widely distributed system covering several buildings.
                              Remedial measures
                              The most common solution to prevent equipotential bonding currents on cable shields
                              is to ensure low-impedance and current-carrying equipotential bonding. If this equipo-
                              tential bonding is not possible, the following solution approaches serve as a sugges-
                              tion.

                              NOTICE
                              We expressly advise against opening up the cable shields. This would mean that the
                              EMC limit values can no longer be complied with and that the safe operation of the
                              device data interfaces can no longer be guaranteed.

                              Measures for widely distributed system installations
                              On widely distributed system installations with correspondingly large potential differ-
                              ences, the setting up of local islands and connecting them using commercially availa-
                              ble electro-optical signal isolators is recommended. This measure achieves a high
                              degree of resistance to electromagnetic interference.




8028981/1X1R/2026-06-10 | SICK                                                                              multiScan165       45
SUBJECT TO CHANGE WITHOUT NOTICE

6 ELECTRICAL INSTALLATION

                          1                    2                     2                     3                       4

                                            Electro-               Electro-
                        System               optical                optical               SICK                   Power
                       Controller            signal                 signal               Device                  Supply
                                            isolator               isolator




                                    6                                                     5

                         =7            =8          =9

                     Figure 38: Example: Prevention of equipotential bonding currents in the system configuration by
                     the use of electro-optical signal isolators

                     1        System controller
                     2        Electro-optical signal isolator
                     3        Device
                     4        Voltage supply
                     5        Grounding point 2
                     6        Grounding point 1
                     7        Metal housing
                     8        Shielded electrical cable
                     9        Fibers


                     The use of electro-optical signal isolators between the islands isolates the ground loop.
                     Within the islands, a stable equipotential bonding prevents equalizing currents on the
                     cable shields.
                     Measures for small system installations
                     For smaller installations with only slight potential differences, insulated mounting of the
                     device and peripheral devices may be an adequate solution.




46    multiScan165                                                                           8028981/1X1R/2026-06-10 | SICK
                                                                                       SUBJECT TO CHANGE WITHOUT NOTICE

ELECTRICAL INSTALLATION 6

                                      1                                  2                                  3



                                    System                              SICK
                                   Controller                                                         Power Supply
                                                                       Device




                                                                                          5



                                     8                    U            6                                   4
                                                7

                                   =9           =ß

                              Figure 39: Example: Prevention of equipotential bonding currents in the system configuration by
                              the insulated mounting of the device

                              1       System controller
                              2       Device
                              3       Voltage supply
                              4       Grounding point 3
                              5       Insulated mounting
                              6       Grounding point 2
                              7       Ground potential difference
                              8       Grounding point 1
                              9       Metal housing
                              ß       Shielded electrical cable


                              Even in the event of large differences in the ground potential, ground loops are effec-
                              tively prevented. As a result, equalizing currents can no longer flow via the cable shields
                              and metal housing.

                              NOTICE
                              The voltage supply for the device and the connected peripheral devices must also
                              guarantee the required level of insulation.
                              Under certain circumstances, a tangible potential can develop between the insulated
                              metal housings and the local ground potential.


6.3            Calculation rule
                              The device can be connected via optional accessories, see "Accessories", page 67.
                              The following formulas can be used to estimate the required cable lengths or supply
                              voltages. Other conditions of the system must be considered in detail.

                              Formula for the voltage drop to be considered

                                        I•2•L
                               ΔV=            •ρ•(1 + α•(T - T0))
                                          A



8028981/1X1R/2026-06-10 | SICK                                                                              multiScan165    47
SUBJECT TO CHANGE WITHOUT NOTICE

6 ELECTRICAL INSTALLATION

                      Formula for permissible length of cable

                                 Δ V•A
                      L=
                            2•I•ρ•(1 + α•(T - T0))


                      Sample calculations
                      Prerequisites:
                      O   Steady state of the voltage supply
                      O    Only applies for copper cable material
                      Table 6: Values used in both example calculations
                      Cable properties
                      A = 0.34 • 10-6 m²                                  Cross-section of the cable surface [m2]
                      ρ = 1.72 • 10-8 Ωm                                  Specific resistance of copper [Ωm]
                      α = 3.9 • 10-3 K-1                                  Temperature coefficient of copper [1/K]
                      Ambient conditions
                      T0 = 20 °C                                          Reference temperature [°C]
                      T = 80 °C                                           Cable temperature [°C]
                      Cable load
                      I = P/U = 1.46 A                                    Load current I [A]
                      P = 35 W                                            Maximum expected power consumption P [W]
                      U= 24 V                                             Supply voltage U [V]

                      Table 7: Example: voltage drop to be considered for cable part no. 2096241
                      L = 10 m                                            Cable length [m]
                             I•2•L                              Voltage drop ΔV [V]
                      ΔV=          •ρ•(1 + α•(T - T0)) = 1.82 V
                               A

                      Table 8: Calculation of the cable length for allowed voltage drop of 1.82 V
                      ΔV = 1.82 V                                         Voltage drop on the cable [V]
                                 Δ V•A                                    Permissible length of cable [m]
                      L=                           = 10 m
                            2•I•ρ•(1 + α•(T - T0))


6.4         Cable reserve on system plug
                      Allow for sufficient cable reserve of the supplied cables at the system plug. You can
                      easily exchange the device with the cable reserve if needed.
                      Keep the cable reserve only long enough that the system plug cannot be accidentally
                      plugged into an adjacent device when replacing the device! This prevents a device with
                      an incorrect configuration being put into operation. Experience has shown that 200 to
                      300 mm of cable reserve on the device is ideal.
                      The reserve cable should be laid as a drip loop so no moisture (e.g., condensation) is
                      directed towards the device but instead drips off the cable beforehand.


6.5         Pinouts

                      NOTE
                      The recommended connecting cables and their associated technical data can be found
                      on the online product page.
                      The product page can be accessed via the SICK Product ID: pid.sick.com/{P/N}/{S/N}
                      {P/N} corresponds to the part number of the product, see type label.
                      {S/N} corresponds to the serial number of the product, see type label (if indicated).



48    multiScan165                                                                                 8028981/1X1R/2026-06-10 | SICK
                                                                                             SUBJECT TO CHANGE WITHOUT NOTICE

ELECTRICAL INSTALLATION 6


                              NOTE
                              The connections depend on the mounted system plug.


                              PWR/IOs connection
                              2                      1

                                                     5

                              3                      4

                              Figure 40: Male connector, M12, 5-pin, A-coded


                              Table 9: Pin assignment for PWR & 3 I/Os connection (part no. 2116047)
                               Contact           Signs                  Description                                   Wire color, part num-
                                                                                                                      ber 2095733 1)
                               1                 Vs                     Supply voltage: +9 ... +30 V DC               Brown
                               2                 IN2 / OUT2             Digital input 2 / digital output 2            White
                               3                 GND                    Supply voltage: 0 V                           Blue
                               4                 IN1 / OUT1             Digital input 1 / digital output 1            Black
                               5                 IN3 / OUT3             Digital input 3 / digital output 3            Gray

                              1)    Data only valid when using the specified connecting cable with flying leads, which is available as an acces-
                                    sory

                              2                    1
                              3                   10
                              11                   9
                              4                    8
                              5                   12
                              6                    7

                              Figure 41: M12 male connector, 12-pin, A-coded


                              Table 10: Pin assignment for PWR & 8 I/Os connection (part no. 2130754)
                               Contact           Labels                 Description                                   Wire color part no.
                                                                                                                      2119045 1)
                               1                 IN1/OUT1               Digital input 1 / digital output 1            Brown
                               2                 GND                    Supply voltage: 0 V                           Blue
                               3                 IN2/OUT2               Digital input 2 / digital output 2            White
                               4                 IN7/OUT7               Digital input 7 / digital output 7            Green
                               5                 IN8/OUT8               Digital input 8 / digital output 8            Pink
                               6                 IN3/OUT3               Digital input 3 / digital output 3            Yellow
                               7                 IN4/OUT4               Digital input 4 / digital output 4            Black
                               8                 IN6/OUT6               Digital input 6 / digital output 6            Gray
                               9                 Vs                     Supply voltage: +9 ... +30 V DC               Red
                               10                IN5/OUT5               Digital input 5 / digital output 5            Violet
                               11                –                      –                                             Gray-pink
                               12                –                      –                                             Red-blue

                              1)    Data only valid when using the specified connecting cable with flying leads, which is available as an acces-
                                    sory




8028981/1X1R/2026-06-10 | SICK                                                                                            multiScan165        49
SUBJECT TO CHANGE WITHOUT NOTICE

6 ELECTRICAL INSTALLATION

                      Ethernet connection
                      1                2



                      4                3

                      Figure 42: M12 female connector, 4-pin, D-coded


                      Table 11: Pin assignment for Ethernet connection (part no. 2116047 & 2130754)
                       Contact       Signs              Description
                       1             TX+                Sender+
                       2             RX+                Receiver+
                       3             TX-                Sender-
                       4             RX-                Receiver-


6.6         Connecting the device electrically

                      NOTICE
                      Observe the wiring instructions, see "Wiring instructions", page 43.

                      1.   Ensure that the power supply unit can provide the necessary voltage and current
                           for operating the device. Particular attention must be given to the voltage drop
                           across the supply line (see "Calculation rule", page 47),and for digital outputs the
                           additional voltage drop in the opposite direction and the required start-up power
                           (see "Mechanics/Electronics", page 62), without which the device cannot start
                           reliably.
                      2.   Ensure the voltage supply is not connected.
                      3.   Connect the device according to the connection diagram, see "Pinouts", page 48.




50    multiScan165                                                                            8028981/1X1R/2026-06-10 | SICK
                                                                                        SUBJECT TO CHANGE WITHOUT NOTICE

COMMISSIONING 7

7              Commissioning
7.1            Operation using SOPASair
                              The browser-based SOPASair software can be used to parameterize the device and for
                              service and diagnostic purposes.
                              To parameterize the device, you will require a computer with a web browser installed
                              and a free Ethernet connection. Alternatively, the connection can be established via a
                              USB connection using an Ethernet USB adapter.

7.1.1          Opening the web server user interface (SOPASair)
                              Before opening the user interface, perform the following work steps:
                              O   Connect the device to the computer via Ethernet.
                              O        Set up the voltage supply for the device.
                              O        Ensure that the computer and device are located in the same network.
                              O        Ensure that the computer uses a different IP address than the device, but is in the
                                       same IP address range (e.g. 192.168.0.xxx)
                              Open the user interface:
                              1. Open web browser (recommendation: Google Chrome).
                              2. Enter the device IP address into the address line. The standard IP address is:
                                 192.168.0.1
                              m  The SOPASair user interface is displayed.

7.1.2          Overview

                                                                        2                                  3

                                   4                5




                               1


                              1         Show and hide menu bar
                              2         Menu path for opened menu
                              3         Status indicators | toolbar
                              4         Menu panel Status and Product
                              5         Workspace with live image and menu panels


                              Status indicators


                                          LED display

                                          Device connection status



8028981/1X1R/2026-06-10 | SICK                                                                           multiScan165    51
SUBJECT TO CHANGE WITHOUT NOTICE

7 COMMISSIONING



                                      Measurement status

                            Toolbar

                                      Save permanently


                                      Open login window
                                      Change the user interface language

                                      Open the global online help. The same icon is also displayed for help contents
                                      right next to parameters.

                                      Device menu

                            Navigation

                            1.   Click on the desired menu.
                            m    The workspace changes depending on the selected menu.

7.1.3         Navigating in the live image
                            Overview
                            The view of the scan data In SOPASair can be adjusted using the computer mouse.

                            Using the computer mouse
                            Function                                      Computer mouse
                            Zoom in and zoom out                          Using the scroll wheel
                            Rotate and tilt the view                      Left mouse button
                            Move the view                                 Right mouse button


7.1.4         User levels
                            The device has different user levels.
                            The user levels have different authorizations for configuring the device.
                            The current user level is displayed in the Log in panel.

                            Activate the user level during initial commissioning of the device
                            1.
                                 Click on the       button.
                            m    The Log in to device input screen opens. The Service user level is selected.
                            2.   Enter the password servicelevel and click on Log in.
                            3.   Activate the desired user level.

                            Logging in to the device
                            1.  User levels have been activated.
                            2.
                                 Click on the       button.
                            m    The Log in to device input screen opens.
                            3.   Select user level(User level), enter a password(Password) then click Login in.

                            User levels                  Password                  User and authorizations
                            Maintenance                  main                      Customers: Display only, no configu-
                                                                                   ration
                            Authorized customer          client                    Technical staff: Install and configure
                                                                                   device


52      multiScan165                                                                             8028981/1X1R/2026-06-10 | SICK
                                                                                           SUBJECT TO CHANGE WITHOUT NOTICE

COMMISSIONING 7

                               User levels               Password                    User and authorizations
                               Service                   servicelevel                Service staff: Make advanced config-
                                                                                     uration settings


                              NOTE
                              Change the passwords during initial commissioning to protect your device.
                              A higher user level can change the password of a lower user level.


7.1.5          Changing the password
                              Overview
                              Passwords should meet the following requirements:
                              O   Use secure passwords. Information on secure passwords can be obtained, for
                                  example, from the authority responsible for IT security.
                              O    Protect passwords from unauthorized access.
                              O    Do not assign a password more than once.

                              Procedure

                              1.   Establish a connection to the product in the web browser.
                              2.
                                   Select     .
                              3.   Log in with the last assigned password.
                              4.   Select Change password.
                              5.   Assign a new password.
                              m    The new password is valid immediately.

7.1.6          Resetting the password

                              NOTE
                              The responsible SICK sales company or the responsible SICK service partner carefully
                              checks each code request to reset the password. A risk of deception by third parties
                              nevertheless exists. The operating entity should therefore take suitable security meas-
                              ures.
                              The operating entity should also take suitable measures to limit, as best as possible,
                              access to the product. This includes, in particular, physical access as well as access to
                              the software interfaces of the product.

                              Resetting the password for the Service user
                              1.
                                   Click on the       button.
                              m    The Log in input screen opens.
                              2.   Click on Password forgotten?.

                              Resetting the password for the Authorized client/Maintenance personnel user
                              1.  The password for the Service user has been reset.
                              2.  Save the device parameterization using the parameter export in SOPAS ET.
                              3.
                                  Click on the     button.
                              4.  Select Reset to factory settings.

7.1.7          Displaying live data
                              1.   In SOPASair: Open the user interface see "Opening the web server user interface
                                   (SOPASair)", page 51.




8028981/1X1R/2026-06-10 | SICK                                                                         multiScan165    53
SUBJECT TO CHANGE WITHOUT NOTICE

7 COMMISSIONING

                             If no scan data are shown:
                             1.    Click Configuration > Defaults.
                             2.    Select Measuring.

                             Notes
                             O    The visualized live data is displayed at a lower refresh rate than the actual measur-
                                  ing frequency.

7.1.7.1         Activating/deactivating filters
                             Prerequisites
                             O    You must be logged into the device see "User levels", page 52.

                             Selecting filters

                             1.   Menu: Select Configuration > Default.
                             2.   Activate or deactivate one or more filters.

                             Selecting the data reduction filter/region of interest filter

                             1.   Menu: Select Application > Data output .
                             2.   Activate or deactivate one or more filters.

7.1.8           Configuring interfaces
                             Settings for using the multifunctional I/Os can be configured in the Application >
                             Inputs and outputs menu. In addition, the current status and saved function of the
                             input/output are displayed.
                             The multifunctional I/Os are switchable and can therefore each be used as either a
                             digital input or output.
                             The inputs may switch on, switch off, and switch over analysis cases, for example. The
                             inputs can also be used to activate other functions, such as measurement data output
                             triggering.
                             The outputs can be used as digital switching outputs, for example to ground (PNP)
                             (depending on the device type). For each output, it is necessary to define whether it is
                             to be switched by means of CoLa telegrams, or whether it is being used to signal device
                             readiness (Device Ready).


7.2             Operation in SOPAS ET
                             Execute the functions listed below via the SOPAS ET configuration software.
                             Functions
                             O   Install firmware updates
                             O    Import and export data

                             NOTE
                             To use the sensor with SOPAS ET, we recommend using port 2122 or port 80 in
                             SOPAS ET. When using the aforementioned ports, no limitation with regard to SOPASair
                             can be expected.
                             If a legacy protocol (CoLa A/B) is used on the ports 2111 and 2112, however, functional
                             limitations in the SOPAS ET interface may arise.

                             The most up-to-date version of the SOPAS ET software can be downloaded from
                             www.sick.com/software, category: Configuration software, software type: SOPAS ET.




54        multiScan165                                                                             8028981/1X1R/2026-06-10 | SICK
                                                                                             SUBJECT TO CHANGE WITHOUT NOTICE

COMMISSIONING 7

7.2.1          Operation with SOPAS ET
                              Version 3.3.3 and higher of the SOPAS Engineering Tool (SOPAS ET) software can be
                              used to parameterization of the device and for service and diagnostic purposes.
                              To configure the device, you will require a computer with SOPAS ET installed and a
                              free Ethernet connection. Alternatively, the connection can be established via a USB
                              connection using an Ethernet USB adapter.

                              1.   Connect the communication interface (Ethernet, 4-pin M12 female connector) of
                                   the device to the computer.
                              2.   Switch on and start the computer.
                              3.   Supply the device with voltage (5-pin M12 male connector, supply voltage
                                   9 … 30 V DC).
                              m    After successful initialization, the two status LEDs light up green. The device is
                                   ready for use.

                              NOTE
                              To use SOPAS ET with the device, you need a device description file (SDD, SOPAS
                              Device Description) for this device. You can install this within SOPAS ET using the
                              device catalog. The device description file is saved on the device and can be installed
                              there. Alternatively, installation is possible from the SICK website (Internet connection
                              required).

                              Following installation of the device description file, the device can be selected from the
                              device catalog and added to a project.
                              A connection to the device is established via the communication interface. The connec-
                              tion must be activated for data transmission (online).
                              Certain functions (e.g., Edit parameters) require you to be logged in to the device
                              (Device > Log In menu, User Level: Authorized customer, Password (factory default):
                              client).
                              Table 12: Keywords for factory setting
                               User levels                                  Keyword according to factory setting
                               Maintenance personnel                        main
                               Authorized client                            client
                               Service                                      servicelevel


                              NOTE
                              Change the passwords during initial commissioning to protect your device.
                              A higher user level can change the password of a lower user level.

                              Information about the device is displayed in the device window and the device can also
                              be configured here (Device> Open menu).

                              Resetting the password

                              NOTE
                              The responsible SICK sales company or the responsible SICK service partner carefully
                              checks each code request to reset the password. A risk of deception by third parties
                              nevertheless exists. The operating entity should therefore take suitable security meas-
                              ures.
                              The operating entity should also take suitable measures to limit, as best as possible,
                              access to the product. This includes, in particular, physical access as well as access to
                              the software interfaces of the product.



8028981/1X1R/2026-06-10 | SICK                                                                        multiScan165    55
SUBJECT TO CHANGE WITHOUT NOTICE

7 COMMISSIONING

                    Resetting the password for the Service user
                    1.
                         Click on the      button.
                    m    The Log in to device input screen opens.
                    2.   Click on Password forgotten?.

                    Resetting the password for the Authorized client/Maintenance personnel user
                    1.  The password for the Service user has been reset.
                    2.  Save the device parameterization using the parameter export (Device menu >
                        Export > To a file).
                    3.
                        In the device window, click on the   button.
                    4.  Select Reset to factory settings.




56   multiScan165                                                                 8028981/1X1R/2026-06-10 | SICK
                                                                            SUBJECT TO CHANGE WITHOUT NOTICE

MAINTENANCE 8

8              Maintenance
8.1            Maintenance plan
                              During operation, the device works maintenance-free.

                              NOTE
                              No maintenance is required to ensure compliance with the laser class.

                              Depending on the assignment location, the following preventive maintenance tasks
                              may be required for the device at regular intervals:
                              Table 13: Maintenance plan
                               Maintenance work                     Interval                             To be carried out
                                                                                                         by
                               Check device and connecting cables   Depends on ambient conditions and    Specialist
                               for damage at regular intervals.     climate.
                               Clean housing.                       Depends on ambient conditions and    Specialist
                                                                    climate.
                               Clean housing and optics cover.      Depends on ambient conditions and    Specialist
                                                                    climate.
                               Check the screw connections and      Depends on the place of use, ambi-   Specialist
                               plug connectors.                     ent conditions or operating require-
                                                                    ments. Recommended: At least every
                                                                    6 months.
                               Check the mounting accessories and   Depends on the place of use, ambi-   Specialist
                               vibration dampers used.              ent conditions or operating require-
                                                                    ments. Recommended: At least every
                                                                    6 months.


8.2            Cleaning

                              NOTICE
                              Equipment damage due to improper cleaning.
                              Improper cleaning may result in equipment damage.
                              O    Only use recommended cleaning agents and tools.
                              O    Never use sharp objects for cleaning.

                              →    Clean the optics cover at regular intervals and in the event of contamination with a
                                   lint-free lens cloth and plastic cleaning agent. Rinse off coarse dirt first with water.
                                   The cleaning interval essentially depends on the ambient conditions.

                              NOTICE
                              If the optics cover is scratched or damaged (cracked, broken), it must be replaced.
                              Contact SICK Support to arrange this.
                              O    If the optics cover is cracked or broken, take the device out of operation immedi-
                                   ately for safety reasons and have it repaired by SICK.




8028981/1X1R/2026-06-10 | SICK                                                                          multiScan165    57
SUBJECT TO CHANGE WITHOUT NOTICE

9 TROUBLESHOOTING

9           Troubleshooting
9.1         General faults, warnings, and errors
                      Possible faults and corrective actions are described in the table below for troubleshoot-
                      ing. For faults that cannot be rectified using the information below, please contact SICK
                      Service. To find your agency, see the final page of this document.

                      NOTE
                      Before calling, make a note of all type label data such as type designation, serial
                      number, etc., to ensure faster assistance.


                      Table 14: Troubleshooting Q&A
                       Question / status                        Response / remedial actions
                       Both LEDs flash red.                     Device error: Read the error code via the SOPAS ET PC
                                                                software and remedy the cause of the error.
                       LEDs indicate an undefined status.       Check the device status, if necessary contact the SICK
                                                                Service department.
                       All LEDs are off                         Check the voltage supply to the device.
                                                                In SOPASair, check whether the LEDs were switched off.
                       All LEDs of the device light up red at   Check the voltage supply to the device. The power supply
                       startup and do not change to green.      unit may not be supplying the required current or the
                                                                required voltage to start the device.
                       All LEDs of the device flash red.        The device may not be able to recognize the system plug.
                                                                Check that the system plug is mounted correctly and that
                                                                both contact sides are clean and dry.
                       Measurement data show anomalies.         Optics cover contaminated: Clean the optics cover.
                       When accessing the device via a web      Try connecting again. If this does not work: Restart the
                       browser, the SOPASair user interface     device.
                       is not loaded, the SOPASair loading
                       screen is permanently displayed.
                       SOPASair is not started in the           Check the IP address of device and network adapter (e.g.,
                       browser.                                 using device search in SOPAS ET) and adjust if necessary.
                                                                Then try to establish the connection again.
                       No connection to the device possible. Check whether the system plug is securely mounted see
                                                             "Mounting the system plug on the device", page 41.


9.2         Repairs
                      Repair work on the device may only be performed by qualified and authorized person-
                      nel from SICK AG. Interruptions or modifications to the device by the customer will
                      invalidate any warranty claims against SICK AG.


9.3         Returns
                      →     Only send in devices after consulting with SICK Service.
                      →     The device must be sent in the original packaging or an equivalent padded pack-
                            aging.

                      NOTE
                      To enable efficient processing and allow us to determine the cause quickly, please
                      include the following when making a return:
                      O     Details of the contact person
                      O     Description of the application
                      O     Description of the fault that occurred




58    multiScan165                                                                                8028981/1X1R/2026-06-10 | SICK
                                                                                            SUBJECT TO CHANGE WITHOUT NOTICE

TROUBLESHOOTING 9

9.4            Disposal
                              If a device can no longer be used, dispose of it in an environmentally friendly manner
                              in accordance with the applicable country-specific waste disposal regulations. Do not
                              dispose of the product along with household waste.

                              NOTICE
                              Danger to the environment due to improper disposal of the device.
                              Disposing of devices improperly may cause damage to the environment.
                              Therefore, observe the following information:
                              O    Always observe the national regulations on environmental protection.
                              O    Separate the recyclable materials by type and place them in recycling containers.




8028981/1X1R/2026-06-10 | SICK                                                                      multiScan165   59
SUBJECT TO CHANGE WITHOUT NOTICE

10 TECHNICAL DATA

10           Technical data

                        NOTE
                        The relevant online product page for your product, including technical data, dimen-
                        sional drawing, and connection diagrams, can be downloaded, saved, and printed from
                        the Internet.
                        The product page can be accessed via the SICK Product ID: pid.sick.com/{P/N}/{S/N}
                        {P/N} corresponds to the part number of the product, see type label.
                        {S/N} corresponds to the serial number of the product, see type label (if indicated).
                        Please note: This documentation may contain further technical data.


10.1         Features
                         Measurement principle           Statistical measurement procedure
                         Application                     Indoor and outdoor
                         Light source                    Infrared (wavelength 905 nm)
                         Laser class                     Laser class 1 (EN 60825-1:2014+A11:2021, IEC 60825-1:2014,
                                                         EN/IEC 60825-1:2007)
                                                         Complies with 21 CFR 1040.10 and 1040.11 except for conformance
                                                         with IEC 60825-1 Ed. 3 as described in Laser Notice No. 56, dated
                                                         May 8, 2019.
                         Horizontal aperture angle       360°
                         Vertical aperture angle         42° (approx. +35.3° to –7.3°, DIN ISO 8855)
                         Scan field flatness             ± 0.65°
                         Scan rate                       20 Hz
                                                         40 Hz (between scan layer 4 and 13)
                         Angular resolution              Horizontal: 0.5°; in interlaced mode: 0.25° (10 Hz), 0.125° (5 Hz)
                                                         Vertical: approx. 2.5° and 5° see "Scan layer address", page 27.
                                                         Note: The actual position of a scan layer may differ.
                                                         The actual vertical angle value is included in the output of meas-
                                                         ured values.
                         Working range                   0.05 m ≤ x ≤ 62 m 1)
                         Scanning range at 10%           20 m @ 100 klx
                         remission and > 99%             22 m @ 30 klx
                         detection probability           25 m @ 10 klx
                         Scanning range at 60%           62 m @ 10 klx
                         remission and > 99%
                         detection probability
                         Scanning range at 90%           40 m @ 100 klx
                         remission and > 99%             60 m @ 30 klx
                         detection probability           62 m @ 10 klx
                         Spot divergence                 Vertical: 5.3 mrad / 0.3°
                                                         Horizontal 2): 5.3 mrad + 2.2 mrad / 0.3° + 0.125°
                         Light spot size at front        13 mm
                         screen
                         Maximum number of ech-          3
                         oes that are output

                        1)   Specified measurement accuracy for ≥ 0.1 m
                        2)   In the scan direction




60     multiScan165                                                                                  8028981/1X1R/2026-06-10 | SICK
                                                                                               SUBJECT TO CHANGE WITHOUT NOTICE

TECHNICAL DATA 10

                              Working range diagram
                                        Scanning range in m 1
                                   70

                                   60

                                   50

                                   40
                                   30
                                   20
                                   10

                                    0

                               –10

                               –20

                               –30

                               –40

                               –50

                               –60

                               –70
                                 –70 -60 -50 -40 –30 –20 –10 0            10 20 30 40 50 60 70
                                                                                 Scanning range in m 1

                                    Scanning range for objects with up to 60 and 90 % remission: 62 m 2

                                    Scanning range for objects with up to 10 % remission: 25 m      3
                              Figure 43: Diagram of the working range (10 klx), topview

                              1          Scanning range in m
                              2          Scanning range for object with up to 60% and 90% remission: 62 m
                              3          Scanning range for object with up to 10% remission: 25 m




                              Figure 44: Positions of the 16 scan layers, side view, in relation to the horizon

                              1          Scan layer 1
                              2          Scan layer 16



8028981/1X1R/2026-06-10 | SICK                                                                                    multiScan165   61
SUBJECT TO CHANGE WITHOUT NOTICE

10 TECHNICAL DATA

                           Height in m (ft) 1
                               50
                          (164.04)




                               40
                          (131.24)
                                                                                           5.4°


                                                                                           2.6°
                               30
                           (98.43)                                                         2.6°
                                                                                           2.0°
                                                                                           3.1°
                               20
                           (65.62)                                                         2.1°
                                                                                           2.8°
                                                                                           2.2°
                                                                                           2.5°
                               10
                           (32.81)                                                         2.6°
                                                                                           2.0°
                                                                                           2.9°
                                                                                           2.5°
                                0
                                                                                           2.4°

                                                                                           4.9°
                              -10
                          (-32.81) 0     10       20       30      40       50      60       70
                                        (32.81) (65.62) (98.43) (131.24) (164.04) (196.85) (229.66)

                                                      Typical                             Radius in m (ft)
                                                  scanning range 3                              2
                                       60 % Remission 4
                                       10 % Remission 5

                      Figure 45: Working range diagram, side view. The actual position of a scan layer can vary. The
                      exact actual vertical angle value of each scan layer can be read from the device.

                      1       Height in m (ft)
                      2       Radius in m (ft)
                      3       Typical scanning range
                      4       60% and 90% remission
                      5       10% remission


10.2         Mechanics/Electronics
                      Connection type                  Depending on the mounted system plug, 2 x M12 round connectors
                      Supply voltage                   9 V DC ... 30 V DC
                      Permissible residual rip-        ± 5%
                      ple




62     multiScan165                                                                                     8028981/1X1R/2026-06-10 | SICK
                                                                                                  SUBJECT TO CHANGE WITHOUT NOTICE

TECHNICAL DATA 10

                               Power consumption                 Ptyp = 10 W
                                                                 Pstart = 35 W for 5 s (motor start-up)
                                                                 Pmax = 22 W (with full specified current at all outputs)
                               Digital inputs                    Voltage range:
                                                                 O  low: -3 V ... 0.45 x VS
                                                                 O  high: 0.72 x VS ... VS

                                                                 Switching frequency range:
                                                                 O ≤100 Hz
                               Digital outputs                   Output mode (configurable):
                                                                 O Push/pull
                                                                 O NPN
                                                                 O PNP

                                                                 Voltage range:
                                                                 O  low: 0 V... 1 V
                                                                 O  high: (VS - 1 V) ... VS

                                                                 Output current per output, short-circuit protected:
                                                                 O 2x max. 200 mA
                                                                 O 4x max. 100 mA
                                                                 O > 4x 50 mA
                               Material                          Housing: ALSi12
                                                                 Optics cover: polycarbonate
                               Housing color                     Grey (RAL 7016)
                               Enclosure rating 1)               IP65 / IP67 / IP69 (IEC 60529:1989+AMD1:1999+AMD2:2013) IPX9K
                                                                 (ISO 20653:2013)

                                                                 Test conditions:
                                                                 O  Water spray volume: 14 l/min ... 16 l/min
                                                                 O  Water pressure/temperature: 10000 KPa (100 bar) / 80 °C
                                                                 O  Flat jet nozzle distance: 100 mm ... 150 mm
                                                                 O  Spray angle: 0°, 30°, 60°, 90°
                                                                 O  Cycle: 30 seconds per position
                                                                 O  Rotational speed of test specimen: 5 rpm
                               Protection class                  III (IEC 61140:2016-11)
                               Electrical safety                 IEC 61010-1:2010-06
                               Weight                            0.7 kg
                               Dimensions (L x W x H)            100.3 mm x 100.3 mm x 98.5 mm
                               Maximum output current            Depends on the number of outputs used/parameterized.
                                                                 100 mA per channel when using 4 outputs, 200 mA per channel for
                                                                 2 outputs, 50 mA per channel for 8 outputs.
                               MTBF                              ≥ 50 years, at 20 °C ambient temperature
                                                                 ≥ 25.7 years, at 30 °C ambient temperature
                               MTTFD                             ≥ 100 years, at 25 °C ambient temperature (EN/ISO 13849-1:2015)

                              1)   Prerequisites:
                                   O     The system plug is mounted.
                                   O     The cables plugged into the electrical connections must be screwed tight.
                                   O     Unused electrical connections are sealed off with a protective cap.




8028981/1X1R/2026-06-10 | SICK                                                                                       multiScan165   63
SUBJECT TO CHANGE WITHOUT NOTICE

10 TECHNICAL DATA

10.3         Dimensional drawing

                                                                                                                                                                                         0.5 (0.02)
                                                                A 2:1                                                                                       B 2:1




                                                   1.1 (0.04)
                                                                                4
                                                                                                                                                            5

                                                                                                                                                                                   3                                                                   6 (0.24)                         7
                                                                                                                                                                                           A                                   6
                                                                                                                                                                                                                              42.7°
                                                                                                                                                                                                                               3 5 .4
                                                                        1 2
                                    12.5 (0.49)
                                                                                                                                20 (0.79)
                                                                                                                                                                                                                                                                      8
                      98.4 (3.87)
                                                                                                                                                                                                                                      °
                                                                                                   (4x)

                                                                                                                                                                                                                                                                                                    63 (2.48)
                                                                                             M5

                                                                                                                                                                                                                                                                                6 (0.24)
                                                                                                                                                                       multiScan


                                                                                                                                                                                           B

                                                                                                                                            2.5 (0.10)
                                                                                                   30 (1.18)                                                     94.8 (3.73)
                                                                                                   35.2 (1.39 )

                                                                 100.5 (3.96)
                                                                   120.7 (4.75)




                                                                                                                                                          50.4 (1.98)



                                                                                                                                                                                                           50. 3 (1.98)
                                                                  61.5 (2.42)                                     50.4 (1.98)


                                                                                     17.5 (0.69)

                                                                                                                                                                                                                                                                                                  118.9 (4.68)
                                                                                                                                                                         +/-180°




                                    53 (2.09)
                                                                                                                                                                                                                                                      àá
                                                                                                                                                                 90°               90°




                                                                         1
                                                                                                                  50.2 (1.98)
                                                                                                                                                                           0°
                                                                                                                                                                                                      M5
                                                                                                                                                                                                             (3x                  43.5 (1.71)
                                                                                M5                                                                                                                              )

                                                                                                                                                                                                                                                                  20.5 (0.81)       39.5 (1.56)
                                                                                     (3x
                                                                                        )
                                                                                                                                                                                                      9                   ß               22 (0.87)


                                                                                                                                            50.4 (1.98)
                                                                                                                                                                                              58 (2.28)




                      Figure 46: Device structure and dimensions, dimensions in mm (inch)

                      1                           M5 threaded mounting hole, 6.4 mm deep; tightening torque ≤ 3 Nm; for mounting the
                                                  device
                      2                           Ventilation element (membrane)
                      3                           Optics cover
                      4                           Top edge of the optics cover
                      5                           Base of housing
                      6                           Aperture angle (vertical field of vision)
                      7                           Defined device origin
                      8                           Visual zero position with maximum viewing range
                      9                           Direction of rotation
                      ß                           M5 threaded mounting hole; 6.4 mm deep; for accessories only
                      à                           Supply voltage connection
                      á                           Ethernet connection


10.4         Performance
                         Measurement data rate                                                         230,400 … 691,200 measuring points/second
                         Scanning frequency                                                            20 Hz
                         Response time                                                                 ≤ 50 ms
                         Response time                                                                 Measurement data output: ≤ 60 ms 1)
                                                                                                       Field evaluation: ≤ 175 ms see "Delay time of field evaluation",
                                                                                                       page 38


64     multiScan165                                                                                                                                                                                                             8028981/1X1R/2026-06-10 | SICK
                                                                                                                                                                                                                          SUBJECT TO CHANGE WITHOUT NOTICE

TECHNICAL DATA 10

                               Measurement data output           < 5 ms
                               per segment
                               Power-up time                     typ. 15 s
                               Systematic error                  ± 35 mm
                                                                 Temperature drift: Typically ± 0.5 mm/K
                               Statistical error                 ≤ 10 mm
                               Integrated application            Measurement data output (based on ordered configuration), inte-
                                                                 grated field evaluation with flexible fields (based on ordered config-
                                                                 uration), vertical distance measurement (based on ordered config-
                                                                 uration)
                               Number of configurable            Up to 48 fields
                               fields
                               Simultaneous detection            Up to 20 fields see "Field evaluation", page 37.
                               fields
                               Filters                           Fog filter, echo filter, particle filter, moving average filter, interval
                                                                 filter, scan range filter, scan layer filter, cuboid area filter, distance
                                                                 filter

                              1)   Network delays, e.g. due to cables or Ethernet switches, must also be taken into account.


10.5           Interfaces
                               Ethernet                          ✓, UDP/IP (Compact, MSGPACK), TCP/IP (configuration and secon-
                                                                 dary data via COLA telegrams)
                                                                 Function: HOST, NTP, PTP
                                                                 Measured data output (distance, RSSI)
                                                                 Data transmission rate: 100 Mbit/s, optionally up to 1 Gbit/s,
                                                                 depending on the mounted system plug
                               Digital inputs/outputs            I/O (8 multiports), depending on the mounted system plug
                               Measurement data output           MSGPACK, Compact
                               format
                               Additional data                   Contamination indication, IMU (secondary sensor data)
                               IMU (inertial measuring           Sampling rate: 100 Hz
                               unit)
                                                                 Relative position of the IMU to the optical origin:
                                                                 O  X: -17 mm
                                                                 O  Y: +23.5 mm
                                                                 O  Z: -34.5 mm
                               Optical displays                  4 LEDs
                               Configuration software            SOPASair (web server), SOPAS ET (software), REST API
                               Driver                            ROS1, ROS2, C++


10.6           Ambient data
                               Remission factor                  2% ... > 1,000% (reflector)
                               Electromagnetic compati- Radiation emitted:
                               bility (EMC)             O Industrial environment (IEC 61000-6-4:2018 / EN
                                                          IEC 61000-6-4:2019 IEC 61000-6-4:2006+A1:2010 / EN
                                                          61000-6-4:2007+A1:2011)
                                                        O Emission from devices in residential areas
                                                          (IEC 61000-6-3:2020)

                                                                 Electromagnetic immunity:
                                                                 O  Industrial environment
                                                                    (IEC 61000-6-2:2016 / EN IEC 61000-6-2:2019 / IEC 61000-6-2:2
                                                                    005 / EN 61000-6-2:2005 / EN 61000-6-2:2005 / AC:2005)

                                                                 Application areas:
                                                                 O Automotive (UN ECE R10 ready) 1)
                                                                 O Agricultural and forestry machinery (ISO 14982-1, ISO 14982-2) 1)
                                                                 O Earthmoving and construction machinery (ISO 13766-1) 1)



8028981/1X1R/2026-06-10 | SICK                                                                                           multiScan165     65
SUBJECT TO CHANGE WITHOUT NOTICE

10 TECHNICAL DATA

                               Vibration resistance               Sine resonance scan: 10 Hz ... 1,000 Hz (IEC 60068-2-6:2007)
                                                                  Sine test: 10 Hz ... 500 Hz; 0.35 mm/5 g; 10 cycles
                                                                  (IEC 60068-2-6:2007)
                                                                  Noise test: 10 Hz … 250 Hz; 4.24 g RMS, 5 h (IEC 60068-2-64:2008)
                               Shock resistance                   IEC 60068-2-27:2008
                                                                  50 g, 11 ms, ± 3 single shocks/axis
                                                                  25 g, 6 ms, ± 1,000 continuous shocks/axis
                                                                  50 g, 3 ms, 5,000 continuous shocks/axis
                               Impact resistance                  IEC 60068-2-75: Hammer impact test: 0.5 joule & 2 joule
                               Ambient temperature                Switching on: -30 °C ... +60 °C
                                                                  Operation: -40 °C … +60 °C 2) (IEC 60068-2-1, IEC 60068-2-2,
                                                                  IEC 60068-2-14 (Nb))
                               Storage temperature                -40 °C … +75 °C (IEC 60068-2-14 (Nb))
                               Operating and storage air          max. 95% RH (non-condensing) (IEC 60068-2-30 (Db1))
                               humidity 3)
                               Temperature change                 –30 °C ... +50 °C, 10 cycles (EN 60068-2-14:2009)
                               Chemical resistance                Salt mist test (IEC 60068-2-52, Procedure 4)
                               Altitude                           < 5,000 m above sea level
                               Ambient light immunity             100 klx (indirect)

                              1)   Load dump: from ISO 16750-2 Test B Severity Level 4 passed for 12 V systems. Required in case of transient
                                   disturbances on the input filtering signal lines (debounce > 10 ms).
                              2)   At operating temperatures above +50 °C, mechanical mounting of the device is required, preferably using
                                   the mounting accessories provided.
                              3)   Condensation can occur on the device (especially on the optics cover) if the device is exposed to rapid
                                   temperature fluctuations (e.g. changing halls). Take suitable countermeasures such as warming up the
                                   device before changing halls or blowing in air-conditioned air.


10.6.1         Mission time
                              The mission time is the period during which the failure rates can be assumed to be
                              constant. At the end of the mission time, the failure rates gradually increase due to wear.
                              The mission time of the product is influenced by various factors, including operating
                              conditions and user handling.
                              The typical mission time to be expected under normal operating conditions and proper
                              use can be found in the technical data see "Technical data", page 60. It is important
                              to note that the actual mission time may vary depending on individual circumstances.
                              Factors such as frequency of use and ambient factors can affect the service life of the
                              product.
                              According to the IEC/EN 61508-2 standard, a mission time based on general expe-
                              rience can be assumed. In addition, the mission time can be extended by suitable
                              measures taken by the system operator, e.g., operation at a low ambient temperature or
                              avoidance of shocks and vibrations.
                              Table 15: Example sensor mission times at different ambient temperatures
                               Continuous use at 25 °C                                                         42 years
                               Continuous use rarely above 30 °C                                               37.5 years
                               Continuous use 55% up to 30 °C, 35% up to 40 °C and 10% up to                   20 years
                               50 °C
                               Continuous use 70% to 30 °C, 30% to 50 °C                                       18 years
                               Continuous use 80% to 30 °C and 20% to 60 °C                                    13.4 years
                               Continuous use at 50 °C                                                         8 years




66       multiScan165                                                                                             8028981/1X1R/2026-06-10 | SICK
                                                                                                            SUBJECT TO CHANGE WITHOUT NOTICE

ACCESSORIES 11

11             Accessories

                              NOTE
                              On the product page you will find accessories and, if applicable, related installation
                              information for your product.
                              The product page can be accessed via the SICK Product ID: pid.sick.com/{P/N}/{S/N}
                              {P/N} corresponds to the part number of the product, see type label.
                              {S/N} corresponds to the serial number of the product, see type label (if indicated).


                              Support Portal

                              NOTE
                              In the SICK Support Portal (support.sick.com, registration required) you will find not
                              only useful service and support information for your product as well as commands
                              for test purposes via the REST communication interface, but also the Cybersecurity
                              Hardening Guide as well as further detailed information on the available accessories
                              and their use.




8028981/1X1R/2026-06-10 | SICK                                                                        multiScan165     67
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

12           Annex
12.1         Declarations of conformity and certificates
                        You can download declarations of conformity and certificates via the product page.
                        The product page can be accessed via the SICK Product ID: pid.sick.com/{P/N}/{S/N}
                        {P/N} corresponds to the part number of the product, see type label.
                        {S/N} corresponds to the serial number of the product, see type label (if indicated).


12.2         Licenses
                        SICK uses open source software which is published by the rights holders under a
                        free license. Among others, the following license types are used: GNU General Public
                        License (GPL version 2, GPL version 3), GNU Lesser General Public License (LGPL), MIT
                        license, zlib license and licenses derived from the BSD license.
                        This program is provided for general use without warranty of any kind. This warranty
                        disclaimer also extends to the implicit assurance of marketability or suitability of the
                        program for a particular purpose.
                        More details can be found in the GNU General Public License.
                        For license texts see www.sick.com/licensetexts.
                        Printed copies of the license texts are also available on request.


12.3         Communication interfaces
                        Communication with the device is possible via CoLa A/B and REST. For more informa-
                        tion, see the following English telegram listing.

                        Under Downloads on the product page, you can download, for example, the Open API
                        file.
                        The product page can be accessed via the SICK Product ID: pid.sick.com/{P/N}/{S/N}
                        {P/N} corresponds to the part number of the product, see type label.
                        {S/N} corresponds to the serial number of the product, see type label (if indicated).


12.4         Data format description (EN)

Contents
                        12.4.1.1         Glossary............................................................................................................   69
                        12.4.1.2         General information on the transmission of measurement data......                                                      70
                        12.4.1.3         MSPACK format..............................................................................................            70
                        12.4.1.3.1             Framing.......................................................................................................   70
                        12.4.1.3.2             MSGPACK keywords...............................................................................                  71
                        12.4.1.3.3             Serialization of a segment.....................................................................                  72
                        12.4.1.3.3.1                 Notation used.....................................................................................         73
                        12.4.1.3.3.2                 Serialization of the ScanSegment class....................................                                 73
                        12.4.1.3.3.3                 Serialization of the Scan class......................................................                      74
                        12.4.1.3.3.4                 Serialization of arrays.......................................................................             76
                        12.4.1.4         Compact format..............................................................................................           77
                        12.4.1.4.1             Working with Compact...........................................................................                  77



68     multiScan165                                                                                                        8028981/1X1R/2026-06-10 | SICK
                                                                                                                     SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                              12.4.1.4.2             Framing.......................................................................................................   77
                              12.4.1.4.3             telegramType 1: Primary Data – Spherical Coordinates................                                             79
                              12.4.1.4.3.1                Header specifics................................................................................            79
                              12.4.1.4.3.2                Payload.................................................................................................    79
                              12.4.1.4.3.3                Metadata..............................................................................................      81
                              12.4.1.4.4             telegramType2: IMU................................................................................               87
                              12.4.1.4.4.1                Header specifics................................................................................            87
                              12.4.1.4.4.2                Payload.................................................................................................    88
                              12.4.1.5           General measurement data definitions...................................................                              89
                              12.4.1.5.1             Azimuth angle...........................................................................................         89
                              12.4.1.5.2             Segment counter.....................................................................................             89
                              12.4.1.5.3             Representation of RSSI values.............................................................                       90
                              12.4.1.5.4             Representation of bit fields...................................................................                  90
                              12.4.1.5.5             Representation of beam characteristics (Properties)..................                                            91
                              12.4.1.6           Behavior of serialization for data reduction............................................                             92
                              12.4.1.6.1             Behavior in relation to the number of available echoes...............                                            92
                              12.4.1.6.2             Behavior when restricting the azimuth angular range..................                                            92
                              12.4.1.6.3             Behavior when reducing the available layers..................................                                    93

12.4.1.1       Glossary
                               Designation                              Explanation
                               Azimuth angle                            Horizontal angle described by Theta
                               Beam                                     With the term beam we denote a beam of light which is emit-
                                                                        ted by the lidar sensor in a certain direction. There may be
                                                                        multiple reflections of light on that beam which are caused by
                                                                        object which intersect with that beam. These reflections are
                                                                        called echoes.
                               Elevation angle                          Vertical angle described by Phi
                               Frame                                    A frame is defined as the data acquired within the entire field
                                                                        of view of a LiDAR sensor (e.g., 360° for rotating LiDAR sensors
                                                                        such as the multiScan100)

                                                                        multiScan136 example:
                                                                        O 1 frame consists of 12 segments
                                                                        O 1 segment comprises n layers = n scans (multiScan136
                                                                          example: 16 layers = 16 scans)
                                                                        O 1 scan comprises several beams
                               Layer                                    A traditional 2D LiDAR has a layer at 0°. Multi-layer scanners
                                                                        can have multiple layers (e.g. multiScan136 => 16 layers).
                               Module                                   A module is an object that creates/provides data for different
                                                                        layers
                               RSSI                                     RSSI (received signal strength indicator) is defined as an indi-
                                                                        cator of the strength of the received signal.

                                                                        Context:
                                                                        O Small RSSI value = low signal strength
                                                                        O Large RSSI value = high signal strength
                                                                        The magnitude of the RSSI values is not standardized and can
                                                                        vary from device to device.
                               Scan                                     Collection of beams in the azimuth direction of a layer.




8028981/1X1R/2026-06-10 | SICK                                                                                                               multiScan165             69
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                                 Designation                             Explanation
                                 Scan segment                            A scan segment is defined as a collection of scans that rep-
                                                                         resent a portion of a frame. All scans in a segment have dif-
                                                                         ferent elevation angles (i.e., they belong to different layers in
                                                                         the case of a multi-layer LiDAR sensor). The angular range
                                                                         in azimuth may (but need not) be different for each scan in
                                                                         a segment. For multi-layer LiDAR sensors, a scan segment
                                                                         is typically used to combine scans that were acquired at the
                                                                         same time or that have the same azimuth range.


12.4.1.2           General information on the transmission of measurement data
                                 The measurement data are transmitted segment by segment, i.e., each transmitted
                                 data package (for example a UDP packet or TCP packet) contains a segment (cf. the
                                 Segmented data output section in the operating instructions). Each segment can be
                                 interpreted separately, i.e., it is not necessary to collect all segments in a frame (=all
                                 measurement data recorded in one revolution) to start processing. This makes it possi-
                                 ble to reduce the latency between the generation of the measurement data and the
                                 processing of that data on the client side.
                                 Two formats are available for the transmission of measurement data, which will be
                                 referred to in the following as MSGPACK format and Compact format.
                                 The MSGPACK format encodes the measurement data according to the MSGPACK
                                 standard (see also www.msgpack.org), which has the advantage that the data pack-
                                 ages can be easily parsed using the standard libraries available for numerous program-
                                 ming languages. The MSGPACK format is self-describing. Each data field is described
                                 by a keyword, so it is easy to determine which data field is currently being read without
                                 having to know the exact structure of the data.
                                 In the Compact format, the measurement data of the sensor are represented as com-
                                 pactly as possible. The individual fields are not self-describing, but only a string of bytes
                                 is transmitted. The structure of the transmitted data package must be known to the user
                                 in advance. This has the advantage that as little bandwidth as possible is used on the
                                 data line and that a very efficient interpretation of the data is possible by copying the
                                 transmitted byte sequence into a structure using a single command (e.g., memcpy in
                                 the programming language C/C++).

12.4.1.3           MSPACK format

12.4.1.3.1                  Framing
                                 The data packages transmitted in MSGPACK format are enclosed within a frame (see
                                 figure 47, page 70):
                                 The actual MSGPACK payload data is preceded by 4 <STX> characters (hex code 0x02)
                                 and the size of the actual payload data (without the checksum at the end) in bytes as
                                 a uint32 value. Following the MSGPACK data is a CRC32 checksum calculated on the
                                 MSGPACK data only (without the <STX> characters and packet size). The little-endian
                                 representation is used for both the size of the payload and the checksum.
                                        4 Bytes          4 Bytes                                                  4 Bytes
                                                     Size of MSGPACK             MSGPACK buffer                   CRC32
                                      \x2\x2\x2\x2
                                                       buffer in bytes

                                 Figure 47: Framing in the MSGPACK format




70           multiScan165                                                                                        8028981/1X1R/2026-06-10 | SICK
                                                                                                           SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

12.4.1.3.2             MSGPACK keywords
                              To reduce the bandwidth on the transmission line, the keywords used in MSGPACK are
                              encoded as uint8 values. The bandwidth savings from this are significant, but the user
                              must interpret the read uint8 keywords according to the following table. The description
                              of the keywords in the table is for overview purposes only. A detailed description can be
                              found in the sections referred to in the respective table rows. Exactly the same names
                              for the keywords are used there.

                              NOTE
                              The data packages can be read using standard MSGPACK parsers after removing the
                              framing. For some parsers, options must be set to allow uint8 values as keywords. For
                              the Python msgpack module, for example, the option strict_map_key=False must be
                              set:
                              unpacked = msgpack.unpackb(msgpackValue, strict_map_key=False)


                              Table 16: Used MSGPACK keywords and associated uint8 codes
                               Keyword name                 Uint8 value   Description
                               classname                    0x10          Keyword for the Scan (see "Serialization of
                                                                          the Scan class", page 74) and ScanSegment
                                                                          (see "Serialization of the ScanSegment class",
                                                                          page 73) classes represented in the data
                               data                         0x11          Keyword for the data part, which belongs to the
                                                                          Array, Scan or ScanSegment classes, see "Seri-
                                                                          alization of the Scan class", page 74; see "Seri-
                                                                          alization of the ScanSegment class", page 73;
                                                                          see "Serialization of arrays", page 76.
                               numOfElems                   0x12          Number of elements in an array, see "Serializa-
                                                                          tion of arrays", page 76
                               elemSz                       0x13          Size of an array element in bytes, see "Serializa-
                                                                          tion of arrays", page 76
                               endian                       0x14          Keyword describing the endianness of the array
                                                                          elements, see "Serialization of arrays", page 76
                               elemTypes                    0x15          Keyword for the type of array elements, see
                                                                          "Serialization of arrays", page 76
                               Little                       0x30          Keyword for endianness “little”.
                               float32                      0x31          Data type float32
                               uint32                       0x32          Data type uint32
                               uint8                        0x33          Data type uint8
                               uint16                       0x34          Data type unit16
                               ChannelTheta                 0x50          Data channel with azimuth angles, see "Seriali-
                                                                          zation of the Scan class", page 74
                               ChannelPhi                   0x51          Data channel with elevation angles, see "Seriali-
                                                                          zation of the Scan class", page 74
                               DistValues                   0x52          Channel with distance values, see "Serialization
                                                                          of the Scan class", page 74
                               RssiValues                   0x53          Channel with RSSI values, see "Serialization of
                                                                          the Scan class", page 74
                               PropertiesValues             0x54          Channel with further properties of a measure-
                                                                          ment beam, see "Serialization of the Scan class",
                                                                          page 74 and see "Representation of beam char-
                                                                          acteristics (Properties)", page 91
                               Scan                         0x70          Keyword for the “Scan” class, see "Serialization
                                                                          of the Scan class", page 74
                               TimestampStart               0x71          Start time stamp of a scan, see "Serialization of
                                                                          the Scan class", page 74




8028981/1X1R/2026-06-10 | SICK                                                                            multiScan165         71
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                               Keyword name                 Uint8 value   Description
                               TimestampStop                0x72          Stop time stamp of a scan, see "Serialization of
                                                                          the Scan class", page 74
                               ThetaStart                   0x73          Azimuth start angle of a scan, see "Serialization
                                                                          of the Scan class", page 74
                               ThetaStop                    0x74          Azimuth stop angle of a scan, see "Serialization
                                                                          of the Scan class", page 74
                               ScanNumber                   0x75          Number of a scan, see "Serialization of the Scan
                                                                          class", page 74
                               ModuleId                     0x76          ModuleID of a scan, see "Serialization of the
                                                                          Scan class", page 74
                               BeamCount                    0x77          Number of beams in a scan, see "Serialization of
                                                                          the Scan class", page 74
                               EchoCount                    0x78          Number of echoes in a scan, see "Serialization of
                                                                          the Scan class", page 74
                               ScanSegment                  0x90          Keyword for the “ScanSegment” class, see "Seri-
                                                                          alization of the ScanSegment class", page 73
                               SegmentCounter               0x91          Segment number of a segment, see "Serializa-
                                                                          tion of the ScanSegment class", page 73
                               FrameNumber                  0x92          Frame number of a segment, see "Serialization
                                                                          of the ScanSegment class", page 73
                               Availability                 0x93          Availability of a segment, see "Serialization of
                                                                          the ScanSegment class", page 73
                               SenderId                     0x94          SenderID of a segment, see "Serialization of the
                                                                          ScanSegment class", page 73
                               SegmentData                  0x96          Array with the actual measurement data for each
                                                                          layer, see "Serialization of the ScanSegment
                                                                          class", page 73
                               LayerId                      0xA0          Array with layer IDs, see "Serialization of the
                                                                          ScanSegment class", page 73
                               TelegramCounter              0xB0          Telegram counter, see "Serialization of the Scan-
                                                                          Segment class", page 73


12.4.1.3.3              Serialization of a segment
                              Each data package transmits one segment enclosed within a frame as per section
                              section 12.4.1.4.2. A segment contains various fields, which are described in see table 17.
                              The actual measurement data is located in the SegmentData field, which contains one
                              element of the Scan class (see "Serialization of the Scan class", page 74) for each
                              layer of the sensor (see figure 48, page 73).




72       multiScan165                                                                               8028981/1X1R/2026-06-10 | SICK
                                                                                              SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12



                                         ScanSegment

                                    TelegramCounter

                                    TimeStampTransmit

                                    SegmentCounter

                                    FrameNumber

                                    Availability

                                    SenderId

                                    LayerId

                                    SegmentData
                                                                         SegmentData

                                                                   Scan1

                                                                   Scan2

                                                                   ...

                                                                   ScanN




                              Figure 48: General structure of a segment. In addition to some metadata, the ScanSegment class
                              contains an array named SegmentData that contains an object of type Scan for each layer of the
                              sensor.


                              The data of a segment are encoded in MSGPACK format. The following exception
                              should be noted: Measurement data in arrays such as distance, RSSI, angle etc. are
                              binary coded here to allow easier serialization (see "Serialization of arrays", page 76).

12.4.1.3.3.1                  Notation used
                              The following notes on the notation used relate to the description of the structures
                              encoded in MSGPACK:
                              O    Msgpack_map_header is used to denote the header of a msgpack map
                                   as per this specification: https://github.com/msgpack/msgpack/blob/mas-
                                   ter/spec.md#map-format-family
                              O    The keyword names and other names used in the structures correspond to those
                                   from see table 16, page 71.
                              O    Angle brackets are used to specify placeholders for values referred to in the
                                   respective declarations, e.g., <numOfElems> for the number of elements of an
                                   array.
                              O    Keywords printed in bold refer to substructures of a type, e.g., other types or arrays.
                              O    Although a structure similar to JSON is used for the description in this document,
                                   the data is however encoded according to the MSGPACK specification: https://
                                   github.com/msgpack/msgpack/blob/master/spec.md

12.4.1.3.3.2                  Serialization of the ScanSegment class
                              The ScanSegment class is represented as a nesting of MSGPACK maps as follows:
                              msgpack_map_header {
                              "classname": ScanSegment,
                              "data":
                              msgpack_map_header {
                              "TelegramCounter": <telegramCounter>,


8028981/1X1R/2026-06-10 | SICK                                                                             multiScan165    73
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                        "TimeStampTransmit": <timeStampTransmit>,
                        "SegmentCounter": <segmentCounter>,
                        "FrameNumber": <frameNumber>,
                        "Availability": <availability>,
                        "SenderId": <senderId>,

                        "LayerId": layerIdVector,,
                        "SegmentData", segmentData
                        }
                        }

                        Definition: Definition of the ScanSegment class
                        The meaning of the individual fields is shown in the following table.
                        Table 17: Description of the attributes of the ScanSegment class
                         Name                    Type                Description
                         TelegramCounter         MSGPACK int 1)      Counts all telegrams with measurement data sent in
                                                                     MSGPACK format since switching on the device. The
                                                                     counter starts at 1.
                         TimeStampTransmit       MSGPACK int 1)      Sensor system time in µs since 1.1.1970 00:00 in UTC.
                         SegmentCounter          MSGPACK int 1)      Segment counter as described in section.
                         FrameNumber             MSGPACK int 1)      Counts the number of full revolutions since the
                                                                     device was started.
                         Reserved
                         SenderId                MSGPACK int 1)      Device serial code. It can be used to detect on the
                                                                     recipient which sensor the data was sent from.
                         LayerId                 MSGPACK array 2) Array of layer indices. The layer indices start at 1 and
                                                 of int 1)        increase with decreasing elevation angle.
                         SegmentData             MSGPACK array 2) Array of elements of the Scan class (see "Seri-
                                                 of scans         alization of the Scan class", page 74) that con-
                                                                  tain the actual measurement data. The following
                                                                  applies: The scan at position i has the layer number
                                                                  LayerId[i].

                        1)   github.com/msgpack/msgpack/blob/master/spec.md#int-format-family
                        2)   github.com/msgpack/msgpack/blob/master/spec.md#array-format-family

                            NOTE The arrays LayerId and SegmentData are MSGPACK arrays as per the
                        MSGPACK specification and are not represented like arrays containing measurement
                        data (see "Serialization of arrays", page 76).


12.4.1.3.3.3            Serialization of the Scan class
                        The Scan class is represented as a nesting of MSGPACK maps as follows:
                        msgpack_map_header {
                        "classname": Scan,
                        "data":
                        msgpack_map_header {
                        "TimeStampStart": <timeStampStart>,
                        "TimeStampStop": <timeStampStop>,
                        "ThetaStart": <thetaStart>,
                        "ThetaStop": <thetaStop>,



74       multiScan165                                                                            8028981/1X1R/2026-06-10 | SICK
                                                                                           SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                              "ScanNumber": <scanNumber>,
                              "ModuleId": <moduleId>,
                              "ChannelTheta": <channelTheta>,
                              "ChannelPhi": <channelPhi>,
                              "DistValues": <distValues>,
                              "RssiValues": <rssiValues>,
                              "PropertyValues": <propertyValues>,
                              "BeamCount": <beamCount>,
                              "EchoCount": <echoCount> }
                              }

                              Definition: Definition of the Scan class. The fields highlighted in gray are optional, i.e.,
                              they are not necessarily present in the structure.
                              The meaning of the individual fields is shown in the following table:
                              Table 18: Description of the attributes of the Scan class
                               Name                     Type                 Description
                               TimeStampStart           MSGPACK int 1)       Acquisition time of the first beam of the scan in µs.
                                                                             The device's internal time base is used or, if the sen-
                                                                             sor offers the feature, the time set externally.
                               TimeStampStop            MSGPACK int 1)       Acquisition time of the last beam of the scan in µs.
                                                                             The device's internal time base is used or, if the sen-
                                                                             sor offers the feature, the time set externally.
                               ThetaStart               MSGPACK int 1)       Azimuth angle of the first beam of the scan in radi-
                                                                             ans.
                               ThetaStop                MSGPACK int 1)       Azimuth angle of the last beam of the scan in radi-
                                                                             ans.
                               ScanNumber               MSGPACK int 1)       Not used.
                               ModuleId                 MSGPACK int 1)       Number of the physical module that generated the
                                                                             data. In the case of the multiScan, for example, this
                                                                             is one of the two measuring modules.
                               ChannelTheta             array of float32     Array of azimuth angles of a specific beam in radi-
                                                                             ans. See also section 12.4.1.5.1. The encoding of the
                                                                             data in this array is described in section 12.4.1.3.3.4.
                                                                             The user can configure whether the array is present
                                                                             in the data structure.
                               ChannelPhi               array of float32     Array with the elevation angle (cf. operating instruc-
                                                                             tions, Coordinate system section) of the scan in
                                                                             radians. For single layer and multi-layer sensors,
                                                                             this array contains only one element. The encod-
                                                                             ing of the data in this array is described in
                                                                             section 12.4.1.3.3.4. The user can configure whether
                                                                             the array is present in the data structure.
                               DistValues               array of (array of   Array containing an array of distance values for each
                                                        float32)             echo of the scan. The number of sub-arrays corre-
                                                                             sponds to the number of echoes in the scan, see
                                                                             also the EchoCount field below. The distance values
                                                                             are specified in mm. The encoding of the data in this
                                                                             array is described in section 12.4.1.3.3.4. The user
                                                                             can configure whether the array is present in the
                                                                             data structure.
                                                                             The structure of the nested array is illustrated in
                                                                             figure 49.




8028981/1X1R/2026-06-10 | SICK                                                                                   multiScan165       75
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                         Name                                   Type                       Description
                         RssiValues                             array of (array of         Array containing an array of RSSI values for each
                                                                uint16)                    echo of the scan. The number of sub-arrays corre-
                                                                                           sponds to the number of echoes in the scan, see
                                                                                           also the EchoCount field below. For the represen-
                                                                                           tation of RSSI values, see "Representation of RSSI
                                                                                           values", page 90. The encoding of the data in this
                                                                                           array is described in section 12.4.1.3.3.4. The user
                                                                                           can configure whether the array is present in the
                                                                                           data structure.
                                                                                           The structure of the nested array is illustrated in
                                                                                           figure 49.
                         PropertyValues                         array of uint8             Array with additional properties, for example “reflec-
                                                                                           tor”, for each beam of a scan. See section 12.4.1.5.4
                                                                                           for details. The encoding of the data in this array
                                                                                           is described in section 12.4.1.3.3.4. This array is
                                                                                           optional.
                         BeamCount                              MSGPACK int 1)             Number of beams in the current scan.
                         EchoCount                              MSGPACK int 1)             Number of echoes in the current scan.

                        1)     github.com/msgpack/msgpack/blob/master/spec.md#int-format-family

                        DistValues                                                               RssiValues

                                                                                       Echos                                                          Echos

                                DistValues[0]   DistValues[1]          DistValues[2]                  RssiValues[0]   RssiValues[1]   RssiValues[2]

                                      d0             d0                     d0                              r0              r0             r0
                                      d1             d1                     d1                              r1              r1             r1
                                      d2             d2                     d2                              r2              r2             r2
                                      d3             d3                     d3                              r3              r3             r3
                                      d4             d4                     d4                              r4              r4             r4
                                      d5             d5                     d5                              r5              r5             r5
                                      d6             d6                     d6                              r6              r6             r6
                                      d7             d7                     d7                              r7              r7             r7
                                      d8             d8                     d8                              r8              r8             r8
                                      d9             d9                     d9                              r9              r9             r9
                                     d10            d10                    d10                             r10             r10            r10
                                     d11            d11                    d11                             r11             r11            r11
                                     d12            d12                    d12                             r12             r12            r12
                                     d13            d13                    d13                             r13             r13            r13
                                     d14            d14                    d14                             r14             r14            r14

                             Beams                                                                 Beams



                        Figure 49: Example of the structure of the DistValues and RssiValues arrays. Shown here are data
                        for a scan with 3 echoes and 15 beams.


12.4.1.3.3.4            Serialization of arrays
                        Arrays of measurement data (ChannelTheta, ChannelPhi, DistValues, RssiValues and
                        PropertyValues from see table 18, page 75) are encoded as follows:
                        msgpack_map_header {
                        "numOfElems": <number of array elements>,
                        "elemSz", < size of one array element in bytes>,
                        "endian", little,

                        "elemTypes", typesArray, ,
                        "data": binaryData
                        }

                        Definition: Definition of the Array class
                        The meaning of the individual fields of the Array class are shown in the following table.




76       multiScan165                                                                                                       8028981/1X1R/2026-06-10 | SICK
                                                                                                                      SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                              Table 19: Description of the attributes of the Array class
                               Name                                 Description
                               numOfElems                           Number of array elements
                               elemSz                               Size of an array element in bytes, e.g., 4 for float32 or 1 for
                                                                    uint8.
                               endian                               The value is always little
                               elemTypes                            Array of element types. Only arrays with one element are
                                                                    supported here. Example: {float32} for an array of float32
                                                                    values. To represent an array of tuples, elemTypes would
                                                                    therefore have multiple elements. This is not relevant, how-
                                                                    ever.
                               data                                 Actual payload. The data is encoded as a byte array in
                                                                    the MSGPACK int 1) and can be copied directly into a struc-
                                                                    ture/array after parsing the MSGPACK structure, taking into
                                                                    account the endianness and the data type.

                              1)   github.com/msgpack/msgpack/blob/master/spec.md#int-format-family


12.4.1.4       Compact format

12.4.1.4.1             Working with Compact
                              SICK provides the following software tools for working with the Compact data format:

                              Wireshark Dissector
                              The Wireshark dissector is a plugin that extends Wireshark with full decoding support
                              for the Compact format, including protocol details and filtering capabilities.
                              To use the dissector, the following components are required:
                              O    The freely available Wireshark software: www.wireshark.org
                              O       The SICK Compact dissector, including installation instructions, available on the
                                      SICK Support Portal support.sick.com (ID KA-08425)

                              LiDAR SDK
                              The SICK LiDAR SDK enables fast and seamless integration of SICK LiDAR sensors. It
                              provides functionality for device configuration, handling acyclic device messages, and
                              data transmission when the sensor is configured to use the Compact data format.
                              The SDK and its documentation are available on GitHub under the project name
                              sick_perception_sdk on https://github.com/SICKAG.
                              Additional information and further documentation can be found on the SICK Support
                              Portal: support.sick.com

12.4.1.4.2             Framing
                              The data packages transmitted in Compact format are enclosed in a frame consisting of
                              a header before the actual payload and a checksum (CRC) after the payload.




8028981/1X1R/2026-06-10 | SICK                                                                                   multiScan165         77
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX




                    Figure 50: Framing in the Compact format, consisting of a header before the payload and a
                    checksum after the payload.


                    NOTE
                    The payload content depends on the telegramType field of the frame header. Detailed
                    payload description, deviations from the frame header defined in this chapter as well
                    as telegramType specific frame header values are described in the chapter for each
                    telegramType.

                    The structure of the Compact frame header is defined in the table below.
                    Table 20: Description of the fields of the Compact frame header.
                    Offset         Name                Lenght            Type          Description
                    (bytes)                            (bytes)
                    0              Start of frame      4             uint32            Four <STX> characters (hex
                                                                                       code 0x02): \x2\x2\x2\x2
                    4              Telegram type       4             uint32            Defines the telegram type and
                                                                                       content that follows in the pay-
                                                                                       load section of this frame.
                                                                                       This field was named 'comman-
                                                                                       dId' in previous versions of this
                                                                                       documentation.
                    8              Telegram counter 8                uint64            Counts all telegrams sent since
                                                                                       the device was switched on. The
                                                                                       counter starts at 1.
                    16             Transmit time-      8             uint64            The sensor system time in
                                   stamp                                               microseconds since January 1,
                                                                                       1970, 00:00 (UTC). If a time
                                                                                       server is being used, the config-
                                                                                       ured system time is used.
                                                                                       This field was named 'timeS-
                                                                                       tampTransmit' in previous ver-
                                                                                       sions of this documentation




78   multiScan165                                                                              8028981/1X1R/2026-06-10 | SICK
                                                                                         SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                               Offset          Name                  Lenght             Type        Description
                               (bytes)                               (bytes)
                               24              Telegram version      4              uint32          Version of the payload for the
                                                                                                    telegram type defined in the
                                                                                                    header.
                                                                                                    The changes of the version are
                                                                                                    described in the telegram type
                                                                                                    specific chapters.
                               28              Payload length        4              uint32          Length of the payload excluding
                                                                                                    the checksum in bytes.
                                                                                                    This field was named 'sizeMod-
                                                                                                    ule0' in previous versions of this
                                                                                                    documentation
                               32              Sender Id             4              uint32          Serial number of the sensor
                                                                                                    sending the data. To be used
                                                                                                    to identify the origin of the data
                                                                                                    packet.

                              The CRC32 checksum that follows the payload is calculated over the entire data pack-
                              age, i.e. over the header and the entire payload. All values in the header and the
                              checksum are encoded as little endian.

12.4.1.4.3             telegramType 1: Primary Data – Spherical Coordinates

12.4.1.4.3.1                  Header specifics
                              The following table describes the specific values and changes to the standard header
                              described in section 12.4.1.4.2 for telegram type 1 Primary Data – Spherical Coordinate.
                              Table 21: Description of the fields of the Compact frame header
                               Name                             Offset         Change compared to standard header
                                                                (bytes)
                               Telegram type                    4              For telegram type Primary Data – Spherical Coordi-
                                                                               nates, this is set to 1.
                               Telegram version                 24             For telegram type Primary Data – Spherical Coordi-
                                                                               nates, this value is set to 4 for the latest version.
                               Payload length                   28             For telegram type Primary Data – Spherical Coordi-
                                                                               nates, this is the size of the first module.
                               Sender id                        None           Does not exist for this telegram type in the header,
                                                                               following fields are shifted to the previous field with-
                                                                               out padding.

                              Table 22: Version history for the telegram version field of the telegram type Primary Data –
                              Spherical Coordinates
                               Version                     Note
                               3                           First released version
                               4                           Distance scaling factor was added to the metadata


12.4.1.4.3.2                  Payload
                              The telegram type Primary Data – Spherical Coordinates is designed to transport 2D
                              and 3D LiDAR sensor data. To map different sensor specific features, the payload field
                              is separated into different modules that can group multiple layers of the sensor. Every
                              module contains the actual measurement data and metadata describing this module’s
                              measurement data.




8028981/1X1R/2026-06-10 | SICK                                                                                     multiScan165      79
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX




                    Figure 51: Schematic of the segmentation of the Primary Data – Spherical Coordinates payload
                    with a variable number of modules and a Metadata and MeasurementData block per module.


                    The layers of a sensor are separated in a new module when either the sensor uses
                    multiple physical measurement units or the sensor uses different angular resolutions
                    (e.g. a 3D LiDAR with 0.5° resolution on 0° layer and 1° resolution for other layers would
                    result in 2 modules when only a single physical measurement unit is used).
                    The following table shows the number of modules depending on the sensor family:
                    Sensor family                                  Number of modules
                    multiScan165                                   2




80   multiScan165                                                                         8028981/1X1R/2026-06-10 | SICK
                                                                                    SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12




                              Figure 52: For the multiScan136, a segment consists of four modules, which are shown as colored
                              dots in the figure: For each of the two physical measurement units 0 and 1 there are two modules:
                              One for the layers with 1° angular resolution, and one for the high resolution layers with 1/8° angular
                              resolution.


                              The modules available in a data package can vary depending on the configuration of
                              the sensor. It is therefore recommended to process module by module when reading
                              the data, as illustrated in the following pseudo code (Example of reading the individual
                              modules from a data package):
                              Read the 32 Byte Header
                              Set currentModuleSize = payloadLength from the header
                              As long as currentModuleSize =! 0
                               Read next module of size currentModuleSize
                               Set currentModuleSize = nextModuleSize from the module just read


12.4.1.4.3.3                  Metadata
                              This section describes the metadata of a module.
                              Table 23: Metadata of a module for the Compact format – Version 4
                               Offset         Name           Length     Type      Description
                               (bytes)                       (bytes)
                               32             Segment        8          uint64    Segment counter as described in see "Seg-
                                              counter                             ment counter", page 89
                               40             Frame num-     8          uint64    Counts the number of full revolutions since the
                                              ber                                 device was started.
                               48             Sender id      4          uint32    Device serial code. It can be used to detect on
                                                                                  the receiver which sensor the data was sent
                                                                                  from.
                               52             Number of     4           uint32    Number of layers contained in one module,
                                              lines in mod-                       figure 55.
                                              ule
                               56             Number of      4          uint32    Number of beams per scan from one layer,
                                              beams per                           figure 55. Scans from all layers in a module
                                              scan                                have the same number of beams.
                               60             Number of      4          uint32    Number of echoes per beam, figure 54.
                                              echoes per
                                              beam




8028981/1X1R/2026-06-10 | SICK                                                                                  multiScan165      81
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                    Offset            Name          Length    Type      Description
                    (bytes)                         (bytes)
                    64                Time stamp    Number array of     Array of acquisition times for the first beam of
                                      start         of ele- uint64      each scan in the current module. Time base is
                                                    ments *             the sensor system time in microseconds since
                                                    8                   January 1, 1970, 00:00 (UTC). If a time server is
                                                                        being used, the configured system time is used.
                                                                        The length of the array equals the Number of
                                                                        lines in module.
                    64 + N * 8 * 1    Time stamp    Number array of     Array of acquisition times for the last beam of
                                      stop          of ele- uint64      each scan in the current module. Time base is
                                                    ments *             the sensor system time in microseconds since
                                                    8                   January 1, 1970, 00:00 (UTC). If a time server is
                                                                        being used, the configured system time is used.
                                                                        The length of the array equals the Number of
                                                                        lines in module.
                    64 + N * 8 * 2 Phi              Number array of     Array of elevation angles (cf. operating instruc-
                                                    of ele- float32     tions, Coordinate system section) in radians of
                                                    ments *             each layer in the current module. The length of
                                                    4                   the array equals the Number of lines in mod-
                                                                        ule.
                    64 + (N * 8) *    Theta start   Number array of     Array of azimuth angles in radians for the first
                    2 + (N * 4) * 1                 of ele- float32     beam of each scan of a layer in the current
                                                    ments *             module. The length of the array equals the
                                                    4                   Number of lines in module.
                    64 + (N * 8) * Theta stop       Number array of     Array of azimuth angles in radians for the last
                    2 + (N * 4) * 2                 of ele- float32     beam of each scan of a layer in the current
                                                    ments *             module. The length of the equals the Number
                                                    4                   of lines in module.
                    64 + (N * 8) * Distance         4         float32   This factor is used to scale the distance val-
                    2 + (N * 4) * 3 scaling fac-                        ues in the beam data to allow the display of
                                    tor                                 values over 65,535 mm with 16 bits - Formula:
                                                                        d_mm_external = DistanceScalingFactor * d
                                                                        d is the distance value contained in the beam
                                                                        data.
                                                                        d_mm_external is the distance value in mm
                                                                        which can be derived from a consumer of
                                                                        streaming data from d. The factor can always
                                                                        be rounded to the next whole number.
                    68 + (N * 8) * Next module 4              uint32    Size of the next module, or 0 if the current
                    2 + (N * 4) * 3 size                                module is the last one. This value is important
                                                                        when reading the data using the principle in /
                                                                        figure 53.
                    72 + (N * 8) * Reserved         1         uint8     –
                    2 + (N * 4) * 3
                    73 + (N * 8) * Data content 1             uint8     The individual bits of this byte describe which
                    2 + (N * 4) * 3 echos                               data are available in that part of the measure-
                                                                        ment data that is acquired per echo, e.g., dis-
                                                                        tance or RSSI, table 24.
                    74 + (N * 8) * Data content 1             uint8     The individual bits of this byte describe which
                    2 + (N * 4) * 3 beams                               data are available in that part of the meas-
                                                                        urement data that is only acquired once per
                                                                        beam, e.g., azimuth angle or beam properties,
                                                                        table 25.
                    75 + (N * 8) * Reserved         1         uint8     Reserved field
                    2 + (N * 4) * 3




82   multiScan165                                                                               8028981/1X1R/2026-06-10 | SICK
                                                                                          SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12




                              Figure 53: Example of the NextModuleSize field for multiScan136. The modules with the 1° layers
                              are 2,660 bytes in size, the modules with the HighRes layers are 3,000 bytes in size. The value for
                              NextModuleSize in the header as well as in the first serialized module is therefore 2660 bytes, and
                              in the two subsequent modules 3000 bytes. In the last serialized module the value is 0, because
                              no further module follows.


                              The bit indices in the DataContentEchos and DataContentBeams bytes are derived as
                              described in see "Representation of bit fields", page 90.
                              Table 24: Description of the bits of Data content echos
                               Bit index           Value
                               0                   1 if distance data is available, otherwise 0.
                               1                   1 if RSSI data is available, otherwise 0.
                               2                   Reserved
                               3                   Reserved
                               4                   Reserved
                               5                   Reserved
                               6                   Reserved
                               7                   Reserved

                              Table 25: Description of the bits of Data content beams
                               Bit index           Value
                               0                   1 if additional beam properties are available, otherwise 0.
                               1                   1 if azimuth angles per beam are available, otherwise 0.
                               2                   Reserved
                               3                   Reserved
                               4                   Reserved
                               5                   Reserved
                               6                   Reserved
                               7                   Reserved




8028981/1X1R/2026-06-10 | SICK                                                                                   multiScan165   83
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

12.4.1.4.3.3.1          Measurement data
                        Each beam of a scan is represented as a tuple whose elements are represented by the
                        bytes (table 24) and Data content beams (table 25). The data available per beam (as
                        defined by Data content beams) follows. The representation of the respective contents
                        is shown in the following table.
                        Name           Lenght          Type           Description
                                       (bytes)
                        Distance       2               uint16         The measured distance can be computed as fol-
                                                                      lows:
                                                                      Distance * Distance scaling factor = Distance in mm
                                                                      For “Distance scaling factor” = 1 this value is already
                                                                      the measured distance.
                        RSSI           2               uint16         see "Representation of RSSI values", page 90
                        Beam char-     1               uint8          see "Representation of beam characteristics (Prop-
                        acteristics                                   erties)", page 91
                        (“Proper-
                        ties”)
                        Azimuth        2               uint16         uint16 integers, where the following conversion
                        angle                                         applies:
                                                                      O   a_uint: Angle value as integer
                                                                      O   a_rad: Angle value in radians.
                                                                      O   a_rad = (a_uint – 16384)/5215
                                                                      This conversion ensures that the maximum allowed
                                                                      value range of [-pi, 3*pi] is fully utilized.

                                  echo 0                  echo 1                    echo 2


                         distance_0    rssi_0     distance_1     rssi_1    distance_2     rssi_2      properties       theta


                                                       Described by                                        Described by
                                                    DataContentEchoes                                   DataContentBeams

                        Figure 54: Example representation of a beam as a tuple. There are three echoes available. Both
                        distance and RSSI values exist per echo, i.e., the corresponding bits of DataContentEcho have the
                        value 1. Values for beam properties and azimuth angle are also available, i.e., the corresponding
                        bits of DataContentBeams have the value 1.


                        The individual tuples are located directly behind each other in the data stream. Their
                        sequence is described in figure 55. Here the data is arranged in a matrix where the
                        individual layers of the current module correspond to the rows, and the columns
                        correspond to the measurement beams of the scans for the individual layers. (Note:
                        This arrangement assumes that all scans of a module have the same length, which is
                        ensured by the division into modules. The order of the beam tuples in the data stream
                        is determined by sweeping the matrix shown in figure 55 column by column, i.e., the
                        tuples of beam index 0 for all layers are incorporated into the data stream first, then the
                        tuples for beam index 1, etc.




84       multiScan165                                                                              8028981/1X1R/2026-06-10 | SICK
                                                                                             SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                               Module with one single layer
                                                                                                                        Beam index




                                                 0,0            0,1              0,2             0,3              0,4




                                   Line/ layer
                                   index


                               Module with multiple layers

                                                                                                                        Beam index




                                                 0,0            0,1             0,2              0,3              0,4


                                                 1,0           1,1,             1,2              1,4              1,4


                                                 2,0            2,1             2,2              2,3              2,4


                                                 3,0            3,1             3,2             3,3,              3,4


                                                 4,0            4,1             4,2              4,3              4,4


                                                 5,0            5,1             5,2              5,3              5,4


                                                 6,0            6,1             6,2              6,3              6,4


                                                 7,0            7,1             7,2              7,3              7,4




                              Line/ layer
                              index

                              Figure 55: Sequence of data tuples in the memory for the individual beams. Top: Module with only
                              one layer. Bottom: Module with 8 layers. The individual layers of a module correspond to the rows,
                              and the individual measurement beams correspond to the columns. For linear storage of the data
                              in the data package, this matrix is then swept column by column, as indicated by the gray arrows in
                              the figure.


                              O         The elevation angle of the data in row i is Phi[i] from the metadata.
                              O         The azimuth angle of the first beam in line i is ThetaStart[i]
                              O         The azimuth angle of the last beam in line i is ThetaStop[i]




8028981/1X1R/2026-06-10 | SICK                                                                               multiScan165      85
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX



                                                   Line 0/ Phi[0]
                             ThetaStart[0]
                             thetaStart[...

                             ThetaStart[1]
                             thetaStart[...        Line 1/ Phi[1]

                             ThetaStart[2]
                             thetaStart[...        Line 2/ Phi[2]

                             ThetaStart[3]         Line 3/ Phi[3]
                                                                          ThetaStop[0]
                               ThetaStart[4]       Line 4/ Phi[4]

                                                   Line 5/ Phi[5]
                               ThetaStart[5]
                                                                          ThetaStop[1]
                                                   Line 6/ Phi[6]
                                 ThetaStart[6]
                                                                         ThetaStop[2]
                                                   Line 7/ Phi[7]
                                   ThetaStart[7]
                                                                         ThetaStop[3]


                                                                         ThetaStop[4]

                                                                       ThetaStop[5]

                                                                     ThetaStop[6]

                                                                    ThetaStop[7]




                    Figure 56: Correspondences between measurement data and metadata using the example of a
                    module with 8 layers. Each line from figure 55 corresponds to a layer in figure 54. The first and last
                    azimuth angles of each layer, and the elevation angles of each layer are in the Phi, ThetaStart and
                    ThetaStop fields.


                        NOTE LayerIds, which define the individual layers by their elevation angle as in the
                    MSGPACK format (see table 17, page 74), are not used in the Compact format. The row
                    index of the matrix with the data relates only to the current module and is therefore
                    generally not the same as the LayerId.




                    Figure 57: Data structure example for a 2D sensor with a single module




86   multiScan165                                                                               8028981/1X1R/2026-06-10 | SICK
                                                                                          SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12




                              Figure 58: Data structure example for a 3D sensor with a four module


12.4.1.4.4             telegramType2: IMU

12.4.1.4.4.1                  Header specifics
                              The telegram type 2 IMU uses a reduced header compared to the standard Header
                              described in section 12.4.1.4.2. The following table describes the specific values and
                              changes to the standard header for telegram type IMU.
                              Table 26: Description of the fields of the Compact frame header
                               Name                          Offset         Change compared to standard header
                                                             (bytes)
                               Telegram type                 4              For telegram type IMU, this is set to 2.
                               Telegram counter              None           Does not exist for this telegram type in the header,
                                                                            following fields are shifted to the previous field with-
                                                                            out padding.
                               Transmit timestamp            None           Does not exist for this telegram type in the header,
                                                                            following fields are shifted to the previous field with-
                                                                            out padding.
                               Telegram version              24             For telegram type: IMU, this value is set to 1 for the
                                                                            latest version.
                               Payload length                None           Does not exist for this telegram type in the header,
                                                                            following fields are shifted to the previous field with-
                                                                            out padding.
                               Sender id                     None           Does not exist for this telegram type in the header,
                                                                            following fields are shifted to the previous field with-
                                                                            out padding.

                              Table 27: Version history for the telegram version field of the telegram type: IMU
                               Version                  Note
                               1                        First released version

                              The reduced header breaks down to the following structure.
                              Table 28: Payload of the telegram type 2 IMU
                               Offset      Name         Length    Type      Description
                               (bytes)                  (bytes)
                               0           Start of     4         uint32    Always four STX characters: \x2\x2\x2\x2.
                                           frame
                               4           Telegram     4         uint32    For telegram type: IMU, this is set to 2
                                           type




8028981/1X1R/2026-06-10 | SICK                                                                                  multiScan165         87
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                        Offset    Name           Length    Type     Description
                        (bytes)                  (bytes)
                        8         Telegram       4         uint32   For telegram type: IMU, this value is set to 1 for the
                                  version                           latest version


12.4.1.4.4.2            Payload
                        The telegram type IMU is designed to efficiently transport device internal IMU informa-
                        tion. The reduced standard header described in section 12.4.1.4.4.1 with the payload
                        defined in the table below:
                        Table 29: Payload of the telegram type 2 IMU- Version 1
                        Offset    Name           Length    Type     Description
                        (bytes)                  (bytes)
                        12        Acceleration 4           float    Acceleration in m/s² along the x-axis including grav-
                                  x                                 ity; gravity is not subtracted from the data.
                        16        Acceleration 4           float    Acceleration in m/s² along the y-axis including grav-
                                  y                                 ity; gravity is not subtracted from the data.
                        20        Acceleration 4           float    Acceleration in m/s² along the z-axis including grav-
                                  z                                 ity; gravity is not subtracted from the data.
                        24        Angular        4         float    Angular velocity in rad/s along the x-axis.
                                  velocity x
                        28        Angular        4         float    Angular velocity in rad/s along the y-axis.
                                  velocity y
                        32        Angular        4         float    Angular velocity in rad/s along the z-axis.
                                  velocity z
                        36        Orientation  4           float    Quaternion orientation for w-axis.
                                  quaternion w
                        40        Orientation    4         float    Quaternion orientation for x-axis.
                                  quaternion x
                        44        Orientation    4         float    Quaternion orientation for y-axis.
                                  quaternion y
                        48        Orientation    4         float    Quaternion orientation for z-axis.
                                  quaternion z
                        52        Sensor time    8         uint64   The sensor system time in microseconds since Jan-
                                  stamp                             uary 1, 1970, 00:00 (UTC). If a time server is being
                                                                    used, the configured system time is used.

                        The word size is 32 bits.
                        The data is specified in the following coordinate system based on the DIN 70000
                        system: The x-axis lies on the 0° beam of the 0° plane. The y-axis is perpendicular
                        to the x-axis and lies in the 0° plane. The y-values increase in the counter rotation
                        direction (right-handed system). The z-axis is perpendicular to the y-axis and the top of
                        the device points towards increasing z-values.




88       multiScan165                                                                            8028981/1X1R/2026-06-10 | SICK
                                                                                           SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12




                              1      Roll angle
                              2      pitch angle
                              3      Yaw angle


12.4.1.5       General measurement data definitions

12.4.1.5.1             Azimuth angle
                              The azimuth angles (also called theta angles in the data formats) of a scan are always
                              monotonically increasing.
                              For sensors that have a horizontal measuring field of 360°, this means in particular
                              that the angles of a segment can be greater than 180° if the segment exceeds the
                              +180°/-180° limit:
                                                  0°




                              90°                                      -90°

                                          160°
                                                   189°
                                                               -141°
                                                       -170°

                                           180°/ -180°

                              Figure 59: Azimuth angle for different segments. The angular range of the blue segment exceeds
                              the 180°/-180° limit. Since the azimuth angles are nevertheless monotonically ascending, angles
                              > 180° are used here. The green segment already starts in the negative angular range, which is why
                              the azimuth angles are negative here.


12.4.1.5.2             Segment counter
                              The segment counter counts the segments in a frame. A frame is all the data recorded
                              in one revolution. The segment counter is a value between 0 and < number of segments
                              per revolution > - 1 and increases with increasing azimuth angle.




8028981/1X1R/2026-06-10 | SICK                                                                              multiScan165    89
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                              An exception to this is shown in figure 60: Here the beams of a segment exceed the
                              +180°/-180° limit so most azimuth angles of this segment have values > 180°, see
                              "Azimuth angle", page 89. (This would correspond to negative values close to -180°
                              when normalized to (-180°, +180°].) If the majority of the values of the segment are
                              > 180°, this segment is assigned the segment counter 0 again. This only applies to the
                              multiScan100 due to the specific arrangement of the lasers in the measuring module.
                                                              0°




                                  -90                                            -90°



                                                                           computed counter = 12
                                                                           new counter = 12
                                                                      209° module 12 = 0
                              computed counter = 11
                                                       179°

                                                      180° -180°

                              Figure 60: Segment counter for a segment (blue), the majority of whose azimuth angles are > 180°.
                              Assuming a segment size of 30°, the segment counter would be 12 if it were calculated only on the
                              basis of the angle values. The majority of the blue segment is already in the next frame, however,
                              which is why it is assigned the segment number 0.


12.4.1.5.3              Representation of RSSI values
                              RSSI values are represented as a 16-bit integer (uint16). The RSSI is a dimensionless
                              quantity. The values can fall within the complete value range between 0 and 216 – 1,
                              whereby it is possible that the maximum value is rarely or even never reached. The
                              RSSI is generally also not standardized and therefore not exactly comparable between
                              devices.

12.4.1.5.4              Representation of bit fields
                              For both the DataContentEchos and DataContentBeams values and for the beam prop-
                              erties (see "Representation of beam characteristics (Properties)", page 91), bytes are
                              interpreted as bit fields in which information about the states of the individual bits is
                              encoded.
                              The relationship between the representation of the byte as a decimal value and its bit
                              indices is as follows:
                              O       Let bi with i = 0,...,k be the bits with index i in the binary representation of a value v
                                      with, bi ∈ {0,1}.
                              O       The decimal representation vdec of v is then given as vdec = ∑i=0..7 bi * 2i

                              Examples:

                              Let v be an 8-bit value with decimal representation vdec and hexadecimal representa-
                              tion vhex. Let the bit indices of v be b0 to b7.

                              Table 30: Examples of the relationship between the bit indices and the decimal representation of a
                              value
                               Bit num- Bit 7                 Bit 6      Bit 5          Bit 4      Bit 3   Bit 2         Bit 1        Bit 0
                               ber
                               Bit value 1                    1          1              1          1       1             1            1




90       multiScan165                                                                                                8028981/1X1R/2026-06-10 | SICK
                                                                                                               SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                               Bit num- Bit 7        Bit 6      Bit 5       Bit 4      Bit 3      Bit 2      Bit 1          Bit 0
                               ber
                               Bit posi- 27          26         25          24         2³         2²         21             20
                               tion
                               Decimal 128           64         32          16         8          4          2              1
                               value

                              Table 31: Examples for the decimal value 128.
                               Bit num- Bit 7        Bit 6      Bit 5       Bit 4      Bit 3      Bit 2      Bit 1          Bit 0
                               ber
                               Bit value 1           0          0           0          0          0          0              0
                               Bit posi- 27          26         25          24         2³         2²         21             20
                               tion
                               Decimal 128
                               value
                               Hexa-       0x80
                               deximal
                               value

                              Table 32: Examples for the decimal value 1.
                               Bit num- Bit 7        Bit 6      Bit 5       Bit 4      Bit 3      Bit 2      Bit 1          Bit 0
                               ber
                               Bit value 0           0          0           0          0          0          0              1
                               Bit posi- 27          26         25          24         2³         2²         21             20
                               tion
                               Decimal 1
                               value
                               Hexa-       0x01
                               deximal
                               value

                              Table 33: Examples for the decimal value 130.
                               Bit num- Bit 7        Bit 6      Bit 5       Bit 4      Bit 3      Bit 2      Bit 1          Bit 0
                               ber
                               Bit posi- 1           0          0           0          0          0          1              0
                               tion
                               Bit posi- 27          26         25          24         2³         2²         21             20
                               tion
                               Decimal 130
                               value
                               Hexa-       0x82
                               deximal
                               value


12.4.1.5.5             Representation of beam characteristics (Properties)
                              The additional characteristics of a beam are called “properties” here. They are encoded
                              in a bit field according to "Representation of bit fields", page 90. The meaning of the
                              individual bit indices is shown in the following table.
                              Table 34: Description of the bits of the field for beam characteristics (Properties)
                               Bit index                     Content
                               0                             1 if a reflector was detected for any echo on this beam, otherwise 0.
                               1                             Reserved
                               2                             Reserved
                               3                             Reserved
                               4                             Reserved
                               5                             Reserved
                               6                             Reserved



8028981/1X1R/2026-06-10 | SICK                                                                                    multiScan165      91
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                                   Bit index                   Content
                                   7                           Reserved

                                  If the reflector bit (bit with index 0) is set for a beam, it can be assumed that the last
                                  echo measured for this beam came from a reflector. It is virtually impossible physically
                                  for a reflector to be measured for an echo and then be followed by another on the same
                                  beam.

12.4.1.6           Behavior of serialization for data reduction
                                  Different data reduction options (e.g., limiting the number of available echoes, limiting
                                  the azimuth angular range, limiting the layers used) affect the data output in different
                                  ways.
                                  The behavior is somewhat different for the MSGPACK format and the Compact format.
                                  The data reduction can be configured either via all available configuration paths. These
                                  effects are described in this section.

12.4.1.6.1                  Behavior in relation to the number of available echoes
                                  Multi-echo capable sensors usually provide the option to define the number of available
                                  echoes by means of an echo filter. This then affects the data output as follows:

                                  All echoes setting
                                  If the sensor is configured so that all echoes are available, then all theoretically avail-
                                  able echoes are also always serialized, regardless of the number of echoes actually
                                  received per beam. If fewer echoes than theoretically available are received on a beam,
                                  the measured values for the remaining echoes (distance and RSSI) are padded with 0
                                  (see also the example in table 35).

                                  Single echo setting
                                  If the sensor is configured so that only a single echo is available (e.g., last or first echo),
                                  only the data for this echo is serialized.
                                  Table 35: Example data output for different numbers of available echoes
                                                                     All echoes                                Last echo
                                   Angles          Distance echo Distance echo Distance echo Distance
                                                   0             1             2
                                   42°             3,422 mm        5,022 mm         0 mm            5,022 mm
                                   43°             3,420 mm        0 mm             0 mm            3,420 mm
                                   44°             0 mm            0 mm             0 mm            0 mm

                                  Example:
                                  O   The sensor is capable of measuring a maximum of 3 echoes, and it is configured to
                                      output all echoes (All Echoes columns) or the last echo (Last Echo column).
                                  O      For the angle 42° the measured distance is 3,422 mm for echo 0 and 5,022mm for
                                         echo 1, for the angle 43° the measured distance is 3,420 mm for echo 0, and for
                                         angle 44° no valid distance is measured.
                                  O      The following distance values are then output (RSSI values are omitted for reasons
                                         of clarity, they are treated in the same way as distance values):

12.4.1.6.2                  Behavior when restricting the azimuth angular range
                                  If a restricted azimuth angular range is configured for the data output, it is possible for
                                  complete segments to lie outside the configured angular range. These segments are
                                  not serialized and therefore not transmitted from the device to the client.




92           multiScan165                                                                                8028981/1X1R/2026-06-10 | SICK
                                                                                                   SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                              For sensors with different physical measuring modules, for example the multiScan1xx,
                              it should be noted that complete segments only lie outside the configured angular
                              range if this applies to the data of both measuring modules. If data from one measuring
                              module only lies within the available angular range, the segment will still be output.
                              The layers of the other measuring module for which the data are outside the available
                              angular range, are then treated as follows:

                              MSGPACK format
                              If the data of a layer is completely outside the configured angular range, that layer will
                              not be output, see "Behavior when reducing the available layers", page 93. As soon as
                              at least one beam is within the configured angular range, both the distance value and
                              the RSSI value are set to 0 for the remaining beams of the segment, and the azimuth
                              angle remains unchanged.

                              Compact format
                              If the data of a layer are completely outside the configured angular range, then in
                              contrast to the MSGPACK format the distance values and the RSSI values are set to 0
                              for that layer, and the azimuth value is output unchanged. As soon as at least one beam
                              is within the configured angular range, the procedure is the same as for the MSGPACK
                              format: For the remaining beams of the segment, both the distance value and the RSSI
                              value are set to 0, and the azimuth angle remains unchanged.
                              The different behavior for the MSGPACK format and the Compact format is due to the
                              fact that in the case of the Compact format, the data structure needs to remain the
                              same for each segment so the data can be easily interpreted (e.g., via memcpy into a
                              structure). This is not necessary with the MSGPACK format, where the data has to be
                              parsed anyway. A more extensive data reduction is therefore possible in this case.


                                                                                  MSGPACK and Compact:
                                                               Parameterized      Distance and RSSI are ﬁlled with 0
                                                               angle
                                                               range




                                                                                                 scan layers
                                                                                                 of measuring module 0
                                                                                                 scan layers
                                                                                                 of measuring module 1


                              MSGPACK: no output
                              Compact: Distance and RSSI are ﬁlled with 0
                              Figure 61: Handling of data that is outside the configured angular range. Data from 4 layers are
                              shown, all belonging to one segment but to different measuring modules. red and violet: measur-
                              ing module 0, blue and green: measuring module 1. With no restriction of the angular range, the
                              data would be output for all layers. With the angular range restriction shown (red circle segment),
                              the data is output as follows: The blue layer and the green layer are not output in the MSGPACK
                              format, and in the Compact format distance and RSSI are filled with 0. Distance and RSSI values in
                              the part of the red layer outside the configured angular range are padded with 0 in the MSGPACK
                              format and Compact format.


12.4.1.6.3             Behavior when reducing the available layers
                              For multilayer sensors, for example the multiScan1xx, it is possible for individual layers
                              to fall within the measuring range excluded by data reduction. This can occur, for
                              example, when using a layer filter. The layers for the complete azimuth angular range




8028981/1X1R/2026-06-10 | SICK                                                                                 multiScan165      93
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                       are excluded. The case where the data for a layer are outside the measuring range only
                       in individual segments is described in "Behavior when restricting the azimuth angular
                       range", page 92.
                       For the MSGPACK format, this affects the serialization as follows:
                       O    Scan type data for the layers that have been excluded will no longer appear in the
                            SegmentData array (see table 17, page 74).
                       O     The LayerId array (see table 17, page 74) is adjusted accordingly, i.e., the IDs of the
                             layers that are no longer present are removed.
                       For the Compact format, this affects the serialization as follow:
                       O    The data for the layers that were excluded are removed from the measurement
                            data block, i.e., the corresponding rows of the matrix in figure 55 are removed.
                       O     The metadata in the metadata block that are associated with this line will be
                             removed as well. The arrays affected are ThetaStart, ThetaStop, TimeStampStart,
                             TimeStampStop and Phi in table 23.
                       O     If all layers of a module are outside the configured measuring range, the entire
                             module (metadata and measurement data) is not output.

12.5         Telegram listing (EN)

Contents
                       12.5.1.1          About this document.....................................................................................                97
                       12.5.1.1.1             Information on the telegram listing.....................................................                           97
                       12.5.1.1.2             Explanation of symbols..........................................................................                   98
                       12.5.1.2          Communication format.................................................................................                   98
                       12.5.1.2.1             Binary telegram (CoLa B).......................................................................                    98
                       12.5.1.2.2             ASCII telegram (CoLa A).........................................................................                   99
                       12.5.1.2.3             Variable types...........................................................................................        100
                       12.5.1.2.4             Command basics.....................................................................................               101
                       12.5.1.2.5             Log in: Required user level....................................................................                   101
                       12.5.1.3          Workflows.........................................................................................................     101
                       12.5.1.3.1             Parameterize the scan............................................................................                 101
                       12.5.1.3.2             Set timestamp/data angle..................................................................... 102
                       12.5.1.3.3             Common telegrams................................................................................                 102
                       12.5.1.4          Telegrams.........................................................................................................    103
                       12.5.1.4.1             Log in [sMN SetAccessMode] ............................................................. 103
                       12.5.1.4.2             Enable/ disable CoLa user levels [sMN EnableLegacyUserLe-
                                              vel]................................................................................................................ 104
                       12.5.1.4.3             Basic Settings...........................................................................................        105
                       12.5.1.4.3.1                 Read for frequency and angular resolution [sRN
                                                    LMPscancfg]....................................................................................... 105
                       12.5.1.4.3.2                 Set scan configuration [sMN mCLsetscancfglist]...................                                          106
                       12.5.1.4.3.3                 Start measurement [sMN LMCstartmeas].................................                                       107
                       12.5.1.4.3.4                 Stop measurement [sMN LMCstopmeas].................................. 108
                       12.5.1.4.3.5                 Autostart measurement [sWN LMPautostartmeas]................                                               109
                       12.5.1.4.3.6                 Load factory defaults [sMN mSCloadfacdef]............................                                       110
                       12.5.1.4.3.7                 Load application defaults [sMN mSCloadappdef]..................                                              111
                       12.5.1.4.3.8                 Change password [sMN SetPassword].......................................                                     111
                       12.5.1.4.3.9                 Check password [sMN CheckPassword]....................................                                      113


94     multiScan165                                                                                                       8028981/1X1R/2026-06-10 | SICK
                                                                                                                    SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                              12.5.1.4.3.10         Set contamination indication settings [sWN Contamina-
                                                    tionConfig]...........................................................................................         114
                              12.5.1.4.3.11         Read contamination indication settings [sRN Contamina-
                                                    tionConfig]...........................................................................................         115
                              12.5.1.4.3.12         Send contamination indication data permanently [sEN
                                                    ContaminationData].........................................................................                    116
                              12.5.1.4.3.13         Read contamination indication result [sRN Contamination-
                                                    Result]...................................................................................................     118
                              12.5.1.4.3.14         Send contamination indication result permanently [sEN
                                                    ContaminationResult]......................................................................                     118
                              12.5.1.4.3.15         Save parameters permanently [sMN mEEwriteall]..................                                                119
                              12.5.1.4.3.16         Set to run [sMN Run]......................................................................... 120
                              12.5.1.4.3.17         Reboot device [sMN mSCreboot].................................................                                 121
                              12.5.1.4.4      Measurement output telegram............................................................                              122
                              12.5.1.4.4.1          Configure aperture angle of the scandata for output [sWN
                                                    LMPoutputRange].............................................................................                   122
                              12.5.1.4.4.2          Read for actual output range [sRN LMPoutputRange]...........                                                   123
                              12.5.1.4.4.3          Set scan data enable [sWN ScanDataEnable]..........................                                            124
                              12.5.1.4.4.4          Set streaming ethernet settings [sWN ScanDataEthSet-
                                                    tings].....................................................................................................    125
                              12.5.1.4.4.5          Read streaming ethernet settings [sRN ScanDataEthSet-
                                                    tings].....................................................................................................    126
                              12.5.1.4.4.6          Set IMU data enable [sWN ImuDataEnable]..............................                                          127
                              12.5.1.4.4.7          Set IMU data streaming ethernet settings [sWN ImuDa-
                                                    taEthSettings].....................................................................................            127
                              12.5.1.4.4.8          Read scan data format [sRN ScanDataFormat]........................ 128
                              12.5.1.4.4.9          Set Scan data format [sWN ScanDataFormat]..........................                                            129
                              12.5.1.4.5      Time stamp................................................................................................ 130
                              12.5.1.4.5.1          Set time synchronization [sWN TSCRole]................................... 130
                              12.5.1.4.5.2          Set time stamp [sMN LSPsetdatetime].......................................                                     131
                              12.5.1.4.5.3          Read device time [sRN DeviceTime]............................................ 133
                              12.5.1.4.5.4          Set NTP (Network Time Protocol) parameters..........................                                           133
                              12.5.1.4.6      Filters...........................................................................................................   137
                              12.5.1.4.6.1          Set particle filter [sWN LFPparticle].............................................                             137
                              12.5.1.4.6.2          Set echo filter [sWN FREchoFilter]...............................................                              138
                              12.5.1.4.6.3          Set sensitivity fog filter [sWN MCSenseLevel]..........................                                        139
                              12.5.1.4.6.4          Set cubic area filter [sWN LFPcubicareafilter]..........................                                       139
                              12.5.1.4.6.5          Set angle range filter [sWN LFPangleRangeFilter]..................                                             141
                              12.5.1.4.6.6          Read angle range filter [sRN LFPangleRangeFilter]...............                                               142
                              12.5.1.4.6.7          Set interval filter [sWN LFPintervalFilter].................................... 143
                              12.5.1.4.6.8          Set layer filter [sWN LFPlayerFilter].............................................                             144
                              12.5.1.4.6.9          Set moving averaging filter [sWN LFPmovingAveragingFil-
                                                    ter].......................................................................................................... 145
                              12.5.1.4.6.10         Set radial distance range filter [sWN LFPradialDistanceR-
                                                    angeFilter]...........................................................................................         146
                              12.5.1.4.6.11         Set Ground Filter [sWN groundFilterEnable].............................                                        147
                              12.5.1.4.6.12         Read Ground Filter state [sRN groundFilterEnable]................ 148


8028981/1X1R/2026-06-10 | SICK                                                                                                           multiScan165              95
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                    12.5.1.4.6.13         Read Ground Filter type [sRN groundFilterType]......................                                         149
                    12.5.1.4.6.14         Set Ground Filter thresholds [sWN groundFilterThresholds]
                                          ................................................................................................................ 150
                    12.5.1.4.6.15         Read Ground Filter thresholds [sRN groundFilterThres-
                                          holds] ...................................................................................................   152
                    12.5.1.4.7      Inputs and Outputs..................................................................................               153
                    12.5.1.4.7.1          Read state of the ports [sRN LIDportstate]................................                                   153
                    12.5.1.4.7.2          Read Port Configration of all I/Os [sRN PortConfiguration]... 155
                    12.5.1.4.7.3          Set port configuration [sWN PortConfiguration]....................... 158
                    12.5.1.4.7.4          Read state of the inputs [sRN LIDinputstate]............................                                       161
                    12.5.1.4.7.5          Read state of the outputs [sRN LIDoutputstate].......................                                        163
                    12.5.1.4.7.6          Receive outputstate by event [sEN LIDoutputstate]...............                                             163
                    12.5.1.4.7.7          Set output state [sMN mDOSetOutput]....................................... 164
                    12.5.1.4.7.8          Reset output counter [sMN LIDrstoutpcnt]................................                                     165
                    12.5.1.4.8      Status..........................................................................................................    166
                    12.5.1.4.8.1          Read firmware version [sRN DeviceIdent].................................. 166
                    12.5.1.4.8.2          Read version of the application software [sRN Firmware-
                                          Version]................................................................................................      167
                    12.5.1.4.8.3          Read the device state [sRN DevSta]............................................                               168
                    12.5.1.4.8.4          Read the device state [sRN SCdevicestate]..............................                                       169
                    12.5.1.4.8.5          Read device order number [sRN OrdNum]................................                                         170
                    12.5.1.4.8.6          Read serial number [sRN SerialNumber]...................................                                       171
                    12.5.1.4.8.7          Read device type [sRN DItype]......................................................                           172
                    12.5.1.4.8.8          Read operating hours [sRN ODoprh]...........................................                                  173
                    12.5.1.4.8.9          Read operating hours since last power on [sRN ODopdaily]                                                      174
                    12.5.1.4.8.10         Read power on counter [sRN ODpwrc].......................................                                     174
                    12.5.1.4.8.11         Read temperature [sRN OPcurtmpdev]......................................                                      175
                    12.5.1.4.8.12         Set device name [sWN LocationName]......................................                                      176
                    12.5.1.4.8.13         Read device name [sRN LocationName]...................................                                        177
                    12.5.1.4.8.14         Initiate an acoustic or visual signal for a defined period of
                                          time [sMN FindMe]............................................................................                 177
                    12.5.1.4.8.15         Read date of last permanent save [sRN DIpara]......................                                           178
                    12.5.1.4.8.16         Read time of last permanent save [sRN DIparatm].................                                              179
                    12.5.1.4.8.17         Read the current device temperature alarm status [sRN
                                          temperatureAlarmStatus]...............................................................                       180
                    12.5.1.4.8.18         Set device temperature alarm configuration [sWN temper-
                                          atureAlarmConfiguration]...............................................................                       181
                    12.5.1.4.8.19         Read device temperature alarm configuration [sRN tem-
                                          peratureAlarmConfiguration].........................................................                         182
                    12.5.1.4.9      Interfaces...................................................................................................      183
                    12.5.1.4.9.1          Set IP address [sWN EIIpAddr]......................................................                          183
                    12.5.1.4.9.2          Read IP address [sRN EIIpAddr].................................................... 184
                    12.5.1.4.9.3          Read IP address assigned by DHCP [sRN EIIpAddrDHCP]...                                                       185
                    12.5.1.4.9.4          Set mode for ethernet adress assignment [sWN EIAddr-
                                          Mode]....................................................................................................    186
                    12.5.1.4.9.5          Set fallback for DHCP [sWN EIDHCPFallback].........................                                           187



96   multiScan165                                                                                                8028981/1X1R/2026-06-10 | SICK
                                                                                                           SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                              12.5.1.4.9.6                Set Ethernet gateway [sWN Elgate].............................................                            187
                              12.5.1.4.9.7                Read Ethernet gateway [sRN Elgate]........................................... 188
                              12.5.1.4.9.8                Read ethernet gateway IP adress assigned by DHCP [sRN
                                                          ElgateDHCP].......................................................................................        189
                              12.5.1.4.9.9                Set IP mask [sWN EImask]..............................................................                   190
                              12.5.1.4.9.10               Read IP mask [sRN EImask]...........................................................                       191
                              12.5.1.4.9.11               Read IP mask assigned by DHCP [sRN EImaskDHCP]...........                                                 192
                              12.5.1.4.9.12               Read MAC address [sRN EIMacAdr]............................................                               193
                              12.5.1.4.9.13               Set device search mode [sWN EtherColaScanMode]............                                                194
                              12.5.1.4.9.14               Read device search mode [sRN EtherColaScanMode].........                                                  195
                              12.5.1.4.9.15               Enable/ disable CoLa1 interface [sWN EIAuxEnable].............                                            196
                              12.5.1.4.9.16               Set Webserver state [sMN SetWebserverEnabled].................                                            197
                              12.5.1.4.9.17               Read Webserver state [sMN GetWebserverEnabled]............. 198
                              12.5.1.4.9.18               Enable/ disable LEDs [sWN LEDEnable]....................................                                  198
                              12.5.1.4.9.19               Read state of LEDs [sRN LEDState].............................................                            199
                              12.5.1.4.10           Application................................................................................................. 200
                              12.5.1.4.10.1               Set activation of evaluation group [sMN ActivateEvalua-
                                                          tionGroup]............................................................................................ 200
                              12.5.1.4.10.2               Set field evaluation contour [sMN SetFieldEvaluationCon-
                                                          tour]....................................................................................................... 202
                              12.5.1.4.10.3               Read the current evaluation configuration state [sRN Eval-
                                                          uationConfigState]............................................................................ 204
                              12.5.1.4.10.4               Read field evaluation result [sRN FieldEvaluationResult]...... 205
                              12.5.1.4.10.5               Receive field evaluation result by event [sEN FieldEvalua-
                                                          tionResult]........................................................................................... 207
                              12.5.1.4.10.6               Request perpendicular distance once [sRN perpendicular-
                                                          DistanceResult].................................................................................. 209
                              12.5.1.4.10.7               Request perpendicular distance continiously on event
                                                          [sEN perpendicularDistanceResult]............................................                            210
                              12.5.1.4.10.8               Read evaluation group type [sRN EvaluationGroupType]......                                                212
                              12.5.1.5         Diagnostics......................................................................................................    213
                              12.5.1.5.1            SOPAS error codes..................................................................................             213

12.5.1.1       About this document

12.5.1.1.1             Information on the telegram listing

                              NOTE
                              In case you prefer to use complete drivers instead of single telegrams, the following
                              options are availabe:
                              C++ drivers: https://github.com/SICKAG/sick_perception_sdk
                              ROS2 drivers: https://github.com/SICKAG/sick_scan_xd


                              NOTE
                              Telegrams that are not described in this document for the device should not be imple-
                              mented as they may either be incompetible or cause undesired effects.




8028981/1X1R/2026-06-10 | SICK                                                                                                             multiScan165              97
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX


                                  NOTE
                                  CoLa 2 is a SICK specific communication protocol which is used for communication
                                  between SICK devices and SICK specific tools and services only.

                                  Please read this chapter carefully before beginning to use the telegram listing.
                                  The telegram listing shows how to send telegrams via a terminal program using the
                                  SICK protocol CoLa A (ASCII and hexadecimal values, with TCP port 2111) or CoLa B
                                  (binary/hexadecimal values, with TCP port 2112 only) to the device . This comprises the
                                  query of the current device state or certain parameter values, how to modify parameter
                                  values and the way in which the device confirms or responds to commands/telegrams.
                                  The devices generally support automatic IP address discovery.
                                  Default IP address is:
                                  O   192.168.0.1
                                  Subnet mask is 255.255.255.0.
                                  IP ports:
                                  O    2111: CoLa A
                                  O    2112: CoLa B
                                  Most parameter changes also require certain user levels. Additionally, commands may
                                  change during the product lifecycle and development process with a new firmware.
                                  This document is based on the following firmware version (or newer):
                                  O    V2.0.0
                                  If commands do not seem to work, please verify that your device version supports this
                                  functionality, that the minimum required user level has been selected and check on
                                  updates of this documentation.

12.5.1.1.2                  Explanation of symbols

                                  NOTE
                                  … highlights useful tips and recommendations as well as information for efficient and
                                  trouble-free operation.


                                                        Telegram to device


                                                        Telegram from device


                                                        Unformatted example to copy and paste



12.5.1.2           Communication format

12.5.1.2.1                  Binary telegram (CoLa B)
                                  The binary telegram is a basic protocol of the scanner (CoLa B). All values are in
                                  hexadecimal code and grouped into pairs of two digits (= 1 byte). The string consists
                                  of four parts: header, data length, data and checksum (CS). It is highly recommended
                                  to use this protocol as the transmitted data amount is only about half as much as with
                                  CoLa A).
                                  The header indicates with 4 × STX (02 02 02 02) the start of the telegram.




98           multiScan165                                                                            8028981/1X1R/2026-06-10 | SICK
                                                                                               SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                              The data length defines the size of the data part (command part) by indicating the
                              number of digit pairs in the third part. The size of the data length itself is 4 bytes,
                              which means that the data part might have a maximum of 168 = 4,294,967,295 digit pairs
                              (bytes).
                              The data part comprises the actual command with letters and characters converted
                              to Hex (according to the ASCII chart) and the parameters of either decimal numbers
                              converted to Hex or fixed Hex values with a specific, intrinsic meaning (no conversion).
                              There is always a space (20) between the command and the parameters, but not
                              between the different parameter values.
                              The checksum finally serves to verify that the telegram has been transferred correctly.
                              The length of the checksum is 1 byte, CRC8. It is calculated with XOR.
                              Table 36: Example: Binary telegram
                               02 02 02     00 00 00   73 4D 4E 20 53 65 74 41 63 63 65 73 73 4D 6F 64 65 20 03 F4 72 47 B3
                               02           17         44
                               Header       Length     Data                                                             CS

                              This is an example telegram for setting the user level “Authorized Client”:
                              O    Header = 02 02 02 02
                              O    Length = 23 bytes (17h)
                              O    Data:
                                   -      73 4D 4E 20 = sMN = start of Sopas command (and space)
                                   -      53 65 74 41 63 63 65 73 73 4D 6F 64 65 20 = Set Access Mode = the actual
                                          command for setting the user level (and space)
                                   -      03 = fixed Hex value meaning user level “Authorized Client”
                                   -      F4 72 47 44 = fixed Hex value, serving as password for the selected user level
                                          “Authorized Client”
                              O    Checksum = B3 from XOR calculation

12.5.1.2.2             ASCII telegram (CoLa A)
                              The ASCII telegram is an alternative to the binary telegram, suitable especially to para-
                              metrize the sensor. However, due to the variable string length of ASCII telegrams, the
                              Binary telegram is still recommended when using scanners with a PLC.
                              The ASCII telegram has the advantage that commands can be written in plaintext. The
                              string consists only of two parts: the framing and the data part.
                              The framing indicates with <STX> and <ETX> the start and stop of each telegram.
                              The data part comprises the actual command with letters and characters (plaintext),
                              parameter values either in decimal (special indicator required) or in hexadecimal
                              (example: a frequency of 25 Hz = +2500 (decimal) = 09C4 (Hex)) and fixed hexadecimal
                              values with a specific, intrinsic meaning.

                              NOTE
                              Leading zeros are deleted in ASCII. Therefore a space is always required between all
                              command parts and parameter parts.

                              As further alternative within CoLa A, depending on the preferences of the user, all
                              values can be written directly in Hex. This means however a 1:1 conversion of all letters
                              and characters including numbers and fixed hexadecimal values via the ASCII chart.

                              NOTE
                              The device will confirm parameter values always in hexadecimal code, regardless of the
                              code sent.



8028981/1X1R/2026-06-10 | SICK                                                                           multiScan165    99
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                              Table 37: Example: ASCII telegram
                              ASCI        <STX> sMN{SPC}SetAccessMode{SPC}03{SPC}F4724744                                          <ETX>
                              I
                              Hex             02 73 4D 4E 20 53 65 74 41 63 63 65 73 73 4D 6F 64 65 20 30 33 20 46 34              03
                                                 37 32 34 37 34 34
                                           Start Data                                                                              Stop

                              This is again an example telegram for setting the user level “Authorized Client”. As only
                              fixed hexadecimal parameter values are needed, the option to use parameter values in
                              decimal code with special indicator cannot be applied here:
                              O       Framing = <STX> = telegram start = 02 (Hex)
                              O       Data:
                                      -     sMN = start of Sopas command (and blank) = 73 4D 4E 20 (Hex)
                                      -     SetAccessMode = the actual command for setting the user level (and blank)
                                            = 53 65 74 41 63 63 65 73 73 4D 6F 64 65 20 (Hex)
                                      -     03 = fixed Hex value meaning user level “Authorized Client” (and blank) = 30
                                            33 20 (Hex)
                                      -     F4 72 47 44 = fixed Hex value, serving as password for the selected user level
                                            “Authorized Client” = 46 34 37 32 34 37 34 34 (Hex)
                              O       Framing = <ETX> = telegram stop = 03 (Hex)

12.5.1.2.3              Variable types
                                  Variable type          Length (byte)                   Value range                           Sign
                              Bool_1                1                      0 or 1                                       No
                              Uint_8                1                      0 … 255                                      No
                              Int_8                 1                      -128 … +127                                  Yes
                              Uint_16               2                      0 … 65,535                                   No
                              Int_16                2                      -32,768 … +32,767                            Yes
                              Uint_32               4                      0 … 4,294,967,295                            No
                              Int_32                4                      -2,147,483,648 … +2,147,483,647              Yes
                              ULInt_64              8                      0 ... 18446744073709551616                   No
                              Enum_8                1                      Certain values defined in a list of          No
                                                                           Choices (0 … 255)
                              Enum_16               2                      Certain values defined in a list of          No
                                                                           Choices (0 … 65535)
                              String                Context-depend-        Strings are not terminated in zeroes
                                                    ent
                              FlexString            array of visible       See description of String and FlexArray
                                                    characters with
                                                    preceeding cur-
                                                    rent length
                                                    (UInt lenght)
                                                    (array of 8 bit)
                              Real                  4                      Float according to                           Yes
                                                                           IEEE754 (see www.h-schmidt.net/
                                                                           FloatConverter/IEEE754de.html)

                              Data length is always given in Bytes!
                              Struct                    A structure is a sequence of further types. These types can be of a BasicType,
                                                        Structs again or an Array.
                              Array                     An Array is a repetition of a type. The length of the array is defined with
                                                        each Array. The types can be of a BasicType, a Struct or an Array again (n-
                                                        dimensional).




100      multiScan165                                                                                          8028981/1X1R/2026-06-10 | SICK
                                                                                                         SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                               Flex Array         A FlexArray is a repetition of a type with a variable length. The maximum
                                                  length of the array is defined with each FlexArray. The current length of the
                                                  FlexArray is transferred as a UInt preceeding the Array itself. The types can
                                                  be of a BasicType, a Struct or an Array again (n- dimensional).


12.5.1.2.4             Command basics
                              SOPAS communication is a index based communication and can be identified with
                              telegram beginning of: sRI, sWI, sMI, sAI, sEI, sSI. Since the parallel usage of one port
                              might be confusing, the usage of separate ports is adviced.
                              Every response telegram starts with a separat framed string:
                              <STX>sSI 2 1<ETX><STX>“Answer”<ETX>
                                   Description      Value ASCII              Value Hex                     Value Binary
                               Start of text     <STX>              02                              02 02 02 02 + given length
                               End of text       <ETX>              03                              Calculated checksum
                               Read              sRN                                         73 52 4E
                               Write             sWN                                         73 57 4E
                               Method            sMN                                         73 4D 4E
                               Event             sEN                                         73 45 4E
                               Answer            sRA                                         73 52 41
                                                 sWA                                         73 57 41
                                                 sAN                                         73 41 4E
                                                 sEA                                         73 45 41
                                                 sSN                                         73 53 4E
                               Space             {SPC}              20                              20

                              If values are divided into two parts (e.g. measurement data), they are documented
                              according to LSB 0 (e.g. 00 07), output however is according to MSB (e.g. 07 00).

                              NOTE
                              Every write command (sWN) has a read (sRN) counter part even if it may not be descri-
                              bed in the Telegram Listing. You can verify the current parameters this way, e.g. read the
                              current IP address via sRN EIIpAddr see "Read IP address [sRN EIIpAddr]", page 184.


12.5.1.2.5             Log in: Required user level
                                                         Task                                       Required user level
                               Change sensor parameters                                   Authorized Client
                               Requests or queries                                        None
                               (e.g. for measurement data or device state)
                               Manage passwords                                           Service

                              In general, every sWN command for changing paramters requires to log in to the device
                              first see "Log in [sMN SetAccessMode] ", page 103. When being logged in, any desired
                              parameter valid for this user level can be changed. All changes become active only
                              after having logged off again from the device via the sMN Run command see "Set to run
                              [sMN Run]", page 120.
                              In this document, a required, specific user level is indicated in the telegram structure
                              head line.

12.5.1.3       Workflows

12.5.1.3.1             Parameterize the scan
                              Log in: sMN SetAccessMode see "Log in [sMN SetAccessMode] ", page 103



8028981/1X1R/2026-06-10 | SICK                                                                                multiScan165    101
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                             Configure scandata output: sWN LMPoutputRange see "Configure aperture angle of the
                             scandata for output [sWN LMPoutputRange]", page 122
                             Store parameters: sMN mEEwriteall see "Save parameters permanently [sMN mEE-
                             writeall]", page 119
                             Log out: sMN Run see "Set to run [sMN Run]", page 120


12.5.1.3.2              Set timestamp/data angle
                             Log in: sMN SetAccessMode see "Log in [sMN SetAccessMode] ", page 103

                             SOPAS command: sMN LSPsetdatetime see "Set time stamp [sMN LSPsetdatetime]",
                             page 131
                             Log out: sMN Run see "Set to run [sMN Run]", page 120


12.5.1.3.3              Common telegrams
                             The following telegrams are valid for a wide range of non-safe LiDAR sensors from
                             SICK. Please refer to the telegram listing of the respective device for a detailed descrip-
                             tion of all valid telegrams.
                              "Log in [sMN SetAccessMode] ", page 103
                              "Start measurement [sMN LMCstartmeas]", page 107
                              "Stop measurement [sMN LMCstopmeas]", page 108
                              "Load factory defaults [sMN mSCloadfacdef]", page 110
                              "Load application defaults [sMN mSCloadappdef]", page 111
                              "Change password [sMN SetPassword]", page 111
                              "Check password [sMN CheckPassword]", page 113
                              "Reboot device [sMN mSCreboot]", page 121
                              "Save parameters permanently [sMN mEEwriteall]", page 119
                              "Set to run [sMN Run]", page 120
                              "Configure aperture angle of the scandata for output [sWN LMPoutputRange]", page 122
                              "Read for actual output range [sRN LMPoutputRange]", page 123
                              "Set particle filter [sWN LFPparticle]", page 137
                              "Read state of the inputs [sRN LIDinputstate]", page 161
                              "Read state of the outputs [sRN LIDoutputstate]", page 163
                              "Set output state [sMN mDOSetOutput]", page 164
                              "Read firmware version [sRN DeviceIdent]", page 166
                              "Read the device state [sRN SCdevicestate]", page 169
                              "Read device type [sRN DItype]", page 172
                              "Read operating hours [sRN ODoprh]", page 173
                              "Read power on counter [sRN ODpwrc]", page 174
                              "Set device name [sWN LocationName]", page 176
                              "Read device name [sRN LocationName]", page 177
                              "Reset output counter [sMN LIDrstoutpcnt]", page 165
                              "Set IP address [sWN EIIpAddr]", page 183
                              "Read IP address [sRN EIIpAddr]", page 184
                              "Set Ethernet gateway [sWN Elgate]", page 187
                              "Read Ethernet gateway [sRN Elgate]", page 188
                              "Set IP mask [sWN EImask]", page 190
                              "Read IP mask [sRN EImask]", page 191




102      multiScan165                                                                               8028981/1X1R/2026-06-10 | SICK
                                                                                              SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

12.5.1.4          Telegrams
Telegrams listed in this document are described in the following basic structure:
Table 38: Telegram structure: "Command type" "Command"
                     Telegram structure: "Command type" "Command"
           (Minimum required user level. If nothing is stated, no user level required)

Telegram        Description              Variable    Length    Additional details             Values CoLa A      Values CoLa B
part                                                                                          (ASCII)            (Binary)
Lists the       Describes the corre-     Defines     Defines Gives further information        Defines the        Defines the
different       sponding telegram        the type    the       regarding the values in CoLa   value of the       value of the
parts of        parts.                   of the      length in A/ CoLa B if neccessary.       telegram part in   telegram part in
the tele-                                variable.   byte.                                    CoLa A (ASCII).    CoLa B (Binary).
gram.


NOTE
Commands are colored blue, parameters orange for further differentiation.

Table 39: Example: "Command type" "Command"
             <"Start of text">"Command type value (ASCII)""space""Command value (ASCII)""space""Parameter value
             (ASCII)""space""Parameter value (ASCII)"<"End of text">
CoLa         Copy example with framing (ASCII)
A
             Copy example without framing (ASCII)
             Copy example with framing (Hex)
             "Start of text and given length" "Command type value (Binary)""space""Command value (Binary)""space""Parameter
             value (Binary)""Parameter value (Binary)""Calculated checksum"
CoLa B
             Copy example without framing (Binary)

Table 40: Telegram structure: "Command type" "Command" (Answer)
                       Telegram structure: "Command type" "Command"


Telegram        Description              Variable    Length    Additional details             Values CoLa A      Values CoLa B
part                                                                                          (ASCII)            (Binary)
Lists the       Describes the corre-     Defines     Defines Gives further information        Defines the        Defines the
different       sponding telegram        the type    the       regarding the values in CoLa   value of the       value of the
parts of        parts.                   of the      length in A/ CoLa B if neccessary.       telegram part in   telegram part in
the tele-                                variable.   byte.                                    CoLa A (ASCII).    CoLa B (Binary).
gram.

Table 41: Example: "Command type" "Command" (Answer)
CoLa         <"Start of text">"Command type value (ASCII)""space""Command value (ASCII)""space""Parameter value
A            (ASCII)""space""Parameter value (ASCII)"<"End of text">
             <"Start of text">"Command type value (Hex)""space""Command value (Hex)""space""Parameter value
             (Hex)""space""Parameter value (Hex)"<"End of text">
CoLa B "Start of text and given length""Command type value (Binary)""space""Command value (Binary)""space""Parameter
       value (Binary)""Parameter value (Binary)""Calculated checksum"


12.5.1.4.1               Log in [sMN SetAccessMode]

NOTE
O    An automated hash-value calculator can be found in SOPAS ET under menu “password”. Required userlevel
     'Service' (see "Change password [sMN SetPassword]", page 111).




8028981/1X1R/2026-06-10 | SICK                                                                                multiScan165    103
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

A log in to the device is necessary to change parameters. In most cases, the user level 'Authorized client' is
needed. Changed parameters will be reset to the previous state via a reboot unless the are saved. To save
parameter changes the command "sMN mEEwriteall" (see "Save parameters permanently [sMN mEEwriteall]",
page 119) must be send before log out.
Table 42: Telegram structure: sMN SetAccessMode
                          Telegram structure: sMN SetAccessMode


 Telegram           Description        Variable   Length         Additional details       Values CoLa A       Values CoLa B
    part                                                                                     (ASCII)             (Binary)
Command      Method                   String      3                                      sMN                 73 4D 4E
type
Command      User level               String      13                                     SetAccess-          53 65 74 41 63
                                                                                         Mode                63 65 73 73 4D
                                                                                                             6F 64 65
User level   Select user level        Int_8       1        Maintenance:                  2                   02
                                                           Authorized client:            3                   03
                                                           Service:                      4                   04
Password     Hash value for the       Uint_32     4        Maintenance:                  B21ACE26            B2 1A CE 26
             selected user level                           Authorized client:            F4724744            F4 72 47 44
                                                           Service:                      81BE23AA            81 BE 23 AA

Table 43: Example: sMN SetAccessMode - Log in as “Authorized client” with password “F4724744”
         <STX>sMN{SPC}SetAccessMode{SPC}3{SPC}F4724744<ETX>
CoLa     <STX>sMN SetAccessMode 3 F4724744<ETX>
A        sMN SetAccessMode 3 F4724744
         02 73 4D 4E 20 53 65 74 41 63 63 65 73 73 4D 6F 64 65 20 30 33 20 46 34 37 32 34 37 34 34 03
         02 02 02 02 00 00 00 17 73 4D 4E 20 53 65 74 41 63 63 65 73 73 4D 6F 64 65 20 03 F4 72 47 44 B3
CoLa B
         73 4D 4E 20 53 65 74 41 63 63 65 73 73 4D 6F 64 65 20 03 F4 72 47 44


Table 44: Telegram structure: sAN SetAccessMode
                          Telegram structure: sAN SetAccessMode


 Telegram           Description        Variable   Length         Additional details       Values CoLa A       Values CoLa B
    part                                                                                     (ASCII)             (Binary)
Command      Answer                   String      3                                      sAN                 73 41 4E
type
Command      User level               String      13                                     SetAccess-          53 65 74 41 63
                                                                                         Mode                63 65 73 73 4D
                                                                                                             6F 64 65
Change       Changed level            Bool_1      1        Error:                        0                   00
user level                                                 Success:                      1                   01

Table 45: Example: sAN SetAccessMode

 CoLa    <STX>sAN{SPC}SetAccessMode{SPC}1<ETX>
  A      02 73 41 4E 20 53 65 74 41 63 63 65 73 73 4D 6F 64 65 20 31 03
CoLa B 02 02 02 02 00 00 00 13 73 41 4E 20 53 65 74 41 63 63 65 73 73 4D 6F 64 65 20 01 38


12.5.1.4.2              Enable/ disable CoLa user levels [sMN EnableLegacyUserLevel]
This command enables and disables a specific CoLa user level (Maintenance, Authorized Client).




104      multiScan165                                                                              8028981/1X1R/2026-06-10 | SICK
                                                                                             SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

Table 46: Telegram structure: sMN EnableLegacyUserLevel
                     Telegram structure: sMN EnableLegacyUserLevel


 Telegram           Description          Variable   Length         Additional details        Values CoLa A    Values CoLa B
    part                                                                                        (ASCII)          (Binary)
Command        Method                   String      3                                       sMN              73 4D 4E
type
Command        Enable/ disable CoLa     String      21                                      EnableLega-      45 6E 61 62 6C
               user level                                                                   cyUserLevel      65 4C 65 67 61
                                                                                                             63 79 55 73 65
                                                                                                             72 4C 65 76 65
                                                                                                             6C
User level     -                        Uint_8      1        Maintenance:                   2                02
                                                             Authorized Client:             3                03
Status         Enable/ disable          Bool_1      1        Disable:                       0                00
                                                             Enable:                        1                01

Table 47: Example: sMN EnableLegacyUserLevel - Enable User Level Authorized Client
          <STX>sMN{SPC}EnableLegacyUserLevel{SPC}3{SPC}1<ETX>
 CoLa     <STX>sMN EnableLegacyUserLevel 3 1<ETX>
  A       sMN EnableLegacyUserLevel 3 1
          02 73 4D 4E 20 45 6E 61 62 6C 65 4C 65 67 61 63 79 55 73 65 72 4C 65 76 65 6C 20 33 20 31 03
          02 02 02 02 00 00 00 1D 73 4D 4E 20 45 6E 61 62 6C 65 4C 65 67 61 63 79 55 73 65 72 4C 65 76 65 6C 20 03 20 01 21
CoLa B 73 4D 4E 20 45 6E 61 62 6C 65 4C 65 67 61 63 79 55 73 65 72 4C 65 76 65 6C 20 03 20 01


Table 48: Telegram structure: sAN EnableLegacyUserLevel
                     Telegram structure: sAN EnableLegacyUserLevel


 Telegram           Description          Variable   Length         Additional details        Values CoLa A    Values CoLa B
    part                                                                                        (ASCII)          (Binary)
Command        Answer                   String      3                                       sAN              73 41 4E
type
Command        Enable/ disable CoLa     String      21                                      EnableLega-      45 6E 61 62 6C
               user level                                                                   cyUserLevel      65 4C 65 67 61
                                                                                                             63 79 55 73 65
                                                                                                             72 4C 65 76 65
                                                                                                             6C
Status         Confirmation             Bool_1      1        unsuccessful:                  0                00
code                                                         successful:                    1                01

Table 49: Example: sAN EnableLegacyUserLevel - Enabling/ disabling of the CoLa User Level was successful

 CoLa     <STX>sAN{SPC}EnableLegacyUserLevel{SPC}1<ETX>
  A       02 73 41 4E 20 45 6E 61 62 6C 65 4C 65 67 61 63 79 55 73 65 72 4C 65 76 65 6C 20 31 03
CoLa B 02 02 02 02 00 00 00 1B 73 41 4E 20 45 6E 61 62 6C 65 4C 65 67 61 63 79 55 73 65 72 4C 65 76 65 6C 20 01 0E


12.5.1.4.3              Basic Settings


12.5.1.4.3.1                     Read for frequency and angular resolution [sRN LMPscancfg]
Read the scanning frequency, angular resolution and aperture angle of the device. Values show the information
of the values before any filters are applied. Therefore aperature angle is always showing the maximum, scanning
frequency and angular resolution may also be static depending on device family.




8028981/1X1R/2026-06-10 | SICK                                                                            multiScan165   105
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

Table 50: Telegram structure: sRN LMPscancfg
                            Telegram structure: sRN LMPscancfg


 Telegram             Description       Variable   Length             Additional details    Values CoLa A        Values CoLa B
    part                                                                                       (ASCII)              (Binary)
Command        Read                     String     3                                        sRN                 73 52 4E
type
Command        Info of scan frequency   String     10                                       LMPscancfg          4C 4D 50 73 63
               and angular resolution                                                                           61 6E 63 66 67

Table 51: Example: sRN LMPscancfg
         <STX>sRN{SPC}LMPscancfg<ETX>
 CoLa    <STX>sRN LMPscancfg<ETX>
  A      sRN LMPscancfg
         02 73 52 4E 20 4C 4D 50 73 63 61 6E 63 66 67 03
         02 02 02 02 00 00 00 0E 73 52 4E 20 4C 4D 50 73 63 61 6E 63 66 67 63
CoLa B 73 52 4E 20 4C 4D 50 73 63 61 6E 63 66 67



Table 52: Telegram structure: sRA LMPscancfg
                            Telegram structure: sRA LMPscancfg


 Telegram             Description       Variable   Length             Additional details    Values CoLa A        Values CoLa B
    part                                                                                       (ASCII)              (Binary)
Command        Answer                   String     3                                        sRA                 73 52 41
type
Command        Info of scan frequency   String     10                                       LMPscancfg          4C 4D 50 73 63
               and angular resolution                                                                           61 6E 63 66 67
Scan fre-      [1/100 Hz]               Uint_32    4        20 Hz:                          7D0h                00 00 07 D0
quency
Reserved       -                        Int_16     2        Always:                         1                   00 01
Angular        [1/10000°]               Uint_32    4        0.125°:                         4E2h                00 00 04 E2
resolution
Start angle [1/10000°]                  Int_32     4        -180° ... +180°                 FFE488C0h …         FF E4 88 C0 …
                                                                                            1B7740h             00 1B 77 40
Stop angle [1/10000°]                   Int_32     4        -180° ... +180°                 FFE488C0h …         FF E4 88 C0 …
                                                                                            1B7740h             00 1B 77 40

Table 53: Example: sRA LMPscancfg - 20 Hz scan frequency, 0.125° angular resolution, -90° start angle, +90° stop angle
         <STX>sRA{SPC}LMPscancfg{SPC}7D0{SPC}1{SPC}4E2{SPC}FFF24460{SPC}DBBA0<ETX>
 CoLa
  A      02 73 52 41 20 4C 4D 50 73 63 61 6E 63 66 67 20 37 44 30 20 31 20 34 45 32 20 46 46 46 32 34 34 36 30 20 44 42 42
         41 30 03
         02 02 02 02 00 00 00 21 73 52 41 20 4C 4D 50 73 63 61 6E 63 66 67 20 00 00 07 D0 00 01 00 00 04 E2 FF F2 44 60
CoLa B
         00 0D BB A0 43


12.5.1.4.3.2                   Set scan configuration [sMN mCLsetscancfglist]
Enable/ disable interlace mode.
The interlaced mode enables to achieve a higher angular resolution by shifting single scan points in each rotation.
With combining the shifted scans, a higher resolution can be achieved.
The device has 16 layers with a resolution of 0.5°. If the interlaced mode is active the layers will be shifted by 0.125°
for each scan. After 4 scans a theoretical resolution of 0.125° on all layers can be achieved.




106      multiScan165                                                                                 8028981/1X1R/2026-06-10 | SICK
                                                                                                SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

Table 54: Telegram structure: sMN mCLsetscancfglist
                        Telegram structure: sMN mCLsetscancfglist


 Telegram           Description         Variable   Length          Additional details         Values CoLa A    Values CoLa B
    part                                                                                         (ASCII)          (Binary)
Command        Method                   String     3                                          sMN              73 4D 4E
type
Command        Set scan configuration   String     17                                         mCLsets-         6D 43 4C 73 65
                                                                                              cancfglist       74 73 63 61 6E
                                                                                                               63 66 67 6C 69
                                                                                                               73 74
Mode           Interlace mode           Enum_8     1        Off:                              0                00
                                                            On:                               1                01

Table 55: Example: Set scan configuration 1: sMN mCLsetscancfglist 1
          <STX>sMN{SPC}mCLsetscancfglist{SPC}1<ETX>
 CoLa     <STX>sMN mCLsetscancfglist 1<ETX>
  A       sMN mCLsetscancfglist 1
          02 73 4D 4E 20 6D 43 4C 73 65 74 73 63 61 6E 63 66 67 6C 69 73 74 20 31 03
          02 02 02 02 00 00 00 17 20 73 4D 4E 20 6D 43 4C 73 65 74 73 63 61 6E 63 66 67 6C 69 73 74 20 01 0E
CoLa B 73 4D 4E 20 6D 43 4C 73 65 74 73 63 61 6E 63 66 67 6C 69 73 74 20 01



Table 56: Telegram structure: sAN mCLsetscancfglist
                        Telegram structure: sAN mCLsetscancfglist


 Telegram           Description         Variable   Length          Additional details         Values CoLa A    Values CoLa B
    part                                                                                         (ASCII)          (Binary)
Command        Answer                   String     3                                          sAN              73 41 4E
type
Command        Set scan configuration   String     17                                         mCLsets-         6D 43 4C 73 65
                                                                                              cancfglist       74 73 63 61 6E
                                                                                                               63 66 67 6C 69
                                                                                                               73 74
Status         Wrong setting            Enum_8     1        Ok:                               0                00
code                                                        Error frequency:                  1                01
                                                            Error resolution:                 2                02
                                                            Error resolution and frequency:   3                03
                                                            Error scan field:                 4                04
                                                            Error:                            5                05

Table 57: Example: sAN mCLsetscancfglist Ok

 CoLa     <STX>sAN{SPC}mCLsetscancfglist{SPC}0<ETX>
  A       02 73 41 4E 20 6D 43 4C 73 65 74 73 63 61 6E 63 66 67 6C 69 73 74 20 30 03
CoLa B 02 02 02 02 00 00 00 17 73 41 4E 20 6D 43 4C 73 65 74 73 63 61 6E 63 66 67 6C 69 73 74 20 00 03


12.5.1.4.3.3                    Start measurement [sMN LMCstartmeas]
Start the laser and (unless in Standby mode) the motor of the device




8028981/1X1R/2026-06-10 | SICK                                                                             multiScan165   107
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

Table 58: Telegram structure: sMN LMCstartmeas
                         Telegram structure: sMN LMCstartmeas
                         (User level 'Authorized Client' required)

 Telegram           Description        Variable   Length         Additional details       Values CoLa A        Values CoLa B
    part                                                                                     (ASCII)              (Binary)
Command        Method                 String      3                                       sMN                 73 4D 4E
type
Command        Start measurement      String      12                                      LMCstartmeas        4C 4D 43 73 74
                                                                                                              61 72 74 6D 65
                                                                                                              61 73

Table 59: Example: sMN LMCstartmeas
         <STX>sMN{SPC}LMCstartmeas<ETX>
 CoLa    <STX>sMN LMCstartmeas<ETX>
  A      sMN LMCstartmeas
         02 73 4D 4E 20 4C 4D 43 73 74 61 72 74 6D 65 61 73 03
         02 02 02 02 00 00 00 10 73 4D 4E 20 4C 4D 43 73 74 61 72 74 6D 65 61 73 68
CoLa B 73 4D 4E 20 4C 4D 43 73 74 61 72 74 6D 65 61 73



Table 60: Telegram structure: sAN LMCstartmeas
                         Telegram structure: sAN LMCstartmeas


 Telegram           Description        Variable   Length         Additional details       Values CoLa A        Values CoLa B
    part                                                                                     (ASCII)              (Binary)
Command        Answer                 String      3                                       sAN                 73 41 4E
type
Command        Start measurement      String      12                                      LMCstartmeas        4C 4D 43 73 74
                                                                                                              61 72 74 6D 65
                                                                                                              61 73
Status         Accepted when value is Enum_8      1        Success:                       0                   00
code           0                                           Not allowed:                   1                   01

Table 61: Example: sAN LMCstartmeas

 CoLa    <STX>sAN{SPC}LMCstartmeas{SPC}0<ETX>
  A      02 73 41 4E 20 4C 4D 43 73 74 61 72 74 6D 65 61 73 20 30 03
CoLa B 02 02 02 02 00 00 00 12 73 41 4E 20 4C 4D 43 73 74 61 72 74 6D 65 61 73 20 00 44


12.5.1.4.3.4                 Stop measurement [sMN LMCstopmeas]
Shut off the laser and the motor is running at the set up frequency.
Table 62: Telegram structure: sMN LMCstopmeas
                         Telegram structure: sMN LMCstopmeas
                         (User level 'Authorized client' required)

 Telegram           Description        Variable   Length         Additional details       Values CoLa A        Values CoLa B
    part                                                                                     (ASCII)              (Binary)
Command        Method                 String      3                                       sMN                 73 4D 4E
type
Command        Stop measurement       String      11                                      LMCstopmeas         4C 4D 43 73 74
                                                                                                              6F 70 6D 65 61
                                                                                                              73




108      multiScan165                                                                               8028981/1X1R/2026-06-10 | SICK
                                                                                              SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

Table 63: Example: sMN LMCstopmeas
          <STX>sMN{SPC}LMCstopmeas<ETX>
 CoLa     <STX>sMN LMCstopmeas<ETX>
  A       sMN LMCstopmeas
          02 73 4D 4E 20 4C 4D 43 73 74 6F 70 6D 65 61 73 03
          02 02 02 02 00 00 00 0F 73 4D 4E 20 4C 4D 43 73 74 6F 70 6D 65 61 73 10
CoLa B 73 4D 4E 20 4C 4D 43 73 74 6F 70 6D 65 61 73



Table 64: Telegram structure: sAN LMCstopmeas
                            Telegram structure: sAN LMCstopmeas


 Telegram              Description        Variable   Length          Additional details      Values CoLa A      Values CoLa B
    part                                                                                        (ASCII)            (Binary)
Command        Answer                    String      3                                      sAN                73 41 4E
type
Command        Stop measurement          String      11                                     LMCstopmeas        4C 4D 43 73 74
                                                                                                               6F 70 6D 65 61
                                                                                                               73
Status         Accepted when value is Enum_8         1        No error:                     0                  00
code           0                                              Not allowed:                  1                  01

Table 65: Example: sAN LMCstopmeas

 CoLa     <STX>sAN{SPC}LMCstopmeas{SPC}0<ETX>
  A       02 73 41 4E 20 4C 4D 43 73 74 6F 70 6D 65 61 73 20 30 03
CoLa B 02 02 02 02 00 00 00 11 73 41 4E 20 4C 4D 43 73 74 6F 70 6D 65 61 73 20 00 3C


12.5.1.4.3.5                    Autostart measurement [sWN LMPautostartmeas]
This parameter defines whether the scanner will start to rotate directly and measure when powering up or remain
in idle mode. The changed setting (saved with the command sMN mEEWriteall, see "Save parameters perma-
nently [sMN mEEwriteall]", page 119) will be then be active with the next power-up cycle.
Table 66: Telegram structure: sWN LMPautostartmeas
                          Telegram structure: sWN LMPautostartmeas
                             (User level 'Authorized client' required)

 Telegram              Description        Variable   Length          Additional details      Values CoLa A      Values CoLa B
    part                                                                                        (ASCII)            (Binary)
Command        Write                     String      3                                      sWN                73 57 4E
type
Command        Autostart measurement String          16                                     LMPautostart-      4C 4D 50 61 75
                                                                                            meas               74 6F 73 74 61
                                                                                                               72 74 6D 65 61
                                                                                                               73
Status         Activate / Deactivate     Bool_1      1        Autostart off:                0                  00
code           Autostart                                      Autostart on:                 1                  01

Table 67: Example: sWN LMPautostartmeas 1
          <STX>sWN{SPC}LMPautostartmeas{SPC}1<ETX>
 CoLa     <STX>sWN LMPautostartmeas 1<ETX>
  A       sWN LMPautostartmeas 1
          02 73 57 4E 20 4C 4D 50 61 75 74 6F 73 74 61 72 74 6D 65 61 73 20 31 03
          02 02 02 02 00 00 00 16 73 57 4E 20 4C 4D 50 61 75 74 6F 73 74 61 72 74 6D 65 61 73 20 01 4F
CoLa B 73 57 4E 20 4C 4D 50 61 75 74 6F 73 74 61 72 74 6D 65 61 73 20 01




8028981/1X1R/2026-06-10 | SICK                                                                              multiScan165   109
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

Table 68: Telegram structure: sWA LMDautostartmeas
                          Telegram structure: sWA LMPautostartmeas


 Telegram           Description           Variable   Length         Additional details    Values CoLa A        Values CoLa B
    part                                                                                     (ASCII)              (Binary)
Command        Answer                     String     3                                    sWA                 73 57 41
type
Command        Autostart measurement String          16                                   LMPautostart-       4C 4D 50 61 75
                                                                                          meas                74 6F 73 74 61
                                                                                                              72 74 6D 65 61
                                                                                                              73

Table 69: Example: sWA LMPautostartmeas

 CoLa    <STX>sWA{SPC}LMPautostartmeas<ETX>
  A      02 73 57 41 20 4C 4D 43 73 74 61 72 74 6D 65 61 73 03
CoLa B 02 02 02 02 00 00 00 15 73 57 41 20 4C 4D 50 61 75 74 6F 73 74 61 72 74 6D 65 61 73 20 41


12.5.1.4.3.6                     Load factory defaults [sMN mSCloadfacdef]

NOTE
The Factory-Reset (Load factory defaults) deletes the entire parametrization of the device. All parameters, settings
and system applications will be set to default.

Table 70: Telegram structure: sMN mSCloadfacdef
                            Telegram structure: sMN mSCloadfacdef
                             (User level 'Authorized client' required)

 Telegram               Description        Variable Length          Additional details    Values CoLa A        Values CoLa B
    part                                                                                     (ASCII)              (Binary)
Command        Method                      String    3                                    sMN                 73 4D 4E
type
Command        Load factory defaults       String    13                                   mSCloadfacdef       6D 53 43 6C 6F
                                                                                                              61 64 66 61 63
                                                                                                              64 65 66

Table 71: Example: sMN mSCloadfacdef
         <STX>sMN{SPC}mSCloadfacdef<ETX>
 CoLa    <STX>sMN mSCloadfacdef<ETX>
  A      sMN mSCloadfacdef
         02 73 4D 4E 20 6D 53 43 6C 6F 61 64 66 61 63 64 65 66 03
         02 02 02 02 00 00 00 11 73 4D 4E 20 6D 53 43 6C 6F 61 64 66 61 63 64 65 66 28
CoLa B 73 4D 4E 20 6D 53 43 6C 6F 61 64 66 61 63 64 65 66



Table 72: Telegram structure: sAN mSCloadfacdef
                            Telegram structure: sAN mSCloadfacdef


 Telegram               Description        Variable Length          Additional details    Values CoLa A        Values CoLa B
    part                                                                                     (ASCII)              (Binary)
Command        Answer                      String    3                                    sAN                 73 41 4E
type
Command        Load factory defaults       String    13                                   mSCloadfacdef       6D 53 43 6C 6F
                                                                                                              61 64 66 61 63
                                                                                                              64 65 66




110      multiScan165                                                                               8028981/1X1R/2026-06-10 | SICK
                                                                                              SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

Table 73: Example: sAN mSCloadfacdef

 CoLa     <STX>sAN{SPC}mSCloadfacdef<ETX>
  A       02 73 4D 4E 20 6D 53 43 6C 6F 61 64 66 61 63 64 65 66 03
CoLa B 02 02 02 02 00 00 00 12 73 41 4E 20 6D 53 43 6C 6F 61 64 66 61 63 64 65 66 20 04


12.5.1.4.3.7                  Load application defaults [sMN mSCloadappdef]

NOTE
The Application-Reset (Load application defaults) deletes only the user parametrization of the Fields, Evaluation
cases (EVC) and parameters under the header “Application”. Other parameters like Interface settings, Echo Filter,
etc. remain unaffected.

Table 74: Telegram structure: sMN mSCloadappdef
                         Telegram structure: sMN mSCloadappdef
                          (User level 'Authorized client' required)

 Telegram           Description         Variable   Length        Additional details       Values CoLa A   Values CoLa B
    part                                                                                     (ASCII)         (Binary)
Command        Method                  String      3                                      sMN             73 4D 4E
type
Command        Load application        String      13                                     mSCloadappdef 6D 53 43 6C 6F
               defaults                                                                                 61 64 61 70 70
                                                                                                        64 65 66

Table 75: Example: sMN mSCloadappdef
          <STX>sMN{SPC}mSCloadappdef<ETX>
 CoLa     <STX>sMN mSCloadappdef<ETX>
  A       sMN mSCloadappdef
          02 73 4D 4E 20 6D 53 43 6C 6F 61 64 61 70 70 64 65 66 03
          02 02 02 02 00 00 00 11 73 4D 4E 20 6D 53 43 6C 6F 61 64 61 70 70 64 65 66 2D
CoLa B 73 4D 4E 20 6D 53 43 6C 6F 61 64 61 70 70 64 65 66



Table 76: Telegram structure: sAN mSCloadappdef
                         Telegram structure: sAN mSCloadappdef


 Telegram           Description         Variable   Length        Additional details       Values CoLa A   Values CoLa B
    part                                                                                     (ASCII)         (Binary)
Command        Answer                  String      3                                      sAN             73 41 4E
type
Command        Load application        String      13                                     mSCloadappdef 6D 53 43 6C 6F
               defaults                                                                                 61 64 61 70 70
                                                                                                        64 65 66

Table 77: Example: sAN mSCloadappdef

 CoLa     <STX>sAN{SPC}mSCloadappdef<ETX>
  A       02 73 41 4E 20 6D 53 43 6C 6F 61 64 61 70 70 64 65 66 03
CoLa B 02 02 02 02 00 00 00 12 73 41 4E 20 6D 53 43 6C 6F 61 64 61 70 70 64 65 66 20 01


12.5.1.4.3.8                  Change password [sMN SetPassword]
Changing the log in password for a specific user level.

NOTE
If logged in with a higher user level you may set the password for lower user levels as well.



8028981/1X1R/2026-06-10 | SICK                                                                        multiScan165   111
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

Table 78: Telegram structure: sMN SetPassword
                          Telegram structure: sMN SetPassword
                           (Same user level or higher required)

 Telegram           Description       Variable   Length           Additional details       Values CoLa A        Values CoLa B
    part                                                                                      (ASCII)              (Binary)
Command      Method                   String     3                                        sMN                  73 4D 4E
type
Command      Set password request     String     13                                       SetPassword          53 65 74 50 61
                                                                                                               73 73 77 6F 72
                                                                                                               64
User level   User level that the      Int_8      1        Maintenance:                    2                    02
             password will be                             Authorized client:              3                    03
             applied to                                   Service:                        4                    04
Password     Hash value of the new    Uint_32    4                                                    <Hash value>
             password

Set password for 'Authorized client' to “testtest” (hash value = 1920E4C9).
Table 79: Example: sMN SetPassword
         <STX>sMN{SPC}SetPassword{SPC}3{SPC}1920E4C9<ETX>
 CoLa    <STX>sMN SetPassword 3 1920E4C9<ETX>
  A      sMN SetPassword 3 1920E4C9
         02 73 4D 4E 20 53 65 74 50 61 73 73 77 6F 72 64 20 33 20 31 39 32 30 45 34 43 39 03
         02 02 02 02 00 00 00 15 73 4D 4E 20 53 65 74 50 61 73 73 77 6F 72 64 20 03 19 20 E4 C9 1A
CoLa B 73 4D 4E 20 53 65 74 50 61 73 73 77 6F 72 64 20 03 19 20 E4 C9


Calculating the hash value of the password
→     Login in SOPASair with user level “Service” to the device.
→     Select Diagnosis > Cybersecurity > Hash calculator.
→     For CoLa A/B take calculated hexadecimal hash value.
→
      Alternatively select     > Functions > Calculate password hash value




Table 80: Telegram structure: sAN SetPassword
                          Telegram structure: sAN SetPassword


 Telegram           Description       Variable   Length           Additional details       Values CoLa A        Values CoLa B
    part                                                                                      (ASCII)              (Binary)
Command      Answer                   String     3                                        sAN                  73 41 4E
type
Command      Set password             String     13                                       SetPassword          53 65 74 50 61
             requested                                                                                         73 73 77 6F 72
                                                                                                               64




112      multiScan165                                                                                8028981/1X1R/2026-06-10 | SICK
                                                                                               SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                           Telegram structure: sAN SetPassword


 Telegram            Description         Variable   Length         Additional details      Values CoLa A        Values CoLa B
    part                                                                                      (ASCII)              (Binary)
Success        Confirmation              Int_8      1        Failed:                       0                   00
                                                             Success:                      1                   01

Table 81: Example: sAN SetPassword

 CoLa     <STX>sAN{SPC}SetPassword{SPC}1<ETX>
  A       02 73 4D 4E 20 53 65 74 50 61 73 73 77 6F 72 64 20 31 03
CoLa B 02 02 02 02 00 00 00 11 73 41 4E 20 53 65 74 50 61 73 73 77 6F 72 64 20 01 00


12.5.1.4.3.9                    Check password [sMN CheckPassword]
Check the password for a specific user level, e.g. to verify if it has been changed correctly.
Table 82: Telegram structure: sMN CheckPassword
                          Telegram structure: sMN CheckPassword
                             (Same User level or higher required)

 Telegram            Description         Variable   Length         Additional details      Values CoLa A        Values CoLa B
    part                                                                                      (ASCII)              (Binary)
Command        Method                    String     3                                      sMN                 73 4D 4E
type
Command        Check password            String     13                                     CheckPassword 43 68 65 63 6B
               request                                                                                   50 61 73 73 77
                                                                                                         6F 72 64
User level     User level to check the   Int_8      1        Maintenance:                  2                   02
               password for                                  Authorized client:            3                   03
                                                             Service:                      4                   04
Password       Hash value of the pass-   Uint_32    4                                                 <Hash value>
               word to be checked

Check password “testtest” for 'Authorized client'.
Table 83: Example: sMN CheckPassword
          <STX>sMN{SPC}CheckPassword{SPC}3{SPC}1920E4C9<ETX>
 CoLa     <STX>sMN CheckPassword 3 1920E4C9<ETX>
  A       sMN CheckPassword 3 1920E4C9
          02 73 4D 4E 20 43 68 65 63 6B 50 61 73 73 77 6F 72 64 20 33 20 31 39 32 30 45 34 43 39 03
          02 02 02 02 00 00 00 17 73 4D 4E 20 43 68 65 63 6B 50 61 73 73 77 6F 72 64 20 03 19 20 E4 C9 1E
CoLa B 73 4D 4E 20 43 68 65 63 6B 50 61 73 73 77 6F 72 64 20 03 19 20 E4 C9



Table 84: Telegram structure: sAN CheckPassword
                          Telegram structure: sAN CheckPassword


 Telegram            Description         Variable   Length         Additional details      Values CoLa A        Values CoLa B
    part                                                                                      (ASCII)              (Binary)
Command        Answer                    String     3                                      sAN                 73 41 4E
type
Command        Check password            String     13                                     CheckPassword 43 68 65 63 6B
               request                                                                                   50 61 73 73 77
                                                                                                         6F 72 64
Success        Confirmation              Int_8      1        Failed:                       0                   00
                                                             Success:                      1                   01




8028981/1X1R/2026-06-10 | SICK                                                                              multiScan165   113
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

Table 85: Example: sAN CheckPassword

 CoLa      <STX>sAN{SPC}CheckPassword{SPC}1<ETX>
  A        02 73 41 4E 20 43 68 65 63 6B 50 61 73 73 77 6F 72 64 20 31 03
CoLa B 02 02 02 02 00 00 00 13 73 41 4E 20 43 68 65 63 6B 50 61 73 73 77 6F 72 64 20 01 04


12.5.1.4.3.10                      Set contamination indication settings [sWN ContaminationConfig]
Define the exact way how and when the device shall signal a potential contamination of the optics cover so that it
may be cleaned preventively (see "Contamination indication", page 36).
Table 86: Telegram structure: sWN ContaminationConfig
                          Telegram structure: sWN ContaminationConfig
                              (User level 'Authorized client' required)

 Telegram               Description        Variable   Length          Additional details         Values CoLa A        Values CoLa B
    part                                                                                            (ASCII)              (Binary)
Command         Write                      String     3                                          sWN                 73 57 4E
type
Command                                    String     19                                         Contamination-      43 6F 6E 74 61
                                                                                                 Config              6D 69 6E 61 74
                                                                                                                     69 6F 6E 43 6F
                                                                                                                     6E 66 69 67
Strategy        Strategy code              Enum_8     1        Inactive:                         0                   00
                                                               High available:                   1                   01
                                                               Sensitive:                        2                   02
Response        How fast (in seconds)      Uint_16    2        Value range 3 ... 60              +3d … +60d          00 03 … 00 3C
time            the sensor reacts after                        Default: 3                        (03h … 3Ch)
                a contamination
Threshold       Sensitivity                Enum_8     1        High:                             0                   00
warning                                                        Medium:                           1                   01
                                                               Low:                              2                   02
Cover           Selection of either cus-   Enum_8     1        No weather protection hood:       0                   00
                tom sectors or used                            Weather protection hood cus-
                wheather protection                            tom sectors:                      255d (FFh)          FF
                hood
Custom          Selection of sectors       Array      12       Active: 1                         1                   01
sectors                                                        Inactive: 0                       1                   01
                                                               Default value of all sectors is   1                   01
                                                               active                            1                   01
                                                                                                 1                   01
                                                                                                 1                   01
                                                                                                 1                   01
                                                                                                 1                   01
                                                                                                 1                   01
                                                                                                 1                   01
                                                                                                 1                   01
                                                                                                 1                   01
Enable          Warning monitoring         Bool_1     1        Off (False):                      0                   00
Warning                                                        On (True):                        1                   01
Enable          Error monitoring           Bool_1     1        Off (False):                      0                   00
Error                                                          On (True):                        1                   01

Table 87: Example: sWN ContaminationConfig strategy inactive, response time 3 sec, sensitivity high, Weather protection hood
custom sectors, sector 1-12, enable warning, enable error
           <STX>sWN{SPC}ContaminationConfig{SPC}0{SPC}3{SPC}0{SPC}FF{SPC}1{SPC}1{SPC}1{SPC}1{SPC}1{SPC}1{SPC}1{SP
 CoLa      C}1{SPC}1{SPC}1{SPC}1{SPC}1{SPC}1{SPC}1<ETX>
  A        02 73 57 4E 20 43 6F 6E 74 61 6D 69 6E 61 74 69 6F 6E 43 6F 6E 66 69 67 20 30 20 33 20 30 20 46 46 20 31 20 31 20 31
           20 31 20 31 20 31 20 31 20 31 20 31 20 31 20 31 20 31 20 31 20 31 03




114        multiScan165                                                                                    8028981/1X1R/2026-06-10 | SICK
                                                                                                     SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

          02 02 02 02 00 00 00 2B 73 57 4E 20 43 6F 6E 74 61 6D 69 6E 61 74 69 6F 6E 43 6F 6E 66 69 67 20 00 00 03 00 FF 01
CoLa B
          01 01 01 01 01 01 01 01 01 01 01 01 01 FC

Table 88: Telegram structure: sWA ContaminationConfig
                         Telegram structure: sWA ContaminationConfig


 Telegram              Description       Variable   Length        Additional details        Values CoLa A       Values CoLa B
    part                                                                                       (ASCII)             (Binary)
Command         Answer                  String      3                                      sWA                 73 57 41
type
Command                                 String      19                                     Contamination-      43 6F 6E 74 61
                                                                                           Config              6D 69 6E 61 74
                                                                                                               69 6F 6E 43 6F
                                                                                                               6E 66 69 67

Table 89: Example: sWA ContaminationConfig

 CoLa     <STX>sWA{SPC}ContaminationConfig<ETX>
  A       02 73 57 41 20 43 6F 6E 74 61 6D 69 6E 61 74 69 6F 6E 43 6F 6E 66 69 67 03
CoLa B 02 02 02 02 00 00 00 18 73 57 41 20 43 6F 6E 74 61 6D 69 6E 61 74 69 6F 6E 43 6F 6E 66 69 67 20


12.5.1.4.3.11                   Read contamination indication settings [sRN ContaminationConfig]
Reads the current contamination settings that define how and under which conditions the device indicates a
potential contamination of the optics cover to enable preventive cleaning.
Table 90: Telegram structure: sRN ContaminationConfig
                         Telegram structure: sRN ContaminationConfig


 Telegram              Description       Variable   Length        Additional details        Values CoLa A       Values CoLa B
    part                                                                                       (ASCII)             (Binary)
Command         Read                    String      3                                      sRN                 73 52 4E
type
Command                                 String      19                                     Contamination-      43 6F 6E 74 61
                                                                                           Config              6D 69 6E 61 74
                                                                                                               69 6F 6E 43 6F
                                                                                                               6E 66 69 67

Table 91: Example: sRN ContaminationConfig
          <STX>sRN{SPC}ContaminationConfig<ETX>
 CoLa     <STX>sRN ContaminationConfig<ETX>
  A       sRN ContaminationConfig
          02 73 52 4E 20 43 6F 6E 74 61 6D 69 6E 61 74 69 6F 6E 43 6F 6E 66 69 67 03
          02 02 02 02 00 00 00 17 73 52 4E 20 43 6F 6E 74 61 6D 69 6E 61 74 69 6F 6E 43 6F 6E 66 69 67 25
CoLa B 73 52 4E 20 43 6F 6E 74 61 6D 69 6E 61 74 69 6F 6E 43 6F 6E 66 69 67 25



Table 92: Telegram structure: sRA ContaminationConfig
                         Telegram structure: sRA ContaminationConfig


 Telegram              Description       Variable   Length        Additional details        Values CoLa A       Values CoLa B
    part                                                                                       (ASCII)             (Binary)
Command         Answer                  String      3                                      sRA                 73 52 41
type




8028981/1X1R/2026-06-10 | SICK                                                                              multiScan165   115
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                          Telegram structure: sRA ContaminationConfig


 Telegram              Description         Variable   Length          Additional details         Values CoLa A         Values CoLa B
    part                                                                                            (ASCII)               (Binary)
Command                                    String     19                                         Contamination-       43 6F 6E 74 61
                                                                                                 Config               6D 69 6E 61 74
                                                                                                                      69 6F 6E 43 6F
                                                                                                                      6E 66 69 67
Strategy        Strategy code              Enum_8     1        Inactive:                         0                    00
                                                               High available:                   1                    01
                                                               Sensitive:                        2                    02
Response        How fast (in seconds)      Uint_16    2        Value range 3 ... 60              03h … 3Ch            00 03 … 00 3C
time            the sensor reacts after                        Default: 3
                a contamination
Threshold       Sensitivity                Enum_8     1        High:                             0                    00
warning                                                        Medium:                           1                    01
                                                               Low:                              2                    02
Cover           Selection of either cus-   Enum_8     1        No weather protection hood:       0                    00
                tom sectors or used                            Weather protection hood cus-
                wheather protection                            tom sectors:                      FF                   FF
                hood
Custom          Selection of sectors       Array      12       Active: 1                         1                    01
sectors                                                        Inactive: 0                       1                    01
                                                               Default value of all sectors is   1                    01
                                                               active                            1                    01
                                                                                                 1                    01
                                                                                                 1                    01
                                                                                                 1                    01
                                                                                                 1                    01
                                                                                                 1                    01
                                                                                                 1                    01
Enable          Warning monitoring         Bool_1     1        Off (False):                      0                    00
Warning                                                        On (True):                        1                    01
Enable          Error monitoring           Bool_1     1        Off (False):                      0                    00
Error                                                          On (True):                        1                    01

Table 93: Example: sRA ContaminationConfig strategy inactive, response time 3 sec, sensitivity high, Weather protection hood
custom sectors, sector 1-12, enable warning, enable error
           <STX>sRA{SPC}ContaminationCon-
           fig{SPC}0{SPC}3{SPC}0{SPC}FF{SPC}1{SPC}1{SPC}1{SPC}1{SPC}1{SPC}1{SPC}1{SPC}1{SPC}1{SPC}1{SPC}1{SPC}1{SPC}1{
 CoLa      SPC}1<ETX>
  A
           02 73 52 41 20 43 6F 6E 74 61 6D 69 6E 61 74 69 6F 6E 43 6F 6E 66 69 67 20 30 20 33 20 30 20 46 46 20 31 20 31 20 31
           20 31 20 31 20 31 20 31 20 31 20 31 20 31 20 31 20 31 20 31 20 31 03
           02 02 02 02 00 00 00 2B 73 52 41 20 43 6F 6E 74 61 6D 69 6E 61 74 69 6F 6E 43 6F 6E 66 69 67 20 00 00 03 00 FF 01
CoLa B
           01 01 01 01 01 01 01 01 01 01 01 01 01 F6


12.5.1.4.3.12                      Send contamination indication data permanently [sEN ContaminationData]
Provides continuous contamination indication data for the individual sectors of the optical cover. When a change in
contamination is detected in any sector, the current contamination status of all sectors will be transmitted
Table 94: Telegram structure: sEN ContaminationData
                          Telegram structure: sEN ContaminationData


 Telegram              Description         Variable   Length          Additional details         Values CoLa A         Values CoLa B
    part                                                                                            (ASCII)               (Binary)
Command         Read                       String     3                                          sEN                  73 45 4E
type



116        multiScan165                                                                                     8028981/1X1R/2026-06-10 | SICK
                                                                                                      SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                       Telegram structure: sEN ContaminationData


 Telegram           Description         Variable   Length            Additional details      Values CoLa A      Values CoLa B
    part                                                                                        (ASCII)            (Binary)
Command      Get the contamination     String      17                                       Contamination-     43 6F 6E 74 61
             indication data conti-                                                         Data               6D 69 6E 61 74
             nously                                                                                            69 6F 6E 44 61
                                                                                                               74 61
Data         Start/ Stop               Bool_1      1        Stop:                           0                  00
                                                            Start:                          1                  01

Table 95: Example: sEN ContaminationData
          <STX>sEN{SPC}ContaminationData{SPC}1<ETX>
 CoLa     <STX>sEN ContaminationData 1<ETX>
  A       sEN ContaminationData 1
          02 73 45 4E 20 43 6F 6E 74 61 6D 69 6E 61 74 69 6F 6E 44 61 74 61 20 31 03
          02 02 02 02 00 00 00 17 73 45 4E 20 43 6F 6E 74 61 6D 69 6E 61 74 69 6F 6E 44 61 74 61 20 01 09
CoLa B 73 45 4E 20 43 6F 6E 74 61 6D 69 6E 61 74 69 6F 6E 44 61 74 61 20 01



Table 96: Telegram structure: sSN ContaminationData
                       Telegram structure: sSN ContaminationData


 Telegram           Description         Variable   Length            Additional details      Values CoLa A      Values CoLa B
    part                                                                                        (ASCII)            (Binary)
Command      Answer                    String      3                                        sSN                73 53 4E
type
Command      Get the contamination     String      17                                       Contamination-     43 6F 6E 74 61
             indication data conti-                                                         Data               6D 69 6E 61 74
             nously                                                                                            69 6F 6E 44 61
                                                                                                               74 61
Contami-    Status of contamination Array of       12       Deactivated:                    0                  00
nation data in order of the different Enum_8                Clean:                          1                  01
            sectors                                         Warning:                        2                  02
                                                            Error:                          3                  03




Table 97: Example: sSN ContaminationData
          <STX>sSN{SPC}ContaminationData{SPC}0{SPC}3{SPC}2{SPC}2{SPC}2{SPC}2{SPC}2{SPC}2{SPC}2{SPC}2{SPC}2{SP
 CoLa     C}2<ETX>
  A       02 73 53 4E 20 43 6F 6E 74 61 6D 69 6E 61 74 69 6F 6E 44 61 74 61 20 30 20 33 20 32 20 32 20 32 20 32 20 3220 32 20
          3220 3220 3220 32 03
          02 02 02 02 00 00 00 22 73 53 4E 20 43 6F 6E 74 61 6D 69 6E 61 74 69 6F 6E 44 61 74 61 20 00 03 02 02 02 02 02 02
CoLa B
          02 02 02 02 1D




8028981/1X1R/2026-06-10 | SICK                                                                              multiScan165    117
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

12.5.1.4.3.13                   Read contamination indication result [sRN ContaminationResult]
This telegram is intended to read the contamination result. The telegram returns two Boolean. One for warning and
one for error. Depending on the strategy of the contamination indication the state changes if one or all sectors are
in the specific status (warning or error).
Table 98: Telegram structure: sRN ContaminationResult
                         Telegram structure: sRN ContaminationResult


 Telegram              Description      Variable   Length          Additional details       Values CoLa A          Values CoLa B
    part                                                                                       (ASCII)                (Binary)
Command         Read                    String     3                                        sRN                   73 52 4E
type
Command                                 String     19                                       Contamination-        43 6F 6E 74 61
                                                                                            Result                6D 69 6E 61 74
                                                                                                                  69 6F 6E 52 65
                                                                                                                  73 75 6C 74

Table 99: Example: sRN ContaminationResult
         <STX>sRN{SPC}ContaminationResult<ETX>
 CoLa    <STX>sRN ContaminationResult<ETX>
  A      sRN ContaminationResult
         02 73 52 4E 20 43 6F 6E 74 61 6D 69 6E 61 74 69 6F 6E 52 65 73 75 6C 74 03
         02 02 02 02 00 00 00 17 73 52 4E 20 43 6F 6E 74 61 6D 69 6E 61 74 69 6F 6E 52 65 73 75 6C 74 26
CoLa B 73 52 4E 20 43 6F 6E 74 61 6D 69 6E 61 74 69 6F 6E 52 65 73 75 6C 74



Table 100: Telegram structure: sRA ContaminationResult
                         Telegram structure: sRA ContaminationResult


 Telegram              Description      Variable   Length          Additional details       Values CoLa A          Values CoLa B
    part                                                                                       (ASCII)                (Binary)
Command         Answer                  String     3                                        sRA                   73 52 41
type
Command                                 String     19                                       Contamination-        43 6F 6E 74 61
                                                                                            Result                6D 69 6E 61 74
                                                                                                                  69 6F 6E 52 65
                                                                                                                  73 75 6C 74
Contami-        Result of contamination Enum_8     1        Warning
nation          indication                                  Inactive:                       0                     00
Result          (Order of results:                          Active:                         1                     01
                Warning / Error)
                                                            Error
                                                            Inactive:                       0                     00
                                                            Active:                         1                     01

Table 101: Example: sRA ContaminationResult warning active error inactive

 CoLa    <STX>sRA{SPC}ContaminationResult{SPC}1{SPC}0<ETX>
  A      02 73 52 41 20 43 6F 6E 74 61 6D 69 6E 61 74 69 6F 6E 52 65 73 75 6C 74 20 31 20 30 03
CoLa B 02 02 02 02 00 00 00 1A 73 52 41 20 43 6F 6E 74 61 6D 69 6E 61 74 69 6F 6E 52 65 73 75 6C 74 20 01 00 08


12.5.1.4.3.14                   Send contamination indication result permanently [sEN ContaminationResult]
This telegram is intended to activate the event for read the contamination result permanently. The telegram returns
two Boolean. One for warning and one for error. Depending on the strategy of the contamination indication the
state changes if one or all sectors are in the specific status (warning or error).




118      multiScan165                                                                                   8028981/1X1R/2026-06-10 | SICK
                                                                                                  SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

Table 102: Telegram structure: sEN ContaminationResult
                         Telegram structure: sEN ContaminationResult


 Telegram              Description          Variable   Length            Additional details   Values CoLa A    Values CoLa B
    part                                                                                         (ASCII)          (Binary)
Command         Read                       String      3                                      sEN              73 52 4E
type
Command                                    String      19                                     Contamination-   43 6F 6E 74 61
                                                                                              Result           6D 69 6E 61 74
                                                                                                               69 6F 6E 52 65
                                                                                                               73 75 6C 74
Data            Start/ Stop                Bool_1      1        Stop:                         0                00
                                                                Start:                        1                01

Table 103: Example: sEN ContaminationResult
          <STX>sEN{SPC}ContaminationResult{SPC}1<ETX>
 CoLa     <STX>sEN ContaminationResult 1<ETX>
  A       sEN ContaminationResult 1
          02 73 45 4E 20 43 6F 6E 74 61 6D 69 6E 61 74 69 6F 6E 52 65 73 75 6C 74 20 31 03
          02 02 02 02 00 00 00 19 73 45 4E 20 43 6F 6E 74 61 6D 69 6E 61 74 69 6F 6E 52 65 73 75 6C 74 20 01 10
CoLa B 73 45 4E 20 43 6F 6E 74 61 6D 69 6E 61 74 69 6F 6E 52 65 73 75 6C 74 20 01



Table 104: Telegram structure: sSN ContaminationResult
                         Telegram structure: sSN ContaminationResult


 Telegram              Description          Variable   Length            Additional details   Values CoLa A    Values CoLa B
    part                                                                                         (ASCII)          (Binary)
Command         Answer                     String      3                                      sSN              73 53 4E
type
Contami-        Result of contamination Enum_8         1        Warning
nation          indication                                      Inactive:                     0                00
Result          (Order of results:                              Active:                       1                01
                Warning / Error)
                                                                Error
                                                                Inactive:                     0                00
                                                                Active:                       1                01

Table 105: Example: sSN ContaminationResult warning active error inactive

 CoLa     <STX>sRA{SPC}ContaminationResult{SPC}1{SPC}0<ETX>
  A       02 73 52 41 20 43 6F 6E 74 61 6D 69 6E 61 74 69 6F 6E 52 65 73 75 6C 74 20 31 20 30 03
CoLa B 02 02 02 02 00 00 00 1A 73 52 41 20 43 6F 6E 74 61 6D 69 6E 61 74 69 6F 6E 52 65 73 75 6C 74 20 01 00 08


12.5.1.4.3.15                     Save parameters permanently [sMN mEEwriteall]
Save all parameter changes of the device. Must be sent before loging off and/ or hardware rebooting of the device.
Else all changes will be lost.
Table 106: Telegram structure: sMN mEEwriteall
                               Telegram structure: sMN mEEwriteall
                              (User level 'Authorized client' required)

 Telegram              Description          Variable   Length            Additional details   Values CoLa A    Values CoLa B
    part                                                                                         (ASCII)          (Binary)
Command         Method                     String      3                                      sMN              73 4D 4E
type




8028981/1X1R/2026-06-10 | SICK                                                                             multiScan165    119
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                             Telegram structure: sMN mEEwriteall
                            (User level 'Authorized client' required)

 Telegram             Description          Variable   Length        Additional details   Values CoLa A          Values CoLa B
    part                                                                                    (ASCII)                (Binary)
Command         Store parameters per-     String      11                                 mEEwriteall           6D 45 45 77 72
                manently                                                                                       69 74 65 61 6C
                                                                                                               6C

Table 107: Example: sMN mEEwriteall
         <STX>sMN{SPC}mEEwriteall<ETX>
 CoLa    <STX>sMN mEEwriteall<ETX>
  A      sMN mEEwriteall
         02 73 4D 4E 20 6D 45 45 77 72 69 74 65 61 6C 6C 03
         02 02 02 02 00 00 00 0F 73 4D 4E 20 6D 45 45 77 72 69 74 65 61 6C 6C 21
CoLa B 73 4D 4E 20 6D 45 45 77 72 69 74 65 61 6C 6C



Table 108: Telegram structure: sAN mEEwriteall
                             Telegram structure: sAN mEEwriteall


 Telegram             Description          Variable   Length        Additional details   Values CoLa A          Values CoLa B
    part                                                                                    (ASCII)                (Binary)
Command         Answer                    String      3                                  sAN                   73 41 4E
type
Command         Store parameters per-     String      11                                 mEEwriteall           6D 45 45 77 72
                manently                                                                                       69 74 65 61 6C
                                                                                                               6C
Status          Accepted when value is Bool_1         1        Error:                    0                     00
code            1                                              Success:                  1                     01

Table 109: Example: sAN mEEwriteall

 CoLa    <STX>sAN{SPC}mEEwriteall{SPC}1<ETX>
  A      02 73 41 4E 20 6D 45 45 77 72 69 74 65 61 6C 6C 20 31 03
CoLa B 02 02 02 02 00 00 00 11 73 41 4E 20 6D 45 45 77 72 69 74 65 61 6C 6C 20 01 0C


12.5.1.4.3.16                      Set to run [sMN Run]
Log out from device and activate all parameter changes.
Table 110: Telegram structure: sMN Run
                                   Telegram structure: sMN Run


 Telegram             Description          Variable   Length        Additional details   Values CoLa A          Values CoLa B
    part                                                                                    (ASCII)                (Binary)
Command         Method                    String      3                                  sMN                   73 4D 4E
type
Command         Start the device          String      3                                  Run                   52 75 6E

Table 111: Example: sMN Run
         <STX>sMN{SPC}Run<ETX>
 CoLa    <STX>sMN Run<ETX>
  A      sMN Run
         02 73 4D 4E 20 52 75 6E 03




120      multiScan165                                                                                8028981/1X1R/2026-06-10 | SICK
                                                                                               SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

          02 02 02 02 00 00 00 07 73 4D 4E 20 52 75 6E 19
CoLa B 73 4D 4E 20 52 75 6E



Table 112: Telegram structure: sAN Run
                                   Telegram structure: sAN Run


 Telegram             Description         Variable   Length         Additional details   Values CoLa A   Values CoLa B
    part                                                                                    (ASCII)         (Binary)
Command         Answer                    String     3                                   sAN             73 41 4E
type
Command         Start the device          String     3                                   Run             52 75 6E
Status          Accepted when value is Bool_1        1        Error:                     0               00
code            1                                             Success:                   1               01

Table 113: Example: sAN Run

 CoLa     <STX>sAN{SPC}Run{SPC}1<ETX>
  A       02 73 41 4E 20 52 75 6E 20 31 03
CoLa B 02 02 02 02 00 00 00 09 73 41 4E 20 52 75 6E 20 01 34


12.5.1.4.3.17                      Reboot device [sMN mSCreboot]
This command includes saving all parameters.
Table 114: Telegram structure: sMN mSCreboot
                             Telegram structure: sMN mSCreboot
                            (User level 'Authorized client' required)

 Telegram             Description          Variable Length          Additional details   Values CoLa A   Values CoLa B
    part                                                                                    (ASCII)         (Binary)
Command         Method                     String    3                                   sMN             73 4D 4E
type
Command         Reboot device              String    9                                   mSCreboot       6D 53 43 72 65
                                                                                                         62 6F 6F 74

Table 115: Example: sMN mSCreboot
          <STX>sMN{SPC}mSCreboot<ETX>
 CoLa     <STX>sMN mSCreboot<ETX>
  A       sMN mSCreboot
          02 73 4D 4E 20 6D 53 43 72 65 62 6F 6F 74 03
          02 02 02 02 00 00 00 0D 73 4D 4E 20 6D 53 43 72 65 62 6F 6F 74 2C
CoLa B 73 4D 4E 20 6D 53 43 72 65 62 6F 6F 74



Table 116: Telegram structure: sAN mSCreboot
                             Telegram structure: sAN mSCreboot


 Telegram             Description         Variable   Length         Additional details   Values CoLa A   Values CoLa B
    part                                                                                    (ASCII)         (Binary)
Command         Answer                    String     3                                   sAN             73 41 4E
type
Command         Reboot device             String     9                                   mSCreboot       6D 53 43 72 65
                                                                                                         62 6F 6F 74




8028981/1X1R/2026-06-10 | SICK                                                                       multiScan165    121
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

Table 117: Example: sAN mSCreboot

     CoLa   <STX>sAN{SPC}mSCreboot<ETX>
      A     02 73 41 4E 20 6D 53 43 72 65 62 6F 6F 74 03
 CoLa B 02 02 02 02 00 00 00 0E 73 41 4E 20 6D 53 43 72 65 62 6F 6F 74 20 00


12.5.1.4.4                  Measurement output telegram


12.5.1.4.4.1                        Configure aperture angle of the scandata for output [sWN LMPoutputRange]
Select start and stop angle of the measurement data output. In general only one output range can be be config-
ured.

NOTE
Verify the definition of the angle positions for your product.

Table 118: Telegram structure: sWN LMPoutputRange
                             Telegram structure: sWN LMPoutputRange
                               (User level 'Authorized client' required)

     Telegram            Description            Variable    Length               Additional Details             Values CoLa A      Values CoLa B
        part                                                                                                       (ASCII)            (Binary)
 Command         Write                         String       3                                               sWN                    73 57 4E
 type
 Command         Change output angle           String       14                                              LMPoutputRange 4C 4D 50 6F
                 range                                                                                                     75 74 70 75 74
                                                                                                                           52 61 6E 67 65
 Reserved        -                             Int_16       2          Always:                              1                      00 01
 Angular         [1/10000°]                    Uint_32      4          0.125°:                              +1250d (4E2h)          00 00 04 E2
 resolu-         Fixed value, not
 tion 1)         changeable
 Start angle [1/10000°]                        Int_32       4          -180° ... +180°:                     -1800000d              FF E4 88 C0 …
                                                                                                            (FFE488C0h)            00 1B 77 40
                                                                                                            … +1800000d
                                                                                                            (1B7740h)
 Stop angle [1/10000°]                         Int_32       4          -180° ... +180°                      -1800000d              FF E4 88 C0 …
                                                                                                            (FFE488C0h)            00 1B 77 40
                                                                                                            … +1800000d
                                                                                                            (1B7740h)

1)    Angular resolution can not be changed here, it is taken automatically from the basic scan settings!

Table 119: Example: sWN LMPoutputRange - set output data for angular resolution at 0.125° and range from -90° to +90°
            <STX>sWN{SPC}LMPoutputRange{SPC}1{SPC}+1250{SPC}-900000{SPC}+900000<ETX>
            <STX>sWN LMPoutputRange 1 +1250 -900000 +900000<ETX>
     CoLa
      A     sWN LMPoutputRange 1 +1250 -900000 +900000
            02 73 57 4E 20 4C 4D 50 6F 75 74 70 75 74 52 61 6E 67 65 20 31 20 2B 31 32 35 30 20 2D 39 30 30 30 30 30 20
            2B 39 30 30 30 30 30 03
            02 02 02 02 00 00 00 21 73 57 4E 20 4C 4D 50 6F 75 74 70 75 74 52 61 6E 67 65 20 00 01 00 00 04 E2 FF F2 44 60 00
            0D BB A0 A3
 CoLa B
            73 57 4E 20 4C 4D 50 6F 75 74 70 75 74 52 61 6E 67 65 20 00 01 00 00 04 E2 FF F2 44 60 00 0D BB A0




122          multiScan165                                                                                               8028981/1X1R/2026-06-10 | SICK
                                                                                                                  SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

Table 120: Telegram structure: sWA LMPoutputRange
                         Telegram structure: sWA LMPoutputRange


 Telegram             Description         Variable Length             Additional details     Values CoLa A     Values CoLa B
    part                                                                                        (ASCII)           (Binary)
Command        Answer                     String    3                                        sWA              73 57 41
type
Command        Change output angle        String    14                                       LMPoutpu-        4C 4D 50 6F 75
               range                                                                         tRange           74 70 75 74 52
                                                                                                              61 6E 67 65

Table 121: Example: sWA LMPoutputRange

 CoLa     <STX>sWA{SPC}LMPoutputRange<ETX>
  A       02 73 57 41 20 4C 4D 50 6F 75 74 70 75 74 52 61 6E 67 65 03
CoLa B 02 02 02 02 00 00 00 13 73 57 41 20 4C 4D 50 6F 75 74 70 75 74 52 61 6E 67 65 20 74


12.5.1.4.4.2                     Read for actual output range [sRN LMPoutputRange]
Read the defined angular resolution and current aperture angle for data output.
Table 122: Telegram structure: sRN LMPoutputRange
                            Telegram structure: sRN LMPoutputRange


 Telegram             Description         Variable Length             Additional details     Values CoLa A     Values CoLa B
    part                                                                                        (ASCII)           (Binary)
Command        Read                       String    3                                        sRN              73 52 4E
type
Command        Output range               String    14                                       LMPoutpu-        4C 4D 50 6F 75
                                                                                             tRange           74 70 75 74 52
                                                                                                              61 6E 67 65

Table 123: Example: sRN LMPoutputRange
          <STX>sRN{SPC}LMPoutputRange<ETX>
 CoLa     <STX>sRN LMPoutputRange<ETX>
  A       sRN LMPoutputRange
          02 73 52 4E 20 4C 4D 50 6F 75 74 70 75 74 52 61 6E 67 65 03
          02 02 02 02 00 00 00 12 73 52 4E 20 4C 4D 50 6F 75 74 70 75 74 52 61 6E 67 65 5E
CoLa B 73 52 4E 20 4C 4D 50 6F 75 74 70 75 74 52 61 6E 67 65


Table 124: Telegram structure: sRA LMPoutputRange
                            Telegram structure: sRA LMPoutputRange


 Telegram             Description         Variable Length             Additional details     Values CoLa A     Values CoLa B
    part                                                                                        (ASCII)           (Binary)
Command        Answer                     String    3                                        sRA              73 52 41
type
Command        Output range               String    14                                       LMPoutpu-        4C 4D 50 6F 75
                                                                                             tRange           74 70 75 74 52
                                                                                                              61 6E 67 65
Reserved                                  Int_16    2       Always:                          1h               00 01
Angular        [1/10000°]                 Uint_32   4       0.125°:                          4E2h             00 00 04 E2
resolution
Start angle [1/10000°]                    Int_32    4       -180° ... +180°                  FFE488C0h …      FF E4 88 C0 …
                                                                                             1B7740h          00 1B 77 40




8028981/1X1R/2026-06-10 | SICK                                                                             multiScan165     123
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                           Telegram structure: sRA LMPoutputRange


 Telegram               Description       Variable Length            Additional details      Values CoLa A      Values CoLa B
    part                                                                                        (ASCII)            (Binary)
Stop angle [1/10000°]                     Int_32     4        -180° ... +180°             FFE488C0h …          FF E4 88 C0 …
                                                                                          1B7740h              00 1B 77 40

Table 125: Example: sRA LMPoutputRange – device output set at 0.125° angular resolution and range from -90° to +90°
         <STX>sRA{SPC}LMPoutputRange{SPC}1{SPC}4E2{SPC}FFF24460{SPC}DBBA0<ETX>
 CoLa
  A      02 73 52 41 20 4C 4D 50 6F 75 74 70 75 74 52 61 6E 67 65 20 31 20 34 45 32 20 46 46 46 32 34 34 36 30 20 44 42 42
         41 30 03
         02 02 02 02 00 00 00 21 73 52 41 20 4C 4D 50 6F 75 74 70 75 74 52 61 6E 67 65 20 00 01 00 00 04 E2 FF F2 44 60 00
CoLa B
         0D BB A0 A9


12.5.1.4.4.3                     Set scan data enable [sWN ScanDataEnable]
Enables/ Disables streaming data output
Table 126: Telegram structure: sWN ScanDataEnable
                           Telegram structure: sWN ScanDataEnable
                            (User level 'Authorized client' required)

 Telegram              Description        Variable   Length          Additional details      Values CoLa A      Values CoLa B
    part                                                                                        (ASCII)            (Binary)
Command        Write                     String      3                                    sWN                  73 57 E4
type
Command        Enables/ Disables         String      14                                   ScanDataEna-         53 63 61 6E 44
               streaming data output.                                                     ble                  61 74 61 45 6E 61
                                                                                                               62 6C 65
Data                                     Bool        1        Off:                        0d (00h)             00 ... 01
                                                              On:                         +1d (01h)

Table 127: Example: sWN ScanDataEnable 0 - Disable the streaming data output
         <STX>sWN{SPC}ScanDataEnable{SPC}0<ETX>
 CoLa    <STX>sWN ScanDataEnable 0<ETX>
  A      sWN ScanDataEnable 0
         02 73 57 4E 20 53 63 61 6E 44 61 74 61 45 6E 61 62 6C 65 20 30 03
         02 02 02 02 00 00 00 14 73 57 4E 20 53 63 61 6E 44 61 74 61 45 6E 61 62 6C 65 20 00 44
CoLa B 73 57 4E 20 53 63 61 6E 44 61 74 61 45 6E 61 62 6C 65 20 00


Table 128: Telegram structure: sWA ScanDataEnable
                           Telegram structure: sWA ScanDataEnable
                            (Required User Level authorized clinet)

 Telegram              Description        Variable   Length          Additional details      Values CoLa A      Values CoLa B
    part                                                                                        (ASCII)            (Binary)
Command        Answer                    String      3                                    sWA                  73 57 41
type
Command        Enables/ Disables         String      14                                   ScanDataEna-         53 63 61 6E 44
               streaming data output.                                                     ble                  61 74 61 45 6E 61
                                                                                                               62 6C 65

Table 129: Example: sWA ScanDataEnable

 CoLa    <STX>sWA{SPC}ScanDataEnable<ETX>
  A      02 73 57 41 20 53 63 61 6E 44 61 74 61 45 6E 61 62 6C 65 03
CoLa B 02 02 02 02 00 00 00 13 73 57 41 20 53 63 61 6E 44 61 74 61 45 6E 61 62 6C 65 20 4B




124      multiScan165                                                                                8028981/1X1R/2026-06-10 | SICK
                                                                                               SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

12.5.1.4.4.4                    Set streaming ethernet settings [sWN ScanDataEthSettings]
Ethernet settings for the scan data streaming functionality of the device
Table 130: Telegram structure: sWN ScanDataEthSettings
                        Telegram structure: sWN ScanDataEthSettings
                            (User level 'Authorized client' required)

 Telegram              Description        Variable   Length          Additional details       Values CoLa A      Values CoLa B
    part                                                                                         (ASCII)            (Binary)
Command        Write                      String     3                                       sWN                73 57 4E
type
Command        String                     String     19                                      ScanDataEth-       53 63 61 6E 44
                                                                                             Settings           61 74 61 45 74 68
                                                                                                                53 65 74 74 69
                                                                                                                6E 67 73
Protocol       Transport protocol for     Enum_8     1        UDP:                           +1d (01h)          01
               streaming data                                 TCP:                           +2d (02h)          02
IPAddress      IP address of the desti-   Array      4                                       0 …+255d (00…      00 … FF
               nation for data receiver                                                      FF)
                                                                                             0 …+255d           00 … FF
                                                                                             (00..FF)
                                                                                             0 …+255d (00…      00 … FF
                                                                                             FF)
                                                                                             0 …+255d (00…      00 … FF
                                                                                             FF)
Port           Port destination of the    Uint_16    2                                       0 .. +65535d(00 00 00 … FF FF
               data reseiver                                                                 00…FF FF)

Example: sWN ScanDataEthSettings +1 +192 +168 +0 +100 +2115
Protocol is set to UDP (1), IPAddress (192.168.0.100), Port (2115)
Table 131: Example: sWN ScanDataEthSettings
           <STX>sWN{SPC}ScanDataEthSettings{SPC}+1{SPC}+192{SPC}+168{SPC}+0{SPC}+100{SPC}+2115<ETX>
           <STX>sWN ScanDataEthSettings +1 +192 +168 +0 +100 +2115<ETX>
 CoLa
  A        sWN ScanDataEthSettings +1 +192 +168 +0 +100 +2115
           02 73 57 4E 20 53 63 61 6E 44 61 74 61 45 74 68 53 65 74 74 69 6E 67 73 20 31 20 43 30 20 41 38 20 30 20 36 34
           20 38 34 33 03
           02 02 02 02 00 00 00 1F 73 57 4E 20 53 63 61 6E 44 61 74 61 45 74 68 53 65 74 74 69 6E 67 73 20 01 C0 A8 00 64 08
           43 5F
CoLa B
           73 57 4E 20 53 63 61 6E 44 61 74 61 45 74 68 53 65 74 74 69 6E 67 73 20 01 C0 A8 00 64 08 43


Table 132: Telegram structure: sWA ScanDataEthSettings
                         Telegram structure: sWA ScanDataEthSettings


 Telegram              Description        Variable   Length          Additional details       Values CoLa A      Values CoLa B
    part                                                                                         (ASCII)            (Binary)
Command        Answer                     String     3                                       sWA                73 57 41
type
Command        String                     String     19                                      ScanDataEth-       53 63 61 6E 44
                                                                                             Settings           61 74 61 45 74 68
                                                                                                                53 65 74 74 69
                                                                                                                6E 67 73

Table 133: Example: sWA ScanDataEthSettings

 CoLa      <STX>sWA{SPC}ScanDataEthSettings<ETX>
  A        02 73 57 41 20 53 63 61 6E 44 61 74 61 45 74 68 53 65 74 74 69 6E 67 73 03
CoLa B 02 02 02 02 00 00 00 18 73 57 41 20 53 63 61 6E 44 61 74 61 45 74 68 53 65 74 74 69 6E 67 73 20 16




8028981/1X1R/2026-06-10 | SICK                                                                               multiScan165    125
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

12.5.1.4.4.5                     Read streaming ethernet settings [sRN ScanDataEthSettings]
Read ethernet settings for the scan data streaming functionality of the device.
Table 134: Telegram structure: sRN ScanDataEthSettings
                          Telegram structure: sRN ScanDataEthSettings
                              (User level 'Authorized client' required)

 Telegram             Description         Variable   Length          Additional details       Values CoLa A        Values CoLa B
    part                                                                                         (ASCII)              (Binary)
Command        Read                       String     3                                        sRN                 73 52 4E
type
Command        String                     String     19                                       ScanDataEth-        53 63 61 6E 44
                                                                                              Settings            61 74 61 45 74 68
                                                                                                                  53 65 74 74 69
                                                                                                                  6E 67 73

Table 135: Example: sRN ScanDataEthSettings
           <STX>sWN{SPC}ScanDataEthSettings<ETX>
 CoLa      <STX>sRN ScanDataEthSettings<ETX>
  A        sRN ScanDataEthSettings
           02 73 52 4E 20 53 63 61 6E 44 61 74 61 45 74 68 53 65 74 74 69 6E 67 73 03
           02 02 02 02 00 00 00 17 73 52 4E 20 53 63 61 6E 44 61 74 61 45 74 68 53 65 74 74 69 6E 67 73 3C
CoLa B 73 57 4E 20 53 63 61 6E 44 61 74 61 45 74 68 53 65 74 74 69 6E 67 73


Table 136: Telegram structure: sRA ScanDataEthSettings
                          Telegram structure: sRA ScanDataEthSettings


 Telegram             Description         Variable   Length          Additional details       Values CoLa A        Values CoLa B
    part                                                                                         (ASCII)              (Binary)
Command        Answer                     String     3                                        sRA                 73 52 41
type
Command        String                     String     19                                       ScanDataEth-        53 63 61 6E 44
                                                                                              Settings            61 74 61 45 74 68
                                                                                                                  53 65 74 74 69
                                                                                                                  6E 67 73
Protocol       Transport protocol for     Enum_8     1        UDP:                            +1d (01h)           01
               streaming data                                 TCP:                            +2d (02h)           02
IPAddress      IP address of the desti-   Array      4                                        0 …+255d (00…       00 … FF
               nation for data receiver                                                       FF)
                                                                                              0 …+255d            00 … FF
                                                                                              (00..FF)
                                                                                              0 …+255d (00…       00 … FF
                                                                                              FF)
                                                                                              0 …+255d (00…       00 … FF
                                                                                              FF)
Port           Port destination of the    Uint_16    2                                        0 .. +65535d(00 00 00 … FF FF
               data receiver                                                                  00…FF FF)

Example: sRA ScanDataEthSettings +1 +192 +168 +0 +100 +2115
Protocol is set to UDP (1), IPAddress (192.168.0.100), Port (2115)
Table 137: Example: sRA ScanDataEthSettings
           <STX>sRA{SPC}ScanDataEthSettings{SPC}1{SPC}C0{SPC}A8{SPC}0{SPC}64{SPC}843<ETX>
 CoLa
  A        02 73 52 41 20 53 63 61 6E 44 61 74 61 45 74 68 53 65 74 74 69 6E 67 73 20 31 20 43 30 20 41 38 20 30 20 36 34 20 38
           34 33 03




126        multiScan165                                                                                 8028981/1X1R/2026-06-10 | SICK
                                                                                                  SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

       02 02 02 02 00 00 00 1F 73 52 41 20 53 63 61 6E 44 61 74 61 45 74 68 53 65 74 74 69 6E 67 73 20 01 C0 A8 00 64 08 43
CoLa B 5F



12.5.1.4.4.6                     Set IMU data enable [sWN ImuDataEnable]
Enables/ Disables streaming IMU data output.
Table 138: Telegram structure: sWN ImuDataEnable
                           Telegram structure: sWN ImuDataEnable
                            (User level 'Authorized client' required)

 Telegram              Description       Variable   Length            Additional details    Values CoLa A   Values CoLa B
    part                                                                                       (ASCII)         (Binary)
Command        Write                     String     3                                       sWN             73 57 4E
type
Command        Set streaming IMU data    String     13                                      ImuDataEnable   49 6D 75 44 61
               output.                                                                                      74 61 45 6E 61
                                                                                                            62 6C 65
IMU data       Enable/ disable           Bool       1        Disbale:                       0d (00h)        00 ... 01
stream                                                       Enable:                        +1d (01h)

Table 139: Example: sWN ImuDataEnable 0 - Disable the streaming IMU data output
           <STX>sWN{SPC}ImuDataEnable{SPC}0<ETX>
 CoLa      <STX>sWN ImuDataEnable 0<ETX>
  A        sWN ImuDataEnable 0
           02 73 57 4E 20 49 6D 75 44 61 74 61 45 6E 61 62 6C 65 20 30 03
           02 02 02 02 00 00 00 13 73 57 4E 20 49 6D 75 44 61 74 61 45 6E 61 62 6C 65 20 00 2A
CoLa B 73 57 4E 20 49 6D 75 44 61 74 61 45 6E 61 62 6C 65 20 00


Table 140: Telegram structure: sWA ImuDataEnable
                           Telegram structure: sWA ImuDataEnable


 Telegram              Description       Variable   Length            Additional details    Values CoLa A   Values CoLa B
    part                                                                                       (ASCII)         (Binary)
Command        Answer                    String     3                                       sWA             73 57 41
type
Command        Set streaming IMU data    String     13                                      ImuDataEnable   49 6D 75 44 61
               output.                                                                                      74 61 45 6E 61
                                                                                                            62 6C 65

Table 141: Example: sWA ImuDataEnable

 CoLa      <STX>sWA{SPC}ImuDataEnable<ETX>
  A        02 73 57 41 20 49 6D 75 44 61 74 61 45 6E 61 62 6C 65 03
CoLa B 02 02 02 02 00 00 00 12 73 57 41 20 49 6D 75 44 61 74 61 45 6E 61 62 6C 65 20 25


12.5.1.4.4.7                     Set IMU data streaming ethernet settings [sWN ImuDataEthSettings]
Ethernet settings for the IMU data streaming functionality of the device
Table 142: Telegram structure: sWN ImuDataEthSettings
                         Telegram structure: sWN ImuDataEthSettings
                            (User level 'Authorized client' required)

 Telegram              Description       Variable   Length            Additional details    Values CoLa A   Values CoLa B
    part                                                                                       (ASCII)         (Binary)
Command        Write                     String     3                                       sWN             73 57 4E
type


8028981/1X1R/2026-06-10 | SICK                                                                          multiScan165    127
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                          Telegram structure: sWN ImuDataEthSettings
                             (User level 'Authorized client' required)

 Telegram             Description         Variable   Length          Additional details       Values CoLa A       Values CoLa B
    part                                                                                         (ASCII)             (Binary)
Command        Set IMU data streaming    String      18                                      ImuDataEthSet- 49 6D 75 44 61
               ethernet settings                                                             tings          74 61 45 74 68
                                                                                                            53 65 74 74 69
                                                                                                            6E 67 73
Protocol       Transport protocol for    Enum_8      1        UDP:                           +1d (01h)           01
               streaming IMU data
IP address     IP address of the des-    Array       4                                       0 …+255d (00…       00 … FF
               tination for IMU data                                                         FF)
               receiver                                                                      0 …+255d            00 … FF
                                                                                             (00..FF)
                                                                                             0 …+255d (00…       00 … FF
                                                                                             FF)
                                                                                             0 …+255d (00…       00 … FF
                                                                                             FF)
Port           Port destination of the   Uint_16     2                                       0 .. +65535d(00 00 00 … FF FF
               IMU data reseiver                                                             00…FF FF)

Example: sWN ImuDataEthSettings +1 +192 +168 +0 +100 +7503
Protocol is set to UPD (1), IPAddress (192.168.0.100), Port (7503)
Table 143: Example: sWN ImuDataEthSettings
           <STX>sWN{SPC}ImuDataEthSettings{SPC}+1{SPC}+192{SPC}+168{SPC}+0{SPC}+100{SPC}+7503<ETX>
           <STX>sWN ImuDataEthSettings +1 +192 +168 +0 +100 +7503<ETX>
 CoLa
  A        sWN ImuDataEthSettings +1 +192 +168 +0 +100 +7503
           02 73 57 4E 20 49 6D 75 44 61 74 61 45 74 68 53 65 74 74 69 6E 67 73 20 31 20 43 30 20 41 38 20 30 20 36 34
           20 31 44 34 46 03
           02 02 02 02 00 00 00 1E 73 57 4E 20 49 6D 75 44 61 74 61 45 74 68 53 65 74 74 69 6E 67 73 20 01 C0 A8 00 64 1D 4F
           28
CoLa B
           73 57 4E 20 49 6D 75 44 61 74 61 45 74 68 53 65 74 74 69 6E 67 73 20 01 C0 A8 00 64 1D 4F


Table 144: Telegram structure: sWA ImuDataEthSettings
                          Telegram structure: sWA ImuDataEthSettings


 Telegram             Description         Variable   Length          Additional details       Values CoLa A       Values CoLa B
    part                                                                                         (ASCII)             (Binary)
Command        Answer                    String      3                                       sWA                 73 57 41
type
Command        Set IMU data streaming    String      18                                      ImuDataEthSet- 49 6D 75 44 61
               ethernet settings                                                             tings          74 61 45 74 68
                                                                                                            53 65 74 74 69
                                                                                                            6E 67 73

Table 145: Example: sWA ImuDataEthSettings

 CoLa      <STX>sWA{SPC}ImuDataEthSettings<ETX>
  A        02 73 57 41 20 49 6D 75 44 61 74 61 45 74 68 53 65 74 74 69 6E 67 73 03
CoLa B 02 02 02 02 00 00 00 17 73 57 41 20 49 6D 75 44 61 74 61 45 74 68 53 65 74 74 69 6E 67 73 20 78


12.5.1.4.4.8                     Read scan data format [sRN ScanDataFormat]
Return of the scan data format




128        multiScan165                                                                                8028981/1X1R/2026-06-10 | SICK
                                                                                                 SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

Table 146: Telegram structure: sRN ScanDataFormat
                           Telegram structure: sRN ScanDataFormat
                            (User Level 'Authorized client' required)

 Telegram              Description         Variable   Length       Additional details        Values CoLa A      Values CoLa B
    part                                                                                        (ASCII)            (Binary)
Command        Read                        String     3                                      sRN               73 52 4E
type
Command        Data serialization for-     String     14                                     ScanDataFor-      53 63 61 6E 44
               mat                                                                           mat               61 74 61 46 6F 72
                                                                                                               6D 61 74

Example: sRN ScanDataFormat
Read of the data serialization format
Table 147: Example: sRN ScanDataFormat
          <STX>sRN{SPC}ScanDataFormat<ETX>
 CoLa     <STX>sRN ScanDataFormat<ETX>
  A       sRN ScanDataFormat
          02 73 52 4E 20 53 63 61 6E 44 61 74 61 46 6F 72 6D 61 74 03
          02 02 02 02 00 00 00 12 73 52 4E 20 53 63 61 6E 44 61 74 61 46 6F 72 6D 61 74 63
CoLa B 73 52 4E 20 53 63 61 6E 44 61 74 61 46 6F 72 6D 61 74


Table 148: Telegram structure: sRA ScanDataFormat
                           Telegram structure: sRA ScanDataFormat


 Telegram              Description          Variable Length        Additional details        Values CoLa A      Values CoLa B
    part                                                                                        (ASCII)            (Binary)
Command        Answer                       String    3                                      sRA               73 52 41
type
Command        Data serialization format    String    14                                     ScanDataFor-      53 63 61 6E 44
                                                                                             mat               61 74 61 46 6F 72
                                                                                                               6D 61 74
Data                                        Enum_8    1        MSGPACK:                      1h                01
                                                               Compact:                      2h                02

Example: sRA ScanDataFormat
Scan data format is set to Compact = 2
Table 149: Example: sRA ScanDataFormat

 CoLa     <STX>sRA{SPC}ScanDataFormat{SPC}2<ETX>
  A       02 73 57 41 20 53 63 61 6E 44 61 74 61 46 6F 72 6D 61 74 20 32 03
CoLa B 02 02 02 02 00 00 00 14 73 57 41 20 53 63 61 6E 44 61 74 61 46 6F 72 6D 61 74 20 02 4E


12.5.1.4.4.9                    Set Scan data format [sWN ScanDataFormat]
Set the data serialization format
Table 150: Telegram structure: sWN ScanDataFormat
                           Telegram structure: sWN ScanDataFormat
                            (User Level 'Authorized client' required)

 Telegram              Description         Variable   Length       Additional details        Values CoLa A      Values CoLa B
    part                                                                                        (ASCII)            (Binary)
Command        Write                       String     3                                      sWN               73 57 4E
type




8028981/1X1R/2026-06-10 | SICK                                                                              multiScan165    129
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                           Telegram structure: sWN ScanDataFormat
                            (User Level 'Authorized client' required)

 Telegram              Description        Variable   Length          Additional details          Values CoLa A      Values CoLa B
    part                                                                                            (ASCII)            (Binary)
Command        Data serialization for-   String      14                                      ScanDataFor-          53 63 61 6E 44
               mat                                                                           mat                   61 74 61 46 6F 72
                                                                                                                   6D 61 74
Variable       Data                      Enum_8      1        MSGPACK:                       +1d (1h)              01
Data                                                          Compact:                       +2d (2h)              02

Example: sWN ScanDataFormat
Scan data format set to Compact format
Table 151: Example: sWN ScanDataFormat
           <STX>sWN{SPC}ScanDataFormat{SPC}2<ETX>
 CoLa      <STX>sWN ScanDataFormat 2<ETX>
  A        sWN ScanDataFormat 2
           02 73 57 4E 20 53 63 61 6E 44 61 74 61 46 6F 72 6D 61 74 20 32 03
           02 02 02 02 00 00 14 73 57 4E 20 53 63 61 6E 44 61 74 61 46 6F 72 6D 61 74 20 02 44
CoLa B 73 57 4E 20 53 63 61 6E 44 61 74 61 46 6F 72 6D 61 74 20 02


Table 152: Telegram structure: sWA ScanDataFormat
                           Telegram structure: sWA ScanDataFormat


 Telegram              Description        Variable   Length          Additional details          Values CoLa A      Values CoLa B
    part                                                                                            (ASCII)            (Binary)
Command        Answer                    String      3                                       sWA                   73 57 41
type
Command        Data serialization for-   String      14                                      ScanDataFor-          53 63 61 6E 44
               mat                                                                           mat                   61 74 61 46 6F 72
                                                                                                                   6D 61 74

Table 153: Example: sWA ScanDataFormat

 CoLa      <STX>sWA{SPC}ScanDataFormat<ETX>
  A        02 73 57 41 20 53 63 61 6E 44 61 74 61 46 6F 72 6D 61 74 03
CoLa B 02 02 02 02 00 00 00 13 73 57 41 20 53 63 61 6E 44 61 74 61 46 6F 72 6D 61 74 20 49


12.5.1.4.5                Time stamp


12.5.1.4.5.1                    Set time synchronization [sWN TSCRole]
Set the device synchronization mode.
Table 154: Telegram structure: sWN TSCRole
                               Telegram structure: sWN TSCRole
                            (User Level 'Authorized client' required)

 Telegram              Description        Variable   Length          Additional details          Values CoLa A      Values CoLa B
    part                                                                                            (ASCII)            (Binary)
Command        Write                     String      3                                       sWN                   73 57 4E
type
Command        Set timestamp role        String      7                                       TSCRole               54 53 43 52 6F
                                                                                                                   6C 65
Status         Timestamp role            Uint_8      1        Off:                           0                     00
                                                              NTP:                           1                     01
                                                              PTP:                           3                     03



130        multiScan165                                                                                  8028981/1X1R/2026-06-10 | SICK
                                                                                                   SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

Table 155: Example: sWN TSCRole
          <STX>sWN{SPC}TSCRole{SPC}1<ETX>
 CoLa     <STX>sWN TSCRole 1<ETX>
  A       sWN TSCRole 1
          02 73 57 4E 20 54 53 43 52 6F 6C 65 20 31 03
          02 02 02 02 00 00 00 0D 73 57 4E 20 54 53 43 52 6F 6C 65 20 01 1B
CoLa B 73 57 4E 20 54 53 43 52 6F 6C 65 20 01



Table 156: Telegram structure: sWA TSCRole
                             Telegram structure: sWA TSCRole


 Telegram           Description        Variable    Length        Additional details     Values CoLa A    Values CoLa B
    part                                                                                   (ASCII)          (Binary)
Command        Answer                  String      3                                   sWA              73 57 41
type
Command        Set timestamp role      String      7                                   TSCRole          54 53 43 52 6F
                                                                                                        6C 65

Table 157: Example: sWA TSCRole

 CoLa     <STX>sWA{SPC}TSCRole<ETX>
  A       02 73 57 41 20 54 53 43 52 6F 6C 65 03
CoLa B 02 02 02 02 00 00 00 0C 73 57 41 20 54 53 43 52 6F 6C 65 20 15


12.5.1.4.5.2                    Set time stamp [sMN LSPsetdatetime]
The data format in the telegram is: +2009{SPC}+7{SPC}+22{SPC}+12{SPC}+0{SPC}+0{SPC}+0.
The numbers represent year, month, day, hour, minute, second, microsecond.
If plus is used up-front the data it is interpreted as an integer decimal number, without the plus it's the scanner
reads the data as hex format.
The answer is always in ASCII format.

NOTE
There is no real time clock inside the device. When the scanner is switched off and after a reboot, the time has to
be set again. However, it is possible to analyze the Off-time in order to evade this issue.

Table 158: Telegram structure: sMN LSPsetdatetime
                         Telegram structure: sMN LSPsetdatetime
                          (User level 'Authorized client' required)

 Telegram           Description        Variable    Length        Additional details     Values CoLa A    Values CoLa B
    part                                                                                   (ASCII)          (Binary)
Command        Method                  String      3                                   sMN              73 4D 4E
type
Command        Set time stamp          String      14                                  LSPsetdatetime 4C 53 50 73 65
                                                                                                      74 64 61 74 65
                                                                                                      74 69 6D 65
Year                                   Uint_16     2                                   +1970d …         07 B2 … 08 33
                                                                                       +2099d (07B2h
                                                                                       … 0833h)
Month                                  Uint_8      1                                   +1d … +12d       01 … 0C
                                                                                       (01h … 0Ch)
Day                                    Uint_8      1                                   +1d … +31d       00 … 1F
                                                                                       (01h … 1Fh)




8028981/1X1R/2026-06-10 | SICK                                                                       multiScan165     131
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                        Telegram structure: sMN LSPsetdatetime
                         (User level 'Authorized client' required)

 Telegram           Description       Variable      Length        Additional details       Values CoLa A       Values CoLa B
    part                                                                                      (ASCII)             (Binary)
Hour                                  Uint_8        1                                     +0d … +23d          00 … 17
                                                                                          (00h … 17h)
Minute                                Uint_8        1                                     +0d … +59d          00 … 3B
                                                                                          (00h … 3Bh)
Second                                Uint_8        1                                     +0d … +59d          00 … 3B
                                                                                          (00h … 3Bh)
Microsec-                             Uint_32       4                                     +0d …               00 00 00 00 …
ond                                                                                       +999999d            00 0F 42 3F
                                                                                          (00000000h …
                                                                                          000F423Fh)

Table 159: Example 1: sMN LSPsetdatetime Date: 17.02.2009; Time: 16:34
         <STX>sMN{SPC}LSPsetdatetime{SPC}7D9{SPC}2{SPC}11{SPC}10{SPC}22{SPC}0{SPC}0<ETX>
         <STX>sMN LSPsetdatetime 7D9 2 11 10 22 0 0<ETX>
 CoLa
  A      sMN LSPsetdatetime 7D9 2 11 10 22 0 0
         02 73 4D 4E 20 4C 53 50 73 65 74 64 61 74 65 74 69 6D 65 20 37 44 39 20 32 20 31 31 20 31 30 20 32 32 20 30
         20 30 03
         02 02 02 02 00 00 00 1E 73 4D 4E 20 4C 53 50 73 65 74 64 61 74 65 74 69 6D 65 20 07 D9 02 11 10 22 00 00 00 00 00
         B3
CoLa B
         73 4D 4E 20 4C 53 50 73 65 74 64 61 74 65 74 69 6D 65 20 07 D9 02 11 10 22 00 00 00 00 00


Table 160: Example 2: sMN LSPsetdatetime Date: 26.01.2010; Time: 10:35
         <STX>sMN{SPC}LSPsetdatetime{SPC}+2010{SPC}+01{SPC}+26{SPC}+10{SPC}+35{SPC}0{SPC}0<ETX>
         <STX>sMN LSPsetdatetime +2010 +01 +26 +10 +35 0 0<ETX>
 CoLa
  A      sMN LSPsetdatetime +2010 +01 +26 +10 +35 0 0
         02 73 4D 4E 20 4C 53 50 73 65 74 64 61 74 65 74 69 6D 65 20 2B 32 30 31 30 20 2B 30 31 20 2B 32 36 20 2B 31
         30 20 2B 33 35 20 2B 30 30 20 2B 30 30 30 30 03
         02 02 02 02 00 00 00 1E 73 4D 4E 20 4C 53 50 73 65 74 64 61 74 65 74 69 6D 65 20 07 DA 01 1A 0A 23 00 00 00 00
         00 B3
CoLa B
         73 4D 4E 20 4C 53 50 73 65 74 64 61 74 65 74 69 6D 65 20 07 DA 01 1A 0A 23 00 00 00 00 00



Table 161: Telegram structure: sAN LSPsetdatetime
                        Telegram structure: sAN LSPsetdatetime


 Telegram           Description       Variable      Length        Additional details       Values CoLa A       Values CoLa B
    part                                                                                      (ASCII)             (Binary)
Command      Answer                   String        3                                     sAN                 73 41 4E
type
Command      Set time stamp           String        14                                    LSPsetdatetime 4C 53 50 73 65
                                                                                                         74 64 61 74 65
                                                                                                         74 69 6D 65
Status       Code number              Enum_8        1        Success:                     0                   00
code

Table 162: Example 1, 2: sAN LSPsetdatetime

 CoLa    <STX>sAN{SPC}LSPsetdatetime{SPC}0<ETX>
  A      02 73 41 4E 20 4C 53 50 73 65 74 64 61 74 65 74 69 6D 65 20 30 03
CoLa B 02 02 02 02 00 00 00 14 73 41 4E 20 4C 53 50 73 65 74 64 61 74 65 74 69 6D 65 20 00 50

Activate time stamp in the output string format or on SOPAS page “data processing”.



132      multiScan165                                                                               8028981/1X1R/2026-06-10 | SICK
                                                                                              SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

12.5.1.4.5.3                   Read device time [sRN DeviceTime]
Command to read the actual time of the internal clock (ms).
The timer is 32 counter with a resolution of 1 ms.
Table 163: Telegram structure: sRN DeviceTime
                            Telegram structure: sRN DeviceTime


 Telegram             Description       Variable    Length        Additional details   Values CoLa A      Values CoLa B
    part                                                                                  (ASCII)            (Binary)
Command        Read                     String      3                                  sRN               73 52 4E
type
Command                                 String      10                                 DeviceTime        44 65 76 69 63
                                                                                                         65 54 69 6D 65

Table 164: Example: sRN DeviceTime
          <STX>sRN{SPC}DeviceTime<ETX>
 CoLa     <STX>sRN DeviceTime<ETX>
  A       sRN DeviceTime
          02 73 52 4E 20 44 65 76 69 63 65 54 69 6D 65 03
          02 02 02 02 00 00 00 0E 73 52 4E 20 44 65 76 69 63 65 54 69 6D 65 42
CoLa B 73 52 4E 20 44 65 76 69 63 65 54 69 6D 65



Table 165: Telegram structure: sRA DeviceTime
                            Telegram structure: sRA DeviceTime


 Telegram             Description        Variable Length          Additional details   Values CoLa A      Values CoLa B
    part                                                                                  (ASCII)            (Binary)
Command        Answer                    String     3                                  sRA               73 52 41
type
Command                                  String     10                                 DeviceTime        44 65 76 69 63
                                                                                                         65 54 69 6D 65
Device         The sensor system time     Uint_32   4                                  0d … +9999d       00 00 00 00 …
time           in milliseconds since                                                   (0h … 270Fh)      00 00 27 0F
               January 1, 1970, 00:00
               (UTC). If a time server
               is being used, the config-
               ured system time is used.

Table 166: Example: sRA DeviceTime 0

 CoLa     <STX>sRA{SPC}DeviceTime{SPC}0<ETX>
  A       02 73 52 41 20 44 65 76 69 63 65 54 69 6D 65 20 00 03
CoLa B 02 02 02 02 00 00 00 13 73 52 41 20 44 65 76 69 63 65 54 69 6D 65 20 00 00 00 00 6D


12.5.1.4.5.4                   Set NTP (Network Time Protocol) parameters

12.5.1.4.5.4.1                 Set time server IP address [sWN TSCTCSrvAddr]
Define the IP address from which the device will receive the time synchronization.




8028981/1X1R/2026-06-10 | SICK                                                                        multiScan165   133
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

Table 167: Telegram structure: sWN TSCTCSrvAddr
                          Telegram structure: sWN TSCTCSrvAddr
                           (User level 'Authorized client' required)

 Telegram            Description        Variable   Length          Additional details     Values CoLa A       Values CoLa B
    part                                                                                     (ASCII)             (Binary)
Command      Write                      String     3                                     sWN                 73 57 4E
type
Command      Set time server IP         String     12                                    TSCTCSrvAddr        54 53 43 54 43
             address                                                                                         53 72 76 41 64
                                                                                                             64 72
                                                            First part of IP address     0 …+255d (00…       00 … FF
                                                                                         FF)
                                                            Second part of IP address    0 …+255d (00…       00 … FF
IP address                                                                               FF)
             Set values                 Uint_8     1
data                                                        Third part of IP address     0 …+255d (00…       00 … FF
                                                                                         FF)
                                                            Fourth part of IP address    0 …+255d (00…       00 … FF
                                                                                         FF)

Table 168: Example: sWN TSCTCSrvAddr 192.168.0.11
         <STX>sWN{SPC}TSCTCSrvAddr{SPC}C0{SPC}A8{SPC}00{SPC}0B<ETX>
 CoLa    <STX>sWN TSCTCSrvAddr C0 A8 00 0B<ETX>
  A      sWN TSCTCSrvAddr C0 A8 00 0B
         02 73 57 4E 20 54 53 43 54 43 53 72 76 41 64 64 72 20 43 30 20 41 38 20 30 30 20 30 42 03
         02 02 02 02 00 00 00 15 73 57 4E 20 54 53 43 54 43 53 72 76 41 64 64 72 20 C0 A8 00 0B 3E
CoLa B 73 57 4E 20 54 53 43 54 43 53 72 76 41 64 64 72 20 C0 A8 00 0B



Table 169: Telegram structure: sWA TSCTCSrvAddr
                          Telegram structure: sWA TSCTCSrvAddr


 Telegram            Description        Variable   Length          Additional details     Values CoLa A       Values CoLa B
    part                                                                                     (ASCII)             (Binary)
Command      Answer                     String     3                                     sWA                 73 57 41
type
Command      Set time server IP         String     12                                    TSCTCSrvAddr        54 53 43 54 43
             address                                                                                         53 72 76 41 64
                                                                                                             64 72

Table 170: Example: sWA TSCTCSrvAddr

 CoLa    <STX>sWA{SPC}TSCTCSrvAddr<ETX>
  A      02 73 57 41 20 54 53 43 54 43 53 72 76 41 64 64 72 03
CoLa B 02 02 02 02 00 00 00 11 73 57 41 20 54 53 43 54 43 53 72 76 41 64 64 72 20 52


12.5.1.4.5.4.2                 Set time zone [sWN TSCTCtimezone]
Table 171: Telegram structure: sWN TSCTCtimezone
                          Telegram structure: sWN TSCTCtimezone
                           (User level 'Authorized client' required)

 Telegram            Description        Variable   Length          Additional details     Values CoLa A       Values CoLa B
    part                                                                                     (ASCII)             (Binary)
Command      Write                      String     3                                     sWN                 73 57 4E
type




134      multiScan165                                                                              8028981/1X1R/2026-06-10 | SICK
                                                                                             SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                           Telegram structure: sWN TSCTCtimezone
                            (User level 'Authorized client' required)

 Telegram              Description        Variable   Length         Additional details        Values CoLa A       Values CoLa B
    part                                                                                         (ASCII)             (Binary)
Command         Set time zone             String     13                                       TSCTCtimezone 54 53 43 54 43
                                                                                                            74 69 6D 65 7A
                                                                                                            6F 6E 65
Time zone       Select the time zone of   Enum_8     1        List of time zones see table 172, +0d … +104d      00 … 68
data            the client                                    page 135                          (00h … 68h)

Table 172: Time zone data Values CoLa (ASCII)
0          DATE_LINE_STANDARD               35     MONROVIA_REYKJAVIK               70     MUMBAI_NEUDELHI
1          COORD_WORLD_TIME_11              36     AMSTERDAM_BERLIN_ROM             71     SRI_JAYAWARDENEPURA
2          HAWAII                           37     BELGRAD_BUDAPEST_PRAG            72     KATMANDU
3          ALASKA                           38     BRUESSEL_MADRID_PARIS            73     ASTANA
4          CALIFORNIA                       39     SARAJEVO_WARSCHAU                74     DAKKA
5          USA_CANADA                       40     WEST_CENTRAL_AFRICA              75     NOWOSIBIRSK
6          ARIZONA                          41     WINDHUK                          76     YANGON
7          LA_PAZ                           42     AMMAN                            77     BANGKOK_HANOI_JAKARTA
8          MOUNTAIN_TIME_USA                43     ATHEN_BUKAREST                   78     KRASNOJARSK
9          CENTRAL_TIME_USA                 44     BEIRUT                           79     IRKUTSK
10         MEXICO_CITY                      45     DAMASCUS                         80     KUALA_LUMPUR_SINGAPUR
11         MIDDLE_AMERICA                   46     HARARE_PRETORIA                  81     PEKING_HONGKONG
12         SASKATCHEWAN                     47     HELSINKI_KIEW_RIGA               82     PERTH
13         BOGOTA_LIMA                      48     ISTANBUL                         83     TAIPEH
14         EASTERN_TIME_USA                 49     JERUSALEM                        84     ULAN_BATOR
15         INDIANA                          50     KAIRO                            85     JAKUTSK
16         CARACAS                          51     KALININGRAD                      86     OSAKA_TOKIO
17         ASUNCION                         52     EASTERN_EUROPE                   87     SEOUL
18         ATLANTIC_KANADA                  53     TRIPOLIS                         88     ADELAIDE
19         CUIABA                           54     BAGDAD                           89     DARWIN
20         LAPAZ_SANJUAN                    55     KUWAIT_RIAD                      90     BRISBANE
21         SANTIAGO                         56     MINSK                            91     CANBERRA_SYDNEY
22         NEUFUNDLAND                      57     MOSKAU_PETERSBURG                92     GUAM_PORT_MORESBY
23         BRASILIA                         58     NAIROBI                          93     HOBART
24         BUENOS_AIRES                     59     TEHERAN                          94     MAGADAN
25         CAYENNE_FORTALEZA                60     ABU_DHABI                        95     WLADIWOSTOK
26         GROENLAND                        61     BAKU                             96     SALOMONEN_KALEDONIEN
27         MONTEVIDEO                       62     ERIWAN                           97     TSCHOKURDACH
28         SALVADOR                         63     ISCHEWSK_SAMARA                  98     ANADYR
29         COORD_WORLD_TIME_02              64     PORT_LOUIS                       99     AUCKLAND_WELLINGTON
30         AZOREN                           65     TIFLIS                           100    FIDSCHI
31         KAP_VERDE                        66     KABUL                            101    COORD_WORLD_TIME_12
32         CASABLANCA                       67     ASCHGABET_TASCHKENT              102    NAKUALOFA
33         DUBLIN_LISSABON_LONDON           68     ISLAMABAD_KARATSCHI              103    SAMOA
34         COORD_WORLD_TIME                 69     JEKATERINBURG                    104    KIRITIMATI

Table 173: Example: sWN TSCTCtimezone Amsterdam, Berlin, Rom
             <STX>sWN{SPC}TSCTCtimezone{SPC}+36<ETX>
    CoLa     <STX>sWN TSCTCtimezone +36<ETX>
     A       sWN TSCTCtimezone +36
             02 73 57 4E 20 54 53 43 54 43 74 69 6D 65 7A 6F 6E 65 20 24 03




8028981/1X1R/2026-06-10 | SICK                                                                                multiScan165   135
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

         02 02 02 02 00 00 00 13 73 57 4E 20 54 53 43 54 43 74 69 6D 65 7A 6F 6E 65 20 24 16
CoLa B 73 57 4E 20 54 53 43 54 43 74 69 6D 65 7A 6F 6E 65 20 24



Table 174: Telegram structure: sWA TSCTCtimezone
                         Telegram structure: sWA TSCTCtimezone


 Telegram            Description       Variable   Length        Additional details        Values CoLa A         Values CoLa B
    part                                                                                     (ASCII)               (Binary)
Command      Answer                    String     3                                       sWA                  73 57 41
type
Command      Set time zone             String     13                                      TSCTCtimezone 54 53 43 54 43
                                                                                                        74 69 6D 65 7A
                                                                                                        6F 6E 65

Table 175: Example: sWA TSCTCtimezone

 CoLa    <STX>sWA{SPC}TSCTCtimezone<ETX>
  A      02 73 57 41 20 54 53 43 54 43 74 69 6D 65 7A 6F 6E 65 03
CoLa B 02 02 02 02 00 00 00 12 73 57 41 20 54 53 43 54 43 74 69 6D 65 7A 6F 6E 65 20 3D


12.5.1.4.5.4.3                Set update time [sWN TSCTCupdatetime]
Define the time period after which the sensor will attempt to get the current system time for the TSC server.
Table 176: Telegram structure: sWN TSCTCupdatetime
                        Telegram structure: sWN TSCTCupdatetime
                          (User level 'Authorized client' required)

 Telegram            Description       Variable   Length        Additional details        Values CoLa A         Values CoLa B
    part                                                                                     (ASCII)               (Binary)
Command      Write                     String     3                                       sWN                  73 57 4E
type
Command      Set update time of syn-   String     15                                      TSCTCupdate-         54 53 43 54 43
             chronization                                                                 time                 75 70 64 61 74
                                                                                                               65 74 69 6D 65
Update       Set values in seconds     Uint_32    4                                       +1d … +3600d         00 00 00 00 …
time of                                                                                   (01h … 0E10h)        00 00 0E 10
synchroni-
zation

Table 177: Example: sWN TSCTCupdatetime 600 s
         <STX>sWN{SPC}TSCTCupdatetime{SPC}+600<ETX>
 CoLa    <STX>sWN TSCTCupdatetime +600<ETX>
  A      sWN TSCTCupdatetime +600
         02 73 57 4E 20 54 53 43 54 43 75 70 64 61 74 65 74 69 6D 65 20 2B 36 30 30 03
         02 02 02 02 00 00 00 18 73 57 4E 20 54 53 43 54 43 75 70 64 61 74 65 74 69 6D 65 20 00 00 02 58 67
CoLa B 73 57 4E 20 54 53 43 54 43 75 70 64 61 74 65 74 69 6D 65 20 00 00 02 58



Table 178: Telegram structure: sWA TSCTCupdatetime
                        Telegram structure: sWA TSCTCupdatetime


 Telegram            Description       Variable   Length        Additional details        Values CoLa A         Values CoLa B
    part                                                                                     (ASCII)               (Binary)
Command      Answer                    String     3                                       sWA                  73 57 41
type




136      multiScan165                                                                                8028981/1X1R/2026-06-10 | SICK
                                                                                               SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                             Telegram structure: sWA TSCTCupdatetime


     Telegram            Description            Variable     Length             Additional details   Values CoLa A      Values CoLa B
        part                                                                                            (ASCII)            (Binary)
 Command         Set update time of syn-       String        15                                      TSCTCupdate-      54 53 43 54 43
                 chronization                                                                        time              75 70 64 61 74
                                                                                                                       65 74 69 6D 65

Table 179: Example: sWA TSCTCupdatetime

     CoLa    <STX>sWA{SPC}TSCTCupdatetime<ETX>
      A      02 73 57 41 20 54 53 43 54 43 75 70 64 61 74 65 74 69 6D 65 03
 CoLa B 02 02 02 02 00 00 00 14 73 57 41 20 54 53 43 54 43 75 70 64 61 74 65 74 69 6D 65 20 32


12.5.1.4.6                  Filters


12.5.1.4.6.1                           Set particle filter [sWN LFPparticle]
Filter out disturbances in the meausurement data caused by particles such as dust, snow flakes or similar see
"Particle filter", page 24.
Table 180: Telegram structure: sWN LFPparticle
                                 Telegram structure: sWN LFPparticle
                                (User level 'Authorized client' required)

     Telegram            Description            Variable     Length             Additional details   Values CoLa A      Values CoLa B
        part                                                                                            (ASCII)            (Binary)
 Command         Write                         String        3                                       sWN               73 57 4E
 type
 Command         Set particle filter           String        11                                      LFPparticle       4C 46 50 70 61
                                                                                                                       72 74 69 63 6C
                                                                                                                       65
 Status          Code number                   Bool_1        1          Inactive:                    0                 00
 code                                                                   Active:                      1                 01
 Threshold1) Particle threshold in             Uint_16       2          (must be taken)              +500d (1F4h)      01 F4
             mm

1)    Never change the threshold here, it is taken by the device to handle the particles.

Table 181: Example: sWN LFPparticle
             <STX>sWN{SPC}LFPparticle{SPC}1{SPC}+500<ETX>
     CoLa    <STX>sWN LFPparticle 1 +500<ETX>
      A      sWN LFPparticle 1 +500
             02 73 57 4E 20 4C 46 50 70 61 72 74 69 63 6C 65 20 31 20 2B 35 30 30 03
             02 02 02 02 00 00 00 13 73 57 4E 20 4C 46 50 70 61 72 74 69 63 6C 65 20 01 01 F4 D0
 CoLa B 73 57 4E 20 4C 46 50 70 61 72 74 69 63 6C 65 20 01 01 F4



Table 182: Telegram structure: sWA LFPparticle
                                 Telegram structure: sWA LFPparticle


     Telegram            Description            Variable     Length                   Sensor         Values CoLa A      Values CoLa B
        part                                                                                            (ASCII)            (Binary)
 Command         Answer                        String        3                                       sWA               73 57 41
 type



1)      1)



8028981/1X1R/2026-06-10 | SICK                                                                                      multiScan165   137
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                              Telegram structure: sWA LFPparticle


 Telegram              Description           Variable   Length                 Sensor        Values CoLa A        Values CoLa B
    part                                                                                        (ASCII)              (Binary)
Command        Set particle filter          String      11                                   LFPparticle         4C 46 50 70 61
                                                                                                                 72 74 69 63 6C
                                                                                                                 65

Table 183: Example: sWA LFPparticle

 CoLa    <STX>sWA{SPC}LFPparticle<ETX>
  A      02 73 57 41 20 4C 46 50 70 61 72 74 69 63 6C 65 03
CoLa B 02 02 02 02 00 00 00 10 73 57 41 20 4C 46 50 70 61 72 74 69 63 6C 65 20 2B


12.5.1.4.6.2                         Set echo filter [sWN FREchoFilter]

NOTE
Only available with firmware versions > V1.10.

Select which measurement value(s) shall be send via LMDscanata, if the meausrement of one angular position
returns several distance values (see "Multi-echo analysis", page 18)
Table 184: Telegram structure: sWN FREchoFilter
                              Telegram structure: sWN FREchoFilter
                             (User level 'Authorized client' required)

 Telegram              Description           Variable   Length          Additional details   Values CoLa A        Values CoLa B
    part                                                                                        (ASCII)              (Binary)
Command        Write                        String      3                                    sWN                 73 57 4E
type
Command        Set echo filter              String      12                                   FREchoFilter        46 52 45 63 68
                                                                                                                 6F 46 69 6C 74
                                                                                                                 65 72
Status         Code number                  Enum_8      1        First echo:                 0                   00
code                                                             All echos:                  1                   01
                                                                 Last echo:                  2                   02

Table 185: Example: sWN FREchoFilter
         <STX>sWN{SPC}FREchoFilter{SPC}1<ETX>
 CoLa    <STX>sWN FREchoFilter 1<ETX>
  A      sWN FREchoFilter 1
         02 73 57 4E 20 46 52 45 63 68 6F 46 69 6C 74 65 72 20 31 03
         02 02 02 02 00 00 00 12 73 57 4E 20 46 52 45 63 68 6F 46 69 6C 74 65 72 20 01 7E
CoLa B 73 57 4E 20 46 52 45 63 68 6F 46 69 6C 74 65 72 20 01



Table 186: Telegram structure: sWA FREchoFilter
                             Telegram structure: sWA FREchoFilter


 Telegram              Description           Variable   Length          Additional details   Values CoLa A        Values CoLa B
    part                                                                                        (ASCII)              (Binary)
Command        Answer                       String      3                                    sWA                 73 57 41
type
Command        Set echo filter              String      12                                   FREchoFilter        46 52 45 63 68
                                                                                                                 6F 46 69 6C 74
                                                                                                                 65 72




138      multiScan165                                                                                  8028981/1X1R/2026-06-10 | SICK
                                                                                                 SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

Table 187: Example: sWa FREchoFilter

 CoLa     <STX>sWA{SPC}FREchoFilter<ETX>
  A       02 73 57 41 20 46 52 45 63 68 6F 46 69 6C 74 65 72 03
CoLa B 02 02 02 02 00 00 00 11 73 57 41 20 46 52 45 63 68 6F 46 69 6C 74 65 72 20 70


12.5.1.4.6.3                     Set sensitivity fog filter [sWN MCSenseLevel]
Filter out disturbances in the meausurement data caused by fog or steam.
Table 188: Telegram structure: sWN MCSenseLevel
                           Telegram structure: sWN MCSenseLevel
                            (User level 'Authorized client' required)

 Telegram              Description       Variable   Length          Additional details       Values CoLa A   Values CoLa B
    part                                                                                        (ASCII)         (Binary)
Command        Write                     String     3                                    sWN                 73 57 4E
type
Command        Sense level               String     12                                   MCSenseLevel        4D 43 53 65 6E
                                                                                                             73 65 4C 65 76
                                                                                                             65 6C
Sensitivity    Enable or disable fog     Uint_8     1        Fog Filter off              0                   00
level          filter and Sense Level                        Fog Filter on               1                   01

Table 189: Example: sWN MCSenseLevel
          <STX>sWN{SPC}MCSenseLevel{SPC}1<ETX>
 CoLa     <STX>sWN MCSenseLevel 1<ETX>
  A       sWN MCSenseLevel 1
          02 73 57 4E 20 4D 43 53 65 6E 73 65 4C 65 76 65 6C 20 31 03
          02 02 02 02 00 00 00 10 73 57 4E 20 4D 43 53 65 6E 73 65 4C 65 76 65 6C 20 01 70
CoLa B 73 57 4E 20 4D 43 53 65 6E 73 65 4C 65 76 65 6C 20 01



Table 190: Telegram structure: sWA MCSenseLevel
                             Telegram structure: sWA MCSenseLevel


 Telegram              Description       Variable   Length          Additional details       Values CoLa A   Values CoLa B
    part                                                                                        (ASCII)         (Binary)
Command        Answer                    String     3                                    sWA                 73 57 41
type
Command        Sense level               String     12                                   MCSenseLevel        4D 43 53 65 6E
                                                                                                             73 65 4C 65 76
                                                                                                             65 6C

Table 191: Example: sWA MCSenseLevel

 CoLa     <STX>sWA{SPC}MCSenseLevel<ETX>
  A       02 73 57 41 20 4D 43 53 65 6E 73 65 4C 65 76 65 6C 20 03
CoLa B 02 02 02 02 00 00 00 0F 73 57 41 20 4D 43 53 65 6E 73 65 4C 65 76 65 6C 20 73


12.5.1.4.6.4                     Set cubic area filter [sWN LFPcubicareafilter]
The cubic area filter limits a polar scan to a axisparallel cube defined by its extension in x-, y- and z-range.




8028981/1X1R/2026-06-10 | SICK                                                                           multiScan165   139
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

Table 192: Telegram structure: sWN LFPcubicareafilter
                          Telegram structure: sWN LFPcubicareafilter
                            (User level 'Authorized client' required)

 Telegram              Description        Variable   Length          Additional details      Values CoLa A        Values CoLa B
    part                                                                                        (ASCII)              (Binary)
Command        Write                      String     3                                      sWN                  73 57 4E
type
Command        CubicAreaFilter limits a   String     18                                     LFPcubicarea-        4C 46 50 63 75
               polar scan to a axispar-                                                     filter               62 69 63 61 72
               allel cube                                                                                        65 61 66 69 6C
                                                                                                                 74 65 72
Variable       Enables/Disables the       Bool       1        Off:                          0d                   00
data 1         filter.                                        On:                           1d                   01
Variable       X min                      Int_32     4                                      -200000d…            FF FF B1 E0 …
Data 2         1/10 mm                                                                      +200000d             00 00 4E 20
Variable       X max                      Int_32     4                                      -200000d…            FF FF B1 E0 …
Data 3         1/10 mm                                                                      +200000d             00 00 4E 20
Variable       Y min                      Int_32     4                                      -200000d…            FF FF B1 E0 …
Data 4         1/10 mm                                                                      +200000d             00 00 4E 20
Variable       Y max                      Int_32     4                                      -200000d…            FF FF B1 E0 …
Data 5         1/10 mm                                                                      +200000d             00 00 4E 20
Variable       Z min                      Int_32     4                                      -200000d…            FF FF B1 E0 …
Data 6         1/10 mm                                                                      +200000d             00 00 4E 20
Variable       Z max                      Int_32     4                                      -200000d…            FF FF B1 E0 …
Data 7         1/10 mm                                                                      +200000d             00 00 4E 20

Disables the cubic area filter and set up to the -20000mm…+20000mm in x,y,z direction.
Table 193: Example: sWN LFPcubicAreafilter
           <STX>sWN{SPC}LFPcubicfreafilter{SPC}0{SPC}FFFFB1E0{SPC}4E20{SPC}FFFFB1E0{SPC}4E20{SPC}FFFFB1E0{SPC}
           4E20<ETX>
 CoLa      <STX>sWN LFPcubicareafilter 0 FFFFB1E0 4E20 FFFFB1E0 4E20 FFFFB1E0 4E20<ETX>
  A        sWN LFPcubicareafilter 0 FFFFB1E0 4E20 FFFFB1E0 4E20 FFFFB1E0 4E20
           02 73 57 4E 20 4C 46 50 63 75 62 69 63 61 72 65 61 66 69 6C 74 65 72 20 30 20 46 46 46 46 42 31 45 30 20 34
           45 32 30 20 46 46 46 46 42 31 45 30 20 34 45 32 30 20 46 46 46 46 42 31 45 30 20 34 45 32 30 03
           02 02 02 02 00 00 00 30 73 57 4E 20 4C 46 50 63 75 62 69 63 61 72 65 61 66 69 6C 74 65 72 20 00 FF FF B1 E0 00 00
           4E 20 FF FF B1 E0 00 00 4E 20 FF FF B1 E0 00 00 4E 20 66
CoLa B
           73 57 4E 20 4C 46 50 63 75 62 69 63 61 72 65 61 66 69 6C 74 65 72 20 00 FF FF B1 E0 00 00 4E 20 FF FF B1 E0
           00 00 4E 20 FF FF B1 E0 00 00 4E 20


Table 194: Telegram structure: sWA LFPcubicareafilter
                          Telegram structure: sWALFPcubicareafilter


 Telegram              Description        Variable   Length          Additional details      Values CoLa A        Values CoLa B
    part                                                                                        (ASCII)              (Binary)
Command        Answer                     String     3                                      sWA                  73 57 41
type
Command        CubicAreaFilter limits a   String     18                                     LFPcubicarea-        4C 46 50 63 75
               polar scan to a axispar-                                                     filter               62 69 63 61 72
               allel cube                                                                                        65 61 66 69 6C
                                                                                                                 74 65 72

Table 195: Example: sWA LFPcubicareafilter

 CoLa      <STX>sWA{SPC}LFPcubicareafilter<ETX>
  A        02 73 57 41 20 4C 46 50 63 75 62 69 63 61 72 65 61 66 69 6C 74 65 72 03
CoLa B 02 02 02 02 00 00 00 17 73 57 41 20 4C 46 50 63 75 62 69 63 61 72 65 61 66 69 6C 74 65 72 20 56




140        multiScan165                                                                                8028981/1X1R/2026-06-10 | SICK
                                                                                                 SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

12.5.1.4.6.5                     Set angle range filter [sWN LFPangleRangeFilter]
The angle range filter set up the horizontal (theta) and vertical (phi) start- and stop angle in rad.
With multiScan only the horizontal (theta) angle is adjustable. To adjust the vertical limits use the layer filter
(LFPlayerFilter)
BeamIncrement = the 'beamIncrement' which is used to subsample the beams within the selected angle range.
With a 'beamIncrement' of n only every nth beam from the selected angle range is copied to the output scan, i.e.
the angle resolution is reduced by factor n. If the beamIncrement is zero it is set to one.
Table 196: Telegram structure: sWN LFPangleRangeFilter
                          Telegram structure: sWN LFPangleRangeFilter
                             (User Level 'Authorized client' required)

 Telegram              Description         Variable   Length          Additional details     Values CoLa A         Values CoLa B
    part                                                                                        (ASCII)               (Binary)
Command        Write                       String     3                                      sWN                  73 57 4E
type
Command        filter set up the hori-     String     19                                     LFPangleRan-         4C 46 50 61 6E
               zontal (theta) and verti-                                                     geFilter             67 6C 65 52 61
               cal (phi) start- and stop                                                                          6E 67 65 46 69
               angle in rad                                                                                       6C 74 65 72
Variable       Enables/Disables the        Bool_1     1        Off:                          +0d                  00
Data 1         filter                                          On:                           +1d                  01
Variable       ThetaStart                  Real       4        No impact on sensor setting   -1,800,000d ...      FF E4 88 C0 …
Data 2                                                         but needs to be filled (see   +1,800,000d          00 1B 77 40
                                                               example)                      (FFE488C0 ...
                                                                                             001B7740h)
Variable       ThetaStop                   Real       4        No impact on sensor setting   -1,800,000d ...      FF E4 88 C0 …
Data 3                                                         but needs to be filled (see   +1,800,000d          00 1B 77 40
                                                               example)                      (FFE488C0 ...
                                                                                             001B7740h)
Variable       PhiStart                    Real       4        No impact on sensor setting   -900,000d ...        FF F2 44 60 …
Data 4                                                         but needs to be filled (see   +900,000d            00 0D BB A0
                                                               example)                      (FFF24460 ...
                                                                                             000DBBA0h)
Variable       PhiStop                     Real       4        No impact on sensor setting   -900,000d ...        FF F2 44 60 …
Data 5                                                         but needs to be filled (see   +900,000d            00 0D BB A0
                                                               example)                      (FFF24460 ...
                                                                                             000DBBA0h)
Variable       BeamIncrement               UInt_16    2        No impact on sensor setting   1d…+20d              00 01 … 00 14
Data 6                                                         but needs to be filled (see
                                                               example)

Explanation: Enable the angle range filter and set up theta (horizontal) start -90°, theta stop +90°, phi (vertical) start
-90°, phi stop +90°, beam increment 1
Table 197: Example: sWN LFPanlgeRangeFilter
           <STX>sWN{SPC}LFPangleRangeFilter{SPC}1{SPC}-900000{SPC}+900000{SPC}-900000{SPC}
           +900000{SPC}1<ETX>
 CoLa      <STX>sWN LFPangleRangeFilter 1 -900000 +900000 -900000 +900000 1<ETX>
  A        sWN LFPangleRangeFilter 1 -900000 +900000 -900000 +900000 1
           02 73 57 4E 4C 46 50 61 6E 67 6C 65 52 61 6E 67 65 46 69 6C 74 65 72 20 31 20 2D 39 30 30 30 30 30 20 2B 39
           30 30 30 30 30 20 2D 39 30 30 30 30 30 20 2B 39 30 30 30 30 30 20 31 03
           02 02 02 02 00 00 00 2B 73 57 4E 20 4C 46 50 61 6E 67 6C 65 52 61 6E 67 65 46 69 6C 74 65 72 20 01 FF F2 44 60 00
           0D BB A0 FF F2 44 60 00 0D BB A0 00 01 2E
CoLa B
           73 57 4E 20 4C 46 50 61 6E 67 6C 65 52 61 6E 67 65 46 69 6C 74 65 72 20 01 FF F2 44 60 00 0D BB A0 FF F2 44
           60 00 0D BB A0 00 01




8028981/1X1R/2026-06-10 | SICK                                                                                 multiScan165   141
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

Table 198: Telegram structure: sWA LFP AngleRangeFilter
                          Telegram structure: sWA LFPangleRangeFilter


 Telegram             Description          Variable   Length          Additional details   Values CoLa A       Values CoLa B
    part                                                                                      (ASCII)             (Binary)
Command        Answer                      String     3                                    sWA                73 57 41
type
Command        filter set up the hori-     String     19                                   LFPangleRan-       4C 46 50 61 6E
               zontal (theta) and verti-                                                   geFilter           67 6C 65 52 61
               cal (phi) start- and stop                                                                      6E 67 65 46 69
               angle in rad                                                                                   6C 74 65 72

Table 199: Example: sWA LFPangleRangeFilter

 CoLa      <STX>sWA{SPC}LFPangleRangeFilter<ETX>
  A        02 73 57 41 20 4C 46 50 61 6E 67 6C 65 52 61 6E 67 65 46 69 6C 74 65 72 03
CoLa B 02 02 02 02 00 00 00 18 73 57 41 20 4C 46 50 61 6E 67 6C 65 52 61 6E 67 65 46 69 6C 74 65 72 20 21


12.5.1.4.6.6                     Read angle range filter [sRN LFPangleRangeFilter]
The angle range filter set up the horizontal (theta) and vertical (phi) start- and stop angle in rad.
BeamIncrement = the 'beamIncrement' which is used to subsample the beams within the selected angle range.
With a 'beamIncrement' of n only every nth beam from the selected angle range is copied to the output scan, i.e.
the angle resolution is reduced by factor n. If the beamIncrement is zero it is set to one.
Table 200: Telegram structure: sRN LFPangleRangeFilter
                          Telegram structure: sRN LFPangleRangeFilter
                             (User Level 'Authorized client' required)

 Telegram             Description          Variable   Length          Additional details   Values CoLa A       Values CoLa B
    part                                                                                      (ASCII)             (Binary)
Command        Read                        String     3                                    sRN                73 52 4E
type
Command        filter set up the hori-     String     19                                   LFPangleRan-       4C 46 50 61 6E
               zontal (theta) and verti-                                                   geFilter           67 6C 65 52 61
               cal (phi) start- and stop                                                                      6E 67 65 46 69
               angle in rad                                                                                   6C 74 65 72

Table 201: Example: sRN LFPangleRangeFilter

 CoLa      <STX>sRN{SPC}LFPangleRangeFilter<ETX>
  A        02 73 52 4E 20 4C 46 50 61 6E 67 6C 65 52 61 6E 67 65 46 69 6C 74 65 72 03
CoLa B 02 02 02 02 00 00 00 18 73 52 4E 20 4C 46 50 61 6E 67 6C 65 52 61 6E 67 65 46 69 6C 74 65 72 20 21

Table 202: Telegram structure: sRA LFP AngleRangeFilter
                          Telegram structure: sRA LFPangleRangeFilter


 Telegram             Description          Variable   Length          Additional details   Values CoLa A       Values CoLa B
    part                                                                                      (ASCII)             (Binary)
Command        Answer                      String     3                                    sRA                73 52 41
type
Command        filter set up the hori-     String     19                                   LFPangleRan-       4C 46 50 61 6E
               zontal (theta) and verti-                                                   geFilter           67 6C 65 52 61
               cal (phi) start- and stop                                                                      6E 67 65 46 69
               angle in rad                                                                                   6C 74 65 72
Variable       Enables/Disables the        Bool_1     1        Off:                        +0d                00
Data 1         filter                                          On:                         +1d                01




142        multiScan165                                                                             8028981/1X1R/2026-06-10 | SICK
                                                                                              SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                          Telegram structure: sRA LFPangleRangeFilter


 Telegram              Description         Variable   Length          Additional details     Values CoLa A         Values CoLa B
    part                                                                                        (ASCII)               (Binary)
Variable       ThetaStart                 Real        4        No impact on sensor setting   -1,800,000d ...      FF E4 88 C0 …
Data 2                                                                                       +1,800,000d          00 1B 77 40
                                                                                             (FFE488C0 ...
                                                                                             001B7740h)
Variable       ThetaStop                  Real        4        No impact on sensor setting   -1,800,000d ...      FF E4 88 C0 …
Data 3                                                                                       +1,800,000d          00 1B 77 40
                                                                                             (FFE488C0 ...
                                                                                             001B7740h)
Variable       PhiStart                   Real        4        No impact on sensor setting   -900,000d ...        FF F2 44 60 …
Data 4                                                                                       +900,000d            00 0D BB A0
                                                                                             (FFF24460 ...
                                                                                             000DBBA0h)
Variable       PhiStop                    Real        4        No impact on sensor setting   -900,000d ...        FF F2 44 60 …
Data 5                                                                                       +900,000d            00 0D BB A0
                                                                                             (FFF24460 ...
                                                                                             000DBBA0h)
Variable       BeamIncrement              UInt_16     2        No impact on sensor setting   1d…+20d              00 01 … 00 14
Data 6

Explanation: Angle range filter enabled and set up theta (horizontal) start -90°, theta stop +90°, phi (vertical) start
-90°, phi stop +90°, beam increment 1
Table 203: Example: sRA LFPanlgeRangeFilter
           <STX>sRA{SPC}LFPangleRangeFilter{SPC}1{SPC}-900000{SPC}+900000{SPC}-900000{SPC}
           +900000{SPC}1<ETX>
 CoLa      <STX>sRA LFPangleRangeFilter 1 -900000 +900000 -900000 +900000 1<ETX>
  A        sRA LFPangleRangeFilter 1 -900000 +900000 -900000 +900000 1
           02 73 52 41 4C 46 50 61 6E 67 6C 65 52 61 6E 67 65 46 69 6C 74 65 72 20 31 20 2D 39 30 30 30 30 30 20 2B 39
           30 30 30 30 30 20 2D 39 30 30 30 30 30 20 2B 39 30 30 30 30 30 20 31 03
           02 02 02 02 00 00 00 2B 73 52 41 20 4C 46 50 61 6E 67 6C 65 52 61 6E 67 65 46 69 6C 74 65 72 20 01 FF F2 44 60 00
           0D BB A0 FF F2 44 60 00 0D BB A0 00 01 2E
CoLa B
           73 52 41 20 4C 46 50 61 6E 67 6C 65 52 61 6E 67 65 46 69 6C 74 65 72 20 01 FF F2 44 60 00 0D BB A0 FF F2 44
           60 00 0D BB A0 00 01


12.5.1.4.6.7                     Set interval filter [sWN LFPintervalFilter]
Enables and set up the interval filter. The interval filter reduce the scan output rate by a given factor.
Table 204: Telegram structure: sWN LFPintervalFilter
                            Telegram structure: sWN LFPintervalFilter
                             (User level 'Authorized client' required)

 Telegram              Description         Variable   Length          Additional details     Values CoLa A         Values CoLa B
    part                                                                                        (ASCII)               (Binary)
Command        Write                      String      3                                      sWN                  73 57 4E
type
Command        Reduce the scan output String          17                                     LFPintervalFilter 4C 46 50 69 6E
               rate by a given factor                                                                          74 65 72 76 61
                                                                                                               6C 46 69 6C 74
                                                                                                               65 72
Variable       Enables/Disables the       Bool        1        Off:                          0d (00h)             00
data 1         filter.                                         On:                           +1d (01h)            01




8028981/1X1R/2026-06-10 | SICK                                                                                 multiScan165   143
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                           Telegram structure: sWN LFPintervalFilter
                            (User level 'Authorized client' required)

 Telegram              Description        Variable   Length          Additional details       Values CoLa A       Values CoLa B
    part                                                                                         (ASCII)             (Binary)
Variable       Only every nth scan is    Uint_32     4                                        1d…+50d         00 00 00 01 …
Data 2         output where n is given                                                        (00 00 00 01h … 00 00 00 32
               by                                                                             00 00 00 32h)
               the value of uiReduc-
               tionFactor.

Enables the interval filter an set up to the 3rd scan
Table 205: Example: sWN LFPintervalFilter
           <STX>sWN{SPC}LFPintervalFilter{SPC}1{SPC}3<ETX>
 CoLa      <STX>sWN LFPintervalFilter 1 3<ETX>
  A        sWN LFPintervalFilter 1 3
           02 73 57 4E 20 4C 46 50 69 6E 74 65 72 76 61 6C 46 69 6C 74 65 72 20 31 20 33 03
           02 02 02 02 00 00 00 1B 73 57 4E 20 4C 46 50 69 6E 74 65 72 76 61 6C 46 69 6C 74 65 72 20 01 00 00 00 03 0E
CoLa B 73 57 4E 20 4C 46 50 69 6E 74 65 72 76 61 6C 46 69 6C 74 65 72 20 01 00 00 00 03



Table 206: Telegram structure: sWA LFPintervalFilter
                           Telegram structure: sWA LFPintervalFilter


 Telegram              Description        Variable   Length          Additional details       Values CoLa A       Values CoLa B
    part                                                                                         (ASCII)             (Binary)
Command        Answer                    String      3                                        sWA                73 57 41
type
Command        Reduce the scan output String         17                                       LFPintervalFilter 4C 46 50 69 6E
               rate by a given factor                                                                           74 65 72 76 61
                                                                                                                6C 46 69 6C 74
                                                                                                                65 72

Table 207: Example: sWA LFPintervalFilter

 CoLa      <STX>sWA{SPC}LFPintervalFilter<ETX>
  A        02 73 57 41 20 46 50 69 6E 74 65 72 76 61 6C 46 69 6C 74 65 72 03
CoLa B 02 02 02 02 00 00 00 16 73 57 41 20 4C 46 50 69 6E 74 65 72 76 61 6C 46 69 6C 74 65 72 20 00


12.5.1.4.6.8                    Set layer filter [sWN LFPlayerFilter]
Filter complete layers in the output data
Table 208: Telegram structure: sWN LFPlayerFilter
                            Telegram structure: sWN LFPlayerFilter
                            (User level 'Authorized client' required)

 Telegram              Description        Variable   Length          Additional details       Values CoLa A       Values CoLa B
    part                                                                                         (ASCII)             (Binary)
Command        Write                     String      3                                        sWN                73 57 4E
type
Command        Filter complete layers in String      14                                       LFPlayerFilter     4C 46 50 6C 61
               the output data                                                                                   79 65 72 46 69
                                                                                                                 6C 74 65 72
Variable       Enables/Disables the      Bool_1      1        Off:                            +0d (0h)           00
Data 1         filter.                                        On:                             +1d (1h)           01




144        multiScan165                                                                                8028981/1X1R/2026-06-10 | SICK
                                                                                                 SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                               Telegram structure: sWN LFPlayerFilter
                               (User level 'Authorized client' required)

 Telegram              Description               Variable     Length          Additional details   Values CoLa A        Values CoLa B
    part                                                                                              (ASCII)              (Binary)
Variable       Selection of the layers          Array of      16       Layer 1 off:                +0d (0h)            00 00 00 00 00
Data 2         for data output                  Bool_1                 Layer 1 on:                 +1d (1h)            00 00 00 00 00
                                                                       ...                         …                   00 00 00 00 00
                                                                       Layer 16 off:               +0d (0h)            00 00 00 … 01
                                                                                                                       01 01 01 01 01 01
                                                                       Layer 16 on:                +1d (1h)
                                                                                                                       01 01 01 01 01 01
                                                                                                                       01 01 01 01 01

Disable the layer filter and enables each layers
Table 209: Example: sWN LFPlayerFilter
           <STX>sWN{SPC}LFPlayerFil-
           ter{SPC}0{SPC}1{SPC}1{SPC}1{SPC}1{SPC}1{SPC}1{SPC}1{SPC}1{SPC}1{SPC}1{SPC}1{SPC}1{SPC}1{SPC}1{SPC}1{SPC}1<ET
           X>
 CoLa      <STX>sWN LFPlayerFilter 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<ETX>
  A
           sWN LFPlayerFilter 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
           02 73 57 4E 20 4C 46 50 6C 61 79 65 72 46 69 6C 74 65 72 20 30 20 31 20 31 20 31 20 31 20 31 20 31 20 31 20 31
           20 31 20 31 20 31 20 31 20 31 20 31 20 31 20 31 03
           02 02 02 02 00 00 00 24 73 57 4E 20 4C 46 50 6C 61 79 65 72 46 69 6C 74 65 72 20 00 01 01 01 01 01 01 01 01 01 01 01
           01 01 01 01 01 73
CoLa B
           73 57 4E 20 4C 46 50 6C 61 79 65 72 46 69 6C 74 65 72 20 00 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01



Table 210: Telegram structure: sWA LFPlayerFilter
                               Telegram structure: sWA LFPlayerFilter


 Telegram              Description               Variable     Length          Additional details   Values CoLa A        Values CoLa B
    part                                                                                              (ASCII)              (Binary)
Command        Answer                           String        3                                    sWA                 73 57 41
type
Command        Filter complete layers in String               14                                   LFPlayerFilter      4C 46 50 6C 61
               the output data                                                                                         79 65 72 46 69
                                                                                                                       6C 74 65 72

Table 211: Example: sWA LFPlayerFilter

 CoLa      <STX>sWA{SPC}LFPlayerFilter<ETX>
  A        02 73 57 41 20 4C 46 50 6C 61 79 65 72 46 69 6C 74 65 72 03
CoLa B 02 02 02 02 00 00 00 13 73 57 41 20 4C 46 50 6C 61 79 65 72 46 69 6C 74 65 72 20 7C


12.5.1.4.6.9                        Set moving averaging filter [sWN LFPmovingAveragingFilter]
Enables the moving average filter
Table 212: Telegram structure: sWN LFPmovingAveragingFilter
                       Telegram structure: sWN LFPmovingAveragingFilter
                             (User level 'Authorized client' required)

 Telegram              Description               Variable     Length          Additional details   Values CoLa A        Values CoLa B
    part                                                                                              (ASCII)              (Binary)
Command        Write                            String        3                                    sWN                 73 57 4E
type




8028981/1X1R/2026-06-10 | SICK                                                                                      multiScan165    145
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                        Telegram structure: sWN LFPmovingAveragingFilter
                              (User level 'Authorized client' required)

 Telegram               Description       Variable   Length          Additional details       Values CoLa A        Values CoLa B
    part                                                                                         (ASCII)              (Binary)
Command         String                   String      24                                       LFPmovingA-         4C 46 50 6D 6F
                                                                                              veragingFilter      76 69 6E 67 41
                                                                                                                  76 65 72 61 67
                                                                                                                  69 6E 67 46 69
                                                                                                                  6C 74 65 72
Variable        Moving averaging is      Bool        1        Off:                            0d (00h)            00
Data 1          enabled                                       On:                             +1d (01h)           01
Variable        averaging depth          UInt        2        Minimum:                        +2d (02h)           00 02
Data 2                                                        Maximum:                        +4d (0Ah)           00 04

Disable the moving average filter and set averaging depth to 3
Table 213: Example: sWN LFPmovingAveragingFilter +0 +3
           <STX>sWN{SPC}LFPmovingAveragingFilter{SPC}+0{SPC}+3<ETX>
 CoLa      <STX>sWN LFPmovingAveragingFilter +0 +3<ETX>
  A        sWN LFPmovingAveragingFilter +0 +3
           02 73 57 4E 20 4C 46 50 6D 6F 76 69 6E 67 41 76 65 72 61 67 69 6E 67 46 69 6C 74 65 72 20 2B 30 20 2B 33 03
           02 02 02 02 00 00 00 20 73 57 4E 20 4C 46 50 6D 6F 76 69 6E 67 41 76 65 72 61 67 69 6E 67 46 69 6C 74 65 72 20 01
           00 03 41
CoLa B
           73 57 4E 20 4C 46 50 6D 6F 76 69 6E 67 41 76 65 72 61 67 69 6E 67 46 69 6C 74 65 72 20 01 00 03



Table 214: Telegram structure: sWA LFPmovingAveragingFilter
                        Telegram structure: sWN LFPmovingAveragingFilter


 Telegram               Description       Variable   Length          Additional details       Values CoLa A        Values CoLa B
    part                                                                                         (ASCII)              (Binary)
Command         Answer                   String      3                                        sWA                 73 57 41
type
Command         String                   String      24                                       LFPmovingA-         4C 46 50 6D 6F
                                                                                              veragingFilter      76 69 6E 67 41
                                                                                                                  76 65 72 61 67
                                                                                                                  69 6E 67 46 69
                                                                                                                  6C 74 65 72

Table 215: Example: sWA LFPmovingAveragingFilter

 CoLa      <STX>sWA{SPC}LFPmovingAveragingFilter<ETX>
  A        02 73 57 41 20 4C 46 50 6D 6F 76 69 6E 67 41 76 65 72 61 67 69 6E 67 46 69 6C 74 65 72 03
CoLa B 02 02 02 02 00 00 00 1D 73 57 41 20 4C 46 50 6D 6F 76 69 6E 67 41 76 65 72 61 67 69 6E 67 46 69 6C 74 65 72 20 4D


12.5.1.4.6.10                     Set radial distance range filter [sWN LFPradialDistanceRangeFilter]
Restriction of the scan(s) to a specified distance range.
Table 216: Telegram structure: sWN LFPradialDistanceRangeFilter
                   Telegram structure: sWN LFPradialDistanceRangeFilter
                          (User level 'Authorized client' required)

 Telegram               Description       Variable   Length          Additional details       Values CoLa A        Values CoLa B
    part                                                                                         (ASCII)              (Binary)
Command         Write                    String      3                                        sWN                 73 57 4E
type




146        multiScan165                                                                                 8028981/1X1R/2026-06-10 | SICK
                                                                                                  SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                   Telegram structure: sWN LFPradialDistanceRangeFilter
                          (User level 'Authorized client' required)

 Telegram             Description         Variable   Length          Additional details        Values CoLa A       Values CoLa B
    part                                                                                          (ASCII)             (Binary)
Command         Restriction of the       String      28                                       LFPradialDis-        4C 46 50 72 61
                scan(s) to a specified                                                        tanceRangeFil-       64 69 61 6C 44
                distance range.                                                               ter                  69 73 74 61 6E
                                                                                                                   63 65 52 61 6E
                                                                                                                   67 65 46 69 6C
                                                                                                                   74 65 72
Variable        Enables/Disables the     Bool_1      1        Off:                            0d (0h)              00
Data 1          filter.                                       On:                             1d (1h)              01
DistMin         Lower boundary of the    Int_32      4        Minimum:                        +0d (0h)             00 00 00 00
                distance range.                               Maximum:                        +200000d             00 03 0D 40
                                                                                              (30D40h)
DistMax         Upper boundary of the    Int_32      4        Minimum:                        +0d (0h)             00 00 00 00
                distance range.                               Maximum:                        +200000d             00 03 0D 40
                                                                                              (30D40h)

Disable the radial distance range filter and set up the bounderies to min 0mm and max 200000mm.
Table 217: Example: sWN LFPradialDistanceRangeFilter
           <STX>sWN{SPC}LFPradialDistanceRangeFilter{SPC}0{SPC}0{SPC}30D40<ETX>
           <STX>sWN LFPradialDistanceRangeFilter 0 0 30D40<ETX>
 CoLa
  A        sWN LFPradialDistanceRangeFilter 0 0 30D40
           02 73 57 4E 20 4C 46 50 72 61 64 69 61 6C 44 69 73 74 61 6E 63 65 52 61 6E 67 65 46 69 6C 74 65 72 20 00 20
           00 20 30D40 03
           02 02 02 02 00 00 00 2A 73 57 4E 20 4C 46 50 72 61 64 69 61 6C 44 69 73 74 61 6E 63 65 52 61 6E 6765 46 69 6C 74 65
           72 20 00 00 00 00 00 00 03 0D 40 31
CoLa B
           73 57 4E 20 4C 46 50 72 61 64 69 61 6C 44 69 73 74 61 6E 63 65 52 61 6E 67 65 46 69 6C 74 65 72 20 00 00 00
           00 00 00 03 0D 40


Table 218: Telegram structure: sWA LFPradialDistanceRangeFilter
                   Telegram structure: sWA LFPradialDistanceRangeFilter


 Telegram             Description         Variable   Length          Additional details        Values CoLa A       Values CoLa B
    part                                                                                          (ASCII)             (Binary)
Command         Answer                   String      3                                        sWA                  73 57 41
type
Command         Restriction of the       String      28                                       LFPradialDis-        4C 46 50 72 61
                scan(s) to a specified                                                        tanceRangeFil-       64 69 61 6C 44
                distance range.                                                               ter                  69 73 74 61 6E
                                                                                                                   63 65 52 61 6E
                                                                                                                   67 65 46 69 6C
                                                                                                                   74 65 72

Table 219: Example: sWA LFPradialDistanceRangeFilter

 CoLa      <STX>sWA{SPC}LFPradialDistanceRangeFilter<ETX>
  A        02 73 57 41 20 4C 46 50 72 61 64 69 61 6C 44 69 73 74 61 6E 63 65 52 61 6E 67 65 46 69 6C 74 65 72 03
           02 02 02 02 00 00 00 21 73 57 41 20 4C 46 50 72 61 64 69 61 6C 44 69 73 74 61 6E 63 65 52 61 6E 67 65 46 69 6C 74 65
CoLa B
           72 20 70


12.5.1.4.6.11                    Set Ground Filter [sWN groundFilterEnable]
                                 This telegram is intended to set the ground filter. If the ground filter is enabled, it only
                                 affects the field evaluation and the perpendicular distance application. Measurement
                                 points on the ground are not taken into account for evaluation.




8028981/1X1R/2026-06-10 | SICK                                                                               multiScan165      147
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                        Table 220: Telegram structure: sWN groundFilterEnable
                                      Telegram structure: sWN groundFilterEnable
                                         (User level 'Authorized client' required)

                          Tele-        Description      Varia- Leng       Additional details       Values           Values
                          gram                           ble    th                                 CoLa A          CoLa B
                          part                                                                     (ASCII)         (Binary)
                        Com-        Write               String   3                               sWN             73 57 4E
                        mand
                        type
                        Com-        Ground Filter       String   18                              groundFil-      67 72 6F 75
                        mand                                                                     terEnable       6E 64 46 69
                                                                                                                 6C 74 65 72
                                                                                                                 45 6E 61 62
                                                                                                                 6C 65
                        State       Enable/ disable     Bool     1     Disable:                  0d (00h)        00 ... 01
                                                                       Enable:                   +1d (01h)

                        Table 221: Example: sWN groundFilterEnable
                                  <STX>sWN{SPC}groundFilterEnable{SPC}1<ETX>
                         CoL      <STX>sWN groundFilterEnable 1<ETX>
                         aA       sWN groundFilterEnable 1
                                  02 73 57 4E 20 67 72 6F 75 6E 64 46 69 6C 74 65 72 45 6E 61 62 6C 65 20 31 03
                                  02 02 02 02 00 00 00 18 73 57 4E 20 67 72 6F 75 6E 64 46 69 6C 74 65 72 45 6E 61 62 6C
                         CoL      65 20 01 6F
                         aB       73 57 4E 20 67 72 6F 75 6E 64 46 69 6C 74 65 72 45 6E 61 62 6C 65 20 01

                        Table 222: Telegram structure: sWA groundFilterEnable
                                      Telegram structure: sWA groundFilterEnable


                          Tele-        Description      Varia- Leng       Additional details       Values           Values
                          gram                           ble    th                                 CoLa A          CoLa B
                          part                                                                     (ASCII)         (Binary)
                        Com-        Answer              String   3                               sWA             73 57 41
                        mand
                        type
                        Com-        Ground Filter       String   18                              groundFil-      67 72 6F 75
                        mand                                                                     terEnable       6E 64 46 69
                                                                                                                 6C 74 65 72
                                                                                                                 45 6E 61 62
                                                                                                                 6C 65

                        Table 223: Example: sWA groundFilterEnable

                         CoL      <STX>sWA{SPC}groundFilterEnable<ETX>
                         aA       02 73 57 41 20 67 72 6F 75 6E 64 46 69 6C 74 65 72 45 6E 61 62 6C 65 03
                         CoL      02 02 02 02 00 00 00 17 73 57 41 20 67 72 6F 75 6E 64 46 69 6C 74 65 72 45 6E 61 62 6C
                         aB       65 20 61


12.5.1.4.6.12           Read Ground Filter state [sRN groundFilterEnable]
                        This telegram is intended to read the ground filter state. If the ground filter is enabled,
                        it only affects the field evaluation and the perpendicular distance application. Measure-
                        ment points on the ground are not taken into account for evaluation.




148      multiScan165                                                                             8028981/1X1R/2026-06-10 | SICK
                                                                                            SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                              Table 224: Telegram structure: sRN groundFilterEnable
                                               Telegram structure: sRN groundFilterEnable
                                                 (User level 'Authorized client' required)

                                   Tele-        Description      Varia- Leng       Additional details       Values          Values
                                   gram                           ble    th                                 CoLa A         CoLa B
                                   part                                                                     (ASCII)        (Binary)
                               Com-          Read                String   3                              sRN            73 52 4E
                               mand
                               type
                               Com-          Ground Filter       String   18                             groundFil-     67 72 6F 75
                               mand                                                                      terEnable      6E 64 46 69
                                                                                                                        6C 74 65 72
                                                                                                                        45 6E 61 62
                                                                                                                        6C 65

                              Table 225: Example: sRN groundFilterEnable
                                           <STX>sRN{SPC}groundFilterEnable<ETX>
                                   CoL     <STX>sRN groundFilterEnable<ETX>
                                   aA      sRN groundFilterEnable
                                           02 73 52 4E 20 67 72 6F 75 6E 64 46 69 6C 74 65 72 45 6E 61 62 6C 65 03
                                           02 02 02 02 00 00 00 16 73 52 4E 20 67 72 6F 75 6E 64 46 69 6C 74 65 72 45 6E 61 62 6C
                                   CoL     65 4B
                                   aB      73 52 4E 20 67 72 6F 75 6E 64 46 69 6C 74 65 72 45 6E 61 62 6C 65

                              Table 226: Telegram structure: sRA groundFilterEnable
                                               Telegram structure: sRA groundFilterEnable


                                   Tele-        Description      Varia- Leng       Additional details       Values          Values
                                   gram                           ble    th                                 CoLa A         CoLa B
                                   part                                                                     (ASCII)        (Binary)
                               Com-          Answer              String   3                              sRA            73 52 41
                               mand
                               type
                               Com-          Ground Filter       String   18                             groundFil-     67 72 6F 75
                               mand                                                                      terEnable      6E 64 46 69
                                                                                                                        6C 74 65 72
                                                                                                                        45 6E 61 62
                                                                                                                        6C 65
                               State         Enabled/ disa-      Bool     1     Disabled:                0d (00h)       00 ... 01
                                             bled                               Enabled:                 +1d (01h)

                              Table 227: Example: sRA groundFilterEnable 0 - Ground Filter is disabled

                                   CoL     <STX>sRA{SPC}groundFilterEnable{SPC}0<ETX>
                                   aA      02 73 52 41 20 67 72 6F 75 6E 64 46 69 6C 74 65 72 45 6E 61 62 6C 65 20 30 03
                                   CoL     02 02 02 02 00 00 00 18 73 52 41 20 67 72 6F 75 6E 64 46 69 6C 74 65 72 45 6E 61 62 6C
                                   aB      65 20 00 64


12.5.1.4.6.13                 Read Ground Filter type [sRN groundFilterType]
                              This telegram is intended to read the ground filter type. Currently, the ground filter only
                              works on plain measurement data (P3D-algorythm). The option IMU is currently not
                              available.




8028981/1X1R/2026-06-10 | SICK                                                                                  multiScan165        149
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                        Table 228: Telegram structure: sRN groundFilterType
                                       Telegram structure: sRN groundFilterType
                                        (User level 'Authorized client' required)

                          Tele-        Description       Varia- Leng      Additional details       Values           Values
                          gram                            ble    th                                CoLa A          CoLa B
                          part                                                                     (ASCII)         (Binary)
                        Com-        Read                 String   3                              sRN             73 52 4E
                        mand
                        type
                        Com-        Ground Filter type String     16                             groundFil-      67 72 6F 75
                        mand                                                                     terType         6E 64 46 69
                                                                                                                 6C 74 65 72
                                                                                                                 54 79 70 65

                        Table 229: Example: sRN groundFilterType
                                  <STX>sRN{SPC}groundFilterType<ETX>
                         CoL      <STX>sRN groundFilterType<ETX>
                         aA       sRN groundFilterType
                                  02 73 52 4E 20 67 72 6F 75 6E 64 46 69 6C 74 65 72 54 79 70 65 03
                                  02 02 02 02 00 00 00 14 73 52 4E 20 67 72 6F 75 6E 64 46 69 6C 74 65 72 54 79 70 65 52
                         CoL
                         aB       73 52 4E 20 67 72 6F 75 6E 64 46 69 6C 74 65 72 54 79 70 65

                        Table 230: Telegram structure: sRA groundFilterType
                                       Telegram structure: sRA groundFilterType


                          Tele-        Description       Varia- Leng      Additional details       Values           Values
                          gram                            ble    th                                CoLa A          CoLa B
                          part                                                                     (ASCII)         (Binary)
                        Com-        Answer               String   3                              sRA             73 52 41
                        mand
                        type
                        Com-        Ground Filter type String     16                             groundFil-      67 72 6F 75
                        mand                                                                     terType         6E 64 46 69
                                                                                                                 6C 74 65 72
                                                                                                                 54 79 70 65
                        Variable Type                    Bool     1    P3D:                      0d (00h)        00
                        data                                           IMU:                      +1d (01h)       01

                        Table 231: Example: sRA groundFilterType 0 - Ground Filter type is set to P3D

                         CoL      <STX>sRA{SPC}groundFilterType{SPC}0<ETX>
                         aA       02 73 52 41 20 67 72 6F 75 6E 64 46 69 6C 74 65 72 54 79 70 65 20 30 03
                         CoL      02 02 02 02 00 00 00 16 73 52 41 20 67 72 6F 75 6E 64 46 69 6C 74 65 72 54 79 70 65 20
                         aB       00 7D


12.5.1.4.6.14           Set Ground Filter thresholds [sWN groundFilterThresholds]
                        This telegram is intended to set the threshold limits [mm] of the ground filter. All points
                        with a (signed) distance to the ground plane larger than the minimumDistance and
                        smaller than the maximumDistance will be considered to be ground points.




150      multiScan165                                                                             8028981/1X1R/2026-06-10 | SICK
                                                                                            SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                              Table 232: Telegram structure: sWN groundFilterThresholds
                                             Telegram structure: sWN groundFilterThresholds
                                                  (User level 'Authorized client' required)

                                   Tele-        Description      Varia- Leng       Additional details       Values         Values
                                   gram                           ble    th                                 CoLa A        CoLa B
                                   part                                                                     (ASCII)       (Binary)
                               Com-          Write               String   3                              sWN            73 57 4E
                               mand
                               type
                               Com-          Ground Filter       String   22                             groundFil-     67 72 6F 75
                               mand          thresholds                                                  terThres-      6E 64 46 69
                                                                                                         holds          6C 74 65 72
                                                                                                                        54 68 72 65
                                                                                                                        73 68 6F 6C
                                                                                                                        64 73
                               Variable Minimum dis-             Int_8    2     Default value: -100 mm   -1000d ...     FC 18 ... 03
                               data 1   tance                                                            +1000d         E8
                                                                                                         (FC18h ...
                                                                                                         3E8h)
                               Variable Maximum dis-             Int_8    2     Default value: +100 mm -1000d ...       FC 18 ... 03
                               data 2   tance                                                          +1000d           E8
                                                                                                       (FC18h ...
                                                                                                       3E8h)

                              Table 233: Example: sWN groundFilterThresholds - minimum threshold -50 mm, maximum thresh-
                              old+50 mm
                                           <STX>sWN{SPC}groundFilterThresholds{SPC}-50{SPC}+50<ETX>
                                           <STX>sWN groundFilterThresholds -50 +50<ETX>
                                   CoL
                                   aA      sWN groundFilterThresholds -50 +50
                                           02 73 57 4E 20 67 72 6F 75 6E 64 46 69 6C 74 65 72 54 68 72 65 73 68 6F 6C 64 73
                                           20 2D 35 30 20 2B 35 30 03
                                           02 02 02 02 00 00 00 1F 73 57 4E 20 67 72 6F 75 6E 64 46 69 6C 74 65 72 54 68 72 65 73
                                   CoL     68 6F 6C 64 73 20 FF CE 00 32 68
                                   aB      73 57 4E 20 67 72 6F 75 6E 64 46 69 6C 74 65 72 54 68 72 65 73 68 6F 6C 64 73 20
                                           FF CE 00 32

                              Table 234: Telegram structure: sWA groundFilterThresholds
                                             Telegram structure: sWA groundFilterThresholds


                                   Tele-        Description      Varia- Leng       Additional details       Values         Values
                                   gram                           ble    th                                 CoLa A        CoLa B
                                   part                                                                     (ASCII)       (Binary)
                               Com-          Answer              String   3                              sWA            73 57 41
                               mand
                               type
                               Com-          Ground Filter       String   22                             groundFil-     67 72 6F 75
                               mand          thresholds                                                  terThres-      6E 64 46 69
                                                                                                         holds          6C 74 65 72
                                                                                                                        54 68 72 65
                                                                                                                        73 68 6F 6C
                                                                                                                        64 73

                              Table 235: Example: sWA groundFilterThresholds

                                   CoL     <STX>sWA{SPC}groundFilterThresholds<ETX>
                                   aA      02 73 57 41 20 67 72 6F 75 6E 64 46 69 6C 74 65 72 54 68 72 65 73 68 6F 6C 64 73 03
                                   CoL     02 02 02 02 00 00 00 1B 73 57 41 20 67 72 6F 75 6E 64 46 69 6C 74 65 72 54 68 72 65 73
                                   aB      68 6F 6C 64 73 20 64




8028981/1X1R/2026-06-10 | SICK                                                                                  multiScan165       151
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

12.5.1.4.6.15           Read Ground Filter thresholds [sRN groundFilterThresholds]
                        This telegram is intended to read the threshold limits [mm] of the ground filter. All points
                        with a (signed) distance to the ground plane larger than the minimumDistance and
                        smaller than the maximumDistance will be considered to be ground points.
                        Table 236: Telegram structure: sRN groundFilterThresholds
                                    Telegram structure: sRN groundFilterThresholds
                                        (User level 'Authorized client' required)

                          Tele-        Description      Varia- Leng       Additional details       Values           Values
                          gram                           ble    th                                 CoLa A          CoLa B
                          part                                                                     (ASCII)         (Binary)
                        Com-        Read                String   3                               sRN             73 52 4E
                        mand
                        type
                        Com-        Ground Filter       String   22                              groundFil-      67 72 6F 75
                        mand        thresholds                                                   terThres-       6E 64 46 69
                                                                                                 holds           6C 74 65 72
                                                                                                                 54 68 72 65
                                                                                                                 73 68 6F 6C
                                                                                                                 64 73

                        Table 237: Example: sRN groundFilterThresholds
                                  <STX>sRN{SPC}groundFilterThresholds<ETX>
                                  <STX>sRN groundFilterThresholds<ETX>
                         CoL
                         aA       sRN groundFilterThresholds
                                  02 73 52 4E 20 67 72 6F 75 6E 64 46 69 6C 74 65 72 54 68 72 65 73 68 6F 6C 64 73
                                  03
                                  02 02 02 02 00 00 00 1A 73 52 4E 20 67 72 6F 75 6E 64 46 69 6C 74 65 72 54 68 72 65 73
                         CoL      68 6F 6C 64 73 4E
                         aB       73 57 4E 20 67 72 6F 75 6E 64 46 69 6C 74 65 72 54 68 72 65 73 68 6F 6C 64 73

                        Table 238: Telegram structure: sRA groundFilterThresholds
                                    Telegram structure: sRA groundFilterThresholds


                          Tele-        Description      Varia- Leng       Additional details       Values           Values
                          gram                           ble    th                                 CoLa A          CoLa B
                          part                                                                     (ASCII)         (Binary)
                        Com-        Answer              String   3                               sWA             73 52 41
                        mand
                        type
                        Com-        Ground Filter       String   22                              groundFil-      67 72 6F 75
                        mand        thresholds                                                   terThres-       6E 64 46 69
                                                                                                 holds           6C 74 65 72
                                                                                                                 54 68 72 65
                                                                                                                 73 68 6F 6C
                                                                                                                 64 73
                        Variable Minimum dis-           Int_8    2     Default value: -100 mm    -1000d ...      FC 18 ... 03
                        data 1   tance                                                           +1000d          E8
                                                                                                 (FC18h ...
                                                                                                 3E8h)
                        Variable Maximum dis-           Int_8    2     Default value: +100 mm -1000d ...         FC 18 ... 03
                        data 2   tance                                                        +1000d             E8
                                                                                              (FC18h ...
                                                                                              3E8h)




152      multiScan165                                                                             8028981/1X1R/2026-06-10 | SICK
                                                                                            SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                                Table 239: Example: sRA groundFilterThresholds - minimum threshold -100 mm, maximum
                                threshold +100 mm
                                         <STX>sRA{SPC}groundFilterThresholds{SPC}FF9C{SPC}64<ETX>
                                   CoL
                                   aA    02 73 52 41 20 67 72 6F 75 6E 64 46 69 6C 74 65 72 54 68 72 65 73 68 6F 6C 64 73 20 2D
                                         31 30 30 20 2B 31 30 30 03
                                   CoL   02 02 02 02 00 00 00 1F 73 52 41 20 67 72 6F 75 6E 64 46 69 6C 74 65 72 54 68 72 65 73
                                   aB    68 6F 6C 64 73 20 FF 9C 00 64 66


12.5.1.4.7              Inputs and Outputs


12.5.1.4.7.1                    Read state of the ports [sRN LIDportstate]
LIDportstate has to be available additionally or as successor of the LIDoutputstate telegram.
Valid for all sensors with Ethernet and ports (inputs / outputs).
Table 240: Telegram structure: sRN LIDportstate
                            Telegram structure: sRN LIDportstate


 Telegram             Description          Variable   Length         Additional details        Values CoLa A       Values CoLa B
    part                                                                                          (ASCII)             (Binary)
Command        Read                       String      3                                        sRN                73 52 4E
type
Command        Ask for port configura-    String      12                                       LIDportstate       4C 49 44 70 6F
               tion                                                                                               72 74 73 74 61 74
                                                                                                                  65

Table 241: Example: sRN LIDportstate
          <STX>sRN{SPC}LIDportstate<ETX>
 CoLa     <STX>sRN LIDportstate<ETX>
  A       sRN LIDportstate
          02 73 52 4E 20 4C 49 44 70 6F 72 74 73 74 61 74 65 03
          02 02 02 02 00 00 00 10 73 52 4E 20 4C 49 44 70 6F 72 74 73 74 61 74 65 60
CoLa B 73 52 4E 20 4C 49 44 70 6F 72 74 73 74 61 74 65



Table 242: Telegram structure: sRA LIDportstate
                            Telegram structure: sRA LIDportstate


 Telegram             Description          Variable   Length         Additional details        Values CoLa A       Values CoLa B
    part                                                                                          (ASCII)             (Binary)
Command        Answer                     String      3                                        sRA                73 52 41
type
Command        Port state                 String      12                                       LIDportstate       4C 49 44 70 6F
                                                                                                                  72 74 73 74 61 74
                                                                                                                  65
Status         Version number             Uint_16     2                                        0 … FFFFh          00 01 … FF FF
code                                                           Current version:                0
               System counter (time in Uint_32        4                                        0 … FFFFFFFFh      00 00 00 00 …
               µs since power up max.                                                                             FF FF FF FF
               71min then starting from
               0 again)




8028981/1X1R/2026-06-10 | SICK                                                                                 multiScan165    153
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                            Telegram structure: sRA LIDportstate


 Telegram            Description         Variable   Length          Additional details          Values CoLa A         Values CoLa B
    part                                                                                           (ASCII)               (Binary)
ARRAY         Array includes 8x inter-   Uint_16    2        Hex:                               0000 - FFFF          00 00 - FF FF
which         nal port states and 8x                         Not available:                     00
defines the   external port states.                          Number of ports:                   01 ... n
number of     Structure of ports see
internal      following rows
ports*
State of      Internal port state        Enum_8     1        Output voltage low:                00                   00
the ports                                                    (Relays open)
and count                                                    Output voltage high:               01                   01
value in                                                     (Relays closed)
hex                                                          Tri-state:                         02                   02
                                                             Input voltage high (level):        03                   03
                                                             Input voltage from low to high
                                                             (edge)
                                                             Input voltage low (level):         04                   04
                                                             Input voltage high to low (edge)
              Internal port counter      Uint_32    4                                           0 … FFFFFFFFh        00 00 00 00 …
                                                                                                                     FF FF FF FF
              …..
ARRAY       0...n                        Uint_16    1        Hex:                               00 00 - FF FF        00 00 - FF FF
which                                                        Not available:                     00
defines the                                                  Numer of ports:                    01 ... n
number of
external or
virtual
ports*
State of      External port state        Enum_8     1        Output voltage low:                00                   00
the ports                                                    (Relays open)
and count                                                    Output voltage high:               01                   01
value in                                                     (Relays closed)
hex                                                          Tri-state:                         02                   02
                                                             Input voltage high (level):        03                   03
                                                             Input voltage from low to high
                                                             (edge)
                                                             Input voltage low (level):         04                   04
                                                             Input voltage high to low (edge)
              External port counter      Uint_32    4                                           0 … FFFFFFFFh        00 00 00 00 …
                                                                                                                     FF FF FF FF
Time          States code                Enum_16    1        No time data:                      00 00                00 00
                                                             Time data:                         00 01                00 01
Time Block    Year                       Array      2        E.g.                               1970                 07 B2
(sensor       Month                                 1                                           1 … 12               01 … 0C
time from
the last      Day                                   1                                           1 … 31               01 … 1F
change of     Hour                                  1                                           0 … 23               00 … 17
min. one of   Minute                                1                                           0 … 59               00 … 3B
the out-
              Second                                1                                           0 … 59               00 … 3B
puts)
              Microsecond                           4                                           0 … 999999           00 00 00 00 …
                                                                                                                     00 0F 42 3F

Inputs/outputs: If the device has separate inputs and outputs (instead of general purpose ports) the ARRAY shall
start with inputs followed by the outputs.
Virtual ports are ports that can be used to expand the number of ports but are not physically available. They just
show up in the corresponding ethernet telegrams (like LIDportstate).
Tri-State: Port is neither input nor output; the port is set inactive in SOPAS



154      multiScan165                                                                                      8028981/1X1R/2026-06-10 | SICK
                                                                                                     SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12




Example default parameter of mulitScan136 with 3 ports. Ports configuration: Internal port counter of port 1,2 is 2
Table 243: Example: sRA LIDportstate
          <STX>sRA{SPC}LIDport-
          state{SPC}0{SPC}5F0FF0{SPC}1{SPC}2{SPC}1{SPC}2{SPC}4{SPC}0{SPC}2{SPC}0{SPC}2{SPC}0{SPC}2{SPC}0{SPC}2{
          SPC}0{SPC}2{SPC}0{SPC}2{SPC}0{SPC}2{SPC}0{SPC}2{SPC}0{SPC}2{SPC}0{SPC}2{SPC}0{SPC}2{SPC}0{SPC}2{SPC}
 CoLa     0{SPC}2{SPC}0{SPC}1{SPC}7B2{SPC}1{SPC}1{SPC}0{SPC}0{SPC}6{SPC}38270<ETX>
  A
          02 73 52 41 20 4C 49 44 70 6F 72 74 73 74 61 74 65 20 30 20 35 46 30 46 46 30 20 31 20 32 20 31 20 32 20 34 20 30
          20 32 20 30 20 32 20 30 20 32 20 30 20 32 20 30 20 32 20 30 20 32 20 30 20 32 20 30 20 32 20 30 20 32 20 30 20
          32 20 30 20 32 20 30 20 32 20 30 20 32 20 30 20 31 20 37 42 32 20 31 20 31 20 30 20 30 20 36 20 33 38 32 37 30 03
       02 02 02 02 00 00 00 74 73 52 41 20 4C 49 44 70 6F 72 74 73 74 61 74 65 20 00 00 00 5F 0F F0 01 00 00 00 02 01 00
       00 00 02 04 00 00 00 00 02 00 00 00 00 02 00 00 00 00 02 00 00 00 00 02 00 00 00 00 02 00 00 00 00 02 00
CoLa B
       00 00 00 02 00 00 00 00 02 00 00 00 00 02 00 00 00 00 02 00 00 00 00 02 00 00 00 00 02 00 00 00 00 02 00
       00 00 00 00 01 07 B2 01 01 00 00 06 00 03 82 70 AA


12.5.1.4.7.2                   Read Port Configration of all I/Os [sRN PortConfiguration]
Read the configuration of the digital inputs and outputs.
Table 244: Telegram structure: sRN PortConfiguration
                         Telegram structure: sRN PortConfiguration


 Telegram             Description      Variable   Length        Additional details        Values CoLa A     Values CoLa B
    part                                                                                     (ASCII)           (Binary)
Command        Read                    String     3                                       sRN              73 52 4E
type




8028981/1X1R/2026-06-10 | SICK                                                                          multiScan165   155
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                        Telegram structure: sRN PortConfiguration


 Telegram           Description          Variable   Length          Additional details         Values CoLa A       Values CoLa B
    part                                                                                          (ASCII)             (Binary)
Command      Ask for port configura-     String     12                                        PortConfigura-      50 6F 72 74 43
             tion                                                                             tion                6F 6E 66 69 67
                                                                                                                  75 72 61 74 69
                                                                                                                  6F 6E

Table 245: Example: sRN PortConfiguration
         <STX>sRN{SPC}PortConfiguration<ETX>
 CoLa    <STX>sRN PortConfiguration<ETX>
  A      sRN PortConfiguration
         02 73 52 4E 20 50 6F 72 74 43 6F 6E 66 69 67 75 72 61 74 69 6F 6E 03
         02 02 02 02 00 00 00 15 73 52 4E 20 50 6F 72 74 43 6F 6E 66 69 67 75 72 61 74 69 6F 6E 26
CoLa B 73 52 4E 20 50 6F 72 74 43 6F 6E 66 69 67 75 72 61 74 69 6F 6E



Table 246: Telegram structure: sRA PortConfiguration
                        Telegram structure: sRA PortConfiguration


Telegram     Description                 Variable   Length Additional details                 Values CoLa A       Values CoLa B
part                                                                                          (ASCII)             (Binary)
Command      Answer                      String     3                                         sRA                 73 52 41
type
Command      Configuration of all I/Os   String     12                                        PortConfigura-      50 6F 72 74 43
                                                                                              tion                6F 6E 66 69 67
                                                                                                                  75 72 61 74 69
                                                                                                                  6F 6E
Start of loop, number of loops = amount of all current and future Inputs and Outputs of device family
Port Type    Input or Output             Enum_8     1         Input:                          0                   00
                                                              Output:                         1                   01
Port Name    Amount of characters of Uint_16        2                                         0h … 20h            00 00 … 00 20
             the following port name
             Port name                   String     16                                        [Port name]         [Port name]
                                                    (depen
                                                    ding
                                                    on
                                                    string
                                                    length)
                                                         Input Settings
Logic        Logic of the input          Bool_1     1         Active high:                    0                   00
                                                              Active low:                     1                   01
Debounc-     Select debouncing time Uint_16         2         (max. 10,000ms)                 0h … 2710h          00 00 … 27 10
ing          in ms
Reserved     -                           Enum_8     1         Always:                         0                   00
Reserved     Reserved value 1            Uint_16    2                                         0                   00 00
Reserved     Reserved value 2            Uint_16    2                                         0                   00 00
                                                         Output Settings
Logic        Logic of the input          Bool_1     1         Active high:                    0                   00
                                                              Active low:                     1                   01
Output       PNP, NPN or Push-Pull       Enum_8     1         PNP:                            0                   00
Mode                                                          NPN:                            1                   01
                                                              Push-Pull:                      2                   02




156      multiScan165                                                                                   8028981/1X1R/2026-06-10 | SICK
                                                                                                  SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                         Telegram structure: sRA PortConfiguration


Telegram       Description                Variable   Length Additional details               Values CoLa A      Values CoLa B
part                                                                                         (ASCII)            (Binary)
Restart        Restart behavior of out-   Enum_8     1       Immediately:                    0                  00
type           put after event: imme-                        Time:                           1                  01
               diatly or after specific                      Input:                          2                  02
               time
Restart        [Only with restart type = Uint_32     4       (20 ms … 600,000 ms)            14h … 927C0h       00 00 00 14 …
time           Time], time in ms                                                                                00 09 27 C0
Restart        [Only with restart type = Uint_16     2                                       1 ... 8            00 01 ... 00 08
input          Input], input for restart
Combina-       Combining multiple         Enum_8     1       AND:                            0                  00
tion           Events and/or Inputs                          OR:                             1                  01
                                                             XOR:                            2                  02
Reserved       Reserved value 3           Uint_16    2                                       0                  00 00
Reserved       Reserved value 4           Uint_16    2                                       0                  00 00
Sources        Amount (n) of combined Uint_16        2                                       0h ... FFFFh       00 00 ... FF FF
               sources
               Start of source loop, number of loops = amount of combined sources
               Source name                String     4                                       [Source]           [Source]
                                                             Device Ready:                   DRDY
                                                             Sopas Command:                  SCxx
                                                             (xx = Number of output port)
                                                             Indexsignal:                    SROT
                                                             SyncOutByClock:                 SCLK
                                                             Input = Port Name:              INxx
                                                             (INxx = Number of input port)
               Source Inverted or not     Bool_1     1       Not inverted:                   0                  00
                                                             Inverted:                       1                  01
               Reserved value 5           Uint_8     1                                       0                  00
               Reserved value 6           Uint_8     1                                       0                  00
               Stop of source loop
Reserved       Reserved value 7           Uint_16    2                                       0                  00 00
Reserved       Reserved value 8           Uint_16    2                                       0                  00 00
Reserved       Reserved value 9           Uint_16    2                                       0                  00 00
Reserved       Reserved value 10          Uint_16    2                                       0                  00 00
Stop of loop




8028981/1X1R/2026-06-10 | SICK                                                                               multiScan165    157
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

Table 247: Example: sRA ProtConfiguration
         <STX>sRA{SPC}PortConfigura-
         tion{SPC}1{SPC}6{SPC}InOut1{SPC}0{SPC}A{SPC}0{SPC}0{SPC}0{SPC}1{SPC}0{SPC}0{SPC}C8{SPC}1{SPC}1{SPC}0{SP
         C}0{SPC}1{SPC}DRDY{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}1{SPC}6{SPC}InOut2{SPC}0{SPC}A{SPC}
         1{SPC}0{SPC}0{SPC}1{SPC}0{SPC}0{SPC}C8{SPC}1{SPC}1{SPC}0{SPC}0{SPC}1{SPC}DRDY{SPC}0{SPC}0{SPC}0{SPC}
         0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}6{SPC}InOut3{SPC}0{SPC}A{SPC}1{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}C8{SP
         C}1{SPC}1{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}6{SPC}InOut4{SPC}0{SPC}A{SPC}1{SPC}0{SP
         C}0{SPC}0{SPC}0{SPC}0{SPC}C8{SPC}1{SPC}1{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}6{SPC}I
         nOut5{SPC}0{SPC}A{SPC}1{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}C8{SPC}1{SPC}1{SPC}0{SPC}0{SPC}0{SPC}0{SPC
         }0{SPC}0{SPC}0{SPC}0{SPC}6{SPC}InOut6{SPC}0{SPC}A{SPC}1{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}C8{SPC}1{SP
         C}1{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}1{SPC}6{SPC}InOut7{SPC}0{SPC}A{SPC}1{SPC}0{SPC}0{SP
 CoLa    C}1{SPC}0{SPC}0{SPC}C8{SPC}1{SPC}1{SPC}0{SPC}0{SPC}1{SPC}DRDY{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SP
  A      C}0{SPC}1{SPC}6{SPC}InOut8{SPC}0{SPC}A{SPC}1{SPC}0{SPC}0{SPC}1{SPC}0{SPC}0{SPC}C8{SPC}1{SPC}1{SPC}0{SP
         C}0{SPC}1{SPC}DRDY{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0<ETX>
         <STX>sRA PortConfiguration 1 6 InOut1 0 A 0 0 0 1 0 0 C8 1 1 0 0 1 DRDY 0 0 0 0 0 0 0 1 6 InOut2 0 A 1 0 0 1 0 0
         C8 1 1 0 0 1 DRDY 0 0 0 0 0 0 0 0 6 InOut3 0 A 1 0 0 0 0 0 C8 1 1 0 0 0 0 0 0 0 0 6 InOut4 0 A 1 0 0 0 0 0 C8 1 1 0 0
         0 0 0 0 0 0 6 InOut5 0 A 1 0 0 0 0 0 C8 1 1 0 0 0 0 0 0 0 0 6 InOut6 0 A 1 0 0 0 0 0 C8 1 1 0 0 0 0 0 0 0 1 6 InOut7 0
         A 1 0 0 1 0 0 C8 1 1 0 0 1 DRDY 0 0 0 0 0 0 0 1 6 InOut8 0 A 1 0 0 1 0 0 C8 1 1 0 0 1 DRDY 0 0 0 0 0 0 0<ETX>
         sRA PortConfiguration 1 6 InOut1 0 A 0 0 0 1 0 0 C8 1 1 0 0 1 DRDY 0 0 0 0 0 0 0 1 6 InOut2 0 A 1 0 0 1 0 0 C8 1 1 0
         0 1 DRDY 0 0 0 0 0 0 0 0 6 InOut3 0 A 1 0 0 0 0 0 C8 1 1 0 0 0 0 0 0 0 0 6 InOut4 0 A 1 0 0 0 0 0 C8 1 1 0 0 0 0 0 0
         0 0 6 InOut5 0 A 1 0 0 0 0 0 C8 1 1 0 0 0 0 0 0 0 0 6 InOut6 0 A 1 0 0 0 0 0 C8 1 1 0 0 0 0 0 0 0 1 6 InOut7 0 A 1 0 0
         1 0 0 C8 1 1 0 0 1 DRDY 0 0 0 0 0 0 0 1 6 InOut8 0 A 1 0 0 1 0 0 C8 1 1 0 0 1 DRDY 0 0 0 0 0 0 0
         02 02 02 02 00 00 01 7A 73 52 41 20 50 6F 72 74 43 6F 6E 66 69 67 75 72 61 74 69 6F 6E 20 01 00 06 49 6E 4F 75 74 31
         00 00 0A 00 00 00 00 00 01 00 00 00 00 00 C8 00 01 01 00 00 00 00 00 01 44 52 44 59 00 00 00 00 00 00 00 00
         00 00 00 01 00 06 49 6E 4F 75 74 32 00 00 0A 01 00 00 00 00 01 00 00 00 00 00 C8 00 01 01 00 00 00 00 00 01 44
         52 44 59 00 00 00 00 00 00 00 00 00 00 00 00 00 06 49 6E 4F 75 74 33 00 00 0A 01 00 00 00 00 00 00 00 00 00
         00 C8 00 01 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 06 49 6E 4F 75 74 34 00 00 0A 01 00 00 00 00
         00 00 00 00 00 00 C8 00 01 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 06 49 6E 4F 75 74 35 00 00 0A
         01 00 00 00 00 00 00 00 00 00 00 C8 00 01 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 06 49 6E 4F 75
         74 36 00 00 0A 01 00 00 00 00 00 00 00 00 00 00 C8 00 01 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00
         06 49 6E 4F 75 74 37 00 00 0A 01 00 00 00 00 01 00 00 00 00 00 C8 00 01 01 00 00 00 00 00 01 44 52 44 59 00 00
         00 00 00 00 00 00 00 00 00 01 00 06 49 6E 4F 75 74 38 00 00 0A 01 00 00 00 00 01 00 00 00 00 00 C8 00 01 01
         00 00 00 00 00 01 44 52 44 59 00 00 00 00 00 00 00 00 00 00 00 01
CoLa B
         73 52 41 20 50 6F 72 74 43 6F 6E 66 69 67 75 72 61 74 69 6F 6E 20 01 00 06 49 6E 4F 75 74 31 00 00 0A 00 00
         00 00 00 01 00 00 00 00 00 C8 00 01 01 00 00 00 00 00 01 44 52 44 59 00 00 00 00 00 00 00 00 00 00 00
         01 00 06 49 6E 4F 75 74 32 00 00 0A 01 00 00 00 00 01 00 00 00 00 00 C8 00 01 01 00 00 00 00 00 01 44 52
         44 59 00 00 00 00 00 00 00 00 00 00 00 00 00 06 49 6E 4F 75 74 33 00 00 0A 01 00 00 00 00 00 00 00 00
         00 00 C8 00 01 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 06 49 6E 4F 75 74 34 00 00 0A 01 00
         00 00 00 00 00 00 00 00 00 C8 00 01 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 06 49 6E 4F 75
         74 35 00 00 0A 01 00 00 00 00 00 00 00 00 00 00 C8 00 01 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00
         00 00 06 49 6E 4F 75 74 36 00 00 0A 01 00 00 00 00 00 00 00 00 00 00 C8 00 01 01 00 00 00 00 00 00 00
         00 00 00 00 00 00 00 01 00 06 49 6E 4F 75 74 37 00 00 0A 01 00 00 00 00 01 00 00 00 00 00 C8 00 01 01 00
         00 00 00 00 01 44 52 44 59 00 00 00 00 00 00 00 00 00 00 00 01 00 06 49 6E 4F 75 74 38 00 00 0A 01 00
         00 00 00 01 00 00 00 00 00 C8 00 01 01 00 00 00 00 00 01 44 52 44 59 00 00 00 00 00 00 00 00 00 00 00


12.5.1.4.7.3                    Set port configuration [sWN PortConfiguration]
Configuration of the given ports. Telegram structure represents the configuration of 1 port.
If the device has multiple ports, use the same structure.
Table 248: Telegram structure: sWN PortConfiguration
                          Telegram structure: sWN PortConfiguration
                            (Required User Level: authorized client)

 Telegram              Description       Variable   Length           Additional details           Values CoLa A        Values CoLa B
    part                                                                                             (ASCII)              (Binary)
Command        Write                    String      3                                            sWN                  73 57 4E
type
Command        Configuration of the     String      17                                           PortConfigura-       50 6F 72 74 43
               given ports                                                                       tion                 6F 6E 66 69 67
                                                                                                                      75 72 61 74 69
                                                                                                                      6F 6E




158      multiScan165                                                                                       8028981/1X1R/2026-06-10 | SICK
                                                                                                      SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                        Telegram structure: sWN PortConfiguration
                          (Required User Level: authorized client)

 Telegram           Description         Variable   Length           Additional details   Values CoLa A         Values CoLa B
    part                                                                                    (ASCII)               (Binary)
Port Type    Input or Output            Enum_8     1         Input:                      +0d (0h)              00
                                                             Output:                     +1d (1h)              01
Name         Name of the port           Flex-      9         Default:                    InOut1                00 06 49 6E 4F
                                        String     (0..32)                                                     75 74 31 00
                                                         Input Settings
Logic        Logic of the input         Enum_8     1         Active high:                +0d (0h)              00
                                                             Active low:                 +1d (1h)              01
Debounce     Select debouncing time Uint_8         1                                     +0d ... +255d         00 … FF
             in ms                                                                       (0h … FFh)
Reserved     -                          Enum_8     1         Always:                     +0d (0h)              00
Reserved1                               Uint_16    2                                     +0d (0h)              00 00
Reserved2                               Uint_16    2                                     +0d (0h)              00 00
                                                        Output Settings


Logic        Definition of the output   Enum_8     1         Active high:                +0d (0h)              00
             logic                                           Active low:                 +1d (1h)              01
Output       Set kind of mode for       Enum_8     1         PNP:                        0                     00
Mode         output pin                                      NPN:                        1                     01
                                                             Push-Pull:                  2                     02
Restart      Defines type of restart    Enum_8     1         Immediately:                +0d (0h)              00
Type         to be used                                      Time:                       +1d (1h)              01
Restart      [Only with restart type = Uint_32     4         (20 ms … 600,000 ms)        +20d …                00 00 00 00 …
Time         Time], time in ms                                                           +600000d              00 09 27 C0
                                                                                         (C8h ... 927C0h)
Restart      [Only with restart type = Uint_16     2                                     +1d ... +8d (1h ...   00 00 … 00 08
Input        Input], input for restart                                                   8h)
Combina-     Combining multiple         Enum_8     1         AND:                        +0d (0h)
tion         Events and/or Inputs                            OR:                         +1d (1h)
                                                             XOR:                        +2d (2h)
Reserved     Reserved value 3           Uint_16    2                                     +0d (0h)              00 00
Reserved     Reserved value 4           Uint_16    2                                     +0d (0h)              00 00
                                                                    Source
Source       The source parameter                  2                                     +1d (1h)              00 01
             are only existing if the
             port is set to OUTPUT!
Source       Name of the source         String     4         DeviceNotReady:             DRDY                  44 52 44 59
Name         option                                          Input1:                     IN01                  49 4E 30 31
                                                             Input2:                     IN02                  49 4E 30 32
                                                             SopasCommand:               SC01                  53 43 30 31
Invert       Invert the source signal   Bool_1     1         Not inverted:               +0d (0h)              00
                                                             Inverted:                   +1d (1h)              01
Reserved     Reserved value 5           Uint_8     1                                     +0d (0h)              00
Reserved     Reserved value 6           Uint_8     1                                     +0d (0h)              00
                                                             Reserved
Reserved     Reserved value 7           Uint_16    2                                     +0d (0h)              00 00
Reserved     Reserved value 8           Uint_16    2                                     +0d (0h)              00 00
Reserved     Reserved value 9           Uint_16    2                                     +0d (0h)              00 00
Reserved     Reserved value 10          Uint_16    2                                     +0d (0h)              00 00

Example multiScan136 with 3 ports: sWN PortConfiguration




8028981/1X1R/2026-06-10 | SICK                                                                             multiScan165      159
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX




Figure 62: Example multiScan136 with 3 ports


Table 249: Example: sWN ProtConfiguration
         <STX>sWN{SPC}PortConfiguration{SPC}1{SPC}6{SPC}InOut1{SPC}0{SPC}A{SPC}0{SPC}0{SPC}0{SPC}1{SPC}0{SPC}0{
         SPC}C8{SPC}1{SPC}1{SPC}0{SPC}0{SPC}1{SPC}DRDY{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}1{SPC}6{
         SPC}InOut2{SPC}0{SPC}A{SPC}1{SPC}0{SPC}0{SPC}1{SPC}0{SPC}0{SPC}C8{SPC}1{SPC}1{SPC}0{SPC}0{SPC}1{SPC}D
         RDY{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}6{SPC}InOut3v0{SPC}A{SPC}1{SPC}0{SPC}0{SPC}
         0{SPC}0{SPC}0{SPC}C8{SPC}1{SPC}1{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0<ETX>
         <STX>sWN PortConfiguration 1 6 InOut1 0 A 0 0 0 1 0 0 C8 1 1 0 0 1 DRDY 0 0 0 0 0 0 0 1 6 InOut2 0 A 1 0 0 1 0 0
         C8 1 1 0 0 1 DRDY 0 0 0 0 0 0 0 0 6 InOut3 0 A 1 0 0 0 0 0 C8 1 1 0 0 0 0 0 0 0<ETX>
 CoLa
  A      sWN PortConfiguration 1 6 InOut1 0 A 0 0 0 1 0 0 C8 1 1 0 0 1 DRDY 0 0 0 0 0 0 0 1 6 InOut2 0 A 1 0 0 1 0 0 C8 1 1 0
         0 1 DRDY 0 0 0 0 0 0 0 0 6 InOut3 0 A 1 0 0 0 0 0 C8 1 1 0 0 0 0 0 0 0
         02 73 57 4E 20 50 6F 72 74 43 6F 6E 66 69 67 75 72 61 74 69 6F 6E 20 31 20 36 20 49 6E 4F 75 74 31 20 30 20 41
         20 31 20 30 20 30 20 31 20 30 20 30 20 43 38 20 31 20 31 20 30 20 30 20 31 20 44 52 44 59 20 30 20 30 20 30
         20 30 20 30 20 30 20 30 20 31 20 36 20 49 6E 4F 75 74 32 20 30 20 41 20 31 20 30 20 30 20 31 20 30 20 30 20
         43 38 20 31 20 31 20 30 20 30 20 31 20 44 52 44 59 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 36
         20 49 6E 4F 75 74 33 20 30 20 41 20 31 20 30 20 30 20 30 20 30 20 30 20 43 38 20 31 20 31 20 30 20 30 20 30
         20 30 20 30 20 30 20 30 03
         02 02 02 02 00 00 00 9F 73 57 4E 20 50 6F 72 74 43 6F 6E 66 69 67 75 72 61 74 69 6F 6E 20 01 00 06 49 6E 4F 75 74
         31 00 00 0A 00 00 00 00 00 01 00 00 00 00 00 C8 00 01 01 00 00 00 00 00 01 44 52 44 59 00 00 00 00 00 00 00
         00 00 00 00 01 00 06 49 6E 4F 75 74 32 00 00 0A 01 00 00 00 00 01 00 00 00 00 00 C8 00 01 01 00 00 00 00 00 01
         44 52 44 59 00 00 00 00 00 00 00 00 00 00 00 00 00 06 49 6E 4F 75 74 33 00 00 0A 01 00 00 00 00 00 00 00 00
         00 00 C8 00 01 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 9F
CoLa B
         73 57 4E 20 50 6F 72 74 43 6F 6E 66 69 67 75 72 61 74 69 6F 6E 20 01 00 06 49 6E 4F 75 74 31 00 00 0A 00 00
         00 00 00 01 00 00 00 00 00 C8 00 01 01 00 00 00 00 00 01 44 52 44 59 00 00 00 00 00 00 00 00 00 00 00
         01 00 06 49 6E 4F 75 74 32 00 00 0A 01 00 00 00 00 01 00 00 00 00 00 C8 00 01 01 00 00 00 00 00 01 44 52
         44 59 00 00 00 00 00 00 00 00 00 00 00 00 00 06 49 6E 4F 75 74 33 00 00 0A 01 00 00 00 00 00 00 00 00
         00 00 C8 00 01 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00




160      multiScan165                                                                                     8028981/1X1R/2026-06-10 | SICK
                                                                                                    SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

Table 250: Telegram structure: sWA PortConfiguration
                         Telegram structure: sWA PortConfiguration


 Telegram             Description         Variable   Length           Additional details   Values CoLa A        Values CoLa B
    part                                                                                      (ASCII)              (Binary)
Command        Answer                     String     3                                     sWA                 73 57 41
type
Command        Configuration of the       String     17                                    PortConfigura-      50 6F 72 74 43
               given ports                                                                 tion                6F 6E 66 69 67
                                                                                                               75 72 61 74 69
                                                                                                               6F 6E

Table 251: Example: sWA PortConfiguration

 CoLa     <STX>sWA{SPC}PortConfiguration<ETX>
  A       02 73 57 41 20 50 6F 72 74 43 6F 6E 66 69 67 75 72 61 74 69 6F 6E 03
CoLa B 02 02 02 02 00 00 00 16 73 57 41 20 50 6F 72 74 43 6F 6E 66 69 67 75 72 61 74 69 6F 6E 20 0C


12.5.1.4.7.4                     Read state of the inputs [sRN LIDinputstate]
Use sEN LIDinputstate 1 to receive a telegram each time an input signal (e.g. by trigger) changes. Compare
with chapter "Receive outputstate by event [sEN LIDoutputstate]", page 163.
Table 252: Telegram structure: sRN LIDinputstate
                              Telegram structure: sRN LIDinputstate


 Telegram             Description         Variable   Length           Additional details   Values CoLa A        Values CoLa B
    part                                                                                      (ASCII)              (Binary)
Command        Read                       String     3                                     sRN                 73 52 4E
type
Command        Input state                String     14                                    LIDinputstate       4C 49 44 69 6E
                                                                                                               70 75 74 73 74
                                                                                                               61 74 65

Table 253: Example: sRN LIDinputstate
          <STX>sRN{SPC}LIDinputstate<ETX>
 CoLa     <STX>sRN LIDinputstate<ETX>
  A       sRN LIDinputstate
          02 73 52 4E 20 4C 49 44 69 6E 70 75 74 73 74 61 74 65 03
          02 02 02 02 00 00 00 11 73 52 4E 20 4C 49 44 69 6E 70 75 74 73 74 61 74 65 0F
CoLa B 73 52 4E 20 4C 49 44 69 6E 70 75 74 73 74 61 74 65



Table 254: Telegram structure: sRA LIDinputstate
                              Telegram structure: sRA LIDinputstate


 Telegram             Description         Variable   Length           Additional details   Values CoLa A        Values CoLa B
    part                                                                                      (ASCII)              (Binary)
Command        Answer                     String     3                                     sRA                 73 52 41
type
Command        Output state               String     14                                    LIDinputstate       4C 49 44 69 6E
                                                                                                               70 75 74 73 74
                                                                                                               61 74 65




8028981/1X1R/2026-06-10 | SICK                                                                              multiScan165   161
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                            Telegram structure: sRA LIDinputstate


 Telegram            Description        Variable   Length           Additional details   Values CoLa A        Values CoLa B
    part                                                                                    (ASCII)              (Binary)
Status        Version number            Uint_16    2                                     0h … FFFFh          00 00 … FF FF
code          System counter            Uint_32    4                                     0h…                 00 00 00 00 …
              (time in µs since power                                                    FFFFFFFFh           FF FF FF FF
              up max. 71min then
              starting from 0 again)
State of     Amount of inputs (n)       Enum_8     1        Not active:                  0                   00
the inputs 1 depending of device                            Active:                      1                   01
…n           family                                         Input not used:              2                   02
Time          States code               Uint_16    2        No time data:                0                   00 00
                                                            Time data:                   1                   00 01
Time Block Year                         Array      2        E. g.                        1970                07 B2
(sensor-      Month                                1                                     1 … 12              01 … 0C
time from     Day                                  1                                     1 … 31              01 … 1F
the last
change of     Hour                                 1                                     0 … 23              00 … 17
min. one of   Minute                               1                                     0 … 59              00 … 3B
the out-      Second                               1                                     0 … 59              00 … 3B
puts)
              Microsecond                          4                                     0 … 999999          00 00 00 00 …
                                                                                                             00 0F 42 3F




162      multiScan165                                                                              8028981/1X1R/2026-06-10 | SICK
                                                                                             SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

Table 255: Example: sRA LIDinputstate default settings with port 3 set as input: In1 not used, In2 not used, In3 inactive, In4 not
used, In5 not used, In6 not used, In7 not used, In8 not used, time: 1970-01-01 00:00 5 sec 665,000 microseconds
          <STX>sRA{SPC}LIDinput-
          state{SPC}1{SPC}566D00{SPC}2{SPC}2{SPC}0{SPC}2{SPC}2{SPC}2{SPC}2{SPC}2{SPC}1{SPC}7B2{SPC}1{SPC}1{SPC}0
 CoLa     {SPC}0{SPC}5{SPC}A25A8<ETX>
  A
          02 73 52 41 20 4C 49 44 69 6E 70 75 74 73 74 61 74 65 20 31 20 35 36 36 44 30 30 20 32 20 32 20 30 20 32 20 32 20
          32 20 32 20 32 20 31 20 37 42 32 20 31 20 31 20 30 20 30 20 35 20 41 32 35 41 38 03
          02 02 02 02 00 00 00 2D 73 52 41 20 4C 49 44 69 6E 70 75 74 73 74 61 74 65 20 00 01 00 56 6D 00 02 02 00 02 02
CoLa B
          02 02 02 00 01 07 B2 01 01 00 00 05 00 0A 25 A8 2E


12.5.1.4.7.5                    Read state of the outputs [sRN LIDoutputstate]
Status of all outputs
Table 256: Telegram structure: sRN LIDoutputstate
                            Telegram structure: sRN LIDoutputstate


 Telegram              Description       Variable    Length            Additional details         Values CoLa A       Values CoLa B
    part                                                                                             (ASCII)             (Binary)
Command        Read                      String      3                                           sRN                 73 52 4E
type
Command        Output state              String      14                                          LIDoutputstate      4C 49 44 6F 75
                                                                                                                     74 70 75 74 73
                                                                                                                     74 61 74 65

Table 257: Example: sRN LIDoutputstate
          <STX>sRN{SPC}LIDoutputstate<ETX>
 CoLa     <STX>sRN LIDoutputstate<ETX>
  A       sRN LIDoutputstate
          02 73 52 4E 20 4C 49 44 6F 75 74 70 75 74 73 74 61 74 65 03
          02 02 02 02 00 00 00 12 73 52 4E 20 4C 49 44 6F 75 74 70 75 74 73 74 61 74 65 66
CoLa B 73 52 4E 20 4C 49 44 6F 75 74 70 75 74 73 74 61 74 65


Table 258: Telegram structure: sRA LIDoutputstate
                            Telegram structure: sRA LIDoutputstate


 Telegram              Description       Variable    Length            Additional details         Values CoLa A       Values CoLa B
    part                                                                                             (ASCII)             (Binary)
Complete telegram structure of the answer see "Receive outputstate by event [sEN LIDoutputstate]", page 163.


12.5.1.4.7.6                    Receive outputstate by event [sEN LIDoutputstate]
Output telegram is sent every time an output state changes.
Table 259: Telegram structure: sEN LIDoutputstate
                            Telegram structure: sEN LIDoutputstate


 Telegram              Description       Variable    Length            Additional details         Values CoLa A       Values CoLa B
    part                                                                                             (ASCII)             (Binary)
Command        Event                     String      3                                           sEN                 73 45 4E
type
Command        Output state              String      14                                          LIDoutputstate      4C 49 44 6F 75
                                                                                                                     74 70 75 74 73
                                                                                                                     74 61 74 65
               Start/stop                Enum_8      1        Start:                             1                   01
                                                              Stop:                              0                   00



8028981/1X1R/2026-06-10 | SICK                                                                                    multiScan165   163
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

Table 260: Example: sEN LIDoutputstate
         <STX>sEN{SPC}LIDoutputstate{SPC}1<ETX>
 CoLa    <STX>sEN LIDoutputstate 1<ETX>
  A      sEN LIDoutputstate 1
         02 73 45 4E 20 4C 49 44 6F 75 74 70 75 74 73 74 61 74 65 20 31 03
         02 02 02 02 00 00 00 14 73 45 4E 20 4C 49 44 6F 75 74 70 75 74 73 74 61 74 65 20 01 50
CoLa B 73 45 4E 20 4C 49 44 6F 75 74 70 75 74 73 74 61 74 65 20 01



Table 261: Telegram structure: sRA/sSN LIDoutputstate
                        Telegram structure: sRA/sSN LIDoutputstate


 Telegram             Description        Variable   Length           Additional details    Values CoLa A       Values CoLa B
    part                                                                                      (ASCII)             (Binary)
Command        Answer                    String     3                                     sRA / sSN           73 52 41 / 73 53
type                                                                                                          4E
Command        Output state              String     14                                    LIDoutputstate      4C 49 44 6F 75
                                                                                                              74 70 75 74 73
                                                                                                              74 61 74 65
Status         Version number            Uint_16    2                                     0h … FFFFh          00 00 … FF FF
code           System counter            Uint_32    4                                     0h …                00 00 00 00 …
               (time in µs since power                                                    FFFFFFFFh           FF FF FF FF
               up max. 71min then
               starting from 0 again)
State of     Output 1 ... n state        Enum_8     1        Not active:                  0                   00
the out-                                                     Active:                      1                   01
puts 1 ... n                                                 Output not used:             2                   02
and count
             Output 1 ... n count        Uint_32    4                                     0h …                00 00 00 00 …
value in
                                                                                          FFFFFFFFh           FF FF FF FF
hex. (val-
ues of an
example)
Amount of
outputs (n)
depending
of device
family
Time           States code               Uint_16    2        No time data:                0                   00 00
                                                             Time data:                   1                   00 01
Time Block Year                          Array      2        E. g.                        1970                07 B2
(sensor-       Month                                1                                     1 … 12              01 … 0C
time from      Day                                  1                                     1 … 31              01 … 1F
the last
change of      Hour                                 1                                     0 … 23              00 … 17
min. one of    Minute                               1                                     0 … 59              00 … 3B
the out-       Second                               1                                     0 … 59              00 … 3B
puts)
               Microsecond                          4                                     0 … 999999          00 00 00 00 …
                                                                                                              00 0F 42 3F


12.5.1.4.7.7                    Set output state [sMN mDOSetOutput]
Set a specific output to high or low via software command.

NOTE
Output source needs to be set to "SOPAS command" and the port configured as Output (in case of I/O).




164      multiScan165                                                                               8028981/1X1R/2026-06-10 | SICK
                                                                                              SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

Table 262: Telegram structure: sMN mDOSetOutput
                          Telegram structure: sMN mDOSetOutput


 Telegram            Description           Variable   Length         Additional details    Values CoLa A   Values CoLa B
    part                                                                                      (ASCII)         (Binary)
Command        Method                     String      3                                   sMN              73 4D 4E
type
Command        Set output state           String      12                                  mDOSetOutput     6D 44 4F 53 65
                                                                                                           74 4F 75 74 70
                                                                                                           75 74
Output                                    Uint_8      1                                   1…3              01 … 03
number
Output                                    Enum_8      1        Not active:                0                00
state                                                          Active:                    1                01

Table 263: Example: sMN mDOSetOutput
          <STX>sMN{SPC}mDOSetOutput{SPC}1{SPC}1<ETX>
 CoLa     <STX>sMN mDOSetOutput 1 1<ETX>
  A       sMN mDOSetOutput 1 1
          02 73 4D 4E 20 6D 44 4F 53 65 74 4F 75 74 70 75 74 20 31 20 31 03
          02 02 02 02 00 00 00 13 73 4D 4E 20 6D 44 4F 53 65 74 4F 75 74 70 75 74 20 01 01 6B
CoLa B 73 4D 4E 20 6D 44 4F 53 65 74 4F 75 74 70 75 74 20 01 01



Table 264: Telegram structure: sAN mDOSetOutput
                          Telegram structure: sAN mDOSetOutput


 Telegram            Description           Variable   Length         Additional details    Values CoLa A   Values CoLa B
    part                                                                                      (ASCII)         (Binary)
Command        Answer                     String      3                                   sAN              73 41 4E
type
Command        Set output state           String      12                                  mDOSetOutput     6D 44 4F 53 65
                                                                                                           74 4F 75 74 70
                                                                                                           75 74
Status         Status code                Bool_1      1        Error:                     0                00
Code                                                           Success:                   1                01

Table 265: Example: sAN mDOSetOutput

 CoLa     <STX>sAN{SPC}mDOSetOutput{SPC}1<ETX>
  A       02 73 41 4E 20 6D 44 4F 53 65 74 4F 75 74 70 75 74 20 31 03
CoLa B 02 02 02 02 00 00 00 12 73 41 4E 20 6D 44 4F 53 65 74 4F 75 74 70 75 74 20 01 66


12.5.1.4.7.8                      Reset output counter [sMN LIDrstoutpcnt]
Reset the counter which keeps track of how often an digital output has been active (and not active). Informa-
tion from the counter is included in LIDoutputstate (see "Receive outputstate by event [sEN LIDoutputstate]",
page 163).
Table 266: Telegram structure: sMN LIDrstoutpcnt
                             Telegram structure: sMN LIDrstoutpcnt
                             (User level 'Authorized client' required)

 Telegram            Description           Variable   Length         Additional details    Values CoLa A   Values CoLa B
    part                                                                                      (ASCII)         (Binary)
Command        Method                     String      3                                   sMN              73 4D 4E
type




8028981/1X1R/2026-06-10 | SICK                                                                         multiScan165   165
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                           Telegram structure: sMN LIDrstoutpcnt
                           (User level 'Authorized client' required)

 Telegram             Description        Variable   Length         Additional details    Values CoLa A        Values CoLa B
    part                                                                                    (ASCII)              (Binary)
Command        Reset output counter     String      13                                   LIDrstoutpcnt       4C 49 44 72 73
                                                                                                             74 6F 75 74 70
                                                                                                             63 6E 74

Table 267: Example: sMN LIDrstoutpcnt
         <STX>sMN{SPC}LIDrstoutpcnt<ETX>
 CoLa    <STX>sMN LIDrstoutpcnt<ETX>
  A      sMN LIDrstoutpcnt
         02 73 4D 4E 20 4C 49 44 72 73 74 6F 75 74 70 63 6E 74 03
         02 02 02 02 00 00 00 11 73 4D 4E 20 4C 49 44 72 73 74 6F 75 74 70 63 6E 74 03
CoLa B 73 4D 4E 20 4C 49 44 72 73 74 6F 75 74 70 63 6E 74



Table 268: Telegram structure: sAN LIDrstoutpcnt
                           Telegram structure: sAN LIDrstoutpcnt


 Telegram             Description        Variable   Length         Additional details    Values CoLa A        Values CoLa B
    part                                                                                    (ASCII)              (Binary)
Command        Answer                   String      3                                    sAN                 73 41 4E
type
Command        Reset output counter     String      13                                   LIDrstoutpcnt       4C 49 44 72 73
                                                                                                             74 6F 75 74 70
                                                                                                             63 6E 74
Status         Code number              Bool_1      1        Success:                    0                   00
code                                                         Error:                      1                   01

Table 269: Example: sAN LIDrstoutpcnt

 CoLa    <STX>sAN{SPC}LIDrstoutpcnt{SPC}0<ETX>
  A      02 73 41 4E 20 4C 49 44 72 73 74 6F 75 74 70 63 6E 74 20 30 03
CoLa B 02 02 02 02 00 00 00 13 73 41 4E 20 4C 49 44 72 73 74 6F 75 74 70 63 6E 74 20 00 2F


12.5.1.4.8              Status


12.5.1.4.8.1                   Read firmware version [sRN DeviceIdent]
Table 270: Telegram structure: sRN DeviceIdent
                            Telegram structure: sRN DeviceIdent


 Telegram             Description        Variable   Length         Additional details    Values CoLa A        Values CoLa B
    part                                                                                    (ASCII)              (Binary)
Command        Read                     String      3                                    sRN                 73 52 4E
type
Command        Read firmware version    String      11                                   DeviceIdent         44 65 76 69 63
                                                                                                             65 49 64 65 6E
                                                                                                             74

Table 271: Example: sRN DeviceIdent
         <STX>sRN{SPC}DeviceIdent<ETX>
 CoLa    <STX>sRN DeviceIdent<ETX>
  A      sRN DeviceIdent
         02 73 52 4E 20 44 65 76 69 63 65 49 64 65 6E 74 03


166      multiScan165                                                                              8028981/1X1R/2026-06-10 | SICK
                                                                                             SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

          02 02 02 02 00 00 00 0F 73 52 4E 20 44 65 76 69 63 65 49 64 65 6E 74 25
CoLa B 73 52 4E 20 44 65 76 69 63 65 49 64 65 6E 74



Table 272: Telegram structure: sRA DeviceIdent
                            Telegram structure: sRA DeviceIdent


 Telegram             Description        Variable   Length        Additional details        Values CoLa A      Values CoLa B
    part                                                                                       (ASCII)            (Binary)
Command        Answer                    String     3                                      sRA                73 52 41
type
Command                                  String     11                                     DeviceIdent        44 65 76 69 63
                                                                                                              65 49 64 65 6E
                                                                                                              74
Value          Length of firmware des- Enum_16      2                                      0 ... 22h          0 ... 22h
               ignation
Value          Firmware designation      String                                            (See example)      (See example)
               for device family
Value          Length of firmware ver-   Enum_16    2                                      0 ... 22h          0 ... 22h
               sion
Value          Firmware version          String                                            (See example)      (See example)

Table 273: Example: sRA DeviceIdent
 CoLa     <STX>sRA{SPC}DeviceIdent{SPC}9{SPC}multiScan{SPC}8{SPC}2.1.0.2B<ETX>
  A
CoLa B 02 02 02 02 00 00 00 25 73 52 41 20 44 65 76 69 63 65 49 64 65 6E 74 20 00 09 6D 75 6C 74 69 53 63 61 6E 00 08 32
       2E 31 2E 30 2E 32 42 30


12.5.1.4.8.2                   Read version of the application software [sRN FirmwareVersion]
Table 274: Telegram structure: sRN FirmwareVersion
                          Telegram structure: sRN FirmwareVersion


 Telegram             Description        Variable   Length        Additional details        Values CoLa A      Values CoLa B
    part                                                                                       (ASCII)            (Binary)
Command        Read                      String     3                                      sRN                73 52 4E
type
Command        Read version of the       String     15                                     FirmwareVer-       46 69 72 6D 77
               application software                                                        sion               61 72 65 56 65
                                                                                                              72 73 69 6F 6E

Table 275: Example: sRN FirmwareVersion
          <STX>sRN{SPC}FirmwareVersion<ETX>
 CoLa     <STX>sRN FirmwareVersion<ETX>
  A       sRN FirmwareVersion
          02 73 52 4E 20 46 69 72 6D 77 61 72 65 56 65 72 73 69 6F 6E 03
          02 02 02 02 00 00 00 13 73 52 4E 20 46 69 72 6D 77 61 72 65 56 65 72 73 69 6F 6E 24
CoLa B 73 52 4E 20 46 69 72 6D 77 61 72 65 56 65 72 73 69 6F 6E




8028981/1X1R/2026-06-10 | SICK                                                                             multiScan165   167
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

Table 276: Telegram structure: sRA FirmwareVersion
                          Telegram structure: sRA FirmwareVersion


    Telegram          Description       Variable   Length          Additional details         Values CoLa A       Values CoLa B
       part                                                                                      (ASCII)             (Binary)
Command        Answer                   String     3                                         sRA                 73 52 41
type
Command        Read version of the      String     15                                        FirmwareVer-        46 69 72 6D 77
               application software                                                          sion                61 72 65 56 65
                                                                                                                 72 73 69 6F 6E
Value          Length of version        Uint_16    2                                         0 ... 28h           0 ... 28h
Value          Version                  String     16                                        (See example)       (See example)

Table 277: Example: sRA FirmwareVersion
    CoLa   <STX>sRA{SPC}FirmwareVersion{SPC}14{SPC}1.2.0-b.0+1225.523ef<ETX>
     A     02 73 52 41 20 46 69 72 6D 77 61 72 65 56 65 72 73 69 6F 6E 20 31 34 20 31 2E 32 2E 30 2D 62 2E 30 2B 31 32 32 35 2E
           35 32 33 65 66 03
CoLa B 02 02 02 02 00 00 00 2A 73 52 41 20 46 69 72 6D 77 61 72 65 56 65 72 73 69 6F 6E 20 00 14 31 2E 32 2E 30 2D 62 2E
       30 2B 31 32 32 35 2E 35 32 33 65 66 4B


12.5.1.4.8.3                   Read the device state [sRN DevSta]
This telegram reads the device state.
Possible status codes:
O   Reserved
O      Startup
       o    This state is used during the startup phase of the device. The state is a temporary state. It tells, that the
            user shall wait a given time (as specified in the documentation of the device) until the state will change to
            another value.
O      Service mode
       o    This state is used during service actions like software update, comprehensive parameter exchange or
            similar actions. The state does not tell whether the device is able to work properly. But it is a normal non
            critical state.
O      Normal operation
       o    This state signals the normal behavior of the device. The startup phase has ended and no errors or
            warnings occurred so far.
O      Suspended operation
       o    This state signals that any internal or environmental condition prohibits the adequate measurement.
O      Service recommended
       o    This state signals that the device is working properly. The measurement function is not affected by any
            circumstance. Hence the measuring function is as specified. But there is some issue which might be
            profitable to be handled by a service technician.
O      Service required
       o    This state signals, that a service technician is required. The device is still able to provide measured
            values but the results might be slightly affected by any circumstance.
O      Recoverable error
       o    This state signals a malfunction of the device. The measuring service is most probably disrupted. But the
            error might be fixed by a service technician.
O      Fatal error
       o    This state signals a malfunction of the device. The measuring service is most probably disrupted. But the
            error cannot be fixed by a service technician. The device must be replaced.




168        multiScan165                                                                                8028981/1X1R/2026-06-10 | SICK
                                                                                                 SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

Table 278: Telegram structure: sRN DevSta
                              Telegram structure: sRN DevSta


 Telegram             Description      Variable    Length        Additional details   Values CoLa A   Values CoLa B
    part                                                                                 (ASCII)         (Binary)
Command        Read                    String      3                                  sRN             73 52 4E
type
Command        Read the current device String      13                                 DevSta          44 65 76 53 74
               state                                                                                  61

Table 279: Example: sRN DevSta
          <STX>sRN{SPC}DevSta<ETX>
 CoLa     <STX>sRN DevSta<ETX>
  A       sRN DevSta
          02 73 52 4E 20 44 65 76 53 74 61 03
          02 02 02 02 00 00 00 0A 73 52 4E 20 44 65 76 53 74 61 5E
CoLa B 73 52 4E 20 44 65 76 53 74 61



Table 280: Telegram structure: sRA DevSta
                              Telegram structure: sRA DevSta


 Telegram             Description      Variable    Length        Additional details   Values CoLa A   Values CoLa B
    part                                                                                 (ASCII)         (Binary)
Command        Answer                  String      3                                  sRA             73 52 41
type
Command        Read the current device String      13                                 DevSta          44 65 76 53 74
               state                                                                                  61
Status         Code number             Enum_8      1        Reserved:                 0               00
code                                                        Startup:                  1               01
                                                            Service mode:             2               02
                                                            Normal operation:         3               03
                                                            Suspended operation:      4               04
                                                            Service recommended:      5               05
                                                            Service required:         6               06
                                                            Recoverable error:        7               07
                                                            Fatal error:              8               08

Table 281: Example: sRA DevSta

 CoLa     <STX>sRA{SPC}DevSta{SPC}3<ETX>
  A       02 73 52 41 20 44 65 76 53 74 61 20 33 03
CoLa B 02 02 02 02 00 00 00 0C 73 52 41 20 44 65 76 53 74 61 20 03 72


12.5.1.4.8.4                   Read the device state [sRN SCdevicestate]
This telegram reads the general device state.
Table 282: Telegram structure: sRN SCdevicestate
                           Telegram structure: sRN SCdevicestate


 Telegram             Description      Variable    Length        Additional details   Values CoLa A   Values CoLa B
    part                                                                                 (ASCII)         (Binary)
Command        Read                    String      3                                  sRN             73 52 4E
type




8028981/1X1R/2026-06-10 | SICK                                                                    multiScan165    169
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                           Telegram structure: sRN SCdevicestate


 Telegram             Description      Variable    Length           Additional details       Values CoLa A      Values CoLa B
    part                                                                                        (ASCII)            (Binary)
Command        Read the device state   String      13                                    SCdevicestate         53 43 64 65 76
                                                                                                               69 63 65 73 74
                                                                                                               61 74 65

Table 283: Example: sRN SCdevicestate
         <STX>sRN{SPC}SCdevicestate<ETX>
 CoLa    <STX>sRN SCdevicestate<ETX>
  A      sRN SCdevicestate
         02 73 52 4E 20 53 43 64 65 76 69 63 65 73 74 61 74 65 03
         02 02 02 02 00 00 00 11 73 52 4E 20 53 43 64 65 76 69 63 65 73 74 61 74 65 30
CoLa B 73 52 4E 20 53 43 64 65 76 69 63 65 73 74 61 74 65



Table 284: Telegram structure: sRA SCdevicestate
                           Telegram structure: sRA SCdevicestate


 Telegram             Description      Variable    Length           Additional details       Values CoLa A      Values CoLa B
    part                                                                                        (ASCII)            (Binary)
Command        Answer                  String      3                                     sRA                   73 52 41
type
Command        Read the device state   String      13                                    SCdevicestate         53 43 64 65 76
                                                                                                               69 63 65 73 74
                                                                                                               61 74 65
Status         Code number             Enum_8      1        Busy / logged-in:            0                     00
code                                                        Ready:                       1                     01
                                                            Error:                       2                     02

Table 285: Example: sRA SCdevicestate

 CoLa    <STX>sRA{SPC}SCdevicestate{SPC}1<ETX>
  A      02 73 52 41 20 53 43 64 65 76 69 63 65 73 74 61 74 65 20 31 03
CoLa B 02 02 02 02 00 00 00 13 73 52 41 20 53 43 64 65 76 69 63 65 73 74 61 74 65 20 01 1E


12.5.1.4.8.5                   Read device order number [sRN OrdNum]
This telegram reads the device order number which corresponds to the SICK part number of the device.
Table 286: Telegram structure: sRN OrdNum
                              Telegram structure: sRN OrdNum


 Telegram             Description      Variable    Length           Additional details       Values CoLa A      Values CoLa B
    part                                                                                        (ASCII)            (Binary)
Command        Read                    String      3                                     sRN                   73 52 4E
type
Command        Read device order       String      6                                     OrdNum                4F 72 64 4E 75
               number                                                                                          6D

Table 287: Example: sRN OrdNum
         <STX>sRN{SPC}OrdNum<ETX>
 CoLa    <STX>sRN OrdNum<ETX>
  A      sRN OrdNum
         02 73 52 4E 20 4F 72 64 4E 75 6D 03




170      multiScan165                                                                                8028981/1X1R/2026-06-10 | SICK
                                                                                               SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

          02 02 02 02 00 00 00 0A 73 52 4E 20 4F 72 64 4E 75 6D 40
CoLa B 73 52 4E 20 4F 72 64 4E 75 6D



Table 288: Telegram structure: sRA OrdNum
                              Telegram structure: sRA OrdNum


 Telegram             Description       Variable   Length         Additional details     Values CoLa A     Values CoLa B
    part                                                                                    (ASCII)           (Binary)
Command        Answer                   String     3                                    sRA               73 52 41
type
Command        Read device order        String     6                                    OrdNum            4F 72 64 4E 75
               number                                                                                     6D
Length         Number of characters     Uint_16    2                                    0h ... 20h        00 00 ... 00 20
               of the following order
               number
Order          Order number in 7 digits String     7                                    0000000 …         00 00 00 00 00
number                                                                                  9999999           00 00 … FF FF
                                                                                                          FF FF FF FF FF

Example: sRA OrdNum 1134610 (Order Number for picoScan150 Pro-1)
Table 289: Example for picoScan150 Pro-1: sRA OrdNum
 CoLa     <STX>sRA{SPC}OrdNum{SPC}7{SPC}1134610<ETX>
  A       02 73 52 41 20 4F 72 64 4E 75 6D 20 37 20 31 31 33 34 36 31 30 03
CoLa B 02 02 02 02 00 00 00 14 73 52 41 20 4F 72 64 4E 75 6D 20 00 07 31 31 33 34 36 31 30 58


12.5.1.4.8.6                   Read serial number [sRN SerialNumber]
Read the serial number of the device.
Table 290: Telegram structure: sRN SerialNumber
                           Telegram structure: sRN SerialNumber


 Telegram             Description       Variable   Length         Additional details     Values CoLa A     Values CoLa B
    part                                                                                    (ASCII)           (Binary)
Command        Read                     String     3                                    sRN               73 52 4E
type
Command        Read serial number of    String     12                                   SerialNumber      53 65 72 69 61
               the device                                                                                 6C 4E 75 6D 62
                                                                                                          65 72

Table 291: Example: sRN SerialNumber
          <STX>sRN{SPC}SerialNumber<ETX>
 CoLa     <STX>sRN SerialNumber<ETX>
  A       sRN SerialNumber
          02 73 52 4E 20 53 65 72 69 61 6C 4E 75 6D 62 65 72 03
          02 02 02 02 00 00 00 10 73 52 4E 20 53 65 72 69 61 6C 4E 75 6D 62 65 72 4C
CoLa B 73 52 4E 20 53 65 72 69 61 6C 4E 75 6D 62 65 72




8028981/1X1R/2026-06-10 | SICK                                                                         multiScan165    171
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

Table 292: Telegram structure: sRA SerialNumber
                           Telegram structure: sRA SerialNumber


 Telegram             Description       Variable   Length         Additional details      Values CoLa A        Values CoLa B
    part                                                                                     (ASCII)              (Binary)
Command        Answer                   String     3                                      sRA                 73 52 41
type
Command        Read serial number of    String     12                                     SerialNumber        53 65 72 69 61
               the device                                                                                     6C 4E 75 6D 62
                                                                                                              65 72
Length of      Number of characters     Uint_16    2                                      0 ... 8h            00 00 ... 00 08h
serial         of the serial number
number
Serial         Production period (year, String     8                                      (See example)       (See example)
number         calendar week, num-
               ber): YYWWxxxx

Table 293: Example: sRA SerialNumber

 CoLa    <STX>sRA{SPC}SerialNumber{SPC}8{SPC}23360024<ETX>
  A      02 73 52 41 20 53 65 72 69 61 6C 4E 75 6D 62 65 72 20 38 20 32 33 33 36 30 30 32 34 03
CoLa B 02 02 02 02 00 00 00 1B 73 52 41 20 53 65 72 69 61 6C 4E 75 6D 62 65 72 20 00 08 32 33 33 36 30 30 32 34 69


12.5.1.4.8.7                   Read device type [sRN DItype]
This telegram asks for the device type of the product familiy.
Table 294: Telegram structure: sRN DItype
                               Telegram structure: sRN DItype


 Telegram             Description       Variable   Length         Additional details      Values CoLa A        Values CoLa B
    part                                                                                     (ASCII)              (Binary)
Command        Read                     String     3                                      sRN                 73 52 4E
type
Command        Ask state                String     6                                      DItype              44 49 74 79 70
                                                                                                              65

Table 295: Example: sRN DItype
         <STX>sRN{SPC}DItype<ETX>
 CoLa    <STX>sRN DItype<ETX>
  A      sRN DItype
         02 73 52 4E 20 44 49 74 79 70 65 03
         02 02 02 02 00 00 00 0A 73 52 4E 20 44 49 74 79 70 65 5A
CoLa B 73 52 4E 20 44 49 74 79 70 65



Table 296: Telegram structure: sRA DItype
                               Telegram structure: sRA DItype


 Telegram             Description       Variable   Length         Additional details      Values CoLa A        Values CoLa B
    part                                                                                     (ASCII)              (Binary)
Command        Answer                   String     3                                      sRA                 73 52 41
type
Command        Ask state                String     6                                      DItype              44 49 74 79 70
                                                                                                              65




172      multiScan165                                                                               8028981/1X1R/2026-06-10 | SICK
                                                                                              SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                               Telegram structure: sRA DItype


 Telegram             Description        Variable   Length        Additional details         Values CoLa A       Values CoLa B
    part                                                                                        (ASCII)             (Binary)
Length of      Number of digits of       Uint_8     1                                        0d … 255d (0h … 00 … FF
type key       the following type code                                                       FFh)
               length
Device         Type code of the device String       (var.)                                   (Device type)      (Device type)
type

Table 297: sRA DItype Example for multiScan136:

 CoLa     <STX>sRA{SPC}DItype{SPC}C{SPC}multiScan136<ETX>
  A       02 73 52 41 20 44 49 74 79 70 65 20 43 20 6D 75 6C 74 69 53 63 61 6E 31 33 36 03
CoLa B 02 02 02 02 00 00 00 19 73 52 41 20 44 49 74 79 70 65 20 00 0C 6D 75 6C 74 69 53 63 61 6E 31 33 36 1B


12.5.1.4.8.8                   Read operating hours [sRN ODoprh]
Views the total number of operating hours during the lifetime of the device.
Table 298: Telegram structure: sRN ODoprh
                              Telegram structure: sRN ODoprh


 Telegram             Description        Variable   Length        Additional details         Values CoLa A       Values CoLa B
    part                                                                                        (ASCII)             (Binary)
Command        Read                      String     3                                        sRN                73 52 4E
type
Command        Read operating hours      String     6                                        ODoprh             4F 44 6F 70 72
                                                                                                                68

Table 299: Example: sRN ODoprh
          <STX>sRN{SPC}ODoprh<ETX>
 CoLa     <STX>sRN ODoprh<ETX>
  A       sRN ODoprh
          02 73 52 4E 20 4F 44 6F 70 72 68 03
          02 02 02 02 00 00 00 0A 73 52 4E 20 4F 44 6F 70 72 68 41
CoLa B 73 52 4E 20 4F 44 6F 70 72 68



Table 300: Telegram structure: sRA ODoprh
                              Telegram structure: sRA ODoprh


 Telegram             Description        Variable   Length        Additional details         Values CoLa A       Values CoLa B
    part                                                                                        (ASCII)             (Binary)
Command        Answer                    String     3                                        sRA                73 52 41
type
Command        Read operating hours      String     6                                        ODoprh             4F 44 6F 70 72
                                                                                                                68
Value          Operating hours in 1/10   Uint_32    4                                        0h …               00 00 00 00 …
               h                                                                             FFFFFFFFh          FF FF FF FF

Table 301: Example: sRA ODoprh
 CoLa     <STX>sRA{SPC}ODoprh{SPC}1B50B<ETX>
  A       02 73 52 41 20 4F 44 6F 70 72 68 20 31 42 35 30 42 03
CoLa B 02 02 02 02 00 00 00 0F 73 52 41 20 4F 44 6F 70 72 68 20 00 01 B5 0B D1

Calculation of the value: 1B50B (hex) → 111883 (dez) × 1/10 h = 11188.3 h



8028981/1X1R/2026-06-10 | SICK                                                                               multiScan165       173
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

12.5.1.4.8.9                   Read operating hours since last power on [sRN ODopdaily]
Shows the runtime duration since the last power on of the device.
Table 302: Telegram structure: sRN ODopdaily
                             Telegram structure: sRN ODopdaily


 Telegram             Description        Variable   Length       Additional details   Values CoLa A       Values CoLa B
    part                                                                                 (ASCII)             (Binary)
Command        Read                      String     3                                 sRN                73 52 4E
type
Command        Read operating hours      String     9                                 ODopdaily          4F 44 6F 70 64
                                                                                                         61 69 6C 79

Table 303: Example: sRN ODopdaily
         <STX>sRN{SPC}ODopdaily<ETX>
 CoLa    <STX>sRN ODopdaily<ETX>
  A      sRN ODopdaily
         02 73 52 4E 20 4F 44 6F 70 64 61 69 6C 79 03
         02 02 02 02 00 00 00 0D 73 52 4E 20 4F 44 6F 70 64 61 69 6C 79 22
CoLa B 73 52 4E 20 4F 44 6F 70 64 61 69 6C 79



Table 304: Telegram structure: sRA ODopdaily
                             Telegram structure: sRA ODopdaily


 Telegram             Description        Variable   Length       Additional details   Values CoLa A       Values CoLa B
    part                                                                                 (ASCII)             (Binary)
Command        Answer                    String     3                                 sRA                73 52 41
type
Command        Read operating hours      String     9                                 ODopdaily          4F 44 6F 70 64
               since last power on                                                                       61 69 6C 79
Value          Operating hours in 1/10   Uint_32    4                                 0h …               00 00 00 00 …
               h                                                                      FFFFFFFFh          FF FF FF FF

Table 305: Example: sRA ODopdaily
 CoLa    <STX>sRA{SPC}ODopdaily{SPC}424772B8<ETX>
  A      02 73 52 41 20 4F 44 6F 70 72 68 20 34 32 34 37 37 32 42 38 03
CoLa B 02 02 02 02 00 00 00 12 73 52 41 20 4F 44 6F 70 72 68 20 42 47 72 B8 D7


12.5.1.4.8.10                  Read power on counter [sRN ODpwrc]
Shows the number of power on cycles.
Table 306: Telegram structure: sRN ODpwrc
                              Telegram structure: sRN ODpwrc


 Telegram             Description        Variable   Length       Additional details   Values CoLa A       Values CoLa B
    part                                                                                 (ASCII)             (Binary)
Command        Read                      String     3                                 sRN                73 52 4E
type
Command        Read power on counter     String     6                                 ODpwrc             4F 44 70 77 72
                                                                                                         63




174      multiScan165                                                                          8028981/1X1R/2026-06-10 | SICK
                                                                                         SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

Table 307: Example: sRN ODpwrc
          <STX>sRN{SPC}ODpwrc<ETX>
 CoLa     <STX>sRN ODpwrc<ETX>
  A       sRN ODpwrc
          02 73 52 4E 20 4F 44 70 77 72 63 03
          02 02 02 02 00 00 00 0A 73 52 4E 20 4F 44 70 77 72 63 52
CoLa B 73 52 4E 20 4F 44 70 77 72 63



Table 308: Telegram structure: sRA ODpwrc
                               Telegram structure: sRA ODpwrc


 Telegram              Description      Variable   Length         Additional details   Values CoLa A     Values CoLa B
    part                                                                                  (ASCII)           (Binary)
Command         Answer                  String     3                                   sRA              73 52 41
type
Command         Read power on counter   String     6                                   ODpwrc           4F 44 70 77 72
                                                                                                        63
Value           Power on counter        Uint_32    4                                   0h …             00 00 00 00 …
                                                                                       FFFFFFFFh        FF FF FF FF

Table 309: Example: sRA ODpwrc

 CoLa     <STX>sRA{SPC}ODpwrc{SPC}9A<ETX>
  A       02 73 52 41 20 4F 44 70 77 72 63 20 39 41 03
CoLa B 02 02 02 02 00 00 00 0F 73 52 41 20 4F 44 70 77 72 63 20 00 00 00 9A E7


12.5.1.4.8.11                   Read temperature [sRN OPcurtmpdev]
With this command the internal temperature of the device can be identified. Please note that it does not give an
indication of the current ambient temperature.
Table 310: Telegram structure: sRN OPcurtmpdev
                            Telegram structure: sRN OPcurtmpdev


 Telegram              Description      Variable   Length         Additional details   Values CoLa A     Values CoLa B
    part                                                                                  (ASCII)           (Binary)
Command         Read                    String     3                                   sRN              73 52 4E
type
Command         Read temperature of     String     11                                  OPcurtmpdev      4F 50 63 75 72
                the device                                                                              74 6D 70 64 65
                                                                                                        76

Table 311: Example: sRN OPcurtmpdev
          <STX>sRN{SPC}OPcurtmpdev<ETX>
 CoLa     <STX>sRN OPcurtmpdev<ETX>
  A       sRN OPcurtmpdev
          02 73 52 4E 20 4F 50 63 75 72 74 6D 70 64 65 76 03
          02 02 02 02 00 00 00 0F 73 52 4E 20 4F 50 63 75 72 74 6D 70 64 65 76 2A
CoLa B 73 52 4E 20 4F 50 63 75 72 74 6D 70 64 65 76




8028981/1X1R/2026-06-10 | SICK                                                                       multiScan165   175
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

Table 312: Telegram structure: sRA OPcurtmpdev
                             Telegram structure: sRA OPcurtmpdev


 Telegram               Description       Variable   Length         Additional details     Values CoLa A       Values CoLa B
    part                                                                                      (ASCII)             (Binary)
Command         Answer                    String     3                                     sRA                73 52 41
type
Command         Read temperature of       String     11                                    OPcurtmpdev        4F 50 63 75 72
                the device                                                                                    74 6D 70 64 65
                                                                                                              76
Tempera-        [°C]                      Real as    4        (-50°C … +100°C)             C2480000h …        C2 48 00 00 …
ture data                                 float                                            42C80000h          42 C8 00 00
                                          accord-
                                          ing to
                                          IEEE754

Example: sRA OPcurtmpdev (35°C)
Table 313: Example: sRA OPcurtmpdev

 CoLa    <STX>sRA{SPC}OPcurtmpdev{SPC}420C0000<ETX>
  A      02 73 52 41 20 4F 50 63 75 72 74 6D 70 64 65 76 20 34 32 30 43 30 30 30 30 03
CoLa B 02 02 02 02 00 00 00 14 73 52 41 20 4F 50 63 75 72 74 6D 70 64 65 76 20 42 0C 00 00 4B


12.5.1.4.8.12                    Set device name [sWN LocationName]
Give the device a specific description name such as its location.
Table 314: Telegram structure: sWN LocationName
                             Telegram structure: sWN LocationName
                               (User level 'Maintenance' required)

 Telegram               Description       Variable   Length         Additional details     Values CoLa A       Values CoLa B
    part                                                                                      (ASCII)             (Binary)
Command         Write                     String     3                                     sWN                73 57 4E
type
Command         Set device name           String     12                                    LocationName       4C 6F 63 61 74
                                                                                                              69 6F 6E 4E 61
                                                                                                              6D 65
Value           Number of characters      Uint_16    2                                     0d … +16d (0h … 00 00 … 00 10
                of the following device                                                    10h )
                name
Value           Device name               String     32                                    [Device name]      [Device name]

Table 315: Example: sWN LocationName +9 LongRange
         <STX>sWN{SPC}LocationName{SPC}+9{SPC}LongRange<ETX>
 CoLa    <STX>sWN LocationName +9 LongRange<ETX>
  A      sWN LocationName +9 LongRange
         02 73 57 4E 20 4C 6F 63 61 74 69 6F 6E 4E 61 6D 65 20 39 20 4C 6F 6E 67 52 61 6E 67 65 03
         02 02 02 02 00 00 00 1D 73 57 4E 20 4C 6F 63 61 74 69 6F 6E 4E 61 6D 65 20 00 09 4C 6F 6E 67 52 61 6E 67 65 2C
CoLa B 73 57 4E 20 4C 6F 63 61 74 69 6F 6E 4E 61 6D 65 20 00 09 4C 6F 6E 67 52 61 6E 67 65




176      multiScan165                                                                               8028981/1X1R/2026-06-10 | SICK
                                                                                              SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

Table 316: Telegram structure: sWA LocationName
                            Telegram structure: sWA LocationName


 Telegram              Description      Variable   Length         Additional details    Values CoLa A     Values CoLa B
    part                                                                                   (ASCII)           (Binary)
Command         Answer                  String     3                                   sWA               73 57 41
type
Command         Set device name         String     12                                  LocationName      4C 6F 63 61 74
                                                                                                         69 6F 6E 4E 61
                                                                                                         6D 65

Table 317: Example: sWA LocationName
 CoLa     <STX>sWA{SPC}LocationName<ETX>
  A       02 73 57 41 20 4C 6F 63 61 74 69 6F 6E 4E 61 6D 65 03
CoLa B 02 02 02 02 00 00 00 11 73 57 41 20 4C 6F 63 61 74 69 6F 6E 4E 61 6D 65 20 7F


12.5.1.4.8.13                   Read device name [sRN LocationName]
Read the given name of the device (Default is the serial number of the device).
Table 318: Telegram structure: sRN LocationName
                            Telegram structure: sRN LocationName


 Telegram              Description      Variable   Length         Additional details    Values CoLa A     Values CoLa B
    part                                                                                   (ASCII)           (Binary)
Command         Read                    String     3                                   sRN               73 52 4E
type
Command         Read device name        String     12                                  LocationName      4C 6F 63 61 74
                                                                                                         69 6F 6E 4E 61
                                                                                                         6D 65

Table 319: Example: sRN LocationName
          <STX>sRN{SPC}LocationName<ETX>
 CoLa     <STX>sRN LocationName<ETX>
  A       sRN LocationName
          02 73 52 4E 20 4C 6F 63 61 74 69 6F 6E 4E 61 6D 65 03
          02 02 02 02 00 00 00 10 73 52 4E 20 4C 6F 63 61 74 69 6F 6E 4E 61 6D 65 55
CoLa B 73 52 4E 20 4C 6F 63 61 74 69 6F 6E 4E 61 6D 65



Table 320: Telegram structure: sRA LocationName
                            Telegram structure: sRA LocationName


 Telegram              Description      Variable   Length         Additional details    Values CoLa A     Values CoLa B
    part                                                                                   (ASCII)           (Binary)
Find complete telegram structure of the answer in see table 314, page 176


12.5.1.4.8.14                   Initiate an acoustic or visual signal for a defined period of time [sMN FindMe]
This command can be used to make the device easier to find.




8028981/1X1R/2026-06-10 | SICK                                                                        multiScan165   177
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

Table 321: Telegram structure: sMN FindMe
                                Telegram structure: sMN FindMe
                             (User level 'Authorized client' required)

 Telegram              Description         Variable   Length         Additional details   Values CoLa A       Values CoLa B
    part                                                                                     (ASCII)             (Binary)
Command         Method                    String      3                                   sMN                73 4D 4E
type
Command         Initiate an acoustic or   String      11                                  FindMe             46 69 6E 64 4D
                visual signal                                                                                65
Period of       Duration in seconds       Uint_16     2                                   0d … 65535d        00 ... FF FF
time                                                                                      (0h .. FF FF)

Table 322: Example: sMN FindMe
            <STX>sMN{SPC}FindMe{SPC}1<ETX>
 CoLa       <STX>sMN FindMe 1<ETX>
  A         sMN FindMe 1
            02 73 4D 4E 20 46 69 6E 64 4D 65 20 31 03
            02 02 02 02 00 00 00 0D 73 4D 4E 20 46 69 6E 64 4D 65 20 01 7C
CoLa B 73 4D 4E 20 46 69 6E 64 4D 65 20 01



Table 323: Telegram structure: sAN FindMe
                                Telegram structure: sAN FindMe


 Telegram              Description         Variable   Length         Additional details   Values CoLa A       Values CoLa B
    part                                                                                     (ASCII)             (Binary)
Command         Answer                    String      3                                   sAN                73 41 4E
type
Command         Initiate an acoustic or   String      11                                  FindMe             46 69 6E 64 4D
                visual signal                                                                                65

Table 324: Example: sAN FindMe

 CoLa       <STX>sAN{SPC}Findme<ETX>
  A         02 73 41 4E 20 46 69 6E 64 4D 65 03
CoLa B 02 02 02 02 00 00 00 0B 73 41 4E 20 46 69 6E 64 4D 65 20 71


12.5.1.4.8.15                    Read date of last permanent save [sRN DIpara]
This command reads the date at which the last permanent save (see "Save parameters permanently [sMN mEEwri-
teall]", page 119) was executed.
Table 325: Telegram structure: sRN DIpara
                                 Telegram structure: sRN DIpara


 Telegram              Description         Variable   Length         Additional details   Values CoLa A       Values CoLa B
    part                                                                                     (ASCII)             (Binary)
Command         Read                      String      3                                   sRN                73 52 4E
type
Command         Read date of last per-    String      6                                   DIpara             44 49 70 61 72
                manent save                                                                                  61




178         multiScan165                                                                           8028981/1X1R/2026-06-10 | SICK
                                                                                             SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

Table 326: Example: sRN DIpara
          <STX>sRN{SPC}DIpara<ETX>
 CoLa     <STX>sRN DIpara<ETX>
  A       sRN DIpara
          02 73 52 4E 20 44 49 70 61 72 61 03
          02 02 02 02 00 00 00 4E 73 52 4E 20 44 49 70 61 72 61 40
CoLa B 73 52 4E 20 44 49 70 61 72 61



Table 327: Telegram structure: sRA DIpara
                                Telegram structure: sRA DIpara


 Telegram              Description       Variable   Length         Additional details    Values CoLa A       Values CoLa B
    part                                                                                    (ASCII)             (Binary)
Command         Answer                   String     3                                   sRA                 73 52 41
type
Command         Read date of last per-   String     6                                   DIpara              44 49 70 61 72
                manent save                                                                                 61
Reserved        -                        Uint_8     1        Always:                    Ah                  0A
Date of last DD.MM.YYYY                  Flex-      10                                  (see example)       (see example)
permanent                                String
save

Table 328: Example: sRA DIpara

 CoLa     <STX>sRA{SPC}DIpara{SPC}A{SPC}09.01.2024<ETX>
  A       02 73 52 41 20 44 49 70 61 72 61 20 41 20 30 39 2E 30 31 2E 32 30 32 34 03
CoLa B 02 02 02 02 00 00 00 17 73 52 41 20 44 49 70 61 72 61 20 00 0A 30 39 2E 30 31 2E 32 30 32 34 69


12.5.1.4.8.16                    Read time of last permanent save [sRN DIparatm]
This command reads the time at which the last permanent save (see "Save parameters permanently [sMN mEEwri-
teall]", page 119) was executed.
Table 329: Telegram structure: sRN DIparatm
                               Telegram structure: sRN DIparatm


 Telegram              Description       Variable   Length         Additional details    Values CoLa A       Values CoLa B
    part                                                                                    (ASCII)             (Binary)
Command         Read                     String     3                                   sRN                 73 52 4E
type
Command         Read time of last per-   String     8                                   DIparatm            44 49 70 61 72
                manent save                                                                                 61 74 6D

Table 330: Example: sRN DIparatm
          <STX>sRN{SPC}DIparatm<ETX>
 CoLa     <STX>sRN DIparatm<ETX>
  A       sRN DIparatm
          02 73 52 4E 20 44 49 70 61 72 61 74 6D 03
          02 02 02 02 00 00 00 4E 73 52 4E 20 44 49 70 61 72 61 74 6D 59
CoLa B 73 52 4E 20 44 49 70 61 72 61 74 6D




8028981/1X1R/2026-06-10 | SICK                                                                           multiScan165   179
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

Table 331: Telegram structure: sRA DIparatm
                                  Telegram structure: sRA DIparatm


 Telegram              Description          Variable   Length         Additional details          Values CoLa A         Values CoLa B
    part                                                                                             (ASCII)               (Binary)
Command         Answer                     String      3                                          sRA                  73 52 41
type
Command         Read time of last per-     String      8                                          DIparatm             44 49 70 61 72
                manent save                                                                                            61 74 6D
Reserved        -                          Uint_16     2        Always:                           5h                   00 05
Time of         HH:MM                      String      5                                          (see example)        (see example)
last per-
manent
save

Table 332: Example: sRA DIparatm

 CoLa       <STX>sRA{SPC}DIparatm{SPC}5{SPC}12:28<ETX>
  A         02 73 52 41 20 44 49 70 61 72 61 74 6D 20 35 20 31 32 3A 32 38 03
CoLa B 02 02 02 02 00 00 00 14 73 52 41 20 44 49 70 61 72 61 74 6D 20 00 05 31 32 3A 32 38 40


12.5.1.4.8.17                      Read the current device temperature alarm status [sRN temperatureAlarmStatus]
Current device temperature alarm status. If true, the configured temperature alarm is active.
Table 333: Telegram structure: sRN temperatureAlarmStatus
                           Telegram structure: sRN temperatureAlarmStatus
                                (User level 'Authorized client' required)

 Telegram              Description          Variable   Length         Additional details          Values CoLa A         Values CoLa B
    part                                                                                             (ASCII)               (Binary)
Command         Read                       String      3                                          sRN                  73 52 4E
type
Command         Device temperature         String      22                                         temperatureA-        74 65 6D 70 65
                alarm status                                                                      larmStatus           72 61 74 75 72
                                                                                                                       65 41 6C 61 72
                                                                                                                       6D 53 74 61 74
                                                                                                                       75 73

Table 334: Example: sRN temperatureAlarmStatus
            <STX>sRN{SPC}temperatureAlarmStatus<ETX>
 CoLa       <STX>sRN temperatureAlarmStatus<ETX>
  A         sRN temperatureAlarmStatus
            02 73 52 4E 20 74 65 6D 70 65 72 61 74 75 72 65 41 6C 61 72 6D 53 74 61 74 75 73 03
            02 02 02 02 00 00 00 1A 73 52 4E 20 74 65 6D 70 65 72 61 74 75 72 65 41 6C 61 72 6D 53 74 61 74 75 73 44
CoLa B 73 52 4E 20 74 65 6D 70 65 72 61 74 75 72 65 41 6C 61 72 6D 53 74 61 74 75 73


Table 335: Telegram structure: sRA temperatureAlarmStatus
                           Telegram structure: sRA temperatureAlarmStatus


 Telegram              Description          Variable   Length         Additional details          Values CoLa A         Values CoLa B
    part                                                                                             (ASCII)               (Binary)
Command         Answer                     String      3                                          sRA                  73 52 41
type




180         multiScan165                                                                                     8028981/1X1R/2026-06-10 | SICK
                                                                                                       SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                        Telegram structure: sRA temperatureAlarmStatus


 Telegram               Description      Variable   Length         Additional details          Values CoLa A        Values CoLa B
    part                                                                                          (ASCII)              (Binary)
Command         Device temperature      String      22                                        temperatureA-        74 65 6D 70 65
                alarm status                                                                  larmStatus           72 61 74 75 72
                                                                                                                   65 41 6C 61 72
                                                                                                                   6D 53 74 61 74
                                                                                                                   75 73
Data            Alarm state             Bool_1      1        Disbaled:                        0d (00h)             00 ... 01
                                                             Enabled:                         +1d (01h)

Table 336: Example: sRA temperatureAlarmStatus - Temperature alarm status is off. The device runs in the defined temperature
range

 CoLa     <STX>sRA{SPC}temperatureAlarmStatus{SPC}0<ETX>
  A       02 73 52 41 20 74 65 6D 70 65 72 61 74 75 72 65 41 6C 61 72 6D 53 74 61 74 75 73 20 30 03
CoLa B 02 02 02 02 00 00 00 1C 73 52 41 20 74 65 6D 70 65 72 61 74 75 72 65 41 6C 61 72 6D 53 74 61 74 75 73 20 00 6B


12.5.1.4.8.18                    Set device temperature alarm configuration [sWN temperatureAlarmConfiguration]
Sets the upper and lower threshold for the temperature alarm status.
Table 337: Telegram structure: sWN temperatureAlarmConfiguration
                  Telegram structure: sWN temperatureAlarmConfiguration
                          (User level 'Authorized client' required)

 Telegram               Description      Variable   Length         Additional details          Values CoLa A        Values CoLa B
    part                                                                                          (ASCII)              (Binary)
Command         Write                   String      3                                         sWN                  73 57 4E
type
Command         Device temperature      String      29                                        temperatureA-        74 65 6D 70 65
                alarm configuration                                                           larmConfigura-       72 61 74 75 72
                                                                                              tion                 65 41 6C 61 72
                                                                                                                   6D 43 6F 6E 66
                                                                                                                   69 67 75 72 61
                                                                                                                   74 69 6F 6E
Data 1          Upper threshold [°C]    Int_8       1        Default: 55                      -128d ... +127d      80 ... 7F
                                                                                              (80h ... 7Fh)
Data 2          Lower threshold [°C]    Int_8       1        Default: 50                      -128d ... +127d      80 ... 7F
                                                                                              (80h ... 7Fh)

Table 338: Example: sWN temperatureAlarmConfiguration - Set the upper threshold to 55 °C and the lower threshold to 50 °C
          <STX>sWN{SPC}temperatureAlarmConfiguration{SPC}37{SPC}32<ETX>
          <STX>sWN temperatureAlarmConfiguration 37 32<ETX>
 CoLa
  A       sWN temperatureAlarmConfiguration 37 32
          02 73 57 4E 20 74 65 6D 70 65 72 61 74 75 72 65 41 6C 61 72 6D 43 6F 6E 66 69 67 75 72 61 74 69 6F 6E 20 33 37
          20 33 32 03
          02 02 02 02 00 00 00 24 73 52 4E 20 74 65 6D 70 65 72 61 74 75 72 65 41 6C 61 72 6D 43 6F 6E 66 69 67 75 72 61 74 69
          6F 6E 20 37 32 00
CoLa B
          73 52 4E 20 74 65 6D 70 65 72 61 74 75 72 65 41 6C 61 72 6D 43 6F 6E 66 69 67 75 72 61 74 69 6F 6E 20 37 32




8028981/1X1R/2026-06-10 | SICK                                                                                  multiScan165   181
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

Table 339: Telegram structure: sWA temperatureAlarmConfiguration
                  Telegram structure: sWA temperatureAlarmConfiguration


 Telegram              Description     Variable   Length          Additional details         Values CoLa A       Values CoLa B
    part                                                                                        (ASCII)             (Binary)
Command         Answer                 String     3                                          sWA                 73 57 41
type
Command         Device temperature     String     29                                         temperatureA-       74 65 6D 70 65
                alarm configuration                                                          larmConfigura-      72 61 74 75 72
                                                                                             tion                65 41 6C 61 72
                                                                                                                 6D 43 6F 6E 66
                                                                                                                 69 67 75 72 61
                                                                                                                 74 69 6F 6E

Table 340: Example: sWA temperatureAlarmConfiguration

 CoLa    <STX>sWA{SPC}temperatureAlarmConfiguration<ETX>
  A      02 73 57 41 20 74 65 6D 70 65 72 61 74 75 72 65 41 6C 61 72 6D 43 6F 6E 66 69 67 75 72 61 74 69 6F 6E03
         02 02 02 02 00 00 00 22 73 57 41 20 74 65 6D 70 65 72 61 74 75 72 65 41 6C 61 72 6D 43 6F 6E 66 69 67 75 72 61 74 69
CoLa B
         6F 6E 20 0A


12.5.1.4.8.19                   Read device temperature alarm configuration [sRN temperatureAlarmConfigura-
                                tion]
Returns the upper and lower threshold for the temperature alarm status.
Table 341: Telegram structure: sRN temperatureAlarmConfiguration
                  Telegram structure: sRN temperatureAlarmConfiguration
                          (User level 'Authorized client' required)

 Telegram              Description     Variable   Length          Additional details         Values CoLa A       Values CoLa B
    part                                                                                        (ASCII)             (Binary)
Command         Read                   String     3                                          sRN                 73 52 4E
type
Command         Device temperature     String     29                                         temperatureA-       74 65 6D 70 65
                alarm configuration                                                          larmConfigura-      72 61 74 75 72
                                                                                             tion                65 41 6C 61 72
                                                                                                                 6D 43 6F 6E 66
                                                                                                                 69 67 75 72 61
                                                                                                                 74 69 6F 6E

Table 342: Example: sRN temperatureAlarmConfiguration
         <STX>sRN{SPC}temperatureAlarmConfiguration<ETX>
 CoLa    <STX>sRN temperatureAlarmConfiguration<ETX>
  A      sRN temperatureAlarmConfiguration
         02 73 52 4E 20 74 65 6D 70 65 72 61 74 75 72 65 41 6C 61 72 6D 43 6F 6E 66 69 67 75 72 61 74 69 6F 6E 03
         02 02 02 02 00 00 00 21 73 52 4E 20 74 65 6D 70 65 72 61 74 75 72 65 41 6C 61 72 6D 43 6F 6E 66 69 67 75 72 61 74 69
         6F 6E 20
CoLa B
         73 52 4E 20 74 65 6D 70 65 72 61 74 75 72 65 41 6C 61 72 6D 43 6F 6E 66 69 67 75 72 61 74 69 6F 6E 20


Table 343: Telegram structure: sRA temperatureAlarmConfiguration
                  Telegram structure: sRA temperatureAlarmConfiguration


 Telegram              Description     Variable   Length          Additional details         Values CoLa A       Values CoLa B
    part                                                                                        (ASCII)             (Binary)
Command         Answer                 String     3                                          sRA                 73 52 41
type




182      multiScan165                                                                                 8028981/1X1R/2026-06-10 | SICK
                                                                                                SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                 Telegram structure: sRA temperatureAlarmConfiguration


    Telegram           Description        Variable   Length          Additional details        Values CoLa A         Values CoLa B
       part                                                                                       (ASCII)               (Binary)
Command        Device temperature        String      29                                        temperatureA-        74 65 6D 70 65
               alarm configuration                                                             larmConfigura-       72 61 74 75 72
                                                                                               tion                 65 41 6C 61 72
                                                                                                                    6D 43 6F 6E 66
                                                                                                                    69 67 75 72 61
                                                                                                                    74 69 6F 6E
Data 1         Upper threshold [°C]      Int_8       1        Default: 55                      -128d ... +127d      80 ... 7F
                                                                                               (80h ... 7Fh)
Data 2         Lower threshold [°C]      Int_8       1        Default: 50                      -128d ... +127d      80 ... 7F
                                                                                               (80h ... 7Fh)

Table 344: Example: sRA temperatureAlarmConfiguration - 55 °C upper threshold and 50 °C lower threshold
           <STX>sRA{SPC}temperatureAlarmConfiguration{SPC}37{SPC}32<ETX>
    CoLa
     A     02 73 52 41 20 74 65 6D 70 65 72 61 74 75 72 65 41 6C 61 72 6D 43 6F 6E 66 69 67 75 72 61 74 69 6F 6E 20 33 37 20 33
           32 03
           02 02 02 02 00 00 00 24 73 52 41 20 74 65 6D 70 65 72 61 74 75 72 65 41 6C 61 72 6D 43 6F 6E 66 69 67 75 72 61 74 69
CoLa B
           6F 6E 20 37 32 0A


12.5.1.4.9               Interfaces


12.5.1.4.9.1                    Set IP address [sWN EIIpAddr]

NOTE
O      Save permanently to set values. Changes will be active after rebooting the device.
O      Settings must correspond with network in which scanner is used. Else device cannot be found any more.

Table 345: Telegram structure: sWN EIIpAddr
                              Telegram structure: sWN EIIpAddr
                            (User level 'Authorized client' required)

    Telegram           Description        Variable   Length          Additional details        Values CoLa A         Values CoLa B
       part                                                                                       (ASCII)               (Binary)
Command        Write                     String      3                                         sWN                  73 57 4E
type
Command        Set IP address            String      8                                         EIIpAddr             45 49 49 50 41
                                                                                                                    64 64 72
                                                              First part of IP adress          0 …+255d (00 ... 00 … FF
                                                                                               FF)
                                                              Second part of IP adress         0 …+255d (00 ... 00 … FF
                                                                                               FF)
IP address     Set values                Uint_8      1
                                                              Third part of IP adress          0 …+255d (00 ... 00 … FF
                                                                                               FF)
                                                              Fourth part of IP adress         0 …+255d (00 ... 00 … FF
                                                                                               FF)

Table 346: Example: sWN EIIpAddr 192.168.0.2
           <STX>sWN{SPC}EIIpAddr{SPC}C0{SPC}A8{SPC}0{SPC}2<ETX>
    CoLa   <STX>sWN EIIpAddr C0 A8 0 2<ETX>
     A     sWN EIIpAddr C0 A8 0 2
           02 73 57 4E 20 45 49 49 70 41 64 64 72 20 43 30 20 41 38 20 30 20 32 03




8028981/1X1R/2026-06-10 | SICK                                                                                   multiScan165   183
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

         02 02 02 02 00 00 00 11 73 57 4E 20 45 49 49 70 41 64 64 72 20 C0 A8 00 02 06
CoLa B 73 57 4E 20 45 49 49 70 41 64 64 72 20 C0 A8 00 02



Table 347: Telegram structure: sWA EIIpAddr
                                Telegram structure: sWA EIIpAddr


 Telegram             Description         Variable   Length        Additional details    Values CoLa A       Values CoLa B
    part                                                                                    (ASCII)             (Binary)
Command        Answer                    String      3                                   sWA                73 57 41
type
Command        Set IP address            String      8                                   EIIpAddr           45 49 49 50 41
                                                                                                            64 64 72

Table 348: Example: sWA EIIpAddr

 CoLa    <STX>sWA{SPC}EIIpAddr<ETX>
  A      02 73 57 41 20 45 49 49 70 41 64 64 72 03
CoLa B 02 02 02 02 00 00 00 0D 73 57 41 20 45 49 49 70 41 64 64 72 20 63


12.5.1.4.9.2                     Read IP address [sRN EIIpAddr]
Read the IP address of the device.
Table 349: Telegram structure: sRN EIIpAddr
                                Telegram structure: sRN EIIpAddr


 Telegram             Description         Variable   Length        Additional details    Values CoLa A       Values CoLa B
    part                                                                                    (ASCII)             (Binary)
Command        Read                      String      3                                   sRN                73 52 4E
type
Command        Read IP address           String      8                                   EIIpAddr           45 49 49 50 41
                                                                                                            64 64 72

Table 350: Example: sRN EIIpAddr
         <STX>sRN{SPC}EIIpAddr<ETX>
 CoLa    <STX>sRN EIIpAddr<ETX>
  A      sRN EIIpAddr
         02 73 52 4E 20 45 49 49 70 41 64 64 72 03
         02 02 02 02 00 00 00 0C 73 52 4E 20 45 49 49 70 41 64 64 72 49
CoLa B 73 52 4E 20 45 49 49 70 41 64 64 72



Table 351: Telegram structure: sRA EIIpAddr
                                Telegram structure: sRA EIIpAddr


 Telegram             Description         Variable   Length        Additional details    Values CoLa A       Values CoLa B
    part                                                                                    (ASCII)             (Binary)
Command        Answer                    String      3                                   sRA                73 52 41
type
Command        Read IP address           String      8                                   EIIpAddr           45 49 49 50 41
                                                                                                            64 64 72




184      multiScan165                                                                             8028981/1X1R/2026-06-10 | SICK
                                                                                            SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                               Telegram structure: sRA EIIpAddr


 Telegram             Description        Variable   Length          Additional details   Values CoLa A      Values CoLa B
    part                                                                                    (ASCII)            (Binary)
                                                             First part of IP address    0 …+255d (00 … 00 … FF
                                                                                         FF)
                                                             Second part of IP address   0 …+255d (00 … 00 … FF
                                                                                         FF)
IP address     Default: 192.168.0.1     Uint_8      1
                                                             Third part of IP address    0 …+255d (00 … 00 … FF
                                                                                         FF)
                                                             Fourth part of IP address   0 …+255d (00 … 00 … FF
                                                                                         FF)

Table 352: Example: sRA EIIpAddr 192.168.0.2

 CoLa     <STX>sRA{SPC}EIIpAddr{SPC}C0{SPC}A8{SPC}00{SPC}02<ETX>
  A       02 73 57 41 20 45 49 49 70 41 64 64 72 20 C0 20 A8 20 00 20 02 03
CoLa B 02 02 02 02 00 00 00 11 73 52 41 20 45 49 49 70 41 64 64 72 20 C0 A8 00 02 0C


12.5.1.4.9.3                     Read IP address assigned by DHCP [sRN EIIpAddrDHCP]

NOTE
DHCP needs to be set as mode for ethernet assignment.

Table 353: Telegram structure: sRN EIIpAddrDHCP
                            Telegram structure: sRN EIIpAddrDHCP


 Telegram             Description        Variable   Length          Additional details   Values CoLa A      Values CoLa B
    part                                                                                    (ASCII)            (Binary)
Command        Read                     String      3                                    sRN               73 52 4E
type
Command        Read IP address          String      12                                   EIIpAddrDHCP      45 49 49 70 41
               assigned by DHCP                                                                            64 64 72 44 48
                                                                                                           43 50

Table 354: Example: srN EIIpAddrDHCP
          <STX>sRN{SPC}EIIpAddrDHCP<ETX>
 CoLa     <STX>sRN EIIpAddrDHCP<ETX>
  A       sRN EIIpAddrDHCP
          02 73 57 4E 20 45 49 49 70 41 64 64 72 44 48 43 50 03
          02 02 02 02 00 00 00 10 73 52 4E 20 45 49 49 70 41 64 64 72 44 48 43 50 56
CoLa B 73 52 4E 20 45 49 49 70 41 64 64 72 44 48 43 50



Table 355: Telegram structure: sRA EIIpAddrDHCP
                            Telegram structure: sRA EIIpAddrDHCP


 Telegram             Description        Variable   Length          Additional details   Values CoLa A      Values CoLa B
    part                                                                                    (ASCII)            (Binary)
Command        Answer                   String      3                                    sRA               73 52 41
type
Command        Read IP address          String      12                                   EIIpAddrDHCP      45 49 49 70 41
               assigned by DHCP                                                                            64 64 72 44 48
                                                                                                           43 50




8028981/1X1R/2026-06-10 | SICK                                                                          multiScan165   185
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                            Telegram structure: sRA EIIpAddrDHCP


 Telegram              Description        Variable   Length             Additional details   Values CoLa A        Values CoLa B
    part                                                                                        (ASCII)              (Binary)
                                                              First part of IP address       0 …+255d (00 … 00 … FF
                                                                                             FF)
                                                              Second part of IP address      0 …+255d (00 … 00 … FF
                                                                                             FF)
IP address     Default: 192.168.0.1      Uint_8      1
                                                              Third part of IP address       0 …+255d (00 … 00 … FF
                                                                                             FF)
                                                              Fourth part of IP address      0 …+255d (00 … 00 … FF
                                                                                             FF)

Table 356: Example: sRA EIIpAddrDHCP 192.168.0.1

 CoLa      <STX>sRA{SPC}EIIpAddrDHCP{SPC}C0{SPC}A8{SPC}0{SPC}1<ETX>
  A        02 73 52 41 20 45 49 49 70 41 64 64 72 44 48 43 50 20 43 30 20 41 38 20 30 20 31 03
CoLa B 02 02 02 02 00 00 00 15 73 52 41 20 45 49 49 70 41 64 64 72 44 48 43 50 20 C0 A8 00 01 10


12.5.1.4.9.4                     Set mode for ethernet adress assignment [sWN EIAddrMode]
This Command determins the mode for the ethernet adress assignment.
Table 357: Telegram structure: sWN EIAddrMode
                             Telegram structure: sWN EIAddrMode
                            (User level 'Authorized client' required)

 Telegram              Description        Variable   Length             Additional details   Values CoLa A        Values CoLa B
    part                                                                                        (ASCII)              (Binary)
Command        Write                     String      3                                       sWN                 73 57 4E
type
Command        Set mode for ethernet     String      10                                      EIAddrMode          45 49 41 64 64
               adress assignment                                                                                 72 4D 6F 64 65
Ethernet       Static IP adress / DHCP   Enum_8      1        Static:                        0                   00
adress                                                        DHCP:                          1                   01
assign-
ment

Table 358: Example: sWN EIAddrMode
           <STX>sWN{SPC}EIAddrMode{SPC}1<ETX>
 CoLa      <STX>sWN EIAddrMode 1<ETX>
  A        sWN EIAddrMode 1
           02 73 57 4E 20 45 49 41 64 64 72 4D 6F 64 65 20 31 03
           02 02 02 02 00 00 00 4E 73 57 4E 20 45 49 41 64 64 72 4D 6F 64 65 20 01 76
CoLa B 73 57 4E 20 45 49 41 64 64 72 4D 6F 64 65 20 01



Table 359: Telegram structure: sWA EIAddrMode
                             Telegram structure: sWA EIAddrMode


 Telegram              Description        Variable   Length             Additional details   Values CoLa A        Values CoLa B
    part                                                                                        (ASCII)              (Binary)
Command        Answer                    String      3                                       sWA                 73 57 41
type
Command        Set mode for ethernet     String      10                                      EIAddrMode          45 49 41 64 64
               adress assignment                                                                                 72 4D 6F 64 65




186        multiScan165                                                                                8028981/1X1R/2026-06-10 | SICK
                                                                                                 SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

Table 360: Example: sWA EIAddrMode

 CoLa      <STX>sWA{SPC}EIAddrMode<ETX>
  A        02 73 57 41 20 45 49 41 64 64 72 4D 6F 64 65 03
CoLa B 02 02 02 02 00 00 00 0F 73 57 41 20 45 49 41 64 64 72 4D 6F 64 65 20 79


12.5.1.4.9.5                    Set fallback for DHCP [sWN EIDHCPFallback]
This Command determins the fallback when DHCP is not successful.
Table 361: Telegram structure: sWN EIDHCPFallback
                           Telegram structure: sWN EIDHCPFallback
                            (User level 'Authorized client' required)

 Telegram              Description        Variable   Length          Additional details    Values CoLa A     Values CoLa B
    part                                                                                      (ASCII)           (Binary)
Command        Write                     String      3                                     sWN              73 57 4E
type
Command        Set fallback for DHCP     String      14                                    EIDHCPFall-      45 49 44 48 43
                                                                                           back             50 46 61 6C 6C
                                                                                                            62 61 63 6B
Fallback       Use Static IP adress /    Enum_8      1        Static IP adress:            0                00
ethernet       Retry DHCP                                     DHCP retry:                  1                01
adress
assign-
ment

Table 362: Example: sWN EIDHCPFallback
           <STX>sWN{SPC}EIDHCPFallback{SPC}1<ETX>
 CoLa      <STX>sWN EIDHCPFallback 1<ETX>
  A        sWN EIDHCPFallback 1
           02 73 57 4E 20 45 49 44 48 43 50 46 61 6C 6C 62 61 63 6B 20 31 03
           02 02 02 02 00 00 00 14 73 57 4E 20 45 49 44 48 43 50 46 61 6C 6C 62 61 63 6B 20 01 54
CoLa B 73 57 4E 20 45 49 44 48 43 50 46 61 6C 6C 62 61 63 6B 20 01



Table 363: Telegram structure: sWA EIDHCPFallback
                           Telegram structure: sWA EIDHCPFallback


 Telegram              Description        Variable   Length          Additional details    Values CoLa A     Values CoLa B
    part                                                                                      (ASCII)           (Binary)
Command        Answer                    String      3                                     sWA              73 57 41
type
Command        Set fallback for DHCP     String      14                                    EIDHCPFall-      45 49 44 48 43
                                                                                           back             50 46 61 6C 6C
                                                                                                            62 61 63 6B

Table 364: Example: sWA EIDHCPFallback

 CoLa      <STX>sWA{SPC}EIDHCPFallback<ETX>
  A        02 73 57 41 20 45 49 44 48 43 50 46 61 6C 6C 62 61 63 6B 03
CoLa B 02 02 02 02 00 00 00 13 73 57 41 20 45 49 44 48 43 50 46 61 6C 6C 62 61 63 6B 20 5A


12.5.1.4.9.6                    Set Ethernet gateway [sWN Elgate]
Change Ethernet gateway IP address (TCP/IP)




8028981/1X1R/2026-06-10 | SICK                                                                           multiScan165   187
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX


NOTE
O      Save permanently to set values. Changes will be active after rebooting the device.
O      Settings must correspond with network in which scanner is used. Else device cannot be found any more.

Table 365: Telegram structure: sWN Elgate
                               Telegram structure: sWN EIgate
                            (User level 'Authorized client' required)

    Telegram           Description        Variable   Length         Additional details         Values CoLa A       Values CoLa B
       part                                                                                       (ASCII)             (Binary)
Command        Write                     String      3                                         sWN                73 57 4E
type
Command        Set gateway adress        String      6                                         EIgate             45 49 67 61 74
                                                                                                                  65
                                                              First part of gateway address    0 …+255d (00…      00 …FF
                                                                                               FF)
                                                              Second part of gateway           0 …+255d (00…      00 …FF
Gateway                                                       address                          FF)
               Set values                Uint_8      1
address                                                       Third part of gateway address    0 …+255d (00…      00 …FF
                                                                                               FF)
                                                              Fourth part of gateway address   0 …+255d (00…      00 …FF
                                                                                               FF)

Table 366: Example: sWN EIgate 192.168.0.1
           <STX>sWN{SPC}EIgate{SPC}C0{SPC}A8{SPC}00{SPC}01<ETX>
    CoLa   <STX>sWN EIgate C0 A8 00 01<ETX>
     A     sWN EIgate C0 A8 00 01
           02 73 57 4E 20 45 49 67 61 74 65 20 43 30 20 41 38 20 30 30 20 30 31 03
           02 02 02 02 00 00 00 0F 73 57 4E 20 45 49 67 61 74 65 20 C0 A8 00 01 18
CoLa B 73 57 4E 20 45 49 67 61 74 65 20 C0 A8 00 01



Table 367: Telegram structure: sWA Elgate
                                Telegram structure: sWA EIgate


    Telegram           Description        Variable   Length         Additional details         Values CoLa A       Values CoLa B
       part                                                                                       (ASCII)             (Binary)
Command        Answer                    String      3                                         sWA                73 57 41
type
Command        Set gateway adress        String      6                                         EIgate             45 49 67 61 74
                                                                                                                  65

Table 368: Example: sWA EIgate

    CoLa   <STX>sWA{SPC}EIgate<ETX>
     A     02 73 57 41 20 45 49 67 61 74 65 03
CoLa B 02 02 02 02 00 00 00 0B 73 57 41 20 45 49 67 61 74 65 20 7E


12.5.1.4.9.7                    Read Ethernet gateway [sRN Elgate]
Read for the Ethernet gateway (TCP/IP)




188        multiScan165                                                                                 8028981/1X1R/2026-06-10 | SICK
                                                                                                  SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

Table 369: Telegram structure: sRN Elgate
                                  Telegram structure: sRN EIgate


 Telegram             Description          Variable   Length         Additional details         Values CoLa A   Values CoLa B
    part                                                                                           (ASCII)         (Binary)
Command        Read                       String      3                                         sRN             73 52 4E
type
Command        Read gateway address       String      6                                         EIgate          45 49 67 61 74
                                                                                                                65

Table 370: Example: sRN EIgate
          <STX>sRN{SPC}EIgate<ETX>
 CoLa     <STX>sRN EIgate<ETX>
  A       sRN EIgate
          02 73 52 4E 20 45 49 67 61 74 65 03
          02 02 02 02 00 00 00 0A 73 52 4E 20 45 49 67 61 74 65 54
CoLa B 73 52 4E 20 45 49 67 61 74 65



Table 371: Telegram structure: sRA Elgate
                                  Telegram structure: sRA EIgate


 Telegram             Description          Variable   Length         Additional details         Values CoLa A   Values CoLa B
    part                                                                                           (ASCII)         (Binary)
Command        Answer                     String      3                                         sRA             73 52 41
type
Command        Read gateway address       String      6                                         EIgate          45 49 67 61 74
                                                                                                                65
                                                               First part of gateway address    0 …+255d (00…   00 … FF
                                                                                                FF)
                                                               Second part of gateway           0 …+255d (00…   00 … FF
Gateway                                                        address                          FF)
               Default: 0.0.0.0           Uint_8      1
address                                                        Third part of gateway address    0 …+255d (00…   00 … FF
                                                                                                FF)
                                                               Fourth part of gateway address   0 …+255d (00…   00 … FF
                                                                                                FF)

Table 372: Example: sRA EIgate 192.168.0.1

 CoLa     <STX>sRA{SPC}EIgate{SPC}C0{SPC}A8{SPC}00{SPC}01<ETX>
  A       02 73 52 41 20 45 49 67 61 74 65 20 C0 A8 00 01 03
CoLa B 02 02 02 02 00 00 00 0F 73 52 41 20 45 49 67 61 74 65 20 C0 A8 00 01 12


12.5.1.4.9.8                      Read ethernet gateway IP adress assigned by DHCP [sRN ElgateDHCP]

NOTE
DHCP needs to be set as mode for ethernet assignment.

Read for the ethernet gateway IP adress which was assigned by DHCP.




8028981/1X1R/2026-06-10 | SICK                                                                              multiScan165    189
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

Table 373: Telegram structure: sRN ElgateDHCP
                            Telegram structure: sRN EIgateDHCP


    Telegram          Description       Variable   Length          Additional details           Values CoLa A       Values CoLa B
       part                                                                                        (ASCII)             (Binary)
Command        Read                     String     3                                            sRN                73 52 4E
type
Command        Read ethernet gateway    String     6                                            EIgateDHCP         45 49 67 61 74
               IP address assigned by                                                                              65 44 48 43 50
               DHCP

Table 374: Example: sRN EIgate
           <STX>sRN{SPC}EIgateDHCP<ETX>
    CoLa   <STX>sRN EIgateDHCP<ETX>
     A     sRN EIgateDHCP
           02 73 52 4E 20 45 49 67 61 74 65 44 48 43 50 03
           02 02 02 02 00 00 00 0E 73 52 4E 20 45 49 67 61 74 65 44 48 43 50 4B
CoLa B 73 52 4E 20 45 49 67 61 74 65 44 48 43 50



Table 375: Telegram structure: sRA ElgateDHCP
                            Telegram structure: sRA ElgateDHCP


    Telegram          Description       Variable   Length          Additional details           Values CoLa A       Values CoLa B
       part                                                                                        (ASCII)             (Binary)
Command        Answer                   String     3                                            sRA                73 52 41
type
Command        Read ethernet gateway    String     6                                            EIgateDHCP         45 49 67 61 74
               IP address assigned by                                                                              65 44 48 43 50
               DHCP
                                                             First part of gateway IP address   0 …+255d (00…      00 … FF
                                                                                                FF)
                                                             Second part of gateway IP          0 …+255d (00…      00 … FF
Gateway IP                                                   address                            FF)
           Default: 0.0.0.0             Uint_8     1
address                                                      Third part of gateway IP           0 …+255d (00…      00 … FF
                                                             address                            FF)
                                                             Fourth part of gateway IP          0 …+255d (00…      00 … FF
                                                             address                            FF)

Table 376: Example: sRA ElgateDHCP 0.0.0.0

    CoLa   <STX>sRA{SPC}EIgateDHCP{SPC}0{SPC}0{SPC}0{SPC}0<ETX>
     A     02 73 52 41 20 45 49 67 61 74 65 44 48 43 50 20 30 20 30 20 30 20 30 03
CoLa B 02 02 02 02 00 00 00 13 73 52 41 20 45 49 67 61 74 65 44 48 43 50 20 00 00 00 00 64


12.5.1.4.9.9                   Set IP mask [sWN EImask]
Define the subnet mask of the device.

NOTE
O      Save permanently to set values. Changes will be active after rebooting the device.
O      Settings must correspond with network in which scanner is used. Else device cannot be found any more.




190        multiScan165                                                                                  8028981/1X1R/2026-06-10 | SICK
                                                                                                   SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

Table 377: Telegram structure: sWN EImask
                                 Telegram structure: sWN EImask
                              (User level 'Authorized client' required)

 Telegram               Description         Variable   Length          Additional details   Values CoLa A   Values CoLa B
    part                                                                                       (ASCII)         (Binary)
Command         Write                      String      3                                    sWN             73 57 4E
type
Command         Set IP mask                String      6                                    EImask          45 49 6D 61 73
                                                                                                            6B
                                                                First part of IP mask       0 …+255d (00…   00 …FF
                                                                                            FF)
                                                                Second part of IP mask      0 …+255d (00…   00 …FF
                                                                                            FF)
IP mask         Set values                 Uint_8      1
                                                                Third part of IP mask       0 …+255d (00…   00 …FF
                                                                                            FF)
                                                                Fourth part of IP mask      0 …+255d (00…   00 …FF
                                                                                            FF)

Table 378: Example: sWN EImask 255.255.254.0
          <STX>sWN{SPC}EImask{SPC}FF{SPC}FF{SPC}FE{SPC}00<ETX>
 CoLa     <STX>sWN EImask FF FF FE 00<ETX>
  A       sWN EImask FF FF FE 00
          02 73 57 4E 20 45 49 6D 61 73 6B 20 46 46 20 46 46 20 46 45 20 30 30 03
          02 02 02 02 00 00 00 0F 73 57 4E 20 45 49 6D 61 73 6B 20 FF FF FE 00 8C
CoLa B 73 57 4E 20 45 49 6D 61 73 6B 20 FF FF FE 00



Table 379: Telegram structure: sWA EImask
                                 Telegram structure: sWA EImask


 Telegram               Description         Variable   Length          Additional details   Values CoLa A   Values CoLa B
    part                                                                                       (ASCII)         (Binary)
Command         Answer                     String      3                                    sWA             73 57 41
type
Command         Set IP mask                String      6                                    EImask          45 49 6D 61 73
                                                                                                            6B

Table 380: Example: sWA EImask
 CoLa     <STX>sWA{SPC}EImask<ETX>
  A       02 73 57 41 20 45 49 6D 61 73 6B 03
CoLa B 02 02 02 02 00 00 00 0B 73 57 41 20 45 49 6D 61 73 6B 20 7D


12.5.1.4.9.10                     Read IP mask [sRN EImask]
Read the subnet mask of the device.
Table 381: Telegram structure: sRN Elmask
                                 Telegram structure: sRN EImask


 Telegram               Description         Variable   Length          Additional details   Values CoLa A   Values CoLa B
    part                                                                                       (ASCII)         (Binary)
Command         Read                       String      3                                    sRN             73 52 4E
type
Command         Read IP mask               String      6                                    EImask          45 49 6D 61 73
                                                                                                            6B




8028981/1X1R/2026-06-10 | SICK                                                                          multiScan165    191
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

Table 382: Example: sRN EImask
          <STX>sRN{SPC}EImask<ETX>
 CoLa     <STX>sRN EImask<ETX>
  A       sRN EImask
          02 73 52 4E 20 45 49 6D 61 73 6B 03
          02 02 02 02 00 00 00 0A 73 52 4E 20 45 49 6D 61 73 6B 57
CoLa B 73 52 4E 20 45 49 6D 61 73 6B



Table 383: Telegram structure: sRA Elmask
                               Telegram structure: sRA EImask


 Telegram              Description       Variable   Length                Sensor         Values CoLa A       Values CoLa B
    part                                                                                    (ASCII)             (Binary)
Command         Answer                   String     3                                    sRA                73 52 41
type
Command         Read IP mask             String     6                                    EImask             45 49 6D 61 73
                                                                                                            6B
                                                             First part of IP mask       0 …+255d (00…      00 … FF
                                                                                         FF)
                                                             Second part of IP mask      0 …+255d (00…      00 … FF
                                                                                         FF)
IP mask         Default: 255.255.255.0   Uint_8     1
                                                             Third part of IP mask       0 …+255d (00…      00 … FF
                                                                                         FF)
                                                             Fourth part of IP mask      0 …+255d (00…      00 … FF
                                                                                         FF)

Table 384: Example: sRA EImask 255.255.254.0

 CoLa     <STX>sRA{SPC}EImask{SPC}FF{SPC}FF{SPC}FE{SPC}00<ETX>
  A       02 73 52 41 20 45 49 6D 61 73 6B 20 45 49 6D 61 73 6B 03
CoLa B 02 02 02 02 00 00 00 0F 73 52 41 20 45 49 6D 61 73 6B 20 FF FF FE 00 86


12.5.1.4.9.11                   Read IP mask assigned by DHCP [sRN EImaskDHCP]

NOTE
DHCP needs to be set as mode for ethernet assignment.

Read for the IP mask which was assigned by DHCP.
Table 385: Telegram structure: sRN EImaskDHCP
                            Telegram structure: sRN EImaskDHCP


 Telegram              Description       Variable   Length          Additional details   Values CoLa A       Values CoLa B
    part                                                                                    (ASCII)             (Binary)
Command         Read                     String     3                                    sRN                73 52 4E
type
Command         Read IP mask assigned    String     10                                   EImaskDHCP         45 49 6D 61 73
                by DHCP                                                                                     6B 44 48 43 50

Table 386: Example: sRN EImaskDHCP
          <STX>sRN{SPC}EImaskDHCP<ETX>
 CoLa     <STX>sRN EImaskDHCP<ETX>
  A       sRN EImaskDHCP
          02 73 52 4E 20 45 49 6D 61 73 6B 44 48 43 50 03




192       multiScan165                                                                            8028981/1X1R/2026-06-10 | SICK
                                                                                            SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

          02 02 02 02 00 00 00 0E 73 52 4E 20 45 49 6D 61 73 6B 44 48 43 50 4B
CoLa B 73 52 4E 20 45 49 6D 61 73 6B 44 48 43 50



Table 387: Telegram structure: sRA EImaskDHCP
                             Telegram structure: sRA EImaskDHCP


 Telegram              Description       Variable   Length          Additional details       Values CoLa A   Values CoLa B
    part                                                                                        (ASCII)         (Binary)
Command         Answer                   String     3                                    sRA                 73 52 41
type
Command         Read IP mask assigned    String     10                                   EImaskDHCP          45 49 6D 61 73
                by DHCP                                                                                      6B 44 48 43 50
                                                             First part of IP mask       0 …+255d (00…       00 … FF
                                                                                         FF)
                                                             Second part of IP mask      0 …+255d (00…       00 … FF
                                                                                         FF)
IP mask         Default: 255.255.255.0   Uint_8     1
                                                             Third part of IP mask       0 …+255d (00…       00 … FF
                                                                                         FF)
                                                             Fourth part of IP mask      0 …+255d (00…       00 … FF
                                                                                         FF)

Table 388: Example: sRA EImaskDHCP 255.255.255.0

 CoLa     <STX>sRA{SPC}EIgateDHCP{SPC}FF{SPC}FF{SPC}FF{SPC}0<ETX>
  A       02 73 52 41 20 45 49 6D 61 73 6B 44 48 43 50 20 46 46 20 46 46 20 46 46 20 30 03
CoLa B 02 02 02 02 00 00 00 13 73 52 41 20 45 49 6D 61 73 6B 44 48 43 50 20 FF FF FF 00 98


12.5.1.4.9.12                   Read MAC address [sRN EIMacAdr]
Read the MAC address of the device.
Table 389: Telegram structure: sRN EIMacAdr
                              Telegram structure: sRN EIMacAdr


 Telegram              Description       Variable   Length          Additional details       Values CoLa A   Values CoLa B
    part                                                                                        (ASCII)         (Binary)
Command         Read                     String     3                                    sRN                 73 52 4E
type
Command         Read MAC address of      String     8                                    EIMacAdr            45 49 4D 61 63
                the device                                                                                   41 64 72

Table 390: Example: sRN EIMacAdr
          <STX>sRN{SPC}EIMacAdr<ETX>
 CoLa     <STX>sRN EIMacAdr<ETX>
  A       sRN EIMacAdr
          02 73 57 4E 20 45 49 4D 61 63 41 64 72 03
          02 02 02 02 00 00 00 0C 73 52 4E 20 45 49 4D 61 63 41 64 72 5B
CoLa B 73 52 4E 20 45 49 4D 61 63 41 64 72




8028981/1X1R/2026-06-10 | SICK                                                                           multiScan165    193
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

Table 391: Telegram structure: sRA EIMacAdr
                               Telegram structure: sRA EIMacAdr


 Telegram               Description       Variable   Length         Additional details         Values CoLa A        Values CoLa B
    part                                                                                          (ASCII)              (Binary)
Command         Answer                    String     3                                         sRA                 73 52 41
type
Command         Read MAC address of       String     8                                         EIMacAdr            45 49 4D 61 63
                the device                                                                                         41 64 72
                                          Uint_8     1        First part of MAC address        0 …+255d (00…       00 … FF
                                                                                               FF)
                                          Uint_8     1        Second part of MAC address       0 …+255d (00…       00 … FF
                                                                                               FF)
                                          Uint_8     1        Third part of MAC address        0 …+255d (00…       00 … FF
MAC                                                                                            FF)
                Values
address                                   Uint_8     1        Fourth part of MAC address       0 …+255d (00…       00 … FF
                                                                                               FF)
                                          Uint_8     1        Fifth part of MAC address        0 …+255d (00…       00 … FF
                                                                                               FF)
                                          Uint_8     1        Sixth part of MAC address        0 …+255d (00…       00 … FF
                                                                                               FF)

Table 392: Example: sRA EIMacAdr 00:06:77:22:40:EA

 CoLa     <STX>sRA{SPC}EIMacAdr{SPC}0{SPC}6{SPC}77{SPC}22{SPC}40{SPC}EA<ETX>
  A       02 73 52 41 20 45 49 4D 61 63 41 64 72 20 30 20 36 20 37 37 20 32 32 20 34 30 20 45 41 03
CoLa B 02 02 02 02 00 00 00 13 73 52 41 20 45 49 4D 61 63 41 64 72 20 00 06 77 22 40 EA 8D


12.5.1.4.9.13                    Set device search mode [sWN EtherColaScanMode]
This command configures the Auto IP functionalites (Device search by SICK Enginnering Tools) and the changea-
bility of the IP address. The functionality can reduces the number of open ports to a miniumum.
Table 393: Telegram structure: sWN EtherCoLaScanMode
                          Telegram structure: sWN EtherCoLaScanMode
                              (User level 'Authorized client' required)

 Telegram               Description       Variable   Length         Additional details         Values CoLa A        Values CoLa B
    part                                                                                          (ASCII)              (Binary)
Command         Write                     String     3                                         sWN                 73 57 4E
type
Command         Set CoLa Scan / AutoIP    String     17                                        EtherCoLaS-         45 74 68 65 72
                search settings                                                                canMode             43 6F 4C 61 53
                                                                                                                   63 61 6E 4D 6F
                                                                                                                   64 65
CoLa        Choose setting                Uint_8     1        IP address can be found/         0                   00
Scan /                                                        changed without login:
AutoIP                                                        IP address can be found/         1                   01
search set-                                                   changed with login:
tings                                                         Disable the Auto IP search/ IP   2                   02
                                                              change:
                                                              IP address can be found/         3                   03
                                                              changed for 1 min:

Table 394: Example: sWN EtherCoLaScanMode 2 - Disable the Auto IP search/ IP change
          <STX>sWN{SPC}EtherCoLaScanMode{SPC}2<ETX>
 CoLa     <STX>sWN EtherCoLaScanMode 2<ETX>
  A       sWN EtherCoLaScanMode 2
          02 73 57 4E 20 45 74 68 65 72 43 6F 4C 61 53 63 61 6E 4D 6F 64 65 20 32 03




194       multiScan165                                                                                   8028981/1X1R/2026-06-10 | SICK
                                                                                                   SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

          02 02 02 02 00 00 00 14 73 57 4E 20 45 74 68 65 72 43 6F 4C 61 53 63 61 6E 4D 6F 64 65 20 02 3B
CoLa B 73 57 4E 20 45 74 68 65 72 43 6F 4C 61 53 63 61 6E 4D 6F 64 65 20 02



Table 395: Telegram structure: sWA EtherCoLaScanMode
                          Telegram structure: sWA EtherCoLaScanMode


 Telegram               Description       Variable   Length        Additional details      Values CoLa A        Values CoLa B
    part                                                                                      (ASCII)              (Binary)
Command         Answer                    String     3                                     sWA                 73 57 41
type
Command         Set CoLa Scan / AutoIP    String     17                                    EtherCoLaS-         45 74 68 65 72
                search settings                                                            canMode             43 6F 4C 61 53
                                                                                                               63 61 6E 4D 6F
                                                                                                               64 65

Table 396: Example: sWA EtherCoLaScanMode

 CoLa     <STX>sWA{SPC}EtherCoLaScanMode<ETX>
  A       02 73 57 41 20 45 74 68 65 72 43 6F 4C 61 53 63 61 6E 4D 6F 64 65 03
CoLa B 02 02 02 02 00 00 00 16 73 57 41 20 45 74 68 65 72 43 6F 4C 61 53 63 61 6E 4D 6F 64 65 20 36


12.5.1.4.9.14                    Read device search mode [sRN EtherColaScanMode]
This command polls the Auto IP functionalites (Device search by SICK Enginnering Tools) and the IP address
changeability settings.
Table 397: Telegram structure: sRN EtherCoLaScanMode
                          Telegram structure: sRN EtherCoLaScanMode
                              (User level 'Authorized client' required)

 Telegram               Description       Variable   Length        Additional details      Values CoLa A        Values CoLa B
    part                                                                                      (ASCII)              (Binary)
Command         Write                     String     3                                     sRN                 73 52 4E
type
Command         Read CoLa Scan /          String     17                                    EtherCoLaS-         45 74 68 65 72
                AutoIP search settings                                                     canMode             43 6F 4C 61 53
                                                                                                               63 61 6E 4D 6F
                                                                                                               64 65

Table 398: Example: sRN EtherCoLaScanMode
          <STX>sRN{SPC}EtherCoLaScanMode<ETX>
 CoLa     <STX>sRN EtherCoLaScanMode<ETX>
  A       sRN EtherCoLaScanMode
          02 73 52 4E 20 45 74 68 65 72 43 6F 4C 61 53 63 61 6E 4D 6F 64 65 03
          02 02 02 02 00 00 00 15 73 52 4E 20 45 74 68 65 72 43 6F 4C 61 53 63 61 6E 4D 6F 64 65 1C
CoLa B 73 52 4E 20 45 74 68 65 72 43 6F 4C 61 53 63 61 6E 4D 6F 64 65



Table 399: Telegram structure: sRA EtherCoLaScanMode
                          Telegram structure: sRA EtherCoLaScanMode


 Telegram               Description       Variable   Length        Additional details      Values CoLa A        Values CoLa B
    part                                                                                      (ASCII)              (Binary)
Command         Answer                    String     3                                     sRA                 73 52 41
type




8028981/1X1R/2026-06-10 | SICK                                                                              multiScan165   195
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                           Telegram structure: sRA EtherCoLaScanMode


 Telegram               Description         Variable   Length         Additional details       Values CoLa A        Values CoLa B
    part                                                                                          (ASCII)              (Binary)
Command         Read CoLa Scan /           String      17                                      EtherCoLaS-         45 74 68 65 72
                AutoIP search settings                                                         canMode             43 6F 4C 61 53
                                                                                                                   63 61 6E 4D 6F
                                                                                                                   64 65
CoLa        Poll setting                   Uint_8      1        IP address can be found/       0                   00
Scan /                                                          changed without login:
AutoIP                                                          IP address can be found/       1                   01
search set-                                                     changed with login:
tings                                                           Auto IP search/ IP change is   2                   02
                                                                disabled:
                                                                IP address can be found/       3                   03
                                                                changed for 1 min:

Table 400: Example: sRA EtherCoLaScanMode 3 - IP address can be found/changed for 1 min

 CoLa       <STX>sRA{SPC}EtherCoLaScanMode{SPC}3<ETX>
  A         02 73 52 41 20 45 74 68 65 72 43 6F 4C 61 53 63 61 6E 4D 6F 64 65 20 33 03
CoLa B 02 02 02 02 00 00 00 17 73 52 41 20 45 74 68 65 72 43 6F 4C 61 53 63 61 6E 4D 6F 64 65 20 03 30


12.5.1.4.9.15                     Enable/ disable CoLa1 interface [sWN EIAuxEnable]
After enabling the CoLa1 interface, use port 2111 for CoLa A and port 2112 for CoLa B.
Table 401: Telegram structure: sWN EIAuxEnable
                               Telegram structure: sWN EIAuxEnable
                              (User level 'Authorized client' required)

 Telegram               Description         Variable   Length         Additional details       Values CoLa A        Values CoLa B
    part                                                                                          (ASCII)              (Binary)
Command         Write                      String      3                                       sWN                 73 57 4E
type
Command         Set CoLa1 interface        String      11                                      EIAuxEnable         45 49 41 75 78
                                                                                                                   45 6E 61 62 6C
                                                                                                                   65
CoLa1           Enable/ disable            Bool_1      1        Disable:                       0                   00
interface                                                       Enable:                        1                   01

Table 402: Example: sWN EIAuxEnable
            <STX>sWN{SPC}EIAuxEnable{SPC}1<ETX>
 CoLa       <STX>sWN EIAuxEnable 1<ETX>
  A         sWN EIAuxEnable 1
            02 73 57 4E 20 45 49 41 75 78 45 6E 61 62 6C 65 20 31 03
            02 02 02 02 00 00 00 11 73 57 4E 20 45 49 41 75 78 45 6E 61 62 6C 65 20 01 0A
CoLa B 73 57 4E 20 45 49 41 75 78 45 6E 61 62 6C 65 20 01



Table 403: Telegram structure: sWA EIAuxEnable
                              Telegram structure: sWA EIAuxEnable


 Telegram               Description         Variable   Length         Additional details       Values CoLa A        Values CoLa B
    part                                                                                          (ASCII)              (Binary)
Command         Answer                     String      3                                       sWA                 73 57 41
type




196         multiScan165                                                                                 8028981/1X1R/2026-06-10 | SICK
                                                                                                   SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                             Telegram structure: sWA EIAuxEnable


 Telegram            Description         Variable   Length         Additional details        Values CoLa A       Values CoLa B
    part                                                                                        (ASCII)             (Binary)
Command         Set CoLa1 interface      String     11                                       EIAuxEnable        45 49 41 75 78
                                                                                                                45 6E 61 62 6C
                                                                                                                65

Table 404: Example: sWA EIAuxEnable

 CoLa     <STX>sWA{SPC}EIAuxEnable<ETX>
  A       02 73 57 41 20 45 49 41 75 78 45 6E 61 62 6C 65 03
CoLa B 02 02 02 02 00 00 00 10 73 57 41 20 45 49 41 75 78 45 6E 61 62 6C 65 20 04


12.5.1.4.9.16                     Set Webserver state [sMN SetWebserverEnabled]
This command enables/ disables the Webserver. Port 80 will not be opened after a reboot.
Table 405: Telegram structure: sMN SetWebserverEnabled
                         Telegram structure: sMN SetWebserverEnabled
                             (User level 'Authorized client' required)

 Telegram            Description         Variable   Length         Additional details        Values CoLa A       Values CoLa B
    part                                                                                        (ASCII)             (Binary)
Command         Method                   String     3                                        sMN                73 4D 4E
type
Command         Set Webserver state      String     19                                       SetWebserver-      53 65 74 57 65
                                                                                             Enabled            62 73 65 72 76
                                                                                                                65 72 45 6E 61
                                                                                                                62 6C 65 64
State           Enable/ disable          Bool_1     1        Disable:                        0                  00
                                                             Enable:                         1                  01

Table 406: Example: sMN SetWebserverEnabled
          <STX>sMN{SPC}SetWebserverEnabled{SPC}1<ETX>
 CoLa     <STX>sMN SetWebserverEnabled 1<ETX>
  A       sMN SetWebserverEnabled 1
          02 73 4D 4E 20 47 65 74 57 65 62 73 65 72 76 65 72 45 6E 61 62 6C 65 64 20 31 03
          02 02 02 02 00 00 00 19 73 4D 4E 20 53 65 74 57 65 62 73 65 72 76 65 72 45 6E 61 62 6C 65 64 20 01 23
CoLa B 73 4D 4E 20 53 65 74 57 65 62 73 65 72 76 65 72 45 6E 61 62 6C 65 64 20 01



Table 407: Telegram structure: sAN SetWebserverEnabled
                         Telegram structure: sAN SetWebserverEnabled


 Telegram            Description         Variable   Length         Additional details        Values CoLa A       Values CoLa B
    part                                                                                        (ASCII)             (Binary)
Command         Answer                   String     3                                        sAN                73 41 4E
type
Command         Set Webserver state      String     19                                       SetWebserver-      53 65 74 57 65
                                                                                             Enabled            62 73 65 72 76
                                                                                                                65 72 45 6E 61
                                                                                                                62 6C 65 64

Table 408: Example: sAN SetWebserverEnabled

 CoLa     <STX>sAN{SPC}SetWebserverEnabled<ETX>
  A       02 73 41 4E 20 47 65 74 57 65 62 73 65 72 76 65 72 45 6E 61 62 6C 65 64 03
CoLa B 02 02 02 02 00 00 00 18 73 41 4E 20 47 65 74 57 65 62 73 65 72 76 65 72 45 6E 61 62 6C 65 64 2E



8028981/1X1R/2026-06-10 | SICK                                                                               multiScan165   197
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

12.5.1.4.9.17                     Read Webserver state [sMN GetWebserverEnabled]
Returns state if Webserver is enabled.
Table 409: Telegram structure: sMN GetWebserverEnabled
                         Telegram structure: sMN GetWebserverEnabled
                             (User level 'Authorized client' required)

 Telegram            Description           Variable   Length         Additional details     Values CoLa A        Values CoLa B
    part                                                                                       (ASCII)              (Binary)
Command         Method                    String      3                                     sMN                 73 4D 4E
type
Command         Webserver state           String      19                                    GetWebserver-       47 65 74 57 65
                                                                                            Enabled             62 73 65 72 76
                                                                                                                65 72 45 6E 61
                                                                                                                62 6C 65 64

Table 410: Example: sMN GetWebserverEnabled
         <STX>sMN{SPC}GetWebserverEnabled<ETX>
 CoLa    <STX>sMN GetWebserverEnabled<ETX>
  A      sMN GetWebserverEnabled
         02 73 4D 4E 20 47 65 74 57 65 62 73 65 72 76 65 72 45 6E 61 62 6C 65 64 03
         02 02 02 02 00 00 00 17 73 4D 4E 20 47 65 74 57 65 62 73 65 72 76 65 72 45 6E 61 62 6C 65 64 16
CoLa B 73 4D 4E 20 47 65 74 57 65 62 73 65 72 76 65 72 45 6E 61 62 6C 65 64



Table 411: Telegram structure: sAN GetWebserverEnabled
                         Telegram structure: sAN GetWebserverEnabled


 Telegram            Description           Variable   Length         Additional details     Values CoLa A        Values CoLa B
    part                                                                                       (ASCII)              (Binary)
Command         Answer                    String      3                                     sAN                 73 41 4E
type
Command         Webserver state           String      19                                    GetWebserver-       47 65 74 57 65
                                                                                            Enabled             62 73 65 72 76
                                                                                                                65 72 45 6E 61
                                                                                                                62 6C 65 64
State           Status of the webserver   Bool_1      1        Disabled:                    0                   00
                                                               Enabled:                     1                   01

Table 412: Example: sAN GetWebserverEnabled

 CoLa    <STX>sAN{SPC}GetWebserverEnabled{SPC}1<ETX>
  A      02 73 41 4E 20 47 65 74 57 65 62 73 65 72 76 65 72 45 6E 61 62 6C 65 64 20 31 03
CoLa B 02 02 02 02 00 00 00 19 73 41 4E 20 47 65 74 57 65 62 73 65 72 76 65 72 45 6E 61 62 6C 65 64 20 01 3B


12.5.1.4.9.18                     Enable/ disable LEDs [sWN LEDEnable]
This command enables/ disables the LEDs of the device.
Table 413: Telegram structure: sWN LEDEnable
                              Telegram structure: sWN LEDEnable
                             (User level 'Authorized client' required)

 Telegram            Description           Variable   Length         Additional details     Values CoLa A        Values CoLa B
    part                                                                                       (ASCII)              (Binary)
Command         Method                    String      3                                     sWN                 73 57 4E
type
Command         Set LEDs                  String      9                                     LEDEnable           4C 45 44 45 6E
                                                                                                                61 62 6C 65



198      multiScan165                                                                                 8028981/1X1R/2026-06-10 | SICK
                                                                                                SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                            Telegram structure: sWN LEDEnable
                           (User level 'Authorized client' required)

 Telegram            Description         Variable   Length          Additional details    Values CoLa A   Values CoLa B
    part                                                                                     (ASCII)         (Binary)
Status          Enable/ disable          Bool_1     1        Off:                         0               00
                                                             On:                          1               01

Table 414: Example: sWN LEDEnable
          <STX>sWN{SPC}LEDEnable{SPC}1<ETX>
 CoLa     <STX>sWN LEDEnable 1<ETX>
  A       sWN LEDEnable 1
          02 73 57 4E 20 4C 45 44 45 6E 61 62 6C 65 20 31 03
          02 02 02 02 00 00 00 0F 73 57 4E 20 4C 45 44 45 6E 61 62 6C 65 20 01 07
CoLa B 73 57 4E 20 4C 45 44 45 6E 61 62 6C 65 20 01



Table 415: Telegram structure: sWA LEDEnable
                             Telegram structure: sWA LEDEnable


 Telegram            Description         Variable   Length          Additional details    Values CoLa A   Values CoLa B
    part                                                                                     (ASCII)         (Binary)
Command         Answer                   String     3                                     sWA             73 57 41
type
Command         Set LEDs                 String     9                                     LEDEnable       4C 45 44 45 6E
                                                                                                          61 62 6C 65

Table 416: Example: sWA LEDEnable

 CoLa     <STX>sWA{SPC}LEDEnable<ETX>
  A       02 73 57 41 20 4C 45 44 45 6E 61 62 6C 65 03
CoLa B 02 02 02 02 00 00 00 0E 73 57 41 20 73 57 41 20 4C 45 44 45 6E 61 62 6C 65 20 09


12.5.1.4.9.19                     Read state of LEDs [sRN LEDState]
Read the current state of the LEDs.
Table 417: Telegram structure: sRN LEDState
                              Telegram structure: sRN LEDState


 Telegram            Description         Variable   Length          Additional details    Values CoLa A   Values CoLa B
    part                                                                                     (ASCII)         (Binary)
Command         Method                   String     3                                     sRN             73 52 4E
type
Command         Read state of LEDs       String     8                                     LEDState        4C 45 44 53 74
                                                                                                          61 74 65

Table 418: Example: sRN LEDState
          <STX>sRN{SPC}LEDState<ETX>
 CoLa     <STX>sRN LEDState<ETX>
  A       sRN LEDState
          02 73 52 4E 20 4C 45 44 53 74 61 74 65 03
          02 02 02 02 00 00 00 0C 73 52 4E 20 4C 45 44 53 74 61 74 65 55
CoLa B 73 52 4E 20 4C 45 44 53 74 61 74 65




8028981/1X1R/2026-06-10 | SICK                                                                        multiScan165   199
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

Table 419: Telegram structure: sRA LEDState
                                 Telegram structure: sRA LEDState


 Telegram               Description        Variable   Length          Additional details          Values CoLa A         Values CoLa B
    part                                                                                             (ASCII)               (Binary)
Command         Answer                     String     3                                           sRA                  73 52 41
type
Command         State of LEDs              String     8                                           LEDState             4C 45 44 53 74
                                                                                                                       61 74 65
LED Color       -                          Enum_8     1        Green:                             0                    00
                                                               Yellow:                            1                    01
                                                               Red:                               2                    02
LED             -                          Enum_8     1        On:                                0                    00
behavior                                                       Off:                               1                    01
                                                               Blinking:                          2                    02
                                                               Blinking fast:                     3                    03
                                                               Blinking delayed:                  4                    04
                                                               Find me active (see "Initiate an   5                    05
                                                               acoustic or visual signal for a
                                                               defined period of time [sMN
                                                               FindMe]", page 177):
LED ID          Name of the LED            String     8                                           LED1                 4C 45 44 31
                                                                                                  LED2                 4C 45 44 32

Table 420: Example: sRA LEDState
           <STX>sRA{SPC}LED-
           State{SPC}2{SPC}0{SPC}0{SPC}LED2{SPC}0{SPC}0{SPC}0{SPC}0{SPC}1{SPC}0{SPC}LED1{SPC}0{SPC}0{SPC}0{SPC}
 CoLa      0<ETX>
  A
           02 73 52 41 20 4C 45 44 53 74 61 74 65 20 32 20 30 20 30 20 4C 45 44 32 00 00 00 00 20 31 20 30 20 4C 45 44 31
           00 00 00 00 03
           02 02 02 02 00 00 00 23 73 52 41 20 4C 45 44 53 74 61 74 65 20 00 02 00 00 4C 45 44 32 00 00 00 00 01 00 4C 45
CoLa B
           44 31 00 00 00 00 7A


12.5.1.4.10                 Application


12.5.1.4.10.1                      Set activation of evaluation group [sMN ActivateEvaluationGroup]
The telegram is intended to activate or deactivate groups via telegram. The group activation needs to be changed
from always to telegram in advance.
Table 421: Telegram structure: sMN ActivateEvaluationGroup
                          Telegram structure: sMN ActivateEvaluationGroup
                               (User level 'Authorized client' required)

Telegram        Description                Variable   Length Additional details                   Values CoLa A        Values CoLa B
part                                                                                              (ASCII)              (Binary)
Command         Method                     String     3                                           sMN                  73 4D 4E
type
Command         Activate / deactivate      String     23                                          ActivateEvalua-      41 63 74 69 76 61
                evaluation group                                                                  tionGroup            74 65 45 76 61
                                                                                                                       6C 75 61 74 69
                                                                                                                       6F 6E 47 72 6F
                                                                                                                       75 70
Amount of       Array                      Uint_16    2        Each array element contains        1d ... 48d (1 ...    00 01 … 00 30
evaluation                                                     two parameters:                    30h)
groups to                                                      O  Evalution group number
activate/                                                      O  Deactivation / activation of
deactivate
                                                                  evaluation group




200        multiScan165                                                                                      8028981/1X1R/2026-06-10 | SICK
                                                                                                       SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                     Telegram structure: sMN ActivateEvaluationGroup
                          (User level 'Authorized client' required)

Telegram       Description             Variable       Length Additional details               Values CoLa A       Values CoLa B
part                                                                                          (ASCII)             (Binary)
Evalution      Evaluation group 1      UInt_16        2                                       1                   00 01
group
number
Deactiva-      Activate / deactivate   Bool_1         1       Deactivate:                     0                   00
tion / acti-   evaluation group 1                             Activate:                       1                   01
vation of
evaluation
group
Evalution      Evaluation group 2      UInt_16        2                                       2                   00 02
group
number
Activate/      Activate / deactivate   Bool_1         1       Deactivate:                     0                   00
deactivate     evaluation group 2                             Activate:                       1                   01
evaluation
group
                                                                 ...
Evalution      Evaluation group 48     UInt_16        2                                       48d (30h)           00 30
group
number
Activate/      Activate / deactivate   Bool_1         1       Deactivate:                     0                   00
deactivate     evaluation group 48                            Activate:                       1                   01
evaluation
group

Table 422: Example1: sMN ActivateEvaluationGroup – Deactivate evaluation group 1
          <STX>sMN{SPC}ActivateEvaluationGroup{SPC}1{SPC}1{SPC}0<ETX>
 CoLa     <STX>sMN ActivateEvaluationGroup 1 1 0<ETX>
  A       sMN ActivateEvaluationGroup 1 1 0
          02 73 4D 4E 20 41 63 74 69 76 61 74 65 45 76 61 6C 75 61 74 69 6F 6E 47 72 6F 75 70 20 31 20 31 20 30 03
          02 02 02 02 00 00 00 21 73 4D 4E 20 41 63 74 69 76 61 74 65 45 76 61 6C 75 61 74 69 6F 6E 47 72 6F 75 70 20 00 01 00
          01 00 20
CoLa B
          73 4D 4E 20 41 63 74 69 76 61 74 65 45 76 61 6C 75 61 74 69 6F 6E 47 72 6F 75 70 20 00 01 00 01 00


Table 423: Example2: sMN ActivateEvaluationGroup – Deactivate evaluation group 1, activate evaluation group 2 and 3
          <STX>sMN{SPC}ActivateEvaluationGroup{SPC}3{SPC}1{SPC}0{SPC}2{SPC}1{SPC}3{SPC}1<ETX>
          <STX>sMN ActivateEvaluationGroup 3 1 0 2 1 3 1<ETX>
 CoLa
  A       sMN ActivateEvaluationGroup 3 1 0 2 1 3 1
          02 73 4D 4E 20 41 63 74 69 76 61 74 65 45 76 61 6C 75 61 74 69 6F 6E 47 72 6F 75 70 20 33 20 31 20 30 20 32 20
          31 20 33 20 31 03
          02 02 02 02 00 00 00 21 73 4D 4E 20 41 63 74 69 76 61 74 65 45 76 61 6C 75 61 74 69 6F 6E 47 72 6F 75 70 20 00 03 00
          01 00 00 02 01 00 03 01 23
CoLa B
          73 4D 4E 20 41 63 74 69 76 61 74 65 45 76 61 6C 75 61 74 69 6F 6E 47 72 6F 75 70 20 00 03 00 01 00 00 02 01 00
          03 01

Table 424: Telegram structure: sAN ActivateEvaluation
                        Telegram structure: sAN ActivateEvaluation


Telegram       Description             Variable       Length Additional details               Values CoLa A       Values CoLa B
part                                                                                          (ASCII)             (Binary)
Command        Answer                  String         3                                       sAN                 73 52 41
type




8028981/1X1R/2026-06-10 | SICK                                                                                 multiScan165   201
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                          Telegram structure: sAN ActivateEvaluation


Telegram        Description                Variable   Length Additional details                   Values CoLa A       Values CoLa B
part                                                                                              (ASCII)             (Binary)
Command         Activate / deactivate      String     23                                          ActivateEvalua-     41 63 74 69 76 61
                evaluation group                                                                  tionGroup           74 65 45 76 61
                                                                                                                      6C 75 61 74 69
                                                                                                                      6F 6E 47 72 6F
                                                                                                                      75 70
Amount of -                                UInt_16    2                                           1h... 30h           00 01 … 00 30
activated/
deacti-
vated eval-
uation
groups
State of     -                             Bool_1     1         Activation/Deactivation failed:   0                   00
activation /                                                    Successfully activated/deacti-
deactiva-                                                       vated:                            1                   01
tion

Table 425: Example 1: sAN ActivateEvaluation – Successfully deactivated evaluation group 1

 CoLa     <STX>sAN{SPC}ActivateEvaluation{SPC}1{SPC}1<ETX>
  A       02 73 41 4E 20 41 63 74 69 76 61 74 65 45 76 61 6C 75 61 74 69 6F 6E 47 72 6F 75 70 20 31 20 31 03
          02 02 02 02 00 00 00 1F 73 41 4E 20 41 63 74 69 76 61 74 65 45 76 61 6C 75 61 74 69 6F 6E 47 72 6F 75 70 20 00 01 01
CoLa B
          2C

Table 426: Example 2: sAN ActivateEvaluation – Successfully deactivated evaluation group 1, successfully activated evaluation
group 2, failed activation of evaluation group 3

 CoLa     <STX>sAN{SPC}ActivateEvaluation{SPC}3{SPC}1{SPC}1{SPC}0<ETX>
  A       02 73 41 4E 20 41 63 74 69 76 61 74 65 45 76 61 6C 75 61 74 69 6F 6E 47 72 6F 75 70 20 31 20 31 20 31 20 30 03
          02 02 02 02 00 00 00 1A 73 41 4E 20 41 63 74 69 76 61 74 65 45 76 61 6C 75 61 74 69 6F 6E 47 72 6F 75 70 20 00 03 01
CoLa B
          01 00 73


12.5.1.4.10.2                    Set field evaluation contour [sMN SetFieldEvaluationContour]
This telegram describes how to change the polygon coordinates. A predefined polygon is required. No setup of a
polygon from scratch possible.
Table 427: Telegram structure: sMN SetFieldEvaluationContour
                     Telegram structure: sMN SetFieldEvaluationContour
                           (User level 'Authorized client' required)

Telegram        Description                Variable   Length Additional details                   Values CoLa A       Values CoLa B
part                                                                                              (ASCII)             (Binary)
Command         Method                     String     3                                           sMN                 73 4D 4E
type
Command         Set the region of inter-   String     25                                          SetFieldEvalua-     53 65 74 46 69
                est of an object detec-                                                           tionContour         65 6C 64 45 76
                tion evaluation                                                                                       61 6C 75 61 74
                                                                                                                      69 6F 6E 43 6F
                                                                                                                      6E 74 6F 75 72
Evalution       Specific ID of the eval-   UInt_16    2                                           +1d ... +48d        00 01 … 00 30
ID              uation that is to be                                                              (1h ... 30h)
                changed
Amount of       E. g. triangle = 3, square Array      ... 800                                     +3d ... +800d       00 03... 03 20
polygon         =4                                                                                (3h ... 320h)
verticies




202       multiScan165                                                                                      8028981/1X1R/2026-06-10 | SICK
                                                                                                      SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                   Telegram structure: sMN SetFieldEvaluationContour
                         (User level 'Authorized client' required)

Telegram     Description                Variable   Length Additional details                Values CoLa A      Values CoLa B
part                                                                                        (ASCII)            (Binary)
Polygon      Coordinates of first pol- Dint_32     4       X coordinate:                    -60,000d ...       FF FF 15 A0 …
vertex       ygon vertex in mm                                                              +60,000d           00 00 EA 60
                                                                                            (FFFF15A0h …
                                                                                            EA60h)
                                        Dint_32    4       Y coordinate:                    -60,000d ...       FF FF 15 A0 …
                                                                                            +60,000d           00 00 EA 60
                                                                                            (FFFF15A0h …
                                                                                            EA60h)
Polygon      Coordinates of second      Dint_32    4       X coordinate:                    -60,000d ...       FF FF 15 A0 …
vertex       polygon vertex in mm                                                           +60,000d           00 00 EA 60
                                                                                            (FFFF15A0h …
                                                                                            EA60h)
                                        Dint_32    4       Y coordinate:                    -60,000d ...       FF FF 15 A0 …
                                                                                            +60,000d           00 00 EA 60
                                                                                            (FFFF15A0h …
                                                                                            EA60h)
                                                              ...
Polygon      Coordinates of last pol-   Dint_32    4       X coordinate:                    -60,000d ...       FF FF 15 A0 …
vertex       ygon vertex in mm                                                              +60,000d           00 00 EA 60
                                                                                            (FFFF15A0h …
                                                                                            EA60h)
                                        Dint_32    4       Y coordinate:                    -60,000d ...       FF FF 15 A0 …
                                                                                            +60,000d           00 00 EA 60
                                                                                            (FFFF15A0h …
                                                                                            EA60h)
Lower Z      Lower bound of extru-      Dint_32    4                                        -60,000d ...       FF FF 15 A0 …
limit        sion in Z direction                                                            +60,000d           00 00 EA 60
                                                                                            (FFFF15A0h …
                                                                                            EA60h)
Upper Z      Upper bound of extru-      Dint_32    4                                        -60,000d ...       FF FF 15 A0 …
limit        sion in Z direction                                                            +60,000d           00 00 EA 60
                                                                                            (FFFF15A0h …
                                                                                            EA60h)

Table 428: Example: sMN SetFieldEvaluationContour – Conversion of an evaluation into a 1 m3 cube
          <STX>sMN{SPC}SetFieldEvaluationContour{SPC}1{SPC}4{SPC}+1000{SPC}+1000{SPC}-1000{SPC}
          +1000{SPC}-1000{SPC}-1000{SPC}+1000{SPC}-1000{SPC}-500{SPC}+500<ETX>
          <STX>sMN SetFieldEvaluationContour 1 4 +1000 +1000 -1000 +1000 -1000 -1000 +1000 -1000 -500
 CoLa     +500<ETX>
  A       sMN SetFieldEvaluationContour 1 4 +1000 +1000 -1000 +1000 -1000 -1000 +1000 -1000 -500 +500
          02 73 4D 4E 20 53 65 74 46 69 65 6C 64 45 76 61 6C 75 61 74 69 6F 6E 43 6F 6E 74 6F 75 72 20 31 20 34 20 2B 31
          30 30 30 20 2B 31 30 30 30 20 2D 31 30 30 30 20 2B 31 30 30 30 20 2D 31 30 30 30 20 2D 31 30 30 30 20 2B 31
          30 30 30 20 2D 31 30 30 30 20 2D 35 30 30 20 2B 35 30 30 03
          02 02 02 02 00 00 00 4A 73 4D 4E 20 53 65 74 46 69 65 6C 64 45 76 61 6C 75 61 74 69 6F 6E 43 6F 6E 74 6F 75 72 20
          00 01 00 04 00 00 03 E8 00 00 03 E8 FF FF FC 18 00 00 03 E8 FF FF FC 18 FF FF FC 18 00 00 03 E8 FF FF FC 18 FF
          FF FE 0C 00 00 01 F4 1A
CoLa B
          73 4D 4E 20 53 65 74 46 69 65 6C 64 45 76 61 6C 75 61 74 69 6F 6E 43 6F 6E 74 6F 75 72 20 00 01 00 04 00 00
          03 E8 00 00 03 E8 FF FF FC 18 00 00 03 E8 FF FF FC 18 FF FF FC 18 00 00 03 E8 FF FF FC 18 FF FF FE 0C 00
          00 01 F4




8028981/1X1R/2026-06-10 | SICK                                                                              multiScan165   203
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

Table 429: Telegram structure: sAN SetFieldEvaluationContour
                       Telegram structure: sAN SetFieldEvaluationContour


Telegram        Description                Variable   Length Additional details             Values CoLa A        Values CoLa B
part                                                                                        (ASCII)              (Binary)
Command         Answer                     String     3                                     sAN                  73 52 41
type
Command         Set the region of inter-   String     25                                    SetFieldEvalua-      53 65 74 46 69
                est of an object detec-                                                     tionContour          65 6C 64 45 76
                tion evaluation                                                                                  61 6C 75 61 74
                                                                                                                 69 6F 6E 43 6F
                                                                                                                 6E 74 6F 75 72
State of   -                               Enum_8     1        Conversion successful:       0                    00
evaluation                                                     Invalid Evaluation:          1                    01
conversion                                                     Invalid Polygon:             2                    02
                                                               Invalid Z limit:             3                    03

Table 430: Example: sAN SetFieldEvaluationContour – Evaluation conversion successful

 CoLa    <STX>sAN{SPC}SetFieldEvaluationContour{SPC}0<ETX>
  A      02 73 41 4E 20 53 65 74 46 69 65 6C 64 45 76 61 6C 75 61 74 69 6F 6E 43 6F 6E 74 6F 75 72 20 30 03
         02 02 02 02 00 00 00 1F 73 41 4E 20 53 65 74 46 69 65 6C 64 45 76 61 6C 75 61 74 69 6F 6E 43 6F 6E 74 6F 75 72 20
CoLa B
         00 14


12.5.1.4.10.3                    Read the current evaluation configuration state [sRN EvaluationConfigState]
The telegram is intended to read the current configuration state of the field evaluation. Depending on the device
computational limits can be reached. If so the telegram returns an error or warning if the number of beams or
evaluations reaches the maximum defined threshold.
Table 431: Telegram structure: sRN EvaluationConfigState
                         Telegram structure: sRN EvaluationConfigState


 Telegram              Description         Variable   Length         Additional details     Values CoLa A        Values CoLa B
    part                                                                                       (ASCII)              (Binary)
Command         Read                       String     3                                     sRN                  73 52 4E
type
Command         Info on current configu-   String     21                                    EvaluationCon-       45 76 61 6C 75
                ration state                                                                figState             61 74 69 6F 6E
                                                                                                                 43 6F 6E 66 69
                                                                                                                 67 53 74 61 74
                                                                                                                 65

Table 432: Example: sRN EvaluationConfigState
         <STX>sRN{SPC}EvaluationConfigState<ETX>
 CoLa    <STX>sRN EvaluationConfigState<ETX>
  A      sRN EvaluationConfigState
         02 73 52 4E 20 45 76 61 6C 75 61 74 69 6F 6E 43 6F 6E 66 69 67 53 74 61 74 65 03
         02 02 02 02 00 00 00 19 73 52 4E 20 45 76 61 6C 75 61 74 69 6F 6E 43 6F 6E 66 69 67 53 74 61 74 65 12
CoLa B 73 52 4E 20 45 76 61 6C 75 61 74 69 6F 6E 43 6F 6E 66 69 67 53 74 61 74 65




204      multiScan165                                                                                 8028981/1X1R/2026-06-10 | SICK
                                                                                                SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

Table 433: Telegram structure: sRA EvaluationConfigState
                         Telegram structure: sRA EvaluationConfigState


    Telegram            Description         Variable   Length         Additional details      Values CoLa A           Values CoLa B
       part                                                                                      (ASCII)                 (Binary)
Command         Answer                      String     3                                     sRA                     73 52 41
type
Command         Info on current configu-    String     21                                    EvaluationCon-          45 76 61 6C 75
                ration state                                                                 figState                61 74 69 6F 6E
                                                                                                                     43 6F 6E 66 69
                                                                                                                     67 53 74 61 74
                                                                                                                     65
Active                                      Enum_8     1        OK:                          0                       00
beams                                                           Warning:                     1                       01
limit                                                           Error:                       2                       02
Active                                      Enum_8     1        OK:                          0                       00
evalua-                                                         Warning:                     1                       01
tions limit                                                     Error:                       2                       02
Number of       Array                       Uint_32    48                                    0 ... 65535 (0 ...      00 00 ... FF FF
intersect-                                                                                   FFFF)
ing beams

Table 434: Example: sRA EvaluationConfigState - one evaluation active, intersected by 172 beams, status of active beam limit
and active evaluation limit is OK
           <STX>sRA{SPC}EvaluationConfig-
           State{SPC}0{SPC}0{SPC}AC{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SP
           C}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0
           {SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SP
    CoLa   C}0{SPC}0{SPC} ETX>
     A
           02 73 52 41 20 45 76 61 6C 75 61 74 69 6F 6E 43 6F 6E 66 69 67 53 74 61 74 65 20 30 20 30 20 41 43 20 30 20 30 20 30
           20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30
           20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30
           20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 03
       02 02 02 02 00 00 00 7C 73 52 41 20 45 76 61 6C 75 61 74 69 6F 6E 43 6F 6E 66 69 67 53 74 61 74 65 20 00 00 00 AC
       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
CoLa B
       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 87


12.5.1.4.10.4                    Read field evaluation result [sRN FieldEvaluationResult]
This telegram returns the status information of all evaluations.
Possible status codes:
O   Not configured
       o      This evaluation has not been configured.
O      Inactive
       o      This evaluation has been configured but is currently not evaluated.
O      Free
       o      The field is not infringed.
O      Infringed
       o      The field is infringed.
O      Detecting infringed
       o      An infringement has been detected in the field but the response time has not been reached yet.




8028981/1X1R/2026-06-10 | SICK                                                                                    multiScan165   205
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

Table 435: Telegram structure: sRN FieldEvaluationResult
                         Telegram structure: sRN FieldEvaluationResult


 Telegram            Description         Variable   Length            Additional details     Values CoLa A        Values CoLa B
    part                                                                                        (ASCII)              (Binary)
Command       Read                       String     3                                        sRN                 73 52 4E
type
Command       Info on field evaluation   String     21                                       FieldEvaluation- 46 69 65 6C 64
              result                                                                         Result           45 76 61 6C 75
                                                                                                              61 74 69 6F 6E
                                                                                                              52 65 73 75 6C
                                                                                                              74

Table 436: Example: sRN FieldEvaluationResult
          <STX>sRN{SPC}FieldEvaluationResult<ETX>
 CoLa     <STX>sRN FieldEvaluationResult<ETX>
  A       sRN FieldEvaluationResult
          02 73 52 4E 20 46 69 65 6C 64 45 76 61 6C 75 61 74 69 6F 6E 52 65 73 75 6C 74 03
          02 02 02 02 00 00 00 19 73 52 4E 20 46 69 65 6C 64 45 76 61 6C 75 61 74 69 6F 6E 52 65 73 75 6C 74 12
CoLa B 73 52 4E 20 46 69 65 6C 64 45 76 61 6C 75 61 74 69 6F 6E 52 65 73 75 6C 74


Table 437: Telegram structure: sRA FieldEvaluationResult
                         Telegram structure: sRA FieldEvaluationResult


 Telegram            Description         Variable   Length            Additional details     Values CoLa A        Values CoLa B
    part                                                                                        (ASCII)              (Binary)
Command       Answer                     String     3                                        sRA                 73 52 41
type
Command       Info on field evaluation   String     21                                       FieldEvaluation- 46 69 65 6C 64
              result                                                                         Result           45 76 61 6C 75
                                                                                                              61 74 69 6F 6E
                                                                                                              52 65 73 75 6C
                                                                                                              74
Version       Version number             Uint_16    2                                        0 ... FFFFh         00 ... FF FF
Time-         Time of the last         ULInt_64     8                                        0 ...         00 00 00 00 00
stamp         field infringement. Time                                                       FFFFFFFFFFFFF 00 00 00 ... FF
              base is the sensor sys-                                                        FFFh          FF FF FF FF FF
              tem time in millisec-                                                                        FF FF
              onds since January 1,
              1970, 00:00 (UTC). If
              a time server is being
              used, the configured
              system time is used.
Evaluation    Evaluation state of the    Enum_8     1        Not configured:                 0                   00
Result        first field.                                   Inactive:                       1                   01
                                                             Free:                           2                   02
                                                             Detecting infringed:            3                   03
                                                             Infringed:                      4                   04
Evaluation    Evaluation state of the    Enum_8     1        Not configured:                 0                   00
Result        second field.                                  Inactive:                       1                   01
                                                             Free:                           2                   02
                                                             Detecting infringed:            3                   03
                                                             Infringed:                      4                   04
                                                                ...




206       multiScan165                                                                                 8028981/1X1R/2026-06-10 | SICK
                                                                                                 SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                          Telegram structure: sRA FieldEvaluationResult


    Telegram            Description         Variable   Length            Additional details   Values CoLa A     Values CoLa B
       part                                                                                      (ASCII)           (Binary)
Evaluation      Evaluation state of the     Enum_8     1        Not configured:               0                00
Result          last field. (maximum                            Inactive:                     1                01
                amout of evaluations =                          Free:                         2                02
                48)                                             Detecting infringed:          3                03
                                                                Infringed:                    4                04

Table 438: Example: sSN FieldEvaluationResult
           <STX>sSN{SPC}FieldEvaluationRe-
           sult{SPC}1{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{
           SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SP
           C}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0
    CoLa   {SPC}0{SPC}<ETX>
     A
           02 73 53 4E 20 46 69 65 6C 64 45 76 61 6C 75 61 74 69 6F 6E 52 65 73 75 6C 74 20 31 20 30 20 30 20 30 20 30 20 30
           20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30
           20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30
           20 30 20 30 20 30 20 30 20 30 20 30 03
       02 02 02 02 00 00 00 54 73 52 41 20 46 69 65 6C 64 45 76 61 6C 75 61 74 69 6F 6E 52 65 73 75 6C 74 20 00 01 00 00
CoLa B 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 3C


12.5.1.4.10.5                    Receive field evaluation result by event [sEN FieldEvaluationResult]
This telegram returns the status information of all evaluations.
Possible status codes:
O   Not configured
       o      This evaluation has not been configured.
O      Inactive
       o      This evaluation has been configured but is currently not evaluated.
O      Free
       o      The field is not infringed.
O      Infringed
       o      The field is infringed.
O      Detecting infringed
       o      An infringement has been detected in the field but the response time has not been reached yet.
Table 439: Telegram structure: sEN FieldEvaluationResult
                         Telegram structure: sEN FieldEvaluationResult


    Telegram            Description         Variable   Length            Additional details   Values CoLa A     Values CoLa B
       part                                                                                      (ASCII)           (Binary)
Command         Event                       String     3                                      sEN              73 45 4E
type
Command         Info on field evaluation    String     21                                     FieldEvaluation- 46 69 65 6C 64
                result                                                                        Result           45 76 61 6C 75
                                                                                                               61 74 69 6F 6E
                                                                                                               52 65 73 75 6C
                                                                                                               74
Reporting       Start/ stop                 Enum_8     1        Stop:                         0                00
                                                                Start:                        1                01




8028981/1X1R/2026-06-10 | SICK                                                                              multiScan165   207
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

Table 440: Example: sEN FieldEvaluationResult
          <STX>sEN{SPC}FieldEvaluationResult{SPC}1<ETX>
 CoLa     <STX>sEN FieldEvaluationResult 1<ETX>
  A       sEN FieldEvaluationResult 1
          02 73 45 4E 20 46 69 65 6C 64 45 76 61 6C 75 61 74 69 6F 6E 52 65 73 75 6C 74 20 31 03
          02 02 02 02 00 00 00 1B 73 45 4E 20 46 69 65 6C 64 45 76 61 6C 75 61 74 69 6F 6E 52 65 73 75 6C 74 20 01 24
CoLa B 73 45 4E 20 46 69 65 6C 64 45 76 61 6C 75 61 74 69 6F 6E 52 65 73 75 6C 74 20 01


Table 441: Telegram structure: sSN FieldEvaluationResult
                         Telegram structure: sSN FieldEvaluationResult


 Telegram            Description         Variable   Length            Additional details     Values CoLa A          Values CoLa B
    part                                                                                        (ASCII)                (Binary)
Command       Answer                     String     3                                       sSN                    73 53 4E
type
Command       Info on field evaluation   String     21                                      FieldEvaluation- 46 69 65 6C 64
              result                                                                        Result           45 76 61 6C 75
                                                                                                             61 74 69 6F 6E
                                                                                                             52 65 73 75 6C
                                                                                                             74
Version       Version number             Uint_16    2                                       0 ... FFFFh            00 ... FF FF
Time-         Time of the latest       ULInt_64     8                                       0 ...         00 00 00 00 00
stamp         field infringement. Time                                                      FFFFFFFFFFFFF 00 00 00 ... FF
              base is the sensor sys-                                                       FFFh          FF FF FF FF FF
              tem time in millisec-                                                                       FF FF
              onds since January 1,
              1970, 00:00 (UTC). If
              a time server is being
              used, the configured
              system time is used.
Evaluation    Evaluation state of the    Enum_8     1        Not configured:                0                      00
Result        first field.                                   Inactive:                      1                      01
                                                             Free:                          2                      02
                                                             Detecting infringed:           3                      03
                                                             Infringed:                     4                      04
Evaluation    Evaluation state of the    Enum_8     1        Not configured:                0                      00
Result        second field.                                  Inactive:                      1                      01
                                                             Free:                          2                      02
                                                             Detecting infringed:           3                      03
                                                             Infringed:                     4                      04
                                                                ...
Evaluation    Evaluation state of the    Enum_8     1        Not configured:                0                      00
Result        last field.                                    Inactive:                      1                      01
              (maximum amout of                              Free:                          2                      02
              evaluations = 48)                              Detecting infringed:           3                      03
                                                             Infringed:                     4                      04

Table 442: Example: sSN FieldEvaluationResult
          <STX>sSN{SPC}
          FieldEvaluationResult{SPC}1{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SP
          C}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0
          {SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SP
 CoLa     C}0{SPC}0{SPC}0{SPC} ETX>
  A
          02 73 53 4E 20 46 69 65 6C 64 45 76 61 6C 75 61 74 69 6F 6E 52 65 73 75 6C 74 20 31 20 30 20 30 20 30 20 30 20 30
          20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30
          20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30
          20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 03




208       multiScan165                                                                                   8028981/1X1R/2026-06-10 | SICK
                                                                                                   SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

       02 02 02 02 00 00 00 54 73 52 41 20 46 69 65 6C 64 45 76 61 6C 75 61 74 69 6F 6E 52 65 73 75 6C 74 20 00 01 00 00
CoLa B 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 3C


12.5.1.4.10.6                   Request perpendicular distance once [sRN perpendicularDistanceResult]
This telegram can be used to request the perpendicular distance. The shortest and furthest measuring point in a
range to a reference plane will be transmitted. A field and a reference plane must be defined in the user interface
under Application > Perpendicular distance measurement.
Table 443: Telegram structure: sRN perpendicularDistanceResult
                    Telegram structure: sRN perpendicularDistanceResult
                           (User level 'Authorized client' required)

 Telegram              Description        Variable   Length       Additional details         Values CoLa A       Values CoLa B
    part                                                                                        (ASCII)             (Binary)
Command         Read                      String     3                                      sRN                 73 52 4E
type
Command         Perpendicular distance    String     27                                     perpendicular-      70 65 72 70 65
                values                                                                      DistanceResult      6E 64 69 63 75
                                                                                                                6C 61 72 44 69
                                                                                                                73 74 61 6E 63
                                                                                                                65 52 65 73 75
                                                                                                                6C 74

Table 444: Example: sRN perpendicularDistanceResult
          <STX>sRN{SPC}perpendicularDistanceResult<ETX>
 CoLa     <STX>sRN perpendicularDistanceResult<ETX>
  A       sRN perpendicularDistanceResult
          02 73 52 4E 20 70 65 72 70 65 6E 64 69 63 75 6C 61 72 44 69 73 74 61 6E 63 65 52 65 73 75 6C 74 03
          02 02 02 02 00 00 00 1F 73 52 4E 20 70 65 72 70 65 6E 64 69 63 75 6C 61 72 44 69 73 74 61 6E 63 65 52 65 73 75 6C
          74 3D
CoLa B
          73 52 4E 20 70 65 72 70 65 6E 64 69 63 75 6C 61 72 44 69 73 74 61 6E 63 65 52 65 73 75 6C 74


Table 445: Telegram structure: sRA perpendicularDistanceResult
                    Telegram structure: sRA perpendicularDistanceResult


 Telegram              Description        Variable   Length       Additional details         Values CoLa A       Values CoLa B
    part                                                                                        (ASCII)             (Binary)
Command         Answer                    String     3                                      sRA                 73 52 41
type
Command         Perpendicular distance    String     27                                     perpendicular-      70 65 72 70 65
                values                                                                      DistanceResult      6E 64 69 63 75
                                                                                                                6C 61 72 44 69
                                                                                                                73 74 61 6E 63
                                                                                                                65 52 65 73 75
                                                                                                                6C 74
Time-           Time of the latest        ULInt_64   8                                      0 ...         00 00 00 00 00
stamp           object detection in the                                                     FFFFFFFFFFFFF 00 00 00... FF
                defined fields. Time                                                        FFFh          FF FF FF FF FF
                base is the sensor sys-                                                                   FF FF
                tem time in millisec-
                onds since January 1,
                1970, 00:00 (UTC). If
                a time server is being
                used, the configured
                system time is used.
Amount of       Amount of perpendicu- Uint_16        2                                      1 ... 48d (1 ... 30h) 00 01 ... 00 30
evalua-         lar distance evaluations
tions


8028981/1X1R/2026-06-10 | SICK                                                                               multiScan165     209
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                      Telegram structure: sRA perpendicularDistanceResult


 Telegram              Description          Variable   Length         Additional details    Values CoLa A         Values CoLa B
    part                                                                                       (ASCII)               (Binary)
Evaluation      ID of perpendicular dis-   Uint_16     2                                   1 ... 48d (1 ... 30h) 00 01 ... 00 30
ID X            tance evaluation
                Minimum distance           Int_32      4                                   -62000d …             FF FF 0D D0 …
                [mm]                                                                       +62000d               00 00 F2 30
                                                                                           (FFFF0DD0 …
                                                                                           F230h)
                Maximum distance           Int_32      4                                   -62000d …             FF FF 0D D0 …
                [mm]                                                                       +62000d               00 00 F2 30
                                                                                           (FFFF0DD0 …
                                                                                           F230h)
                X minimum distance         Int_32      4                                   -62000d …             FF FF 0D D0 …
                [mm]                                                                       +62000d               00 00 F2 30
                                                                                           (FFFF0DD0 …
                                                                                           F230h)
                Y minimum distance         Int_32      4                                   -62000d …             FF FF 0D D0 …
                [mm]                                                                       +62000d               00 00 F2 30
                                                                                           (FFFF0DD0 …
                                                                                           F230h)
                Z minimum distance         Int_32      4                                   -62000d …             FF FF 0D D0 …
                [mm]                                                                       +62000d               00 00 F2 30
                                                                                           (FFFF0DD0 …
                                                                                           F230h)
                X maximum distance         Int_32      4                                   -62000d …             FF FF 0D D0 …
                [mm]                                                                       +62000d               00 00 F2 30
                                                                                           (FFFF0DD0 …
                                                                                           F230h)
                Y maximum distance         Int_32      4                                   -62000d …             FF FF 0D D0 …
                [mm]                                                                       +62000d               00 00 F2 30
                                                                                           (FFFF0DD0 …
                                                                                           F230h)
                Z maximum distance         Int_32      4                                   -62000d …             FF FF 0D D0 …
                [mm]                                                                       +62000d               00 00 F2 30
                                                                                           (FFFF0DD0 …
                                                                                           F230h)
Evaluation      ...                        ...         ...      ...                        ...                   ...
ID ...

Table 446: Example: sRA perpendicularDistanceResult - 1 configured field
         <STX>sRA{SPC}perpendicularDistanceResult{SPC}
         230BDCE0{SPC}1{SPC}1{SPC}20C{SPC}324{SPC}20C{SPC}FFFFFFAD{SPC}41{SPC}32{SPC}FFFFFF54{SPC}1E<ETX>
 CoLa
  A      02 73 52 41 20 70 65 72 70 65 6E 64 69 63 75 6C 61 72 44 69 73 74 61 6E 63 65 52 65 73 75 6C 74 20 32 33 30 62 64 63
         65 30 20 31 20 31 20 32 30 63 20 33 32 34 20 32 30 63 20 46 46 46 46 46 46 41 44 20 34 31 20 33 32 34 20 46 46 46
         46 46 46 35 34 20 31 65 03
       02 02 02 02 00 00 00 4C 73 52 41 20 70 65 72 70 65 6E 64 69 63 75 6C 61 72 44 69 73 74 61 6E 63 65 52 65 73 75 6C
CoLa B 74 20 00 00 00 00 23 0B DC E0 00 01 00 01 00 00 02 0C 00 00 03 24 00 00 02 0C FF FF FF AD 00 00 00 41 00 00
       03 24 FF FF FF 54 00 00 00 1E A0


12.5.1.4.10.7                    Request perpendicular distance continiously on event [sEN perpendicularDistan-
                                 ceResult]
This telegram can be used to request the perpendicular distance continiously on event. The shortest and furthest
measuring point in a range to a reference plane will be transmitted. A field and a reference plane must be defined
in the user interface under Application > Perpendicular distance measurement.




210      multiScan165                                                                                  8028981/1X1R/2026-06-10 | SICK
                                                                                                 SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

Table 447: Telegram structure: sEN perpendicularDistanceResult
                  Telegram structure: sEN perpendicularDistanceResult
                         (User level 'Authorized client' required)

 Telegram            Description        Variable   Length            Additional details      Values CoLa A         Values CoLa B
    part                                                                                        (ASCII)               (Binary)
Command      Event                     String      3                                        sEN                   73 45 4E
type
Command      Perpendicular distance    String      27                                       perpendicular-        70 65 72 70 65
             values                                                                         DistanceResult        6E 64 69 63 75
                                                                                                                  6C 61 72 44 69
                                                                                                                  73 74 61 6E 63
                                                                                                                  65 52 65 73 75
                                                                                                                  6C 74
Start/ Stop -                          Enum_8      1        Stop:                           0                     00
                                                            Start:                          1                     01

Table 448: Example: sEN perpendicularDistanceResult
          <STX>sEN{SPC}perpendicularDistanceResult{SPC}1<ETX>
 CoLa     <STX>sEN perpendicularDistanceResult 1<ETX>
  A       sEN perpendicularDistanceResult 1
          02 73 45 4E 20 70 65 72 70 65 6E 64 69 63 75 6C 61 72 44 69 73 74 61 6E 63 65 52 65 73 75 6C 74 20 31 03
          02 02 02 02 00 00 00 21 73 45 4E 20 70 65 72 70 65 6E 64 69 63 75 6C 61 72 44 69 73 74 61 6E 63 65 52 65 73 75 6C
          74 20 01 0B
CoLa B
          73 45 4E 20 70 65 72 70 65 6E 64 69 63 75 6C 61 72 44 69 73 74 61 6E 63 65 52 65 73 75 6C 74 20 01


Table 449: Telegram structure: sSN perpendicularDistanceResult
                  Telegram structure: sSN perpendicularDistanceResult


 Telegram            Description        Variable   Length            Additional details      Values CoLa A         Values CoLa B
    part                                                                                        (ASCII)               (Binary)
Command      Answer                    String      3                                        sSN                   73 53 4E
type
Command      Perpendicular distance    String      27                                       perpendicular-        70 65 72 70 65
             values                                                                         DistanceResult        6E 64 69 63 75
                                                                                                                  6C 61 72 44 69
                                                                                                                  73 74 61 6E 63
                                                                                                                  65 52 65 73 75
                                                                                                                  6C 74
Time-        Time of the latest        ULInt_64    8                                        0 ...         00 00 00 00 00
stamp        object detection in the                                                        FFFFFFFFFFFFF 00 00 00... FF
             defined fields. Time                                                           FFFh          FF FF FF FF FF
             base is the sensor sys-                                                                      FF FF
             tem time in millisec-
             onds since January 1,
             1970, 00:00 (UTC). If
             a time server is being
             used, the configured
             system time is used.
Amount of    Amount of perpendicu- Uint_16         2                                        1 ... 48d (1 ... 30h) 00 01 ... 00 30
evalua-      lar distance evaluations
tions




8028981/1X1R/2026-06-10 | SICK                                                                                 multiScan165     211
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

                      Telegram structure: sSN perpendicularDistanceResult


 Telegram              Description          Variable   Length         Additional details    Values CoLa A         Values CoLa B
    part                                                                                       (ASCII)               (Binary)
Evaluation      ID of perpendicular dis-   Uint_16     2                                   1 ... 48d (1 ... 30h) 00 01 ... 00 30
ID X            tance evaluation
                Minimum distance           Int_32      4                                   -62000d …             FF FF 0D D0 …
                [mm]                                                                       +62000d               00 00 F2 30
                                                                                           (FFFF0DD0 …
                                                                                           F230h)
                Maximum distance           Int_32      4                                   -62000d …             FF FF 0D D0 …
                [mm]                                                                       +62000d               00 00 F2 30
                                                                                           (FFFF0DD0 …
                                                                                           F230h)
                X minimum distance         Int_32      4                                   -62000d …             FF FF 0D D0 …
                [mm]                                                                       +62000d               00 00 F2 30
                                                                                           (FFFF0DD0 …
                                                                                           F230h)
                Y minimum distance         Int_32      4                                   -62000d …             FF FF 0D D0 …
                [mm]                                                                       +62000d               00 00 F2 30
                                                                                           (FFFF0DD0 …
                                                                                           F230h)
                Z minimum distance         Int_32      4                                   -62000d …             FF FF 0D D0 …
                [mm]                                                                       +62000d               00 00 F2 30
                                                                                           (FFFF0DD0 …
                                                                                           F230h)
                X maximum distance         Int_32      4                                   -62000d …             FF FF 0D D0 …
                [mm]                                                                       +62000d               00 00 F2 30
                                                                                           (FFFF0DD0 …
                                                                                           F230h)
                Y maximum distance         Int_32      4                                   -62000d …             FF FF 0D D0 …
                [mm]                                                                       +62000d               00 00 F2 30
                                                                                           (FFFF0DD0 …
                                                                                           F230h)
                Z maximum distance         Int_32      4                                   -62000d …             FF FF 0D D0 …
                [mm]                                                                       +62000d               00 00 F2 30
                                                                                           (FFFF0DD0 …
                                                                                           F230h)
Evaluation      ...                        ...         ...      ...                        ...                   ...
ID ...

Table 450: Example: sSN perpendicularDistanceResult - 1 configured field
         <STX>sRA{SPC}perpendicularDistanceResult{SPC}
         230BDCE0{SPC}1{SPC}1{SPC}20C{SPC}324{SPC}20C{SPC}FFFFFFAD{SPC}41{SPC}32{SPC}FFFFFF54{SPC}1E<ETX>
 CoLa
  A      02 73 52 41 20 70 65 72 70 65 6E 64 69 63 75 6C 61 72 44 69 73 74 61 6E 63 65 52 65 73 75 6C 74 20 32 33 30 62 64 63
         65 30 20 31 20 31 20 32 30 63 20 33 32 34 20 32 30 63 20 46 46 46 46 46 46 41 44 20 34 31 20 33 32 34 20 46 46 46
         46 46 46 35 34 20 31 65 03
       02 02 02 02 00 00 00 4C 73 52 41 20 70 65 72 70 65 6E 64 69 63 75 6C 61 72 44 69 73 74 61 6E 63 65 52 65 73 75 6C
CoLa B 74 20 00 00 00 00 23 0B DC E0 00 01 00 01 00 00 02 0C 00 00 03 24 00 00 02 0C FF FF FF AD 00 00 00 41 00 00
       03 24 FF FF FF 54 00 00 00 1E A0


12.5.1.4.10.8                    Read evaluation group type [sRN EvaluationGroupType]
Array with the type of each group, either perpendicular distance or field evaluation.




212      multiScan165                                                                                  8028981/1X1R/2026-06-10 | SICK
                                                                                                 SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

Table 451: Telegram structure: sRN EvaluationGroupType
                         Telegram structure: sRN EvaluationGroupType
                             (User level 'Authorized client' required)

 Telegram              Description         Variable   Length         Additional details         Values CoLa A      Values CoLa B
    part                                                                                           (ASCII)            (Binary)
Command         Read                      String      3                                        sRN                73 52 4E
type
Command                                   String      19                                       Evaluation-        45 76 61 6C 75
                                                                                               GroupType          61 74 69 6F 6E
                                                                                                                  47 72 6F 75 70
                                                                                                                  54 79 70 65

Table 452: Example: sRN EvaluationGroupType
             <STX>sRN{SPC}EvaluationGroupType<ETX>
 CoLa        <STX>sRN EvaluationGroupType<ETX>
  A          sRN EvaluationGroupType
             02 73 52 4E 20 45 76 61 6C 75 61 74 69 6F 6E 47 72 6F 75 70 54 79 70 65 03
             02 02 02 02 00 00 00 17 73 52 4E 20 45 76 61 6C 75 61 74 69 6F 6E 47 72 6F 75 70 54 79 70 65 1E
CoLa B 73 52 4E 20 45 76 61 6C 75 61 74 69 6F 6E 47 72 6F 75 70 54 79 70 65


Table 453: Telegram structure: sRA EvaluationGroupType
                         Telegram structure: sRA EvaluationGroupType


 Telegram              Description         Variable   Length         Additional details         Values CoLa A      Values CoLa B
    part                                                                                           (ASCII)            (Binary)
Command         Answer                    String      3                                        sRA                73 52 41
type
Command                                   String      19                                       Evaluation-        45 76 61 6C 75
                                                                                               GroupType          61 74 69 6F 6E
                                                                                                                  47 72 6F 75 70
                                                                                                                  54 79 70 65
Data            Type of evaluation        Array       48       Field evaluation:               0d (00h)           00
                group                                          Perpendicular distance:         +1d (01h)          01

Table 454: Example: sRA EvaluationGroupType - 3rd group is set as perpendicular distance
             <STX>sRA{SPC}EvaluationGroup-
             Type{SPC}0{SPC}0{SPC}1{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}
             0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{S
             PC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0{SPC}0<ETX
 CoLa        >
  A
             02 73 52 41 20 45 76 61 6C 75 61 74 69 6F 6E 47 72 6F 75 70 54 79 70 65 20 30 20 30 20 31 20 30 20 30 20 30 20 30
             20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30
             20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30
             20 30 20 30 20 30 20 30 20 30 03
       02 02 02 02 00 00 00 48 73 52 41 20 49 6D 75 44 61 74 61 45 6E 61 62 6C 65 20 00 00 01 00 00 00 00 00 00 00 00
CoLa B 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
       00 00 30


12.5.1.5          Diagnostics

12.5.1.5.1               SOPAS error codes


sFA ErrorCode




8028981/1X1R/2026-06-10 | SICK                                                                                 multiScan165   213
SUBJECT TO CHANGE WITHOUT NOTICE

12 ANNEX

Table 455: SOPAS error codes
                                        Telegram structure: sFA ErrorCode
                       Error code                                    Description                             Dec.        Hex.
Sopas_Ok                                       No error                                                        0           0
Sopas_Error_METHODIN_ACCESSDENIED              Wrong userlevel, access to method not allowed                   1           1
Sopas_Error_METHODIN_UNKNOWNINDEX              Trying to access a method with an unknown Sopas                 2           2
                                               index
Sopas_Error_VARIABLE_UNKNOWNINDEX              Trying to access a variable with an unknown Sopas               3           3
                                               index
Sopas_Error_LOCALCONDITIONFAILED               Local condition violated, e.g. giving a value that              4           4
                                               exceeds the minimum or maximum allowed value
                                               for this variable
Sopas_Error_INVALID_DATA                       Invalid data given for variable, this errorcode is dep-         5           5
                                               recated (is not used anymore).
Sopas_Error_UNKNOWN_ERROR                      An error with unknown reason occurred, this error-              6           6
                                               code is deprecated.
Sopas_Error_BUFFER_OVERFLOW                    The communication buffer was too small for the                  7           7
                                               amount of data that should be serialised.
Sopas_Error_BUFFER_UNDERFLOW                   More data was expected, the allocated buffer could              8           8
                                               not be filled.
Sopas_Error_ERROR_UNKNOWN_TYPE                 The variable that shall be serialised has an unknown            9           9
                                               type. This can only happen when there are variables
                                               in the firmware of the device that do not exist in
                                               the released description of the device. This should
                                               never happen.
Sopas_Error_VARIABLE_WRITE_ACCESSDENIED        It is not allowed to write values to this variable. Prob-      10           A
                                               ably the variable is defined as read-only.
Sopas_Error_UNKNOWN_CMD_FOR_NAMESERVER         When using names instead of indices, a command                  11          B
                                               was issued that the nameserver does not under-
                                               stand.
Sopas_Error_UNKNOWN_COLA_COMMAND               The CoLa protocol specification does not define the             12          C
                                               given command, command is unknown.
Sopas_Error_METHODIN_SERVER_BUSY               It is not possible to issue more than one command               13          D
                                               at a time to an SRT device.
Sopas_Error_FLEX_OUT_OF_BOUNDS                 An array was accessed over its maximum length.                 14           E
Sopas_Error_EVENTREG_UNKNOWNINDEX              The event you wanted to register for does not exist,            15          F
                                               the index is unknown.
Sopas_Error_COLA_A_VALUE_OVERFLOW              The value does not fit into the value field, it is too          16         10
                                               large.
Sopas_Error_COLA_A_INVALID_CHARACTER           Character is unknown, probably not alphanumeric.                17          11
Sopas_Error_OSAI_NO_MESSAGE                    Only when using SRTOS in the firmware and distrib-              18         12
                                               uted variables this error can occur. It is an indica-
                                               tion that no operating system message could be
                                               created. This happens when trying to GET a variable.
Sopas_Error_OSAI_NO_ANSWER_MESSAGE             This is the same as                                             19         13
                                               Sopas_Error_OSAI_NO_MESSAGE with the dif-
                                               ference that it is thrown when trying to PUT a varia-
                                               ble.
Sopas_Error_INTERNAL                           Internal error in the firmware, problably a pointer to a       20          14
                                               parameter was null.
Sopas_Error_HubAddressCorrupted                The Sopas Hubaddress is either too short or too                 21         15
                                               long.
Sopas_Error_HubAddressDecoding                 The Sopas Hubaddress is invalid, it can not be                 22          16
                                               decoded (Syntax).
Sopas_Error_HubAddressAddressExceeded          Too many hubs in the address                                   23          17
Sopas_Error_HubAddressBlankExpected            When parsing a HubAddress an expected blank was                24          18
                                               not found. The HubAddress is not valid.




214     multiScan165                                                                                8028981/1X1R/2026-06-10 | SICK
                                                                                              SUBJECT TO CHANGE WITHOUT NOTICE

ANNEX 12

                                           Telegram structure: sFA ErrorCode
                     Error code                                          Description                          Dec.         Hex.
Sopas_Error_AsyncMethodsAreSuppressed               An asynchronous method call was made although              25           19
                                                    the device was built with “AsyncMethodsSup-
                                                    pressed”. This is an internal error that should never
                                                    happen in a released device.
Sopas_Error_ComplexArraysNotSupported               Device was built with „ComplexArraysSup-                   26           1A
                                                    pressed“ because the compiler does not allow
                                                    recursions. But now a complex array was found. This
                                                    is an internal error that should never happen in a
                                                    released device.

Table 456: Example: sFA ErrorCode Wrong userlevel

 CoLa     <STX>sFA{SPC}1<ETX>
  A       02 73 46 41 20 31 03
CoLa B 02 02 02 02 00 00 00 05 73 46 41 20 00 01 75




8028981/1X1R/2026-06-10 | SICK                                                                              multiScan165     215
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




8028981/1X1R/2026-06-10/en
                                     Since 1946, we have been developing innovative technologies with
                                     passion and a pioneering spirit. With a global network in around
                                     40 countries, SICK has a global presence and is always close by.
                                     The company’s headquarters are located in Waldkirch near Freiburg,
                                     Germany. Our customers benefit from our understanding of both local
                                     and global requirements, which enables us to deliver tailor-made sol-
                                     utions.