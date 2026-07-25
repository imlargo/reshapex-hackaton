OPERATING INSTRUCTIONS


InspectorP64x/65x
2D machine vision

Described product
                                   InspectorP64x Flex
                                   InspectorP65x Flex
                                   InspectorP65x DynamicFocus

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




2   O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                      8019943/1PGH/2024-11 | SICK
                                                                                                        Subject to change without notice

CONTENTS


Contents
                                   1   About this document........................................................................                              5
                                       1.1     Information on the operating instructions..............................................                           5
                                       1.2     Scope.........................................................................................................    5
                                       1.3     Explanation of symbols............................................................................                5
                                       1.4     Further information...................................................................................            6
                                       1.5     SICK service..............................................................................................        6

                                   2   Safety information............................................................................                           7
                                       2.1     Intended use.............................................................................................         7
                                       2.2     Improper use.............................................................................................         8
                                       2.3     Limitation of liability.................................................................................          8
                                       2.4     Modifications and conversions................................................................                     8
                                       2.5     Cybersecurity............................................................................................         9
                                       2.6     Requirements for skilled persons and operating personnel..................                                       10
                                       2.7     Operational safety and specific hazards.................................................                         11
                                       2.8     Repairs......................................................................................................    13

                                   3   Product description........................................................................... 14
                                       3.1     Scope of delivery.......................................................................................         14
                                       3.2     Product ID..................................................................................................     15
                                       3.3     Product characteristics............................................................................              17
                                       3.4     SICK AppSpace.........................................................................................           20

                                   4   Transport and storage....................................................................... 21
                                       4.1     Transport...................................................................................................     21
                                       4.2     Transport inspection.................................................................................            21
                                       4.3     Storage......................................................................................................    21

                                   5   Mounting............................................................................................. 22
                                       5.1     Overview of mounting procedure.............................................................                      22
                                       5.2     Optic kit scope of delivery........................................................................              22
                                       5.3     Preparation for mounting.........................................................................                22
                                       5.4     Mount the optics.......................................................................................          23
                                       5.5     Mounting location.....................................................................................           25
                                       5.6     Mounting the device.................................................................................             30

                                   6   Electrical installation........................................................................ 32
                                       6.1     Wiring instructions....................................................................................          32
                                       6.2     Prerequisites for safe operation of the device........................................                           33
                                       6.3     Connections and pin assignment............................................................                       34
                                       6.4     Connection diagrams...............................................................................               37
                                       6.5     Connecting the device..............................................................................              37

                                   7   Commissioning.................................................................................. 42
                                       7.1     Installing SensorApps and programming the device..............................                                   42

8019943/1PGH/2024-11 | SICK                                                                    O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x     3
Subject to change without notice

CONTENTS


                                    8           Maintenance...................................................................................... 44
                                                8.1         Maintenance plan.....................................................................................            44
                                                8.2         Cleaning.....................................................................................................    44
                                                8.3         Repairs......................................................................................................    45

                                    9           Troubleshooting................................................................................. 46
                                                9.1         Overview of possible errors and faults....................................................                       46
                                                9.2         Detailed fault analysis..............................................................................            46
                                                9.3         SICK service..............................................................................................       46
                                                9.4         Returns......................................................................................................    46

                                    10          Decommissioning............................................................................. 47
                                                10.1 Disposal.....................................................................................................           47

                                    11          Technical data.................................................................................... 48
                                                11.1        Optics and Illumination............................................................................              48
                                                11.2        Performance.............................................................................................         49
                                                11.3        Interfaces..................................................................................................     50
                                                11.4        Mechanics and electronics......................................................................                  50
                                                11.5        Ambient data.............................................................................................        51

                                    12          Accessories........................................................................................ 52

                                    13          Annex.................................................................................................. 53
                                                13.1        Declarations of conformity and certificates............................................                          53
                                                13.2        Licenses....................................................................................................     53
                                                13.3        Connection diagrams of connection module CDB650-204..................                                            53
                                                13.4        Connection diagrams of connection module CDM420-0006...............                                              63




4    O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                                                               8019943/1PGH/2024-11 | SICK
                                                                                                                                                  Subject to change without notice

ABOUT THIS DOCUMENT 1


1                    About this document
1.1                  Information on the operating instructions
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

1.2                  Scope
                                   The operating instructions are valid for all available product types. To obtain more
                                   detailed information on identifying your product type, see "Type code", page 15.

                                   Available product types are listed on the online product page:
                                   •    www.sick.com/InspectorP64x
                                   •    www.sick.com/InspectorP65x

                                   A number of product types are used as examples for commissioning and based on the
                                   default parameter settings for the relevant device.

1.3                  Explanation of symbols
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




8019943/1PGH/2024-11 | SICK                                                     O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   5
Subject to change without notice

1 ABOUT THIS DOCUMENT


                                     CAUTION
                                     … indicates a potentially dangerous situation, which may lead to minor/slight injuries if
                                     not prevented.


                                     NOTICE
                                     … indicates a potentially harmful situation, which may lead to material damage if not
                                     prevented.


                                     NOTE
                                     … highlights useful tips and recommendations as well as information for efficient and
                                     trouble-free operation.


1.4           Further information
                                     More information can be found on the product page.
                                     The call is made via the SICK Product ID: pid.sick.com/{P/N}/{S/N}
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

1.5           SICK service
                                     If you require any technical information, our SICK Service will be happy to help. To find
                                     your agency, see the final page of this document.

                                     NOTE
                                     Before calling, make a note of all type label data such as type code, serial number, etc.,
                                     to ensure faster processing.




6     O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                       8019943/1PGH/2024-11 | SICK
                                                                                                           Subject to change without notice

SAFETY INFORMATION 2


2                    Safety information
2.1                  Intended use
                                   The InspectorP6xx is a programmable vision sensor for industrial use for tasks which
                                   require high-resolution images at long distances.
                                   The device is programmed on a PC by using the development environment software
                                   SICK AppSpace. Depending on the application, a browser-based, graphical user inter‐
                                   face (GUI) can be created, which provides opportunities defined by the application
                                   developer to influence an application at operator level. The device offers various inter‐
                                   faces for controlling, programming, and operating purposes, which can be activated
                                   as necessary via development environments, control systems (programmable logic
                                   controllers), or applications. However, configuration, programming, and control requires
                                   various technical skills, depending on how the device is connected and used.
                                   The devices are primarily designed for use in industrial and logistics areas, and they
                                   meet the requirements for industrial ruggedness, interfaces and data processing. They
                                   are not safety components as per the Machinery Directive 2006/42/EC. They are
                                   not intended and not permitted to be used in areas with explosive atmospheres, in
                                   corrosive environments, or in extreme ambient conditions.

2.1.1                Operating restrictions

                                   NOTE
                                   Radio interference may occur when the device is used in residential areas!
                                   ■    Only use the device in industrial environments (EN 61000-6-4).


2.1.2                Conditions for specified enclosure rating
                                   To ensure compliance with the specified enclosure rating of the device during opera‐
                                   tion, the following requirements must be met: If these requirements are not met, the
                                   device does not fulfill any specified enclosure rating.
                                   •    The cables plugged into the electrical connections must be screwed tight.
                                   •    Any electrical connections that are not being used must be sealed with a tightly-
                                        fastened protective cap (as in the delivery condition).
                                   •    The foldable cover must be flush with the device and screwed tight.
                                   •    The optics protection hood must be screwed tightly onto the device.

2.1.3                Cover on the device

                                   NOTICE
                                   Risk of product damage if cover is open!
                                   In open state, the device does not conform to a specified enclosure rating.
                                   If necessary, only operate the device for a short time with an open cover for the
                                   activities listed in the following: During this time, protect the device against moisture
                                   and dust.

                                   Briefly open the cover for the following activities:
                                   • Inserting or removing the optional memory card
                                   For further warranty provisions, see the General Terms and Conditions of SICK AG, e.g.,
                                   on the delivery note of the device.




8019943/1PGH/2024-11 | SICK                                                      O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   7
Subject to change without notice

2 SAFETY INFORMATION

2.2             Improper use
                                       Any use outside of the stated areas, in particular use outside of the technical specifica‐
                                       tions and the requirements for intended use, will be deemed to be incorrect use.
                                        •       The device does not constitute a safety component in accordance with the respec‐
                                                tive applicable safety standards for machines.
                                        •       The device must not be used in explosion-hazardous areas, in corrosive environ‐
                                                ments or under extreme environmental conditions.
                                        •       Any use of accessories not specifically approved by SICK AG is at your own risk.

                                       WARNING
                                       Danger due to improper use!
                                       Any improper use can result in dangerous situations.
                                       Therefore, observe the following information:
                                        ■       Product should be used only in accordance with its intended use.
                                        ■       All information in the documentation must be strictly observed.
                                        ■       Shut down the product immediately in case of damage.


2.3             Limitation of liability
                                       Relevant standards and regulations, the latest technological developments, and our
                                       many years of knowledge and experience have all been taken into account when
                                       compiling the data and information contained in these operating instructions. The
                                       manufacturer accepts no liability for damage caused by:

                                        ■       Non-adherence to the product documentation (e.g., operating instructions)
                                        ■       Incorrect use
                                        ■       Use of untrained staff
                                        ■       Unauthorized conversions or repair
                                        ■       Technical modifications
                                        ■       Use of unauthorized spare parts, consumables, and accessories

2.3.1           Programmable device
                                       The InspectorP6xx is a programmable device.
                                       Therefore the respective programmer is responsible for his/her programming perform‐
                                       ance and the resulting working principle of the device.
                                       The liability and warranty of SICK AG is limited to the device specification (hardware
                                       functionality and any programming interfaces) according to the agreed conditions.
                                       Therefore, SICK AG is not liable, among other things, for damages that are caused by
                                       programming of the customer or third parties.

2.4             Modifications and conversions

                                       NOTICE
                                       Modifications and conversions to the device may result in unforeseeable dangers.

                                       Interrupting or modifying the device or SICK software will invalidate any warranty claims
                                       against SICK AG. This applies in particular to opening the housing, even as part of
                                       mounting and electrical installation.




8       O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                        8019943/1PGH/2024-11 | SICK
                                                                                                              Subject to change without notice

SAFETY INFORMATION 2


2.5                  Cybersecurity
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
                                   Device capabilities and recommended use
                                   As the device typically uses network communication extensively, please note the follow‐
                                   ing when designing a cybersecurity concept for the system this device shall be part of:
                                   •    When correctly configured, the Nova 2D SensorApp offers basic authentication for
                                        the GUI to prevent unintentional or accidental misuse. However, the underlying
                                        browser-to-device communication is not authenticated.
                                   •    All communication (images, configuration, logs) between the device and network
                                        devices (e.g. a computer used for configuration), should be assumed to be unen‐
                                        crypted unless otherwise specified.
                                   •    It is recommended to always use the latest software to ensure that the latest
                                        security patches are applied.
                                   •    It is recommended to only connect the device to private isolated networks. At
                                        all points where there is a physical connection to external, possibly untrusted
                                        networks, it is strongly recommended to block all network traffic to and from the
                                        device using a firewall.
                                   •    A user who develops custom software running on the device (i.e. development in
                                        SICK AppSpace) is responsible for the security of the developed solution.

                                   Network services
                                   The device uses several network services for its operation. For information about
                                   the factory default settings when using the device with the Nova 2D SensorApp, see
                                   table 1, page 9.
                                   Table 1: Default device settings for the EtherNet connection
                                   Service       Logical    Encrypted Authenti‐    Default           Description
                                                 port                 cated        status
                                   SOPAS         TCP port No            Yes        Listening         Used for configuration of
                                   REST API      80                                                  the device
                                   web server
                                   CROWN         TCP port No            No         Listening         Used for configuration of
                                   REST API      80                                                  the device
                                   server
                                   CROWN      TCP port No               No         Listening         Used for configuration of
                                   Web socket 80                                                     the device and image
                                   server                                                            transfer to GUI
                                   Web server    TCP port No            No         Listening         Used for configuration of
                                                 80                                                  the device
                                   CoLa-2        TCP port No            Yes        Listening         Used for configuration of
                                   server        2122                                                the device




8019943/1PGH/2024-11 | SICK                                                        O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   9
Subject to change without notice

2 SAFETY INFORMATION

                                      Service               Logical   Encrypted Authenti‐     Default     Description
                                                            port                cated         status
                                      ColaScan              UDP port No           No          Listening   Used for device detection
                                                            30718                                         and automatic IP configu‐
                                                                                                          ration
                                      ColaA/B               TCP Port No           Yes         Listening
                                                            2111
                                      FTP client            TCP con‐ No           No          Not used    Used for image recording
                                                            figurable                                     with the Nova 2D Sensor‐
                                                            port,                                         App
                                                            default
                                                            21
                                      DHCP client TCP port No                     No          Not used    Used when DHCP is ena‐
                                                  68                                                      bled on device
                                      SSH server            TCP port Yes          Yes         Not used    Used for device repair
                                                            22
                                      TCP client            TCP con‐ N/A          N/A         Not used    Used by the Nova 2D
                                                            figurable                                     SensorApp, tool TCP Cli‐
                                                            port                                          ent
                                      TCP server            TCP con‐ N/A          N/A         Not used    Used by the Nova 2D
                                                            figurable                                     SensorApp, tool TCP Cli‐
                                                            port                                          ent
                                      EtherNet/IP TCP port No                     No          Not used    Used by the Nova 2D
                                                  44818                                                   SensorApp if Fieldbus
                                                  UDP                                                     with Ethernet/IP commu‐
                                                  ports                                                   nication is set up
                                                  161,
                                                  2222,
                                                  44818,
                                                  68
                                      PROFINET              UDP       No          No          Not used    Used by the Nova 2D
                                                            ports                                         SensorApp if Fieldbus
                                                            161,                                          with Ethernet/IP commu‐
                                                            34964,                                        nication is set up
                                                            49153

                                     In addition, custom SICK AppSpace Software can be used to enable additional network
                                     services. This is described in the LUA API.

2.6           Requirements for skilled persons and operating personnel

                                     WARNING
                                     Risk of injury due to insufficient training.
                                     Improper handling of the device may result in considerable personal injury and material
                                     damage.
                                      ■       All work must only ever be carried out by the stipulated persons.

                                     The following qualifications are required for various activities:
                                     Table 2: Activities and technical requirements
                                      Activities                           Qualification
                                      Mounting, maintenance                ■   Basic practical technical training
                                                                           ■   Knowledge of the current safety regulations in the workplace




10    O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                                     8019943/1PGH/2024-11 | SICK
                                                                                                                         Subject to change without notice

SAFETY INFORMATION 2


                                   Activities                    Qualification
                                   Electrical installation,      ■   Practical electrical training
                                   device replacement            ■   Knowledge of current electrical safety regulations
                                                                 ■   Knowledge of the operation and control of the devices in their
                                                                     particular application
                                   Commissioning, configura‐     ■   Basic knowledge of the computer operating system used
                                   tion                          ■   Basic knowledge of the design and setup of the described
                                                                     connections and interfaces
                                                                 ■   Basic knowledge of data transmission
                                                                 ■   Knowledge of the programming of image-processing systems
                                                                     and network components
                                   Operation of the device for   ■   Knowledge of the operation and control of the devices in their
                                   the particular application        particular application
                                                                 ■   Knowledge of the software and hardware environment for the
                                                                     particular application


2.7                  Operational safety and specific hazards
                                   Please observe the safety notes and the warnings listed here and in other sections
                                   of this product documentation to reduce the possibility of risks to health and avoid
                                   dangerous situations.

                                   LED radiation of the integrated illumination unit

                                   NOTICE
                                   Only the VI83I illumination units from SICK intended for integration in this application
                                   can be used as an integrated illumination unit.

                                   Risk group 1
                                   • Color of the illumination: visible blue light (aperture angle: wide, medium), visible
                                        red light or visible white light
                                   • Color of the feedback LED: visible green light
                                   CAUTION
                                   Optical radiation: LED risk group 1, visible radiation, 400 nm to 780 nm
                                   The LEDs may pose a danger to the eyes in the event of incorrect use.
                                   ■    Do not look into the light source intentionally.
                                   ■    Do not open the housing. Opening the housing will not switch off the light source.
                                        Opening the housing may increase the level of risk.
                                   ■    Comply with the current national regulations on photobiological security of lamps
                                        and lamp systems.

                                   Risk group 2
                                   • Color of the illumination: visible blue light (aperture angle: narrow)




8019943/1PGH/2024-11 | SICK                                                         O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   11
Subject to change without notice

2 SAFETY INFORMATION


                                    CAUTION
                                    Warning! Optical radiation: LED risk group 2, visible radiation, 400 nm to 780 nm
                                    Potentially dangerous optical radiation. Can be damaging to the eyes.
                                     ■       Do not look into the light source for extended periods of time.
                                     ■       Never point the light source at people.
                                     ■       Avoid any reflections on people from reflective surfaces. Be particularly careful
                                             during mounting and alignment work.
                                     ■       Do not open the housing. Opening the housing will not switch off the light source.
                                             Opening the housing may increase the level of risk.
                                     ■       Comply with the current national regulations on photobiological security of lamps
                                             and lamp systems.

                                    If the product is operated in conjunction with external illumination systems, the risks
                                    described here may be exceeded. This must be taken into consideration by users on a
                                    case-by-case basis.

                                    CAUTION
                                    Optical radiation: Class 1 Laser Product
                                    The accessible radiation does not pose a danger when viewed directly for up to 100
                                    seconds. It may pose a danger to the eyes and skin in the event of incorrect use.
                                     ■       Do not open the housing. Opening the housing may increase the level of risk.
                                     ■       Current national regulations regarding laser protection must be observed.

                                    Caution – Use of controls or adjustments or performance of procedures other than
                                    those specified herein may result in hazardous radiation exposure.
                                    For both radiation types:
                                    It is not possible to entirely rule out temporary disorienting optical effects, particularly
                                    in conditions of dim lighting. Disorienting optical effects may come in the form of
                                    dazzle, flash blindness, afterimages, photosensitive epilepsy, or impairment of color
                                    vision, for example.

                                    WARNING
                                    Electrical voltage!
                                    Electrical voltage can cause severe injury or death.
                                     ■       Work on electrical systems must only be performed by qualified electricians.
                                     ■       The power supply must be disconnected when attaching and detaching electrical
                                             connections.
                                     ■       The product must only be connected to a voltage supply as set out in the require‐
                                             ments in the operating instructions.
                                     ■       National and regional regulations must be complied with.
                                     ■       Safety requirements relating to work on electrical systems must be complied with.




