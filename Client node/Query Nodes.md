# Query Nodes

# I. List Related

## **1. Get Corresponding Value From List**

![](./Genshin Impact Miliastra Wonderland_ General Guide_files/b0ef5442-76f9-462e-9c25-f30055914229.png)

**Node Functions**

Returns the value at the specified ID in the List. IDs start at 0

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | ID | Integer |  |
| Input Parameter | Data List | Generic |  |
| Output Parameter | Result | Generic |  |

## **2. Get List Length**

![](./Genshin Impact Miliastra Wonderland_ General Guide_files/e19fd5e2-c0f9-4a2c-bd32-1cf34c20868f.png)

**Node Functions**

Returns the length of the list (number of elements)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input List | Generic |  |
| Output Parameter | Length | Integer |  |

## **3. Get Maximum Value From List**

![](./Genshin Impact Miliastra Wonderland_ General Guide_files/bb4a5b02-25ac-44bc-9479-1646d5b74200.png)

**Node Functions**

Applies only to Floating Point Number or Integer lists; returns the maximum value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | List | Generic |  |
| Output Parameter | Maximum Value | Generic |  |

## **4. Get Minimum Value From List**

![](./Genshin Impact Miliastra Wonderland_ General Guide_files/bfab8902-da9c-4788-bc09-e74acfe4a652.png)

**Node Functions**

Applies only to Floating Point Number or Integer lists; returns the minimum value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | List | Generic |  |
| Output Parameter | Minimum Value | Generic |  |

## **5. Get Ray Filter Type List**

![](./Genshin Impact Miliastra Wonderland_ General Guide_files/b839c851-0421-4c04-9cee-d44a0bf312f6.png)

**Node Functions**

Assembles the required Ray Filter types into a List. Available filters include Hurtbox, Scene, and Object Self-Collision

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | List | Complete list |  |

## **6. Get Entity Type List**

![](./Genshin Impact Miliastra Wonderland_ General Guide_files/367128e5-39b9-4574-9056-dc047c21bffe.png)

**Node Functions**

Assembles the required Entity types into a List. Types include Stages, Objects, Players, Characters, and Creations

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | List | Complete list |  |

## **7. List Includes This Value**

![]()

**Node Functions**

Returns whether the list contains the specified value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Value | Generic |  |
| Input Parameter | List | Generic |  |
| Output Parameter | Result | Boolean |  |

# II. Custom Variables

## **1. Get Custom Variable**

![]()

**Node Functions**

Returns the value of the specified Custom Variable from the Target Entity

If the variable does not exist, returns the type's default value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Variable Name | String |  |
| Output Parameter | Variable Value | Generic |  |

# III. Preset Status

## **1. Get Preset Status**

![]()

**Node Functions**

Returns the Preset Status value of the specified Entity. Returns 0 if the Entity does not have the specified Preset Status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity | Entity |  |
| Input Parameter | Preset Status Index | Integer |  |
| Output Parameter | Preset Status Value | Integer |  |

# IV. Entity Related

## **1. Query If Entity Is on the Field**

![]()

**Node Functions**

Searches whether the specified Entity is present

Note that Character Entities are still considered present even when Downed

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | On the Field | Boolean |  |

## **2. Get Unit Attack Target**

![]()

**Node Functions**

Returns the Target Entity that the Unit Entity is currently attacking

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Unit Entity | Entity |  |
| Output Parameter | Attack Target Entity | Entity |  |

## **3. Get Target Attachment Point Location**

![]()

**Node Functions**

Returns the Attachment Point Location corresponding to the specified Attachment Point Name on the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Attachment Point Name | String |  |
| Output Parameter | Attachment Point Location | 3D Vector |  |

## **4. Get Target Attachment Point Rotation**

![]()

**Node Functions**

Returns the Attachment Point Rotation corresponding to the specified Attachment Point Name on the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Attachment Point Name | String |  |
| Output Parameter | Attachment Point Rotation | 3D Vector |  |

## **5. Get Target Entity**

![]()

**Node Functions**

Returns the Target Entity. The meaning of this output varies depending on the functional module that references the Filter Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Target Entity | Entity |  |

## **6. Get Entity‘s Type**

![]()

**Node Functions**

Returns the type of the specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | Entity Type | Enumeration |  |

## **7. Get Entity Location**

![]()

**Node Functions**

Returns the Location of the specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity | Entity |  |
| Output Parameter | Location | 3D Vector |  |

## **8. Get Entity Rotation**

![]()

**Node Functions**

Returns the Rotation of the specified Entity in Euler Angles

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity | Entity |  |
| Output Parameter | Rotate | 3D Vector |  |

## **9. Get Self Entity**

![]()

**Node Functions**

Returns the Entity associated with this Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Self Entity | Entity |  |

## **10. Filter Entity List Within Square Range**

![]()

**Node Functions**

Filters Entities within a square range according to specified rules and a maximum count, and returns a list of Entities that meet the conditions

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Width | Floating Point Numbers |  |
| Input Parameter | Height | Floating Point Numbers |  |
| Input Parameter | Length | Floating Point Numbers |  |
| Input Parameter | Central Location | 3D Vector |  |
| Input Parameter | Maximum Filter Quantity | Integer |  |
| Input Parameter | Filter Rules | Enumeration | Options: Default, Random, or Nearest-to-Farthest order |
| Output Parameter | Filter Results | Entity List |  |

## **11. Filter Entity List Within Spherical Range**

![]()

**Node Functions**

Filters Entities within a spherical range according to specific rules and a maximum count, and returns a list of Entities that meet the conditions

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Parameter | Radius | Floating Point Numbers |  |
| Input Parameter | Central Location | 3D Vector |  |
| Input Parameter | Maximum Filter Quantity | Integer |  |
| Input Parameter | Filter Rules | Enumeration | Options: Default, Random, or Nearest-to-Farthest order |
| Output Parameter | Filter Results | Entity List |  |

## **12. Query Entity by GUID**

![]()

**Node Functions**

Searches for an Entity by GUID

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | GUID | GUID |  |
| Output Parameter | Entity | Entity |  |

## **13. Check the Preset Status Value of the Complex Creation**

![]()

**Node Functions**

Query the preset state value of the target creation corresponding to the preset state index.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Creation | Entity |  |
| Input Parameter | Preset Status Index | Integer |  |
| Output Parameter | Preset Status Value | Integer |  |

# V. Faction Related

## **1. Query Entity Faction**

![]()

**Node Functions**

Searches Target Entity's Faction

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | Faction | Faction |  |

## **2. Query If Faction Is Hostile**

![]()

**Node Functions**

Searches whether Faction 1 and Faction 2 are hostile

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Faction 1 | Faction |  |
| Input Parameter | Faction 2 | Faction |  |
| Output Parameter | Hostile | Boolean |  |

# VI. Player and Character Related

## **1. Query If Self Is in Combat**

![]()

**Node Functions**

Searches whether the Entity associated with this Node Graph has entered battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | In Combat | Boolean |  |

## **2. Get Current Character**

![]()

**Node Functions**

Returns the Character Entity currently controlled by this Player's client

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Character Entity | Entity |  |

## **3. Get Player Entity to Which the Character Belongs**

![]()

**Node Functions**

Returns the Player Entity that owns the Character Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Character Entity | Entity |  |
| Output Parameter | Affiliated Player Entity | Entity |  |

## **4. Get List of Player Entities on the Field**

![]()

**Node Functions**

Returns a list of all Player Entities present in the scene

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Player Entity List | Entity List |  |

## **5. Get Character Entity of Specified Player**

![]()

**Node Functions**

Returns the Character Entity of the specified Player Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |
| Output Parameter | Character Entity | Entity |  |

## **6. Query GUID by Entity**

