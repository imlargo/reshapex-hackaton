TECHNICAL INFORMATION


microScan3 - PROFINET
Safety laser scanner

SIMATIC STEP 7

Described product
                                   microScan3 - PROFINET

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




2   T E C H N I C A L I N F O R M A T I O N | microScan3 - PROFINET                                       8026537/2021-03-15 | SICK
                                                                                                        Subject to change without notice

CONTENTS


Contents
                                   1   About this document........................................................................                               4
                                       1.1      Purpose of this document........................................................................                 4
                                       1.2      Scope.........................................................................................................   4
                                       1.3      Target groups............................................................................................        4
                                       1.4      Symbols and document conventions......................................................                           4

                                   2   Integration..........................................................................................                     6
                                       2.1      Preparing for the integration....................................................................                6
                                       2.2      Installing microScan3 - PROFINET GSDML.............................................                              6
                                       2.3      Integrating the safety laser scanner........................................................                     7

                                   3   Overview of the PROFIsafe parameters......................................... 12

                                   4   Overview of the process images..................................................... 13

                                   5   Notes on implementing the process images................................ 17

                                   6   Troubleshooting................................................................................. 19




8026537/2021-03-15 | SICK                                                                    T E C H N I C A L I N F O R M A T I O N | microScan3 - PROFINET     3
Subject to change without notice

1 ABOUT THIS DOCUMENT


1             About this document
1.1           Purpose of this document
                                     This integration example guides you step by step through the process of integrating a
                                     safety laser scanner of type microScan3 – PROFINET (all variants) into a SIMATIC STEP
                                     7 project.
                                     Depending on the application, it is possible that this integration example may not suit
                                     your specific application case. The experts at SICK can, on request, assist you with the
                                     integration.
                                     SICK cannot guarantee that the following integration example will be error-free when
                                     implemented, e.g., due to future changes to SIMATIC Manager STEP 7. SICK assumes
                                     no liability for any damage that may result from the use of this integration example.
                                     This example was created using version V5.5 + SP4 + HF11 of SIMATIC Manager STEP
                                     7. The descriptions in this document may therefore vary for future versions of the
                                     software.

1.2           Scope
                                     Product
                                     This document applies to the following products:
                                     • Product designation: microScan3 - PROFINET
                                     Document identification
                                     Document part number:
                                     • This document has the following part number: 8026537
                                     • All available language versions of this document are available under the following
                                         part number: 8026530
                                     You can find the current version of all documents at www.sick.com.

1.3           Target groups
                                     This document is intended for system integrators who want to integrate the safety laser
                                     scanner into their application.

1.4           Symbols and document conventions
                                     The following symbols and conventions are used in this document:

                                     Safety notes and other notes

                                     DANGER
                                     Indicates a situation presenting imminent danger, which will lead to death or serious
                                     injuries if not prevented.


                                     WARNING
                                     Indicates a situation presenting possible danger, which may lead to death or serious
                                     injuries if not prevented.


                                     CAUTION
                                     Indicates a situation presenting possible danger, which may lead to moderate or minor
                                     injuries if not prevented.


4     T E C H N I C A L I N F O R M A T I O N | microScan3 - PROFINET                                       8026537/2021-03-15 | SICK
                                                                                                          Subject to change without notice

ABOUT THIS DOCUMENT 1


                                   NOTICE
                                   Indicates a situation presenting possible danger, which may lead to property damage if
                                   not prevented.


                                   NOTE
                                   Indicates useful tips and recommendations.

                                   Instructions to action
                                   b    The arrow denotes instructions to action.
                                   1.   The sequence of instructions for action is numbered.
                                   2.   Follow the order in which the numbered instructions are given.
                                   ✓    The check mark denotes the result of an instruction.




8026537/2021-03-15 | SICK                                                    T E C H N I C A L I N F O R M A T I O N | microScan3 - PROFINET   5
Subject to change without notice

2 INTEGRATION


2             Integration
2.1           Preparing for the integration
                                     Approach
                                     1.      Update Safety Designer and SIMATIC STEP 7 to the latest release (version and, if
                                             applicable, hotfix).
                                     2.      Configure the safety laser scanner using Safety Designer. Some parameters can
                                             only be specified via Safety Designer.

