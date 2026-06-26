# Execution Nodes (Node Thực Thi)

# I. General (Cài đặt chung)

## **1. Continue Executing Previous Frame Behavior (Tiếp tục hành vi của khung hình trước)**

![](./Genshin Impact Miliastra Wonderland_ General Guide13_files/36707861-18aa-4157-94a8-ff389accd4b8.png)

**Node Functions (Chức năng Node)**

Nếu Chiến thuật (Tactic) được kích hoạt ở khung hình trước vẫn chưa hoàn thành, nó sẽ được tiếp tục thực thi cho đến khi kết thúc.

Nếu Kỹ năng (Skill) đã được thực thi ở khung hình trước, sẽ không có quá trình nào diễn ra thêm.

**Node Parameters (Tham số Node)**

| | | | |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| | | | |

## **2. Execute Skill (Thực thi Kỹ năng)**

![](./Genshin Impact Miliastra Wonderland_ General Guide13_files/0a741a39-5885-4614-ab09-8107e862a53b.png)

**Node Functions (Chức năng Node)**

Thực thi một kỹ năng thông qua Số ID của kỹ năng (Skill ID) được chỉ định.

**Node Parameters (Tham số Node)**

| | | | |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Execute (Thực thi) | Boolean (Luận lý) | |
| Input Parameter (Đầu vào) | Skill ID (Mã Kỹ năng) | Integer (Số nguyên) | |

# II. Tactics

## **1. Tactic: Ground Confrontation**

![]()

![]()

**Node Functions**

The Creation executes a Paving Standoff. It uses four-direction Motion Tactics, with five directions: idle/forward/backward/left/right. Use this to simulate a sustained face-off with the Player.

You can use probability settings to create motion behaviors such as moving left and right around the Player, or preferring to move forward and avoiding moving backward. It also includes settings for adjusting distance to the Player and for obstacle avoidance.

Essentially, it just decides a direction; there is no specific Target Point

Execution Conditions:



Requires the unit or the target to be within the Territory Range



If *Reachable via Pathfinding* is enabled and the unit is not airborne, Tactics will end when Pathfinding fails

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean |  |
| Input Parameter | Inner Radius of Confrontation Distance | Floating Point Numbers |  |
| Input Parameter | Outer Radius of Confrontation Distance | Floating Point Numbers |  |
| Input Parameter | Direction Change Interval | Floating Point Numbers | Transition Time when changing directions. Default is 0. Each time the direction changes, the Creation stays still for the configured time, then switches to the new direction  Switching from another direction to Rest, or from Rest to another direction, does not count as an direction change |
| Input Parameter | Minimum Rest Interval | Floating Point Numbers |  |
| Input Parameter | Maximum Rest Interval | Floating Point Numbers |  |
| Input Parameter | Is Pathfinding Always Achievable? | Boolean |  |
| Input Parameter | Whether Restricted by Territory | Boolean | If set to Yes and there are no valid points within the Territory, this Tactic will end immediately |
| Input Parameter | Cancel Trigger Weight by Movement | Floating Point Numbers |  |
| Input Parameter | Forward Movement Weight | Floating Point Numbers | Affects Motion weights only in the Normal Mode. Even if you set the direction's weight to 0, the character may still move in that direction due to obstacle avoidance or unexpected conditions |
| Input Parameter | Backward Movement Weight | Floating Point Numbers | Same as above |
| Input Parameter | Leftward Movement Weight | Floating Point Numbers | Same as above |
| Input Parameter | Rightward Movement Weight | Floating Point Numbers | Same as above |
| Input Parameter | Lateral Obstacle Avoidance Distance | Floating Point Numbers | If the configured value is less than 0, the obstacle avoidance function will not run |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can Skill be Interrupted | Boolean | Default: No |

## **2. Tactic: Ground Escape**

![]()

![]()

**Node Functions**

The Creation executes a Paving Escape, a tactic for fleeing from the Target. It attempts to turn its back to the Target and move farther away.

Allows you to configure multiple segments of Escape Motion. Each segment/run calculates one escape point.

Execution Conditions:



When the Creation is not in CD, and is inside its Territory, it will trigger fleeing behavior once their distance to the Target is less than *Flee Trigger Distance*

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean |  |
| Input Parameter | Escape Trigger Distance | Floating Point Numbers |  |
| Input Parameter | Movement Speed | Enumeration | Walk and Run |
| Input Parameter | Maximum Escape Angle | Floating Point Numbers | Uses twice the absolute value of the configured value as the actual flee point selection range |
| Input Parameter | Minimum Escape Segments | Integer |  |
| Input Parameter | Maximum Escape Segments | Integer |  |
| Input Parameter | Minimum Escape Distance | Floating Point Numbers |  |
| Input Parameter | Maximum Escape Distance | Floating Point Numbers |  |
| Input Parameter | Escape Trigger CD | Floating Point Numbers |  |
| Input Parameter | Clear Aggro and Cancel Tactic After Countdown | Floating Point Numbers | If the value is less than 0, the Tactic will not be executed.  Otherwise, the timer starts from when the Tactics are entered. If it times out, battle will be forcibly ended.  After the Tactics execution ends, battle will be immediately ended |
| Input Parameter | Whether Restricted by Territory | Boolean | If set to Yes and there are no valid points within the Territory, this Tactic will end immediately |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can Skill be Interrupted | Boolean | Default: No |

## **3. Tactic: Ground Idle Roaming**

![]()

**Node Functions**

The Creation executes a Paving Roam, walking randomly within the AoE

Execution Conditions:



Affected by *Creation Underclock*, Creations that are too far from the Character will not enter this Tactic



Select a suitable Target Point

Point Selection Rules:



Unlike most tactics, the point-selection logic for the *Paving Roam* tactic runs when it is **potentially** possible to execute *Paving Roam*, but before you Enter it

Because choosing the right Target Point is one of the requirements for entering this Tactic



