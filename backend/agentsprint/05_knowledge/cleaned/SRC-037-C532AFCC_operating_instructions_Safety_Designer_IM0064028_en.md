OPERATING INSTRUCTIONS


Safety Designer
Configuration software

Described product
                                    Safety Designer

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




2   O P E R A T I N G I N S T R U C T I O N S | Safety Designer                                       8018180/1U78/2025-10-16 | SICK
                                                                                                         Subject to change without notice

CONTENTS


Contents
                                   1   About this document........................................................................                                 5
                                       1.1      Scope.........................................................................................................     5
                                       1.2      Target groups............................................................................................           5
                                       1.3      Further information...................................................................................              5
                                       1.4      Symbols and document conventions......................................................                              5

                                   2   Safety information............................................................................                              6
                                       2.1      General safety notes................................................................................               6
                                       2.2      Intended use.............................................................................................          6
                                       2.3      Requirements for the qualification of personnel....................................                                6
                                       2.4      Cybersecurity............................................................................................          6

                                   3   Product description...........................................................................                              8
                                       3.1      Product characteristics............................................................................                8
                                       3.2      Structure and function.............................................................................                8

                                   4   Installation..........................................................................................                      9
                                       4.1      Licenses....................................................................................................        9
                                                4.1.1      Activating the license...............................................................                    9
                                                4.1.2      Show license overview.............................................................                       9
                                       4.2      Installing Safety Designer........................................................................                 10
                                       4.3      Unsupervised installation.........................................................................                 10

                                   5   Operation............................................................................................ 11
                                       5.1      Start...........................................................................................................   11
                                       5.2      User interface...........................................................................................          12
                                                5.2.1         Menu and toolbar....................................................................                 12
                                                5.2.2         Navigation................................................................................           13
                                                5.2.3         Working area............................................................................             14
                                                5.2.4         Task list.....................................................................................       14
                                                5.2.5         Notes........................................................................................        14
                                                5.2.6         Adjust user interface...............................................................                 15
                                                5.2.7         Options.....................................................................................         17
                                                5.2.8         Create diagnosis dump............................................................                    17
                                       5.3      Projects......................................................................................................     17
                                                5.3.1         Protecting projects with a password.......................................                           18
                                       5.4      Settings.....................................................................................................      18
                                                5.4.1         Entering project information...................................................                      18
                                                5.4.2         Network settings......................................................................               19
                                                5.4.3         Connections via router (NAT)..................................................                       20
                                                5.4.4         Activating time synchronization..............................................                        21
                                                5.4.5         Configuring the data recorder.................................................                       22
                                       5.5      Configuration.............................................................................................         22
                                                5.5.1         Device management................................................................                    23


8018180/1U78/2025-10-16 | SICK                                                                      O P E R A T I N G I N S T R U C T I O N S | Safety Designer     3
Subject to change without notice

CONTENTS


                                                             5.5.2       Device overview.......................................................................               24
                                                             5.5.3       Connecting to connected devices...........................................                           27
                                                             5.5.4       Assigning device tiles to physically present devices.............                                    28
                                                             5.5.5       Import configuration................................................................                 29
                                                             5.5.6       Open the device window – configure devices........................                                   30
                                                             5.5.7       Logging into or out of a device................................................                      30
                                                             5.5.8       Transfer configuration.............................................................                  31
                                                             5.5.9       Verify configuration..................................................................               32
                                                             5.5.10 Device-specific functions........................................................                         32
                                                             5.5.11 Disconnect...............................................................................                 32
                                                 5.6         Networking................................................................................................       33
                                                             5.6.1       Configuring network.................................................................                 34
                                                             5.6.2       Deleting network......................................................................               34
                                                 5.7         Report........................................................................................................   34
                                                 5.8         User groups...............................................................................................       37
                                                 5.9         Updating Safety Designer.........................................................................                38

                                     6           Deinstallation..................................................................................... 39
                                                 6.1         Uninstalling Safety Designer....................................................................                 39

                                     7           Technical data.................................................................................... 40
                                                 7.1         System requirements...............................................................................               40
                                                 7.2         Compatibility.............................................................................................       40
                                                 7.3         System data..............................................................................................        40

                                     8           List of figures..................................................................................... 41

                                     9           List of tables....................................................................................... 42




4    O P E R A T I N G I N S T R U C T I O N S | Safety Designer                                                                               8018180/1U78/2025-10-16 | SICK
                                                                                                                                                  Subject to change without notice

ABOUT THIS DOCUMENT 1


1                  About this document
1.1                Scope
                                   Document identification
                                   Document part number:
                                   • This document: 8018180
                                   • Available language versions of this document: 8018178
                                   You can find the current version of all documents at www.sick.com.

1.2                Target groups
                                   These operating instructions are intended for the following target groups: Project devel‐
                                   opers (planners, developers, designers), operators, and maintenance personnel.

1.3                Further information
                                   http://www.sick.com
                                   The following information is available via the Internet:
                                   ■    Guide for Safe Machinery (six steps to a safe machine)
                                   ■    Safety Designer (software for configuring safety solutions made by SICK AG)

1.4                Symbols and document conventions
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
                                   1.   The sequence of instructions for action is numbered.
                                   2.   Follow the order in which the numbered instructions are given.
                                   ✓    The check mark denotes the result of an instruction.

8018180/1U78/2025-10-16 | SICK                                                      O P E R A T I N G I N S T R U C T I O N S | Safety Designer   5
Subject to change without notice

2 SAFETY INFORMATION


2             Safety information
2.1           General safety notes

                                      WARNING
                                      Ineffectiveness of the protective device due to incorrect use of the configuration soft‐
                                      ware while configuring a product
                                      In the case of non-compliance, it is possible that the dangerous state of the machine
                                      may not be stopped or not stopped in a timely manner.
                                      ►        Read this document carefully before working with the configuration software.
                                      ►        Read the operating instructions for the products before configuring the products in
                                               the configuration software.
                                      ►        Observe all safety notes in the relevant documents.


2.2           Intended use
                                      Safety Designer can be used to design, configure, commission, and diagnose safety-
                                      related devices or system configurations.

2.3           Requirements for the qualification of personnel
                                      Only qualified safety personnel may use the configuration software to project plan,
                                      configure, commission, and diagnose safety-related devices, device groups or system
                                      configurations.

                                      Project planning
                                      You need safety expertise to implement safety functions and select suitable products
                                      for that purpose. You need expert knowledge of the applicable standards and regula‐
                                      tions.

                                      Configuration
                                      You need suitable expertise and experience. You must be able to assess if the machine
                                      is operating safely.

                                      Commissioning
                                      For commissioning, a person is considered competent when he/she has the expertise
                                      and experience in the relevant field and is sufficiently familiar with the application of
                                      the protective device on the machine that he/she can assess its operational safety
                                      status.

                                      Operation and maintenance
                                      You need suitable expertise and experience. You must be instructed in machine oper‐
                                      ation by the machine operator. For maintenance, you must be able to assess if the
                                      machine is operating safely.

2.4           Cybersecurity
                                      To protect against cybersecurity threats, the operator must have a comprehensive
                                      cybersecurity concept, which must be continuously monitored and maintained. A suita‐
                                      ble concept consists of organizational, technical, procedural, electronic, and physical
                                      levels of defense and considers suitable measures for different types of risks. The
                                      measures implemented in this product can only support protection against cybersecur‐
                                      ity threats if the product is used as part of such a concept.


6     O P E R A T I N G I N S T R U C T I O N S | Safety Designer                                          8018180/1U78/2025-10-16 | SICK
                                                                                                              Subject to change without notice

SAFETY INFORMATION 2


                                   You will find further information at www.sick.com/psirt, e.g.:
                                   • General information on cybersecurity
                                   • Contact option for reporting vulnerabilities
                                   • Information on known vulnerabilities (security advisories)