![]()

**Node Functions**

Searches for the GUID of the specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity | Entity |  |
| Output Parameter | GUID | GUID |  |

## **7. Get Player Client Input Device Type**

![]()

**Node Functions**

Returns the Player's local input device type, as determined by the Interface mapping method

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Input Device Type | Enumeration | Includes keyboard/mouse, gamepad, touchscreen |

## **8. Get Player Movement Input**

![]()

**Node Functions**

Returns the Input Direction and Input Strength of the current client player's movement.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Input Direction | Floating Point Numbers |  |
| Output Parameter | Input Strength | Floating Point Numbers |  |

## **9. Query Skill Variable Value**

![]()

**Node Functions**

Searches for the corresponding variable value based on the Skill Variable Config ID.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Variable Config ID | Config ID |  |
| Output Parameter | Variable Value | Floating Point Numbers |  |

## **10. Get Current Key Behavior**

![]()

**Node Functions**

Returns all Key Behavior IDs and their corresponding entry times from the current Key Behavior Log Panel.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Behavior ID List | Integer List |  |
| Output Parameter | Entry Time List | Floating Point List |  |

## **11. Get Current Key Behavior (High Precision)**

![]()

**Node Functions**

Returns all Key Behavior IDs and their corresponding entry times from the current Key Behavior Log Panel. Due to floating-point precision issues, use this node if you require greater granularity for the entry times.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Behavior ID List | Integer List |  |
| Output Parameter | Entry Time List (s) | Integer List |  |
| Output Parameter | Entry Time List (ms) | Integer List |  |

## **12. Get Current Client Time**

![]()

**Node Functions**

Returns the current client time.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Client Time | Floating Point Numbers |  |

## **13. Get Current Client Time (High Precision)**

![]()

**Node Functions**

Returns the current client time. Due to floating-point precision issues, use this node if you requite greater granularity for the client time.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Client Time (s) | Integer |  |
| Output Parameter | Client Time (ms) | Integer |  |

## **14. Query Whether Player Is Currently in Voice Chat**

![]()

**Node Functions**

Returns "Yes" when microphone input is detected from this player's client.

Note: This node only takes effect during multiplayer games (multiplayer test play, actual multiplayer play). It will not work in single-player games (single-player test play, actual single-player play).

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |
| Output Parameter | Currently in Voice Chat? | Boolean |  |

## **15. Get Skill Config ID by Skill Instance ID**

![]()

**Node Functions**

Returns the corresponding Skill Config ID based on the Skill Instance ID provided.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Instance ID | Integer |  |
| Output Parameter | Skill Config ID | Config ID |  |

## **16. Query Skill Instance List by Specified Slot**

![]()

**Node Functions**

Searches for all skill instances in the slot specified.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Slot | Enumeration |  |
| Output Parameter | Skill Instance ID List | Integer List |  |

## **17. Query Active Skill Instance List of Specified Slot**

![]()

**Node Functions**

Returns the skill instance(s) currently in the foreground for the slot specified.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Slot | Enumeration |  |
| Output Parameter | Skill Instance ID List | Integer |  |

## **18. Query Skill Instance ID by Skill Slot and Skill Config ID**

![]()

**Node Functions**

Returns the corresponding skill instance based on the skill slot and Skill Config ID provided.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Slot | Enumeration |  |
| Input Parameter | Skill Config ID | Config ID |  |
| Output Parameter | Skill Instance ID List | Integer |  |

# VII. Unit Tags

## **1. Get Entity List by Unit Tag**

![]()

**Node Functions**

Returns a list of all Entities in the scene that carry this Unit Tag

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Unit Tag Index | Integer |  |
| Output Parameter | Entity List | Entity List |  |

## **2. Get Entity's Unit Tag List**

![]()

**Node Functions**

Returns a list of all Unit Tags carried by the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | List | Integer List |  |

# VIII. General

## **1. Get Local Variable**

![]()

**Node Functions**

Returns the value of a specific local variable

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Variable Name | String |  |
| Output Parameter | Variable Value | Generic |  |

# IX. Custom Aggro

## **1. Query if Specified Entity is in Combat**

![]()

**Node Functions**

Available only for Custom Aggro Mode

Searches whether the specified Entity has entered battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | In Combat | Boolean |  |

## **2. Get the Aggro List of the Specified Entity**

![]()

**Node Functions**

Available only for Custom Aggro Mode

Gets Specific Entity's Aggro List

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Specified Entity | Entity |  |
| Output Parameter | Aggro List | Entity List |  |

## **3. Get the Aggro Target of the Specified Entity**

![]()

**Node Functions**

Available only for Custom Aggro Mode

Gets Aggro Target of Specific Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Specified Entity | Entity |  |
| Output Parameter | Aggro Target | Entity |  |

# X. Triggers

## **1. Get All Entities Within the Collision Trigger**

![]()

**Node Functions**

Returns all Entities within the Collision Trigger corresponding to a specific ID in the Collision Trigger Component on the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Trigger ID | Integer |  |
| Output Parameter | Entity List | Entity List |  |

# XI. Ray

## **1. Get Ray Detection Result**

![]()

**Node Functions**

Returns the first Target or On-Hit Location that meets the Filter criteria, ordered from nearest to farthest along the ray

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Detection Initiator Entity | Entity |  |
| Input Parameter | Launch Location | 3D Vector |  |
| Input Parameter | Launch Direction | 3D Vector |  |
| Input Parameter | Max Ray Length | Floating Point Numbers |  |
| Input Parameter | Faction Filter | Enumeration |  |
| Input Parameter | Entity Type Filter | Enumeration List | Includes Stage, Object, Player, Character, Creation |
| Input Parameter | Hit Layer Filter | Enumeration List | Options: Hurtbox, Scene, and Object Self-Collision |
| Output Parameter | On-Hit Location | 3D Vector |  |
| Output Parameter | On-Hit Entity | Entity |  |

# XII. Scanning

## **1.** Get All Valid Entities That Are Scannable by Scan Component

![]()

**Node Functions**

Returns all Units carrying a Scan Component whose Filter returns True, regardless of the Unit's scannable status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Object List | Entity List |  |

## **2.** Get Entity Currently Scanned by Scan Component

![]()

**Node Functions**

Returns Entities currently detected by the Scan Component; these are Entities in the Active State

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Corresponding Entity | Entity |  |
| Output Parameter | Scan Tag Config ID | Config ID |  |

## **3.** Get Entity's Current Active Scan Tags

![]()

**Node Functions**

Returns the Target Entity's Current Active Scan Tags

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | Scan Tag Config ID | Config ID |  |

## **4. Get Entity's Scan Status**

![]()

**Node Functions**

Get Entity Scan Status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | Scan Status | Enumeration | Options: Invisible, Current Scan Target, Candidate Target, Not Eligible |

# XIII. Dictionary

## **1. Query If Dictionary Contains Specific Key**

![]()

**Node Functions**

Query if the specified dictionary contains a specific key

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Key | Generic |  |
| Output Parameter | Include | Boolean |  |

## **2. Query If Dictionary Contains Specific Value**

![]()

**Node Functions**

Query if the specified dictionary contains a specific value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Value | Generic |  |
| Output Parameter | Include | Boolean |  |

## **3. Check Dictionary Length**

![]()

**Node Functions**

Query the number of key-value pairs in a dictionary

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Length | Integer |  |

## **4. Get List of Keys From Dictionary**

![]()

**Node Functions**

Get a list of all keys in the dictionary. Since the key-value pairs in the dictionary are unordered, the list of keys retrieved may not be in the order they were inserted.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Key List | Generic |  |

## **5. Get List of Values From Dictionary**

![]()

**Node Functions**