12   O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                             8019943/1PGH/2024-11 | SICK
                                                                                                                Subject to change without notice

SAFETY INFORMATION 2


                                   WARNING
                                   Risk of injury and damage caused by potential equalization currents!
                                   Improper grounding can lead to dangerous equipotential bonding currents, which may
                                   in turn lead to dangerous voltages on metallic surfaces, such as the housing. Electrical
                                   voltage can cause severe injury or death.
                                   ■    Work on electrical systems must only be performed by qualified electricians.
                                   ■    Follow the notes in the operating instructions.
                                   ■    Install the grounding for the product and the system in accordance with national
                                        and regional regulations.


2.8                  Repairs
                                   Repair work on the device may only be performed by qualified and authorized personnel
                                   from SICK AG. Interruptions or modifications to the device by the customer will invalid‐
                                   ate any warranty claims against SICK AG.




8019943/1PGH/2024-11 | SICK                                                    O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   13
Subject to change without notice

3 PRODUCT DESCRIPTION


3             Product description
3.1           Scope of delivery
                                     Depending on the chosen device version, the scope of delivery of a device will include
                                     the following components:
                                     Table 3: Scope of delivery
                                      No. of          Component                            Remarks
                                      units
                                      1               Type of device ordered (com‐         Complete device:
                                                      plete device or basic device)        • Components are assembled at the factory (cam‐
                                                                                             era housing and optics accessories).
                                                                                           • Optics protection hood is provided with a device
                                                                                             seal.
                                                                                           Basic device:
                                                                                           • Mount camera housing with C-mount threaded
                                                                                              connection and individual components on your
                                                                                              own.
                                                                                           • Order individual components separately as
                                                                                              accessories .
                                                                                           •  Light inlet is sealed with a protective cap.
                                                                                           All devices:
                                                                                           • Electrical connections are sealed with protective
                                                                                               caps.
                                                                                           • Without holders and connecting cables
                                      2               Sliding nut, 5.5 mm deep, with       • Alternative mounting option for the device
                                                      M5 threaded fixing hole                  instead of the threaded mounting hole
                                                                                           •   Use in pairs.
                                      1               Hexagon key WAF 2                    • Basic device: mount integratable VI83I illumina‐
                                                                                               tion.
                                                                                           • Open and close foldable cover (access to the
                                                                                               microSD card slot).
                                      1 or 2          LED warning label RG 2 (self-        • Complete device: 1 LED warning label (French)
                                                      adhesive)                                for integrated ring illumination RG 2 in the scope
                                                                                               of delivery of the device.
                                                                                           •   Basic device: 2 LED warning labels in English
                                                                                               and French included in the scope of delivery
                                                                                               of the separately-ordered integratable ring illu‐
                                                                                               mination unit RG 2.
                                      1               Laser warning label (self-adhe‐      Basic device: laser warning label (French) for the
                                                      sive)                                laser output aperture in the camera housing
                                      1               SICK lens cloth                      Basic device: clean optical surfaces (e.g. front
                                                                                           screen in the optics protection hood).
                                      1               Printed safety notes, multilin‐      Brief information and general safety notes
                                                      gual
                                                      Quality Inspection SensorApp         Pre-installed on the device
                                     1)    Depending on order, e.g. optional optics kit (lens, integratable VI88I illumination unit, spacers, optics
                                           protection hood).

                                     Associated components not contained in the delivery:
                                     Table 4: Other components
                                      Component                                            Remarks
                                      SOPAS ET configuration software                      Available online at:

                                                                                           • www.sick.com/SOPAS_ET

14    O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                                           8019943/1PGH/2024-11 | SICK
                                                                                                                               Subject to change without notice

PRODUCT DESCRIPTION 3


                                   Component                                        Remarks
                                   SICK AppStudio software                          Available online at:

                                                                                    • www.sick.com/SICK_AppStudio
                                   SICK AppManager software                         Available online at:

                                                                                    • www.sick.com/SICK_AppManager
                                   This documentation, available in English,        Available online at:
                                   German and French, and in other lan‐
                                   guages if necessary                              • www.sick.com/InspectorP64x
                                                                                    • www.sick.com/InspectorP65x
                                   An overview of available complete devices and a selection guide for the matching
                                   device components for the basic devices is provided on the online product page.

                                   Accessories
                                   Accessories are only supplied if you order them separately, see "Accessories",
                                   page 52.

3.2                  Product ID

3.2.1                Type label
                                   The type label gives information for identification of the device.
                                   The UL certification is dependent on the type. Any existing UL certification can be found
                                   on the type label. The corresponding UL logo is then printed on the label.
                                                                                                         1
                                                  V2D654P-2MEWHA6                                        2
                                                    P/N: 1082301   Exchange
                                    Made in Germany S/N: 2203 0001                                       3
                                                    DC 24V ±20%    20W Imax=2.0A                         4



                                                                           I.T.E.                        5
                                                                          E244281
                                                 MAC P1 00:06:77:05:2E:11
                                                 MAC P3 00:06:77:05:2E:11
                                                  Manufactured: January 2022                             6
                                                                                                         7
                                   Figure 1: InspectorP64x/InspectorP65x type label (example)
                                   1      Type designation according to type code
                                   2      Part number
                                   3      Serial number
                                   4      Supply voltage, power consumption and maximum current consumption
                                   5      Certificates and symbols
                                   6      MAC address (placeholder)
                                   7      Production date


3.2.2                Type code
                                   V      2      D      6     x       x        P      -        x        M         x         x          x          x       x
                                   1      2      3      4     5       6        7               8        9         10        11         12         13      14




8019943/1PGH/2024-11 | SICK                                                               O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x        15
Subject to change without notice

3 PRODUCT DESCRIPTION

                                     Position                        Description
                                     1 ... 5                         Product family
                                                                     V2D6xx InspectorP6xx
                                     6                               Image sensor resolution
                                                                     2: For InspectorP642: 1.7 megapixels (1600 px x 1088 px)
                                                                     2: For InspectorP652: 2.1 megapixels (2048 px x 1088 px)
                                                                     4: 4.2 megapixels (2048 px x 2048 px)
                                     7                               Function
                                                                     P: Programmable
                                     8                               Generation
                                     9                               Image sensor type
                                                                     M: Monochrome
                                     10                              Lens unit type
                                                                     E: Electrical focus (dynamic, auto, teach-auto)
                                                                     C: C-mount thread
                                     11                              Illumination
                                                                     R: Red/Amber
                                                                     W: White
                                                                     B: Blue
                                                                     X: No illumination unit installed
                                     12                              Focal distance (lens unit)
                                                                     H: 54 mm
                                                                     K: 40 mm
                                                                     X: No lens installed
                                     13                              Connection variants1)
                                                                     A: Connection variant 1
                                                                     F: Connection variant 2
                                                                     H: Connection variant 3
                                     14                              IP protection class and front screen
                                                                     5: IP 65: Plastic front screen
                                                                     6: IP 65: Glass front screen
                                    1)    see "Connections and pin assignment", page 34




16   O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                                      8019943/1PGH/2024-11 | SICK
                                                                                                                         Subject to change without notice

PRODUCT DESCRIPTION 3


3.3                  Product characteristics

3.3.1                Device view
                                   InspectorP64x/65x Flex dimensional drawing
                                                             12
                                                                           All distances
                                       6                                   in mm
                                                                     3
                                                                     4
                                                                     5
                                                           21,4
                                                                                 90

                                                               0,2
                                              7                                á

                                                                         à                  â
                                                                           ß                97,2
                                    102
                                                                                              142,8
                                                         9

                                    21,6        8                                           14,2
                                                               46


                                    7,2      75,6                    ã
                                                                     ä
                                                                     å
                                   1       Connection P1, function and design dependent on type
                                   2       Gigabit Ethernet port
                                   3       Connection X2, function and design dependent on type
                                   4       Connection P2, function and design dependent on type
                                   5       Connection X1, function and design dependent on type
                                   6       Reference point for working distance (center of front screen) from InspectorP64x/65x Flex
                                           to object
                                   7       Black cover for the micro SD memory card slot
                                   8       M5 blind tapped holes, 5 mm deep (4 x), for mounting the InspectorP64x/65x Flex
                                   9       Optics protective hood for lens unit and integrated illumination
                                   ß       Sliding nut M5, 5.5 mm deep (2 x), pivoting, for an alternative method of mounting the
                                           InspectorP64x/65x Flex
                                   à       Feedback LED, green
                                   á       Lens unit
                                   â       Outlet opening for light beam from aiming laser
                                   ã       Bar graph display (10 x LEDs)
                                   ä       Function button (2 x)
                                   å       Status display (10 x LEDs)




8019943/1PGH/2024-11 | SICK                                                           O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   17
Subject to change without notice

3 PRODUCT DESCRIPTION

                                       Integrable illumination unit (option)

                                       1                                1
                                       1
                                                                        3
                                       2
                                       1                                1


                                       1           Illumination via 11 LEDs
                                       2           Feedback LED, green (pass), briefly generates a light spot on the object within the field of
                                                   view after a successful analysis (default)
                                       3           Opening in the illumination for the aiming laser for alignment, the red laser LEDs can be
                                                   switched off and generates a red cross on the object within the field of view


3.3.2           Status indicators and functions
                                          Ready |Tst
                                          Result |Tch
                                          Light |A-S
                                          Funct |Usr

                                                                            100%
                                          L/A P3 GbE
                                          L/A P1 GbE
                                                                                           0%
                                          L/A P2 FB
                                          L/A P1 FB
                                          FB|ERR|MS
                                          SF|RUN|NS


                                                                    1   2

                                       1           Enter pushbutton
                                       2           Skip pushbutton

                                       See table 5 for LED descriptions. The functions for the programmable LEDs are defined
                                       by the user in the SICK AppStudio software.
                                       Table 5: LED status descriptions
                                        Display                LED                   Color                        Status
                                        Ready                                        green                        Sensor ready

                                                                                     yellow                       Firmware or SensorApps are
                                                                                                                  being installed on the device.
                                                                                                                  Do not disconnect the power to
                                                                                                                  the device.
                                                                                     red                          Hardware or software error

                                        Result                 Programmable          red, green, blue, fuchsia,   Function defined by user
                                                                                     yellow, aqua, white
                                        Light                  Programmable          red, green, blue, fuchsia,   Function defined by user
                                                                                     yellow, aqua, white
                                        Function               Programmable          red, green, blue, fuchsia,   Function defined by user
                                                                                     yellow, aqua, white
                                        L/A P3 GbE                                   green                        The device is connected to a
                                                                                                                  network
                                        L/A P1 GbE                                                                Not in use
                                        L/A P2 FB                                                                 Not in use
                                        L/A P1 FB                                                                 Not in use
                                        BF|ERR|MS                                                                 Not in use
                                        SF|RUN|NS                                                                 Not in use
                                        LED bar       Programmable                   green                        Function for each LED defined
                                        graph (0 - 9)                                                             by user

                                                    = illuminated,      = flashing




18      O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                                          8019943/1PGH/2024-11 | SICK
                                                                                                                                Subject to change without notice

PRODUCT DESCRIPTION 3


3.3.3                Product features and functionality
                                   The InspectorP6xx is a vision sensor which is well-suited for a wide variety of industrial
                                   tasks thanks to its programmable interface.
                                   Convenient functions such as function buttons, auto-setup, aiming laser, an acoustic
                                   feedback signal, and a green feedback LED reduce the amount of work required for
                                   training and installation.
                                   The microSD memory card can be used to store images or backup copies of parame‐
                                   ters. Thanks to SICK's 4Dpro feature, the InspectorP6xx can be integrated into numer‐
                                   ous industrial networks.

3.3.4                Memory card

                                   NOTICE
                                   Risk of damage to the memory card!
                                   ►    To avoid damaging the microSD memory card, make sure the device is de-ener‐
                                        gized when you insert or remove the card. For this purpose, disconnect the device
                                        from the supply voltage.


                                   NOTICE
                                   Loss of configuration data
                                   Do not remove the memory card or switch off the supply voltage while the parameter
                                   set is being saved. Otherwise all parameters not yet saved permanently will be lost.

                                   The device has a card slot for a microSD memory card integrated in the housing.
                                   The microSD memory card is optional and not included in the scope of delivery of
                                   the device. To ensure that the memory card functions reliably, only use card types
                                   (industrial standard) approved by SICK. These can be found as accessories on the
                                   product page in the Internet, see "Accessories", page 52. The memory card has no
                                   write protection that can be activated.

                                   Inserting the memory card in the device
                                   The card slot for the memory card is located under the hinged cover on the rear side of
                                   the device.
                                   1.   Switch off the supply voltage to the device.
                                   2.   Undo screws (size 2 hex key) on the hinged cover and open the cover.
                                   3.   Opening cover:
                                         ° Carefully pull the upper edge of the cover away from the housing a little at the
                                              level of the hinges on the side. Use both of the recesses on the inside of the
                                              cover to do this.
                                         ° Fold the cover upwards starting from the bottom edge.
                                   4.   Making sure it is in the correct position, insert the memory card into the slot until
                                        it locks into place. When doing this, position the contacts so that they are facing to
                                        the rear and upwards, see the card symbol on the device.
                                   5.   Close the cover again. Make sure that the cover is completely flush with the
                                        housing.
                                   6.   Re-tighten the screws on the cover.
                                   7.   Switch on the supply voltage for the device.

                                   Removing the memory card from the device:
                                   1.   Switch off the supply voltage to the device.
                                   2.   Undo the screws on the cover.



8019943/1PGH/2024-11 | SICK                                                     O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   19
Subject to change without notice

3 PRODUCT DESCRIPTION

                                     3.       Making sure it is in the correct position, push the memory card into the slot until
                                              it is released. When doing this, position the contacts so that they are facing to the
                                              rear and upwards, see the card symbol on the device.
                                     4.       Remove the memory card.
                                     5.       Close the cover again. Make sure that the cover is completely flush with the
                                              housing.
                                     6.       Tighten the screws on the cover.
                                     7.       Switch on the supply voltage for the device.

3.4           SICK AppSpace
                                     The InspectorP6xx product family is part of the SICK AppSpace ecosystem, which
                                     consists of software tools and programmable sensors or devices. See figure 2 for an
                                     overview of SICK AppSpace.




                                        APP DEVELOPERS                                                                         PROGRAMMABLE DEVICES



                                                                                       AppPool
                                            Support                                                                                      Sensor
                                             Portal
                                                                                       TOOLS

                                                                                                   AM
                                                                              AS                            SensorApps
                                          Conference                       AppStudio           AppManager                         Sensor Integration
                                                                                                                                      Machine


                                     Figure 2: SICK AppSpace

                                     SICK AppSpace includes the following components and resources:
                                     • SICK AppManager: A software tool used for the installation and management of
                                         SensorApps and device firmware updates.
                                     • SICK AppPool: A cloud-based repository for storing and sharing SensorApps. SICK
                                         AppPool can be accessed directly from SICK AppManager, SICK AppStudio, and
                                         from the web.
                                     • SICK AppStudio: A Software Development Kit (SDK) for developing SensorApps
                                         on programmable SICK devices. Its user interface for machine operators can be
                                         created individually as a web GUI.
                                     • The SICK Support Portal (support.sick.com) contains tutorials and instructions for
                                         programming the InspectorP6xx in SICK AppStudio.
                                     For more information about downloading SensorApps and programming the device, see
                                     "Commissioning", page 42.
                                     For more information about SICK AppSpace, see www.sick.com/SICK_AppSpace.




20    O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                                      8019943/1PGH/2024-11 | SICK
                                                                                                                          Subject to change without notice

TRANSPORT AND STORAGE 4


4                    Transport and storage
4.1                  Transport

                                   NOTICE
                                   Damage due to improper transport!
                                   ■    The product must be packaged with protection against shock and damp.
                                   ■    Recommendation: Use the original packaging.
                                   ■    Note the symbols on the packaging.
                                   ■    Do not remove packaging until immediately before you start mounting.


4.2                  Transport inspection
                                   Immediately upon receipt in Goods-in, check the delivery for completeness and for any
                                   damage that may have occurred in transit. In the case of transit damage that is visible
                                   externally, proceed as follows:
                                   •    Do not accept the delivery or only do so conditionally.
                                   •    Note the scope of damage on the transport documents or on the transport compa‐
                                        ny's delivery note.
                                   •    File a complaint.

                                   NOTE
                                   Complaints regarding defects should be filed as soon as these are detected. Damage
                                   claims are only valid before the applicable complaint deadlines.


4.3                  Storage
                                   •    Do not store outdoors.
                                   •    Store in a place protected from moisture and dust.
                                   •    Recommendation: Use the original packaging.
                                   •    Do not expose to any aggressive substances.
                                   •    Protect from sunlight.
                                   •    Avoid mechanical shocks.
                                   •    Storage temperature: see "Technical data", page 48.
                                   •    Relative humidity: see "Technical data", page 48.
                                   •    For storage periods of longer than 3 months, check the general condition of all
                                        components and packaging on a regular basis.