8018180/1U78/2025-10-16 | SICK                                                   O P E R A T I N G I N S T R U C T I O N S | Safety Designer   7
Subject to change without notice

3 PRODUCT DESCRIPTION


3             Product description
3.1           Product characteristics
                                      Safety Designer is the SICK configuration software for safety solutions.
                                      Features:
                                      • Can be used to design, configure, commission, and diagnose safety solutions
                                      • Uniform user interface across individual devices through to complex system land‐
                                           scapes
                                      • Workflow-oriented navigation
                                      • Reports on configuration documentation

3.2           Structure and function
                                      Overview
                                      Safety Designer comprises the following components:
                                       •       The main window with Device tile(s)
                                       •       One or more Device windows

                                      Important information

                                      NOTE
                                      These operating instructions describe the functions of the main Safety Designer win‐
                                      dow.
                                      For a description of configuration in the Device windows, please refer to the operating
                                      instructions for the relevant device.

                                      Main window
                                      The main window includes all the devices in a project, shown as Device tiles. Reports
                                      for the entire project can be created in the main window.

                                      Device window
                                      The devices for a project are configured in the Device windows.

                                      Further topics
                                       •       "User interface", page 12
                                       •       "Open the device window – configure devices", page 30




8     O P E R A T I N G I N S T R U C T I O N S | Safety Designer                                       8018180/1U78/2025-10-16 | SICK
                                                                                                           Subject to change without notice

INSTALLATION 4


4                  Installation
4.1                Licenses

4.1.1              Activating the license
                                   Overview
                                   Certain functions of the Safety Designer require licenses.
                                   The “WIBU Codemeter User Runtime” software is required for licensed functions. The
                                   software can optionally be installed as part of the Safety Designer installation. Alterna‐
                                   tively, the software can be downloaded and installed afterwards from the manufactur‐
                                   er's website: https://www.wibu.com/support/user/user-software.html
                                   You can activate the licenses in a browser using the CodeMeter License Central WebDe‐
                                   pot.

                                   Prerequisites
                                   •    License tool is installed on the server.
                                   •    Activation takes place from the server where the license tool is installed.
                                   •    Server has a connection to the Internet.
                                   •    Ticket number of the license order is available.

                                   Procedure
                                   1.   Opening the CodeMeter License Central WebDepot:
                                        https://license.sick.com/
                                   2.   Enter the Ticket ID and click on Next.
                                   3.   Select the binding for the licenses:
                                         ° Binding to a PC
                                         ° Binding to a dongle
                                   4.   Select the desired licenses.
                                            NOTE Note the specified number of licenses. If you have purchased a license
                                        package and only want to activate specific licenses in it, you need to first distribute
                                        the licenses.
                                   5.   Activate the licenses by clicking the Now activate the selected licenses button.

                                   Complementary information
                                   •    It is also possible to activate a license offline. To do so, following the File-based
                                        license transfer instructions in the WebDepot.

4.1.2              Show license overview
                                   Procedure
                                   1.   Click on License Management under Settings in the main window.
                                   2.   Enter the ticket number in the License field.
                                   3.   Click on Activate.
                                   ✓    The CodeMeter License Central WebDepot opens.
                                   4.   Activate the license here.
                                   ✓    This newly added license is displayed in the License Management of the Safety
                                        Designer.
                                   In addition to single licenses, there are also network licenses. To display them, activate
                                   the display under Options - General settings - Licenses. For details on setting up the license
                                   server, see the documentation for the Wibu CodeMeter tool.




8018180/1U78/2025-10-16 | SICK                                                      O P E R A T I N G I N S T R U C T I O N S | Safety Designer   9
Subject to change without notice

4 INSTALLATION

4.2           Installing Safety Designer
                                      Prerequisites
                                       •       Your Windows user account has rights for installing software.

                                      Procedure
                                      1.       Call up the download web page and enter Safety Designer in the search field on
                                               www.sick.com.
                                      2.       Take note of the system requirements on the download page.
                                      3.       Download the installation file from the download page. Extract it and run it.
                                      4.       Follow the notes from the setup assistant.

4.3           Unsupervised installation
                                      Unsupervised installation
                                      In the case of a silent installation, the Safety Designer installation routine runs without
                                      additional input by the user. Unsupervised installation is configured with parameters in
                                      the command line.
                                      The Inno Setup parameters are available for Safety Designer. You can find the parame‐
                                      ters and their description under: http://www.jrsoftware.org/ishelp
                                      The following syntax applies for the command line:
                                      SafetyDesigner.exe [Parameter1] [Parameter2] [Parameter n]
                                      If you do not want the WIBU Codemeter User Runtime to be installed as well, use
                                      the /NOCODEMETER command.

                                      Example
                                      For unsupervised installation of Safety Designer without calling up message boxes and
                                      restarting the system, the following invocation is required in the command line:
                                      SafetyDesigner_[Version]_Setup.exe /SUPPRESSMSGBOXES /VERYSILENT /NORES‐
                                      TART




10    O P E R A T I N G I N S T R U C T I O N S | Safety Designer                                          8018180/1U78/2025-10-16 | SICK
                                                                                                              Subject to change without notice

OPERATION 5


5                  Operation
5.1                Start
                                   Overview
                                   Following startup, Safety Designer displays the Home screen.




Figure 1: Home screen
1        Create and open a new project.
2        Search for connected devices.
3        Open an existing project.
4        Open a recently saved project.

                                   Certain functions (for example verification) can only be performed on a computer that
                                   meets all the system requirements.
                                   When starting up, the Safety Designer checks the hardware and the operating system.
                                   The Safety Designer reports any issues that were found.

                                   Procedure
                                   ►    Select one of the options.
                                   ✓    Safety Designer switches to its user interface.




8018180/1U78/2025-10-16 | SICK                                                    O P E R A T I N G I N S T R U C T I O N S | Safety Designer   11
Subject to change without notice

5 OPERATION

5.2               User interface




Figure 2: Software controls
1       Menu bar
2       Toolbar
3       Main navigation
4       Working range
5       Device catalog
6       Task list and notes


5.2.1             Menu and toolbar
                                          Menu bar
                                          The following menus are available in the menu bar:
                                           •       Project
                                                   ° Create new project
                                                   ° Open project
                                                   ° Last used
                                                   ° Protect project with password
                                                   ° Save
                                                   ° Save as
                                                   ° Save partial project
                                                   ° History of the project
                                                   ° Close project
                                                   ° Quit
                                           •       Devices

12        O P E R A T I N G I N S T R U C T I O N S | Safety Designer                          8018180/1U78/2025-10-16 | SICK
                                                                                                  Subject to change without notice

OPERATION 5


                                         °    Connect
                                         °    Disconnect
                                         °    Upload
                                         °    Transfer
                                   •    Settings
                                        ° Language
                                        ° Options
                                        ° Update device catalog
                                   •    Extras
                                        ° Create diagnosis dump
                                   •    Help
                                        ° Help (operating instructions)
                                        ° Info (Access information on the software version)
                                        ° Check for update
                                        ° License information
                                   Toolbar
                                   The toolbar includes the commands needed for the various work situations. All the
                                   buttons on the toolbar are described below. Depending on the jobs in progress, fewer
                                   buttons may be displayed (e.g., immediately following startup of Safety Designer).
                                   The following buttons are available in the toolbar:
                                   Table 1: Buttons on the toolbar
                                   Button              Meaning

                                                       Create new project


                                                       Open project


                                                       Save project as file


                                                       Connect to a device or system configuration


                                                       Disconnect from a device or system configuration


                                                       Read configuration from the device or system configuration


                                                       Transfer configuration to a device or system configuration



                                                       Logout from all devices



