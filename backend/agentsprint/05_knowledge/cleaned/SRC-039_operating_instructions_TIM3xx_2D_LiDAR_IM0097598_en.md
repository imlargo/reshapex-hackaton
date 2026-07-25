OPERATING INSTRUCTIONS


TiM3xx
2D LiDAR sensors

Product described
                                     TiM3xx

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




                                                         25




2   O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                 8024851/1ONO/2024-09-25 | SICK
                                                                                                           Subject to change without notice

CONTENTS


Contents
                                   1   About this document........................................................................                              5
                                       1.1     Information on the operating instructions..............................................                           5
                                       1.2     Explanation of symbols............................................................................                5
                                       1.3     Further information...................................................................................            6

                                   2   Safety information............................................................................                           7
                                       2.1     Intended use.............................................................................................        7
                                       2.2     Improper use.............................................................................................        7
                                       2.3     Cybersecurity............................................................................................        7
                                       2.4     Limitation of liability.................................................................................         8
                                       2.5     Modifications and conversions................................................................                    8
                                       2.6     Requirements for skilled persons and operating personnel..................                                       8
                                       2.7     Operational safety and specific hazards.................................................                         9

                                   3   Product description........................................................................... 10
                                       3.1     Scope of delivery.......................................................................................         10
                                       3.2     Setup and dimensions.............................................................................                11
                                       3.3     Display and operating elements..............................................................                     14
                                       3.4     Type code..................................................................................................      14
                                       3.5     Product identification...............................................................................            15
                                       3.6     Principle of operation...............................................................................            15
                                               3.6.1      Measurement principle...........................................................                      15
                                               3.6.2      Distance measurement...........................................................                       16
                                               3.6.3      Direction measurement..........................................................                       16
                                               3.6.4      Object sizes..............................................................................            17
                                               3.6.5      Scan field flatness (conical error and tilt)..............................                            18
                                               3.6.6      Impact of object surfaces on the measurement...................                                       18
                                               3.6.7      Scanning range........................................................................                20
                                               3.6.8      Filter..........................................................................................      21
                                               3.6.9      Calculation of the field size for mobile applications..............                                   23

                                   4   Transport and storage....................................................................... 26
                                       4.1     Transport...................................................................................................     26
                                       4.2     Unpacking..................................................................................................      26
                                       4.3     Transport inspection.................................................................................            26
                                       4.4     Storage......................................................................................................    26

                                   5   Mounting............................................................................................. 27
                                       5.1     Mounting instructions...............................................................................             27
                                       5.2     Mounting device.......................................................................................           27
                                       5.3     Mutual interference..................................................................................            28

                                   6   Electrical installation........................................................................ 29
                                       6.1     Prerequisites for safe operation of the device........................................                           29
                                       6.2     Electrical block diagram for commissioning...........................................                            33

8024851/1ONO/2024-09-25 | SICK                                                                             O P E R A T I N G I N S T R U C T I O N S | TiM3xx    3
Subject to change without notice

CONTENTS


                                                  6.3       Wiring instructions....................................................................................         34
                                                  6.4       Connection diagram.................................................................................             35
                                                            6.4.1      TiMxxx-01xxxxx.........................................................................              35
                                                            6.4.2      TiMxxx-10xxxxx.........................................................................              36
                                                            6.4.3      TiMxxx-11xxxxx/TiMxxx-21xxxxx..............................................                          36
                                                            6.4.4      USB interface (TiM35x / 36x only).........................................                           37
                                                  6.5       Connecting the device electrically...........................................................                   37
                                                  6.6       Wiring digital inputs / digital outputs......................................................                   38

                                      7           Operation............................................................................................ 43
                                                  7.1       SOPAS ET...................................................................................................     43
                                                            7.1.1      Parameter - network................................................................                  45
                                                            7.1.2      Parameter - filters....................................................................              45
                                                  7.2       Field evaluation.........................................................................................       45
                                                            7.2.1      Teach-in / Field set selection..................................................                     45
                                                            7.2.2      Monitor - field evaluation monitor...........................................                        48
                                                            7.2.3      Parameter - evaluation cases.................................................                        48
                                                            7.2.4      Parameters - detection fields..................................................                      49
                                                  7.3       ROS driver.................................................................................................     51

                                      8           Maintenance...................................................................................... 52
                                                  8.1       Maintenance plan.....................................................................................           52
                                                  8.2       Cleaning.....................................................................................................   52

                                      9           Troubleshooting................................................................................. 53
                                                  9.1       Detecting and displaying errors...............................................................                  53
                                                  9.2       Resetting the password for the Service user level...................................                            53
                                                  9.3       Repairs......................................................................................................   54
                                                  9.4       Returns......................................................................................................   54
                                                  9.5       Disposal.....................................................................................................   54

                                      10          Technical data.................................................................................... 55
                                                  10.1      Features....................................................................................................    55
                                                  10.2      Performance.............................................................................................        56
                                                  10.3      Interfaces..................................................................................................    57
                                                  10.4      Mechanics/electronics.............................................................................              57
                                                  10.5      Ambient data.............................................................................................       58

                                      11          Accessories........................................................................................ 59

                                      12          Annex.................................................................................................. 60
                                                  12.1 Declarations of conformity and certificates............................................                              60
                                                  12.2 Licenses....................................................................................................         60




4    O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                                                      8024851/1ONO/2024-09-25 | SICK
                                                                                                                                                 Subject to change without notice

ABOUT THIS DOCUMENT 1


1                  About this document
1.1                Information on the operating instructions
                                   These operating instructions provide important information on how to use devices from
                                   SICK AG.
                                   Prerequisites for safe work are:
                                   •    Compliance with all safety notes and handling instructions supplied.
                                   •    Compliance with local work safety regulations and general safety regulations for
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
                                   These operating instructions do not provide information on the handling and safe
                                   operation of the machine or system in which the device is integrated. Information on
                                   this can be found in the operating instructions for the machine or system.

1.2                Explanation of symbols
                                   Warnings and important information in this document are labeled with symbols. Sig‐
                                   nal words introduce the instructions and indicate the extent of the hazard. To avoid
                                   accidents, damage, and personal injury, always comply with the instructions and act
                                   carefully.

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



8024851/1ONO/2024-09-25 | SICK                                                          O P E R A T I N G I N S T R U C T I O N S | TiM3xx   5
Subject to change without notice

1 ABOUT THIS DOCUMENT

1.3           Further information
                                       More information can be found on the product page.
                                       The product page can be accessed via the SICK Product ID: pid.sick.com/{P/N}/{S/N}
                                       {P/N} corresponds to the part number of the product, see type label.
                                       {S/N} corresponds to the serial number of the product, see type label (if indicated).

                                       The following information is available depending on the product:
                                       • Data sheets
                                       • This document in all available language versions
                                       • CAD files and dimensional drawings
                                       • Certificates (e.g., declaration of conformity)
                                       • Other publications
                                       • Software
                                       • Accessories




6     O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                  8024851/1ONO/2024-09-25 | SICK
                                                                                                              Subject to change without notice

SAFETY INFORMATION 2


2                  Safety information
2.1                Intended use
                                   The TiM3xx 2D LiDAR sensor features a scan plane and is designed for the following
                                   applications:
                                   • Field monitoring of freely defined areas with signaling of object detection via digital
                                        outputs.
                                   It is suitable for applications which demand precise, non-contact optical measuring
                                   contours and dimensioning. Typical fields of application are, for example, stationary
                                   field protection, area monitoring, access control, mobile applications (navigation and
                                   anti-collision of mobile platforms).
                                   SICK AG assumes no liability for losses or damage arising from the use of the product,
                                   either directly or indirectly. This applies in particular to use of the product that does not
                                   conform to its intended purpose and is not described in this documentation.

2.2                Improper use
                                   Any use outside of the stated areas, in particular use outside of the technical specifica‐
                                   tions and the requirements for intended use, will be deemed to be incorrect use.
                                   •    The device does not constitute a safety component in accordance with the respec‐
                                        tive applicable safety standards for machines.
                                   •    The device must not be used in explosion-hazardous areas, in corrosive environ‐
                                        ments or under extreme environmental conditions.
                                   •    Any use of accessories not specifically approved by SICK AG is at your own risk.

                                   WARNING
                                   Danger due to improper use!
                                   Any improper use can result in dangerous situations.
                                   Therefore, observe the following information:
                                   ■    Product should be used only in accordance with its intended use.
                                   ■    All information in the documentation must be strictly observed.
                                   ■    Shut down the product immediately in case of damage.


2.3                Cybersecurity
                                   Overview
                                   To protect against cybersecurity threats, it is necessary to continuously monitor and
                                   maintain a comprehensive cybersecurity concept. A suitable concept consists of organi‐
                                   zational, technical, procedural, electronic, and physical levels of defense and considers
                                   suitable measures for different types of risks. The measures implemented in this
                                   product can only support protection against cybersecurity threats if the product is used
                                   as part of such a concept.
                                   You will find further information at www.sick.com/psirt, e.g.:
                                   • General information on cybersecurity
                                   • Contact option for reporting vulnerabilities
                                   • Information on known vulnerabilities (security advisories)




8024851/1ONO/2024-09-25 | SICK                                                           O P E R A T I N G I N S T R U C T I O N S | TiM3xx   7
Subject to change without notice

2 SAFETY INFORMATION

2.4           Limitation of liability
                                       Relevant standards and regulations, the latest technological developments, and our
                                       many years of knowledge and experience have all been taken into account when
                                       compiling the data and information contained in these operating instructions. The
                                       manufacturer accepts no liability for damage caused by:

                                       ■        Non-adherence to the product documentation (e.g., operating instructions)
                                       ■        Incorrect use
                                       ■        Use of untrained staff
                                       ■        Unauthorized conversions or repair
                                       ■        Technical modifications
                                       ■        Use of unauthorized spare parts, consumables, and accessories

2.5           Modifications and conversions

                                       NOTICE
                                       Modifications and conversions to the device may result in unforeseeable dangers.

                                       Interrupting or modifying the device or SICK software will invalidate any warranty claims
                                       against SICK AG. This applies in particular to opening the housing, even as part of
                                       mounting and electrical installation.

2.6           Requirements for skilled persons and operating personnel

                                       WARNING
                                       Risk of injury due to insufficient training.
                                       Improper handling of the device may result in considerable personal injury and material
                                       damage.
                                       ■        All work must only ever be carried out by the stipulated persons.

                                       The following qualifications are required for various activities:
                                       Table 1: Activities and technical requirements
                                        Activities                    Qualification
                                        Mounting, maintenance         ■   Basic practical technical training
                                                                      ■   Knowledge of the current safety regulations in the workplace
                                        Electrical installation,      ■   Practical electrical training
                                        device replacement            ■   Knowledge of current electrical safety regulations
                                                                      ■   Knowledge of the operation and control of the devices in their
                                                                          particular application
                                        Commissioning, configura‐     ■   Basic knowledge of the computer operating system used
                                        tion                          ■   Basic knowledge of the design and setup of the described
                                                                          connections and interfaces
                                                                      ■   Basic knowledge of data transmission
                                        Operation of the device for   ■   Knowledge of the operation and control of the devices in their
                                        the particular application        particular application
                                                                      ■   Knowledge of the software and hardware environment for the
                                                                          particular application




8     O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                         8024851/1ONO/2024-09-25 | SICK
                                                                                                                     Subject to change without notice

SAFETY INFORMATION 2


2.7                Operational safety and specific hazards
                                   Please observe the safety notes and the warnings listed here and in other sections
                                   of this product documentation to reduce the possibility of risks to health and avoid
                                   dangerous situations.

                                   CAUTION
                                   Optical radiation: Class 1 Laser Product
                                   The accessible radiation does not pose a danger when viewed directly for up to 100
                                   seconds. It may pose a danger to the eyes and skin in the event of incorrect use.
                                   ■    Do not open the housing. Opening the housing may increase the level of risk.
                                   ■    Current national regulations regarding laser protection must be observed.

                                   Caution – Use of controls or adjustments or performance of procedures other than
                                   those specified herein may result in hazardous radiation exposure.
                                   It is not possible to entirely rule out temporary disorienting optical effects, particularly
                                   in conditions of dim lighting. Disorienting optical effects may come in the form of
                                   dazzle, flash blindness, afterimages, photosensitive epilepsy, or impairment of color
                                   vision, for example.

                                   WARNING
                                   Electrical voltage!
                                   Electrical voltage can cause severe injury or death.
                                   ■    Work on electrical systems must only be performed by qualified electricians.
                                   ■    The power supply must be disconnected when attaching and detaching electrical
                                        connections.
                                   ■    The product must only be connected to a voltage supply as set out in the require‐
                                        ments in the operating instructions.
                                   ■    National and regional regulations must be complied with.
                                   ■    Safety requirements relating to work on electrical systems must be complied with.


                                   WARNING
                                   Risk of injury and damage caused by potential equalization currents!
                                   Improper grounding can lead to dangerous equipotential bonding currents, which may
                                   in turn lead to dangerous voltages on metallic surfaces, such as the housing. Electrical
                                   voltage can cause severe injury or death.
                                   ■    Work on electrical systems must only be performed by qualified electricians.
                                   ■    Follow the notes in the operating instructions.
                                   ■    Install the grounding for the product and the system in accordance with national
                                        and regional regulations.




8024851/1ONO/2024-09-25 | SICK                                                            O P E R A T I N G I N S T R U C T I O N S | TiM3xx   9
Subject to change without notice

3 PRODUCT DESCRIPTION


3             Product description
3.1           Scope of delivery
                                       The delivery of the device includes the following components:
                                       Table 2: Scope of delivery
                                        No. of             Component                         Notes
                                        units
                                        1                  Device in the version ordered     TiM310 / TiM320: Connecting cable on the device
                                                           2x fastening clips, 2x            TiM351 / TiM361: No connecting cables
                                                           M3 x 5 mm screws
                                        1                  Printed safety notes, multilin‐   Quick guide and general safety notes
                                                           gual

                                       The actual scope of delivery may differ for special designs, additional orders or due to
                                       the latest technical changes.




10    O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                               8024851/1ONO/2024-09-25 | SICK
                                                                                                                           Subject to change without notice

PRODUCT DESCRIPTION 3