Get a list of all values in the dictionary. Since the key-value pairs in the dictionary are unordered, the list of values retrieved may not be in the order they were inserted.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Value List | Generic |  |

## **6. Query Dictionary Value by Key**

![]()

**Node Functions**

Query the value corresponding to a key in the dictionary, and return the default value of the type if the key does not exist.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Key | Generic |  |
| Output Parameter | Value | Generic |  |

# XIV. Unit Status

## **1. Whether the Entity Has the Specified Unit Status**

![]()

**Node Functions**

Query whether the entity has the specified unit status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Unit Status | Configuration ID |  |
| Output Parameter | Has the Status | Boolean |  |

Operation Nodes

1

Explain

---

# Query Nodes

# I. General

## **1. Check Target Position Pathfinding Availability**

![](./Genshin Impact Miliastra Wonderland_ General Guide11_files/be43614f-1a89-4518-888d-c691a1f413f3.png)

**Node Functions**

Check whether a Creation can reach the current Target Point using normal pathfinding

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Is Pathfinding Achievable? | Boolean |  |

## **2. Check the Coordinates When Entering Battle**

![](./Genshin Impact Miliastra Wonderland_ General Guide11_files/b2c297f0-9df1-41a8-be73-a0016b2dc3d8.png)

**Node Functions**

Query the Coordinate Points when a Creation enters battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Entering Battle Position | 3D Vector |  |
| Output Parameter | Entering Battle Rotation | 3D Vector |  |

## **3. Check If Entity Is on the Field**

![](./Genshin Impact Miliastra Wonderland_ General Guide11_files/6148df0d-7109-4956-a2e1-629e6e40a638.png)

**Node Functions**

Check whether the Target Entity is present. Note: even if a Character Entity is in a Down state, it is still considered present

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | On the Field | Boolean |  |

## **4. Check the Vertical Angle From Self to Target**

![](./Genshin Impact Miliastra Wonderland_ General Guide11_files/f2a563cc-7532-4041-83fb-10f96b9301e3.png)

**Node Functions**

Query the vertical angle between the Creation and the Target Entity. Valid only when the Creation has a Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Vertical Angle | Floating Point Numbers |  |

## **5. Check the Vertical Distance From Self to Target**

![](./Genshin Impact Miliastra Wonderland_ General Guide11_files/274ba676-7202-4c5c-bf54-0285f8a8a2ed.png)

**Node Functions**

Query the vertical distance from this Creation to its Target Entity. Valid only when the Creation has a Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Vertical Distance | Floating Point Numbers |  |

## **6. Check the Distance From Self to Target**

![]()

**Node Functions**

Query the distance from this Creation to its Target Entity. Valid only when the Creation has a Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Distance | Floating Point Numbers |  |

## **7. Check the Horizontal Angle From Self to Target**

![]()

**Node Functions**

Query the horizontal angle between this Creation and the Target Entity. Valid only when the Creation has a Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Horizontal Angle | Floating Point Numbers |  |

## **8. Check the Horizontal Distance From Self to Target**

![]()

**Node Functions**

Query the horizontal distance from this Creation to the Target Entity. Valid only when the Creation has a Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Horizontal Distance | Floating Point Numbers |  |

## **9. Check Whether Self Is in Battle**

![]()

**Node Functions**

Check whether the Creation is currently in battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Whether in Battle | Boolean |  |

## **10. Check If Self Is in the Territory**

![]()

**Node Functions**

Check whether this Creation's current location is within the Territory

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Is in the Territory | Boolean |  |

## **11. Check Whether Self Is Using a Skill**

![]()

**Node Functions**

Check whether a Creation is currently casting a Skill. If so, returns the index of the Skill being cast

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Is The Unit Using a Skill? | Boolean |  |
| Output Parameter | Skill ID | Integer |  |

## **12. Get Spawn Point Location Information**

![]()

**Node Functions**

Obtain the Creation's own Spawn Point information

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Spawn Point Coordinates | 3D Vector |  |
| Output Parameter | Spawn Point Rotation | 3D Vector |  |

## **13. Get Stage Entity**

![]()

**Node Functions**

Obtain Stage Entities

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Stage Entity | Entity |  |

## **14. Get Target Level**

![]()

**Node Functions**

Obtain the Target Entity's current level

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | Current Level | Integer |  |

## **15. Get Target ATK**

![]()

**Node Functions**

Obtain the Target Entity's ATK parameters

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | Base ATK | Floating Point Numbers |  |
| Output Parameter | Current ATK | Floating Point Numbers |  |

## **16. Get Target HP**

![]()

**Node Functions**

Obtain HP-related parameters for the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | Base HP | Floating Point Numbers |  |
| Output Parameter | Max HP | Floating Point Numbers |  |
| Output Parameter | Current HP Percentage | Floating Point Numbers |  |

## **17. Get Target Entity**

![]()

**Node Functions**

Obtain the Creation's current Target Entity. Valid only when the Creation has a Target.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Target Entity | Entity |  |

## **18. Get Previous Frame Execution Tactic**

![]()

**Node Functions**

Obtain the Tactic executed by Creations in the previous frame

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Tactic Type | Enumeration |  |
| Output Parameter | Tactical Context | String |  |

## **19. Get Previous Frame Execution Status**

![]()

**Node Functions**

Obtain the Config ID of the [Creation Status Node Graph] executed in the previous frame

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Status Node Graph Configuration ID | Config ID |  |

## **20. Get Entity's Type**

![]()

**Node Functions**

Obtain the Target Entity's Type

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | Entity Type | Enumeration |  |

## **21. Get Entity Location**

![]()

**Node Functions**

Obtain the Target Entity's Location

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | Location | 3D Vector |  |

## **22. Get Entity Rotation**

![]()

**Node Functions**

Obtain the Target Entity's Rotation

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | Rotation | 3D Vector |  |

## **23. Get Object Preset Status**

![]()

**Node Functions**

Obtain the Preset Status Value at the specified Preset Status index from the Target Entity. If the Entity does not have the specified Preset Status, return 0

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Input Parameter | Preset Status Index | Integer |  |
| Output Parameter | Preset Status Value | Integer |  |

## **24. Get Custom Variable**

![]()

**Node Functions**

Obtain the Variable Value of the specified Custom Variable from the Target Entity. If the variable does not exist, returns the default value for that type

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Input Parameter | Variable Name | String |  |
| Output Parameter | Variable Value | Generic |  |

## **25. Get Current Execution Status**

![]()

**Node Functions**

Obtain the config ID of the [Creation Status Node Graph] currently being executed by this Creation

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Status Node Graph Configuration ID | Config ID |  |

## **26. Get Self Entity**

![]()

**Node Functions**

Returns the Entity associated with this Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Self Entity | Entity |  |

## **27. Get Self Preset Status Value**

![]()

**Node Functions**

Obtain the Preset Status Value at the specified Preset Status index for this Entity. If the Entity does not have the specified Preset Status index, return 0

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Preset Status Index | Integer |  |
| Output Parameter | Preset Status Value | Integer |  |

# II. Faction

## **1. Check Entity Faction**

![]()

**Node Functions**

Search for Target Entity's Faction

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | Faction | Faction |  |

## **2. Query If Faction Is Hostile**

![]()

**Node Functions**

Check whether Faction 1 and Faction 2 are hostile

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Faction 1 | Faction |  |
| Input Parameter | Faction 2 | Faction |  |
| Output Parameter | Hostile | Boolean |  |

# III. Lists

## **1. Get Corresponding Value From List**

![]()

**Node Functions**

Return the value at the specified index in the Data List. Indexes start at 0

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | ID | Integer |  |
| Input Parameter | Data List | Generic |  |
| Output Parameter | Result | Generic |  |

## **2. Get List Length**

![]()

**Node Functions**