2.2           Installing microScan3 - PROFINET GSDML
                                     Overview
                                     The GSDML file contains the device description of the safety laser scanner for the
                                     controller. It only needs to be installed once.

                                     Important information

                                     NOTE
                                     Always install the latest GSDML file in the controller.

                                     Approach
                                     1.      The current GSDML file for integrating the safety laser scanner into the controller
                                             can be downloaded at www.sick.com.
                                     2.      In SIMATIC STEP 7 (HW Config): Options > Install GSD File…




                                     3.      Select the folder containing the GSDML file.




                                     4.      Select the GSDML file and click on Install.



6     T E C H N I C A L I N F O R M A T I O N | microScan3 - PROFINET                                          8026537/2021-03-15 | SICK
                                                                                                             Subject to change without notice

INTEGRATION 2




                                   5.   If the following message appears, click Yes to confirm it.




                                   ✓




2.3                   Integrating the safety laser scanner
                                   Prerequisites
                                   The GDSML file of the safety laser scanner has been installed.

                                   Approach
                                   1.   In the HW Config tab: Using drag and drop, drag microscan3 from the Catalog to
                                        PROFINET IO system. You will find microScan3 under PROFINET IO > Additional Field
                                        Devices > Sensors > Safety Laser Scanners.




8026537/2021-03-15 | SICK                                                     T E C H N I C A L I N F O R M A T I O N | microScan3 - PROFINET   7
Subject to change without notice

2 INTEGRATION




                                    2.      If the following message appears, click OK to confirm it.




                                    3.      Select a suitable module.
                                            see "Overview of the process images", page 13
                                    4.      If applicable, right-click on the standard module (Slot 1) and select Delete to
                                            remove it.




                                    5.      To add a new module, double-click on the desired module in the Catalog. Alterna‐
                                            tively, use drag and drop to drag the desired module into Slot 1.




                                    6.      Double-click on microScan 3. Alternatively, right-click > Object Properties.




8    T E C H N I C A L I N F O R M A T I O N | microScan3 - PROFINET                                               8026537/2021-03-15 | SICK
                                                                                                                 Subject to change without notice

INTEGRATION 2




                                   7.   General > Properties
                                   8.   Enter the Device name (PROFINET name). The entered Device name must match the
                                        Profinet Name field in Safety Designer.




                                   9.   General > Properties > Ethernet…




                                   10. Enter the IP address and click OK to confirm. The entered value must match the
                                       value configured in Safety Designer.
                                   11. Close the window.




8026537/2021-03-15 | SICK                                                   T E C H N I C A L I N F O R M A T I O N | microScan3 - PROFINET   9
Subject to change without notice

2 INTEGRATION




                                    12. Double-click on the module in Slot1 (e.g., mS3 6Byte In/Out…). Alternatively, right-
                                        click > Object Properties….




                                    13. Under Addresses: Enter the Start address. The value is generated automatically in
                                        SIMATIC STEP 7 but can be modified if necessary.




                                    14. Properties > PROFIsafe
                                    15. Enter the F_Dest_Add, F_WD_Time and, if applicable, F_iPar_CRC.




10   T E C H N I C A L I N F O R M A T I O N | microScan3 - PROFINET                                        8026537/2021-03-15 | SICK
                                                                                                          Subject to change without notice

INTEGRATION 2


                                   16. To modify a value: Select the parameter and click Change value…. The entered
                                       values must match the values configured in Safety Designer.
                                       see "Overview of the PROFIsafe parameters", page 12




                                   ✓   The safety laser scanner has been successfully integrated into the hardware con‐
                                       figuration.




8026537/2021-03-15 | SICK                                                   T E C H N I C A L I N F O R M A T I O N | microScan3 - PROFINET   11
Subject to change without notice

3 OVERVIEW OF THE PROFISAFE PARAMETERS