3.2                Setup and dimensions
                                   TiM31x, TiM32x
                                                                           [68.8 (2.71)]
                                                                             51 (20)
                                                                                                                     7   )]
                                                                                                                  .1
                                                                                                             (0                                     2x
                                                                                                         3
                                                                                                     4.
                                                                                                [Ø

                                                                                                1


                                                    38.3 (1.50)
                                                                                                2



                                                                                            3
                                                                                            4
                                              79 (3.11)                                     5
                                                                                                                                                                                                 ß
                                         55.8 (2.19)                                         6

                                                                                                     4.3
                                    [19.4                                                         [ Ø 16 )]
                                                     27.3 (1.08)                                     0.
                                                                                                     (
                                   (0.76)]
                                                                                                                                                                                                        (0.76)
                                                                                                  4.4 (0.17)
                                                      8 (0.31)                                                                                                                                   19.4

                                               7                              60 (2.36)                                       [0.5      60 (2.36)                            51 (2.00)
                                                                            [68.8 (2.71)]                                     (0.02)]
                                                                             [76.3 (3.0)]
                                                                                                                                        8            9                     2              2

                                                                                 30°
                                                                                             â


                                                     ‒45°                                       225°




                                     0°                                                                             180°

                                                                                                                     à



                                                                                                              á

                                                                                 90°

                                   Figure 1: Structure and dimensions, unit: mm (inch), decimal separator: period
                                   1                              2x fastening clip with M3 x 5 mm countersunk screw, self-locking (included in scope of
                                                                  delivery)
                                   2                              M3 threaded mounting hole, 2.8 mm deep (blind hole thread), max. tightening torque
                                                                  0.8 Nm
                                   3                              Optics cover
                                   4                              Receiving range (light inlet)
                                   5                              Transmission range (light emission)
                                   6                              Red and green LED (status indicators)
                                   7                              Function button for teach-in
                                   8                              Connecting cable outlet 0.9 m with 15-pin D-Sub HD male connector or connecting cable
                                                                  0.8 m with 12-pin M12 plug (“power/digital inputs/outputs” connection)
                                   9                              Micro USB female contact, behind the black plastic cover (“Aux interface” connection for
                                                                  configuration with computer)
                                   ß                              Marking for the position of the light emission level
                                   à                              Bearing marking to support alignment (90° axis)


8024851/1ONO/2024-09-25 | SICK                                                                                                              O P E R A T I N G I N S T R U C T I O N S | TiM3xx          11
Subject to change without notice

3 PRODUCT DESCRIPTION


                                      á           270° aperture angle (visual range)
                                      â           Area in which no reflective surfaces are permitted when the device is mounted




12   O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                          8024851/1ONO/2024-09-25 | SICK
                                                                                                                     Subject to change without notice

PRODUCT DESCRIPTION 3


                                   TiM35x, TiM36x
                                                                                    51 (2.01)

                                                              [Ø                                                                               2x


                                   44.79 (1.76)
                                                            (0. 4.3
                                                               17
                                                                  )]
                                                                                                                              Mounting set 1
                                                                                                   1
                                                            33 (1.3)                               2
                                           16.79   (0.66)



                                                                                                                                  61 (2.40)

                                                                                                   3
                                                                                                   4
                                           85.75 (3.38)                                            5                                                     9                                 à
                                                                                                   6                                                     ß                                 á

                                                                                                       101.12 (3.98)
                                       62.46 (2.46)
                                                                       (0.31)
                                    [24.4
                                                                                                                       8
                                                      27.3
                                   (0.96)]           (1.07)
                                               8                                                                                                                                              (0.96)
                                                                                                                                                                                           24.4

                                                                                0.7 (0.03)
                                          7                                          60 (2.30)                                        å
                                                                                   [68.8 (2.71)]       17.37                                                           51 (2.01)
                                                                                  [76.25 (3.00)]          (0.68)                  46.71 (1.84)
                                                                                                                              74.39 (2.93)
                                                                                       30°                                                                         2               2
                                                                                                   â
                                                     ‒45°                                          225°




                                          0°                                                                           180°
                                                                                                                       ã

                                                                                                                       ä

                                                                                       90°

                                   Figure 2: Structure and dimensions, unit: mm (inch), decimal separator: period
                                   1                         2x fastening clip with M3 x 5 mm countersunk screw, self-locking (included in scope of
                                                             delivery)
                                   2                         M3 threaded mounting hole, 2.8 mm deep (blind hole thread), max. tightening torque
                                                             0.8 Nm
                                   3                         Optics cover
                                   4                         Receiving range (light inlet)
                                   5                         Transmission range (light emission)
                                   6                         Function button for teach-in
                                   7                         Red and green LED (status indicators)
                                   8                         Swivel connector unit with electrical connections
                                   9                         Micro USB port, behind the black plastic cover (“Aux interface” connection for configura‐
                                                             tion with computer)
                                   ß                         Connection for power supply, digital inputs/outputs, 12-pin M12 female connector.
                                   à                         Marking for the position of the light emission level


8024851/1ONO/2024-09-25 | SICK                                                                                                        O P E R A T I N G I N S T R U C T I O N S | TiM3xx          13
Subject to change without notice

3 PRODUCT DESCRIPTION


                                       á           Ethernet connection, 4-pin M12 female connector
                                       â           Area in which no reflective surfaces are permitted when the device is mounted
                                       ã           Bearing marking to support alignment (90° axis)
                                       ä           270° aperture angle (visual range)
                                       å           2 x countersunk screw (Torx TX 6) M2 x 4 mm


3.3           Display and operating elements




                                          1 2 3

                                       Figure 3: Display and operating elements
                                       1           Red LED (status indicator)
                                       2           Green LED (status indicator)
                                       3           Teach-in pushbutton

                                       Status indicators
                                                       LED (red)                  LED (green)                Description
                                                               -                        O                    Device ready/monitoring mode
                                                               O                        O                    Object detection within field/fields (if
                                                                                                             there are lots of object detections in
                                                                                                             a short space of time, the red LED
                                                                                                             lighting up might look like flashing)
                                                               -                       Ö                     Teach-in: start
                                                               O                        O                    Teach-in: End of pre-warning stage,
                                                                                                             60 seconds teach-in stage
                                                               -                       Ö                     Teach-in: End of teach-in phase
                                                               Ö                        -                    Error, start up, firmware update,
                                                                                                             parameterization
                                                               -                        -                    Device without supply voltage

                                             O = illuminated; Ö = flashing


3.4           Type code
                                       The devices of the product family are arranged according to the following type code:
                                        TIM                x        y         z                  ‒           aa        bb            c             dd
                                        1                  2        3         4    5                         6         7             8             9

                                       Table 3: Type code
                                        Position               Description                  Characteristic
                                        1                      Device name                  TIM: Short range 2D-LiDAR sensor
                                        2                      Device type                  3: Field evaluation
                                        3                      Performed by                 1: 4 m measuring range, performance basic
                                                                                            2: 4 m measuring range, performance advanced
                                                                                            5: 10 m measuring range, 1.0° angular resolution,
                                                                                            performance professional
                                                                                            6: 10 m measuring range, 0.33° angular resolution,
                                                                                            performance professional


14    O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                                    8024851/1ONO/2024-09-25 | SICK
                                                                                                                                Subject to change without notice

PRODUCT DESCRIPTION 3


                                   Position     Description                    Characteristic
                                   4            Housing                        0: Housing IP65 without heating
                                   5                                           “Empty”: standard
                                   6            Connection                     01: Cable 12-pin (2.0 m), open strand
                                                                               10: Cable (approx. 0.9 m) with male connector, D-
                                                                               Sub-HD, 15-pin
                                                                               11: Cable (approx. 0.8 m) with M12 male connec‐
                                                                               tor, 12-pin, D-coded
                                   7            Application                    30: Standard field evaluation
                                                                               31: Flexible field evaluation
                                                                               34: Flexible field evaluation with contour fields and
                                                                               particle filters
                                   8            Laser type                     0: Pulse power up to 880 mW, pulse width up to
                                                                               5 ns, pulse rate 500 kHz
                                                                               1: Pulse power up to 880 mW, pulse width up to
                                                                               5 ns, pulse rate 1,500 kHz
                                   9            Color                          00: Blue


3.5                Product identification
                                   The type label gives information for identification of the product variant.

                                          TIM351-2134001                              1
                                                                                      2

                                   8
                                                              1067299
                                                              19160001
                                                                                      3
                                                              9-28V
                                                              16W                     4
                                                                                      5                                                   9
                                                                                      6
                                   7
                                   1      Type code
                                   2      Conformity mark/certification mark, symbol: Observe the operating instructions!
                                   3      Product ID with part number (P/N) and serial number (S/N)
                                   4      Voltage supply, maximum power consumption
                                   5      Production date
                                   6      MAC address
                                   7      Manufacturer/production location
                                   8      QR code with product data (part number, serial number), example: pid.sick.com/
                                          1090608/23000000
                                   9      Conformity mark/certification mark


3.6                Principle of operation

3.6.1              Measurement principle
                                   The device is an opto-electronic LiDAR sensor (laser scanner) that uses laser beams
                                   for non-contact scanning of the outline of its surroundings on a plane. The device meas‐
                                   ures its surroundings in two-dimensional polar coordinates, relative to its measurement
                                   origin. This is marked by a circular indentation in the center of the optics cover. If
                                   a laser beam strikes an object, the position of that object is determined in terms of
                                   distance and direction.




8024851/1ONO/2024-09-25 | SICK                                                             O P E R A T I N G I N S T R U C T I O N S | TiM3xx   15
Subject to change without notice

3 PRODUCT DESCRIPTION




                                         Figure 4: The 2D LiDAR sensor measurement principle


3.6.2           Distance measurement
                                         The device emits beams pulsed by a laser diode. If a laser pulse hits an object or
                                         person, it is reflected on the surface of the object or person in question. The reflec‐
                                         tion is registered by a photosensitive element in the device receiver. The device uses
                                         SICK’s own HDDM/HDDM+ (High Definition Distance Measurement) technology. With
                                         this measurement process, a measured value is formed by adding together multiple
                                         single pulses. The device calculates the distance from the object based on the elapsed
                                         time that the light requires between emitting the beam and receiving the reflection.
                                         Radar systems apply this “pulse time-of-flight measurement” principle in a similar way.

3.6.3           Direction measurement
                                         The device uses a rotating mirror to deflect the emitted laser beams, thereby scanning
                                         its surroundings in a circular pattern. The measurements are triggered internally by an
                                         encoder in regular angle increments.
                                         The measuring procedure uses the averaging from multiple pulses to determine individ‐
                                         ual measured values. A measuring point is the average value of several measurements
                                         combined.

                                                                                               2




                                                                   1

                                         1           Device
                                         2           Laser pulse



16      O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                8024851/1ONO/2024-09-25 | SICK
                                                                                                              Subject to change without notice

PRODUCT DESCRIPTION 3


3.6.4              Object sizes
                                   As the distance from the device increases, the laser beam expands. As a result, the
                                   diameter of the light spot on the surface of the object increases.
                                                                                                                          1
                                                                                                                                            2


                                   Figure 5: Beam expansion
                                   1     Expanded laser beam
                                   2     Optical axis

                                   Required values for calculating the light spot size and minimum object size:
                                   • Light spot size on the device cover: 7 mm (rounded up)
                                   • Light spot divergence per single pulse: 0.49 deg (8.6 mrad)
                                   • supplement HDDM/HDDM+ (1 measured value consists of several overlapping
                                       single pulses): 5.8 mrad for devices with 0.33° angular resolution; 17.5 mrad for
                                       devices with 1° angular resolution
                                   Formula for calculating the light spot width:
                                   (Light spot divergence [mrad] + supplement [mrad]) * distance [mm] + light spot size
                                   on the device cover [mm] = light spot width [mm]
                                   Calculation example of light spot width at a distance of 4 m, with supplement 5.8 mrad:
                                   (8.6 mrad +5.8 mrad) * 4,000 mm +7 mm = 64.6 mm
                                   Formula for calculating the height of the light spot:
                                   Light spot divergence [mrad] * Distance [mm] + Light spot size at the device cover
                                   [mm] = Light spot width [mm]
                                   Example calculation of the light spot height at a distance of 4 m:
                                   8.6 mrad * 4,000 mm +7 mm = 41.4 mm
                                   Formula for calculating the minimum object size:
                                   2 * supplement [mrad] * distance [mm] + light spot height [mm] = minimum object
                                   size [mm]
                                   Calculation example of minimum object size at a distance of 4 m, with supplement
                                   5.8 mrad:
                                   2 * 5.8 mrad * 4,000 mm + 41.4 mm = 87.8 mm




8024851/1ONO/2024-09-25 | SICK                                                         O P E R A T I N G I N S T R U C T I O N S | TiM3xx   17
Subject to change without notice

3 PRODUCT DESCRIPTION

                                         Size in mm (inch) 1                                                   Size in mm (inch) 1
                                              250                                                                   500
                                              (9.8)                                                                (19.7)



                                              200                                                                   400
                                              (7.9)                                                                (15.7)



                                              150                             3                                     300                          3
                                              (5.9)                                                                (11.8)


                                                                              4
                                              100                                                                   200                          4
                                              (3.9)                                                                 (7.9)
                                                                                     5
                                               50                                                                   100
                                              (2.0)                                                                 (3.9)
                                                                                                                                                 5

                                                0                                                                     0
                                                    0        2.5       5       7.5          10        12.5                0     2.5       5          7.5        10        12.5
                                                             (8.2)   (16.4)   (24.6)       (32.8)    (41.0)                     (8.2)   (16.4)    (24.6)       (32.8)    (41.0)

                                                                                       Distance in m (ft) 2                                                Distance in m (ft) 2

                                         Figure 6: Minimum object size TiM36x                                  Figure 7: Minimum object size TiM31x/TiM32x
                                                                                                               (max. distance: 4 m) and TiM35x
                                         1              Size in millimeters (inc)
                                         2              Distance in meters (feet)
                                         3              Minimum object size
                                         4              Light spot width
                                         5              Light spot height

3.6.5           Scan field flatness (conical error and tilt)
                                         The scan field flatness describes the production-related vertical deviation of the hori‐
                                         zontal scan plane of the sensor. Conical errors and tilt can affect the three-dimensional
                                         measurements. This should be taken into consideration to ensure reliable measure‐
                                         ment results. Conical errors can only be corrected for a small viewing range. Tilt errors
                                         can be compensated for in many cases by mounting the sensor at a compensating
                                         angle. An alignment aid (e.g. item no.: 2086761) can help to position the sensor
                                         precisely and avoid alignment errors.

3.6.6           Impact of object surfaces on the measurement
                                         Remission value
                                         Remission is the ability of a material to reflect light. The remission correlates with the
                                         amount of laser light emitted by the LiDAR sensor which is reflected by an object (see
                                         Lambert’s law).
                                         Glossy surfaces have different remissions at the same distance with different angles of
                                         impact. In the case of shiny surfaces, maximum remission is achieved when the beam
                                         makes vertical impact.
                                         Matt and dull surfaces have diffuse remission. They therefore exhibit similar relative
                                         remissions with the same angle of impact regardless of the distance from the zero
                                         point.
                                         Table 4: Typical remissions of frequently used materials
                                          Material                                                            Typ. relative remission
                                          Rubber tires (vulcanized, black)                                    2%
                                          Foam rubber (black)                                                 2.4%
                                          Photographic board (black, matte)                                   10%
                                          Cardboard (gray)                                                    20%
                                          Wood (untreated fir, soiled)                                        40%


18      O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                                                8024851/1ONO/2024-09-25 | SICK
                                                                                                                                              Subject to change without notice

PRODUCT DESCRIPTION 3


                                   Material                                           Typ. relative remission
                                   PVC (gray)                                         50%
                                   Paper (white, matte)                               80%
                                   Plaster (white)                                    100%
                                   Aluminum (black anodized)                          110 … 150%
                                   Steel (stainless, shiny)                           120 … 150%
                                   Steel (high gloss)                                 140 … 200%

                                   Reflection
                                   Most surfaces produce a diffuse reflection of the laser beam in all directions. The
                                   structure (smooth or rough), shape (flat or curved), and color (light or dark) of the
                                   surface determine how well the laser beam is reflected.
                                   On very rough surfaces, a large proportion of the energy is lost due to absorption.
                                   Curved surfaces produce a higher diffusion. Dark surfaces reflect the laser beam worse
                                   than light ones (brilliant white plaster reflects approx. 100% of the light, while black
                                   foam rubber reflects approx. 2.4%). The aforementioned surface characteristics can
                                   reduce the scanning range of the device, in particular for surfaces with low remission
                                   values.




                                   Figure 8: Reflection of light on the surface of the object

                                   Angle of reflection
                                   The angle of reflection corresponds to the angle of incidence. If the laser beam hits
                                   a surface at right angles, the energy is optimally reflected. If the laser beam hits a
                                   surface at an oblique angle, energy and range are lost accordingly.




                                   Figure 9: Angle of reflection

                                   Retroreflection
                                   If the reflective energy is greater than 100%, the beam is not reflected diffusely in all
                                   directions; instead it is reflected in a targeted way (retroreflection). Thus a large part of
                                   the emitted energy can be received by the laser distance measurer. Plastic reflectors
                                   (cat’s eyes), reflective tape, and triple prisms have these properties.




8024851/1ONO/2024-09-25 | SICK                                                                  O P E R A T I N G I N S T R U C T I O N S | TiM3xx   19
Subject to change without notice

3 PRODUCT DESCRIPTION




                                         Figure 10: Retroreflection

                                         Reflective surfaces
                                         The laser beam is almost completely deflected on reflective surfaces. This means that
                                         an object hit by the deflected beam may be detected instead of the reflective surface.




                                         Figure 11: Specular surfaces

                                         Small objects
                                         Objects that are smaller than the diameter of the laser beam cannot reflect the laser
                                         light’s full energy. The portion of the light beam that does not reach the object is lost. If
                                         all of the light reflected to the sensor is insufficient, the object may not be detected.
                                         The portion of the light that does not reach the front object can be reflected by a larger
                                         object in the background. If all of the light reflected to the sensor is sufficient, this
                                         object is detected. This can lead to a corruption of the measured value.




                                         Figure 12: Object smaller than the laser beam diameter


3.6.7           Scanning range
                                         The scanning range of the device depends on the remission of the object to be
                                         detected. The better a surface reflects the incident beam back to the device, the
                                         greater the scanning range of the device.




20      O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                    8024851/1ONO/2024-09-25 | SICK
                                                                                                                  Subject to change without notice

PRODUCT DESCRIPTION 3


                                   Object remission in % 1                                                          Object remission in % 1
                                   100                                                                            100
                                    90                                                                               90
                                    80                                                                               80
                                    70                                                                               70
                                    60                                                                               60
                                    50                                                                               50
                                    40                                                                               40
                                    30                                                                               30
                                    20                                                                               20
                                    10                                                                               10
                                     0                                                                                0
                                         0   0.5     1.0     1.5     2.0     2.5     3.0      3.5    4.0    4.5           0        2          4         6            8          10     12
                                             (1.6)   (3.3)   (4.9)   (6.6)   (8.2)   (9.8)   (11.5) (13.1) (14.8)                 (6.6)     (13.1)    (19.7)       (26.2)    (32.8)   (39.4)

                                                                                Measuring range in m (ft) 2                                                    Measuring range in m (ft) 2

                                   Figure 13: Scanning range as a function of                                     Figure 14: Scanning range as a function of
                                   object remission, TiM31x / TiM32x                                              object remission, TiM35x / TiM36x
                                   1          Object remission in percent                                         1           Object remission in percent
                                   2          Measuring range in meters (feet)                                    2           Measuring range in meters (feet)


3.6.8              Filter
                                   The device has digital filters for pre-processing and optimizing the measured distance
                                   values. They enable the device to be adapted to meet the specific requirements of the
                                   respective application.
                                   The filters can be combined without restrictions. If several filters are active, then the
                                   filters are applied sequentially to the results of the preceding filter. The processing
                                   sequence is as follows:
                                    • Edge filter
                                    • Particle filter
                                    • Average filter
                                   The active filter functions affect the output measured values. It is not possible to recal‐
                                   culate the original measured values from the filtered output values. For this reason,
                                   certain combinations of filters might not be advisable.
                                   A particularly effective way to reduce the data in a scan (reduction of measurement
                                   points) is to restrict the scan range (“Data output” > “Output range”) or the media filter.

3.6.8.1            Edge filter
                                   The edge filter eliminates erroneous or extreme distance values at edges. These arise
                                   as a result of laser light that partially hits an object in the front and partially hits an
                                   object farther away, or due to too little light remission at the object itself, see "Impact
                                   of object surfaces on the measurement", page 18. The filter evaluates the difference in
                                   distance between adjacent points.
                                   The previous and next measurement point are taken into consideration in this. As soon
                                   as the configured maximum adjacent distance to the previous and next measurement
                                   point is exceeded, the device sets the distance value to 0 (value highlighted in see
                                   table 5, page 21 bold). If the maximum adjacent distance is not exceeded, or only
                                   exceeded to one of the adjacent measurement points, the measurement point is not
                                   filtered. If the measurement point or one of the adjacent measurement points is 0, then
                                   the filter is not applied to this measurement point.
                                   Table 5: Example: Measured values with and without edge filter
                                                                                             Measurement points (distance values in mm)
                                                                              1               2              3                4              5                 6            7           …
                                   not filtered                        1800            1750            1145               1150            1147         800               871            …


8024851/1ONO/2024-09-25 | SICK                                                                                                O P E R A T I N G I N S T R U C T I O N S | TiM3xx        21
Subject to change without notice

3 PRODUCT DESCRIPTION

                                                                                  Measurement points (distance values in mm)
                                                                          1        2           3            4            5       6             7             …
                                            filtered               1800       1750         1145         1150        1147         0         871               …

                                           The edge filter enables points to be entirely suppressed at the outer edges of the
                                           object.

                                           Maximum edge filter range (range limitation)
                                           The maximum distance can be set to 8,000 mm 1). The measurement points within the
                                           configured range are taken into account.

3.6.8.2           Particle filter
                                           The particle filter blanks small, irrelevant reflection pulses in dusty environments and in
                                           rain or snow which are caused by dust particles, raindrops, snowflakes or the like.
                                           In doing so, successive scans are continuously evaluated in order to detect static
                                           objects.




                                                       !                                                        "




                                           Figure 15: Without the particle filter: Violation           Figure 16: Using the particle filter: The
                                           of the contour due to dust particles in the                 response to dust particles in the detection
                                           vicinity of the object.                                     field is delayed by one scan. Particles can
                                                                                                       thereby be blanked.


3.6.8.3           Average filter
                                           The sliding average filter smooths the distance value. It does this by calculating the
                                           arithmetic mean from several scans of the same point. The number of scans can be
                                           configured (maximum 4 scans).
                                           Table 6: Example: Average filter over 5 scans
                                                                                           Angle (distance values in mm)
                                            Scan                      1       2        3           4        5        6       7         8           9         …
                                            1                         0       0 1100 1100 1150 1150 1380 1380                                      0         …
                                            2                         0       0 1200 1200 1190                      950 1500 1500                  0         …
                                            3                         0       0 1150 1450 1200 1200 1450 1450                                      0         …
                                            4                         0       0 1170 1170 1220 1220 1470 1150                                      0         …
                                            1 Output value            0       0 1155 1230 1190 1130 1450 1370                                      0         …
                                            (scan 1-4)
                                            5                         0       0        0 1110 1150 1150 1380 1380                                  0         …
                                            2. Output value           0       0 1173 1225 1190 1130 1450 1370                                      0
                                            (scan 2-5)
                                            6                         0       0 1200 1210 1190                       0 1500 1500                   0         …


1)   For the variants TiM310 / TiM320, the maximum distance can be set to 4,000 mm.