Returns the length of the list (number of elements)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input List | Generic |  |
| Output Parameter | Length | Integer |  |

## **3. Get Maximum Value From List**

![]()

**Node Functions**

Applies only to Floating Point Number or Integer lists; returns the maximum value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | List | Generic |  |
| Output Parameter | Maximum Value | Generic |  |

## **4. Get Minimum Value From List**

![]()

**Node Functions**

Applies only to Floating Point Number or Integer lists; returns the minimum value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | List | Generic |  |
| Output Parameter | Minimum Value | Generic |  |

## **5. List Includes This Value**

![]()

**Node Functions**

Check whether the specified list contains a specific value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Value | Generic |  |
| Input Parameter | List | Generic |  |
| Output Parameter | Result | Boolean |  |

# IV. Dictionary

## **1. Query If Dictionary Contains Specific Key**

![]()

**Node Functions**

Check whether the specified Dictionary contains the specified Key

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Key | Generic |  |
| Output Parameter | Include | Boolean |  |

## **2. Query If Dictionary Contains Specific Value**

![]()

**Node Functions**

Check whether the specified Dictionary contains the specified Value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Value | Generic |  |
| Output Parameter | Include | Boolean |  |

## **3. Query Dictionary Length**

![]()

**Node Functions**

Query the number of Key-Value Pairs in the Dictionary

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Length | Integer |  |

## **4. Get List of Keys From Dictionary**

![]()

**Node Functions**

Returns a list of all Keys in the Dictionary. Because Key-Value Pairs are unordered, the Keys may not be returned in insertion order

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Key List | Generic |  |

## **5. Query List of Values From Dictionary**

![]()

**Node Functions**

Returns a list of all Values in the Dictionary. Because Key-Value Pairs are unordered, the Values may not be returned in insertion order

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Value List | Generic |  |

## **6. Query Dictionary Value by Key**

![]()

**Node Functions**

Query the corresponding Value in the Dictionary by Key. If the Key does not exist, returns the type's default value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Key | Generic |  |
| Output Parameter | Value | Generic |  |

Operation Nodes

1

Explain

Nút hoạt động

---

# Query Nodes

# I. General

## **1. Check Target Position Pathfinding Availability**

![](./Genshin Impact Miliastra Wonderland_ General Guide16_files/5d1e84da-6c5e-4317-b41d-22d5463cbfbc.png)

**Node Functions**

Check whether a Creation can reach the current Target Point using normal pathfinding

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Is Pathfinding Achievable? | Boolean |  |

## **2. Check the Coordinates When Entering Battle**

![](./Genshin Impact Miliastra Wonderland_ General Guide16_files/d446c295-e1e6-44ac-bca4-f3f6dfd490c9.png)

**Node Functions**

Query the Coordinate Points when a Creation enters battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Entering Battle Position | 3D Vector |  |
| Output Parameter | Entering Battle Rotation | 3D Vector |  |

## **3. Check If Entity Is on the Field**

![]()

**Node Functions**

Check whether the Target Entity is present. Note: even if a Character Entity is in a Down state, it is still considered present

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | On the Field | Boolean |  |

## **4. Check the Vertical Angle From Self to Target**

![]()

**Node Functions**

Query the vertical angle between the Creation and the Target Entity. Valid only when the Creation has a Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Vertical Angle | Floating Point Numbers |  |

## **5. Check the Vertical Distance From Self to Target**

![]()

**Node Functions**

Query the vertical distance from this Creation to its Target Entity. Valid only when the Creation has a Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Vertical Distance | Floating Point Numbers |  |

## **6. Check the Distance From Self to Target**

![]()

**Node Functions**

Query the distance from this Creation to its Target Entity. Valid only when the Creation has a Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Distance | Floating Point Numbers |  |

## **7. Check the Horizontal Angle From Self to Target**

![]()

**Node Functions**

Query the horizontal angle between this Creation and the Target Entity. Valid only when the Creation has a Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Horizontal Angle | Floating Point Numbers |  |

## **8. Check the Horizontal Distance From Self to Target**

![]()

**Node Functions**

Query the horizontal distance from this Creation to the Target Entity. Valid only when the Creation has a Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Horizontal Distance | Floating Point Numbers |  |

## **9. Check Whether Self Is in Battle**

![]()

**Node Functions**

Check whether the Creation is currently in battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Whether in Battle | Boolean |  |

## **10. Check if Self Is in the Territory**

![]()

**Node Functions**

Check whether this Creation's current location is within the Territory

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Is in the Territory | Boolean |  |

## **11. Check Whether Self Is Using a Skill**

![]()

**Node Functions**

Check whether a Creation is currently casting a Skill. If so, returns the index of the Skill being cast

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Is the Unit Using a Skill? | Boolean |  |
| Output Parameter | Skill ID | Integer |  |

## **12. Get Spawn Point Location Information**

![]()

**Node Functions**

Obtain the Creation's own Spawn Point information

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Spawn Point Coordinates | 3D Vector |  |
| Output Parameter | Spawn Point Rotation | 3D Vector |  |

1.

## Get Stage Entity

![]()

**Node Functions**

Obtain Stage Entities

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Stage Entity | Entity |  |

## **14. Get Target Level**

![]()

**Node Functions**

Obtain the Target Entity's current level

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | Current Level | Integer |  |

## **15. Get Target ATK**

![]()

**Node Functions**

Obtain the Target Entity's ATK parameters

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | Base ATK | Floating Point Numbers |  |
| Output Parameter | Current ATK | Floating Point Numbers |  |

## **16. Get Target HP**

![]()

**Node Functions**

Obtain HP-related parameters for the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | Base HP | Floating Point Numbers |  |
| Output Parameter | Max HP | Floating Point Numbers |  |
| Output Parameter | Current HP Percentage | Floating Point Numbers |  |

## **17. Get Target Entity**

![]()

**Node Functions**

Obtain the Creation's current Target Entity. Valid only when the Creation has a Target.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Target Entity | Entity |  |

## **18. Get Previous Frame Execution Tactic**

![]()

**Node Functions**

Obtain the Tactic executed by Creations in the previous frame

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Tactic Type | Enumeration |  |
| Output Parameter | Tactical Context | String |  |

## **19. Get Previous Frame Execution Status**

![]()

**Node Functions**

Obtain the Config ID of the [Creation Status Node Graph] executed in the previous frame

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Status Node Graph Configuration ID | Config ID |  |

## **20. Get Entity's Type**

![]()

**Node Functions**

Obtain the Target Entity's Type

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | Entity Type | Enumeration |  |

## **21. Get Entity Location**

![]()

**Node Functions**

Obtain the Target Entity's Location

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | Location | 3D Vector |  |

## **22. Get Entity Rotation**

![]()

**Node Functions**

Obtain the Target Entity's Rotation

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | Rotatation | 3D Vector |  |

## **23. Get Object Preset Status**

![]()

**Node Functions**

Obtain the Preset Status Value at the specified Preset Status index from the Target Entity. If the Entity does not have the specified Preset Status, return 0

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Input Parameter | Preset Status Index | Integer |  |
| Output Parameter | Preset Status Value | Integer |  |

## **24. Get Custom Variable**

![]()

**Node Functions**

Obtain the Variable Value of the specified Custom Variable from the Target Entity. If the variable does not exist, returns the default value for that type

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Input Parameter | Variable Name | String |  |
| Output Parameter | Variable Value | Generic |  |

## **25. Get Current Execution Status**

![]()

**Node Functions**

Obtain the config ID of the [Creation Status Node Graph] currently being executed by this Creation

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Status Node Graph Configuration ID | Config ID |  |

## **26. Get Self Entity**

![]()

**Node Functions**

Returns the Entity associated with this Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Self Entity | Entity |  |