Upon entering a Tactic, execute the Motion quest immediately. Keep it running until the Motion stops (when you reach the destination or hit an obstacle). Then apply the CD and exit the Tactic



If a Creation's current Location is already outside the *Roaming Radius* AoE, the *Paving Roam* Tactic selects a point in the direction from the current location toward the Spawn Point, at a distance equal to the *Roaming Radius*, as the Target Point



If Pathfinding is supported, it will be used to check whether the Target Point is valid

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean |  |
| Input Parameter | Speed | Enumeration | Walk and Run |
| Input Parameter | Idle Roaming Radius | Floating Point Numbers | Farthest distance you can roam from the Spawn Point |
| Input Parameter | Minimum Idle Roaming Interval | Floating Point Numbers | The cooldown time between roaming behaviors. Each time roaming ends, the system randomly selects a CD between [Minimum Idle Roaming Interval, Maximum Idle Roaming Interval] and uses it as the new CD. This Tactic will not be executed during cooldown periods |
| Input Parameter | Maximum Idle Roaming Interval | Floating Point Numbers |  |
| Input Parameter | Single Minimum Idle Roaming Distance | Floating Point Numbers | Roam Distance from Current Point |
| Input Parameter | Single Maximum Idle Roaming Distance | Floating Point Numbers | Roam Distance from Current Point |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can Skill be Interrupted | Boolean | Default: No |

## **4. Tactic: Ground Pursuit**

![]()

![]()

**Node Functions**

The Creation executes a Paving Pursuit

Target Pursuit Tactic automatically selects a suitable location near the Target as the Target Point

Execution Conditions:

[Required]

1.

Has a Target

2.

Not airborne

3.

This unit or the target is within the Territory Range

[Meet any one of the Conditions]

1.

If this unit is not currently in this Tactic and the distance between the unit and the Target is within [*Minimum Pursuit Trigger Distance*, *Maximum Pursuit Trigger Distance*], the unit will enter this Tactic

2.

When already in the Tactic, the unit will continue to execute the Tactic only if the distance between this unit and the Target is greater than the *Stop Pursuit Distance*

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Type** | **Type** | **Description** |
| Input Parameter | Execute | Boolean |  |
| Input Parameter | Minimum Pursuit Trigger Distance | Floating Point Numbers |  |
| Input Parameter | Maximum Pursuit Trigger Distance | Floating Point Numbers |  |
| Input Parameter | Stop Pursuit Distance | Floating Point Numbers |  |
| Input Parameter | Outer Ring Pursuit Speed | Enumeration | Walk and Run |
| Input Parameter | Inner Ring Radius | Floating Point Numbers | Inner Ring Boundary Radius |
| Input Parameter | Inner Ring Pursuit Speed | Enumeration | Walk and Run |
| Input Parameter | Single Pursuit Duration | Floating Point Numbers | If value less than 0, do not execute the Tactic |
| Input Parameter | Tactical Instance CD | Floating Point Numbers |  |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can Skill be Interrupted | Boolean | Default: No |

## **5. Tactic: Stand Still**

![]()

**Node Functions**

The Creation executes the Idle behavior

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean |  |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can Skill be Interrupted | Boolean | Default: No |

## **6. Tactic: Return to Spawn Point After Leaving Battle**

![]()

**Node Functions**

The Creation returns to the Spawn Point after leaving battle

A tactic that makes a unit return to the initial point when leaving battle. While this tactic is running, the Aggro system is disabled and will not be re-enabled until the tactic ends.

Execution Conditions:

3.

This is only available in the pre-battle and out-of-battle phases. Place it first in your pre-battle Tactics so the Aggro system switches to it as soon as the battle ends

Select Target Points:

The Target Point is selected on the frame you enter the Tactic, and it will not be edited while the Tactic is being executed

Check the following conditions in order. When a condition is met, set the Target Point based on that item.

a.

When the [Execute a Patrol] Tactic is performed and *Set End Point to Spawn Point* is enabled, the new Spawn Point will be used as the Target Point

b.

Set the Spawn Point as the Target Point

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean |  |
| Input Parameter | Movement Speed | Enumeration |  |
| Input Parameter | Teleport Back to Spawn Point? | Boolean |  |
| Input Parameter | Force Teleport Trigger Distance | Floating Point Numbers | Prerequisite: Set *Teleport Back to Spawn Point* to Yes  When this unit's distance from the Spawn Point is greater than or equal to the configured distance, a teleport will be forcibly triggered |
| Input Parameter | Force Teleport Trigger Time | Floating Point Numbers | Prerequisite: *Teleport Back to the Spawn Point* must be set to Yes  If the Tactic duration exceeds the configured timer and this unit has not yet returned to the Spawn Point, a teleport will be forcibly triggered |
| Input Parameter | Disable HP Recovery After Leaving Battle | Boolean |  |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can Skill be Interrupted | Boolean | Default: No |

## **7. Tactic: Rotate to the Target Entity**

![]()

**Node Functions**

The Creation rotates to face the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean |  |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Horizontal Rotation Angular Velocity | Floating Point Numbers |  |
| Input Parameter | Use Rotation Animation | Boolean |  |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can Skill be Interrupted | Boolean | Default: No |

## **8. Tactic: Rotate to the Specified Direction**

![]()

**Node Functions**

The Creation rotates to the Specified Orientation

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean |  |
| Input Parameter | Target Orientation | 3D Vector |  |
| Input Parameter | Horizontal Rotation Angular Velocity | Floating Point Numbers |  |
| Input Parameter | Use Rotation Animation? | Boolean |  |
| Input Parameter | Rotation Direction | Enumeration | Default: use the shortest angle  Clockwise  Counterclockwise |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can Skill be Interrupted | Boolean | Default: No |

## **9. Tactic: Rotate by Specified Angle**

![]()

**Node Functions**