22        O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                                 8024851/1ONO/2024-09-25 | SICK
                                                                                                                                 Subject to change without notice

PRODUCT DESCRIPTION 3


                                                                              Angle (distance values in mm)
                                   Scan                    1      2       3        4      5           6            7           8            9   …
                                   3. Output value         0      0 1173 1235 1190 1190 1450 1370                                           0
                                   (scan 3-6)
                                   7                       0    730 1150           0 1200 1200 1450 1450                                    0   …
                                   4. Output value         0    730 1173 1163 1190 1190 1450 1370                                           0
                                   (4-7)
                                   …                      …       …       …       …       …          …            …            …            …   …

                                   Individual outliers (shown in bold in the table) influence the average value.
                                   Once the measured value telegram has been confirmed, the first measured value is
                                   not output until after the configured number of scans. Therefore, there is always a time
                                   delay equivalent to the number of scans configured for averaging. The digit of the first
                                   scan included in the averaging calculation is always output in the scan counter. Invalid
                                   distance values (= 0) are not included in the averaging calculation, so that in these
                                   places a smaller number of scans is used in the division calculation.
                                   Based on the scanning frequency of 15 Hz, a measured value is generated every
                                   67 s. The time delay affecting data output results from this base value multiplied
                                   by the number of averaging operations (e.g., 2 averaging operations = 134 ms,
                                   10 averaging operations = 670 ms).

3.6.9              Calculation of the field size for mobile applications
                                   In order to prevent collisions between vehicles, and between vehicles and fixed objects,
                                   the switching field must have sufficient length and width.
                                   To calculate the switching field length, you need to take into consideration the stop‐
                                   ping distance of the vehicle. This comprises the following:
                                   • the braking distance, which can be found in the vehicle documentation
                                   • the distance covered during the vehicle control’s response time, which can be
                                        found in the vehicle documentation
                                   • The distance covered during the response time of the LiDAR sensor, "Technical
                                        data", page 55.

                                   NOTE
                                   •    We recommend adding a supplement of at least 100 mm to the protective field
                                        length in order to stop the vehicle before a possible collision.
                                   •    If retro-reflectors are situated in the path of the vehicles, or if you anticipate that
                                        the braking force of the vehicle will diminish over time, you may, under certain
                                        circumstances, need to increase the recommended supplement.
                                   •    The width of the switching field should cover the vehicle width. You should also
                                        configure a supplement of at least 100 mm on every side.

                                   Mounting height
                                   The recommended mounting height for mobile applications is at least 150 mm.

3.6.9.1            Switching field length
                                   You must configure the switching field so that a minimum distance to the vehicle is
                                   maintained at all times. This ensures that a vehicle monitored by the LiDAR sensor
                                   stops before an object is reached. You can define multiple monitoring cases each with
                                   different switching fields. These can be switched over dynamically via static control
                                   inputs, for example to adjust the protective field size based on the vehicle speed.
                                   In this kind of application, you must calculate the switching field sizes (in particular the
                                   switching field lengths) for all speeds.

8024851/1ONO/2024-09-25 | SICK                                                             O P E R A T I N G I N S T R U C T I O N S | TiM3xx   23
Subject to change without notice

3 PRODUCT DESCRIPTION

                                      The switching field length SL can be calculated using the following formula (guideline
                                      values based on a pixel calculation):
                                      SL = SA + ZG + ZR + ZB
                                      SA = Stopping distance
                                      ZG = General supplement of the LiDAR sensor = 100 mm
                                      ZR = Supplement for application-related influences or the selected application parame‐
                                      ters
                                      ZB = Supplement for the decreasing braking force of the vehicle. This can be obtained
                                      from the relevant vehicle documentation, or alternatively: 10% of the stopping distance.

                                      Stopping distance SA
                                      The stopping distance comprises the vehicle’s braking distance and the distance cov‐
                                      ered during the response time of the LiDAR sensor and the vehicle control’s response
                                      time.




                                                                     2      3               4

                                                                                     1

                                      Figure 17: Stopping distance
                                      1           SA
                                      2           SAnF
                                      3           SAnS
                                      4           SBr


                                      NOTE
                                      Please note that a vehicle’s braking distance does not increase linearly with increasing
                                      speed, but rather in a squared relationship. This is particularly important if you switch
                                      between different-sized switching fields depending on the speed.

                                      How to calculate the stopping distance SA:
                                      SA = SAnF + SAnS + SBr
                                      SAnF = The distance covered during the vehicle control’s response time, which is speci‐
                                      fied in the vehicle documentation
                                      SAnS = The distance covered during the response time of the LiDAR sensor
                                      SBr = The braking distance, found in the vehicle documentation
                                      The distance SAnS covered during the response time of the LiDAR sensor depends on:
                                      • the response time of the LiDAR sensor
                                      • the maximum speed of the vehicle in your mobile application
                                      For more information on the response time TS of the LiDAR sensor, see "Technical data",
                                      page 55.