## **27. Get Self Preset Status Value**

![]()

**Node Functions**

Obtain the Preset Status Value at the specified Preset Status index for this Entity. If the Entity does not have the specified Preset Status index, return 0

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Preset Status Index | Integer |  |
| Output Parameter | Preset Status Value | Integer |  |

# II. Faction

## **1. Check Entity Faction**

![]()

**Node Functions**

Search for Target Entity's Faction

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Enumeration |  |
| Output Parameter | Faction | Faction |  |

## **2. Query If Faction Is Hostile**

![]()

**Node Functions**

Check whether Faction 1 and Faction 2 are hostile

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Faction 1 | Faction |  |
| Input Parameter | Faction 2 | Faction |  |
| Output Parameter | Hostile | Boolean |  |

# III. Lists

## **1. Get Corresponding Value From List**

![]()

**Node Functions**

Return the value at the specified index in the Data List. Indexes start at 0

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | ID | Integer |  |
| Input Parameter | Data List | Generic |  |
| Output Parameter | Result | Generic |  |

## **2. Get List Length**

![]()

**Node Functions**

Returns the length of the list (number of elements)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input List | Generic |  |
| Output Parameter | Length | Integer |  |

## **3. Get Maximum Value From List**

![]()

**Node Functions**

Applies only to Floating Point Number or Integer lists; returns the maximum value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | List | Generic |  |
| Output Parameter | Maximum Value | Generic |  |

## **4. Get Minimum Value From List**

![]()

**Node Functions**

Applies only to Floating Point Number or Integer lists; returns the minimum value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | List | Generic |  |
| Output Parameter | Minimum Value | Generic |  |

## **5. List Includes This Value**

![]()

**Node Functions**

Check whether the specified list contains a specific value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Value | Generic |  |
| Input Parameter | List | Generic |  |
| Output Parameter | Result | Boolean |  |

# IV. Dictionary

## **1. Query If Dictionary Contains Specific Key**

![]()

**Node Functions**

Check whether the specified Dictionary contains the specified Key

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Key | Generic |  |
| Output Parameter | Include | Boolean |  |

## **2. Query If Dictionary Contains Specific Value**

![]()

**Node Functions**

Check whether the specified Dictionary contains the specified Value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Value | Generic |  |
| Output Parameter | Include | Boolean |  |

## **3. Query Dictionary Length**

![]()

**Node Functions**

Query the number of Key-Value Pairs in the Dictionary

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Length | Integer |  |

## **4. Get List of Keys From Dictionary**

![]()

**Node Functions**

Returns a list of all Keys in the Dictionary. Because Key-Value Pairs are unordered, the Keys may not be returned in insertion order

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Key List | Generic |  |

## **5. Query List of Values From Dictionary**

![]()

**Node Functions**

Returns a list of all Values in the Dictionary. Because Key-Value Pairs are unordered, the Values may not be returned in insertion order

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Value List | Generic |  |

## **6. Query Dictionary Value by Key**

![]()

**Node Functions**

Query the corresponding Value in the Dictionary by Key. If the Key does not exist, returns the type's default value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Key | Generic |  |
| Output Parameter | Value | Generic |  |

Operation Nodes

1

Explain

---

# Query Nodes

# I. List Related

## **1. Get Corresponding Value From List**

![](./Genshin Impact Miliastra Wonderland_ General Guide21_files/8e5bfaaa-51b0-4afc-a94c-9b16c57fe5e5.png)

**Node Functions**

Returns the value at the specified ID in the List. IDs start at 0

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | ID | Integer |  |
| Input Parameter | Data List | Generic |  |
| Output Parameter | Result | Generic |  |

## **2. Get List Length**

![](./Genshin Impact Miliastra Wonderland_ General Guide21_files/b2b7ea54-b27e-42c7-932f-4184b436a5ee.png)

**Node Functions**

Returns the length of the list (number of elements)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input List | Generic |  |
| Output Parameter | Length | Integer |  |

## **3. Get Maximum Value From List**

![](./Genshin Impact Miliastra Wonderland_ General Guide21_files/153c2315-3ea6-4b02-ae54-95bf12665611.png)

**Node Functions**

Applies only to Floating Point Number or Integer lists; returns the maximum value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | List | Generic |  |
| Output Parameter | Maximum Value | Generic |  |

## **4. Get Minimum Value From List**

![](./Genshin Impact Miliastra Wonderland_ General Guide21_files/aa3c41d7-5f59-4c1a-a57a-6ae0aa6ea154.png)

**Node Functions**

Applies only to Floating Point Number or Integer lists; returns the minimum value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | List | Generic |  |
| Output Parameter | Minimum Value | Generic |  |

## **5. Get Ray Filter Type List**

![](./Genshin Impact Miliastra Wonderland_ General Guide21_files/7387d1b6-8350-40a5-9277-0d66da3bd0f6.png)

**Node Functions**

Assembles the required Ray Filter types into a List. Available filters include Hurtbox, Scene, and Object Self-Collision

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | List | Enumerationd List |  |

## **6. Get Entity Type List**

![](./Genshin Impact Miliastra Wonderland_ General Guide21_files/e06ef6d8-beb5-4084-bbf4-2c0fe3a0988b.png)

**Node Functions**

Assembles the required Entity types into a List. Types include Stages, Objects, Players, Characters, and Creations

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | List | Enumerationd List |  |

## **7. List Includes This Value**

![](./Genshin Impact Miliastra Wonderland_ General Guide21_files/c2485422-9403-4ee3-a51d-584ca198a5c2.png)

**Node Functions**

Returns whether the list contains the specified value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Value | Generic |  |
| Input Parameter | List | Generic |  |
| Output Parameter | Result | Boolean |  |

# II. Custom Variables

## **1. Get Custom Variable**

![]()

**Node Functions**

Returns the value of the specified Custom Variable from the Target Entity

If the variable does not exist, returns the type's default value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Variable Name | String |  |
| Output Parameter | Variable Value | Generic |  |

# III. Preset Status

## **1. Get Preset Status**

![]()

**Node Functions**

Returns the Preset Status value of the specified Entity. Returns 0 if the Entity does not have the specified Preset Status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity | Entity |  |
| Input Parameter | Preset Status Index | Integer |  |
| Output Parameter | Preset Status Value | Integer |  |

# IV. Entity Related

## **1. Check the Preset Status Value of the Complex Creation**

![]()

**Node Functions**

Query the Preset Status Value of the Target Creation under the corresponding Preset Status index

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Creation | Entity |  |
| Input Parameter | Preset Status Index | Integer |  |
| Output Parameter | Preset Status Value | Integer |  |

## **2. Query If Entity Is on the Field**

![]()

**Node Functions**

Check whether the specified Entity is present

Note that Character Entities are still considered present even when Downed

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | On the Field | Boolean |  |

## **3. Get Unit Attack Target**

![]()

**Node Functions**

Returns the Target Entity that the Unit Entity is currently attacking

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Unit Entity | Entity |  |
| Output Parameter | Attack Target Entity | Entity |  |

## **4. Get Target Attachment Point Location**

![]()

**Node Functions**

Returns the Location of the specified Attachment Point on the Target Entity.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Attachment Point Name | String |  |
| Output Parameter | Attachment Point Location | 3D Vector |  |

## **5. Get Target Entity**

![]()

**Node Functions**

Returns the Target Entity. The meaning of this output varies depending on the functional module that references the Filter Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Target Entity | Entity |  |

## **6. Get Entity's Type**

![]()

**Node Functions**

Returns the type of the specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | Entity Type | Enumeration |  |

## **7. Get Entity Location**

![]()

**Node Functions**

Returns the Location of the specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity | Entity |  |
| Output Parameter | Location | 3D Vector |  |