8019943/1PGH/2024-11 | SICK                                                    O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   21
Subject to change without notice

5 MOUNTING


5               Mounting
5.1             Overview of mounting procedure
                                       The mounting of the device is divided into the following steps:
                                        •       Mount the device.
                                        •       Align the device with the object.
                                        •       Connect the device to interfaces and supply voltage.
                                        •       Adjust the device.

5.2             Optic kit scope of delivery


                                                               -        -




                                       Figure 3: Optic kit

                                       The optics kit is an accessory which can be optionally ordered for the basic device
                                       (InspectorP64x Flex, InspectorP65x Flex) and is mounted on the C-Mount threaded
                                       connection of the camera housing.

                                       NOTE
                                       The IP protection class IP65 can only be guaranteed with the optic protective hood (can
                                       also be ordered individually).

                                       The following components are included in the scope of delivery of the optic kit:
                                        •       Application-specific lens unit
                                        •       Application-specific integratable illumination unit (VI83I ring illumination unit),
                                                luminous field appropriate for focal distance of lens
                                        •       Two spacers, one with a plated-through connection for the electrical connection
                                        •       Screws: 4 x M2, 5 x 6 mm, 4 x M2, 5 x 12 mm, all screws have a hexagon cylinder
                                                head, SW 2
                                        •       IP65 optics protective hood with screw thread and viewing window

5.3             Preparation for mounting

5.3.1           Installation requirements
                                       Mounting requirements
                                        •       Typical space requirement: see "Field of view diagrams", page 26 and type-spe‐
                                                cific dimensional drawing
                                        •       Comply with the technical data, such as the permitted ambient conditions for
                                                operation, see "Technical data", page 48.
                                        •       Only mount the device using the threaded mounting holes provided or the movable
                                                sliding nuts.
                                        •       Mount the device in a shock and vibration insulated manner.
                                        •       Make sure the device has a clear view of the objects to be scanned.




22      O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                          8019943/1PGH/2024-11 | SICK
                                                                                                                Subject to change without notice

MOUNTING 5


                                   Auxiliary equipment required
                                   ■    Mounting system with sufficient load-bearing capacity and suitable dimensions
                                   ■    4 or 2 M5 screws for mounting the device on a mounting system supplied by the
                                        customer
                                   The screw length depends on the mounting base (wall thickness of the bracket). When
                                   using an optional SICK mounting system, the screws for mounting the device are
                                   included with delivery.

5.3.2                Mounting systems
                                   Mount the device to the mounting systems using at least 2 threaded mounting holes
                                   (M5) or sliding nuts.
                                   The threaded mounting holes are located on the rear side of the device.
                                   The sliding nuts can each be inserted into a slot on the side of the housing.
                                   SICK offers prefabricated mounting systems that are optimally suited for mounting the
                                   device, see "Accessories", page 52.

                                   Customer-supplied mounting system
                                   A customer-supplied mounting system must meet the following requirements:
                                   •    The device can be aligned in the X- and Y-axes.
                                   •    The mounting system must be able to bear the weight of the device and connect‐
                                        ing cables without shock.
                                   •    In mounting situations with strong vibrations, it may be necessary to provide shock
                                        mounts.
                                   •    Mounting options for the device using the threaded mounting holes or sliding nuts
                                        must be available.

5.4                  Mount the optics

                                   NOTE
                                   This mounting step is only required if the optional optics accessory has been included
                                   in the order for a programmable vision sensor of the InspectorP6xx Flex product family.
                                   This does not apply for the Dynamic Focus type.


5.4.1                Mounting the lens and illumination

                                   NOTE
                                   When mounting the optics accessories on the camera housing, always ensure that
                                   there is no power to the system.




8019943/1PGH/2024-11 | SICK                                                    O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   23
Subject to change without notice

5 MOUNTING


                                                                                      5



                                                                                      6


                                                                                      7


                                    1
                                                                                      8
                                    2                                                 9
                                    3
                                    4




                                    1           Spacer, left with electrical connection
                                    2           4 tapped blind holes, M2.5, 5.5 mm deep, for mounting the spacer
                                    3           4 x screws, long
                                    4           Electrical connection for integratable ring illumination unit
                                    5           4 screws, short
                                    6           Integratable ring illumination unit
                                    7           Spacer, right
                                    8           Laser warning shield of the laser output aperture
                                    9           Light inlet with threaded connection for lens

                                    1.  Switch off the supply voltage to the device.
                                    2.  Peel off the white protective sticker on the camera housing that covers the electri‐
                                        cal connection for the ring illumination unit.
                                    3. Place the camera housing on a nonslip base.
                                    4. If required for the country in question, stick the French laser warning label sup‐
                                        plied over the English laser warning label in the camera housing. Make sure to
                                        stick the label exactly over the other one. For safety reasons, the English laser
                                        warning label must not be removed.
                                    5. Remove the protective cap from the round light inlet.
                                    6. Carefully insert the optional filter and spacer disk into the light inlet.
                                    7. Screw the lens unit into the C-mount thread until it engages. This will also lock the
                                        optional filter in place at the same time.
                                    8. Take two pairs of long screws and screw them into the tapped blind holes to
                                        mount each spacer to the correct side of the camera housing.
                                    9. Use the 4 short screws to mount the ring illumination unit to the two spacers.
                                    10. Manually preset the sharpness and mask of the lens unit.
                                    11. Check the setting of the SOPAS ET configuration software.
                                             NOTE
                                             If the required adjustments to the lens are not carried out immediately, mount the
                                             optics protective hood for the lens.




24   O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                                 8019943/1PGH/2024-11 | SICK
                                                                                                                    Subject to change without notice

MOUNTING 5


                                   12. With illumination unit variants with LEDs in risk group RG 2: Attach the country-
                                       specific warning label to the optics protective hood near the light emission, see
                                       "Warning label", page 25.

5.4.2                Warning label
                                   Devices and illumination units with LEDs in risk group RG 2 are provided with the
                                   following warning label.




                                   Figure 4: Risk Group 2: CAUTION - Possibly hazardous optical radiation emitted from this product.
                                   Do not look into the lamp during operation. This could damage your eyes. ICE 62471:2006-07;
                                   EN62471:2008-09

                                   The warning label is located on the exterior of the housing of the devices. For the
                                   illumination units, the warning label is located on the outer ring.
                                   The mounted optics protective hood covers the warning label on the illumination unit.
                                   The integrable illumination unit types in risk group RG 2 therefore contain an additional
                                   warning label for risk group RG 2.
                                   Attach the additional warning label in a well visible location on the outside of the optics
                                   protective hood of the device.

                                   1.   Affix the illumination unit to the device housing.
                                   2.   Manually adjust the focus and aperture of the lens and check these using the live
                                        image in SICK AppStudio.
                                   3.   Attach the protective optics cover and screw it tight.
                                   4.   Attach the warning label to the optics protection hood in a well visible location
                                        near the light outlet.
                                   5.   If the device itself is, for example, integrated into a machine in such a way that
                                        the attached warning label is obscured, attach further clearly visible labels to the
                                        machine close to where the light is emitted.
                                   For commissioning using SICK AppStudio see "Installing SensorApps and programming
                                   the device", page 42.

5.5                  Mounting location

5.5.1                Work area
                                   Depending on the device type, the working range is between 50 mm and 2,200 mm.
                                   •    Dynamic Focus device variant: the device automatically adjusts its focus position
                                        to the working distance with Auto-Setup.
                                   •    Flex device variant: the focus position is manually set on the lens.

                                   The field of view is determined by the focus position, the focal length of the lens, and
                                   the working distance. The necessary working distance can be determined from the field
                                   of view diagram, see "Field of view diagrams", page 26.

5.5.2                Mounting bracket and reflection prevention
                                   In order to avoid reflections from the surfaces to be scanned, mount the device so that
                                   it is tilted from the perpendicular to the surface.


8019943/1PGH/2024-11 | SICK                                                        O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   25
Subject to change without notice

5 MOUNTING




                                       typically 10°... 20°




                                       Figure 5: Mounting angle to use, depending on the application
                                       1           Typical angle 10° ... 20°

                                       Depending on the application, an angle of 0° (brightfield illumination) or up to 45°
                                       (darkfield illumination) is appropriate.

5.5.3           Field of view diagrams
                                       InspectorP64x Flex

                                       Field of view: H x V (mm) 1                                                                   Approx. resolution (mm/px) 2

                                           780 x 530
                                                                                                                                                   0.45
                                           700 x 475
                                                                                         a        b
                                                                                                                      c                            0.40
                                           625 x 425
                                                                                                                                                   0.35
                                           545 x 370
                                                                                                                             d
                                           470 x 320                                                                                               0.30
                                                                                                                                     3             0.25
                                           390 x 265
                                                                                                                                 e
                                           310 x 210                                                                                               0.20

                                                                                                                                 f                 0.15
                                           235 x 160

                                           155 x 105                                                                                               0.10

                                              80 x 55                                                                                              0.05

                                                      0
                                                          0    200      400   600     800    1000 1200 1400 1600 1800 2000 2200

                                                                                    Working distance/focus position (mm) 4
                                                                  a: f = 12 mm                             d: f = 35 mm
                                                                  b: f = 16 mm                             e: f = 50 mm
                                                                  c: f = 25 mm                             f: f = 75 mm

                                       1           Field of view: horizontal x vertical in mm
                                       2           Approximate resolution in mm/px
                                       3           Lens focal length
                                       4           Working distance/focus position in mm




26      O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                                                 8019943/1PGH/2024-11 | SICK
                                                                                                                                       Subject to change without notice

MOUNTING 5


                                   InspectorP652 Dynamic Focus

                                   Field of view: H x V (mm) 1                                                                  Approx. resolution (mm/px) 2

                                   750 x 375
                                                                                                                                                 0.35


                                   600 x 300                                                                                                     0.30

                                                                                                                                 3
                                                                                                                                                 0.25
                                   450 x 225
                                                                                                                                                 0.20


                                   300 x 150                                                                                                     0.15


                                                                                                                                                 0.10
                                    150 x 75
                                                                                                                                                 0.05


                                           0
                                               0   200       600       1000       1400        1800           2200           2600
                                                                   Working distance/focus position (mm) 4

                                                     f = 40 mm (V2D65xR-xxKxx)
                                                     f = 54 mm (V2D652R-xxHxx)

                                   1       Field of view: horizontal x vertical in mm
                                   2       Approximate resolution in mm/px
                                   3       Lens focal length
                                   4       Working distance/focus position in mm




8019943/1PGH/2024-11 | SICK                                                                O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   27
Subject to change without notice

5 MOUNTING

                                    InspectorP652 Flex

                                    Field of view: H x V (mm) 1                                                              Approx. resolution (mm/px) 2

                                     1000 x 500

                                      900 x 450                                                                                             0.45
                                                                                    a        b
                                                                                                                c                           0.40
                                      800 x 400

                                      700 x 350                                                                                             0.35
                                                                                                                     d        3
                                      600 x 300                                                                                             0.30

                                      500 x 250                                                                                             0.25
                                                                                                                         e
                                      400 x 200                                                                                             0.20

                                      300 x 150                                                                          f                  0.15

                                      200 x 100                                                                                             0.10

                                        100 x 50                                                                                            0.05

                                                  0
                                                      0    200       400   600   800    1000 1200 1400 1600 1800 2000 2200
                                                                           Working distance/focus position (mm) 4

                                                              a: f = 12 mm                            d: f = 35 mm
                                                              b: f = 16 mm                            e: f = 50 mm
                                                              c: f = 25 mm                            f: f = 75 mm

                                    1           Field of view: horizontal x vertical in mm
                                    2           Approximate resolution in mm/px
                                    3           Lens focal length
                                    4           Working distance/focus position in mm




28   O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                                             8019943/1PGH/2024-11 | SICK
                                                                                                                                Subject to change without notice

MOUNTING 5


                                   InspectorP654 Dynamic Focus

                                   Field of view: H x V (mm) 1                                                                           Approx. resolution (mm/px) 2

                                   750 x 750
                                                                                                                                                          0.35


                                   600 x 600                                                                                                              0.30

                                                                                                                                            3
                                                                                                                                                          0.25
                                   450 x 450
                                                                                                                                                          0.20


                                   300 x 300                                                                                                              0.15


                                                                                                                                                          0.10
                                   150 x 150
                                                                                                                                                          0.05


                                           0
                                               0       200        600           1000       1400        1800             2200          2600
                                                                            Working distance/focus position (mm) 4

                                                         f = 40 mm (V2D65xR-xxKxx)
                                                         f = 54 mm (V2D654R-xxHxx)

                                   1        Field of view: horizontal x vertical in mm
                                   2        Approximate resolution in mm/px
                                   3        Lens focal length
                                   4        Working distance/focus position in mm

                                   InspectorP654 Flex

                                   Field of view: H x V (mm) 1                                                                            Approx. resolution (mm/px) 2

                                   1000 x 1000

                                     900 x 900                                                                                                            0.45
                                                                                    a       b
                                                                                                                    c                                     0.40
                                     800 x 800

                                     700 x 700                                                                                                            0.35
                                                                                                                           d
                                     600 x 600
                                                                                                                                             3            0.30

                                     500 x 500                                                                                                            0.25
                                                                                                                               e
                                     400 x 400                                                                                                            0.20

                                                                                                                               f                          0.15
                                     300 x 300

                                     200 x 200                                                                                                            0.10

                                     100 x 100                                                                                                            0.05

                                               0
                                                   0     200    400     600      800    1000 1200 1400 1600 1800 2000 2200

                                                                              Working distance/focus position (mm) 4
                                                             a: f = 12 mm                             d: f = 35 mm
                                                             b: f = 16 mm                             e: f = 50 mm
                                                             c: f = 25 mm                             f: f = 75 mm

                                   1        Field of view: horizontal x vertical in mm
                                   2        Approximate resolution in mm/px
                                   3        Lens focal length
                                   4        Working distance/focus position in mm

8019943/1PGH/2024-11 | SICK                                                                         O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   29
Subject to change without notice

5 MOUNTING

                                     Interpretation aid for the field of view diagram
                                     Using the diagram, you can determine the following data for each device type:
                                     • The maximum working distance for a selected resolution
                                     • The dimensions of the field of view that is available for this distance
                                                                                                                                       Approx. resolution (mm/px) 3

                                     Field of view: H x V (mm) 1                    Complete area 2
                                                                                                                       6
                                     1200 x 960
                                                                                                                 a                             0.9

                                                                                                                                               0.8
                                     1000 x 800

                                                                                                                                               0.7

                                       800 x 640
                                                                                                                           b                   0.6
                                                8
                                       600 x 480
                                                                                                                                               0.5   5
                                                                                                                                               0.4

                                       400 x 320                                                                                               0.3

                                                                                                                                               0.2
                                       200 x 160
                                                                                                                                               0.1

                                                                                     7
                                                 0
                                                     0    200         400   600    800    1000   1200   1400    1600   1800    2000

                                                                             Working distance/focus position (mm) 4

                                                             a: f = 9.6 mm
                                                             b: f = 17.1 mm

                                     Figure 6: Example of field of view diagram
                                     1           Field of view: horizontal x vertical in mm
                                     2           Complete area
                                     3           Approximate resolution in mm/px
                                     4           Working distance/Focus position in mm
                                     5           Selected resolution
                                     6           Focal length of lens, here example for f = 9.6 mm
                                     7           Reading off: resultant maximum working distance
                                     8           Reading off: resultant field of view (mm x mm)

                                     Given (in red):
                                     • Resolution 5: approx. 0.5 mm/px
                                     • Focal length of lens 6: 9.6 mm
                                     Read off (in green):
                                     • Maximum working distance 7: approx. 930 mm
                                     • Field of view 8: approx. 640 mm x approx. 510 mm
                                     Both axes of the diagrams must be interpreted linearly.

5.6           Mounting the device
                                     1.       If required for the country in question, stick the French warning label supplied over
                                              the English warning label for LED risk group RG 2.
                                     2.       Mount the device in a suitably prepared mounting system with M5 screws using
                                              the threaded mounting holes or sliding nuts provided.




30    O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                                                   8019943/1PGH/2024-11 | SICK
                                                                                                                                       Subject to change without notice