The Creation rotates by the specified angle, and the Angular Velocity may have minor deviations during actual operation

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean |  |
| Input Parameter | Specified Angle | Floating Point Numbers |  |
| Input Parameter | Horizontal Rotation Angular Velocity | Floating Point Numbers | If set to a positive value, rotates clockwise;  if set to a negative value, rotates counterclockwise; |
| Input Parameter | Use Rotation Animation? | Boolean |  |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can Skill be Interrupted | Boolean | Default: No |

## **10. Tactic: Move to the Target Position**

![]()

**Node Functions**

The Creation moves to the Target Point

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean |  |
| Input Parameter | Target Position | 3D Vector |  |
| Input Parameter | Arrival Detection Range | Floating Point Numbers |  |
| Input Parameter | Movement Speed | Enumeration | Walk and Run |
| Input Parameter | Turn Speed | Floating Point Numbers |  |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can Skill be Interrupted | Boolean | Default: No |

## **11. Tactic: Move to the Target Entity**

![]()

**Node Functions**

The Creation moves to the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean |  |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Arrival Detection Range | Floating Point Numbers | If the Distance to the Target Entity is less than or equal to the configured value, it is considered arrived |
| Input Parameter | Movement Speed | Enumeration | Walk and Run |
| Input Parameter | Turn Speed | Floating Point Numbers |  |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can Skill be Interrupted | Boolean | Default: No |

## **12. Tactic: Execute Patrol**

![]()

**Node Functions**

A tactic setting where the Creation executes its patrol , using its configured Patrol Template to drive its motion.

Execution Conditions:

4.

The Creation is configured with a Patrol Template

5.

Patrol Template referenced by Tactics; the referenced path data is not empty

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean |  |
| Input Parameter | Patrol Template ID | Integer |  |
| Input Parameter | Start From the Nearest Waypoint? | Boolean |  |
| Input Parameter | Set End Point as Spawn Point | Boolean | Affects the *Return to Spawn Point After Leaving Battle* Tactic |
| Input Parameter | Tactical Context | String |  |
| Input Parameter | Can Skill be Interrupted | Boolean | Default: No |

Operation Nodes

Flow Control Node

1

Explain

---

# Execution Nodes

# I. General

## **1. Switch to self execution status**

![](./Genshin Impact Miliastra Wonderland_ General Guide18_files/2ed0eba9-5205-499d-ad61-6af180a30e98.png)

**Node Functions**

Once the execution conditions are met, run the Status Node Graph linked to this config ID

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Execute | Boolean |  |
| Input Parameter | Status Node Graph Configuration ID | Config ID | Config ID for the Creation Status Node Graph |
| Input Parameter | Autonomous Logic Parameter ID | Integer |  |

Operation Nodes

Flow Control Node

1

Explain

---

# Execution Nodes

# I. Character Skills

## **1. Traverse Entity List**

![](./Genshin Impact Miliastra Wonderland_ General Guide3_files/a1764fe9-e666-4ed5-8b35-6c8cec9f5a72.png)

**Node Functions**

Iterates through each Entity in the input Entity List

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity List | Entity List |  |
| Output Parameter | Current Entity | Entity |  |

## **2. Play Timed Effects**

![](./Genshin Impact Miliastra Wonderland_ General Guide3_files/9d9f99a2-538e-4c71-8891-36cc655c8bfe.png)

**Node Functions**

Plays Timed Effects at the specified World Location

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Special Effects Asset Configuration ID | Config ID |  |
| Input Parameter | Location | 3D Vector |  |
| Input Parameter | Rotate | 3D Vector |  |
| Input Parameter | Zoom Multiplier | Floating Point Numbers |  |
| Input Parameter | Play Default Sound Effects? | Boolean |  |

## **3. Fixed-Point Projectile Launch**

![]()

**Node Functions**

Spawns a Local Projectile at the specified Location in the World Coordinate System

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Projectile's Prefab ID | Prefab ID |  |
| Input Parameter | Create Location | 3D Vector |  |
| Input Parameter | Create Rotation | 3D Vector |  |
| Input Parameter | Track Target | Entity |  |
| Input Parameter | Projectile Faction | Faction |  |

## **4. Fixed-Point Displacement**

![]()

**Node Functions**

Moves from the current Location to the Target Location

Supports configuring movement duration and speed; if both are small, the movement may not reach the Target Location

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Displacement Duration | Floating Point Numbers |  |
| Input Parameter | Displacement Attenuation Duration | Floating Point Numbers |  |
| Input Parameter | Displacement Speed | Floating Point Numbers |  |
| Input Parameter | Displacement Target Location | 3D Vector |  |
| Input Parameter | Terminate Displacement on Collision | Boolean |  |

## **5. Recover Character's HP**

![]()

**Node Functions**

Initiates a one-time HP restoration for the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Recovery Amount | Floating Point Numbers |  |
| Input Parameter | Ignore Recovery Adjustment Effect | Boolean |  |
| Input Parameter | Aggro Multiplier for This Healing | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Healing | Integer |  |

## **6. Camera Orientation Detection Data**

![]()

**Node Functions**

Casts a ray from the Camera to the emission Location and returns the Rotation and Location of valid Targets along the path

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Type | Enumeration |  |
| Input Parameter | Launch Location | 3D Vector |  |
| Input Parameter | Nearest Distance | Floating Point Numbers |  |
| Input Parameter | Furthest Distance | Floating Point Numbers |  |
| Output Parameter | Target Rotation | 3D Vector |  |
| Output Parameter | Target Location | 3D Vector |  |

## **7. Force Exit Aiming State**

![]()

**Node Functions**

When the character is in the aiming state, they will be forced to exit the aiming state.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
|  |  |  |  |

## **8. Set Own Attack Target**

![]()

**Node Functions**

Sets the Target Entity as its Attack Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Whether to Turn Immediately | Boolean |  |

## **9. Trigger Hitbox at Specific Location**

![]()

![]()

![]()

![]()

**Node Functions**