## **8. Get Entity Rotation**

![]()

**Node Functions**

Returns the Rotation of the specified Entity in Euler Angles

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity | Entity |  |
| Output Parameter | Rotate | 3D Vector |  |

## **9. Get Self Entity**

![]()

**Node Functions**

Returns the Entity associated with this Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Self Entity | Entity |  |

## **10. Filter Entity List Within Square Range**

![]()

**Node Functions**

Filters Entities within a square range according to specified rules and a maximum count, and returns a list of Entities that meet the conditions

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Width | Floating Point Numbers |  |
| Input Parameter | Height | Floating Point Numbers |  |
| Input Parameter | Length | Floating Point Numbers |  |
| Input Parameter | Central Location | 3D Vector |  |
| Input Parameter | Maximum Filter Quantity | Integer |  |
| Input Parameter | Filter Rules | Enumeration | Options: Default, Random, or Sort From Near to Far |
| Output Parameter | Filter Results | Entity List |  |

## **11. Filter Entity List Within Spherical Range**

![]()

**Node Functions**

Filters Entities within a spherical range according to specific rules and a maximum count, and returns a list of Entities that meet the conditions

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Parameter | Radius | Floating Point Numbers |  |
| Input Parameter | Central Location | 3D Vector |  |
| Input Parameter | Maximum Filter Quantity | Integer |  |
| Input Parameter | Filter Rules | Enumeration | Options: Default, Random, or Sort From Near to Far |
| Output Parameter | Filter Results | Entity List |  |

## **12. Query Entity by GUID**

![]()

**Node Functions**

Search for an Entity by GUID

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | GUID | GUID |  |
| Output Parameter | Entity | Entity |  |

# V. Faction Related

## **1. Query Entity Faction**

![]()

**Node Functions**

Search for Target Entity's Faction

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | Faction | Faction |  |

## **2. Query If Faction Is Hostile**

![]()

**Node Functions**

Check whether Faction 1 and Faction 2 are hostile

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Faction 1 | Faction |  |
| Input Parameter | Faction 2 | Faction |  |
| Output Parameter | Hostile | Boolean |  |

# VI. Player and Character Related

## **1. Query If Self Is in Combat**

![]()

**Node Functions**

Check whether the Entity associated with this Node Graph has entered battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | In Combat | Boolean |  |

## **2. Get Player Client Input Device Type**

![]()

**Node Functions**

Returns the Player's local input device type, as determined by the Interface mapping method

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Input Device Type | Enumeration | Includes keyboard/mouse, gamepad, touchscreen |

## **3. Get Current Character**

![]()

**Node Functions**

Returns the Character Entity currently controlled by this Player's client

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Character Entity | Entity |  |

## **4. Get Player Entity to Which the Character Belongs**

![]()

**Node Functions**

Returns the Player Entity that owns the Character Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Character Entity | Entity |  |
| Output Parameter | Affliated Player Entity | Entity |  |

## **5. Get List of Player Entities on the Field**

![]()

**Node Functions**

Returns a list of all Player Entities present in the scene

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Player Entity List | Entity List |  |

## **6. Get Character Entity of Specified Player**

![]()

**Node Functions**

Returns the Character Entity of the specified Player Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |
| Output Parameter | Character Entity | Entity |  |

## **7. Query GUID by Entity**

![]()

**Node Functions**

Search for the GUID of the specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity | Entity |  |
| Output Parameter | GUID | GUID |  |

## **8. Get Active Character of Specified Player**

![]()

**Node Functions**

Available only in Classic Mode. Returns the on-field character in the player's team

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |
| Output Parameter | Character Entity | Entity |  |

## **9. Check Classic Mode Character IDs**

![]()

**Node Functions**

Only available in the Classic Mode. Query the character ID of the Target Character. Check the appendix to see which Character it corresponds toClassic Mode Character ID List

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Character | Entity |  |
| Output Parameter | Character ID | Integer |  |

## **10.** **Get Player's Character List**

![]()

**Node Functions**

Returns a list of characters in the player's team. Available only in Classic Mode.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |
| Output Parameter | Character List | Entity List |  |

## **11. Get Player Movement Input**

![]()

**Node Functions**

Returns the Input Direction and Input Strength of the player's movement on the current client.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input Direction | Floating Point Numbers |  |
| Output Parameter | Input Strength | Floating Point Numbers |  |

## **12. Query Skill Variable Value**

![]()

**Node Functions**

Queries the corresponding Variable Value based on the Skill Variable Config ID.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Variable Config ID | Config ID |  |
| Output Parameter | Variable Value | Floating Point Numbers |  |

## **13. Get Current Key Behavior**

![]()

**Node Functions**

Returns all Key Behavior IDs on the current Key Behavior Log Panel and their corresponding entry times.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Behavior ID List | Integer List |  |
| Output Parameter | Entry Time List | Floating Point List |  |

## **14. Get Current Key Behavior (High Precision)**

![]()

**Node Functions**

Returns all Key Behavior IDs on the current Key Behavior Log Panel and their corresponding entry times. Due to floating-point precision issues, use this node if you require greater granularity for the entry times.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Behavior ID List | Integer List |  |
| Output Parameter | Entry Time List (s) | Integer List |  |
| Output Parameter | Entry Time List (ms) | Integer List |  |

## **15. Get Current Client Time**

![]()

**Node Functions**

Returns the current client time.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Client Time | Floating Point Numbers |  |

## **16. Get Current Client Time (High Precision)**

![]()

**Node Functions**

Returns the current client time. Due to floating-point precision issues, use this node if you need greater granularity for the client time.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Client Time (s) | Integer |  |
| Output Parameter | Client Time (ms) | Integer |  |

## **17. Query Whether Player Is Currently in Voice Chat**

![]()

**Node Functions**

Returns "Yes" when microphone input is detected from this player's client.

Note: This node only takes effect in multiplayer games (multiplayer test play, actual multiplayer play). It will not work in single-player games (single-player test play, actual single-player play).

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |
| Output Parameter | Currently in Voice Chat? | Boolean |  |

## **18. Get Skill Config ID by Skill Instance ID**

![]()

**Node Functions**

Returns the corresponding Skill Config ID based on the Skill Instance ID provided

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Instance ID | Integer |  |
| Output Parameter | Skill Config ID | Config ID |  |

## **19. Query Skill Instance List by Specified Slot**

![]()

**Node Functions**

Returns a list of all skill instances in the slot specified.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Slot | Enumeration |  |
| Output Parameter | Skill Instance ID List | Integer List |  |

## **20. Query Active Skill Instance List of Specified Slot**

![]()

**Node Functions**

Gets the skill instance currently in the foreground for the slot specified.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Slot | Enumeration |  |
| Output Parameter | Skill Instance ID List | Integer |  |

## **21. Query Skill Instance ID by Skill Slot and Skill Config ID**

![]()

**Node Functions**

Returns the corresponding skill instance based on the skill slot and Skill Config ID provided.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Slot | Enumeration |  |
| Input Parameter | Skill Config ID | Config ID |  |
| Output Parameter | Skill Instance ID List | Integer |  |

# VII. Attachment Points

## **1. Get Target Attachment Point Rotation**

![]()

**Node Functions**

Returns the Rotation of the specified Attachment Point on the Target Entity.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Attachment Point Name | String |  |
| Output Parameter | Attachment Point Rotation | 3D Vector |  |

# VIII. Triggers

## **1. Get All Entities Within the Collision Trigger**

![]()

**Node Functions**

Returns all Entities within the Collision Trigger corresponding to a specific ID in the Collision Trigger Component on the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Trigger ID | Integer |  |
| Output Parameter | Entity List | Entity List |  |

# IX. Rays