3            Overview of the PROFIsafe parameters
                                    Several PROFIsafe parameters are available. Of these parameters, the following are
                                    relevant for integrating the device.
                                    •       F_Dest_Add
                                            F destination address. For PROFIsafe communication, the safety laser scanner
                                            needs a clear F_Dest_Add. You need to enter the same value as the one config‐
                                            ured in Safety Designer.
                                    •       F_WD_Time
                                            Watchdog time (monitoring time) for the cyclical service. The watchdog time should
                                            be long enough to tolerate short delays in communication. It does, however, have
                                            an effect on the response time of the overall system (for example in the event of a
                                            fault) and is therefore safety-relevant.
                                            The default value is 150 ms. This is adequate in many cases. The integrator needs
                                            to check the value and, if necessary, adjust it to avoid errors at a later time.
                                    •       F_iPar_CRC
                                            Checksum of the safety configuration. Is used to check whether the safety-relevant
                                            settings were changed. The entered value must match the value configured in
                                            Safety Designer for the configuration checksum (function and network). It is only
                                            needed if a process image is used where F_iPar_CRC is checked (module with
                                            the suffix –iParCRC). This parameter must be updated if the configuration of the
                                            safety laser scanner is modified in any way. If the parameter is not updated (e.g.,
                                            due to an unauthorized modification of the configuration), the controller goes into
                                            the safe state.




12   T E C H N I C A L I N F O R M A T I O N | microScan3 - PROFINET                                         8026537/2021-03-15 | SICK
                                                                                                           Subject to change without notice

OVERVIEW OF THE PROCESS IMAGES 4


4                     Overview of the process images
                                       Variants
                                       The microScan3 - PROFINET supports 8 PROFIsafe process images (in the controller:
                                       modules). The 8 process images can be divided into 2 groups depending on the PROFI‐
                                       safe version (2.4 or 2.6.1). Which process images to use depends on the version of
                                       PROFIsafe that the controller supports. If you do not know which PROFIsafe version your
                                       controller supports, use the process images for PROFIsafe version 2.4.
                                           PROFIsafe version 2.4                             PROFIsafe version 2.6.1
                                           12-byte                                           12-byte
                                           12-byte with iParCRC                              12-byte with iParCRC
                                           6-byte                                            6-byte
                                           6-byte with iParCRC                               6-byte with iParCRC

                                       The process images differ with regard to their size (6 bytes or 12 bytes) and the
                                       incorporation of the iParCRC parameter.
                                       6-byte process images must be used in the following cases:
                                       • Only a limited range of peripheral addresses are available in your application.
                                       • The microScan3 PROFINET is replacing a safety laser scanner of type S3000
                                            PROFINET.
                                       • The safety software for your S7 does not support 12-byte process images.
                                       If your application requires constant monitoring of the checksums of the sensor config‐
                                       uration, use a process image with iParCRC.



                                       Structure of the process image (12 bytes)
Table 1: Safety-related PROFIsafe process image: input of the device, output of the control
 Byte           Bit 7              Bit 6            Bit 5          Bit 4         Bit 3              Bit 2                  Bit 1                 Bit 0
 0              Reserved                                                         ActivateS‐ StopAlarm‐                     Reserved              TriggerRun‐
                                                                                 tandbyMode Detection                                            Mode
 1              SetMonitoringCaseNoTable1
 2              Reserved
 3              Reserved
 4              Reserved
 5              Reserved
 6              Reserved
 7              Reserved
 8              Reserved
 9   1)
                TriggerReset‐ TriggerReset‐ TriggerReset‐ TriggerReset‐ TriggerReset‐ TriggerReset‐ TriggerReset‐ TriggerReset‐
                CutOff‐       CutOff‐       CutOff‐       CutOff‐       CutOff‐       CutOff‐       CutOff‐       CutOff‐
                Path08        Path07        Path06        Path05        Path04        Path03        Path02        Path01
 10             Reserved
 11             Reserved                                                                                                   TriggerDevi‐ TriggerDevi‐
                                                                                                                           ceReboot‐    ceRebootWi‐
                                                                                                                           WithNetwork thoutNet‐
                                                                                                                                        work
1)    Cut-off paths 5 to 8 are only available for the Pro performance package.




8026537/2021-03-15 | SICK                                                                T E C H N I C A L I N F O R M A T I O N | microScan3 - PROFINET       13
Subject to change without notice

4 OVERVIEW OF THE PROCESS IMAGES