MOUNTING 5


                                        °    Screw the screws no more than 5 mm into the threaded mounting holes or
                                             sliding nuts.
                                        ° To do so, either use all 4 threaded mounting holes on the rear of the device
                                             or the two sliding nuts on the side of the device.
                                        ° Attach the separately-ordered, optional SICK mounting system using the slid‐
                                             ing nuts on the device. Mounting systems are available as accessories, see
                                             "Accessories", page 52.
                                   3.   Align the device taking into consideration the field of view (see "Field of view
                                        diagrams", page 26) and the application circumstances (see "Installation require‐
                                        ments", page 22).
                                        1 4,2 Mpx                     2 2,1 Mpx                                  3 1,7 Mpx




                                                                  4                                    4                                          4

                                        Figure 7: Resolution-dependent field of view geometries
                                        1      InspectorP654 with 4.2 mpx image sensor
                                        2      InspectorP652 with 2.1 mpx image sensor
                                        3      InspectorP642 with 1.7 mpx image sensor
                                        4      Field of view

                                   4.   Connect the device to interfaces and supply voltage when disconnected from
                                        voltage, see "Connecting the device", page 37.
                                   ✓    The Ready status LED lights up green.
                                   5.   Perform fine adjustment.




8019943/1PGH/2024-11 | SICK                                                       O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   31
Subject to change without notice

6 ELECTRICAL INSTALLATION


6               Electrical installation
6.1             Wiring instructions

                                       NOTE
                                       Pre-assembled cables can be found on the product page.
                                       The call is made via the SICK Product ID: pid.sick.com/{P/N}/{S/N}
                                       {P/N} corresponds to the part number of the product, see type label.
                                       {S/N} corresponds to the serial number of the product, see type label (if indicated).


                                       NOTICE
                                       Faults during operation and defects in the device or the system
                                       Incorrect wiring may result in operational faults and defects.
                                        ■       Follow the wiring notes precisely.

                                       The enclosure rating stated in the technical data is achieved only with screwed plug
                                       connectors or protective caps.
                                       Configure the circuits connected to the device as ES1 circuits or as SELV circuits (SELV
                                       = Safety Extra Low Voltage). The voltage source must meet the requirements of ES1
                                       and PS2 (EN 62368-1) or SELV and LPS (EN 60950-1).
                                       Protect the device with an external slow-blow fuse at the beginning of the supply cable.
                                       Connect the connecting cables in a de-energized state. Do not switch on the supply
                                       voltage until installation is complete and all connecting cables are connected to the
                                       device and control.
                                       Wire cross-sections in the supply cable from the customer’s power system must be
                                       implemented in accordance with the applicable standards.
                                       In the case of open end cables, make sure that bare wire ends do not touch. Wires
                                       must be appropriately insulated from each other.

6.1.1           Data cables
                                       Important information

                                       NOTE
                                       Layout of data cables
                                        ■       Use screened data cables with twisted-pair wires.
                                        ■       Implement the screening design correctly and completely.
                                        ■       To avoid interference, always use EMC-compliant cables and layouts. This applies,
                                                for example, to cables for switched-mode power supplies, motors, clocked drives,
                                                and contactors.
                                        ■       Do not lay cables over long distances in parallel with power supply cables and
                                                motor cables in cable channels.

                                       Length of cable and data transmission rate
                                       The maximum length of cable between device and host computer depends on the
                                       interface type and the data transmission rate.

                                       Further topics
                                        •       For information on data transmission rates and lengths of cable: Wiring the data
                                                interface


32      O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                         8019943/1PGH/2024-11 | SICK
                                                                                                               Subject to change without notice

ELECTRICAL INSTALLATION 6


6.2                  Prerequisites for safe operation of the device

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




8019943/1PGH/2024-11 | SICK                                                     O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   33
Subject to change without notice

6 ELECTRICAL INSTALLATION

                                     On widely distributed system installations with correspondingly large potential differen‐
                                     ces, the setting up of local islands and connecting them using commercially available
                                     electro-optical signal isolators is recommended. This measure achieves a high degree
                                     of resistance to electromagnetic interference.
                                     The use of electro-optical signal isolators between the islands isolates the ground loop.
                                     Within the islands, a stable equipotential bonding prevents equalizing currents on the
                                     cable shields.
                                     Measures for small system installations
                                     For smaller installations with only slight potential differences, insulated mounting of the
                                     device and peripheral devices may be an adequate solution.
                                     Even in the event of large differences in the ground potential, ground loops are effec‐
                                     tively prevented. As a result, equalizing currents can no longer flow via the cable shields
                                     and metal housing.

                                     NOTICE
                                     The voltage supply for the device and the connected peripheral devices must also
                                     guarantee the required level of insulation.
                                     Under certain circumstances, a tangible potential can develop between the insulated
                                     metal housings and the local ground potential.


6.3           Connections and pin assignment
                                     Overview



                                                 P2            P1

                                          X1          X2               P3




                                     Table 6: Connection overview
                                      Connec‐ V2D6xxR-MCxxAx connec‐            V2D6xxR-MCxxFx connec‐ V2D6xxR-MCxxHx connec‐
                                      tion    tion variant 1 (stand-alone       tion variant 2 (for systems) tion variant 3 (with Dual
                                              solution)                                                      Port PROFINET)
                                      X1              Power/SerialData/CAN/IO   CAN IN                       Power/SerialData/CAN/IO
                                      X2              USB                       Triggering of external illumi‐ USB
                                                                                nation
                                      P1              Gigabit Ethernet          Gigabit Ethernet             Ethernet (100 Mbit/s)
                                      P2              ‒                         CAN OUT                      Ethernet (100 Mbit/s)
                                      P3              Gigabit Ethernet          Gigabit Ethernet             Gigabit Ethernet

                                     Power/SerialData/CAN/IO
                                     12  2                 1         11
                                     3                               10
                                     13                              16
                                     4                                9
                                     17                               8
                                     5 14 6                7         15
                                     Figure 8: Male connector, M12, 17-pin, A-coded

                                     Table 7: Pin assignment for Power/SerialData/CAN/IO
                                      Pin                           Signal          Description
                                      1                             GND             Supply voltage: 0 V


34    O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                                  8019943/1PGH/2024-11 | SICK
                                                                                                                      Subject to change without notice

ELECTRICAL INSTALLATION 6


                                   Pin           Signal                       Description
                                   2             VS                           Supply voltage: DC 24 V ± 20%
                                   3             CAN L                        CAN-Bus LOW (IN/OUT)
                                   4             CAN H                        CAN-Bus HIGH (IN/OUT)
                                   5             TD+ (RS-422), Host           Host interface (sender+)
                                   6             TD- (RS-422), Host           Host interface (sender-)
                                                 TxD (RS-232), host
                                   7             TxD (RS-232), AUX            AUX interface (sender)
                                   8             RxD (RS-232), AUX            AUX interface (receiver)
                                   9             SensGND                      Digital input ground
                                   10            Sensor 1                     Digital input 1
                                   11            RD+ (RS-422) Host            Host interface (receiver+)
                                   12            RD- (RS-422), host           Host interface (receiver–)
                                                 RxD (RS-232), host
                                   13            Result 1                     Digital output 1
                                   14            Result 2                     Digital output 2
                                   15            Sensor 2                     Digital input 2
                                   16            Result 3                     Digital output 3
                                   17            Result 4                     Digital output 4


                                   CAN IN
                                   2                  1

                                                      5

                                   3                  4

                                   Figure 9: Male connector, M12, 5-pin, A-coded

                                   Table 8: Pin assignment for CAN IN
                                   Pin           Signal                       Description
                                   1             –                            Shielding
                                   2             VS                           Supply voltage: DC 24 V ± 20%
                                   3             GND                          Supply voltage: 0 V
                                   4             CAN H                        CAN-Bus HIGH (IN/OUT)
                                   5             CAN L                        CAN-Bus LOW (IN/OUT)


                                   CAN OUT
                                   1                  2

                                   5

                                   4                  3

                                   Figure 10: M12 female connector, 5-pin, A-coded

                                   Table 9: Pin assignment for CAN OUT
                                   Pin           Signal                       Description
                                   1             –                            Shielding
                                   2             VS                           Supply voltage: DC 24 V ± 20%
                                   3             GND                          Supply voltage: 0 V
                                   4             CAN H                        CAN-Bus HIGH (IN/OUT)
                                   5             CAN L                        CAN-Bus LOW (IN/OUT)




8019943/1PGH/2024-11 | SICK                                                        O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   35
Subject to change without notice

6 ELECTRICAL INSTALLATION

                                     USB
                                     1                            3



                                     2                            4

                                     Figure 11: Female connector M8, 4-pin

                                     Table 10: Pin assignment for USB
                                      Pin                    Signal                Description
                                      1                      D-                    Data-
                                      2                      VUSB                  USB voltage: DC 5 V
                                      3                      D+                    Data+
                                      4                      GND                   Supply voltage: 0 V


                                     Triggering of external illumination
                                                     4
                                      3
                                                         1


                                     Figure 12: Female connector M8, 3-pin

                                     Table 11: Pin assignment for triggering of external illumination unit
                                      Pin                    Signal                Description
                                      1                      Sensor 1              Digital input 1
                                      2                      ‒                     ‒
                                      3                      Result 4              Digital output 4
                                      4                      SensGND               Digital input ground


                                     Gigabit Ethernet
                                     2                            3
                                     1                            4
                                     8                            5
                                     7                            6

                                     Figure 13: Female connector, M12, 8-pin, X-coded

                                     Table 12: Pin assignment for Gigabit Ethernet
                                      Pin                    Signal                Description
                                      1                      TRD0_P                Sender+/receiver+ 0
                                      2                      TRD0_N                Sender–/receiver– 0
                                      3                      TRD1_P                Sender+/Receiver+ 1
                                      4                      TRD1_N                Sender–/Receiver– 1
                                      5                      TRD3_P                Sender+/Receiver+ 3
                                      6                      TRD3_N                Sender–/Receiver– 3
                                      7                      TRD2_P                Sender+/Receiver+ 2
                                      8                      TRD2_N                Sender–/Receiver– 2


                                     Ethernet
                                     1                            2



                                     4                            3

                                     Figure 14: M12 female connector, 4-pin, D-coded


36    O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                          8019943/1PGH/2024-11 | SICK
                                                                                                              Subject to change without notice

ELECTRICAL INSTALLATION 6


                                   Table 13: Pin assignment for Ethernet
                                    Pin                      Signal                              Description
                                    1                        TX+                                 Sender+
                                    2                        RX+                                 Receiver+
                                    3                        TX-                                 Sender-
                                    4                        RX-                                 Receiver-



6.4                  Connection diagrams
                                   Connection principle
                                                CDB650-204
                                                Connection Inspector64x               Ethernet
                                                module 1 Inspector65x
                                                       ...                                          SICK
                                                       ...
                                                                                                  AppStudio

                                                1 2

                                                  GND                 X1    P3                    Programming 2
                                            DC 24 V ± 20 %
                                                               Power...    Ethernet
                                                                                       USB
                                                                                                  Image display 3
                                                                                                  Diagnostics 4
                                                              Cable 5      Cable 6
                                   Figure 15: General connection principle
                                   1          CDB650-204 connection module
                                   2          Programming
                                   3          Image display
                                   4          Diagnostics
                                   5          Cable, e.g. part no. 6051194 (3 m)
                                   6          Cable, e.g. part no. 6049728 (2 m)

                                   Wiring without SICK connection module
                                   When using customer-specific connection units, the wiring principle for the signals can
                                   be found in the connection diagrams for the connection module CDM420-0006, see
                                   "Connection of the device to CDM420-0006", page 63.

6.5                  Connecting the device

6.5.1                Using CDB and CDM connection modules
                                   Table 14: Possible combinations of device and connection modules
                                    Connection on the device                          Connection modules                             Connection cable
                                    Male connector, M12, 17-pin, A-                   CDB650-204                                     Cable 1:1 1)
                                    coded
                                                                                      CDM420-0006 2)                                 Adapter cable 3)
                                   1)     Connection cable 1:1 (female connector, M12, 17-pin, A-coded / male connector, M12, 17-pin, A-coded).
                                   2)     CDM420-0007: for connecting 2 devices.
                                   3)     Adapter cable (female connector, M12, 17-pin, A-coded / male connector, D-Sub-HD, 15-pin).

                                   Connecting device with connection module
                                    Connection modules                     Reference
                                    CDB650-204                             see "Connection of the device to CDB650-204", page 53
                                    CDM420-0006                            see "Connection of the device to CDM420-0006", page 63




8019943/1PGH/2024-11 | SICK                                                                           O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   37
Subject to change without notice

6 ELECTRICAL INSTALLATION


                                       NOTE
                                       The operating instructions of the connection modules contains detailed information
                                       on mounting and electrical installation. The operating instructions are available as a
                                       download on the product page of the connection module.
                                       Connection module product page
                                       • www.sick.com/CDB
                                       • www.sick.com/CDM

6.5.2           Connecting the supply voltage
                                       The voltage source meets the requirements of ES1 and PS2 (EN 62368-1) or SELV and
                                       LPS (EN 60950-1).
                                       Table 15: Required supply voltage VS and power output
                                        Supply voltage VS                                        Power source: required power output 1)
                                        DC 24 V ± 20%                                            At least 30 W
                                       1)    Valid for device with 4 loaded digital outputs (each 100 mA).

                                       When connecting via the optional CDB or CDM connection module: if the CMC600
                                       cloning module is used, an additional output power of 0.5 W is required.

                                       Protecting the supply cables
                                       To ensure protection against short-circuits/overload in the customer’s supply cables,
                                       appropriately choose and protect the wire cross-sections used.
                                       Observe applicable standards (Germany):
                                       • DIN VDE 0100 (part 430)
                                       • DIN VDE 0298 (part 4) and DIN VDE 0891 (part 1)
                                       Connecting device without connection module
                                       For a supply voltage of 24 V DC ± 20%, protect the device using a separate fuse rated
                                       at 2 A.
                                       ►        Install the fuse in the supply circuit at the start of the supply cable.

                                       Connecting device with connection module
                                       The supply voltage for the device is protected in the connection modules in the circuit
                                       after switch S1.
                                       Table 16: Protection of the supply voltage in the connection module
                                        Connection modules                Supply voltage fuse protec‐ Reference
                                                                          tion
                                        CDB650-204                        2 A (slow-blow)                    see "Connecting supply voltage
                                                                                                             for the device in CDB650-204",
                                                                                                             page 56
                                        CDM420-0006                       2 A (slow-blow)                    see "Connecting supply voltage
                                                                                                             for the device in CDM420-0006",
                                                                                                             page 66


6.5.3           Wiring the data interface
                                       Wiring the Internet interface
                                       1.       Connect the device to the Ethernet connection of the computer via the adapter
                                                cable.
                                       2.       Set up communication via the SICK AppManager software.


38      O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                                      8019943/1PGH/2024-11 | SICK
                                                                                                                            Subject to change without notice

ELECTRICAL INSTALLATION 6


                                   NOTE
                                   The Ethernet interface of the device has an Auto-MDIX function. This automatically
                                   adjusts the transmission speed as well as any necessary crossover connections.

                                   Wiring the serial data interface
                                   The maximum data transmission rate for the serial interface depends on the length of
                                   cable and on the type of interface.
                                   Table 17: Data transmission rates and recommended maximum lengths of cable
                                   Interface          Data transmission rate                     Distance to the target computer
                                                                                                 (host)

                                   NOTICE
                                   Risk of damage to the internal interface modules!
                                   If the serial data interfaces are wired incorrectly, then electronic components in the
                                   device could get damaged.
                                   ■    Observe the information on wiring.
                                   ■    Carefully check the wiring prior to switching on the device.


                                   NOTE
                                   Control the serial data interface in the device with the API functions. In order to activate
                                   the serial data interface, use an installed SensorApp which contains this function.

                                   Wiring data interfaces via a connection module
                                   Connection modules          Data interface                    Reference


6.5.4                Wiring the CAN interface

                                   NOTE
                                   Control the CAN data interface in the device with the API functions. In order to activate
                                   the CAN data interface, use an installed SensorApp which contains this function.

                                   Wiring CAN interfaces via a connection module
                                   Connection modules          Interface                         Reference
                                   CDB650-204                  CAN                               see "Wiring the CAN interface of
                                                                                                 the device in the CDB650-204",
                                                                                                 page 58
                                   CDM420-0006                 CAN                               see "Wiring the CAN interface of
                                                                                                 the device in the CDM420-0006",
                                                                                                 page 68


6.5.5                Wiring the digital inputs
                                   The device has 2 switching digital inputs (Sensor1, Sensor 2). IN/OUT 3 ... 6 can also
                                   be used as digital inputs.
                                   Functions (examples)
                                   • Start and end external reading cycle.
                                   • Feed in incremental signal.




8019943/1PGH/2024-11 | SICK                                                      O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   39
Subject to change without notice

6 ELECTRICAL INSTALLATION

                                       Position of digital inputs
                                       • Male connector of the device (M12, 17-pin, A-coded)
                                       • Adapter cable (female connector, M12, 17-pin, A-coded/male connector, D-Sub-
                                            HD, 15-pin)
                                       • Open end of the adapter cable (female connector, M12, 17-pin, A-coded/open
                                            end)
                                       All digital inputs are available at the individual positions.

                                       Wiring digital inputs via connection module
                                        Connection modules              Digital inputs            Reference
                                        CDB650-204                      SENS/IN 1                 see "Wiring digital inputs of
                                                                        SENS/IN 2                 the device in the CDB650-204",
                                                                                                  page 60
                                                                        Parameterizable digital   page 63
                                                                        inputs IN 3 ... IN 6
                                        CDM420-0006                     Sensor 1                  see "Wiring digital inputs of the
                                                                        Sensor 2                  device in the CDM420-0006",
                                                                                                  page 70
                                                                        Parameterizable digital   page 63
                                                                        inputs IN 3 and IN 4


6.5.6           Wiring the digital outputs
                                       The four IN/OUT 3 ... 6 switching digital outputs can be assigned independently of each
                                       other with various functions for the output of the result status. If the allocated event
                                       occurs in the analysis process, then the corresponding digital output is live after the
                                       end of the trigger for the selected pulse duration.
                                       Position of digital outputs
                                       • Male connector of the device (M12, 17-pin, A-coded)
                                       • Open end of the adapter cable (female connector, M12, 17-pin, A-coded/open
                                            end)
                                       •    CDB650-204      connection module
                                       All digital outputs are each available at the individual positions.

                                       NOTE
                                       Provide an arc-suppression switch at the digital output if inductive load is present.
                                       ►        Attach a freewheeling diode directly to the load for this purpose.


                                       NOTE
                                       Capacitive loads on the digital outputs have an effect on the switch-on and switch-off
                                       behavior. A maximum capacitance of 100 nF is the limit value.

                                       Function assignment

                                       NOTE
                                       Control the digital outputs in the device with the API functions. In order to assign the
                                       digital output functions, use an installed SensorApp which contains this function.




40      O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                             8019943/1PGH/2024-11 | SICK
                                                                                                                   Subject to change without notice