## **1. Get Ray Detection Result**

![]()

**Node Functions**

Returns the first Target or On-Hit Location that meets the Filter criteria, ordered from nearest to farthest along the ray

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Detect Initiator Entity | Entity |  |
| Input Parameter | Launch Location | 3D Vector |  |
| Input Parameter | Launch Direction | 3D Vector |  |
| Input Parameter | Max Ray Length | Floating Point Numbers |  |
| Input Parameter | Faction Filter | Enumeration |  |
| Input Parameter | Entity Type Filter | Enumeration List | Includes Stage, Object, Player, Character, Creation |
| Input Parameter | Hit Layer Filter | Enumeration List | Options: Hurtbox, Scene, and Object Self-Collision |
| Output Parameter | On-Hit Location | 3D Vector |  |
| Output Parameter | On-Hit Entity | Entity |  |

# X. Scanning

1.

## Get All Valid Entities That Are Scannable by Scan Component

![]()

**Node Functions**

Returns all Units carrying a Scan Component whose Filter returns True, regardless of the Unit's scannable status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Object List | Entity List |  |

2.

## Get Entity Currently Scanned by Scan Component

![]()

**Node Functions**

Returns Entities currently detected by the Scan Component; these are Entities in the Active State

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Corresponding Entity | Entity |  |
| Output Parameter | Scan Tag Config ID | Config ID |  |

3.

## Get Entity's Current Active Scan Tags

![]()

**Node Functions**

Returns the Target Entity's Current Active Scan Tags

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | Scan Tag Config ID | Config ID |  |

## **4. Get Entity's Scan Status**

![]()

**Node Functions**

Get Entity Scan Status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | Scan Status | Enumeration | Options: Invisible, Current Scan Target, Candidate Target, Criteria Not Met |

# **XI**. Dictionary

## **1. Query If Dictionary Contains Specific Key**

![]()

**Node Functions**

Check whether the specified Dictionary contains the specified Key

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Key | Generic |  |
| Output Parameter | Include | Boolean |  |

## **2. Query If Dictionary Contains Specific Value**

![]()

**Node Functions**

Check whether the specified Dictionary contains the specified Value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Value | Generic |  |
| Output Parameter | Include | Boolean |  |

## **3. Check Dictionary Length**

![]()

**Node Functions**

Query the number of Key-Value Pairs in the Dictionary

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Length | Integer |  |

## **4. Get List of Keys From Dictionary**

![]()

**Node Functions**

Returns a list of all Keys in the Dictionary. Because Key-Value Pairs are unordered, the Keys may not be returned in insertion order

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Key List | Generic |  |

## **5. Get List of Values From Dictionary**

![]()

**Node Functions**

Returns a list of all Values in the Dictionary. Because Key-Value Pairs are unordered, the Values may not be returned in insertion order

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Value List | Generic |  |

## **6. Query Dictionary Value by Key**

![]()

**Node Functions**

Query the corresponding Value in the Dictionary by Key. If the Key does not exist, returns the type's default value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Key | Generic |  |
| Output Parameter | Value | Generic |  |

# **XII**. Unit Status

## **1. Whether the Entity has the Specified Unit Status**

![]()

**Node Functions**

Check whether the Target Entity has the specified Unit Status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Unit Status | Config ID |  |
| Output Parameter | Has the Status | Boolean |  |

Operation Nodes

1

Explain

---

# Query Nodes

# I. Skills

## **1.** Get the Complex Creation's Current Using Skill

![](./Genshin Impact Miliastra Wonderland_ General Guide6_files/9717a7ba-5519-4965-a091-6b6fdacb7cc7.png)

**Node Functions**

Return to the ID of the Skill currently being cast by the current Complex Creation

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Skill ID | Integer |  |

## **2. Query Skill Variable Value**

![](./Genshin Impact Miliastra Wonderland_ General Guide6_files/8c420ec9-05e8-495d-9c30-07a40fe25e0b.png)

**Node Functions**

Returns the corresponding variable value based on Skill Variable Config ID

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Variable Config ID | Config ID |  |
| Output Parameter | Variable Value | Floating Point Numbers |  |

# II. List Operations

## **1. Get Corresponding Value From List**

![]()

**Node Functions**

Returns the value at the specified ID in the List. IDs start at 0

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | ID | Integer |  |
| Input Parameter | Data List | Generic |  |
| Output Parameter | Result | Generic |  |

## **2. Get List Length**

![]()

**Node Functions**

Returns the length of the list (number of elements)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input List | Generic |  |
| Output Parameter | Length | Integer |  |

## **3. Get Maximum Value From List**

![]()

**Node Functions**

Applies only to Floating Point Number or Integer lists; returns the maximum value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | List | Generic |  |
| Output Parameter | Maximum Value | Generic |  |

## **4. Get Minimum Value From List**

![]()

**Node Functions**

Applies only to Floating Point Number or Integer lists; returns the minimum value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | List | Generic |  |
| Output Parameter | Minimum Value | Generic |  |

## **5. Get Ray Filter Type List**

![]()

**Node Functions**

Assembles the required Ray Filter types into a List. Available filters include Hurtbox, Scene, and Object Self-Collision

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | List | Enumeration List |  |

## **6. Get Entity Type List**

![]()

**Node Functions**

Assembles the required Entity types into a List. Types include Stages, Objects, Players, Characters, and Creations

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | List | Enumeration List |  |

## **7. List Includes This Value**

![]()

**Node Functions**

Returns whether the list contains the specified value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Value | Generic |  |
| Input Parameter | List | Generic |  |
| Output Parameter | Result | Boolean |  |

# III. Custom Variables

## **1. Get Custom Variable**

![]()

**Node Functions**

Returns the value of the specified Custom Variable from the Target Entity

If the variable does not exist, returns the type's default value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Variable Name | String |  |
| Output Parameter | Variable Value | Generic |  |

# IV. Preset Status

## **1. Get Preset Status**

![]()

**Node Functions**

Returns the Preset Status value of the specified Entity. Returns 0 if the Entity does not have the specified Preset Status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity | Entity |  |
| Input Parameter | Preset Status Index | Integer |  |
| Output Parameter | Preset Status Value | Integer |  |

# V. Entity-Related

## **1. Check the preset status value of the complex creation**

![]()

**Node Functions**

Query the Preset Status Value of the Target Creation under the corresponding Preset Status index

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Creation | Entity |  |
| Input Parameter | Preset Status Index | Integer |  |
| Output Parameter | Preset Status Value | Integer |  |

## **2. Query if Entity Is on the Field**

![]()

**Node Functions**

Check whether the specified Entity is present

Note that Character Entities are still considered present even when Downed

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | On the Field | Boolean |  |

## **3. Get Unit Attack Target**

![]()

**Node Functions**

Returns the Target Entity that the Unit Entity is currently attacking

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Unit Entity | Entity |  |
| Output Parameter | Attack Target Entity | Entity |  |

## **4. Get Target Attachment Point Location**

![]()

**Node Functions**

Returns the Location of the specified Attachment Point on the Target Entity.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Attachment Point Name | String |  |
| Output Parameter | Attachment Point Location | 3D Vector |  |

## **5. Get Target Attachment Point Rotation**

![]()

**Node Functions**

Returns the Rotation of the specified Attachment Point on the Target Entity.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Attachment Point Name | String |  |
| Output Parameter | Attachment Point Rotation | 3D Vector |  |

## **6. Get Entity's Type**

![]()

**Node Functions**

Returns the type of the specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | Entity Type | Enumeration |  |

## **7. Get Entity Location**

![]()

**Node Functions**

Returns the Location of the specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity | Entity |  |
| Output Parameter | Location | 3D Vector |  |

## **8. Get Entity Rotation**