Table 2: Safety-related PROFIsafe process image: output of the device, input of the control
 Byte         Bit 7                 Bit 6                 Bit 5               Bit 4         Bit 3         Bit 2         Bit 1              Bit 0
 0            Reserved                                    Manipula‐           Reference‐    Contamina‐    Contamina‐    Standbymo‐         RunModeac‐
                                                          tionStatus          ContourSta‐   tionError     tionWarning   deActive           tive
                                                                              tus
 1 1)         SafeCutOff‐           SafeCutOff‐           SafeCutOff‐         SafeCutOff‐   SafeCutOff‐   SafeCutOff‐   SafeCutOff‐        SafeCutOff‐
              Path08                Path07                Path06              Path05        Path04        Path03        Path02             Path01
 2            Reserved
 3   1)
              NonsafeCu‐            NonsafeCu‐            NonsafeCu‐          NonsafeCu‐    NonsafeCu‐    NonsafeCu‐    NonsafeCu‐         NonsafeCu‐
              tOffPath08            tOffPath07            tOffPath06          tOffPath05    tOffPath04    tOffPath03    tOffPath02         tOffPath01
 4            Reserved
 5   1)
              ResetRequir‐ ResetRequir‐ ResetRequir‐ ResetRequir‐ ResetRequir‐ ResetRequir‐ ResetRequir‐ ResetRequir‐
              edCutOff‐    edCutOff‐    edCutOff‐    edCutOff‐    edCutOff‐    edCutOff‐    edCutOff‐    edCutOff‐
              Path08       Path07       Path06       Path05       Path04       Path03       Path02       Path01
 6            Reserved
 7            CurrentMonitoringCaseNoTable1
 8            Reserved
 9            Reserved
 10           Reserved
 11           Reserved                                                                                                  DeviceError        Applicatio‐
                                                                                                                                           nError
1)    Cut-off paths 5 to 8 are only available for the Pro performance package.

Table 3: Non-safety-related PROFINET process image: output of the device, input of the control
 Byte         Bit 7                 Bit 6                 Bit 5               Bit 4         Bit 3         Bit 2         Bit 1              Bit 0
 0            Reserved                                    Manipula‐           Reference‐    Contamina‐    Contamina‐    Standbymo‐         RunModeac‐
                                                          tionStatus          ContourSta‐   tionError     tionWarning   deActive           tive
                                                                              tus
 1 1)         StatusSafe‐           StatusSafe‐           StatusSafe‐         StatusSafe‐   StatusSafe‐   StatusSafe‐   StatusSafe‐        StatusSafe‐
              CutOff‐               CutOff‐               CutOff‐             CutOff‐       CutOff‐       CutOff‐       CutOff‐            CutOff‐
              Path08                Path07                Path06              Path05        Path04        Path03        Path02             Path01
 2            Reserved
 3   1)
              NonsafeCu‐            NonsafeCu‐            NonsafeCu‐          NonsafeCu‐    NonsafeCu‐    NonsafeCu‐    NonsafeCu‐         NonsafeCu‐
              tOffPath08            tOffPath07            tOffPath06          tOffPath05    tOffPath04    tOffPath03    tOffPath02         tOffPath01
 4            Reserved
 5   1)
              ResetRequir‐ ResetRequir‐ ResetRequir‐ ResetRequir‐ ResetRequir‐ ResetRequir‐ ResetRequir‐ ResetRequir‐
              edCutOff‐    edCutOff‐    edCutOff‐    edCutOff‐    edCutOff‐    edCutOff‐    edCutOff‐    edCutOff‐
              Path08       Path07       Path06       Path05       Path04       Path03       Path02       Path01
 6            Reserved
 7            CurrentMonitoringCaseNoTable1
 8            Reserved
 9            Reserved
 10           Reserved
 11           Reserved                                                                                                  DeviceError        Applicatio‐
                                                                                                                                           nError
1)    Cut-off paths 5 to 8 are only available for the Pro performance package.




14          T E C H N I C A L I N F O R M A T I O N | microScan3 - PROFINET                                                       8026537/2021-03-15 | SICK
                                                                                                                                Subject to change without notice

OVERVIEW OF THE PROCESS IMAGES 4


                                       Structure of the process image (6 bytes)