ELECTRICAL INSTALLATION 6


                                   Wiring digital outputs via connection module
                                   Connection mod‐ Digital outputs                               Reference
                                   ules
                                   CDB650-204       IN/OUT 3 ... 6 (RES/OUT 1 ... 4)             see "Wiring digital outputs of
                                                                                                 the device in the CDB650-204",
                                                                                                 page 62
                                   CDM420-0006      N/OUT 3 ... 4                                see "Wiring digital outputs of
                                                                                                 the device in the CDM420-0006",
                                                                                                 page 72




8019943/1PGH/2024-11 | SICK                                                      O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   41
Subject to change without notice

7 COMMISSIONING


7             Commissioning
7.1           Installing SensorApps and programming the device

                                     NOTE
                                     Update the device firmware version before you start using the device. Always use the
                                     latest version, unless there is a specific need to use an older version. Download the
                                     latest version of the firmware from the SICK Support Portal (support.sick.com) and
                                     install it using SICK AppManager.

                                     Installing SensorApps on the device
                                     Use the SICK AppManager software to manage and install SensorApp packages
                                     (*.sapk files) on the device. The latest version of SICK AppManager is available from
                                     www.sick.com/SICK_AppManager.
                                     Many SensorApps have a web user interface which is accessed by following the steps
                                     below:
                                     1.       Open a Google Chrome web browser window.
                                     2.       Type the IP address of the device. The default IP address is 192.168.0.1.

                                     Installing and starting the development environment
                                     The SICK AppStudio development environment is used by default to program the device
                                     and to perform diagnostics in case of faults.
                                     1.       Download and install the latest version of SICK AppStudio from www.sick.com/
                                              SICK_AppStudio. Administrator rights may be required on the PC to install the
                                              software.
                                     2.       Enter your personal license key to complete the installation.
                                     3.       Start the program. Path: Start > All programs > SICK > SICK AppStudio
                                     4.       Establish a connection between the software and the device via Ethernet.
                                     ✓        The connection wizard starts automatically.
                                     5.       The following IP address is configured by default on the device:
                                              ° IP address P1: 192.168.0.1
                                     First steps with the device
                                     The device is supplied with a pre-installed SensorApp called ImageSetup.
                                     1.       In SICK AppStudio, double-click the paths in the AppExplorer to display all content.
                                     2.       Double-click the primary script file to open it in the script editor and display the
                                              source code.

                                     Receiving images
                                     1.       Click on the corresponding button to start all apps.
                                     2.       The device page (in online mode) will now display an image on the right-hand
                                              side, enabling basic configuration to adjust parameters such as illumination, gain,
                                              contrast, and trigger methods.

                                     NOTE
                                     If the device page displays Error 404, port 80 is already occupied by another piece
                                     of software. To find out which process you need to quit, go to Task Manager > Perform‐
                                     ance tab > Resource monitor > Network tab.
                                     Search for port 80 among the listed ports.




42    O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                          8019943/1PGH/2024-11 | SICK
                                                                                                              Subject to change without notice

COMMISSIONING 7


                                   C-mount lens: adjusting the brightness and sharpness
                                   1.   Remove the protective optics cover.
                                   2.   Loosen the lock nut fitting on the aperture ring and sharpness ring.
                                   3.   Adjust the mask using the aperture ring (top ring) on the lens to a low value such
                                        as “2”.
                                   4.   Reduce the shutter time and brightness until the object is clearly visible on the
                                        image.
                                   5.   Increase the image sharpness using the sharpness ring (bottom ring) on the lens.
                                        The object must be clearly displayed in sharp focus so that all edges are easy to
                                        identify.
                                   6.   Use the lock nut fitting to fix the sharpness ring setting in place.
                                   7.   Apply the correct mask setting for the depth of field. In order to do this, check the
                                        settings with the test object. Adjust the mask to a higher value. If a greater depth
                                        of field is required, select a higher value. Bear in mind that using a greater mask
                                        value reduces image brightness, meaning that brightness must be increased using
                                        the software. This reduces image quality.
                                   8.   Fix the aperture ring using the lock nut fitting.
                                   9.   Mount the protective optics cover.

                                   Continuing programming
                                   ►    Adjust the settings for additional functions during planned operation such as
                                        triggers, result formats, data interface, etc.

                                   Quitting programming
                                   1.   Save the program in the non-volatile memory of the device.
                                   2.   Save the parameter set on the PC.




8019943/1PGH/2024-11 | SICK                                                    O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   43
Subject to change without notice

8 MAINTENANCE


8             Maintenance
8.1           Maintenance plan


8.2           Cleaning
                                     Cleaning includes the viewing window and the housing of the device.

                                     NOTICE
                                     Equipment damage due to improper cleaning.
                                     Improper cleaning may result in equipment damage.
                                      ■       Only use recommended cleaning agents and tools.
                                      ■       Never use sharp objects for cleaning.

                                     ►        The device must be cleaned regularly from the outside to guarantee heat dissipa‐
                                              tion and therefore operation. Use a dry cloth or an industrial vacuum cleaner for
                                              cleaning. Do not use cleaning agents.

                                     Cleaning the viewing window
                                     Check the viewing window of the device for accumulated dirt at regular intervals.
                                     This is especially important in harsh operating environments (dust, abrasion, damp,
                                     fingerprints, etc.).
                                     The viewing window lens must be kept clean and dry during operation.

                                     NOTE
                                     Static charging may cause dust particles to stick to the viewing window. This effect can
                                     be reduced by using an anti-static cleaning agent in combination with the SICK lens
                                     cloth (part number 4003353).

                                     The type of material used for the viewing window can be found on the type label (see
                                     "Type code", page 15).

                                     Cleaning procedure:

                                     CAUTION
                                     Optical radiation: LED risk group 1, visible radiation, 400 nm to 780 nm
                                     The LEDs may pose a danger to the eyes in the event of incorrect use.
                                      ■       Do not look into the light source intentionally.
                                      ■       Do not open the housing. Opening the housing will not switch off the light source.
                                              Opening the housing may increase the level of risk.
                                      ■       Comply with the current national regulations on photobiological security of lamps
                                              and lamp systems.




44    O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                          8019943/1PGH/2024-11 | SICK
                                                                                                              Subject to change without notice

MAINTENANCE 8


                                   CAUTION
                                   Warning! Optical radiation: LED risk group 2, visible radiation, 400 nm to 780 nm
                                   Potentially dangerous optical radiation. Can be damaging to the eyes.
                                   ■    Do not look into the light source for extended periods of time.
                                   ■    Never point the light source at people.
                                   ■    Avoid any reflections on people from reflective surfaces. Be particularly careful
                                        during mounting and alignment work.
                                   ■    Do not open the housing. Opening the housing will not switch off the light source.
                                        Opening the housing may increase the level of risk.
                                   ■    Comply with the current national regulations on photobiological security of lamps
                                        and lamp systems.

                                   If the product is operated in conjunction with external illumination systems, the risks
                                   described here may be exceeded. This must be taken into consideration by users on a
                                   case-by-case basis.

                                   CAUTION
                                   Optical radiation: Class 1 Laser Product
                                   The accessible radiation does not pose a danger when viewed directly for up to 100
                                   seconds. It may pose a danger to the eyes and skin in the event of incorrect use.
                                   ■    Do not open the housing. Opening the housing may increase the level of risk.
                                   ■    Current national regulations regarding laser protection must be observed.

                                   For both radiation types:
                                   It is not possible to entirely rule out temporary disorienting optical effects, particularly
                                   in conditions of dim lighting. Disorienting optical effects may come in the form of
                                   dazzle, flash blindness, afterimages, photosensitive epilepsy, or impairment of color
                                   vision, for example.
                                   ►    Switch off the device for the duration of the cleaning operation. If this is not
                                        possible, wear suitable laser safety goggles. These must absorb radiation of the
                                        device’s wavelength effectively.
                                   ►    Glass window: remove dust from the viewing window using a soft, clean brush. If
                                        necessary, also clean the viewing window with a clean, damp, lint-free cloth, and a
                                        mild anti-static lens cleaning fluid.
                                   ►    Plastic window: clean the viewing window only with a clean, damp, lint-free cloth,
                                        and a mild anti-static lens cleaning fluid.

                                   NOTICE
                                   If the inspection window is scratched or damaged (cracked or broken), the lens must be
                                   replaced. Contact SICK Support to arrange this.
                                   ■    If the inspection window is cracked or broken, take the device out of operation
                                        immediately for safety reasons and have it repaired by SICK.


8.3                  Repairs
                                   Repair work on the device may only be performed by qualified and authorized personnel
                                   from SICK AG. Interruptions or modifications to the device by the customer will invalid‐
                                   ate any warranty claims against SICK AG.




8019943/1PGH/2024-11 | SICK                                                       O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   45
Subject to change without notice

9 TROUBLESHOOTING


9               Troubleshooting
9.1             Overview of possible errors and faults
                                       Table 18: Errors and faults
                                        Situation                       Error/fault
                                        Mounting                        ■   Device poorly aligned to the object (e.g. dazzle).
                                        Electrical installation         ■   Data interfaces of the device incorrectly wired.
                                        Programming                     ■   See SICK AppSpace interface documentation (troubleshooting
                                                                            of individual objects and functions).
                                        Operation                       ■   Trigger control incorrect and/or not suitable for the object.
                                                                        ■   Device faults (hardware/software).


9.2             Detailed fault analysis

9.2.1           LEDs on the device
                                       The LED display indicates the status of the device and its connections. When trouble‐
                                       shooting, see the information given for the different LEDs.

                                       Further topics
                                        •       Status indicators and functions

9.3             SICK service
                                       If you require any technical information, our SICK Service will be happy to help. To find
                                       your agency, see the final page of this document.

                                       NOTE
                                       Before calling, make a note of all type label data such as type code, serial number, etc.,
                                       to ensure faster processing.


9.4             Returns
                                       ►        Only send in devices after consulting with SICK Service.
                                       ►        The device must be sent in the original packaging or an equivalent padded pack‐
                                                aging.

                                       NOTE
                                       To enable efficient processing and allow us to determine the cause quickly, please
                                       include the following when making a return:
                                        •       Details of the contact person
                                        •       Description of the application
                                        •       Description of the fault that occurred




46      O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                                  8019943/1PGH/2024-11 | SICK
                                                                                                                        Subject to change without notice

DECOMMISSIONING 10


10                   Decommissioning
10.1                 Disposal
                                   If a device can no longer be used, dispose of it in an environmentally friendly manner
                                   in accordance with the applicable country-specific waste disposal regulations. Do not
                                   dispose of the product along with household waste.

                                   NOTICE
                                   Danger to the environment due to improper disposal of the device.
                                   Disposing of devices improperly may cause damage to the environment.
                                   Therefore, observe the following information:
                                   ■    Always observe the national regulations on environmental protection.
                                   ■    Separate the recyclable materials by type and place them in recycling containers.




8019943/1PGH/2024-11 | SICK                                                    O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   47
Subject to change without notice

11 TECHNICAL DATA


11             Technical data

                                      NOTE
                                      The relevant online product page for your product, including technical data, dimensional
                                      drawing, and connection diagrams, can be downloaded, saved, and printed from the
                                      Internet.
                                      The call is made via the SICK Product ID: pid.sick.com/{P/N}/{S/N}
                                      {P/N} corresponds to the part number of the product, see type label.
                                      {S/N} corresponds to the serial number of the product, see type label (if indicated).
                                      Please note: This documentation may contain further technical data.


11.1           Optics and Illumination
                                       Type                            InspectorP64x Flex (V2D64xP-           InspectorP65x DynamicFocus
                                                                       MCxxxx)                                (V2D65xP-MExxxx)
                                                                       InspectorP65x Flex (V2D65xP-
                                                                       MCxxxx)
                                       Focus                           Manual adjustment of the sharpness Dynamic and externally triggered
                                                                       and aperture on the optional lens  electrical focus adjustment for work‐
                                                                       unit                               ing distance
                                       Shutter technol‐                Global shutter                         Global shutter
                                       ogy
                                       Illumination for                Optional e.g., variants of the VI83I   11 x LED, visible light.
                                       field of view                   integrable illumination unit:          White (λ = 6,000 ± 500 K)
                                                                       11 x LED, visible light.               Blue (λ = 455 ± 20 nm)
                                                                       White (λ = 6,000 ± 500 K)
                                                                       Blue (λ = 455 ± 20 nm)
                                                                       Red (λ = 620 ± 30 nm)
                                       Feedback LED                    Optional e.g., variants of the VI83I   1 x LED, visible light.
                                       (spot in field of               integrable illumination unit:          Green (λ = 525 ± 15 nm)
                                       view)                           1 x LED, visible light.
                                                                       Green (λ = 525 ± 15 nm)




48     O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                                           8019943/1PGH/2024-11 | SICK
                                                                                                                                Subject to change without notice

TECHNICAL DATA 11


                                   Type                InspectorP64x Flex (V2D64xP-                InspectorP65x DynamicFocus
                                                       MCxxxx)                                     (V2D65xP-MExxxx)
                                                       InspectorP65x Flex (V2D65xP-
                                                       MCxxxx)
                                   LED risk group of   “White + Feedback LED” option               “White + Feedback LED” option
                                   illumination unit   “Blue – Medium + Feedback LED”
                                                       option                                       • Risk group 1 (low risk) accord‐
                                                                                                        ing to IEC 62471-1: 2006-07/EN
                                                       “Blue – Wide + Feedback LED”                     62471-1: 2008-09.
                                                       option
                                                                                                   Radiance:
                                                       • Risk group 1 (low risk) accord‐           LB: < 10 x 103 W/(m2sr) within
                                                          ing to IEC 62471-1: 2006-07/EN
                                                                                                   100 s; at a distance of ≥ 200 mm
                                                          62471-1: 2008-09.
                                                                                                   LR: < 7 x 105 W/(m2sr) within 10 s; at
                                                       “Red + Feedback LED” option                 a distance of ≥ 200 mm
                                                       Radiance:
                                                       LB: < 10 x 103 W/(m2sr) within
                                                       100 s; at a distance of ≥ 200 mm
                                                       LR: < 7 x 105 W/(m2sr) within 10 s; at
                                                       a distance of ≥ 200 mm
                                                       “Blue – Narrow + Feedback LED”              “Blue + Feedback LED” option
                                                       option
                                                                                                    • Risk group 2 (moderate risk)
                                                       • Risk group 2 (moderate risk)                   according to IEC 62471-1:
                                                          according to IEC 62471-1:                     2006-07/EN 62471-1: 2008-09
                                                          2006-07/EN 62471-1: 2008-09                   due to exposure to blue light.
                                                          due to exposure to blue light.
                                                                                                   Radiance:
                                                       Radiance:                                   LB: < 10 x 103 W/(m2sr) within 50 s
                                                       LB: < 10 x 103 W/(m2sr) within 50 s         (RG 2); at a distance of ≥ 200 mm
                                                       (RG 2); at a distance of ≥ 200 mm           LR: < 7 x 105 W/(m2sr) within 10 s
                                                       LR: < 7 x 105 W/(m2sr) within 10 s          (RG 1); at a distance of ≥ 200 mm
                                                       (RG 1); at a distance of ≥ 200 mm           Risk RG 1 (low risk) corresponding to
                                                       Risk RG 1 (low risk) corresponding to       LB < 10 x 103 W/(m2sr) within 100 s
                                                       LB < 10 x 103 W/(m2sr) within 100 s         for distances > 1 m.
                                                       for distances > 1 m.
                                   Aiming laser (field Visible light. Red (λ = 630 nm ... 680 nm), can be disengaged
                                   of view)
                                   Laser class         Class 1 Laser Product according to EN 60825-1:2014+A11:2021; IEC
                                                       60825-1:2014. Complies with 21CFR1040.10/11 except for conformance
                                                       with IEC 60825-1 Ed.3., as described in Laser Notice No.56, dated May 8,
                                                       2019. P < 1.40 mW


11.2                 Performance
                                   Type                InspectorP64x Flex (V2D64xP-                InspectorP65x DynamicFocus
                                                       MCxxxx)                                     (V2D65xP-MExxxx)
                                                       InspectorP65x Flex (V2D65xP-
                                                       MCxxxx)
                                   Working distance see "InspectorP64x Flex", page 26  see "InspectorP652 Flex", page 28
                                                    see "InspectorP652 Dynamic Focus",
                                                    page 27
                                   Lens unit           Application-specific                        see "", page 15
                                                       www.sick.com/InspectorP64x
                                                       www.sick.com/InspectorP65x
                                   Image sensor res‐ see "", page 15
                                   olution
                                   Image sensor        see "", page 15
                                   type


8019943/1PGH/2024-11 | SICK                                                        O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   49
Subject to change without notice

11 TECHNICAL DATA

                                       Type                            InspectorP64x Flex (V2D64xP-             InspectorP65x DynamicFocus
                                                                       MCxxxx)                                  (V2D65xP-MExxxx)
                                                                       InspectorP65x Flex (V2D65xP-
                                                                       MCxxxx)
                                       Image recording                 InspectorP64x Flex                       At 2 Mpx: 70 Hz
                                       rate                            At 1.7 Mpx: 40 Hz                        At 4 Mpx: 40 Hz
                                                                       InspectorP65x Flex
                                                                       At 2 Mpx: 70 Hz
                                                                       At 4 Mpx: 40 Hz
                                       Ambient light                   2000 lx on surface
                                       tolerance
                                       Image memory                    Internally 512 MB, externally on optional microSD memory card (max.
                                                                       16 GB)