![]()

**Node Functions**

Returns the Rotation of the specified Entity in Euler Angles

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity | Entity |  |
| Output Parameter | Rotate | 3D Vector |  |

## **9. Get Creation's Current Target**

![]()

**Node Functions**

Return to the specified Creation's current target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Creation | Entity |  |
| Output Parameter | Target Entity | Entity |  |

## **10. Get Self Entity**

![]()

**Node Functions**

Returns the Entity associated with this Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Self Entity | Entity |  |

## **11. Get Sub-Entity List**

![]()

**Node Functions**

Return to the Target Entity's Sub-Entity List

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | Sub-Entity List | Entity List |  |

## **12. Filter Entity List Within Square Range**

![]()

**Node Functions**

Filters Entities within a square range according to specified rules and a maximum count, and returns a list of Entities that meet the conditions

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Width | Floating Point Numbers |  |
| Input Parameter | Height | Floating Point Numbers |  |
| Input Parameter | Length | Floating Point Numbers |  |
| Input Parameter | Central Location | 3D Vector |  |
| Input Parameter | Maximum Filter Quantity | Integer |  |
| Input Parameter | Filter Rules | Enumeration | Options: Default, Random, or Sort From Near to Far |
| Output Parameter | Filter Results | Entity List |  |

## **13. Filter Entity List Within Spherical Range**

![]()

**Node Functions**

Filters Entities within a spherical range according to specific rules and a maximum count, and returns a list of Entities that meet the conditions

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Parameter | Radius | Floating Point Numbers |  |
| Input Parameter | Central Location | 3D Vector |  |
| Input Parameter | Maximum Filter Quantity | Integer |  |
| Input Parameter | Filter Rules | Enumeration | Options: Default, Random, or Sort From Near to Far |
| Output Parameter | Filter Results | Entity List |  |

## **14. Query Entity by GUID**

![]()

**Node Functions**

Search for an Entity by GUID

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | GUID | GUID |  |
| Output Parameter | Entity | Entity |  |

## **15. Get Player Entity to Which the Character Belongs**

![]()

**Node Functions**

Returns the Player Entity that owns the Character Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Character Entity | Entity |  |
| Output Parameter | Affiliated Player Entity | Entity |  |

## **16. Get List of Player Entities on the Field**

![]()

**Node Functions**

Returns a list of all Player Entities present in the scene

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Player Entity List | Entity List |  |

## **17. Get Active Character of Specified Player**

![]()

**Node Functions**

Available only in the Classic Mode. Obtains the on-field character in the player's team

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |
| Output Parameter | Character Entity | Entity |  |

## **18. Get Player's Character List**

![]()

**Node Functions**

Available in the Classic Mode only. Returns a list of all characters in the Player's team

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |
| Output Parameter | Character List | Entity List |  |

## **19. Query GUID by Entity**

![]()

**Node Functions**

Returns the GUID of the specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity | Entity |  |
| Output Parameter | GUID | GUID |  |

## **20. Check Class Mode Character ID**

![]()

**Node Functions**

Available in Classic Mode only. Returns the Character ID of the Target Character, and can be used to look up the corresponding character in the Appendix Classic Mode Character IDs

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Character | Entity |  |
| Output Parameter | Character ID | Integer |  |

# VI. Faction-Related

## **1. Query Entity Faction**

![]()

**Node Functions**

Search for Target Entity's Faction

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | Faction | Faction |  |

## **2. Query If Faction Is Hostile**

![]()

**Node Functions**

Check whether Faction 1 and Faction 2 are hostile

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Faction 1 | Faction |  |
| Input Parameter | Faction 2 | Faction |  |
| Output Parameter | Hostile | Boolean |  |

# VII. Tags

## **1. Get Entity List by Unit Tag**

![]()

**Node Functions**

Returns a list of all Entities in the scene that carry this Unit Tag

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Unit Tag Index | Integer |  |
| Output Parameter | Entity List | Entity List |  |

## **2. Get Entity's Unit Tag List**

![]()

**Node Functions**

Returns a list of all Unit Tags carried by the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | List | Integer List |  |

# VIII. General

## **1. Get Local Variable**

![]()

**Node Functions**

Returns the value of a specific local variable

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Variable Name | String |  |
| Output Parameter | Variable Value | Generic |  |

# IX. Custom Aggro

## **1. Query If Specified Entity Is in Combat**

![]()

**Node Functions**

Available only in Custom Aggro Mode

Check whether the specified Entity has entered battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Output Parameter | In Combat | Boolean |  |

## **2. Get the Aggro List of the Specified Entity**

![]()

**Node Functions**

Available only in Custom Aggro Mode

Get Specified Entity's Aggro List

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Specified Entity | Entity |  |
| Output Parameter | Aggro List | Entity List |  |

## **3. Get the Aggro Target of the Specified Entity**

![]()

**Node Functions**

Available only in Custom Aggro Mode

Get Aggro Target of Specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Specified Entity | Entity |  |
| Output Parameter | Aggro Target | Entity |  |

# X. Triggers

## **1. Get All Entities Within the Collision Trigger**

![]()

**Node Functions**

Returns all Entities within the Collision Trigger corresponding to a specific ID in the Collision Trigger Component on the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Trigger ID | Integer |  |
| Output Parameter | Entity List | Entity List |  |

# XI. Ray

## **1. Get Ray Detection Result**

![]()

**Node Functions**

Returns the first Target or On-Hit Location that meets the Filter criteria, ordered from nearest to farthest along the ray

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Detection Initiator Entity | Entity |  |
| Input Parameter | Launch Location | 3D Vector |  |
| Input Parameter | Launch Direction | 3D Vector |  |
| Input Parameter | Max Ray Length | Floating Point Numbers |  |
| Input Parameter | Faction Filter | Enumeration |  |
| Input Parameter | Entity Type Filter | Enumeration List | Includes Stage, Object, Player, Character, Creation |
| Input Parameter | Hit Layer Filter | Enumeration List | Options: Hurtbox, Scene, and Object Self-Collision |
| Output Parameter | On-Hit Location | 3D Vector |  |
| Output Parameter | On-Hit Entity | Entity |  |

# XII. Dictionary

## **1. Query If Dictionary Contains Specific Key**

![]()

**Node Functions**

Check whether the specified Dictionary contains the specified Key

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Key | Generic |  |
| Output Parameter | Include | Boolean |  |

## **2. Query If Dictionary Contains Specific Value**

![]()

**Node Functions**

Check whether the specified Dictionary contains the specified Value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Value | Generic |  |
| Output Parameter | Include | Boolean |  |

## **3. Check Dictionary Length**

![]()

**Node Functions**

Query the number of Key-Value Pairs in the Dictionary

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Length | Integer |  |

## **4. Get List of Keys From Dictionary**

![]()

**Node Functions**

Returns a list of all Keys in the Dictionary. Because Key-Value Pairs are unordered, the Keys may not be returned in insertion order

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Key List | Generic |  |

## **5. Get List of Values From Dictionary**

![]()

**Node Functions**

Returns a list of all Values in the Dictionary. Because Key-Value Pairs are unordered, the Values may not be returned in insertion order

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Output Parameter | Value List | Generic |  |

## **6. Query Dictionary Value by Key**

![]()

**Node Functions**

Query the corresponding Value in the Dictionary by Key. If the Key does not exist, returns the type's default value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Key | Generic |  |
| Output Parameter | Value | Generic |  |

# **XIII**. Unit Status

## **1. Whether the Entity Has the Specified Unit Status**

![]()

**Node Functions**

Check whether the Target Entity has the specified Unit Status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Unit Status | Configuration ID |  |
| Output Parameter | Has the Status | Boolean |  |

Operation Nodes

1

Explain