5.2.2              Navigation
                                   The navigation is available at the top of the Safety Designer. The buttons will take you to
                                   the following areas:
                                   •    Settings (see "Settings", page 18)
                                   •    Configuration (see "Configuration", page 22)
                                   •    Networking(see "Networking", page 33)
                                   •    Report (see "Report", page 34)


8018180/1U78/2025-10-16 | SICK                                                        O P E R A T I N G I N S T R U C T I O N S | Safety Designer   13
Subject to change without notice

5 OPERATION

5.2.3             Working area
                                          The working area displays the area selected in Navigation: Settings, Configuration or
                                          Report.
                                          For example, in the Configuration working area, you can create a project consisting of
                                          several devices.

5.2.4             Task list
                                          Safety Designer determines which steps are still necessary in order to complete a
                                          typical configuration. Using the task list allows you to gradually work through these
                                          steps.
                                          You can sort the tasks or search for tasks.
                                          ►        Click on the triangle at the far left in the footer.
                                          ✓        The tasks and notes are displayed.
                                          ►        Click on Tasks.
                                          ✓        The Sort by and Search fields are shown.

5.2.5             Notes
                                          Notes can be placed in the working area. These notes might include additional informa‐
                                          tion about selected settings, for example.




Figure 3: Notes
1       Display/hide/create notes
2       Notes on a project



14        O P E R A T I N G I N S T R U C T I O N S | Safety Designer                                         8018180/1U78/2025-10-16 | SICK
                                                                                                                 Subject to change without notice

OPERATION 5


                                   Table 2: Buttons for notes
                                   Button              Meaning

                                                       Show notes

                                                       Hide notes

                                                       Create notes

                                   The number of notes is displayed in the status bar.
                                   •    All notes that have been added to a project and to device windows are displayed in
                                        the main Safety Designer window.
                                   •    The device window only displays notes on an individual device or system configura‐
                                        tion.

                                   Edit a note
                                   You can enter a title and text for the note, select a color for the note, or delete the note.
                                   Table 3: Edit buttons for notes
                                   Button              Meaning
                                                       Select color

                                                       Delete note


                                   Go to a note
                                   You can change to the page on which the note was created.
                                   ►    Click on Notes in the footer.
                                   ✓    The available notes are shown.
                                   ►    Click on Go to note next to the desired note.
                                   ✓    The Safety Designer changes to the page on which the note was created.

5.2.6              Adjust user interface
                                   This section outlines how to adjust the Safety Designer user interface.




8018180/1U78/2025-10-16 | SICK                                                      O P E R A T I N G I N S T R U C T I O N S | Safety Designer   15
Subject to change without notice

5 OPERATION




Figure 4: Adjust user interface
1      Show or hide Navigation
2      Show or hide tasks and notes
3      Show or hide information

                                         Select desired language
                                         ►        Use the Language command in the Settings menu to select the desired language.
                                         ✓        The user interface will switch into the selected language.

                                         Show or hide Navigation
                                         On the left hand side of Safety Designer there is a Navigation tool which you can
                                         choose to show or hide.
                                          •       When Navigation is displayed, you will see all Navigation functions arranged hier‐
                                                  archically.
                                          •       When Navigation is hidden there will be more space in the working area, e.g., for
                                                  large projects with lots of Device tiles.

                                         Show or hide tasks and notes
                                         Tasks and notes for a project are displayed in the footer. You can expand this footer.
                                         ►        Click on the triangle at the far left in the footer.
                                         ✓        The tasks and notes are displayed.




16       O P E R A T I N G I N S T R U C T I O N S | Safety Designer                                           8018180/1U78/2025-10-16 | SICK
                                                                                                                  Subject to change without notice

OPERATION 5


                                   Show or hide information
                                   Information on the settings is shown on the pages of the Safety Designer. You can show
                                   or hide this information.
                                   ►    Select the Options... command in the Settings menu.
                                   ✓    The Options dialog box opens.
                                   ►    Activate or deactivate the Show information on configuration pages option in the General
                                        settings tab.
                                   ✓    The information is then either shown or not shown on the configuration pages

5.2.7              Options
                                   General settings
                                   Under General settings, you can find out whether or not information is displayed on the
                                   pages of Safety Designer.

                                   Connection settings
                                   Under Connection settings, the interfaces available on your computer are displayed. Only
                                   activated connections are included in the search for devices.

                                   Dialogs
                                   Under Dialogs, you can reset all dialog settings to the factory settings.

                                   Data recorder
                                   Under Data recorder, you can set after which amount of time recording is terminated
                                   without data signals.
                                   You can also set whether the recording is saved or deleted.

5.2.8              Create diagnosis dump
                                   Overview
                                   You can generate a diagnostics dump for service purposes.

                                   Prerequisites
                                   •    The project file must be saved.
                                   •    Connect the desired devices if the diagnostics dump contains device data.

                                   Procedure
                                   1.   In the menu bar under Extras, select the Create diagnosis dump function.
                                   2.   Select devices which should be included in the diagnostics dump.
                                   3.   Enter optional user name and comments.
                                   4.   Select Create diagnosis dump.
                                   5.   Select the directory and save the diagnostics dump file.
                                   6.   Send diagnostics dump file (.sdsdmp) to SICK Service.

5.3                Projects
                                   Overview
                                   Safety Designer saves the devices' configuration parameters and information in a
                                   project.




8018180/1U78/2025-10-16 | SICK                                                     O P E R A T I N G I N S T R U C T I O N S | Safety Designer   17
Subject to change without notice

5 OPERATION

                                        Projects
                                        The following functions are available for projects:
                                        • Create new project: Opens an empty project.
                                        • Open project: Loads all device information and parameters from a project file. Any
                                             currently open project will be closed.
                                        • Protect project with password: Protects the project with a passport.
                                        • Save project: Saves all device information and parameters in a project file e.g., on
                                             a hard drive.
                                        • Save project as: Saves a project under a different name or in a different location.
                                        • Save subproject as: Saves a selected subproject under a different name or in a
                                             different location.

5.3.1           Protecting projects with a password
                                        Overview
                                        If you protect a project with a password, the project file can only be opened after
                                        entering the password.

                                        Important information

                                        NOTICE
                                        The password cannot be reset. If the password is lost, the project file has to be created
                                        again.

                                        Procedure
                                        1.       In the menu bar, select Project > Protect project with password.
                                        ✓        The dialog window opens.
                                        2.       Enter the password.
                                        3.       Re-enter the password.
                                        4.       Optionally enter a password hint.
                                        5.       Acknowledge the note that the password cannot be reset.
                                        6.       Select OK.

                                        Complementary information
                                        You can remove the password protection using the following menu entry: Project >
                                        Remove password of the current project.

5.4             Settings

5.4.1           Entering project information
                                        Overview
                                        Under project information, you have the option of entering data, for example, in the
                                        project report. The user name helps subsequent users to find a contact for the project.
                                        A description makes it easier to understand a project’s context more quickly.

                                        Procedure
                                        1.       Under Project Information, you can enter a user name, a project name, and a short
                                                 description of the project.
                                        ✓        The project information is saved in the project.




18      O P E R A T I N G I N S T R U C T I O N S | Safety Designer                                                 8018180/1U78/2025-10-16 | SICK
                                                                                                                       Subject to change without notice

OPERATION 5


5.4.2              Network settings
                                   You can configure the defaults for network-compatible devices under Network > Network
                                   settings.

5.4.2.1            Defining the IP addresses
                                   Overview
                                   You can pre-configure the following under IP settings:
                                   •    The range of IP addresses used for automatic IP address generation.
                                   •    Automatic IP address generation and their device assignment. Automatic IP
                                        address generation ensures that IP addresses are not used more than once.

                                   Procedure
                                   1.   In the IP range: fields, enter the lowest and highest IP addresses that are to be
                                        assigned.
                                   2.   If applicable, enter an alternate subnet mask in the Subnet mask: field.
                                   3.   If applicable, enter the IP address of a router in the Router field.
                                   4.   If you want to assign a configured IP address within the defined IP address range
                                        to every device in the project, enable the Assign an IP address from this IP address range
                                        automatically to each new device in the project. option.