24   O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                  8024851/1ONO/2024-09-25 | SICK
                                                                                                             Subject to change without notice

PRODUCT DESCRIPTION 3


                                   How to calculate the distance SAnS covered during the response time of the LiDAR
                                   sensor:
                                   SAnS = TS × Vmax
                                   TS = Response time of the LiDAR sensor
                                   Vmax Maximum speed of the vehicle, from the relevant vehicle documentation
                                   The response time TS of the LiDAR sensor depends on:
                                   • the base response time of the LiDAR sensor
                                   • whether multiple sampling is set
                                   • Filter settings (e.g., particle filter)
                                   ZR supplement
                                   This supplement must be determined on an application-specific basis and taken into
                                   account appropriately. The following factors can make it necessary to use a supple‐
                                   ment: reflectors or shiny objects on the scan plane, multi-echo analysis, blanking size,
                                   device filter (e.g., particle filter).

3.6.9.2            Switching field width
                                   The width of the switching field must cover the width of the vehicle and take into
                                   account the supplements for the measurement error.
                                   The switching field width SB can be calculated using the following formula (guideline
                                   values based on a pixel calculation):
                                   SB = FB + 2 × (ZG + ZR)
                                   FB = Vehicle width
                                   ZG = General supplement of the LiDAR sensor = 100 mm
                                   ZR = Supplement for application-related influences or the selected application parame‐
                                   ters




8024851/1ONO/2024-09-25 | SICK                                                         O P E R A T I N G I N S T R U C T I O N S | TiM3xx   25
Subject to change without notice

4 TRANSPORT AND STORAGE


4             Transport and storage
4.1           Transport

                                       NOTICE
                                       Damage due to improper transport!
                                       ■        The product must be packaged with protection against shock and damp.
                                       ■        Recommendation: Use the original packaging.
                                       ■        Note the symbols on the packaging.
                                       ■        Do not remove packaging until immediately before you start mounting.


4.2           Unpacking
                                       •        To protect the device against condensation, allow it to equilibrate with the ambient
                                                temperature before unpacking if necessary.
                                       •        Handle the device with care and protect it from mechanical damage.
                                       •        To avoid ingress of dust and water, only remove the protective elements, e.g.
                                                protective caps of the electrical connections just before attaching the connecting
                                                cable.

4.3           Transport inspection
                                       Immediately upon receipt in Goods-in, check the delivery for completeness and for any
                                       damage that may have occurred in transit. In the case of transit damage that is visible
                                       externally, proceed as follows:
                                       •        Do not accept the delivery or only do so conditionally.
                                       •        Note the scope of damage on the transport documents or on the transport compa‐
                                                ny's delivery note.
                                       •        File a complaint.

                                       NOTE
                                       Complaints regarding defects should be filed as soon as these are detected. Damage
                                       claims are only valid before the applicable complaint deadlines.


4.4           Storage
                                       •        Electrical connections are provided with a protective cap.
                                       •        Do not store outdoors.
                                       •        Store in a place protected from moisture and dust.
                                       •        Recommendation: Use the original packaging.
                                       •        To allow any residual dampness to evaporate, do not package in airtight contain‐
                                                ers.
                                       •        Do not expose to any aggressive substances.
                                       •        Protect from sunlight.
                                       •        Avoid mechanical shocks.
                                       •        Storage temperature: see "Technical data", page 55.
                                       •        Relative humidity: see "Technical data", page 55.
                                       •        For storage periods of longer than 3 months, check the general condition of all
                                                components and packaging on a regular basis.




26    O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                     8024851/1ONO/2024-09-25 | SICK
                                                                                                                 Subject to change without notice

MOUNTING 5


5                  Mounting
5.1                Mounting instructions
                                   •    Observe the technical data.
                                   •    Protect the sensor from direct and indirect sunlight.
                                   •    To prevent condensation, avoid exposing the device to rapid changes in tempera‐
                                        ture.
                                   •    The mounting site has to be designed for the weight of the device.
                                   •    The device can be mounted in any position.
                                   •    It should be mounted so that it is exposed to as little shock and vibration as possi‐
                                        ble. Optional mounting accessories are available, see "Accessories", page 59.
                                   •    In application areas with severe vibrations or shocks caused by vibrations,
                                        jolts or abrupt changes in directions (e.g., when mounted to a manned forklift
                                        truck), mounting with vibration dampers is to be carried out (see "Accessories",
                                        page 59). Mount the device in a freely suspended manner.
                                   •    When mounting the device, make sure there are no reflective surfaces behind the
                                        reference target, see "Setup and dimensions", page 11.
                                   •    When mounting the device, make sure the swivel connector area is recessed so it
                                        does not lie on the mounting surface see "Setup and dimensions", page 11.
                                   •    To avoid inaccurate measurements when installing multiple devices: Make sure
                                        that the laser spot of one device is not in the visible range of another device, see
                                        "Mutual interference", page 28.
                                   •    Avoid having shiny or reflective surfaces in the scanning range, e.g., stainless
                                        steel, aluminum, glass, reflectors, or surfaces with these types of coatings.
                                   •    Protect the device from moisture, contamination, and damage.
                                   •    Make sure that the status indicator is clearly visible.
                                   •    Do not subject the device to excessive shock or vibrations. In systems subjected to
                                        heavy vibrations, secure the fixing screws with screw-locking devices.
                                   •    The M3 x 5 screws included with delivery are intended for mounting the fastening
                                        clips via the blind hole threads on the rear or underside of the device, see "Setup
                                        and dimensions", page 11. If the mounting clamps are not used or if other screws
                                        are used, the screws must not be screwed into the thread by more than 2.8 mm.
                                        The maximum tightening torque is 0.8 Nm.

5.2                Mounting device
                                   1.   Mount the LiDAR sensor using the designated fixing holes, see "Setup and dimen‐
                                        sions", page 11.
                                        NOTICE
                                        Risk of damage to the device
                                        the device will be damaged if the tightening torque of the mounting screws is too
                                        high or if the maximum screw-in depth of the blind hole threads is exceeded.
                                        ►    Observe maximum tightening torque.
                                        ►    Use suitable mounting screws for the blind hole threads of the device.
                                             Observe the maximum screw-in depth.

                                   2.   Make the electrical connection. Attach and tighten a voltage-free cable, see "Con‐
                                        necting the device electrically", page 37 .
                                   3.   Switch on the supply voltage.
                                   ✓    The green operating LED lights up.
                                   4.   Align the vertical center line of the field of view of the device with the center of the
                                        area to be monitored. The marking (90° axis) on the upper side of the optics cover
                                        serves as a alignment aid.



8024851/1ONO/2024-09-25 | SICK                                                           O P E R A T I N G I N S T R U C T I O N S | TiM3xx   27
Subject to change without notice

5 MOUNTING

5.3           Mutual interference

                                       NOTE
                                       Optical sensors and other IR light sources can influence the measurement and detec‐
                                       tion capabilities of the device.

                                       The device has been designed to minimize the probability of mutual interference with
                                       devices of the same type. To rule out even the slightest effects on the measurement
                                       accuracy, the devices should be arranged such the laser beams are not received by
                                       another device.




                                       Figure 18: Angle ≥ 6°




                                       Figure 19: Distance ≥ 200 mm




28    O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                               8024851/1ONO/2024-09-25 | SICK
                                                                                                           Subject to change without notice

ELECTRICAL INSTALLATION 6


6                  Electrical installation
6.1                Prerequisites for safe operation of the device

                                   WARNING
                                   Risk of injury and damage caused by electrical current!
                                   As a result of equipotential bonding currents between the device and other grounded
                                   devices in the system, faulty grounding of the device can give rise to the following
                                   dangers and faults:
                                   •    Dangerous voltages are applied to the metal housings.
                                   •    Devices will behave incorrectly or be destroyed.
                                   •    Cable shielding will be damaged by overheating and cause cable fires.
                                   Remedial measures
                                   •    Only skilled electricians should be permitted to carry out work on the electrical
                                        system.
                                   •    If the cable insulation is damaged, disconnect the voltage supply immediately and
                                        have the damage repaired.
                                   •    Ensure that the ground potential is the same at all grounding points.
                                   •    Where local conditions do not meet the requirements for a safe earthing method,
                                        take appropriate measures. For example, ensure low-impedance and current-carry‐
                                        ing equipotential bonding.

                                   The device is connected to the peripheral devices (any local trigger sensor(s), system
                                   controller) via shielded cables. The cable shield – for the data cable, for example –
                                   rests against the metal housing of the device.
                                   The device can be grounded through the cable shield or through a blind tapped hole in
                                   the housing, for example.
                                   If the peripheral devices have metal housings and the cable shields are also in contact
                                   with their housings, it is assumed that all devices involved in the installation have the
                                   same ground potential.
                                   This is achieved by complying with the following conditions:
                                   ■    Mounting the devices on conductive metal surfaces
                                   ■    Correctly grounding the devices and metal surfaces in the system
                                   ■    If necessary: low-impedance and current-carrying equipotential bonding between
                                        areas with different ground potentials




8024851/1ONO/2024-09-25 | SICK                                                         O P E R A T I N G I N S T R U C T I O N S | TiM3xx   29
Subject to change without notice

6 ELECTRICAL INSTALLATION

                                                 1                                         2                                              3


                                              System                                       SICK
                                             Controller                                   Device                                    Power Supply




                                                                        I

                                                                                                                   =8
                                                                                                                   =9


                                                7           6       U            5         4

                                       Figure 20: Example: Occurrence of equipotential bonding currents in the system configuration
                                       1           System controller
                                       2           Device
                                       3           Voltage supply
                                       4           Grounding point 2
                                       5           Closed current loop with equalizing currents via cable shield
                                       6           Ground potential difference
                                       7           Grounding point 1
                                       8           Metal housing
                                       9           Shielded electrical cable

                                       If these conditions are not fulfilled, equipotential bonding currents can flow along the
                                       cable shielding between the devices due to differing ground potentials and cause the
                                       hazards specified. This is, for example, possible in cases where there are devices within
                                       a widely distributed system covering several buildings.
                                       Remedial measures
                                       The most common solution to prevent equipotential bonding currents on cable shields
                                       is to ensure low-impedance and current-carrying equipotential bonding. If this equipo‐
                                       tential bonding is not possible, the following solution approaches serve as a suggestion.

                                       NOTICE
                                       We expressly advise against opening up the cable shields. This would mean that the
                                       EMC limit values can no longer be complied with and that the safe operation of the
                                       device data interfaces can no longer be guaranteed.

                                       Measures for widely distributed system installations
                                       On widely distributed system installations with correspondingly large potential differen‐
                                       ces, the setting up of local islands and connecting them using commercially available
                                       electro-optical signal isolators is recommended. This measure achieves a high degree
                                       of resistance to electromagnetic interference.




30    O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                            8024851/1ONO/2024-09-25 | SICK
                                                                                                                        Subject to change without notice

ELECTRICAL INSTALLATION 6


                                       1                      2                   2                            3                                 4

                                                            Electro-            Electro-
                                     System                  optical             optical                      SICK                              Power
                                    Controller               signal              signal                      Device                             Supply
                                                            isolator            isolator




                                                 6                                                            5

                                       =7          =8             =9

                                   Figure 21: Example: Prevention of equipotential bonding currents in the system configuration by
                                   the use of electro-optical signal isolators
                                   1        System controller
                                   2        Electro-optical signal isolator
                                   3        Device
                                   4        Voltage supply
                                   5        Grounding point 2
                                   6        Grounding point 1
                                   7        Metal housing
                                   8        Shielded electrical cable
                                   9        Optical fiber

                                   The use of electro-optical signal isolators between the islands isolates the ground loop.
                                   Within the islands, a stable equipotential bonding prevents equalizing currents on the
                                   cable shields.
                                   Measures for small system installations
                                   For smaller installations with only slight potential differences, insulated mounting of the
                                   device and peripheral devices may be an adequate solution.




8024851/1ONO/2024-09-25 | SICK                                                             O P E R A T I N G I N S T R U C T I O N S | TiM3xx            31
Subject to change without notice

6 ELECTRICAL INSTALLATION

                                                    1                             2                                  3



                                               System                             SICK
                                              Controller                                                      Power Supply
                                                                                 Device




                                                                                                   5



                                                  8                    U         6                                  4
                                                            7

                                              =9            =ß

                                       Figure 22: Example: Prevention of equipotential bonding currents in the system configuration by
                                       the insulated mounting of the device
                                       1           System controller
                                       2           Device
                                       3           Voltage supply
                                       4           Grounding point 3
                                       5           Insulated mounting
                                       6           Grounding point 2
                                       7           Ground potential difference
                                       8           Grounding point 1
                                       9           Metal housing
                                       ß           Shielded electrical cable

                                       Even in the event of large differences in the ground potential, ground loops are effec‐
                                       tively prevented. As a result, equalizing currents can no longer flow via the cable shields
                                       and metal housing.

                                       NOTICE
                                       The voltage supply for the device and the connected peripheral devices must also
                                       guarantee the required level of insulation.
                                       Under certain circumstances, a tangible potential can develop between the insulated
                                       metal housings and the local ground potential.




32    O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                      8024851/1ONO/2024-09-25 | SICK
                                                                                                                  Subject to change without notice

ELECTRICAL INSTALLATION 6