Initiates a Hitbox Attack at the specified Location in the World Coordinate System, with configurable attack parameters

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Location | 3D Vector |  |
| Input Parameter | Rotate | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Numbers |  |
| Input Parameter | Damage Increment | Floating Point Numbers |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Hitbox Type | Enumeration |  |
| Input Parameter | Scale of Cuboid Hitbox | 3D Vector |  |
| Input Parameter | Radius of Sphere Hitbox | Floating Point Numbers |  |
| Input Parameter | Height of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Sector Angle of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Sector Radius of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Inner Radius of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Detection Direction of Sector Hitbox | Enumeration |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Numbers |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Numbers |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Numbers |  |
| Input Parameter | On-Hit Scene Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Special Effects Zoom | Floating Point Numbers |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Numbers |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Numbers |  |

## **10. Add Unit Status**

![]()

**Node Functions**

Applies the Unit Status defined by the configuration ID to the Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Application Target | Entity |  |
| Input Parameter | Stacks | Integer |  |
| Input Parameter | Unit Status Config ID | Config ID |  |

## **11. Notify Server Node Graph**

![]()

**Node Functions**

Notifies the Server Node Graph; supports up to three String parameters

At runtime, forwards logic to the Server Node Graph and triggers the [On Skill Node Call] Event on the Server Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | String 1 | String |  |
| Input Parameter | String 2 | String |  |
| Input Parameter | String 3 | String |  |

## **12. Player Turning**

![]()

**Node Functions**

Turns the Player using the configured turning mode

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Turning Mode | Enumeration | Includes: Target then Input, Input Direction, Target Direction, Target then Camera, Camera Direction, Input then Target |

## **13. Player Turns to Face Set Direction**

![]()

**Node Functions**

Turns the Player toward the direction specified by the 3D Vector configuration

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Orientation | 3D Vector |  |

## **14. Set Attack Weight**

![]()

**Node Functions**

You can set the weight of the current attack target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Current Attack Target Weight | Floating Point Numbers |  |
| Input Parameter | Forcibly Select a Target Once | Boolean |  |

## **15. Remove Unit Status**

![]()

**Node Functions**

Removes the Unit Status corresponding to the specified configuration ID from the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Removal Target | Entity |  |
| Input Parameter | Unit Status Config ID | Config ID |  |

## **16. Remove Specified Character Disruptor Device**

![]()

**Node Functions**

Removes the specified type of Character Disruptor Device

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Disruptor Device Type | Enumeration | Includes: Force Field Device, Ejector, and Traction Device |

## **17. Trigger Hitbox at Specific Location**

![]()

![]()

![]()

![]()

**Node Functions**

Initiates a Hitbox Attack at the specified Attachment Point, with configurable attack parameters

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Attachment Point Name | String |  |
| Input Parameter | Attachment Point Offset | 3D Vector |  |
| Input Parameter | Attachment Point Rotation | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Numbers |  |
| Input Parameter | Damage Increment | Floating Point Numbers |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Hitbox Type | Enumeration |  |
| Input Parameter | Scale of Cuboid Hitbox | 3D Vector |  |
| Input Parameter | Radius of Sphere Hitbox | Floating Point Numbers |  |
| Input Parameter | Height of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Sector Angle of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Sector Radius of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Inner Radius of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Detection Direction of Sector Hitbox | Enumeration |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Numbers |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Numbers |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Numbers |  |
| Input Parameter | On-Hit Scene Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Special Effects Zoom | Floating Point Numbers |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Numbers |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Numbers |  |
| Input Parameter | Hit Vertical Impulse | String List |  |

## **18. Reset Skill Target**

![]()

**Node Functions**

Resets the Skill Target and reruns the Skill selection logic to choose a new Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
|  |  |  |  |

## **19. Trigger Rectangular Hitbox at Specific Location**

![]()

![]()

**Node Functions**

Initiate a rectangular hitbox at the specified position in the world coordinate system, and you can set various parameters for this attack.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Location | 3D Vector |  |
| Input Parameter | Rotate | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Numbers |  |
| Input Parameter | Damage Increment | Floating Point Numbers |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Scale of Cuboid Hitbox | 3D Vector |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Numbers |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Numbers |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Numbers |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Numbers |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Integer |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Numbers |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Numbers |  |

## **20. Trigger Spherical Hitbox at Specific Location**

![]()

![]()

**Node Functions**

Initiate a spherical hitbox at the specified position in the world coordinate system, and you can set various parameters for this attack.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Location | 3D Vector |  |
| Input Parameter | Rotate | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Numbers |  |
| Input Parameter | Damage Increment | Floating Point Numbers |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Radius of Sphere Hitbox | Floating Point Numbers |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Numbers |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Numbers |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Numbers |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Numbers |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Numbers |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Numbers |  |

## **21. Trigger Sector Hitbox at Specific Location**

![]()

![]()

**Node Functions**

Initiate a sector hitbox at the specified position in the world coordinate system, and you can set various parameters for this attack.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Location | 3D Vector |  |
| Input Parameter | Rotate | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Numbers |  |
| Input Parameter | Damage Increment | Floating Point Numbers |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Height of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Sector Angle of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Sector Radius of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Inner Radius of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Detection Direction of Sector Hitbox | Enumeration |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Numbers |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Numbers |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Numbers |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Numbers |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Numbers |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Numbers |  |

## **22. Trigger Rectangular Hitbox at Specified Attachment Point**

![]()

![]()

**Node Functions**

Initiate a rectangular hitbox at the specified attachment point, and you can set various parameters for this attack.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Attachment Point Name | String List |  |
| Input Parameter | Attachment Point Offset | 3D Vector |  |
| Input Parameter | Attachment Point Rotation | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Numbers |  |
| Input Parameter | Damage Increment | Floating Point Numbers |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Scale of Cuboid Hitbox | 3D Vector |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Numbers |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Numbers |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Numbers |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Numbers |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Numbers |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Numbers |  |

## **23. Trigger Spherical Hitbox at Specified Attachment Point**

![]()

![]()

**Node Functions**