5.4.2.2            Configuring the safety network number
                                   Overview
                                   The safety network number (SNN) for a project is assigned under SNN settings (safety
                                   network number). The safety network number should be identical for all devices in an
                                   EFI-pro network or safety-related EtherNet/IP network.
                                   You can take the following actions:
                                   •    Directly enter a SNN (to do so, you must know the correct SNN format).
                                   •    Use the Paste button to paste an SNN from the clipboard.
                                   •    Use the Copy button to copy an SNN to the clipboard.
                                   •    Generate a SNN.

                                   Procedure
                                   1.   If you want to assign the configured SNN to every device in the project, enable the
                                        Assign this safety network number automatically to each new device in the project. option.
                                   2.   Click on Generate.
                                   ✓    The Safety network number dialog opens.
                                   3.   Generating an SNN:
                                        ►     Click on Time-based.
                                              An SNN with the current time stamp is generated and displayed.
                                        ►     In the Manual (Decimal) field, enter a number between 1 and 9999 and click
                                              on Generate.
                                              An SNN based on the manual entry is generated and displayed.
                                   4.   Click on OK.
                                   ✓    The dialog is closed and the SNN is applied.

                                   Complementary information
                                   If you start the configuration online with a device connected, the SNN of that device is
                                   stored as the default for other devices.




8018180/1U78/2025-10-16 | SICK                                                       O P E R A T I N G I N S T R U C T I O N S | Safety Designer   19
Subject to change without notice

5 OPERATION

5.4.3             Connections via router (NAT)
                                          You can use router connections to find devices from another network and then perform
                                          configuration and diagnostics with Safety Designer.
                                          You can define TCP/IP ports in a NAT table (network address translation table) of a
                                          network router. The devices are available via these ports.

5.4.3.1           Establishing connections to devices via router
                                          Prerequisites
                                           •       The NAT table is configured in the router.

                                          Procedure
                                          In a new project:
                                          1.       Activate the Connection via router active field.
                                          2.       Enter the router IP address.
                                          3.       In the table for the device, enter the TCP/IP configuration port on the router, the
                                                   IP address and the TCP/IP configuration port of the device. The information must
                                                   match the configured NAT table.
                                          ✓        The affected device is assigned to the router.
                                          4.       If necessary, add other devices with the Add line button.
                                          ✓        Another line is added to the table and can be filled with the respective values.
                                          5.       Select Connect.
                                          In an existing project:
                                          1.       Activate the Connection via router active field.
                                          2.       Enter the router IP address.
                                          3.       Select Add device from project.
                                          ✓        A window with all available devices in the project opens.
                                          4.       Select the desired devices by activating the checkbox.
                                          5.       Select Add device(s).
                                          ✓        The desired devices are written in the table.
                                          6.       Select Connect.

                                          Complementary information
                                           •       You can only assign devices to one router.
                                           •       You can find the TCP/IP configuration port of the device in the operating instruc‐
                                                   tions of the respective device.
                                           •       After connecting to the device, the device tile in the configuration receives a serial
                                                   number.

5.4.3.2           Searching for devices in a router
                                          Prerequisites
                                           •       The NAT table is configured in the router.
                                           •       Connections to devices must be separated for assignment.

                                          Procedure
                                          1.       Activate the Connection via router active field.
                                          2.       Enter the router IP address.
                                          3.       Select Search for suitable devices via router.
                                          ✓        All available devices of the router are displayed.
                                          4.       Select the desired devices via Assign. If you would like to access all devices, select
                                                   Assign all.
                                          ✓        The devices can now be configured or diagnosed with the Safety Designer.


20        O P E R A T I N G I N S T R U C T I O N S | Safety Designer                                             8018180/1U78/2025-10-16 | SICK
                                                                                                                     Subject to change without notice

OPERATION 5


                                   5.   Select Connect.

                                   Complementary information
                                   •    You can use the Identify button to identify devices in the application. The respective
                                        device flashes for a certain amount of time after the button is pressed.

5.4.4              Activating time synchronization
                                   Overview
                                   You can synchronize the time and date of the devices in the network. This is important,
                                   amongst other things, for ensuring that diagnostics and reports have synchronized and
                                   correct time stamps.
                                   The following options are available for time synchronization:
                                   •    One device in the project acts as the time server for all other devices. All other
                                        devices obtain the time from this device.
                                   •    A UTC server acts as the time server for all devices. All devices obtain a so-called
                                        coordinated universal time from the UTC server.
                                   •    A UTC server acts as the time server for one device in the project. This device
                                        obtains from the UTC server the coordinated world time and acts as the time
                                        server for all other devices.

                                   Prerequisites
                                   •    Time synchronization only occurs for devices that support SNTP (Simple Network
                                        Time Protocol).

                                   Procedure
                                   A device or a UTC server acts as the time server
                                   1. In the drop-down menu under configuration type, select the device or time server
                                        option.
                                   2. Enter the IP address of the time server (a device on the network or the UTC server)
                                        in the IP address field.
                                   3. For the devices that use the time from the time server, specify the update interval
                                        and Maximum deviation.
                                   4. Click on Apply to all devices from the current project that are included in the time synchroniza‐
                                        tion consistency check.
                                   ✓ The configuration is applied to all devices for which the consistency check has
                                        been enabled.
                                   5. Review the results of the consistency check and, if necessary, correct any errors.
                                   6. Reboot device.
                                   ✓ Time synchronization is activated.
                                   Higher-level device as the time server with upstream time server
                                   1. In the drop-down menu under configuration type, select the Preceding device as a time
                                       server with upstream external time server option.
                                   2. In the IP address field, enter the IP address of the UTC server.
                                   3. Select the IP address of the device that will act as the time server for the other
                                       devices in the project.
                                   4. Specify the update interval and Maximum deviation for the device.
                                   5. For the devices that use the time from the time server, specify the update interval
                                       and Maximum deviation.
                                   6. Click on Apply to all devices from the current project that are included in the time synchroniza‐
                                       tion consistency check.
                                   ✓ The configuration is applied to all devices for which the consistency check has
                                       been enabled.
                                   7. Review the results of the consistency check and, if necessary, correct any errors.


8018180/1U78/2025-10-16 | SICK                                                         O P E R A T I N G I N S T R U C T I O N S | Safety Designer   21
Subject to change without notice

5 OPERATION

                                        8.       Restart the devices.
                                        ✓        Time synchronization is activated.

                                        Complementary information
                                        The consistency check is automatically enabled for all devices that support SNTP. You
                                        can deactivate the consistency check under Time synchronization in the device window.

5.4.5           Configuring the data recorder
                                        Overview
                                        The data recorder saves records in a file.
                                        You can start the data recorder from the relevant device window. The storage location
                                        and file name are specified at the project level, however.

                                        Procedure
                                        ►        Enter the storage location and file location for the record file of the data recorder
                                                 under Data recorder.
                                        ✓        The storage location and file name of the record file are adopted.

5.5             Configuration
                                        You collect the devices of a project in the Configuration area. The available devices can
                                        be found in the Device Catalog. The devices are displayed as Device tiles in the working
                                        range.




22      O P E R A T I N G I N S T R U C T I O N S | Safety Designer                                             8018180/1U78/2025-10-16 | SICK
                                                                                                                   Subject to change without notice

OPERATION 5




Figure 5: Configuration
1        Device management
2        Device tile