11.3           Interfaces
                                       Type                            InspectorP64x Flex (V2D64xP-             InspectorP65x DynamicFocus
                                                                       MCxxxx)                                  (V2D65xP-MExxxx)
                                                                       InspectorP65x Flex (V2D65xP-
                                                                       MCxxxx)
                                       Serial                          Host (300 Bd ... 115.2 kBd), for data output
                                       RS-232/ 422
                                       Serial RS-232                   Aux (57.6 kBd)
                                       USB                             Not supported
                                       Ethernet                        Image transmission (FTP). 10/100/1,000 Mbit/s, TCP/IP, PROFINET OI,
                                                                       EtherNet/IP. MAC address(es), see type label.
                                       CAN                             20 kbit/s ... 1 Mbit/s
                                                                       Protocol: SICK CAN sensor network
                                       PROFIBUS1)                      Optional via external fieldbus module CDF600-21xx
                                       PROFINET IO                     Built-in, additionally available (optional) via external fieldbus module
                                                                       CDF600-2200
                                       Digital switching               2 x Sensor 1 and 2
                                       inputs and out‐                 4 x physical (freely configurable inputs and outputs)
                                       puts                            2 x additional external via optional CMC6001) module in connection module
                                                                       CDB650-204 or CDM420-0006 (external input/output 1 and 2)
                                       Digital switching               2 x Sensor 1 and 2
                                       inputs                          4 x physical (configurable IN 3 ... 6)
                                                                       Ue= max. 32 V, Ie= max. 5 mA, opto-decoupled, reverse polarity protected,
                                                                       adjustable debounce time
                                       Digital switching               4 x physical (configurable OUT 3 ... 6)
                                       outputs                         Ua = UV – 1.5 V, Ia ≤ 100 mA. Short-circuit protected, temperature protected.
                                                                       Not galvanically isolated from the supply voltage.
                                      1)    Function planned


11.4           Mechanics and electronics
                                       Type                            InspectorP64x Flex (V2D64xP-             InspectorP65x DynamicFocus
                                                                       MCxxxx)                                  (V2D65xP-MExxxx)
                                                                       InspectorP65x Flex (V2D65xP-
                                                                       MCxxxx)
                                       Optical indicators 10 x RGB LEDs: status indicators
                                                          1 x LED: feedback LED, green
                                                          10 x RGB LEDs: bar graph, blue



50     O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                                            8019943/1PGH/2024-11 | SICK
                                                                                                                                 Subject to change without notice

TECHNICAL DATA 11


                                    Type                  InspectorP64x Flex (V2D64xP-                    InspectorP65x DynamicFocus
                                                          MCxxxx)                                         (V2D65xP-MExxxx)
                                                          InspectorP65x Flex (V2D65xP-
                                                          MCxxxx)
                                    Acoustic indica‐      1 x beeper for signaling events, can be deactivated
                                    tors
                                    External backup       Optional on plug-in micro SD memory card or via optional CMC600 module
                                    of configuration      in connection module CDB650-204 or CDM420-0006.
                                    data
                                    Supply voltage        DC 24 V ± 20%
                                                          SELV (EN 60950-1: 2014-08) and
                                                          LPS (EN 60950-1: 2014-08) or Class 2 (UL 1310) required
                                    Current consump‐ Max. 2.0 A (with switching outputs)
                                    tion
                                    Power consump‐        Typically 20 W (with switching outputs without load)
                                    tion
                                    Weight                Max. 635 g, without optic kit                   Max. 950 g, model-dependent
                                    Material              Aluminum die cast
                                    Housing
                                    Material              Glass or plastic (PMMA), 2 mm thick, with scratch-proof coating: see "",
                                    Viewing window        page 15
                                    Electrical protec‐    III, in accordance with DIN EN 60950-1: 2014-08
                                    tion class
                                    Enclosure rating      According to EN 60529: 2000-09: see "", page 15


11.5                 Ambient data
                                    Type                  InspectorP64x Flex (V2D64xP-                    InspectorP65x DynamicFocus
                                                          MCxxxx)                                         (V2D65xP-MExxxx)
                                                          InspectorP65x Flex (V2D65xP-
                                                          MCxxxx)
                                    Vibration resist‐ According to EN 60068-2-6: 2008-02
                                    ance              In accordance with EN 60068-2-27: 2009-05
                                    Shock resistance
                                    Ambient tempera‐ Operation1): 0 °C ... +50 °C
                                    ture             Storage –20 °C ... +70 °C
                                    Permissible rela‐     0% ... 90%, non-condensing
                                    tive humidity
                                   1)   Notes regarding adequate dissipation of lost heat: see "Installation requirements", page 22




8019943/1PGH/2024-11 | SICK                                                               O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   51
Subject to change without notice

12 ACCESSORIES


12           Accessories

                                    NOTE
                                    On the product page you will find accessories and, if applicable, related installation
                                    information for your product.
                                    The call is made via the SICK Product ID: pid.sick.com/{P/N}/{S/N}
                                    {P/N} corresponds to the part number of the product, see type label.
                                    {S/N} corresponds to the serial number of the product, see type label (if indicated).




52   O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                       8019943/1PGH/2024-11 | SICK
                                                                                                          Subject to change without notice

ANNEX 13


13                   Annex
13.1                 Declarations of conformity and certificates
                                   You can download declarations of conformity and certificates via the product page.
                                   The call is made via the SICK Product ID: pid.sick.com/{P/N}/{S/N}
                                   {P/N} corresponds to the part number of the product, see type label.
                                   {S/N} corresponds to the serial number of the product, see type label (if indicated).

13.2                 Licenses
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

13.3                 Connection diagrams of connection module CDB650-204

13.3.1               Connection of the device to CDB650-204

Device = InspectorP64x = V2D64xP-xxxxAx
Device = InspectorP65x = V2D65xP-xxxxAx




8019943/1PGH/2024-11 | SICK                                                     O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   53
Subject to change without notice

13 ANNEX

                                                                                                                                         Configuration
                                                                                                                                         Diagnostics 8
                                                                           “Ethernet” (Host 2/Aux 2/Image transfer 7)                    Image display

                                      Device 4
                                                                                        CDB650-204                      “Aux 2”
                                                                                    Connection module 6                                    Computer
                                                                                                                        Ethernet
                                                                                CMC600
                                                                                                                        “Aux 1”
                                                                                          “AUX”
                                    Interfaces 5                                                                        RS-232
                                                                                                                                         Further data
 1                                                                                                                                       processing 9
                                                          “Aux 1”                                                       “Host 2”
                                                          “Host 1”                                                      Ethernet
                                                          “CAN”                                                                            HOST/PLC
                                                          “IN/OUT 3”                                                “Host 1”
 2
                                                          “IN/OUT 4”                                                RS-232/RS-422
                                                          “IN/OUT 5”
                                                          “IN/OUT 6”
                                                          “Sensor 1”
                                                                                                                                          CAN bus
                                                                                                                “IN/OUT 3”
                                                          “Sensor 2”
                                                          „VS”                                                  “IN/OUT 4”
                                                                                                                “IN/OUT 5”
 3                                                        “Sensor 1”                                            “IN/OUT 6”
                                                                                                                                                 PLC
                                                          “Sensor 2”
                                                          “External input 1”                                    “External output 1”
                                                          “External input 2”                                    “External output 2
                                                                     ß                                                   à
                                                                                                      VS á

Figure 16: Connection of the device to peripherals via CDB650-204 (overview)
1        Start/Stop trigger (e.g. photoelectric sensor)
2        Application-dependent alternative stop trigger (e.g. photoelectric sensor) or travel increment (incremental encoder)
3        Other functions
4        Device
5        Interfaces
6        Connection module
7        Image transmission
8        Configuration, diagnostics and image display
9        Further data processing
ß        External switching inputs (not supported)
à        External switching outputs (not supported)
á        Supply voltage VS



13.3.2             Wiring overview of the CDB650-204

Device = InspectorP64x = V2D64xP-xxxxAx, 1 digital input used
Device = InspectorP65x = V2D65xP-xxxxAx, 1 digital input used




54         O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                                              8019943/1PGH/2024-11 | SICK
                                                                                                                                       Subject to change without notice

ANNEX 13


 CDB650-204
                                                        Term CAN                      SGND - GND                               CMC
                             S1
                                                     S2 OFF ON                     S3 OFF ON                                              CMC600 parameter cloning module
                    F                                                                                                          NO
              2AT        OFF ON                                     RS                        Term 485                    S4                       (optional) 2
                                                     S6 422 485                    S7 OFF                   ON                 YES
     LEDs                 POWER                                                                                                                                                                                         - e.g. PLC 3
                                                                                                                                                                                                                             Result 1 4
        50 51 52 53 54                               10 11 12 13 14 15                                       16 17 18                     20 21 22 23 24                                                                     Result 2 4
                            GND                      SENS/                      SENS/
       RES/                                                                                                                               RES/                EXT.
                                                                         SGND                       SGND                           SGND
                    TR                L+
                                                                                                                                                      GND
       OUT 3                                                                                                 EXT.                         OUT 1               OUT 1                                                          GND
       RES/                                          IN 1        UIN*           IN 2        UIN*             IN 1
                                                                                                             EXT.                         RES/
                                                                                                                                          OUT 2
                                                                                                                                                              EXT.
                                                                                                                                                              OUT 2
       OUT 4            Ext. Illum.                                                                          IN 2

                                                                                                                                                                                                           Pin              RS-232




                                                                                                                                                                                       AUX interface 5
                                                                                                                                                                                                           2: RxD
                                                                                                                                                                                                           3: TxD
                                                                                                                                             30 31 32 33 34                                                5: GND       6            1
                                                                                                                                                                                                                                         6
                                                                                                                                              CAN_H   CAN_L   GND
                                                                                                                                                                                                                        9            5
                                                                                                                                                                    T+       R+

                              UIN              GND       UIN             GND       Shield          Shield        Shield        Shield
                                                                                                                                                                                                                    - Computer
                                                                                                                                             40 41 42 43 44

                                                                                                                                              CAN_H                 T‒/TxD   R‒/RxD
                              1                2             3           4          5               6            7              8
                                                                                                                                                      CAN_L
                                                                                                                                                                                       SENSOR
                                                                                                                                                              GND                        7


                                                                                                                                                                                                         12 3
                                                                                                                                                                                                  2
                                                                                                                                                                                                             13
                                                                                                                                                                                      1                         4
                                                                                                                                                                                                                5
                                                                                                                                                                                      11
                                                                                                                                                                                      10
                                                                                                                                                                                                               14
                                                                                                                                                                                                                6
                                                                                                                                                                                                                    8
                                                                                                                                                                                      16                      17
                                                                                                                                                                                             9 8           15 7


     1                                                                                                                                                                                - Device 9

      Out
       VS                                                                                                                                                                                                Host                 Host
     GND                                                                                                                                                                                                 TD‒                 TxD

                                                                                                                                                                                                         TD+

                                                                                                                                                                                                         RD‒                 RxD

                                                                                                                                                                                                         RD+
             VS à
                                                                                                                                                                                                         GND                 GND
                                                                                                                                                                                                         RS-422              RS-232
                                           F           S1
              VS - UIN -                                                - UIN*

                    =ß
Figure 17: Connection of device and peripherals to the CDB650-204 connection module (overview).


1         External trigger sensor
2         Parameter cloning module CMC600 (optional), not supported
3         E.g., PLC (programmable logic controller)
4         Name of the digital output
5         Auxiliary interface “AUX”
6         Male connector, D-Sub, 9-pin
7         SENSOR = Device
8         Female connector, M12, 17-pin, A-coded
9         Device to be connected
ß         External digital inputs and digital outputs of the device, not supported
à         Supply voltage VS




8019943/1PGH/2024-11 | SICK                                                                                                                           O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                          55
Subject to change without notice

13 ANNEX

13.3.3           Connecting supply voltage for the device in CDB650-204

                                        Device = InspectorP64x = V2D64xP-xxxxAx
                                        Device = InspectorP65x = V2D65xP-xxxxAx
                                                                         CDB650-204                                                   Cable 2                    Device 3
                                                                                                 UIN*           2                             2        VS
                                                              1          UIN                                                                                                      VS
                                        Vs 1                                                 F
                                                              2          GND
                                                                                             S1
                                                                                                               .                  .       .
                                                                     UIN*
                                                                                                               .                  .       .
                                                                               POWER                           .                  .       .

                                                               5         Shield
                                                                                             GND                1                             1        GND
                                                                                                                                                                                    GND


                                                             S1 : POWER
                                                                                                                       12 3                3 12
                                                             ON                                                    2
                                                                                                                           13
                                                                                                                              4       4
                                                                                                                                        13
                                                                                                                                                2
                                                                                                           1                                      1
                                                                                                                              5
                                                             OFF                        Shield             11                14
                                                                                                                                      5
                                                                                                                                      14          11
                                                                                                           10                 6       6           10
                                                                                                           16               17         17         16
                                                                                                                   9 8   15 7            7 15 8 9


                                                                                                                       5                   4
                                                                                    F      S1
                                                           VS - UIN -                                   - UIN*

                                        Figure 18: Connecting supply voltage for the device in CDB650-204 connection module.


                                        1           Supply voltage VS
                                        2           Connection cable 1:1 (male connector, M12, 17-pin, A-coded / female connector, M12,
                                                    17-pin, A-coded)
                                        3           Device
                                        4           Device: male connector, M12, 17-pin, A-coded
                                        5           Connection module: female connector, M12, 17-pin, A-coded


                                        Function of switch S1
                                        Table 19: Switch S1: Power
                                         Switch setting                           Function
                                         ON                                       Supply voltage UIN connected to CDB650-204 and device via fuse and
                                                                                  switch S1 as a supply voltage UIN*
                                                                                  Supply voltage UIN* can be additionally tapped at terminals 11 and 14.
                                         OFF                                      CDB650-204 and device disconnected from supply voltage
                                                                                  Recommended setting for all connection work


13.3.4           Wiring serial host interface RS-232 of the device in CDB650-204

Device = InspectorP64x = V2D64xP-xxxxAx
Device = InspectorP65x = V2D65xP-xxxxAx




56       O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                                                                       8019943/1PGH/2024-11 | SICK
                                                                                                                                                              Subject to change without notice

ANNEX 13


                                                        Cable 2
         Device 1                                                                     CDB650-204                                                      Host



                                       6                           6                             S6
            TxD                                                               T‒/TxD 43                                                             RxD
                                                                                              485       422
                                      12                           12
            RxD                                                               R‒/RxD 44                                                             TxD

                                       1                           1
            GND                                                               GND        42                                                         GND
                                                    .
                                                    .                         GND
                                                    .
                                                                              Shield     6
          RS-232                                                                                                                                    RS-232

                                     13
                                        3 12
                                             2               2
                                                                 12 3
                                                                     13
                                                                            S6 : RS    S7: Term 485
                                   4           1        1               4
                                   5                                    5   422        ON
                                   14          11       11             14
                                   6
                                    17
                                               10
                                               16
                                                        10
                                                        16            17
                                                                        6   485        OFF
                                      7 15 8 9               9 8   15 7


                                       4                      3
Figure 19: Wiring data interface RS-232 of the device in connection module CDB650-204.


1         Device
2         Connection cable 1:1 (female connector, M12, 17-pin, A-coded/male connector, M12, 17-pin, A-coded)
3         Connection module: female connector, M12, 17-pin, A-coded
4         Device: male connector, M12, 17-pin, A-coded



                                            NOTE
                                            Activate the RS-232 data interface in the device with the SICK AppStudio development
                                            environment.


13.3.5               Wiring serial host interface RS-422 of the device in CDB650-204

Device = InspectorP64x = V2D64xP-xxxxAx
Device = InspectorP65x = V2D65xP-xxxxAx




8019943/1PGH/2024-11 | SICK                                                                        O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   57
Subject to change without notice

13 ANNEX

      Device 1                                                  Cable 2                           CDB650-204                                      Host

                                     5                                    5                                      S6
          TD+                                                                              T+         33                                        RD+
                                                                                                           485    422
                                     6                                    6
          TD‒                                                                              T‒/TxD 43                                            RD‒
                                    11                                    11                                          S7
          RD+                                                                              R+         34                   OFF
                                                                                                                                                TD+
                                    12                                    12
          RD‒                                                                              R‒/RxD 44                                            TD‒
                                                                                                                        120 Ω
                                      1                                   1
          GND                                                                              GND        42                                        GND
                                                       .
                                                       .                                  GND
                                                       .
                                                                                           Shield     6
         RS-422                                                                                                                                 RS-422

                                   13
                                      3 12
                                           2                          2
                                                                          12 3
                                                                              13
                                                                                        S6 : RS     S7: Term 485
                                 4                                                 4
                                 5
                                             1                   1
                                                                                   5    422         ON
                                 14          11                  11               14
                                 6
                                  17
                                             10
                                             16
                                                                 10
                                                                 16              17
                                                                                   6    485         OFF
                                    7 15 8 9                          9 8     15 7


                                      4                                   3
Figure 20: Wiring data interface RS-422 of the device in connection module CDB650-204.


1        Device
2        Connection cable 1:1 (female connector, M12, 17-pin, A-coded / male connector, M12, 17-pin, A-coded)
3        Connection module: female connector, M12, 17-pin, A-coded
4        Device: male connector, M12, 17-pin, A-coded


                                          Function of switch S7
                                          Table 20: Switch S7: Term 485
                                           Switch setting                              Function
                                           ON                                          Terminates the RS-422 receiver in the device to improve the noise ratio
                                                                                       on the line
                                           OFF                                         No termination


                                          NOTE
                                          User of the RS-422 data interface:
                                           •       The relevant interface drivers for the device comply with the standard in accord‐
                                                   ance with RS-422.
                                           •       The connection shown above is configured for operation of the host with perma‐
                                                   nently activated drivers (often described as “RS-422 operation”).
                                           •       Activate the RS-422 data interface (“Point-to-Point” option) in the device with
                                                   SICK AppStudio.


13.3.6             Wiring the CAN interface of the device in the CDB650-204

                                          Device = InspectorP64x = V2D64xP-xxxxYx
                                          Device = InspectorP65x = V2D65xP-xxxxx
                                          Not considered: connection and looping through of the supply voltage, connection of a
                                          trigger sensor for read cycle generation (e.g. at the master)