Initiate a spherical hitbox at the specified attachment point, and you can set various parameters for this attack.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Attachment Point Name | String List |  |
| Input Parameter | Attachment Point Offset | 3D Vector |  |
| Input Parameter | Attachment Point Rotation | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Numbers |  |
| Input Parameter | Damage Increment | Floating Point Numbers |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Radius of Sphere Hitbox | Floating Point Numbers |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Numbers |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Numbers |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Numbers |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Numbers |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Numbers |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Numbers |  |

## **24. Trigger Sector Hitbox at Specified Attachment Point**

![]()

![]()

![]()

**Node Functions**

Initiate a sector hitbox at the specified attachment point, and you can set various parameters for this attack.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Attachment Point Name | String List |  |
| Input Parameter | Attachment Point Offset | 3D Vector |  |
| Input Parameter | Attachment Point Rotation | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Numbers |  |
| Input Parameter | Damage Increment | Floating Point Numbers |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Height of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Sector Angle of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Sector Radius of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Inner Radius of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Detection Direction of Sector Hitbox | Enumeration |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Numbers |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Numbers |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Numbers |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Numbers |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Numbers |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Numbers |  |

## **25. Interrupt Current Skil**l

![]()

**Node Functions**

Interrupts the skill currently being cast by the character

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
|  |  |  |  |

## **26. Set Skill Variable**

![]()

**Node Functions**

Sets the value of the specified skill variable

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Variable Config ID | Config ID |  |
| Input Parameter | Set Value | Floating Point Numbers | The modified value |

## **27. Increase Skill Variable Value**

![]()

**Node Functions**

Increases the value of the specified skill variable. The increment can be a negative value.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Variable Config ID | Config ID |  |
| Input Parameter | Set Value | Floating Point Numbers | Modified Value = Original Value + Increase Value |

## **28. Character Blink**

![]()

**Node Functions**

Makes the character blink to the target position, with the direction they are facing post-blink adjustable. The maximum blink distance is 200 meters.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Location | 3D Vector |  |
| Input Parameter | Target Orientation | 3D Vector |  |

## **29. Add Key Behavior**

![]()

**Node Functions**

Adds a key behavior with the corresponding ID to the Key Behavior Log Panel, and records the current time along with it. The maximum number of key behaviors that can be recorded is 20.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Key Behavior ID | Integer |  |

## **30. Clear Key Behavior Log Panel**

![]()

**Node Functions**

Clears all recorded key behaviors from the Key Behavior Log Panel.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
|  |  |  |  |

## **31. Cast Skill From Specified Slot**

![]()

**Node Functions**

Makes the character cast the skill corresponding to the specified Skill Instance ID.

For the button to be usable, the skill must be bound to a button and currently be in the foreground

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Instance ID | Integer |  |
| Input Parameter | Check Key Availability | Boolean | Yes: The skill will only be cast when the current button is usable.  No: The skill will be cast regardless of whether the current button is usable. |

## **32. Cast Skill From Specified Slot**

![]()

**Node Functions**

Makes the character cast the skill that is currently in the foreground for the corresponding skill slot.

For the button to be usable, the skill must be bound to a button and currently be in the foreground

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Slot | Enumeration |  |
| Input Parameter | Check Key Availability | Boolean | Yes: The skill will only be cast when the current button is usable.  No: The skill will be cast regardless of whether the current button is usable. |

# II. General

## **1. Set Local Variable**

![]()

**Node Functions**

Sets the value of a local variable

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Variable Name | String |  |
| Input Parameter | Variable Value | Generic |  |

## **2. Break Loop**

![]()

**Node Functions**

Break out of a Finite Loop. The output pin must connect to the [Break Loop] input parameter of the [Finite Loop] Node

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
|  |  |  |  |

## **3. Finite Loop**

![]()

**Node Functions**

From the [Loop Start Value] to the [Loop End Value], the loop iterates, incrementing the Integer by 1 each time. On each iteration, it executes the Nodes connected to [Loop Body]. After a full iteration, it executes the Nodes connected to [Loop Complete].

Use [Break Loop] to end the iteration early

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Loop Start Value | Integer |  |
| Input Parameter | Loop Termination Value | Integer |  |
| Output Parameter | Current Loop Value | Integer |  |

# III. Custom Aggro

## **1. Set the Aggro Value of the Specified Entity Proportionally**

![]()

**Node Functions**

Available only in Custom Aggro Mode

Set the aggro value of the target entity for the specified aggro owner proportionally.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Aggro Owner Entity | Entity |  |
| Input Parameter | Aggro Value Ratio | Floating Point Numbers |  |

## **2. Transfer the Aggro Value of the Specified Entity Proportionally**

![]()

**Node Functions**

Available only in Custom Aggro Mode

Transfers a percentage of Aggro on the Aggro Owner from the Source Entity to the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Transfer Target Entity | Entity |  |
| Input Parameter | Transfer Source Entity | Entity |  |
| Input Parameter | Aggro Owner Entity | Entity |  |
| Input Parameter | Transfer Ratio | Floating Point Numbers |  |

## **3. Taunt Target**

![]()

**Node Functions**

Available only in Custom Aggro Mode

The Taunter Entity taunts the specified Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Taunter Entity | Entity |  |
| Input Parameter | Target Entity | Entity |  |

## **4. Remove Target Entity From Aggro List**

![]()

**Node Functions**

Available only in Custom Aggro Mode

Removes the Target Entity from the Aggro Owner Entity's Aggro List; this may cause the Target Entity to leave battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Aggro Owner Entity | Entity |  |

## **5. Clear the Aggro List of the Specified Entity**

![]()

**Node Functions**

Available only in Custom Aggro Mode

Clears the Aggro List of the specified Entity; this usually causes the Target to leave battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |

## **6. Set the Aggro Value of the Specified Entity**

![]()

**Node Functions**

Available only in Custom Aggro Mode

Sets the Aggro Value of the specified Entity on the Aggro Owner Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Aggro Owner Entity | Entity |  |
| Input Parameter | Aggro Value | Integer |  |