5.5.1              Device management
                                   Overview
                                   Device Management contains all available devices:
                                   • The Catalog tab contains the devices installed in Safety Designer.
                                   • The Search tab contains the devices found during a search.
                                   Search for devices in the Search tab
                                   If a device is connected to the computer, Safety Designer can detect the device.
                                   In Options, you can specify which interfaces of your computer are included in the
                                   search (see "Options", page 17).

                                   Complementary information
                                   •    If devices are located behind a firewall, you need to open the relevant ports.
                                         ° The Safety Designer searches for devices on UDP ports 30718 ... 30738
                                         ° The devices respond on UDP port 30719
                                   •    If the devices are located behind a router in the network, the search function of
                                        the Safety Designer will not find them.




8018180/1U78/2025-10-16 | SICK                                                   O P E R A T I N G I N S T R U C T I O N S | Safety Designer   23
Subject to change without notice

5 OPERATION

                                          ►        In this case you need to enter the complete IP address (including subnet mask
                                                   and gateway address) in the device window.
                                                    ° The Safety Designer searches for devices on TCP port 2122
                                                    ° The devices respond on TCP port 2122
5.5.1.1           Generic EtherNet/IP CIP safety device
                                          Create a generic Ethernet/IP CIP safety device in the device catalog in the main Safety
                                          Designer window. It is possible to integrate devices from third-party manufacturers into
                                          a Flexi Soft system via EtherNet/IP™ in this way.
                                          Possible EtherNet/IP™ connections
                                          • EtherNet/IP™ with CIP Safety™
                                              FX3-GEPR as the originator with an EtherNet/IP™ CIP Safety™ device as the target

5.5.1.1.1                     Creating generic Ethernet/IP CIP safety device
                                          ►        Double-click on generic Ethernet/IP CIP safety device in the device catalog.
                                          ✓        A device tile for the generic Ethernet/IP CIP safety device is added in the device
                                                   overview.

5.5.1.1.2                     Configuring generic Ethernet/IP CIP safety device
                                          Procedure
                                          1.       Click on the device tile for the generic Ethernet/IP CIP safety device to open the
                                                   associated device window.
                                          2.       In the General navigation, make the following settings:
                                                   ►     Enter a device name and assign an image to the device where applicable.
                                                   ►     Enter the device IP address and the project safety network number.
                                                   ►     Enter the general characteristics of the new device (supplier, product type,
                                                         product code, main version, and minor version). You can find this data in the
                                                         manual or the EDS file for the device.
                                                   ►     Optionally, enter a user and/or a comment.
                                          3.       Under Default settings, enter the general connection parameters. This includes the
                                                   data format, as well as the maximum fault number and the standard RPI rate where
                                                   applicable. You can find this data in the manual or the EDS file for the device.
                                          4.       Optionally, you can also enter a configuration signature under Default settings.
                                          5.       In the Connections navigation, configure the connection paths of the new device.
                                                   These can be calculated from the assembly data of the device (can be found in
                                                   the manual or the EDS file). Alternatively, you can enter the hexadecimal connec‐
                                                   tions paths directly under Define connection path.
                                                   NOTE
                                                   You must always enter the assembly size, even if a hexadecimal connection path is
                                                   being used.


                                          Complementary information
                                          There are pre-configured generic profiles for different robot controls available for import
                                          in the configuration of the generic EtherNet/IP CIP safety device. You can select the
                                          profiles in the General navigation via Import example.

5.5.2             Device overview
                                          Devices are displayed as device tiles in the working area of the device overview.




24        O P E R A T I N G I N S T R U C T I O N S | Safety Designer                                            8018180/1U78/2025-10-16 | SICK
                                                                                                                    Subject to change without notice

OPERATION 5




                                   Figure 6: Device tiles


5.5.2.1            Add device tile
                                   Procedure
                                   The devices from the device catalog can be added to a project in the working range:
                                   1. Open main navigation Configuration.
                                   2. Drag a device into the working range using drag and drop. Alternatively, double-
                                        click on a device in the device catalog.
                                   ✓ The device is shown as a tile in the working range.

                                   Complementary information
                                   When a device is configured offline for the first time, the device selection wizard opens
                                   for devices with multiple variants (device types). This is where you select the exact type
                                   of device to be configured.

5.5.2.2            Functions of the device tile
                                   Views
                                   You can use the buttons in the working area to select different views for the tiles.
                                   Table 4: Buttons for selecting the type of information on a tile
                                   Button               Meaning

                                                        Display configuration view on the tile

                                                        Display diagnostics view on the tile

                                                        Display network view on the tile

                                                        The size of the tiles can be adjusted using the slider.




8018180/1U78/2025-10-16 | SICK                                                          O P E R A T I N G I N S T R U C T I O N S | Safety Designer   25
Subject to change without notice

5 OPERATION

                                     Tile menu
                                     In the top right-hand corner of the tile you will find the symbol to open the Tile menu
                                     (gray triangle).

                                     Status indicators
                                     In the top left-hand corner of the tile the status of the device is displayed.
                                     Table 5: Device status displays
                                      Icon                         Meaning
                                                                   The device is ready for use.

                                                                   The device is only partially ready for use (because, for example, the configu‐
                                                                   ration has not yet been verified).
                                                                   There are tasks in the task list. The device is not ready for use.

                                                                   There are tasks in the task list. The device is partially ready for use.

                                                                   There are warnings for the device. But it is still ready for use.

                                                                   One or more errors have occurred. The device is not ready for use.


                                     The footer of the tile shows the status of the connection to the device.
                                     Table 6: Status of connection
                                      Icon                         Meaning
                                                                   Disconnected

                                                                   Addressable

                                                                   Connected

                                                                   Connection broken

                                                                   Device is not reachable


                                     Buttons
                                     Table 7: Tile buttons dependent upon device status
                                      Button                       Meaning
                                                                   Establish connection with device

                                                                   Disconnect from device

                                                                   Write the configuration into the device

                                                                   Import configuration from the device

                                                                   Verifying configuration


                                                                   Start application (function is device-specific (see "Device-specific functions",
                                                                   page 32))
                                                                   Set an initial password for the device




26   O P E R A T I N G I N S T R U C T I O N S | Safety Designer                                                           8018180/1U78/2025-10-16 | SICK
                                                                                                                              Subject to change without notice