Table 4: Safety-related PROFIsafe process image: input of the device, output of the control
 Byte           Bit 7              Bit 6         Bit 5         Bit 4             Bit 3              Bit 2                  Bit 1                 Bit 0
 0              Reserved                                                         ActivateS‐ StopAlarm‐                     Reserved              TriggerRun‐
                                                                                 tandbyMode Detection                                            Mode
 1              SetMonitoringCaseNoTable1
 2              Reserved
 3   1)
                TriggerReset‐ TriggerReset‐ TriggerReset‐ TriggerReset‐ TriggerReset‐ TriggerReset‐ TriggerReset‐ TriggerReset‐
                CutOff‐       CutOff‐       CutOff‐       CutOff‐       CutOff‐       CutOff‐       CutOff‐       CutOff‐
                Path08        Path07        Path06        Path05        Path04        Path03        Path02        Path01
 4              Reserved
 5              Reserved                                                                                                   TriggerDevi‐ TriggerDevi‐
                                                                                                                           ceReboot‐    ceRebootWi‐
                                                                                                                           WithNetwork thoutNet‐
                                                                                                                                        work
1)    Cut-off paths 5 to 8 are only available for the Pro performance package.

Table 5: Safety-related PROFIsafe process image: output of the device, input of the control
 Byte           Bit 7              Bit 6         Bit 5         Bit 4             Bit 3              Bit 2                  Bit 1                 Bit 0
 0              Reserved                         Manipula‐     Reference‐        Contamina‐         Contamina‐             Standbymo‐            RunModeac‐
                                                 tionStatus    ContourSta‐       tionError          tionWarning            deActive              tive
                                                               tus
 1 1)           SafeCutOff‐        SafeCutOff‐   SafeCutOff‐   SafeCutOff‐       SafeCutOff‐        SafeCutOff‐            SafeCutOff‐           SafeCutOff‐
                Path08             Path07        Path06        Path05            Path04             Path03                 Path02                Path01
 2 1)           NonsafeCu‐         NonsafeCu‐    NonsafeCu‐    NonsafeCu‐        NonsafeCu‐         NonsafeCu‐             NonsafeCu‐            NonsafeCu‐
                tOffPath08         tOffPath07    tOffPath06    tOffPath05        tOffPath04         tOffPath03             tOffPath02            tOffPath01
 3 1)           ResetRequir‐ ResetRequir‐ ResetRequir‐ ResetRequir‐ ResetRequir‐ ResetRequir‐ ResetRequir‐ ResetRequir‐
                edCutOff‐    edCutOff‐    edCutOff‐    edCutOff‐    edCutOff‐    edCutOff‐    edCutOff‐    edCutOff‐
                Path08       Path07       Path06       Path05       Path04       Path03       Path02       Path01
 4              CurrentMonitoringCaseNoTable1
 5              Reserved                                                                                                   DeviceError           Applicatio‐
                                                                                                                                                 nError
1)    Cut-off paths 5 to 8 are only available for the Pro performance package.

Table 6: Non-safety-related PROFINET process image: output of the device, input of the control
 Byte           Bit 7              Bit 6         Bit 5         Bit 4             Bit 3              Bit 2                  Bit 1                 Bit 0
 0              Reserved                         Manipula‐     Reference‐        Contamina‐         Contamina‐             Standbymo‐            RunModeac‐
                                                 tionStatus    ContourSta‐       tionError          tionWarning            deActive              tive
                                                               tus
 1 1)           StatusSafe‐        StatusSafe‐   StatusSafe‐   StatusSafe‐       StatusSafe‐        StatusSafe‐            StatusSafe‐           StatusSafe‐
                CutOff‐            CutOff‐       CutOff‐       CutOff‐           CutOff‐            CutOff‐                CutOff‐               CutOff‐
                Path08             Path07        Path06        Path05            Path04             Path03                 Path02                Path01
 2 1)           NonsafeCu‐         NonsafeCu‐    NonsafeCu‐    NonsafeCu‐        NonsafeCu‐         NonsafeCu‐             NonsafeCu‐            NonsafeCu‐
                tOffPath08         tOffPath07    tOffPath06    tOffPath05        tOffPath04         tOffPath03             tOffPath02            tOffPath01
 3 1)           ResetRequir‐ ResetRequir‐ ResetRequir‐ ResetRequir‐ ResetRequir‐ ResetRequir‐ ResetRequir‐ ResetRequir‐
                edCutOff‐    edCutOff‐    edCutOff‐    edCutOff‐    edCutOff‐    edCutOff‐    edCutOff‐    edCutOff‐
                Path08       Path07       Path06       Path05       Path04       Path03       Path02       Path01
 4              CurrentMonitoringCaseNoTable1
 5              Reserved                                                                                                   DeviceError           Applicatio‐
                                                                                                                                                 nError