6.2                Electrical block diagram for commissioning
                                   TiMxxx-01xxxxx
                                                        Customer-provided 1

                                                    OUT 1 OUT 2 OUT 3 OUT 4                                       USB




                                                                                                                        SOPAS
                                   Delay-                                                            "USB 2.0"
                                                        Connection box 4
                                   action
                                   fuse                                                                Device 2
                                   0.8 A                                                                            Configuration
                                                                                                                   Field monitoring
                                   6                                                                                  Diagnosis
                                                   IN 1 IN 2 IN 3 IN 4 PNP:                                               3
                                                                      INGND
                                            Vs 5                       NPN: "Power/I/O"
                                                                        Vs

                                   Figure 23: "Power, I/O" connection: Cable with open end
                                   1          Connection modules
                                   2          Device
                                   3          Configuration, field monitoring or diagnostics
                                   4          Supply voltage Vs

                                   TiMxxx-10xxxxx
                                   IN 1            33                                    20    OUT 1
                                   IN 2            43                                    21    OUT 2
                                                           CDB730-001
                                   IN 3            30      Connection                    10    OUT 3
                                   IN 4            31        module                      13    OUT 4       USB

                                   SGND            12             1                      22    GND
                                                                       OUT 4

                                                                 ...
                                                                       OUT 3
                                                                       OUT 2
                                                                       OUT 1
                                                                 ...                                              SOPAS
                                                                                               "USB 2.0"
                                                                               6   1    5 10

                                                         1 2                                    Device 2
                                                                                                             Configuration
                                                                                   11   15                  Field monitoring
                                                           GND                                                 Diagnosis
                                                        Vs 4                                                       3
                                                                               "Power/I/O"


                                   Figure 24: “Power, I/O” connection: Cable with 15-pin D-Sub-HD male connector
                                   1          Connection modules
                                   2          Device
                                   3          Configuration, field monitoring or diagnostics
                                   4          Supply voltage Vs




8024851/1ONO/2024-09-25 | SICK                                                                                                 O P E R A T I N G I N S T R U C T I O N S | TiM3xx   33
Subject to change without notice

6 ELECTRICAL INSTALLATION

                                       TiMxxx-11xxxxx
                                                              Customer-provided 1        4
                                                                                             3   2
                                                                                      11              1
                                                           OUT 1 OUT 2 OUT 3 OUT 4     5                  10          USB
                                                                                                          9
                                                                                       6
                                                                                                      8
                                                                                             7   12

                                                                                                                            SOPAS
                                                                                                          "USB 2.0"
                                       Delay-                 Connection box 4
                                       action                                                             Device 2
                                       fuse                                                                            Configuration
                                       0.8 A                                                                          Field monitoring
                                       6                                                                                 Diagnosis
                                                           IN 1 IN 2 IN 3 IN 4 PNP:                                          3
                                                                              INGND
                                                Vs 5                           NPN: "Power/I/O"
                                                                                Vs

                                       Figure 25: “Power//I/O” connection: Cable with 12-pin A-coded M12 male connector
                                       1           Provided by customer
                                       2           Device
                                       3           Configuration, field monitoring or diagnostics
                                       4           Connecting device
                                       5           Supply voltage Vs
                                       6           Fuse 0.8 A, slow-acting


6.3           Wiring instructions

                                       NOTE
                                       Pre-assembled cables can be found on the product page.
                                       The product page can be accessed via the SICK Product ID: pid.sick.com/{P/N}/{S/N}
                                       {P/N} corresponds to the part number of the product, see type label.
                                       {S/N} corresponds to the serial number of the product, see type label (if indicated).


                                       NOTICE
                                       Faults during operation and defects in the device or the system
                                       Incorrect wiring may result in operational faults and defects.
                                       ■         Follow the wiring notes precisely.

                                       The enclosure rating stated in the technical data is achieved only with screwed plug
                                       connectors or protective caps.
                                       Protect the device from dust and moisture when the plastic USB cover is open.
                                       The USB interface is only for parameterization. Remove the USB cable for problem-free
                                       operation of the device.
                                       All circuits connected to the device must be configured as SELV or PELV circuits. SELV =
                                       safety extra-low voltage, PELV = protective extra-low voltage.
                                       Protect the device with an external 0.8 A slow-blow fuse at the beginning of the supply
                                       cable.
                                       When operating the device together with a connection module, observe the operating
                                       instructions of the connection module!
                                       Connect the connecting cables in a de-energized state. Do not switch on the supply
                                       voltage until installation is complete and all connecting cables are connected to the
                                       device and control.
                                       Wire cross-sections in the supply cable from the customer’s power system must be
                                       implemented in accordance with the applicable standards.



34    O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                                                 8024851/1ONO/2024-09-25 | SICK
                                                                                                                                             Subject to change without notice

ELECTRICAL INSTALLATION 6


6.4                Connection diagram

                                   NOTE
                                   The recommended connecting cables and their associated technical data can be found
                                   on the online product page.
                                   The product page can be accessed via the SICK Product ID: pid.sick.com/{P/N}/{S/N}
                                   {P/N} corresponds to the part number of the product, see type label.
                                   {S/N} corresponds to the serial number of the product, see type label (if indicated).


6.4.1              TiMxxx-01xxxxx
                                   “Power/I/O” connection

                                   NOTE
                                   All products with the type code TiM3xx-01xxxxx are intended to be operated with
                                   flying leads. For production-related reasons, individual product variants with this type
                                   code are delivered with a 15-pin D-Sub HD male connector. For these products, the
                                   customer is responsible for cutting off the male connector and creating the cable end.
                                   Alternatively, the products may be operated with a male connector. In this case, the
                                   information for the product variants with the type code TiMxxx-10xxxxx applies for the
                                   PIN assignment.

                                   Table 7: Connecting cable 15-wire with open end
                                   Signal               Function                                                   Wire color
                                   VS                   Supply voltage                                             Red
                                   N.c.                 –                                                          Violet
                                   N.c.                 –                                                          Yellow
                                   OUT 4                Digital output 4 (index/error)                             Red and black
                                   GND                  Ground                                                     Black
                                   N.c.                 –                                                          Light blue
                                   N.c.                 –                                                          Dark blue
                                   IN 1                 Digital input 1 (field set selection)                      Turquoise or light gray
                                   IN 2                 Digital input 2 (field set selection)                      Green
                                   IN 3                 Digital input 3 (field set selection)                      Gray
                                   IN 4                 Digital input 4 (field set selection)                      Pink
                                   OUT 1                Digital output 1 (object detection)                        Brown
                                   OUT 2                Digital output 2 (object detection)                        Orange
                                   OUT 3                Digital output 3 (object detection)                        White
                                   PNP: INGND           PNP: Common ground for all inputs NPN:                     White and black
                                   NPN: Vs              Common reference potential for all inputs

                                   –                    Shielding                                                  Metal




8024851/1ONO/2024-09-25 | SICK                                                                  O P E R A T I N G I N S T R U C T I O N S | TiM3xx   35
Subject to change without notice

6 ELECTRICAL INSTALLATION

6.4.2           TiMxxx-10xxxxx
                                         “Power/I/O” connection
                                              1 2 3 4   5
                                         6     7 8 9 10




                                         11 12 13 14 15

                                         Table 8: Connecting cable with male connector, D-Sub-HD, 15-pin
                                          Pin                Signal       Function                                 Wire colors of connecting
                                                                                                                   cable with flying leads 1)
                                          1                  VS           Supply voltage                           Red
                                          2                  N.c.         –                                        Violet
                                          3                  N.c.         –                                        Yellow
                                          4                  OUT 4        Digital output 4 (index/error)           Red and black
                                          5                  GND          Ground                                   Black
                                          6                  N.c.         –                                        Light blue
                                          7                  N.c.         –                                        Dark blue
                                          8                  IN 1         Digital input 1 (field set selection)    Turquoise or light gray
                                          9                  IN 2         Digital input 2 (field set selection)    Green
                                          10                 IN 3         Digital input 3 (field set selection)    Gray
                                          11                 IN 4         Digital input 4 (field set selection)    Pink
                                          12                 OUT 1        Digital output 1 (object detection)      Brown
                                          13                 OUT 2        Digital output 2 (object detection)      Orange
                                          14                 OUT 3        Digital output 3 (object detection)      White
                                          15                 PNP: INGND   PNP: Common ground for all inputs  White and black
                                                             NPN: Vs      NPN: Common reference potential of
                                                                          all inputs
                                          –                  –            Shielding                                Metal
                                         1)    Example values when using the connecting cable part number 2043413. Signal assignment and wire
                                               colors can vary when using other connecting cables.


6.4.3           TiMxxx-11xxxxx/TiMxxx-21xxxxx
                                         “Power/I/O” connection
                                         2                           1
                                         3                          10
                                         11                          9
                                         4                           8
                                         5                          12
                                         6                           7


                                         Table 9: Male connector, M12, 12-pin, A-coded
                                          Pin                Signal       Function                                 Wire colors of connecting
                                                                                                                   cable with flying leads 1)
                                          1                  GND          Ground                                   Blue
                                          2                  VS           Supply voltage                           Brown
                                          3                  IN 1         Digital input 1 (field set selection)    Red
                                          4                  IN 2         Digital input 2 (field set selection)    Green



36      O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                            8024851/1ONO/2024-09-25 | SICK
                                                                                                                          Subject to change without notice

ELECTRICAL INSTALLATION 6


                                    Pin         Signal              Function                                        Wire colors of connecting
                                                                                                                    cable with flying leads 1)
                                    5           OUT 1               Digital output 1 (object detection)             Pink
                                    6           OUT 2               Digital output 2 (object detection)             Yellow
                                    7           OUT 3               Digital output 3 (object detection)             Black
                                    8           OUT 4               Digital output 4 (index/error)                  Gray
                                    9           PNP: INGND          PNP: Common ground for all inputs  White
                                                NPN: Vs             NPN: Common reference potential of
                                                                    all inputs
                                    10          IN 3                Digital input 3 (field set selection)           Violet
                                    11          IN 4                Digital input 4 (field set selection)           Gray and pink
                                    12          –                   Reserved, do not wire this PIN!                 Rot and blue
                                    –           –                   Shielding                                       –
                                   1)    Example values when using the connecting cables part numbers 6054974 (5 m), 6054973 (10 m),
                                         6054972 (20 m). Signal assignment and wire colors can vary when using other connecting cables.

                                   "Ethernet" connection (only TiMxxx-21xxxxx)
                                   1                     2



                                   4                     3


                                   Table 10: Female connector, 4-pin, D-coded
                                    Contact            Labeling           Description
                                    1                  TX+                Sender+
                                    2                  RX+                Receiver+
                                    3                  TX-                Sender-
                                    4                  RX-                Receiver-


6.4.4              USB interface (TiM35x / 36x only)
                                   The Ethernet interface is recommended as a communication interface.
                                   If using the USB interface, please note:
                                    • Use a high-speed USB cable, maximum length of cable: 3 m.
                                    • The connection may be interrupted due to ESD/EMC influences. If necessary:
                                         Disconnect USB cable from the device, then reconnect it. Restart communication
                                         via SOPAS ET software (“Online” button).

6.5                Connecting the device electrically

                                   NOTICE
                                   Observe the wiring instructions, see "Wiring instructions", page 34.

                                   1.     Ensure the voltage supply is not connected.
                                   2.     Connect the device according to the connection diagram, see "Connection dia‐
                                          gram", page 35.




8024851/1ONO/2024-09-25 | SICK                                                                   O P E R A T I N G I N S T R U C T I O N S | TiM3xx   37
Subject to change without notice

6 ELECTRICAL INSTALLATION

6.6           Wiring digital inputs / digital outputs
                                       Digital inputs
                                       The 4 switching digital inputs activate one of the 16 field sets in a binary combination
                                       as an evaluation case.
                                       The digital inputs are decoupled from the supply voltage of the device. They have a
                                       common reference point (INGND), meaning they are not decoupled from one another.
                                       The structure and wiring principle of the digital inputs are shown below.
                                         VS ext 1                 VS 2
                                                                                                              Device 3
                                                                              A         VS
                                                                                                                   VS
                                                                              B         IN X 4 6.64 K

                                                                                             Vin 5
                                                                                                     3.32 K
                                                                              C         INGND
                                                                              D         GND
                                                                                                                   GND


                                       GND                      GND
                                       Figure 26: Wiring of digital input (PNP version)
                                       1           External supply voltage VS ext
                                       2           Supply voltage Vs for device
                                       3           Device
                                       4           Signal IN X
                                       5           Input voltage Vin


                                        Posi‐              Signal     TiM3xx-01xxxx      TiM3xx-10xxxx (15-pin D-        TiM3xx-11xxxx,
                                        tion                          (cable with flying Sub-HD male connector):         TiM3xx-21xxxx (12-pin
                                                                      leads): wire color PIN                             M12 male connector): PIN
                                        A                  VS         Red                1                               2
                                        D                  GND        Black              5                               1
                                        C                  INGND      White and black    15                              9
                                        B1                 IN 1       Turquoise or light 8                               3
                                                                      gray
                                        B2                 IN 2       Green              9                               4
                                        B3                 IN 3       Gray               10                              10
                                        B4                 IN 4       Pink               11                              11




38    O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                                      8024851/1ONO/2024-09-25 | SICK
                                                                                                                                  Subject to change without notice

ELECTRICAL INSTALLATION 6


                                    VS ext 1          VS 2
                                                                                                    Device 3
                                                                   A          VS
                                                                                                          VS
                                                                   B          IN           6.64 K


                                                                                   Vin 4
                                                                                           3.32 K
                                                                   C          IN X 5
                                                                   D          GND
                                                                                                           GND


                                   GND               GND
                                   Figure 27: Wiring of digital input (NPN version)
                                   1       External supply voltage VS ext
                                   2       Supply voltage Vs for device
                                   3       Device
                                   4       Input voltage Vin
                                   5       Signal IN X

                                   Posi‐       Signal      TiM3xx-01xxxx      TiM3xx-10xxxx (15-pin D-                    TiM3xx-11xxxx,
                                   tion                    (cable with flying Sub-HD male connector):                     TiM3xx-21xxxx (12-pin
                                                           leads): wire color PIN                                         M12 male connector): PIN
                                   A           VS          Red                  1                                         2
                                   B           VIN         White and black      15                                        9
                                   D           GND         Black                5                                         1
                                   C1          IN 1        Turquoise or light 8                                           3
                                                           gray
                                   C2          IN 2        Green                9                                         4
                                   C3          IN 3        Gray                 10                                        10
                                   C4          IN 4        Pink                 11                                        11

                                   Switching behav‐          Current to the input starts the assigned function in the device.
                                   ior                       Default: Active high level, debounce 10 ms
                                   Properties                Opto-decoupled
                                                             Switchable with an electronic switch (PNP output) or mechanical switch
                                   Electrical values         see "Mechanics/electronics", page 57

                                   Digital outputs
                                   The device has 4 switching digital outputs.
                                   In combination, the digital outputs OUT 1 to OUT 3 signal the breach of the individual
                                   fields of a field set.
                                   The digital output OUT 4 is used to issue an error and a regular index pulse.
                                   The structure and wiring principle of the digital outputs are shown below.