OPERATION 5


                                   Table 8: Tile buttons not dependent upon device status
                                   Button             Meaning
                                                      Viewing information on the device

                                                      Open device window

                                                      Make device display or LEDs flash (function is device-specific (see "Device-
                                                      specific functions", page 32) and is only active when device is connected)
                                                      Update checksums; the checksums are recalculated (function is then only
                                                      active if the checksums are not up to date)


5.5.2.3            Removing Device tiles
                                   Procedure
                                   1.   Open the Tile menu in the top right-hand corner (gray triangle).
                                   2.   Select the Remove command.
                                   ✓    The Device tile is removed.

5.5.3              Connecting to connected devices
                                   Overview
                                   Depending on the device connection, you can connect the devices to the Safety
                                   Designer via USB, serial connection or via a network (TCP/IP connection).

                                   Important information

                                   NOTE
                                   Using IT security tools, e.g., a firewall, can lead to problems connecting to the devices.

                                   Prerequisites
                                   TCP/IP connection:
                                   • The device has an IP address.
                                   • The IP address of the device is in the same subnet or in a subnet for which a route
                                       is configured.

                                   Procedure
                                   For a new project without devices:
                                   1. In the Devices menu, select the Search command or click on Search in the tool bar.
                                   ✓ The Safety Designer changes to the Search tab in Device Management.
                                   ✓ The detected devices are displayed after a successful scan.
                                   2. Drag the found device or devices from the search to the working area of the device
                                        overview.
                                   ✓ The physical device is assigned to the project. The status of the device tile will
                                        show Connected or Addressable.
                                   For a project with devices from the catalog created offline:
                                   1. In the Devices menu, select the Search command or click on Search in the tool bar.
                                   ✓ The Safety Designer changes to the Search tab in Device Management.
                                   ✓ The detected devices are displayed after a successful scan.
                                   2. Drag the found device or devices from the search to the respective tile of the
                                        device in the working area Device overview.
                                   ✓ The physical device is assigned to the project. The status of the device tile
                                        switches to Connected or Addressable.




8018180/1U78/2025-10-16 | SICK                                                       O P E R A T I N G I N S T R U C T I O N S | Safety Designer   27
Subject to change without notice

5 OPERATION

                                        For a project with devices that have been physically assigned:
                                             Requirement: an assignment to a physically existing device must have already
                                             been carried out in advance, see procedure above.
                                        1. In the Devices menu, click on the Connect all command or the Connect selection or
                                             Connect all command in the toolbar.
                                              ° Connect selection: select the desired device with which a connection is to be
                                                  established in the following window.
                                                  The status of the selected device will change to Connected.
                                              ° Connect all: a connection is established with all assigned devices.
                                                  The status of the device tile(s) will change to Connected.
                                        Additional offline or physical devices can be added in Device Management via the
                                        Catalog or Search.

                                        Complementary information
                                        Connection status:
                                        • Connected: The device is connected via USB or a network and the Safety Designer
                                            can establish a TCP/IP connection to the device.
                                        •   Addressable: If the device is not displayed as Connected, but can be addressed
                                            via UDP broadcast, then the Safety Designer displays the connection status as
                                            Addressable. With this connection status, only a few basic interactions with the
                                            device are possible.

                                        Further topics
                                         •       "Device management", page 23
                                         •       "Functions of the device tile", page 25

5.5.4           Assigning device tiles to physically present devices
                                        Overview
                                        If a project has been configured offline, the device tiles for the project are not assigned
                                        to the devices that are physically present.
                                        The physically present devices can be found in the device catalog on the Found devices
                                        tab, and the device tiles of the project in the workspace.
                                        The assignment of a device tile to a physically present device can also be removed
                                        again. This means that the device tiles for a project can, for example, be reassigned to
                                        different devices at a later point in time.

                                        Important information

                                        NOTE
                                        Before configuration data can be transferred, the device tiles of the project must
                                        be assigned to the found devices. This is essential from a safety technology-related
                                        perspective.

                                        Prerequisites
                                        It is only possible to assign a device tile to a physically present device if the configured
                                        type code of the device tile and the actual type code of the device match.

                                        Procedure
                                        Connecting a device to a device tile
                                        ►   Drag a found device from the device catalog to the respective device tile using
                                            drag and drop.
                                        ✓ The device is now associated with the device tile, and the tile displays the status


28      O P E R A T I N G I N S T R U C T I O N S | Safety Designer                                          8018180/1U78/2025-10-16 | SICK
                                                                                                                Subject to change without notice

OPERATION 5


                                        Connected (see table 6, page 26).
                                   ✓    It is now possible, for example, to transfer a configuration to the device.
                                   Transferring a configuration from one device to another
                                   ►    Drag a found device from the device catalog to the workspace using drag and
                                        drop.
                                   ✓ A device tile is placed in the workspace, and the tile displays the status Connected
                                        (see table 6, page 26).
                                   ►    Import the configuration from the device.
                                   ►    In the Tile menu (triangle in the top right-hand corner of the tile), select the Remove
                                        assignment command.
                                   ✓ The tile displays the status Disconnected.
                                   ►    Drag another device with the same type code onto the device tile.
                                   ✓ The device is now associated with the device tile, and the tile displays the status
                                        Connected (see table 6, page 26).
                                   ►    Transfer the configuration to the device.

                                   Complementary information
                                   Note the version number
                                   Devices have, amongst other things, a version number. This version number is shown
                                   on the type label. The device configuration is generally downward compatible but not
                                   upward compatible.
                                   •    The configuration of a device with a version number V 1.0.0 can be transferred to
                                        a version V 1.1.0 device.
                                   •    The configuration of a device with a version number V 1.1.0 cannot be transferred
                                        to a version V 1.0.0 device.
                                   Preventing automatic allocation
                                   If a device tile has previously been allocated to a device, that device tile will automat‐
                                   ically be connected to the same device in future as soon as the Safety Designer
                                   connects to the connected devices. This is because the sensor is allocated to a project
                                   file. You can use the Remove assignment function to remove this automatic connection
                                   and prevent it from happening in future.

5.5.5              Import configuration
                                   Overview
                                   Safety Designer can import partial configurations or the entire configuration from con‐
                                   nected devices.

                                   Procedure
                                   1.   In the Parameter menu, select the Upload command or, in the toolbar, click on
                                        Upload.
                                   ✓    A dialog box opens. The available partial configurations and connected devices are
                                        displayed in this dialog box.
                                   2.   Under Devices, select the devices from which the partial configurations are to be
                                        read out.
                                   3.   Under Partial configurations, select the partial configurations which are to be read by
                                        the devices.
                                   4.   Click on Read in selection.
                                   ✓    Safety Designer imports the selected partial configurations from the connected
                                        devices.




8018180/1U78/2025-10-16 | SICK                                                     O P E R A T I N G I N S T R U C T I O N S | Safety Designer   29
Subject to change without notice

5 OPERATION

5.5.6           Open the device window – configure devices
                                        Overview
                                        To configure the device, perform diagnostics or create reports, open a device window.




                                        Figure 7: Example of a device window

                                        Procedure
                                        You have the following options:
                                        ►    Double-click on the Device tile.
                                             Or:
                                        ►    Open the tile menu and choose Configure.
                                        ✓ The device window opens.

                                        Complementary information
                                        When a device is configured offline for the first time, the device selection wizard opens
                                        for devices with multiple variants (device types). This is where you select the exact type
                                        of device to be configured.

5.5.7           Logging into or out of a device
                                        Overview
                                        You can log into or out of an assigned device in the device window. You can also change
                                        the user group.



                                        Figure 8: Login button                       Figure 9: Logout button




30      O P E R A T I N G I N S T R U C T I O N S | Safety Designer                                            8018180/1U78/2025-10-16 | SICK
                                                                                                                  Subject to change without notice

OPERATION 5


                                   Important information

                                   NOTICE
                                   When you log into a device, the configuration software stores the password so that you
                                   do not need to re-enter it for other configuration steps.
                                   If you do not change any other settings in the login dialog, the password is deleted as
                                   soon as you exit the configuration software, or log out in the main window or Device
                                   window.
                                   If you enable the Temporarily store password for login on additional devices. function, the
                                   password will be retained even if you log out in the device window only.
                                   If you leave the computer unattended, you must log off to prevent unwanted access to
                                   the device.

                                   Procedure
                                   Logging into a device or changing the user group
                                   1. In the toolbar, click on the Login button.
                                   ✓ The Login dialog window opens.
                                   2. In the User group drop-down menu, select the desired user group.
                                   3. Enter the password in the Password field.
                                   4. If necessary, activate the Temporarily store password for login on additional devices.
                                       function.
                                   ✓ User group and password are temporarily stored for login on additional devices.
                                   5. Click on Login.
                                   Logging out of a device
                                   ►   In the menu and toolbar, click on the Logout button.

                                   Complementary information
                                   The Device tile shows the logged-in user group at the bottom right.

                                   Further topics
                                   •    "User groups", page 37

5.5.8              Transfer configuration
                                   Overview
                                   You can transfer a new or altered configuration to connected devices.
                                   At first, a configuration only exists as a project, namely as a configuration file. You have
                                   to transfer the configuration file to the device. The compatibility of the configuration is
                                   checked during the transfer.
                                   You can transfer the entire configuration or partial configurations to the connected
                                   device.

                                   Procedure
                                   ►    In the Parameter menu, select the Transfer command or, in the toolbar, click on
                                        Transfer.
                                   ✓    A dialog box opens. The available partial configurations and connected devices are
                                        displayed in this dialog box.
                                   ►    Under Devices, select into which devices the partial configurations are to be trans‐
                                        ferred.
                                   ►    Under Partial configurations, select which partial configurations are to be transferred
                                        into the devices.
                                   ►    Click on Transfer selection.
                                   ✓    The Log in dialog box is opened.

8018180/1U78/2025-10-16 | SICK                                                     O P E R A T I N G I N S T R U C T I O N S | Safety Designer   31
Subject to change without notice

5 OPERATION

                                         ►        Select the user group Authorized customer and enter the password.
                                         ►        Click on Log in.
                                         ✓        The progress of the transfer process is displayed in Safety Designer.



                                                  Figure 10: Progress display


                                         Further topics
                                          •       "User groups", page 37

5.5.9            Verify configuration
                                         Overview
                                         The configuration must be verified to ensure that the safety function is implemented
                                         correctly.

                                         Important information

                                         NOTE
                                         Additional information on transferring and verifying a configuration can be found in the
                                         operating instructions for the relevant device.

                                         Procedure
                                         ►        Select Verify in the Tile menu.
                                         ✓        Safety Designer displays the configuration report.
                                         ►        Check the configuration report, and, if appropriate, click on Confirm.
                                         ✓        The device configuration is shown as verified.

5.5.10           Device-specific functions
                                         The following functions are possible depending on the device:
                                          •       Start safety application
                                          •       Stop safety application
                                          •       Identify the devices (e.g., through flashing display or LEDs)

5.5.11           Disconnect
                                         Procedure
                                         1.       In the System menu, select the Disconnect command or click on Disconnect in the
                                                  toolbar.
                                         ✓        The Safety Designer displays all connected devices.
                                         2.       Select specific or all devices to be disconnected.
                                         3.       Select Disconnect.
                                         ✓        The Safety Designer disconnects the selected devices. The status in each relevant
                                                  Device tile changes to Disconnected.

                                         Complementary information
                                         Once the last connected device has been disconnected, the status of Safety Designer
                                         also changes to Disconnected.




32       O P E R A T I N G I N S T R U C T I O N S | Safety Designer                                              8018180/1U78/2025-10-16 | SICK
                                                                                                                     Subject to change without notice

OPERATION 5


5.6                Networking
                                   The Safety Designer is able to establish a network between the following systems:
                                   • Flexi Soft systems with an FX3-GEPR EFI-pro gateway
                                   • Other EFI-pro-enabled SICK devices (e.g., microScan3 Pro EFI-pro)
                                   • Devices from third-party manufacturers that support EtherNet/IP™ CIP Safety™
                                   NOTE
                                   EtherNet/IP™-enabled devices from third-party manufacturers can be integrated as
                                   generic EtherNet/IP CIP safety devices in projects in Safety Designer, see "Generic Ether‐
                                   Net/IP CIP safety device", page 24.




Figure 11: Networking
1        Networking icon for EFI-pro target
2        Networking icon for EFI-pro originator
3        Networking between devices




8018180/1U78/2025-10-16 | SICK                                                      O P E R A T I N G I N S T R U C T I O N S | Safety Designer   33
Subject to change without notice

5 OPERATION

5.6.1           Configuring network
                                        Important information

                                        NOTE
                                         •       An originator must always be networked to a target. Networking two originators or
                                                 two targets is not possible.
                                         •       If you click on a networking icon, then the networking icons with which a network
                                                 can be established are highlighted.
                                         •       Double-clicking on the EFI-pro interface of a device tile opens the associated
                                                 configuration page in the device window for this device.
                                         •       Double-clicking on the EFI-pro networking line opens the associated configuration
                                                 page in the device window for the originator of this network.

                                        Procedure
                                        1.       In the main Safety Designer window, create a project with the desired devices and
                                                 configure these as required.
                                        2.       Click on Networking in the Safety Designer main window.
                                        ✓        The networking view opens.
                                                 In the networking view, the tile of every EFI-pro-enabled device contains one or
                                                 two networking icons for EFI-pro networks.
                                                  ° A networking icon on the upper edge of the device tile indicates that the
                                                       device can act as a CIP Safety™ target.
                                                  °    A networking icon on the lower edge of the device tile indicates that the
                                                       device can act as a CIP Safety™ originator.
                                        3.       Click on a networking icon and establish a network by dragging it to another
                                                 networking icon. During the drag and drop process, possible connection points for
                                                 networks are highlighted in blue.

5.6.2           Deleting network
                                        ►        In this context window of the networking line, click on the Delete button.

5.7             Report
                                        Using reports, you can compile information about all the devices in a project, save it as
                                        a PDF and archive it.




34      O P E R A T I N G I N S T R U C T I O N S | Safety Designer                                            8018180/1U78/2025-10-16 | SICK
                                                                                                                  Subject to change without notice

OPERATION 5




Figure 12: Example of a report
1        Contents of the report
2        Buttons on the report
3        Sorting
4        Compilation of the contents

You can create reports on individual devices in the relevant device window:




8018180/1U78/2025-10-16 | SICK                                           O P E R A T I N G I N S T R U C T I O N S | Safety Designer   35
Subject to change without notice

5 OPERATION




1    Contents of the report
2    Compilation of the contents

                                       Buttons on the report
                                       Table 9: Buttons on the report
                                        Button                       Meaning

                                                                     Save report as a PDF

                                                                     Print report

                                                                     Save project components

                                                                     Update report


                                       Sorting
                                       ►        Select Sort devices.
                                       ✓        The contents will be compiled by individual device.
                                       ►        Select Sort chapters.
                                       ✓        The contents will be compiled in chapters according to theme, e.g., configuration,
                                                parts list etc.

                                       User-specific compilation of contents
                                       ►        Mark the desired devices or working areas of the report in the list.
                                       ✓        All selected information is displayed.

36     O P E R A T I N G I N S T R U C T I O N S | Safety Designer                                               8018180/1U78/2025-10-16 | SICK
                                                                                                                    Subject to change without notice

OPERATION 5


5.8                User groups
                                   Overview
                                   The devices contain a hierarchy of user groups that regulate access to the devices.
                                   For certain actions (e.g., transferring a configuration to the device), you are requested
                                   to log onto the device with the respective user group.
                                   Depending on the device, 3 or 4 user groups are available.

                                   Important information

                                   NOTICE
                                   When you log into a device, the configuration software stores the password so that you
                                   do not need to re-enter it for other configuration steps.
                                   If you do not change any other settings in the login dialog, the password is deleted as
                                   soon as you exit the configuration software, or log out in the main window or Device
                                   window.
                                   If you enable the Temporarily store password for login on additional devices. function, the
                                   password will be retained even if you log out in the device window only.
                                   If you leave the computer unattended, you must log off to prevent unwanted access to
                                   the device.

                                   Device with 3 user groups
                                   Table 10: User groups
                                   User group              Password                                     Authorization
                                        Operator           Does not need a password (anyone             • May read configuration from the
                                                           can log in as a machine operator).                device (if not blocked).
                                        Maintenance        Does not have a factory-set pass‐            • May read configuration from the
                                        personnel          word. The password is created by                  device.
                                                           the authorized client (namely, it is         •    May transfer verified configura‐
                                                           not possible initially to log in as a             tion to the device.
                                                           maintenance technician).
                                        Authorized client The password SICKSAFE is created              • May read configuration from the
                                                          at the factory. Change this pass‐                  device.
                                                          word to protect the device against            • May transfer verified and
                                                          unauthorized access.                               unverified configuration to the
                                                                                                             device.
                                                                                                        •    May verify configuration.
                                                                                                        •    Can set a password for mainte‐
                                                                                                             nance technicians.

                                   Devices with 4 user groups
                                   Table 11: User groups
                                   User group              Password                                     Authorization
                                        Operator           No password required. Anyone can             • May read configuration from the
                                                           log on as a machine operator.                     device.
                                        Maintenance        Deactivated ex-works, i.e. it is not         • May read configuration from the
                                        personnel          initially possible to log on as a                 device.
                                                           maintenance technician. The user             • May transmit verified configura‐
                                                           group can be activated by the user                tion to the device.
                                                           group administrator and provided             • Change own password allowed.
                                                           with a password.




8018180/1U78/2025-10-16 | SICK                                                          O P E R A T I N G I N S T R U C T I O N S | Safety Designer   37
Subject to change without notice

5 OPERATION

                                       User group                   Password                            Authorization
                                               Authorized client Deactivated ex-works, i.e. it is       • May read configuration from the
                                                                 not initially possible to log on as        device.
                                                                 an authorized customer. The user       • May transmit verified and
                                                                 group can be activated by the user         unverified configuration to the
                                                                 group administrator and provided           device.
                                                                 with a password.                       •   May verify configuration.
                                                                                                        •   Resetting the safety function
                                                                                                            and communication settings to
                                                                                                            factory defaults is allowed.
                                                                                                        •   Change own password allowed.
                                                                                                        •   Changing the password of the
                                                                                                            Maintenance personnel user group
                                                                                                            is allowed.
                                               Administrator        The password SICKSAFE is created    • May read configuration from the
                                                                    at the factory.                         device.
                                                                    ►   Change this password to pro‐    •   May transmit verified and
                                                                                                            unverified configuration to the
                                                                        tect the device against unau‐
                                                                                                            device.
                                                                        thorized access.
                                                                                                        •   May verify configuration.
                                                                                                        •   Resetting whole device to fac‐
                                                                                                            tory settings allowed.
                                                                                                        •   Activating and deactivating
                                                                                                            device functions is allowed.
                                                                                                        •   Activating and deactivating the
                                                                                                            Maintenance personnel and Author‐
                                                                                                            ized client user groups is
                                                                                                            allowed.
                                                                                                        •   Change own password allowed.
                                                                                                        •   Changing the passwords of
                                                                                                            the Maintenance personnel and
                                                                                                            Authorized client user groups is
                                                                                                            allowed.

                                      Complementary information
                                      The configuration of the device is saved in the system plug. Therefore, the passwords
                                      are retained when the device is replaced if the system plug is still used.

5.9           Updating Safety Designer
                                      Overview
                                      You can use the Update icon in the menu bar to check whether a newer version of
                                      Safety Designer is available.
                                                      Update


                                      Procedure
                                      1.       Click the Update icon in the menu bar.
                                      ✓        Safety Designer shows the currently installed version and the latest available
                                               version.
                                               If a new version is available, then update Safety Designer as follows:
                                      2.       Select Open website for download.
                                      3.       Download the Safety Designer version from the SICK website.
                                      4.       Install Safety Designer.

                                      Further topics
                                       •       "Installation", page 9

38    O P E R A T I N G I N S T R U C T I O N S | Safety Designer                                                     8018180/1U78/2025-10-16 | SICK
                                                                                                                         Subject to change without notice

DEINSTALLATION 6


6                  Deinstallation
6.1                Uninstalling Safety Designer
                                   Procedure
                                   ►     In the Windows Start menu, select the Remove Safety Designer Package <version-num‐
                                         ber> command in the SICK/Safety Designer program folder and follow the instruc‐
                                         tions.
                                   Or:
                                   ►     Uninstall the Safety Designer Package <version-number> in the system control.




8018180/1U78/2025-10-16 | SICK                                                    O P E R A T I N G I N S T R U C T I O N S | Safety Designer   39
Subject to change without notice

7 TECHNICAL DATA


7             Technical data
7.1           System requirements
                                      Overview
                                      Certain functions (for example verification) can only be performed on a computer that
                                      meets all the system requirements.
                                      When starting up, the Safety Designer checks the hardware and the operating system.
                                      The Safety Designer reports any issues that were found.

                                      Prerequisites
                                      Minimum system configuration:
                                      • Processor: 2 GHz, x64-compatible
                                      • RAM: 4 GB (64 bit)
                                      • Hard drive: 5 GB free space
                                      • Operating system: Windows 11, 24H2 or Windows 10 Enterprise LTSC, 21H2
                                          (64 Bit)
                                      • Software: Microsoft .NET Framework 4.7.2
                                      Recommended system configuration:
                                      • Processor: Intel Core i5 8th generation or AMD Ryzen 5 2500U or newer, x64-com‐
                                          patible
                                      • RAM: 8 GB or more
                                      • Hard drive: SSD with at least 10 GB of free space
                                      • Screen resolution: Full HD (1920 x 1080) or higher
                                      • Operating system: Windows 11 (current version)
                                      • Software: Microsoft .NET Framework 4.7.2
                                      Complementary information
                                      To ensure compatibility and a high level of security, SICK recommends upgrading to
                                      the latest Windows service pack and installing important updates. You can find the
                                      necessary components on the Windows update website.

7.2           Compatibility
                                      The Safety Designer checks the compatibility of the connected devices and, if applica‐
                                      ble, requests you to download the latest version of the Safety Designer.

7.3           System data
                                      Table 12: Safety Designer system data
                                       Designation                                     Data
                                       Communication protocols                         TCP/IP
                                                                                       UDP/IP
                                       Requests to devices                             TCP port: 2122
                                                                                       UDP port: 30718 ... 30738
                                       Response from devices                           TCP port: 2122
                                                                                       UDP port: 30718
                                       Time synchronization - device-side, only rel‐   TCP port: 123
                                       evant for the devices supported in Safety       UDP port: 123
                                       Designer.
                                       Update check                                    HTTPS query to server
                                                                                       Port 443, outbound only



40    O P E R A T I N G I N S T R U C T I O N S | Safety Designer                                           8018180/1U78/2025-10-16 | SICK
                                                                                                               Subject to change without notice

LIST OF FIGURES 8


8                  List of figures
                                   1.    Home screen...............................................................................................................11
                                   2.    Software controls........................................................................................................12
                                   3.    Notes........................................................................................................................... 14
                                   4.    Adjust user interface.................................................................................................. 16
                                   5.    Configuration...............................................................................................................23
                                   6.    Device tiles..................................................................................................................25
                                   7.    Example of a device window...................................................................................... 30
                                   8.    Login button................................................................................................................ 30
                                   9.    Logout button..............................................................................................................30
                                   10.   Progress display..........................................................................................................32
                                   11.   Networking.................................................................................................................. 33
                                   12.   Example of a report.................................................................................................... 35




8018180/1U78/2025-10-16 | SICK                                                                           O P E R A T I N G I N S T R U C T I O N S | Safety Designer    41
Subject to change without notice

9 LIST OF TABLES


9             List of tables
                                      1.        Buttons on the toolbar............................................................................................... 13
                                      2.        Buttons for notes........................................................................................................ 15
                                      3.        Edit buttons for notes................................................................................................. 15
                                      4.        Buttons for selecting the type of information on a tile.............................................25
                                      5.        Device status displays................................................................................................ 26
                                      6.        Status of connection.................................................................................................. 26
                                      7.        Tile buttons dependent upon device status............................................................. 26
                                      8.        Tile buttons not dependent upon device status....................................................... 27
                                      9.        Buttons on the report................................................................................................. 36
                                      10.       User groups................................................................................................................. 37
                                      11.       User groups................................................................................................................. 37
                                      12.       Safety Designer system data..................................................................................... 40




42    O P E R A T I N G I N S T R U C T I O N S | Safety Designer                                                                           8018180/1U78/2025-10-16 | SICK
                                                                                                                                               Subject to change without notice

LIST OF TABLES 9




8018180/1U78/2025-10-16 | SICK     O P E R A T I N G I N S T R U C T I O N S | Safety Designer   43
Subject to change without notice

8018180/1U78/2025-10-16/en
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