1)    Cut-off paths 5 to 8 are only available for the Pro performance package.




8026537/2021-03-15 | SICK                                                                T E C H N I C A L I N F O R M A T I O N | microScan3 - PROFINET       15
Subject to change without notice

4 OVERVIEW OF THE PROCESS IMAGES

                                    Addressing the bits in the controller
                                    The bits of the process images can be accessed in the logic using the following
                                    scheme: Ix.x and Qx.x. The start byte (byte 0) is relative to the specified Start address.
                                    If Start address is set to the value 17, then the output bit 0.0 in the logic can be
                                    accessed as Q17.0. The input bit 3.1 then corresponds to I20.1.




16   T E C H N I C A L I N F O R M A T I O N | microScan3 - PROFINET                                           8026537/2021-03-15 | SICK
                                                                                                             Subject to change without notice

NOTES ON IMPLEMENTING THE PROCESS IMAGES 5


5                     Notes on implementing the process images
                                   Safety-related cut-off paths and non-safety-related cut-off paths
                                   In the following example, cut-off paths 1 (protective field) and 4 (contour detection field)
                                   are safety-related. Cut-off paths 2 and 3 (warning fields) are non-safety-related.




                                   When incorporating the cut-off paths into the logic, the user can select a suitable byte
                                   from the assembly. A cut-off path with a protective field or contour detection field is
                                   always regarded as safety-related. A cut-off path with a warning field is always regarded
                                   as non-safety-related.
                                   Table 7: Example 6-byte process image
                                   Function             Field type           Allocation in the                 Data                               Safe
                                   (Safety Designer)                         process image
                                   Cut-off path 1       Protective field     Safety-related cut-off            I1.0                               Yes
                                                                             path 1
                                   Cut-off path 2       Warning field        Non-safety-related                I2.1                               No
                                                                             cut-off path 2
                                   Cut-off path 3       Warning field        Non-safety-related                I2.2                               No
                                                                             cut-off path 3
                                   Cut-off path 4       Contour detection    Safety-related cut-off            I1.3                               Yes
                                                        field                path 4

                                   Behavior with mixed field types
                                   When a cut-off path with safe and non-safe fields (e.g., protective field and warning
                                   field) is used in different monitoring cases and the monitoring case with the warning
                                   field is active, then the safe cut-off path is deactivated. As a result, the bit for this safe
                                   cut-off path is LOW and the display of the safety laser scanner indicates the OFF state.
                                   The following example illustrates this behavior in the configuration and in the display of
                                   the device. All fields are clear in this example (no field detection).




8026537/2021-03-15 | SICK                                                       T E C H N I C A L I N F O R M A T I O N | microScan3 - PROFINET          17
Subject to change without notice

5 NOTES ON IMPLEMENTING THE PROCESS IMAGES




18   T E C H N I C A L I N F O R M A T I O N | microScan3 - PROFINET     8026537/2021-03-15 | SICK
                                                                       Subject to change without notice

TROUBLESHOOTING 6