## **7. Increase the Aggro Value of the Specified Entity**

![]()

**Node Functions**

Available only in Custom Aggro Mode

Modify the aggro value of the specified entity for the aggro owner entity; the increase value can be negative.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Aggro Owner Entity | Entity |  |
| Input Parameter | Increase Value | Integer | Changed value = original value + increase value |

# IV. Signal

## **1.** **Send Signal to Server Node Graph**

![]()

**Node Functions**

Within the skill node graph, signals can be sent to the server node graph, and all server node graphs can listen for this signal.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Signal Name | String |  |

Operation Nodes

Flow Control Nodes

1

Explain

---

# Execution Nodes

# I. Skills

## **1. Traverse Entity List**

![](./Genshin Impact Miliastra Wonderland_ General Guide8_files/31efe191-c319-4868-b224-a6631801e572.png)

**Node Functions**

Iterates through each Entity in the input Entity List

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity List | Entity List |  |
| Output Parameter | Current Entity | Entity |  |

## **2. Play Timed Effects**

![](./Genshin Impact Miliastra Wonderland_ General Guide8_files/8ff15af7-601f-48d9-b2ea-0f46a65ffc27.png)

**Node Functions**

Plays Timed Effects at the specified World Location

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Special Effects Asset Configuration ID | Configuration ID |  |
| Input Parameter | Location | 3D Vector |  |
| Input Parameter | Rotate | 3D Vector |  |
| Input Parameter | Zoom Multiplier | Floating Point Numbers |  |
| Input Parameter | Play Default Sound Effect | Boolean |  |

## **3. Fixed-Point Projectile Launch**

![]()

**Node Functions**

Spawns a Local Projectile at the specified Location in the World Coordinate System

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Projectile's Prefab ID | Prefab ID |  |
| Input Parameter | Create Location | 3D Vector |  |
| Input Parameter | Create Rotation | 3D Vector |  |
| Input Parameter | Track Target | Entity |  |
| Input Parameter | Projectile Faction | Faction |  |

## **4. Complex Creation Directed Movement**

![]()

**Node Functions**

Moves from the current Location to the Target Location

You can configure the Maximum Distance. If this value is too small, the object may not be able to move to the Target Location

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Location | 3D Vector |  |
| Input Parameter | Displacement Duration | Floating Point Numbers |  |
| Input Parameter | Max Distance | Floating Point Numbers |  |
| Input Parameter | Ignore Collision | Boolean |  |

## **5. Complex Creation Teleport**

![]()

**Node Functions**

Teleport from your current location to the Target Location

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Location | 3D Vector |  |
| Input Parameter | Target Rotation | 3D Vector |  |

## **6. Recover Creation's HP**

![]()

**Node Functions**

Initiates a one-time HP restoration for the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Recovery Amount | Floating Point Numbers |  |
| Input Parameter | Ignore Recovery Adjustment Effect | Boolean |  |

## 7. Set the Global CD of the Creation

![]()

**Node Functions**

Permanently changes the Creation's Global CD for this stage run

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Cooldown | Floating Point Numbers |  |

## **8. Set the Current CD of the Creation Skill**

![]()

**Node Functions**

Adjusts only the CD for this Creation Skill for this use. This is a one-time change and will not be saved

Note: When this Node runs, if the Target Skill is currently casting and is configured to trigger its CD when the Skill ends, the CD will be reset to the Skill's configured CD at End. Even if this Node successfully sets the Current CD, it will be overwritten by the CD triggered at Skill End.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill ID | Integer |  |
| Input Parameter | Current Cooldown | Floating Point Numbers |  |

## **9. Set the CD of the Creation Skill**

![]()

**Node Functions**

Permanently changes the Creation's Skill CD for this stage run

Note:

1.

When this Node runs, it does not change the Target Skill's current remaining CD. It only affects the CD the next time the Skill enters CD

2.

If the Target Skill is being cast and is configured to Trigger CD on Skill End, then when the Skill ends, the CD that starts will use the time set by this Node

3.

Instant Skills have no duration, so their CD always starts counting when the Skill begins

For example:

4.

Skill A has 5 seconds of CD remaining. At this moment, the Node's CD is set to 10 seconds. The Creation can use this Skill after 5 seconds, and after using it, this unit enters a 10-second CD

5.

Skill A is configured to trigger its CD when the Skill ends, with a 5-second CD. If a Creation is casting Skill A and this Node changes the CD to 10 seconds, the Skill will enter a 10-second CD immediately after it ends

6.

Skill A is an Instant Skill with a 5-second cooldown. If a Creation uses this Node in the Node Graph Logic for casting Skill A and changes it to 10 seconds, then, as in Example 1, Skill A will be available after 5 seconds. After you use it, it enters a 10-second cooldown

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill ID | Integer |  |
| Input Parameter | Cooldown (CD) | Floating Point Numbers |  |
| Input Parameter | CD Variation Range | Floating Point Numbers |  |

## 10. Set the Current Time of the Creation Cooldown Group

![]()

**Node Functions**

Adjusts only this Creation's Skill Group CD for this session; changes are not saved

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | CD Group ID | Integer |  |
| Input Parameter | Current Cooldown | Floating Point Numbers |  |

## 11. Set the Time of the Creation Cooldown Group

![]()

**Node Functions**

Permanently changes the Creation's Skill Group CD for this stage run

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | CD Group ID | Integer |  |
| Input Parameter | Cooldown (CD) | Floating Point Numbers |  |
| Input Parameter | CD Variation Range | Floating Point Numbers |  |

## **12. Trigger Hitbox at Specific Location**

![]()

![]()

![]()

**Node Functions**