8024851/1ONO/2024-09-25 | SICK                                                                         O P E R A T I N G I N S T R U C T I O N S | TiM3xx   39
Subject to change without notice

6 ELECTRICAL INSTALLATION

                                                     Device 1




                                                                               OUT X 2        X                             4

                                                                                                           Vout 3
                                                                               GND            Y



                                       Figure 28: Wiring of digital output (PNP version)
                                       1           Device
                                       2           Signal OUT X
                                       3           Output voltage Vout
                                       4           If inductive load is present: Provide an arc-suppression switch at the digital output. Attach
                                                   a freewheeling diode directly to the load for this purpose.

                                        Posi‐              Signal     TiM3xx-01xxxx      TiM3xx-10xxxx (15-pin D-   TiM3xx-11xxxx,
                                        tion                          (cable with flying Sub-HD male connector):    TiM3xx-21xxxx (12-pin
                                                                      leads): wire color PIN                        M12 male connector): PIN
                                        X1                 OUT 1      Brown              12                         5
                                        X2                 OUT 2      Orange             13                         6
                                        X3                 OUT 3      White              14                         7
                                        X4                 OUT 4      Red and black      4                          8
                                        Y                  GND        Black              5                          1

                                                           Device 1                                      VS 2
                                                                                 VS           X
                                                                                                                        4

                                                                                                           Vout 3

                                                                                OUT X 5       Y


                                                                                GND           Z



                                       Figure 29: Wiring of digital output (NPN version)
                                       1           Device
                                       2           Supply voltage Vs of the device
                                       3           Output voltage Vout
                                       4           If inductive load is present: Provide an arc-suppression switch at the digital output. Attach
                                                   a freewheeling diode directly to the load for this purpose.
                                       5           Signal OUT X

                                        Posi‐              Signal     TiM3xx-01xxxx      TiM3xx-10xxxx (15-pin D-   TiM3xx-11xxxx,
                                        tion                          (cable with flying Sub-HD male connector):    TiM3xx-21xxxx (12-pin
                                                                      leads): wire color PIN                        M12 male connector): PIN
                                        X                  VS         Red                1                          2
                                        Y1                 OUT 1      Brown              12                         5



40    O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                                8024851/1ONO/2024-09-25 | SICK
                                                                                                                            Subject to change without notice

ELECTRICAL INSTALLATION 6


                                   Posi‐     Signal          TiM3xx-01xxxx      TiM3xx-10xxxx (15-pin D-             TiM3xx-11xxxx,
                                   tion                      (cable with flying Sub-HD male connector):              TiM3xx-21xxxx (12-pin
                                                             leads): wire color PIN                                  M12 male connector): PIN
                                   Y2        OUT 2           Orange             13                                   6
                                   Y3        OUT 3           White              14                                   7
                                   Y4        OUT 4           Red and black      4                                    8
                                   Z         GND             Black              5                                    1

                                   Switching behav‐          PNP switching against supply voltage UV
                                   ior                       OUT 1 ... OUT 3:
                                                             Resting level: High (no object detection), working level: Low (object detec‐
                                                             tion)
                                                             Response time: 134 ms ... 30 s (configurable via SOPAS ET ), holding
                                                             time: 0 ms ... 10 s (configurable via SOPAS ET)
                                                             OUT 4:
                                                             Resting level: High (device ready)
                                                             working level: Low (error), low pulse (15 Hz, index, corresponds to meas‐
                                                             urement at 90°)
                                   Properties                Short-circuit protected and temperature protected
                                                             Not electrically isolated from supply voltage Uv
                                   Electrical values         see "Mechanics/electronics", page 57

                                   Longer connecting cables at the digital outputs of the device should be avoided due to
                                   the resulting fall in voltage. This is calculated as follows:
                                   Δ U = (2 x length x current) : (conductance value x cross-section)
                                   Conductance value for copper: 56 m/Ω mm2.

                                   Assignment of infringed fields – digital outputs
                                   Output level: The level of the digital outputs OUT 1 ... OUT 3 is active low (in resting
                                   position: high, in working position: low (field infringed)).
                                   All fields of a field set are considered infringed upon switching on, booting, in the event
                                   of an error and when the device is switched off.

                                   Example 1: 3 fields, rectangular, nested inside each other
                                                                   3
                                                               2
                                                         1




                                   Infringed fields                                                                   Digital outputs
                                                                                                  OUT 1                  OUT 2                OUT 3
                                   Fields 1, 2, and 3 infringed                                   Active                 Active               Active
                                   Fields 2 and 3 infringed                                       Deactivated Active                          Active
                                   Field 3 infringed                                              Deactivated Deactivated Active
                                   No field infringed:                                            Deactivated Deactivated Deactivated

                                   Example 2: 3 fields, rectangular, overlapping
                                   The overlapping fields create areas that can be used as additional fields.




8024851/1ONO/2024-09-25 | SICK                                                                    O P E R A T I N G I N S T R U C T I O N S | TiM3xx   41
Subject to change without notice

6 ELECTRICAL INSTALLATION

                                                                   1
                                                           A
                                          2                                3
                                              B      C     D   E       F




                                        Infringed areas (fields)                          Digital outputs
                                                                               OUT 1       OUT 2             OUT 3
                                        A (field 1 infringed)                  Active      Deactivated Deactivated
                                        B (field 2 infringed)                  Deactivated Active            Deactivated
                                        C (fields 1 and 2 infringed)           Active      Active            Deactivated
                                        D (fields 1, 2, and 3 infringed)       Active      Active            Active
                                        E (fields 1 and 3 infringed)           Active      Deactivated Active
                                        F (field 3 infringed)                  Deactivated Deactivated Active
                                        - (no field infringed)                 Deactivated Deactivated Deactivated




42    O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                    8024851/1ONO/2024-09-25 | SICK
                                                                                                Subject to change without notice

OPERATION 7


7                  Operation
7.1                SOPAS ET
                                   The following activities are normally performed using the SOPAS ET configuration
                                   software:
                                   • Field evaluation application: adjusting the 3 fields of a field set.
                                   • Parameterization: tailoring other device parameters to the application.
                                   • Diagnosis: determining the cause of a fault.
                                   To parameterize the device, you will require a computer with SOPAS ET installed and a
                                   free Ethernet connection (recommended) or, alternatively, a free USB interface.

                                   NOTE
                                   The most up-to-date version of the SOPAS ET software can be downloaded from
                                   www.sick.com/SOPAS_ET. The respective system requirements for installing SOPAS
                                   ET are also specified there.

                                   1.     Connect the communication interface of the device to the computer.
                                   2.     Switch on and start the computer.
                                   3.     Supply the device with voltage.
                                   ✓      Following successful initialization, the green status LED lights up. The device is
                                          ready for use.

                                   NOTE
                                   To use SOPAS ET with the device, you need a device description file (SDD) for this
                                   device. You can install this in SOPAS ET using the device catalog. The device description
                                   file is saved on the device and can be installed there. Alternatively, installation is
                                   possible from the SICK website (Internet connection required). Use the wizard in SOPAS
                                   ET to do this.

                                   Following installation of the device description file, the device can be selected from the
                                   device catalog and added to a project.
                                   A connection to the device is established via the communication interface. The connec‐
                                   tion must be activated for data transmission (online).
                                   Certain functions (e.g., Edit parameters) require you to be logged in to the device:
                                        > Device > Login > Select user level and enter password:

                                   NOTE
                                   Software access to the device is protected by user levels and passwords. After success‐
                                   fully configuring the device, you should change the passwords so they can fulfill their
                                   protective function.

                                   User levels                                     Password
                                   Machine operator                                –
                                   Maintenance staff                               main
                                   Authorized client                               client
                                   Service                                         servicelevel




8024851/1ONO/2024-09-25 | SICK                                                            O P E R A T I N G I N S T R U C T I O N S | TiM3xx   43
Subject to change without notice

7 OPERATION

                                         Table 11: User level and authorization
                                          Machine operator           A Machine operator level user can view the basic device parameters.

                                                                     • No password required
                                                                     • Read only permissions
                                                                     • Not all parameters are visible
                                          Maintenance                Maintenance can view the application-related device parameters.

                                                                     • Read only permissions
                                                                     • Not all parameters are visible
                                                                     • Can change the password for this user level
                                          Authorized Client (Inte‐   Device parameters can be set as an Authorized Client.
                                          grator)
                                                                     • Access to most parameters
                                                                     • Can change the password for this user level and the password for
                                                                         the Maintenance user level.
                                                                     •   Can create a diagnostic report
                                          Service                    A Service level user can configure all device parameters.

                                                                     • Access to all parameters
                                                                     • Can change the password for this user level as well as the password
                                                                         for the user levels Maintenance and Authorized Client
                                                                     • Can create a diagnostic report
                                                                     • Can perform firmware updates

                                         NOTE
                                         Change the passwords during initial commissioning to protect your device.
                                         A higher user level can change the password of a lower user level.


                                         NOTE
                                         If the password for the Service user level has been lost: see "Resetting the password for
                                         the Service user level", page 53.

                                         Information about the device is displayed in the device window                (> Device > Open) and
                                         the device can also be configured here.

                                         NOTE
                                         Changes to parameters that are made in SOPAS ET are not saved automatically in
                                         the device. After you have completed the configuration, you must save it in the device
                                         permanently by pressing the            Save permanent button.


                                         NOTE
                                         To reset the device to the factory settings, use the Load defaults option in SOPAS ET.
                                         With the Load application defaults option, the network settings remain unchanged, all
                                         other settings are reset to the factory settings.


Tools
                                         Depending on the selected view, different tools are available to help you perform
                                         configurations or customize the display.
                                         The following are examples of some of the tools for customizing the display:
                                         •
                                                  Button       : Display fields in the polar coordinates system.




44      O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                             8024851/1ONO/2024-09-25 | SICK
                                                                                                                           Subject to change without notice

OPERATION 7


                                   •
                                         Button     : Change over the view of the device/fields. Device black: View from
                                         above, device blue: View from below.
                                   •
                                         Button       or     : Switch off display of the full measuring line or display measur‐
                                         ing line as dotted.

7.1.1              Parameter - network
                                   The network area has input screens for configuring the Ethernet connection, the digital
                                   inputs / digital outputs and the device.
                                   For Ethernet configuration, note that the IP-Address / subnet-mask must correspond
                                   with the address space of the subsequent application.
                                   Table 12: IP-Address factory setting
                                   Parameter                                      Value
                                   IP-Address                                     192.168.0.1
                                   Subnet mask                                    255.255.255.0

                                   NOTE
                                   If you change the parameters of the Ethernet interface via the Ethernet interface, you
                                   must first save the data permanently to non-volatile memory in the device and then
                                   restart the device. A Restart button is provided in SOPAS ET for this purpose.


7.1.2              Parameter - filters
                                   When selecting the filter, consider filter mutual interference, see "Filter", page 21.

7.2                Field evaluation
                                   If the field shape of field set 1 has been taught in without a computer using the teach-in
                                   pushbutton, SOPAS is generally used to continue the configuration.
                                   This includes the following:
                                   • Setting of field shapes/sizes and, if applicable, non-programmable field sets
                                         based on the default setting and the setting of response time of the fields
                                   • Setting of the blanking size and the holding time of the assigned digital outputs
                                         OUT 1 ... OUT 3

7.2.1              Teach-in / Field set selection
                                   For the field evaluation application, it is possible to configure the device as follows
                                   rather than configuring it via SOPAS:
                                    • Selection of one of 16 field sets, each with 3 fields of the same size nested into
                                        one another, by means of input wiring.
                                    • Teach-in of the surrounding contour to automatically generate the outer field with
                                        any shape, including more complex shapes, and to deduce the two inner fields.
                                   The field sets are organized into groups in segmented field shapes. The shape can be
                                   changed at will, the default is rectangular.
                                   In the factory setting, the 3 origin-oriented fields of a field set are nested inside
                                   one another. The size of field 2 corresponds to field 1 plus 25%. The size of field 3
                                   corresponds to field 1 plus 52%.




8024851/1ONO/2024-09-25 | SICK                                                            O P E R A T I N G I N S T R U C T I O N S | TiM3xx   45
Subject to change without notice

7 OPERATION

                                                                   90°
                                                                           Field 3
                                                                           Field 2
                                                                           Field 1

                                                 180°                     0°




                                                    Segmented,            Rectangle
                                                  free shape type

                                           Figure 30: Structure of the fields of a field set and possible field shapes
                                           1           Segmented, free field shape
                                           2           Nested together, rectangle


7.2.1.1           Teach-in
                                           Preparation
                                           •        Remove all objects that will not permanently be in the field of view in monitoring
                                                    mode later on.
                                           •        Distance yourself sufficiently from the device during the advance warning phase of
                                                    the teach-in so that you are not detected as part of the field contour.

                                           Teaching in the field contour
                                           The device uses field set 1 (segmented, initial shape: rectangle) to adjust the field
                                           shape and size to the surrounding contour that was detected. The digital inputs are not
                                           allowed to be supplied with current during this process.
                                           The device forms the outer field 3 from the surrounding contour with a negative offset
                                           of 100 mm, and derives from this the limits of the two inner fields: field 1 = field 3
                                           minus 33%, and field 2 = field 3 minus 17%.
                                           The device stores the shortest value measured during the teach-in phase as a field limit
                                           for each angle.
                                           A parameter upload is required in order to display the newly taught-in field contour in
                                           SOPAS.
                                           1.       Press and hold the Teach-in pushbutton for 3 s to start the teach-in process.
                                           2.       The field shape to be formed can be defined by pacing out the limits during the
                                                    teach-in phase. Do not wear black clothing during this process!
                                           The LEDs display the individual phases of the teach-in process:
                                                           LED (red)                  LED (green)        Phase
                                                               -                         Ö               Teach-in pre-warning:
                                                                                                         LED flashes slowly at first (0.5 Hz)

                                                                                                         LED flashes increasingly rapidly
                                                                                                         within 15 s
                                                               O                          O              Teach-in:
                                                                                                         Duration 60 seconds
                                                               -                         Ö               Teach-in completion:
                                                                                                         LED flashes increasingly rapidly
                                                                                                         within 15 s




46        O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                             8024851/1ONO/2024-09-25 | SICK
                                                                                                                             Subject to change without notice