6                     Troubleshooting
                                   Error indicators in SIMATIC STEP7
                                   Table 8: Online “Module information…” of the microScan3 (online in HW Config):
                                   General                          IO Device Diagnostics                        Possible causes
                                   Failed                           Incorrect module in slot: n                   • Incorrect microScan3 PRO‐
                                                                                                                      FIsafe module configured in
                                                                                                                      TIA Portal.
                                                                                                                  •   Incorrect process image
                                                                                                                      selected in Safety Designer.
                                   Faulty module (diagnostics       PROFIsafe transmission error:                 • F_WD_Time set too short.
                                   interrupt detected)              timeout (F_WD_Time elapsed)                   • Problems executing the
                                                                                                                      safety program. Check the
                                                                                                                      organizational components
                                                                                                                      and the program structure.
                                   Module configured, but not       Empty                                         • Incorrect PROFINET device
                                   available                                                                          name
                                                                                                                  • Faulty connection between
                                                                                                                      the safety laser scanner
                                                                                                                      and the controller (e.g.,
                                                                                                                      defective cable)
                                                                                                                  •   Voltage supply to the safety
                                                                                                                      laser scanner is interrupted
                                   Faulty module (diagnostics       Mismatch of failsafe destina‐                F_Dest_Add does not match
                                   interrupt detected)              tion address (F_Dest_Add)                    the configuration in Safety
                                                                                                                 Designer.
                                   Faulty module (diagnostics       Inconsistent iParameters                     F_iPar_CRC does not match
                                   interrupt detected)              iParCRC error)                               the configuration in Safety
                                                                                                                 Designer.

                                   Table 9: After saving and compiling the HW Config configuration
                                   Message                                               Possible cause
                                   The system data could not be recreated                The selected module or process image is not
                                   because the configuration is inconsistent             supported by the controller.
                                   (Details: CRC error in the F-I/O with the I/O
                                   address…)
                                   Could not complete initialization of the safety       The selected module or process image is not
                                   program                                               supported by the controller.
                                   (Details: A parameter
                                   S7FTO_COUNT_PS_Input…)

                                   Error indicators on the microScan3 – network LEDs
                                   The safety laser scanner has two PROFINET LEDs in addition to the Ethernet LEDs.
                                   Table 10: Bus error LED, inscription: BF
                                   LED status               Meaning                      Troubleshooting
                                   o                        No supply voltage            b Check power supply, wiring and connected
                                                            or PROFINET commu‐             communication partners.
                                                            nication not active or       b Restart device.
                                                            device is not config‐        b Check the configuration of the device.
                                                            ured
                                   O Green                  PROFINET communi‐            –
                                                            cation is active
                                   Ö Green                  No connection to con‐        b Check PROFINET names.
                                                            trol unit                    b Check the control unit.
                                                                                         b Start the controller.

8026537/2021-03-15 | SICK                                                            T E C H N I C A L I N F O R M A T I O N | microScan3 - PROFINET   19
Subject to change without notice

6 TROUBLESHOOTING

                                     LED status                        Meaning                    Troubleshooting
                                     O Red                             Serious error, device      b Check device.
                                                                       not ready                  b Restart device.
                                                                                                  b Replace device.
                                     Ö Red                             Incorrect PROFINET         b Check the PROFINET configuration, in par‐
                                                                       configuration                ticular F_Dest_Add.
                                     Ö Red/green                       PROFINET alarm is          b Check the cause of the error in the con‐
                                                                       active                       figuration program of the controller and
                                                                                                    observe the help text.
                                                                                                  b Check the alarm in the Safety Designer.
                                    Table 11: System error LED, inscription: BF
                                     LED status                        Meaning                    Troubleshooting
                                     o                                 No supply voltage          b Trigger or launch PROFIsafe communica‐
                                                                       or PROFIsafe commu‐          tion.
                                                                       nication not initialized   b Check whether the same process image is
                                                                       or not active or incor‐      selected in the controller and in the device
                                                                       rect process image           (6 bytes or 12 bytes)
                                                                       selected
                                     O Green                           PROFIsafe communi‐         –
                                                                       cation is active
                                     Ö                                 Passivation of the     b Perform reintegration of the device.
                                     0.5 Hz, green                     device has been com‐
                                                                       pleted, e.g. after
                                                                       communication error
                                                                       or connection termina‐
                                                                       tion
                                     Ö                                 A process image with       b Enter the correct F_iPar_CRC in the config‐
                                     2 Hz, green                       F_iPar_CRC is used,          uration program of the controller.
                                                                       but value 0 is speci‐      b Use process image without F_iPar_CRC.
                                                                       fied as F_iPar_CRC.
                                     O Red                             Serious error, device      b Check and restart the device.
                                                                       not ready                  b Replace device.
                                     Ö Red                             Incorrect PROFIsafe        b Check the PROFIsafe parameters, in partic‐
                                                                       configuration                ular, F_Dest_Add, WD_Time, F_iPar_CRC.
                                                                                                  b Check the PROFINET connection (see
                                                                                                    table 10, page 19).

                                    Error indicators on the microScan3 – network LEDs
                                    The safety laser scanner has two PROFINET LEDs in addition to the Ethernet LEDs.
                                    Table 12: Bus error LED, inscription: BF
                                     LED status                        Meaning                    Troubleshooting
                                     o                                 No supply voltage          b Check power supply, wiring and connected
                                                                       or PROFINET commu‐           communication partners.
                                                                       nication not active or     b Restart device.
                                                                       device is not config‐      b Check the configuration of the device.
                                                                       ured
                                     O Green                           PROFINET communi‐          –
                                                                       cation is active
                                     Ö Green                           No connection to con‐      b Check PROFINET names.
                                                                       trol unit                  b Check the control unit.
                                                                                                  b Start the controller.
                                     O Red                             Serious error, device      b Check device.
                                                                       not ready                  b Restart device.
                                                                                                  b Replace device.