Initiates a Hitbox Attack at the specified Location in the World Coordinate System, with configurable attack parameters

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Location | 3D Vector |  |
| Input Parameter | Rotate | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Numbers |  |
| Input Parameter | Damage Increment | Floating Point Numbers |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Hitbox Type | Enumeration |  |
| Input Parameter | Scale of Cuboid Hitbox | 3D Vector |  |
| Input Parameter | Radius of Sphere Hitbox | Floating Point Numbers |  |
| Input Parameter | Height of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Sector Angle of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Sector Radius of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Inner Radius of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Detection Direction of Sector Hitbox | Enumeration |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Numbers |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Numbers |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Numbers |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Offset | Floating Point Numbers |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Numbers |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Numbers |  |

## **13. Trigger Rectangular Hitbox at Specific Location**

![]()

![]()

**Node Functions**

Initiates a Rectangular HitBox Attack at a specified location in the World Coordinate System, with configurable attack parameters

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Location | 3D Vector |  |
| Input Parameter | Rotate | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Numbers |  |
| Input Parameter | Damage Increment | Floating Point Numbers |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Scale of Cuboid Hitbox | 3D Vector |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Numbers |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Numbers |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Numbers |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Numbers |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Numbers |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Numbers |  |

## **14. Trigger Spherical Hitbox at Specific Location**

![]()

![]()

**Node Functions**

Initiates a Sphere Hitbox Attack at a specified location in the World Coordinate System, with configurable attack parameters

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Location | 3D Vector |  |
| Input Parameter | Rotate | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Numbers |  |
| Input Parameter | Damage Increment | Floating Point Numbers |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Radius of Sphere Hitbox | Floating Point Numbers |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Numbers |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Numbers |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Numbers |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Numbers |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Numbers |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Numbers |  |

## **15. Trigger Sector Hitbox at Specific Location**

![]()

![]()

**Node Functions**

Initiates a Sector Hitbox Attack at a specified location in the World Coordinate System, with configurable attack parameters

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Location | 3D Vector |  |
| Input Parameter | Rotate | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Numbers |  |
| Input Parameter | Damage Increment | Floating Point Numbers |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Height of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Sector Angle of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Sector Radius of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Inner Radius of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Detection Direction of Sector Hitbox | Enumeration |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Numbers |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Numbers |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Numbers |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Numbers |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Numbers |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Numbers |  |

## **16. Add Unit Status**

![]()

**Node Functions**

Applies the Unit Status defined by the configuration ID to the Target

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Application Target | Entity |  |
| Input Parameter | Stacks | Integer |  |
| Input Parameter | Unit Status Config ID | Config ID |  |

## **17. Remove Unit Status**

![]()

**Node Functions**

Removes the Unit Status corresponding to the specified configuration ID from the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Removal Target | Entity |  |
| Input Parameter | Unit Status Config ID | Config ID |  |

## **18. Remove Specified Character Disruptor Device**

![]()

**Node Functions**

Removes the specified type of Character Disruptor Device

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Disruptor Device Type | Enumeration | Includes: Force Field Device, Ejector, and Traction Device |

## **19. Resets the Creation's Skill CD**

![]()

**Node Functions**

Resets the Skill CD to 0. If the conditions are met, the Skill can be cast immediately

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill ID | Integer |  |

## **20. Creation Turns to Face Set Direction**

![]()

**Node Functions**

Rotates the Creation to face the orientation of the specified 3D Vector

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Orientation | 3D Vector |  |

## **21. Trigger Hitbox at Specified Attachment Point**

![]()

![]()

![]()

**Node Functions**

Initiates a Hitbox Attack at a specified Attachment Point, with configurable attack parameters

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Attachment Point Name | String |  |
| Input Parameter | Attachment Point Offset | 3D Vector |  |
| Input Parameter | Attachment Point Rotation | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Numbers |  |
| Input Parameter | Damage Increment | Floating Point Numbers |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Hitbox Type | Enumeration |  |
| Input Parameter | Scale of Cuboid Hitbox | 3D Vector |  |
| Input Parameter | Radius of Sphere Hitbox | Floating Point Numbers |  |
| Input Parameter | Height of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Sector Angle of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Sector Radius of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Inner Radius of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Detection Direction of Sector Hitbox | Enumeration |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Numbers |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Numbers |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Numbers |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Numbers |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Numbers |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Numbers |  |

## **22. Trigger Rectangular Hitbox at Specified Attachment Point**

![]()

![]()

**Node Functions**

Initiates a Rectangular HitBox Attack from the Specified Attachment Point, with configurable attack parameters

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Attachment Point Name | String |  |
| Input Parameter | Attachment Point Offset | 3D Vector |  |
| Input Parameter | Attachment Point Rotation | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Numbers |  |
| Input Parameter | Damage Increment | Floating Point Numbers |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Scale of Cuboid Hitbox | 3D Vector |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Numbers |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Numbers |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Numbers |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Numbers |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Numbers |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Numbers |  |

## **23. Trigger Spherical Hitbox at Specified Attachment Point**

![]()

![]()

**Node Functions**

Initiates a Sphere HitBox Attack from the Specified Attachment Point, with configurable attack parameters

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Attachment Point Name | String |  |
| Input Parameter | Attachment Point Offset | 3D Vector |  |
| Input Parameter | Attachment Point Rotation | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Numbers |  |
| Input Parameter | Damage Increment | Floating Point Numbers |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Radius of Sphere Hitbox | Floating Point Numbers |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Numbers |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Numbers |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Numbers |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Numbers |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Numbers |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Numbers |  |

## **24. Trigger Sector Hitbox at Specified Attachment Point**

![]()

![]()

**Node Functions**