OPERATION 7


                                              LED (red)                     LED (green)           Phase
                                                   -                            O                 Monitoring mode:
                                                                                                  Automated return after teach-in com‐
                                                                                                  plete
                                                                                                  All fields free
                                                   O                            O                 Monitoring mode:
                                                                                                  If an object detection has occurred

                                        O = illuminated; Ö = flashing

                                   The taught-in field contour is automatically and permanently saved as a new field set 1.

7.2.1.2            Field set selection via input wiring
                                   One of the predefined field sets can be activated by wiring the digital inputs.

                                   Field set factory settings – digital inputs
                                   Field               Digital inputs          Field shape
                                   set                                         Default size of field 1
                                               IN 1    IN 2    IN 3     IN 4
                                   1           0       0       0        0      Rectangle, segmented L: 1 m, W: 2 m
                                   2           1       0       0        0      Rectangle, segmented L: 1.25 m, W: 2 m
                                   3           0       1       0        0      Rectangle, segmented L: 1.5 m, W: 2 m
                                   4           1       1       0        0      Rectangle, segmented L: 1.75 m, W: 2 m
                                   5           0       0       1        0      Rectangle, segmented L: 1 m, W: 2 m
                                   6           1       0       1        0      Rectangle, segmented L: 1.25 m, W: 2 m
                                   7           0       1       1        0      Rectangle, segmented L: 1.5 m, W: 2 m
                                   8           1       1       1        0      Rectangle, segmented L: 1.75 m, W: 2 m
                                   9           0       0       0        1      Rectangle, segmented L: 1 m, W: 2 m
                                   10          1       0       0        1      Rectangle, segmented L: 1.25 m, W: 2 m
                                   11          0       1       0        1      Rectangle, segmented L: 1.5 m, W: 2 m
                                   12          1       1       0        1      Rectangle, segmented L: 1.75 m, W: 2 m
                                   13          0       0       1        1      Rectangle, segmented L: 1 m, W: 2 m
                                   14          1       0       1        1      Rectangle, segmented L: 1.25 m, W: 2 m
                                   15          0       1       1        1      Rectangle, segmented L: 1.5 m, W: 2 m
                                   16          1       1       1        1      Rectangle, segmented L: 1.75 m, W: 2 m
                                   Output form (rectangle), can be changed as desired, L = length, W = width

                                   Input level: Low (in resting position): ≤ 2 V, high (in working position): ≥ 8 V




8024851/1ONO/2024-09-25 | SICK                                                                 O P E R A T I N G I N S T R U C T I O N S | TiM3xx   47
Subject to change without notice

7 OPERATION

7.2.2           Monitor - field evaluation monitor




                                         Figure 31: Device window: Monitor - field evaluation monitor

                                         In the Field evaluation monitor window, SOPAS displays the field contour (scan line) cur‐
                                         rently seen by the device through ambient reflection in blue.
                                         If the 4 digital inputs are not energized, SOPAS displays the following for field set 1
                                         according to the default setting of the device:
                                          • 3 evaluation fields (segmented rectangles) or the field shape generated with the
                                               aid of teach-in with its dimensions
                                          • Status of the digital inputs/outputs
                                          • Position of the mouse pointer
                                         SOPAS displays the fields as green if no object detection is present.
                                         If objects of a certain size are located for a certain duration in the part of the visual
                                         range that is covered by fields, the device will recognize this as an object detection.
                                         SOPAS displays this separately in yellow for the individual fields.
                                         Click the “Reset” button to make SOPAS reset the digital output counters.

7.2.3           Parameter - evaluation cases
                                         Response time, blanking size and digital output holding time
                                         The blanking size is the smallest size from which an object can be detected in a field
                                         by the device and lead to an object detection. All objects that are smaller than the
                                         minimum size are blanked out.
                                         Like the response time and the holding time, the blanking size applies to all field sets
                                         and their fields.
                                         Objects that are smaller than the blanking size can cause shadows to be cast at close
                                         range. Objects that are larger than the blanking size may be located within this shadow.
                                         These may not be detected correctly.
                                          Parameter                                              Factory setting
                                          Blanking size                                          Cross-section 200 mm
                                          Response time of the fields                            335 ms (5 scans)
                                          Digital output holding time                            335 ms (5 scans)



48      O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                         8024851/1ONO/2024-09-25 | SICK
                                                                                                                       Subject to change without notice

OPERATION 7


                                   When selecting the response time, note that the device internal reaction time must also
                                   be added (max. 67 ms).
                                   To test the effects of the changed settings, change to the Field evaluation monitor view.
                                   If the changed fields have been transferred to the device as described, SOPAS will
                                   also display these in the monitor, displaying the infringed fields in yellow. If you wish to
                                   observe another field set, it must first be activated accordingly using the digital inputs.

7.2.4              Parameters - detection fields




                                   Figure 32: Device window: Parameters - detection fields

                                   The user can change parameters in the right part of the window. SOPAS immediately
                                   transfers these changes to the device (default setting).
                                   However, detection fields that have been changed in size and shape must always be
                                   manually transferred to the device using the button. All changed parameters are only
                                   temporarily stored in the device for the time being and are not stored on the computer.
                                   In order to optimize the dimensions of the detection fields:
                                   1.   Under Field selection, for example, select field set 1.
                                   2.   Select the field to be configured.
                                   3.   Make the required optimizations, see description in the following sections.

                                   Shifting field positions
                                   1.   Button .
                                   2.   Click on the green marking rectangle of the desired field position in the outer field.
                                   ✓    The color of the marker square changes to blue.
                                   3.   Re-click the rectangle and drag it to the desired position, then release the push‐
                                        button.
                                   ✓    SOPAS controls the available positioning area during shifting.

                                   Inserting additional field positions
                                   1.   Button .
                                   2.   Click on the desired position on the limits of the outer field.
                                   ✓    SOPAS inserts a new green marker square. This can also be shifted.




8024851/1ONO/2024-09-25 | SICK                                                               O P E R A T I N G I N S T R U C T I O N S | TiM3xx   49
Subject to change without notice

7 OPERATION

                                      Deleting field points
                                      1.       Button .
                                      2.       Click on the green marking rectangle of the field position to be deleted in the outer
                                               field.
                                      ✓        The color of the marking rectangle changes to red.
                                      3.       Re-click the marking rectangle.
                                      ✓        SOPAS removes the marker square and instead connects the two nearest marker
                                               squares with a new line.

                                      Rotating the field pair and device around the central axis
                                      ►        In order to align the position of the field pair in SOPAS to the conditions on site
                                               from the user´s perspective, enter and confirm the desired angle of rotation in the
                                               0.0° input. A negative “-” sign sets the turning direction to the right.

                                      Setting up the contour as reference field
                                      In each field set, any field can be selected as a contour as reference field.
                                      The contour as reference field is used to monitor contours. This can be used to check
                                      whether the background is still recognized correctly. If this is no longer the case,
                                      possible reasons are that the device is covered or rotated.
                                      The same evaluation strategy is used for all contour as reference fields (evaluation time
                                      and blanking size).
                                                                               Field end point   2
                                      Contour as reference field   1
                                                                                                       Scan line   3
                                                                               Field start point   4



                                      1           Contour as Reference field
                                      2           End point of contour
                                      3           Scanning line
                                      4           Start point of contour

                                      1.       Select the required field in the field set.
                                      2.       Select the contour as reference field check mark under Field selection.
                                      3.       Delete the two field positions closest to the device.
                                      4.       Mark the two remaining field positions and shift them outside of the required
                                               reference contour area.
                                      5.       The button can switch to the configuration for the contour as reference field
                                               start points.
                                               The field starting points must lie between the scan line and the device so that the
                                               scan line passes between the start and end points of the contour as reference
                                               field.
                                      6.       Depending on the required shape of the reference contour field, create additional
                                               field points between the device and the reference contour field. The distance
                                               between the start and end points of the contour as reference field should be
                                               approximately 20 cm.
                                      The button can be used to switch between the start and end points of the contour
                                      as reference field for editing purposes. The active points are highlighted in light green
                                      while the deactivated points are dark green.




50   O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                                8024851/1ONO/2024-09-25 | SICK
                                                                                                                           Subject to change without notice

OPERATION 7


7.3                ROS driver
                                   Suitable drivers for integrating the product into the ROS (Robot Operating System) are
                                   available for download on the product page.

                                   The product page can be accessed via the SICK Product ID: pid.sick.com/{P/N}/{S/N}
                                   {P/N} corresponds to the part number of the product, see type label.
                                   {S/N} corresponds to the serial number of the product, see type label (if indicated).




8024851/1ONO/2024-09-25 | SICK                                                          O P E R A T I N G I N S T R U C T I O N S | TiM3xx   51
Subject to change without notice

8 MAINTENANCE


8             Maintenance
8.1           Maintenance plan
                                       Depending on the assignment location, the following preventive maintenance tasks
                                       may be required for the device at regular intervals:
                                       Table 13: Maintenance plan
                                        Maintenance work                        Interval                                 To be carried out
                                                                                                                         by
                                        Check device and connecting cables      Depends on ambient conditions and        Specialist
                                        for damage at regular intervals.        climate.
                                        Clean housing and optics cover.         Depends on ambient conditions and        Specialist
                                                                                climate.
                                        Check the screw connections and         Depends on the place of use, ambi‐ Specialist
                                        plug connectors.                        ent conditions or operating require‐
                                                                                ments. Recommended: At least every
                                                                                6 months.
                                        Check the mounting accessories and Depends on the place of use, ambi‐ Specialist
                                        vibration dampers used.            ent conditions or operating require‐
                                                                           ments. Recommended: At least every
                                                                           6 months.
                                        Check that all unused connections       Depends on ambient conditions and        Specialist
                                        are sealed with protective caps.        climate. Recommended: At least
                                                                                every 6 months.


8.2           Cleaning

                                       NOTICE
                                       Equipment damage due to improper cleaning.
                                       Improper cleaning may result in equipment damage.
                                       ■        Only use recommended cleaning agents and tools.
                                       ■        Never use sharp objects for cleaning.

                                       ►        Clean the optics cover at regular intervals and in the event of contamination with a
                                                lint-free lens cloth and plastic cleaning agent. Rinse off coarse dirt first with water.
                                                The cleaning interval essentially depends on the ambient conditions.




52    O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                        8024851/1ONO/2024-09-25 | SICK
                                                                                                                    Subject to change without notice

TROUBLESHOOTING 9


9                  Troubleshooting
9.1                Detecting and displaying errors
                                   Error memory
                                   The device has an error memory where its internal error states are recorded. The
                                   content of the error memory is retained when the device is switched off and when the
                                   “Restore Factory Settings” function is used.
                                   The SOPAS ET software can be used to create a diagnostics report containing error
                                   information (Complete view, Configuration tab, Start Diagnosis button).

9.2                Resetting the password for the Service user level
                                   If you have forgotten the password of the Service user level, you can reset it with the
                                   assistance of SICK.

                                   NOTE
                                   The responsible SICK sales company or the responsible SICK service partner carefully
                                   checks each code request to reset the password. A risk of deception by third parties
                                   nevertheless exists. The operating entity should therefore take suitable security meas‐
                                   ures.
                                   The operating entity should also take suitable measures to limit, as best as possible,
                                   access to the product. This includes, in particular, physical access as well as access to
                                   the software interfaces of the product.

                                   Requesting an unlock code
                                   1.   Open SOPAS ET.
                                   2.   Open the device window.
                                   3.   Open the device name > Password > Reset Service password.
                                   ✓    The Reset password window appears.
                                   4.   Enter the relevant data.
                                             NOTE Do not press Generate if an unlock code has already been requested
                                        from SICK. Only press this button if a new device code is required when inquiring
                                        again.
                                   5.   Click Generate e-mail with data.
                                   ✓    Your SICK subsidiary will create the unlock code based on the information pro‐
                                        vided and send it to you.
                                        The code is only valid once for the reset process. You can close the window by
                                        clicking on the x without interrupting the reset process. If you select Cancel or
                                        enter an incorrect code several times, the current reset process is terminated. The
                                        requested code is no longer valid. The process must be restarted.
                                   6.   Wait for the unlock code: The dialog box can be closed and the device switched
                                        off.

                                   Entering the unlock code
                                   Prerequisite
                                   • SICK has sent an unlock code.
                                   1.   Open SOPAS ET.
                                   2.   Open the device window.
                                   3.   Open the device name > Password > Reset Service password.
                                   ✓    The Reset password window appears.
                                   4.   Click Next.
                                   5.   Enter the code sent by SICK.


8024851/1ONO/2024-09-25 | SICK                                                          O P E R A T I N G I N S T R U C T I O N S | TiM3xx   53
Subject to change without notice

9 TROUBLESHOOTING

                                       6.       Click Ok.
                                       ✓        Password has been reset to the default password servicelevel. Parameters are
                                                not changed.

                                       Assigning a new password for the Service user level
                                       1.       Open SOPAS ET.
                                       2.       Log on to the device with the Service user level and the default password
                                                servicelevel.
                                       3.       Open the device name > Password > Change password.
                                       4.       Assign the new password for the Service user level.

9.3           Repairs
                                       Repair work on the device may only be performed by qualified and authorized personnel
                                       from SICK AG. Interruptions or modifications to the device by the customer will invalid‐
                                       ate any warranty claims against SICK AG.

9.4           Returns
                                       ►        Only send in devices after consulting with SICK Service.
                                       ►        The device must be sent in the original packaging or an equivalent padded pack‐
                                                aging.

                                       NOTE
                                       To enable efficient processing and allow us to determine the cause quickly, please
                                       include the following when making a return:
                                       •        Details of the contact person
                                       •        Description of the application
                                       •        Description of the fault that occurred


9.5           Disposal
                                       If a device can no longer be used, dispose of it in an environmentally friendly manner
                                       in accordance with the applicable country-specific waste disposal regulations. Do not
                                       dispose of the product along with household waste.

                                       NOTICE
                                       Danger to the environment due to improper disposal of the device.
                                       Disposing of devices improperly may cause damage to the environment.
                                       Therefore, observe the following information:
                                       ■        Always observe the national regulations on environmental protection.
                                       ■        Separate the recyclable materials by type and place them in recycling containers.




54    O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                     8024851/1ONO/2024-09-25 | SICK
                                                                                                                 Subject to change without notice

TECHNICAL DATA 10