20   T E C H N I C A L I N F O R M A T I O N | microScan3 - PROFINET                                                          8026537/2021-03-15 | SICK
                                                                                                                            Subject to change without notice

TROUBLESHOOTING 6


                                   LED status               Meaning                     Troubleshooting
                                   Ö Red                    Incorrect PROFINET          b Check the PROFINET configuration, in par‐
                                                            configuration                 ticular F_Dest_Add.
                                   Ö Red/green              PROFINET alarm is           b Check the cause of the error in the con‐
                                                            active                        figuration program of the controller and
                                                                                          observe the help text.
                                                                                        b Check the alarm in the Safety Designer.
                                   Table 13: System error LED, inscription: BF
                                   LED status               Meaning                     Troubleshooting
                                   o                        No supply voltage           b Trigger or launch PROFIsafe communica‐
                                                            or PROFIsafe commu‐           tion.
                                                            nication not initialized    b Check whether the same process image is
                                                            or not active or incor‐       selected in the controller and in the device
                                                            rect process image            (6 bytes or 12 bytes)
                                                            selected
                                   O Green                  PROFIsafe communi‐          –
                                                            cation is active
                                   Ö                        Passivation of the     b Perform reintegration of the device.
                                   0.5 Hz, green            device has been com‐
                                                            pleted, e.g. after
                                                            communication error
                                                            or connection termina‐
                                                            tion
                                   Ö                        A process image with        b Enter the correct F_iPar_CRC in the config‐
                                   2 Hz, green              F_iPar_CRC is used,           uration program of the controller.
                                                            but value 0 is speci‐       b Use process image without F_iPar_CRC.
                                                            fied as F_iPar_CRC.
                                   O Red                    Serious error, device       b Check and restart the device.
                                                            not ready                   b Replace device.
                                   Ö Red                    Incorrect PROFIsafe         b Check the PROFIsafe parameters, in partic‐
                                                            configuration                 ular, F_Dest_Add, WD_Time, F_iPar_CRC.
                                                                                        b Check the PROFINET connection (see
                                                                                          table 10, page 19).

                                   Diagnostics using the display
                                   You can use the buttons at the front of the safety laser scanner to display the PROFI‐
                                   NET alarms.
                                   1.   Press the OK button twice.
                                   2.   Diagnostics > PROFINET alarms

                                   NOTE
                                   Active alarms are also displayed in the online module information in Safety Designer and in
                                   SIMATIC Step 7.

                                   Why does “Waiting for input” appear on the display?
                                   • The safety laser scanner has not yet received a valid bit from the controller for
                                       selecting a monitoring case.
                                   • There is an error in the PROFINET/PROFIsafe parameters.
                                   S3000 PROFINET vs microScan3 - PROFINET
                                   If the microScan3 - PROFINET is replacing a safety laser scanner of type S3000 PRO‐
                                   FINET, take into consideration that the process image has a different structure even
                                   though the size of the process image remains the same at 6 bytes.



8026537/2021-03-15 | SICK                                                           T E C H N I C A L I N F O R M A T I O N | microScan3 - PROFINET   21
Subject to change without notice