58         O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                                                8019943/1PGH/2024-11 | SICK
                                                                                                                                         Subject to change without notice

ANNEX 13


                                                                                                                                           Ethernet
                                                                                                                                                          Ethernet (Host port) 1

                                                                                                                                                          Serial Host interface 2

                                                                       CDB650-204                                                       RS-422               Host             RS-232           Host
                                                                        Switch 3                                        R+ 34                              TD+
                                                                        S2 (TermCAN):
                                                                        ON                                          R‒/RxD 44                              TD‒                              TxD
                                                         Connection     OFF

                                                         cable ß        S6 (RS):                                        T+ 33                              RD+
                                      Device 1 4                        422
                                                         amongst        485                                         T‒/TxD 43                              RD‒                              RxD
                                      (Master) 5         others
                                                                                                                      GND 42                               GND                              GND
                                                                          CAN_H       CAN_L
                                                         CAN 7
                                                                                                GND        Shield
                                      GN = 63 6                                                                      Shield   6
                                                                         30          31        32          6


                                                        Stub 9
                                                                                                               CAN

                                      GN = 01 6
                                                                         30          31        32          6         Switch 3
                                                         Connection                                                  S2 (TermCAN):
                                                                                                                     ON
                                                         cable ß         40          41        42          7         OFF
                                      Device 2 4
                                                         amongst

                                                                      CAN_H       CAN_L               Shield
                                       (Slave) 8         others                                                      CDB650-
                                                         CAN 7                                GND                    204
                                                                                                                                                      Alternative connection module â:

                                                                                                               CAN

                                      GN = 02 6
                                                                         30          31        32          6         Switch 3                         21       22    23       6     Switch 3
                                                                                                                     S2 (TermCAN):                                                  S4 (TermCAN):
                                                         Connection                                                  ON                                                             ON
                                                         cable ß         40          41        42          7         OFF                              31       32    33       7     OFF
                                      Device 3 4
                                                         amongst

                                                                      CAN_H       CAN_L               Shield                                      CAN_H     CAN_L         Shield
                                       (Slave) 8         others                                                      CDB650-                                                        CDM420-
                                                         CAN 7                                GND                    204                                            GND             0006


                                                                                                               CAN

                                      GN = 03 6
                                                                         30          31        32          6         Switch 3
                                                         Connection                                                  S2 (TermCAN):
                                                         cable ß                                                     ON

                                                                          CAN_H       CAN_L                Shield
                                      Device 4 4
                                                                                                GND
                                                                                                                     OFF

                                                         amongst
                                       (Slave) 8         others                                                      CDB650-
                                                         CAN 7                                                       204


                                   GN = Device number à
                                   (max. 32 participants) á

                                   Figure 21: Wire the CAN interface of the device in the CDB650-204 connection module.




8019943/1PGH/2024-11 | SICK                                                                                          O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                    59
Subject to change without notice

13 ANNEX


                                          1           Ethernet (host port)
                                          2           Serial host interface
                                          3           Switch
                                          4           Device
                                          5           Master
                                          6           Device number
                                          7           CAN etc.
                                          8           Slave
                                          9           Branch line
                                          ß           Connection cable 1:1 (female connector, M12, 17-pin, A-coded/male connector, M12,
                                                      17-pin, A-coded)
                                          à           Device number (GN)
                                          á           Maximum 32 users
                                          â           Example of alternative connection module CDM420-0006
                                                      An adapter cable (female connector, M12, 17-pin, A-coded / male connector, D-Sub-HD,
                                                      15-pin) is required to connect the device.



                                          NOTE
                                          Activate the CAN data interface in the device with the SICK AppStudio development
                                          environment.
                                          Activate further settings in the device corresponding to the function of the device in the
                                          system configuration.


13.3.7             Wiring digital inputs of the device in the CDB650-204

Device = InspectorP64x = V2D64xP-xxxxAx
Device = InspectorP65x = V2D65xP-xxxxAx
Trigger sensor 1                             CDB650-204                                              Cable 2                         Device 3
                                                                                    2                     2           VS
 9 VS                                   11 UIN*                 UIN*                                                                        VS
                                                                                    C                     C           Sensor D
                                         A    SENS/IN B
              Out                                                                                .                               6.64 K
                                                                                                 .                     Vin 4
                                                                                                                                 3.32 K
                                                         Shield                                  .
                                                                                    9                     9           SensGND
     GND                                12 SGND
                                                              S3
                                         6      Shield                                                                                    SensGND
                                                                                    1                     1           GND
                                                                                                                                  GND
PNP sensor 8                                             GND

E.g. photo-electric                     S3 : SGND-GND                               12 3                  3 12
                                                                                2                              2
                                        ON                                              13             13
switch 7                                                                   1                 4
                                                                                             5
                                                                                                     4
                                                                                                     5
                                                                                                                 1

                                        OFF                                11
                                                                           10
                                                                                            14
                                                                                             6
                                                                                                     14
                                                                                                     6
                                                                                                                 11
                                                                                                                 10
                                                                           16              17         17         16
                                                                                9 8     15 7            7 15 8 9


                                                                                    6                     5
Figure 22: Trigger sensor supplied with power by connection module CDB650-204.




60         O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                                                        8019943/1PGH/2024-11 | SICK
                                                                                                                                                 Subject to change without notice

ANNEX 13


1         Trigger sensor
2         Connection cable 1:1 (female connector, M12, 17-pin, A-coded/male connector, M12, 17-pin, A-coded)
3         Device
4         Input voltage Vin
5         Device: male connector, M12, 17-pin, A-coded
6         Connection module: female connector, M12, 17-pin, A-coded
7         E.g. photoelectric sensor
8         PNP sensor
9         Supply voltage VS


                               2
Trigger sensor 1            VS ext       CDB650-204                                                                    CDB650-204

                                     11 UIN*           UIN*                                                        11 UIN*                UIN*
  4 VS
                                                                                 1
                                     A    SENS/IN B                                                                A     SENS/IN B
                 Out

                                                   Shield                                                                           Shield
    GND                              12 SGND                                                                       12 SGND
                                                       S3                              2                                                 S3
                                     6        Shield                             2   VS ext                         6 Shield

PNP sensor 3                                       GND                                                                              GND
                                     S3 : SGND-GND                                                A                S3 : SGND-GND
                                     ON                                                                            ON
                                     OFF                                   GND                   12                OFF

Figure 23: Left: Trigger sensor connected potential-free and supplied with power externally. Right: Alternatively switch, !
supplied with power by connection module CDB650-204 or " connected potential-free and supplied with power externally.
Now select switch setting S3 as shown in the left figure.


1         Trigger sensor, e.g., for read cycle generation
2         External supply voltage VS ext
3         PNP sensor
4         Supply voltage VS

                                      Table 21: Assignment of placeholders to the digital inputs
                                         CDB650-204                                                                                  Device
                                         Terminal A            Signal B                        Pin C                                 Sensor D
                                         10                    SENS/IN 1                       10                                    1
                                         13                    SENS/IN 2                       15                                    2

                                      Function of switch S3
                                      Table 22: Switch S3: SGND-GND
                                         Switch setting        Function
                                         ON                    GND of the trigger sensor is connected with GND of CDB650-204 and
                                                               GND of the device
                                         OFF                   Trigger sensor is connected volt-free at CDB650-204 and the device.
                                                               Common, isolated reference potential of all digital inputs is SGND.

                                      Characteristic data of the digital inputs
                                      Table 23: Characteristic data of the digital inputs “Sensor 1” and “Sensor 2”
                                         Type                  Switching

8019943/1PGH/2024-11 | SICK                                                                   O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   61
Subject to change without notice

13 ANNEX

                                           Switching behavior                        Power to the input starts the assigned function, e.g. start analysis.
                                                                                     Default setting in the device: logic not inverted (active high), debounce
                                                                                     time 10 ms
                                           Properties                                • Opto-decoupled, reverse polarity protected
                                                                                     • Can be wired with PNP output of a trigger sensor
                                           Electrical values                         Low: Vin 1) ≤ 2 V; Iin 2) ≤ 0.3 mA
                                                                                     High: 6 V ≤ Vin ≤ 30 V; 0.7 mA ≤ Iin ≤ 5 mA
                                          1)    Input voltage.
                                          2)    Input current.

                                          NOTE
                                          Assign the functions for the digital inputs in the device using SICK AppStudio.


13.3.8             Wiring digital outputs of the device in the CDB650-204

Device = InspectorP64x = V2D64xP-xxxxAx
Device = InspectorP65x = V2D65xP-xxxxAx
These digital outputs can be parameterized independently as IN and OUT. Default: IN
                                Device 1                                                      Cable 3                 CDB650-204                   Load (e.g. PLC) 4

                                                                           2                          2
                                          2 VS                                                                       UIN*

                                                                                         .                                  Shield      5
                                                                                         .
                                                                                         .
                                                    Result A               B                          B
                                                                                                                            RES/OUT C   D
                                                                                                                                                             Vout 5
                                                    GND                    1                          1
                       Filter                                                                                               GND         22
                                                                                                                      GND

                                                                         3 12                         2
                                                                                                          12 3
                                                                              2
                                                                      13                                      13
                                                                    4           1                1               4
                                                                    5
                                                                    14          11               11
                                                                                                                 5
                                                                                                                14
                                                                                                                                               For inductive load: 6
                                                                    6           10               10              6
                                                                     17         16               16            17
                                                                       7 15 8 9                       9 8   15 7


                                                                           8                              7

Figure 24: Wire the digital output in the CDB650-204 connection module.


1        Device
2        Supply voltage VS
3        Connection cable 1:1 (female connector, M12, 17-pin, A-coded/male connector, M12, 17-pin, A-coded)
4        Load (e.g. PLC)
5        Output voltage Vout
6        With inductive load: see note
7        Connection module: female connector, M12, 17-pin, A-coded
8        Device: male connector, M12, 17-pin, A-coded




62         O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                                                     8019943/1PGH/2024-11 | SICK
                                                                                                                                              Subject to change without notice

ANNEX 13


                                   Inductive load

                                   NOTE
                                   Provide an arc-suppression switch at the digital output if inductive load is present.
                                   ►       Attach a freewheeling diode directly to the load for this purpose.

                                   Table 24: Assignment of placeholders to the digital outputs
                                    Device                                             CDB650-204
                                    Output A                 Pin B                     Signal C                              Terminal D
                                    IN/OUT 3                 13                        RES/OUT 1                             20
                                    IN/OUT 4                 14                        RES/OUT 2                             21
                                    IN/OUT 5                 16                        RES/OUT 3                             50
                                    IN/OUT 6                 17                        RES/OUT 4                             51

                                   Characteristic data of the digital outputs
                                   Table 25: Characteristic data of the digital switching outputs
                                    Type                     Switching
                                    Switching behavior       PNP switching to supply voltage VS
                                                             Default settings in the device: no function, logic: not inverted (active
                                                             high)
                                    Properties               • Short-circuit protected and temperature protected
                                                             • Not electrically isolated from VS
                                    Electrical values        0 V ≤ Vout 1) ≤ VS
                                                             (VS −1.5 V) ≤ Vout ≤ VS at Iout 2) ≤ 100 mA
                                   1)   Output voltage.
                                   2)   Output current.


                                   NOTE
                                   Assign the functions for the digital outputs in the device using SICK AppStudio.


13.3.9               Wiring a digital switching input in configurable switching inputs
                                   Characteristic data for digital IN/OUT used as a switching input (IN)
                                   V2D65x
                                   •       Low: Ue ≤ 5 V; Ie ≤ 0.3 mA
                                   •       High: 12 V ≤ Ue ≤ UV ; Ie ≤ 1 mA
                                   For the purpose of electromagnetic compatibility, inputs must be set to a defined
                                   low-impedance level!

13.4                 Connection diagrams of connection module CDM420-0006

13.4.1               Connection of the device to CDM420-0006

Device = InspectorP64x = V2D64xP-xxxxAx
Device = InspectorP65x = V2D65xP-xxxxAx




8019943/1PGH/2024-11 | SICK                                                           O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   63
Subject to change without notice

13 ANNEX

                                                                                                                                         Configuration
                                                                                                                                         Diagnostics 8
                                                                           “Ethernet” (Host 2/Aux 2/Image transfer 7)                    Image display

                                      Device 4
                                                                                        CDB650-204                      “Aux 2”
                                                                                    Connection module 6                                    Computer
                                                                                                                        Ethernet
                                                                                CMC600
                                                                                                                        “Aux 1”
                                                                                          “AUX”
                                    Interfaces 5                                                                        RS-232
                                                                                                                                         Further data
 1                                                                                                                                       processing 9
                                                          “Aux 1”                                                       “Host 2”
                                                          “Host 1”                                                      Ethernet
                                                          “CAN”                                                                            HOST/PLC
                                                          “IN/OUT 3”                                                “Host 1”
 2
                                                          “IN/OUT 4”                                                RS-232/RS-422
                                                          “IN/OUT 5”
                                                          “IN/OUT 6”
                                                          “Sensor 1”
                                                                                                                                          CAN bus
                                                                                                                “IN/OUT 3”
                                                          “Sensor 2”
                                                          „VS”                                                  “IN/OUT 4”
                                                                                                                “IN/OUT 5”
 3                                                        “Sensor 1”                                            “IN/OUT 6”
                                                                                                                                                 PLC
                                                          “Sensor 2”
                                                          “External input 1”                                    “External output 1”
                                                          “External input 2”                                    “External output 2
                                                                     ß                                                   à
                                                                                                      VS á

Figure 25: Connection of the device to peripherals via CDM420-0006 (overview)
1        Start/Stop trigger (e.g. photoelectric sensor)
2        Application-dependent alternative stop trigger (e.g. photoelectric sensor) or travel increment (incremental encoder)
3        Other functions
4        Device
5        Interfaces
6        Connection module
7        Image transmission
8        Configuration, diagnostics and image display
9        Further data processing
ß        External switching inputs (not supported)
à        External switching outputs (not supported)
á        Supply voltage VS



13.4.2             Wiring overview of the CDM420-0006

Device = InspectorP64x = V2D64xP-xxxxAx
Device = InspectorP65x = V2D65xP-xxxxAx




64         O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                                              8019943/1PGH/2024-11 | SICK
                                                                                                                                       Subject to change without notice

ANNEX 13


                                                                                                                                                                                                                          CDM420-0006

                              POWER           Sensor 1            Sensor 2            Result 1       Result 2
                                                                                                                S2                    S3                      S4                                 S6



                                                                                                                                                                                                             SGND - GND
                                                                                                                ON                    ON                     ON                                  ON

                                                                                                                           RS485              Term422                TermCAN
       LEDs
                                                                                                                OFF                   OFF                  OFF                                   OFF
                                        S8


                         No CMC ->
                                       ON
                                                                        CMC600 parameter cloning module
                                      OFF                                        (optional) 3
                                                                                                                                                                                      Pin                                                        RS-232
                                                                                                                                                                                      2: RxD                                                      1       5
                                                                                                                                                                                      3: TxD
                                                                                        S1                                                                                            5: GND
                                                                                                                                        AUX interface 4                                                                                                           5
                                                                                      ON                                                                                                                                                          6      9

                                                                    POWER                                                                                                                                                                       - Computer

                                                                                                                internal   internal         Result 1    Result 2                      Aux In 1    Aux In 2
                                                                                      OFF
                                                                                                                                      GND                          GND         SGND                                  SGND
                                                                  F                                             11 12 13 14 15                                     16 17 18 19                                    20
                                                            2AT                                                                                                                                                                                       Result 1 6
                                                                                                                                                                                                                                                  Result 2 6
                                                                                                                                                                                                                                                  GND
                                     1                   2                    3                   4
                                                                                                                                                                                                                                               - e.g. PLC 7


                                     +24 V               GND                 +24 V                GND           CAN_H      CAN_L      GND                          GND         SGND   Sensor 2    +24 V*             Aux Out 2
                                                                                                                                            T+          R+
                                                                                                                21 22 23 24 25                                     26 27 28 29                                    30


                                     5                   6                    7                   8                                                                                                                                            10 5      1    6

                                                                                                                                                                                                                                 SCANNER

                                                                                                                                                                                      Sensor 1                       Aux Out 1
                                                                                                                                                                                                                                                                  9
                                     Shield              Shield              Shield              Shield         CAN_H      CAN_L            T‒/TxD      R‒/RxD                                    +24 V*
                                                                                                                                                                                                                                    8
                                                                                                                                      GND                          GND         SGND
                                                                                                                                                                                                                                                 15     11
                                                                                                                31 32 33 34 35                                     36 37 38 39                                    40
                                                                                                                                                                                                                                               - Device ß



                                                                                                                                                                                                                                       Host             Host
        VS                                                                                                                                                                                                                             TD‒             TxD
        2
                                                                                                                                                                                                                                       TD+

                                                                                                                                                                                                                                       RD‒             RxD

                                                                                                                                                                                                                                       RD+

     1                                                                                                                                                                                                                                 GND             GND
                                                                                                                                                                                                                                      RS-422           RS-232
      Out
       VS
     GND


                                               F                    S1
       VS - +24 V -                                                                              - +24 V*

             =à
Figure 26: Connection of device and peripherals to the CDM420-0006 connection module (overview).




8019943/1PGH/2024-11 | SICK                                                                                                                                                             O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x              65
Subject to change without notice

13 ANNEX


1        External trigger sensor
2        Supply voltage VS
3        Parameter cloning module CMC600 (optional), not supported
4        Auxiliary interface “AUX”
5        Male connector, D-Sub, 9-pin
6        Name of the digital output or digital input of the device (function selectable in the device)
7        E.g., PLC (programmable logic controller)
8        SCANNER = Device
9        Female connector, D-Sub-HD, 15-pin
ß        Device to be connected
à        External digital inputs and digital outputs (not supported)