10                 Technical data

                                   NOTE
                                   The relevant online product page for your product, including technical data, dimensional
                                   drawing, and connection diagrams, can be downloaded, saved, and printed from the
                                   Internet.
                                   The product page can be accessed via the SICK Product ID: pid.sick.com/{P/N}/{S/N}
                                   {P/N} corresponds to the part number of the product, see type label.
                                   {S/N} corresponds to the serial number of the product, see type label (if indicated).
                                   Please note: This documentation may contain further technical data.


10.1               Features
                                    Variant                    TiM31x                 TiM32x                 TiM35x                         TiM36x
                                    Measurement                             HDDM+ (improved behavior for edge hits)
                                    principle
                                    Application                           Indoor                                            Outdoor
                                    Light source              Infrared (wavelength 850 nm, max. pulse power                         Infrared (wave‐
                                                              880 mW, max. pulse width 5 ns, pulse frequency                        length 850 nm,
                                                                                 550 kHz)                                           max. pulse power
                                                                                                                                    880 mW, max.
                                                                                                                                    pulse width 5 ns,
                                                                                                                                    pulse frequency
                                                                                                                                    1,500 kHz)
                                    Laser class                     1 (IEC 60825-1:2014, EN 60825-1:2014+A11:2021)
                                                           Complies with 21 CFR 1040.10 and 1040.11 except for conformance with
                                                          IEC 60825-1 Ed.3., as described in Laser Notice No. 56 dated 8 May 2019.
                                    Aperture angle                                             270°
                                    Scan field flat‐                    Typ. ± 3.0°                                      Typ. ± 1.5°
                                    ness 1)
                                    Scanning fre‐                                              15 Hz
                                    quency
                                    Angular resolu‐                                    1°                                                    0.33°
                                    tion
                                    Working range                     0.05 m ... 4 m                                  0.05 m ... 10 m
                                    Scanning range                           –                                          5 m (typical)
                                    for 5% remission
                                    Scanning range                     2 m (typical)                                   8 m (typical) 2)
                                    with 10% remis‐
                                    sion
                                    Spot size                                    Spot size on the optics cover: 7 mm
                                                                                   Divergence: 8.6 mrad (0.49°)
                                    Number of ech‐                                                1
                                    oes evaluated
                                   1)   Reference area for base of housing
                                   2)   at ambient temperature < -15 °C: typ. 7.5 m




8024851/1ONO/2024-09-25 | SICK                                                                   O P E R A T I N G I N S T R U C T I O N S | TiM3xx   55
Subject to change without notice

10 TECHNICAL DATA

                                        Working range diagram
                                        Scanning range in m (ft) 1                                                       Scanning range in m (feet) 1

                                                                                                                                                               180°
                                                                                180°
                                                 4                                                                             10
                                                                                                                          (32.81)         225°
                                         (13.12)         225°

                                                                                                                                 6
                                                 2                                                                        (19.69)
                                             (6.56)
                                                                                                        270°                                                                            270°
                                                                                                                                 2
                                                                                                                             (6.56)
                                                 0                                                            90°               0                                                              90°
                                                                                                                               –2
                                                                                                                          (–6.56)
                                               –2
                                         (–6.56)                                                                               –6
                                                                                                                         (–19.69)

                                               –4           ‒45°                                                                          ‒45°
                                        (–13.12)                                                                              –10
                                                                                                                         (–32.81)
                                                                                 0°
                                                                                                                                                                0°
                                                            –4        –2         0         2          4                                  –10       –6       –2 0      2        6       10
                                                         (–13.12)   (–6.56)              (6.56)     (13.12)                             (–32.81) (–19.69) (–6.56)   (6.56)   (19.69) (32.81)

                                                                                       Scanning range in m (ft) 1                                                     Scanning range in m (feet) 1

                                                      Scanning range max.: 4 m (13.12 feet) 2                                         Scanning range max.: 10 m (32.81 feet) 2
                                                      Scanning range typical (for objects with 10 % remission):                       Scanning range typical (for objects with 10 % remission):
                                                      2 m (6.56 feet) 3                                                               8 m (26.25 feet) 3


                                        Figure 33: TiMx1x / TiMx2x working range dia‐                                    Figure 34: TiMx5x / TiMx6x working range dia‐
                                        gram                                                                             gram
                                        1             Sensing range in meters (feet)                                     1            Sensing range in meters (feet)
                                        2             Maximum sensing range: 4 m                                         2            Maximum sensing range: 10 m
                                                      (13.12 feet)                                                                    (32.81 feet)
                                        3             Typical sensing range for objects with                             3            Typical sensing range for objects with
                                                      10% remission: 2 m (6.56 feet)                                                  10% remission: 8 m (26.25 feet)


10.2           Performance
                                         Variant                                  TiM31x                            TiM32x                     TiM35x                           TiM36x
                                         Response time                                                                 Typ. 1 scan: 67 ms
                                                                                                                     Max. 2 scans: 134 ms 1)
                                         Power-up delay                                                                        Typ. 20 s
                                         Detectable object                                                                   Almost any
                                         shape
                                         Measurement                              Statistical (1 σ): < 30 mm 2)                                Statistical (1 σ): < 20 mm 2)
                                         errors                                     Systematic: ± 40 mm 2)                                       Systematic: ± 60 mm 2)
                                                                                 Temperature drift: 0.5 mm/K                                  Temperature drift: 0.5 mm/K
                                         Integrated appli‐                    Field evaluation            Field evaluation with flexible fields
                                         cation
                                         Number of field                      16 triple fields (48 fields), of which                   16 triple fields, (48 fields, contour as
                                         sets                                 1 triple (3 fields) can be configured                     reference; 1 triple (3 fields) can be
                                                                                     directly at the scanner)                           configured directly at the scanner)
                                         Simultaneous                                             1 (3 fields)                                        1 (3 fields)
                                         evaluation cases                                                                                2 (2 fields for detection and 1 field
                                                                                                                                              for contour as reference)
                                         Filter                                                                            Edge filter
                                                                                                                          Particle filter
                                                                                                                          Average filter
                                        1)      Corresponds to max. 134 ms between +45° and +225° of the working range, max. 150 ms between
                                                -45° and +45° of the working range (see "Working range diagram", page 56).
                                        2)      Typical value at 90% remission up to maximum sensing range; real value depends on ambient conditions.




56     O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                                                                   8024851/1ONO/2024-09-25 | SICK
                                                                                                                                                                Subject to change without notice

TECHNICAL DATA 10


10.3               Interfaces
                                   Variant                  TiM31x              TiM32x                   TiM35x                         TiM36x
                                   Ethernet                               -                         TCP/IP (SOPAS parameterization)
                                   USB                                                Type: Micro-USB
                                                                                Function: AUX, configuration
                                   Digital inputs                                            4
                                                         PNP: Vin = max. 28 V, Iin = max. 5 mA), opto-decoupled, debouncing time
                                                                                       approx. 10 ms
                                                                      NPN: Common reference potential 9 ... 28 V
                                   Digital outputs                        3 (NPN, additional 1x "device ready")
                                                        Each Iout ≤ 100 mA, not electrically isolated from the supply voltage, short-
                                                                          circuit proof/temperature protected
                                   Delay time                            67 ms ... 30,000 ms (can be configured)
                                   Holding time                         67 ms ... 600,052 ms (can be configured)
                                   Optical indicators                            2 LEDs (0n, output state)
                                   Control elements                                Pushbutton (teach-in)


10.4               Mechanics/electronics
                                   Variant                  TiM31x              TiM32x                   TiM35x                         TiM36x
                                   Electrical connec‐    TiM3xx-01xxxxx: Connecting cable     1 x Ethernet connection, 4-pin M12
                                   tion                       with open end, 15-wire 1)                female connector
                                                         TiM3xx-10xxxxx: Connecting cable 1 x voltage supply connection, 12-pin
                                                        with male connector, D-Sub-HD, 15-           M12 male connector
                                                                        pin                  1 x micro USB female connector, type
                                                         TiM3xx-11xxxxx: Connecting cable                     B
                                                        with male connector, M12, 12-pin, A-
                                                                       coded
                                   Supply voltage                                  9 V DC ... 28 V DC
                                                                     SELV and PELV acc. to IEC 60364-4-41:2005-12
                                   Power consump‐            4 W (typical), with unloaded digital outputs, incl. start-up current
                                   tion                                  16 W, with 4 max. loaded digital outputs
                                   Input voltage                                 Low: Vin ≤ 2 V; Iin ≤ 0.3 mA
                                                                         High: 8 V ≤ Vin ≤ 32 V; 0.7 mA ≤ Iin ≤ 5 mA
                                   Output voltage                                   Low: 0 V ≤ Vout ≤ 2 V
                                                                         High: (VS – 2 V) ≤ Vout ≤ VS; Iout ≤ 100 mA
                                   Housing color               Light blue (RAL 5012)                             Gray (RAL 7032)
                                   Enclosure rating                  IP65                                        IP67
                                                         (IEC 60529:1989+AMD1:1999+                (IEC 60529:1989+AMD1:1999
                                                                  AMD2:2013)                     +AMD2:2013), only valid with closed
                                                                                                     “Aux interface” plastic cover
                                   Protection class                               III (IEC 61140:2016-1)
                                   Housing                                    Base part: Aluminum die cast
                                                                Optics cover: Polycarbonate with scratch-resistant coating
                                   Weight                150 g, without connecting cables          250 g, without connecting cables
                                   Dimensions (L x           60 mm x 60 mm x 79 mm                       60 mm x 60 mm x 86 mm
                                   W x H)




8024851/1ONO/2024-09-25 | SICK                                                               O P E R A T I N G I N S T R U C T I O N S | TiM3xx   57
Subject to change without notice

10 TECHNICAL DATA

                                         Variant                      TiM31x               TiM32x                TiM35x                   TiM36x
                                         MTTFD                   Mean time to dangerous failure: 100 years, at 25 °C ambient temperature
                                                                                        (EN ISO 13849-1:2015)
                                        1)    All products with the type code TiM3xx-01xxxxx are intended to be operated with flying leads. For
                                              production-related reasons, individual product variants with this type code are delivered with a 15-pin
                                              D-Sub HD male connector. For these products, the user is responsible for cutting off the male connector
                                              and creating the cable ends. Alternatively, the products may be operated with a male connector. In this
                                              case, the information for the product variants with the type code TiM3xx-10xxxxx applies for the PIN
                                              assignment.


10.5           Ambient data
                                         Variant                      TiM31x               TiM32x                TiM35x                   TiM36x
                                         Object remission                                   4% ... 1,000% (reflectors)
                                         Electromagnetic                                      Radiation emitted:
                                         compatibility                    Residential area (EN 61000-6-3:2007-01+AMD:A1:2011)
                                         (EMC)                                          Electromagnetic compatibility:
                                                                                Industrial environment (EN 61000-6-2:2005)
                                         Vibration resist‐                                     Sine resonance scan:
                                         ance                                                    10 Hz ...1,000 Hz
                                                                                              (IEC 60068-2-6:2007)
                                                                                                     Sine test:
                                                                                   10 Hz ... 500 Hz; 5 g; 10 frequency cycles
                                                                                              (IEC 60068-2-6:2007)
                                                                                                    Noise test:
                                                                                         10 … 250 Hz; 4.24 grms, 5 h
                                                                                             (IEC 60068-2-64:2008)
                                         Shock resistance                                  50 g; 11 ms; 6 shocks/axis
                                                                                          25 g; 6 ms; 2.000 shocks/axis
                                                                                         50 g; 3 ms; 10,000 shocks/axis
                                                                                             (IEC 60068-2-27:2008)
                                         Impact resist‐               IK05 (0.7 joule) and IK06 (1 joule) as per DIN EN 62262:2022-02
                                         ance
                                         Ambient temper‐             Operation: -10 °C ... +50 °C               Commissioning/switching on:
                                         ature                        Storage: -30 °C ... +70 °C                     –10 °C ... +50 °C
                                                                       (IEC 60068-2-14:2009)                    Operation: –25 °C ... +50 °C
                                                                                                                 Storage: –40 °C ... +75 °C
                                                                                                                  (IEC 60068-2-14:2009)
                                         Ambient humid‐                                Operation: ≤ 80%, non-condensing
                                         ity                                            Storage: ≤ 95%, non-condensing
                                                                                            (EN 60068-2-30:2005)
                                         Altitude                                           < 5,000 m above sea level
                                         Ambient light                                    80,000 lx (indirect exposure)
                                         immunity
                                         Ambient condi‐                            Contamination level 3 outside the housing
                                         tions                                             (EN 61010-1:2011-07)
                                         Damp heat                                    +25 °C ... +55 °C, 95% r.h., 6 cycles
                                                                                           (EN 60068-2-30:2005)
                                         Temperature                 -10 °C … +50 °C, 10 cycles                  -25 °C … +50 °C, 10 cycles
                                         change                        (EN 60068-2-14: 2009)                       (EN 60068-2-14: 2009)




58     O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                                 8024851/1ONO/2024-09-25 | SICK
                                                                                                                              Subject to change without notice

ACCESSORIES 11


11                 Accessories

                                   NOTE
                                   On the product page you will find accessories and, if applicable, related installation
                                   information for your product.
                                   The product page can be accessed via the SICK Product ID: pid.sick.com/{P/N}/{S/N}
                                   {P/N} corresponds to the part number of the product, see type label.
                                   {S/N} corresponds to the serial number of the product, see type label (if indicated).




8024851/1ONO/2024-09-25 | SICK                                                          O P E R A T I N G I N S T R U C T I O N S | TiM3xx   59
Subject to change without notice

12 ANNEX


12             Annex
12.1           Declarations of conformity and certificates
                                        You can download declarations of conformity and certificates via the product page.
                                        The product page can be accessed via the SICK Product ID: pid.sick.com/{P/N}/{S/N}
                                        {P/N} corresponds to the part number of the product, see type label.
                                        {S/N} corresponds to the serial number of the product, see type label (if indicated).

12.2           Licenses
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




60     O P E R A T I N G I N S T R U C T I O N S | TiM3xx                                                    8024851/1ONO/2024-09-25 | SICK
                                                                                                                 Subject to change without notice

ANNEX 12




8024851/1ONO/2024-09-25 | SICK     O P E R A T I N G I N S T R U C T I O N S | TiM3xx   61
Subject to change without notice

8024851/1ONO/2024-09-25/en
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