Initiates a Sector HitBox Attack from the Specified Attachment Point, with configurable attack parameters

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Faction Filter | Enumeration |  |
| Input Parameter | Attachment Point Name | String |  |
| Input Parameter | Attachment Point Offset | 3D Vector |  |
| Input Parameter | Attachment Point Rotation | 3D Vector |  |
| Input Parameter | Damage Coefficient | Floating Point Numbers |  |
| Input Parameter | Damage Increment | Floating Point Numbers |  |
| Input Parameter | Hitbox Entity Type Filter List | Enumeration List |  |
| Input Parameter | Trigger Type | Enumeration |  |
| Input Parameter | On-Hit Scene Effects | Integer |  |
| Input Parameter | Height of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Sector Angle of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Sector Radius of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Inner Radius of Sector Hitbox | Floating Point Numbers |  |
| Input Parameter | Detection Direction of Sector Hitbox | Enumeration |  |
| Input Parameter | Attack Layer Filter | Enumeration |  |
| Input Parameter | Attack Tag List | String List |  |
| Input Parameter | Elemental Type | Enumeration |  |
| Input Parameter | Elemental Attack Potency | Floating Point Numbers |  |
| Input Parameter | Hit Type | Enumeration |  |
| Input Parameter | Attack Type | Enumeration |  |
| Input Parameter | Interrupt Value | Floating Point Numbers |  |
| Input Parameter | Absolute Damage | Boolean |  |
| Input Parameter | On-Hit Special Effects | Integer |  |
| Input Parameter | Knockback Orientation | Enumeration |  |
| Input Parameter | Block Damage Pop-Up | Boolean |  |
| Input Parameter | On-Hit Scene Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Scene Effects Zoom | Floating Point Numbers |  |
| Input Parameter | On-Hit Special Effects Offset | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Rotation | 3D Vector |  |
| Input Parameter | On-Hit Special Effects Zoom | Floating Point Numbers |  |
| Input Parameter | Aggro Multiplier for This Attack | Floating Point Numbers |  |
| Input Parameter | Aggro Increment for This Attack | Integer |  |
| Input Parameter | Hit Level | Enumeration |  |
| Input Parameter | On-Hit Horizontal Impulse | Floating Point Numbers |  |
| Input Parameter | On-Hit Vertical Impulse | Floating Point Numbers |  |

## **25. Set Skill Variable**

![]()

**Node Functions**

Assigns value to specified Skill Variable

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Variable Config ID | Config ID |  |
| Input Parameter | Set Value | Floating Point Numbers | New Value |

## **26. Increase Skill Variable Value**

![]()

**Node Functions**

Adds the given value to the specified Skill Variable. Value can be negative

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Skill Variable Config ID | Config ID |  |
| Input Parameter | Increase Value | Floating Point Numbers | New Value = Original Value + Increase Value |

# II. General

## **1. Set Local Variable**

![]()

**Node Functions**

Sets the value of a Local Variable

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Variable Name | String |  |
| Input Parameter | Variable Value | Generic |  |

## **2. Break Loop**

![]()

**Node Functions**

Break out of a Finite Loop. The output pin must connect to the [Break Loop] input parameter of the [Finite Loop] Node

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
|  |  |  |  |

## **3. Notify Server Node Graph**

![]()

**Node Functions**

Notifies the Server Node Graph; supports up to three String parameters

At runtime, forwards logic to the Server Node Graph and triggers the [On Skill Node Call] Event on the Server Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | String 1 | String |  |
| Input Parameter | String 2 | String |  |
| Input Parameter | String 3 | String |  |

## **4. Finite Loop**

![]()

**Node Functions**

From the [Loop Start Value] to the [Loop Termination Value], the loop iterates, incrementing the Integer by 1 each time. On each iteration, it executes the Nodes connected to [Loop Body]. After a full iteration, it executes the Nodes connected to [Loop Complete].

Use [Break Loop] to end the iteration early

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Loop Start Value | Integer |  |
| Input Parameter | Loop Termination Value | Integer |  |
| Output Parameter | Current Loop Value | Integer |  |

# III. Signals

## **1. Send Signal to Server Node Graph**

![]()

**Node Functions**

In the Skill Node Graph, you can send a signal to the Server Node Graph, and all Server Node Graphs can monitor that signal

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Signal Name | String |  |

# IV. Custom Aggro

## **1. Set the Aggro Value of the Specified Entity Proportionally**

![]()

**Node Functions**

Available only in Custom Aggro Mode

Set the Target Entity's Aggro Value toward the specified Aggro Owner proportionally

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Aggro Owner Entity | Entity |  |
| Input Parameter | Aggro Value Ratio | Floating Point Numbers |  |

## **2. Transfer the Aggro Value of the Specified Entity Proportionally**

![]()

**Node Functions**

Available only in Custom Aggro Mode

Transfers a percentage of Aggro on the Aggro Owner from the Source Entity to the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Transfer Target Entity | Entity |  |
| Input Parameter | Transfer Source Entity | Entity |  |
| Input Parameter | Aggro Owner Entity | Entity |  |
| Input Parameter | Transfer Ratio | Floating Point Numbers |  |

## **3. Taunt Target**

![]()

**Node Functions**

Available only in Custom Aggro Mode

The Taunter Entity taunts the specified Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Taunter Entity | Entity |  |
| Input Parameter | Target Entity | Entity |  |

## **4. Remove Target Entity From Aggro List**

![]()

**Node Functions**

Available only in Custom Aggro Mode

Removes the Target Entity from the Aggro Owner Entity's Aggro List; this may cause the Target Entity to leave battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Aggro Owner Entity | Entity |  |

## **5. Clear the Aggro List of the Specified Entity**

![]()

**Node Functions**

Available only in Custom Aggro Mode

Clears the Aggro List of the specified Entity; this usually causes the Target to leave battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |

## **6. Set the Aggro Value of the Specified Entity**

![]()

**Node Functions**

Available only in Custom Aggro Mode

Sets the Aggro Value of the specified Entity on the Aggro Owner Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Aggro Owner Entity | Entity |  |
| Input Parameter | Aggro Value | Integer |  |

## **7. Increase the Aggro Value of the Specified Entity**

![]()

**Node Functions**

Available only in Custom Aggro Mode

Edit the Aggro Value of the Specified Entity on the Aggro Owner, and the added value can be negative

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Aggro Owner Entity | Entity |  |
| Input Parameter | Increase Value | Integer | Edited Value = Original Value + Increase Value |

# 

##

Operation Nodes

Flow Control Node

1

Explain