13.4.3             Connecting supply voltage for the device in CDM420-0006

Device = InspectorP64x = V2D64xP-xxxxAx
Device = InspectorP65x = V2D65xP-xxxxAx
                            CDM420-0006                                                       Cable 2                 Device 3
                                                     +24 V*            1                               2        VS
                     1       +24 V                                                                                               VS
Vs 1                                                 F
                     2       GND
                                                     S1
                                                                      .                  .         .
                          +24 V*
                                                                      .                  .         .
                                   POWER                              .                  .         .

                      5      Shield
                                                         GND           5                               1        GND
                                                                                                                                 GND


                    S1 : POWER                                                                      3 12
                                                                                                         2
                    ON                                               10 5      1    6          4
                                                                                               5
                                                                                                 13
                                                                                                           1
                                                                                                           11
                    OFF                        Shield                                          14
                                                                                               6           10
                                                                                                           16
                                                                                                17
                                                                          15   11                 7 15 8 9



                                                                           5                           4
                                                 F        S1
                  VS - +24 V -                                      - +24 V*

Figure 27: Connecting supply voltage for the device in CDM420-0006 connection module.


1        Supply voltage VS
2        Adapter cable (male connector, D-Sub-HD, 15-pin / female connector, M12, 17-pin, A-coded)
3        Device
4        Device: male connector, M12, 17-pin, A-coded
5        Connection module: female connector, D-Sub-HD, 15-pin


                                          Function of switch S1
                                          Table 26: Switch S1: Power
                                           Switch setting                               Function
                                           ON                                           Supply voltage +24 V connected to CDM420-0006 and device via fuse
                                                                                        as +24 V* supply voltage
                                                                                        Supply voltage +24 V* can be additionally tapped at terminals 29 and
                                                                                        39



66         O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                                               8019943/1PGH/2024-11 | SICK
                                                                                                                                        Subject to change without notice

ANNEX 13


                                             Switch setting                   Function
                                             OFF                              CDM420-0006 and device disconnected from supply voltage
                                                                              Recommended setting for all connection work


13.4.4               Wiring serial host interface RS-232 of the device in the CDM420-0006

Device = InspectorP64x = V2D64xP-xxxxAx
Device = InspectorP65x = V2D65xP-xxxxAx
                                   2
         Device 1                                                                        CDM420-0006                                                      Host



                                       6                        9                                      S2
            TxD                                                                   T‒/TxD 34                                                             RxD
                                                                                                  ON        OFF
                                      12                        7
            RxD                                                                   R‒/RxD 35                                                             TxD

                                       1                        5
            GND                                                                   GND        36                                                         GND
                                                    .
                                                    .                            GND
                                                    .
                                                                                  Shield     6
          RS-232                                                                                                                                        RS-232

                                     13
                                        3 12
                                             2
                                                              10 5   1    6
                                                                               S2 : RS 485   S3: Term 422
                                   4
                                   5
                                               1
                                                                               ON            ON
                                   14          11
                                   6
                                    17
                                               10
                                               16               15   11
                                                                               OFF           OFF
                                      7 15 8 9


                                        4                        3
Figure 28: Wiring data interface RS-232 of the device in connection module CDM420-0006.


1         Device
2         Adapter cable (male connector, D-Sub-HD, 15-pin / female connector, M12, 17-pin, A-coded)
3         Connection module: female connector, D-Sub-HD, 15-pin
4         Device: male connector, M12, 17-pin, A-coded



                                            NOTE
                                            Activate the RS-232 data interface in the device with the SICK AppStudio development
                                            environment.


13.4.5               Wiring serial host interface RS-422 of the device in the CDM420-0006

Device = InspectorP64x = V2D64xP-xxxxAx
Device = InspectorP65x = V2D65xP-xxxxAx




8019943/1PGH/2024-11 | SICK                                                                            O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   67
Subject to change without notice

13 ANNEX

                                  2
      Device 1                                                                                  CDM420-0006                                      Host

                                       5                               8                                      S2
           TD+                                                                            T+         24                                        RD+
                                                                                                               OFF
                                       6                               9
           TD‒                                                                            T‒/TxD 34                                            RD‒
                                      11                               6                                             S3
           RD+                                                                            R+         25                   OFF
                                                                                                                                               TD+
                                      12                               7
           RD‒                                                                            R‒/RxD 35                                            TD‒
                                                                                                                     120 Ω
                                       1                               5
           GND                                                                            GND        36                                        GND
                                                        .
                                                        .                                GND
                                                        .
                                                                                          Shield      6
         RS-422                                                                                                                                RS-422

                                       3 12
                                    13
                                            2
                                                                     10 5   1    6
                                                                                       S2 : RS 485        S3: Term 422
                                  4           1
                                  5
                                              11
                                                                                       ON                 ON
                                  14
                                              10
                                  6
                                   17         16                       15   11         OFF                OFF
                                     7 15 8 9


                                       4                                   3
Figure 29: Wiring data interface RS-422 of the device in connection module CDM420-0006.


1        Device
2        Adapter cable (male connector, D-Sub-HD, 15-pin / female connector, M12, 17-pin, A-coded)
3        Connection module: female connector, D-Sub-HD, 15-pin
4        Device: male connector, M12, 17-pin, A-coded


                                           Function of switch S3
                                           Table 27: Switch S3: Term 422
                                           Switch setting                            Function
                                           ON                                        Terminates the RS-422 receiver in the device to improve the noise ratio
                                                                                     on the line
                                           OFF                                       No termination


                                           NOTE
                                           Activate the RS-422 data interface (“Point-to-Point” option) in the device with the
                                           SICK AppStudio development environment.

                                           The requirements and restrictions apply when using the RS-422 data interface:
                                           • The relevant interface drivers for the device comply with the standard in accord‐
                                                ance with RS-422.
                                           • The connection shown above is configured for operation of the host with perma‐
                                                nently activated drivers (often described as “RS-422 operation”).

13.4.6             Wiring the CAN interface of the device in the CDM420-0006

Device = InspectorP64x = V2D64xP-xxxxAx
Device = InspectorP65x = V2D65xP-xxxxAx
Not considered: connection and looping through of the supply voltage, connection of a trigger sensor for read cycle
generation (e.g. at the master)




68         O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                                              8019943/1PGH/2024-11 | SICK
                                                                                                                                       Subject to change without notice

ANNEX 13


                                                                                                                     Ethernet
                                                                                                                                     Ethernet (Host port) 1

                                                                                                                                     Serial Host interface 2
                                                                                                                 RS-422
                                                 CDM420-0006                                                                            Host               RS-232               Host
                                                 Switch 3                                          R+ 25                              TD+
                                                 S4 (TermCAN):
                                                 ON                                            R‒/RxD 35                              TD‒                                  TxD
                                   Connection    OFF
                                   cable ß       S2 (RS485):                                       T+ 24                              RD+
      Device 1 4                                 ON
                                   amongst       OFF                                           T‒/TxD 34                              RD‒                                  RxD
      (Master) 5                   others
                                   CAN 1 7                                                       GND 26                               GND                                  GND
                                                    CAN_H       CAN_L     GND        Shield
      GN = 63 6                                                                                 Shield   7
                                                   21          22        23          6



                                   Stub 9                                                CAN

      GN = 01 6
                                                   21          22        23          6          Switch 3
                                   Connection                                                   S4 (TermCAN):
                                                                                                ON
                                   cable ß         31          32        33          7
      Device 2 4                                                                                OFF

                                   amongst

                                                CAN_H       CAN_L               Shield
       (Slave) 8                   others
                                   CAN 1 7                              GND                   CDM420-0006
                                                                                                                                Alternative connection module â:

                                                                                         CAN

      GN = 02 6
                                                   21          22        23          6          Switch 3                        30        31    32         6     Switch 3
                                   Connection                                                   S4 (TermCAN):                                                    S2 (TermCAN):
                                                                                                ON                                                               ON
                                   cable ß         31          32        33          7                                          40        41    42         7
                                                                                                OFF                                                              OFF
      Device 3 4
                                   amongst
                                                CAN_H       CAN_L               Shield                                       CAN_H     CAN_L           Shield
       (Slave) 8                   others                                                                                                                          CDB650-
                                   CAN 1 7                              GND                   CDM420-0006                                      GND                 204


                                                                                         CAN

      GN = 03 6
                                                   21          22        23          6          Switch 3
                                   Connection                                                   S4 (TermCAN):
                                   cable ß                                                      ON

                                                    CAN_H       CAN_L                Shield
      Device 4 4
                                                                          GND
                                                                                                OFF
                                   amongst
       (Slave) 8                   others
                                   CAN 1 7                                                    CDM420-0006

GN = Device number à
(max. 32 participants) á
Figure 30: Wire the CAN interface of the device in the CDM420-0006 connection module.




8019943/1PGH/2024-11 | SICK                                                                                     O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x          69
Subject to change without notice

13 ANNEX


1          Ethernet (host port)
2          Serial host interface
3          Switch
4          Device
5          Master
6          Device number
7          CAN etc.
8          Slave
9          Branch line
ß          Adapter cable (female connector, M12, 17-pin, A-coded/male connector, D-Sub-HD, 15-pin)
à          Device number (GN)
á          Maximum 32 users
â          Example of alternative connection module:
           CDB650-204
           A connection cable 1:1 (female connector, M12, 17-pin, A-coded / male connector, M12, 17-pin, A-coded) is required to
           connect the device.



                                            NOTE
                                            Activate the CAN data interface in the device with the SICK AppStudio development
                                            environment.
                                            Activate further settings in the device corresponding to the function of the device in the
                                            system configuration.


13.4.7               Wiring digital inputs of the device in the CDM420-0006

Device = InspectorP64x = V2D64xP-xxxxAx
Device = InspectorP65x = V2D65xP-xxxxAx
                                                                                                                Cable 2
Trigger sensor 1                             CDM420-0006                                                                             Device 4
                                                                                    1                     2           VS
                                                                +24V*                                                                       VS
 9 VS                                    39 +24 V*
                                                                                    C                     D           Sensor E
                                           A Sensor B
                Out                                                                              .                               6.64 K
                                                                                                 .                     Vin 3
                                                                                                                                 3.32 K
                                                           Shield                                .
                                                                               15                         9           SensGND
     GND                                 37 SGND
                                                                S6
                                          6 Shield                                                                                        SensGND
                                                                                5                         1           GND
                                                                                                                                  GND
PNP sensor 8                                               GND
                                          S6 : SGND-GND
E.g. photo-electric                                                          10 5       1    6            3 12
                                                                                                               2
                                          ON                                                         4
                                                                                                       13
                                                                                                                 1
switch 7                                                                                             5
                                                                                                     14          11
                                          OFF                                  15       11
                                                                                                     6
                                                                                                      17
                                                                                                                 10
                                                                                                                 16
                                                                                                        7 15 8 9



                                                                                6                        5
Figure 31: Trigger sensor supplied with power by connection module CDM420-0006.




70           O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                                                      8019943/1PGH/2024-11 | SICK
                                                                                                                                                 Subject to change without notice

ANNEX 13


1         Trigger sensor
2         Adapter cable (male connector, D-Sub-HD, 15-pin / female connector, M12, 17-pin, A-coded)
3         Input voltage Vin
4         Device
5         Device: male connector, M12, 17-pin, A-coded
6         Connection module: female connector, M12, 17-pin, A-coded
7         E.g. photoelectric sensor
8         PNP sensor
9         Supply voltage VS



Trigger sensor 1                2
                            VS ext    CDM420-0006                                                                     CDM420-0006

                                                    +24V*                                                          39 +24 V*             +24V*
  3 VS                               39 +24 V*
                                                                                  1
                                     A Sensor B                                                                     A Sensor B
                 Out

                                                 Shield                                                                             Shield

    GND                              37 SGND                                                                       37 SGND

                                                     S6                           2     2                                                S6
                                                                                      VS ext                        6 Shield
                                     6 Shield
                                                                                                                                     GND
 PNP sensor 4                                    GND
                                                                                                   A               S6 : SGND-GND
                                     S6 : SGND-GND
                                     ON                                                                            ON
                                                                            GND                   37
                                     OFF                                                                           OFF

Figure 32: Left: Trigger sensor connected potential-free and supplied with power externally. Right: alternative switch, !
supplied with power by connection module CDM420-0006 or " connected volt-free and supplied with power externally. Now
select switch setting S6 as shown in the left figure.


1         Trigger sensor, e.g. for read cycle generation
2         External supply voltage VS ext
3         Supply voltage VS
4         PNP sensor

                                      Table 28: Assignment of placeholders to the digital inputs
                                       CDM420-0006                                                             Device
                                       Terminal A           Signal B          Pin C                            Pin D                          Sensor E
                                       38                   Sensor 1          14                               10                             1
                                       28                   Sensor 2          4                                15                             2

                                      Function of switch S6
                                      Table 29: Switch S6: SGND - GND
                                       Switch setting           Function
                                       ON                       GND of the trigger sensor is connected with GND of CDM420-0006 and
                                                                GND of the device
                                       OFF                      Trigger sensor is connected volt-free at CDM420-0006 and the device.
                                                                Common, isolated reference potential of all digital inputs is SGND.

                                      Characteristic data of the digital inputs
                                      Table 30: Characteristic data of the digital inputs “Sensor 1” and “Sensor 2”
                                       Type                     Switching


8019943/1PGH/2024-11 | SICK                                                                    O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   71
Subject to change without notice

13 ANNEX

                                           Switching behavior                         Power to the input starts the assigned function, e.g. start analysis.
                                                                                      Default setting in the device: logic not inverted (active high), debounce
                                                                                      time 10 ms
                                           Properties                                 • Opto-decoupled, reverse polarity protected
                                                                                      • Can be wired with PNP output of a trigger sensor
                                           Electrical values                          Low: Vin1) ≤ 2 V; Iin2) ≤ 0.3 mA
                                                                                      High: 6 V ≤ Vin ≤ 30 V; 0.7 mA ≤ Iin ≤ 5 mA
                                          1)    Input Voltage
                                          2)    Input current

                                          NOTE
                                          Assign the functions for the digital inputs in the device using SICK AppStudio.


13.4.8             Wiring digital outputs of the device in the CDM420-0006

Device = InspectorP64x = V2D64xP-xxxxAx
Device = InspectorP65x = V2D65xP-xxxxAx
                                Device 1                                                       Cable 3            CDM420-0006                  Load (e.g. PLC) 4

                                                                       2                            1
                                          2 VS                                                                    +24 V* (VS)

                                                                                          .                            Shield   5
                                                                                          .
                                                                                          .
                                                   Result A            B                            C
                                                                                                                      RES/OUT E
                                                                                                                                                         Vout 5
                                                   GND                 1                            5
                       Filter                                                                                          GND      13
                                                                                                                   GND
                                                                          3 12
                                                                               2
                                                                       13                         10 5   1    6
                                                                     4
                                                                                                                                           For inductive load: 6
                                                                                 1
                                                                     5
                                                                     14          11
                                                                     6           10
                                                                      17         16
                                                                                                    15   11
                                                                        7 15 8 9



                                                                           8                             7


Figure 33: Wire the digital output in the CDM420-0006 connection module.


1        Device
2        Supply voltage VS
3        Adapter cable (female connector, M12, 17-pin, A-coded/male connector, D-Sub-HD, 15-pin)
4        Load (e.g. PLC)
5        Output voltage Vout
6        With inductive load: see note
7        Connection module: female connector, D-Sub-HD, 15-pin
8        Device: male connector, M12, 17-pin, A-coded

NOTE
Digital outputs are omitted due to the 15-pin adapter cable.

Not available in CDM420-0006:
• IN/OUT 5
• IN/OUT 6



72         O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x                                                                 8019943/1PGH/2024-11 | SICK
                                                                                                                                          Subject to change without notice

ANNEX 13


                                   Inductive load

                                   NOTE
                                   Provide an arc-suppression switch at the digital output if inductive load is present.
                                   ►       Attach a freewheeling diode directly to the load for this purpose.

                                   Table 31: Assignment of placeholders to the digital outputs
                                    Device                                      CDM420-0006
                                    Output A              Pin B                 Pin C                    Signal D                      Terminal E
                                    IN/OUT 3              13                    12                       Result 1                      14
                                    IN/OUT 4              14                    13                       Result 2                      15

                                   Characteristic data of the digital outputs
                                   Table 32: Characteristic data of the and digital outputs
                                    Type                       Switching
                                    Switching behavior         PNP switching to supply voltage VS
                                                               Default settings in the device: no function, logic: not inverted (active
                                                               high)
                                    Properties                    • Short-circuit protected and temperature protected
                                                                  • Not electrically isolated from the supply voltage VS
                                    Electrical values          0 V ≤ Vout1) ≤ VS
                                                               (VS −1.5 V) ≤ Vout ≤ VS at Iout2) ≤ 100 mA
                                   1)   Output voltage.
                                   2)   Output current.

                                   NOTE
                                   Assign the functions for the digital outputs in the device using SICK AppStudio.


13.4.9               Wiring a digital switching input in configurable switching inputs
                                   Characteristic data for digital IN/OUT used as a switching input (IN)
                                   V2D65x
                                   •       Low: Ue ≤ 5 V; Ie ≤ 0.3 mA
                                   •       High: 12 V ≤ Ue ≤ UV ; Ie ≤ 1 mA
                                   For the purpose of electromagnetic compatibility, inputs must be set to a defined
                                   low-impedance level!




8019943/1PGH/2024-11 | SICK                                                              O P E R A T I N G I N S T R U C T I O N S | InspectorP64x/65x   73
Subject to change without notice

8019943/1PGH/2024-11/en
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