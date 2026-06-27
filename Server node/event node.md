# Event Nodes (Node Sự Kiện)

# I. Custom Variables (Biến Tùy Chỉnh)

## **1. When Node Graph Variable Changes (Khi Biến của Node Graph thay đổi)**

![](./event ndoe_files/781dd23e-fedb-4a96-aef6-1fbbc1d14959.png)

**Node Functions (Chức năng Node)**

Sự kiện này được kích hoạt (triggered) khi một Biến (Node Graph Variable) trong Node Graph hiện tại bị thay đổi.

Giá trị trước (previous) và hiện tại (current) mang kiểu Chung (Generic). Cần xác định kiểu Generic để nhận đúng sự kiện cho các Biến có kiểu tương ứng.

Các Biến thuộc kiểu Vật chứa (Vessel-type) sẽ không cung cấp các tham số đầu ra chứa giá trị trước và sau khi thay đổi (before-value và after-value).

**Node Parameters (Tham số Node)**

| | | | |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Output Parameter (Đầu ra) | Event Source Entity (Thực thể Nguồn Sự kiện) | Entity (Thực thể) | Thực thể (Entity) liên kết với Node Graph này |
| Output Parameter (Đầu ra) | Event Source GUID (GUID Nguồn Sự kiện) | GUID | Mã định danh GUID của Thực thể liên kết với Node Graph này |
| Output Parameter (Đầu ra) | Variable Name (Tên Biến) | String (Chuỗi) | Tên của Biến vừa bị thay đổi |
| Output Parameter (Đầu ra) | Pre-Change Value (Giá trị Trước thay đổi) | Generic (Chung) | Giá trị của Biến trước khi bị thay đổi |
| Output Parameter (Đầu ra) | Post-Change Value (Giá trị Sau thay đổi) | Generic (Chung) | Giá trị của Biến sau khi thay đổi |

## **2. When Custom Variable Changes (Khi Biến Tùy chỉnh thay đổi)**

![]()

**Node Functions (Chức năng Node)**

Sự kiện này được kích hoạt khi Biến Tùy chỉnh (Custom Variable) của Thực thể (Entity) được liên kết với Node Graph hiện tại thay đổi.

Giá trị trước (previous) và hiện tại (current) mang kiểu Chung (Generic). Xác định kiểu Generic trước thì bạn mới có thể nhận đúng sự kiện cho các Biến Tùy chỉnh có kiểu tương ứng.

Các Biến Tùy chỉnh thuộc kiểu Vật chứa (Vessel-type) sẽ không cung cấp các tham số đầu ra chứa giá trị trước và sau khi thay đổi (before-value và after-value).

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Output Parameter (Đầu ra) | Event Source Entity (Thực thể Nguồn Sự kiện) | Entity (Thực thể) | Thực thể được liên kết với Node Graph này |
| Output Parameter (Đầu ra) | Event Source GUID (GUID Nguồn Sự kiện) | GUID | Mã định danh GUID của Thực thể được liên kết với Node Graph này |
| Output Parameter (Đầu ra) | Variable Name (Tên Biến) | String (Chuỗi) | Tên của Biến vừa bị thay đổi |
| Output Parameter (Đầu ra) | Pre-Change Value (Giá trị Trước thay đổi) | Generic (Chung) | Giá trị của Biến trước khi bị thay đổi |
| Output Parameter (Đầu ra) | Post-Change Value (Giá trị Sau thay đổi) | Generic (Chung) | Giá trị của Biến sau khi thay đổi |

# II. Preset Status (Trạng thái Cài sẵn)

## **1. When Preset Status Changes (Khi Trạng thái Cài sẵn thay đổi)**

![]()

**Node Functions (Chức năng Node)**

Sự kiện này được kích hoạt khi Trạng thái Cài sẵn (Preset Status) của Thực thể được liên kết với Node Graph thay đổi.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Output Parameter (Đầu ra) | Event Source Entity (Thực thể Nguồn Sự kiện) | Entity (Thực thể) |  |
| Output Parameter (Đầu ra) | Event Source GUID (GUID Nguồn Sự kiện) | GUID |  |
| Output Parameter (Đầu ra) | Preset Status ID (ID Trạng thái Cài sẵn) | Integer (Số nguyên) |  |
| Output Parameter (Đầu ra) | Pre-Change Value (Giá trị Trước thay đổi) | Integer (Số nguyên) |  |
| Output Parameter (Đầu ra) | Post-Change Value (Giá trị Sau thay đổi) | Integer (Số nguyên) |  |

# III. Entity Related (Liên quan đến Thực thể)

## **1. When Character Movement SPD Meets Condition (Khi Tốc độ di chuyển của Nhân vật đáp ứng Điều kiện)**

![]()

**Node Functions (Chức năng Node)**

Thêm hiệu ứng Trạng thái Đơn vị (Unit Status) [Monitor Movement Speed] (Theo dõi Tốc độ Di chuyển) vào Thực thể Nhân vật. Sự kiện này được kích hoạt khi các điều kiện được đáp ứng.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Output Parameter (Đầu ra) | Event Source Entity (Thực thể Nguồn Sự kiện) | Entity (Thực thể) |  |
| Output Parameter (Đầu ra) | Event Source GUID (GUID Nguồn Sự kiện) | GUID |  |
| Output Parameter (Đầu ra) | Unit Status Config ID (ID Cấu hình Trạng thái Đơn vị) | Config ID (ID Cấu hình) |  |
| Output Parameter (Đầu ra) | Condition: Comparison Type (Điều kiện: Loại So sánh) | Enumeration (Liệt kê) |  |
| Output Parameter (Đầu ra) | Condition: Comparison Value (Điều kiện: Giá trị So sánh) | Floating Point Numbers (Số thực) |  |
| Output Parameter (Đầu ra) | Current Movement SPD (Tốc độ Di chuyển Hiện tại) | Floating Point Numbers (Số thực) |  |

## **2. When Entity Is Created (Khi Thực thể được tạo ra)**

![]()

**Node Functions (Chức năng Node)**

Sự kiện này được kích hoạt khi một Thực thể (Entity) được tạo ra.

Tất cả các loại Thực thể đều có thể kích hoạt sự kiện này. Thực thể Màn chơi (Stage Entities), Thực thể Nhân vật (Character Entities) và Thực thể Người chơi (Player Entities) kích hoạt sự kiện này khi bước vào một Màn chơi (Stage).

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Output Parameter (Đầu ra) | Event Source Entity (Thực thể Nguồn Sự kiện) | Entity (Thực thể) |  |
| Output Parameter (Đầu ra) | Event Source GUID (GUID Nguồn Sự kiện) | GUID |  |

## **3. When Entity Is Destroyed (Khi Thực thể bị phá hủy)**

![]()

**Node Functions (Chức năng Node)**

Sự kiện này kích hoạt khi các đối tượng và vật thể trong màn chơi bị phá hủy. Sự kiện này chỉ có thể kích hoạt trên các thực thể của màn chơi (stage entities).

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity | Destroyed Entity |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Location | 3D Vector |  |
| Output Parameter | Orientation | 3D Vector |  |
| Output Parameter | Entity Type | Enumeration |  |
| Output Parameter | Faction | Faction |  |
| Output Parameter | Damage Source | Entity |  |
| Output Parameter | Owner Entity | Entity |  |
| Output Parameter | Custom Variable Component Snapshot | Custom Variable Snapshot | On destroy, captures a snapshot of the Custom Variable component on this Entity. Use the Search Custom Variable Snapshot node to retrieve its Custom Variable values |

## **4. When Entity Is Removed/Destroyed (Khi Thực thể bị Loại bỏ/Phá hủy)**

![]()

**Node Functions (Chức năng Node)**

This event is triggered when any Entity in the Stage is removed or destroyed, and it can only be triggered on Stage Entities

This event is triggered upon Entity destruction or removal. Therefore, when an Entity is destroyed, it triggers both the [On Entity Destroyed] and [On Entity Removed/Destroyed] events in sequence

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source GUID | GUID |  |

# IV. Faction Related (Liên quan đến Phe phái)

## **1. When Entity Faction Changes (Khi Phe phái Thực thể thay đổi)**

![]()

**Node Functions (Chức năng Node)**

This event is triggered when an Entity's Faction changes

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Pre-Change Faction | Faction |  |
| Output Parameter | Post-Change Faction | Faction |  |

# V. Player and Character Related (Liên quan đến Người chơi và Nhân vật)

## **1. When the Character Is Down (Khi Nhân vật bị Đánh bại)**

![]()

**Node Functions (Chức năng Node)**

When a Character is Downed, the Node Graph on the Character Entity can trigger this event

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Character Entity | Entity |  |
| Output Parameter | Reason | Enumeration | Node Graph caused: the Character was Downed by the Destroy Entity node in the Node Graph  Normal Down: the Character was Downed because HP reached 0  Abnormal Down: the character was downed due to drowning, falling into an abyss, etc. |
| Output Parameter | Knockdown Entity | Entity |  |

## **2. When Character Revives (Khi Nhân vật Hồi sinh)**

![]()

**Node Functions (Chức năng Node)**

Khi một Nhân vật được Hồi sinh, Node Graph trên Thực thể Nhân vật có thể kích hoạt sự kiện này

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Character Entity | Entity |  |

## **3. When Player Teleport Completes (Khi Người chơi Hoàn thành Dịch chuyển)**

![]()

**Node Functions (Chức năng Node)**

Sự kiện này được kích hoạt trên Node Graph của Thực thể Người chơi khi Người chơi hoàn thành dịch chuyển

Sự kiện này cũng được kích hoạt khi Người chơi lần đầu tiên vào một Màn chơi

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Player Entity | Entity |  |
| Output Parameter | Player GUID | GUID |  |

## **4. When All Player's Characters Are Down (Khi Tất cả Nhân vật của Người chơi bị Đánh bại)**

![]()

**Node Functions (Chức năng Node)**

Sự kiện này được kích hoạt trên Node Graph của Thực thể Người chơi khi tất cả Nhân vật của Người chơi bị Đánh bại

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Player Entity | Entity |  |
| Output Parameter | Reason | Enumeration | Node Graph caused: the Character was Downed by the Destroy Entity node in the Node Graph  Normal Down: the Character was Downed because HP reached 0  Abnormal Down: the character was downed due to drowning, falling into an abyss, etc. |

## **5. When All Player's Characters Are Revived (Khi Tất cả Nhân vật của Người chơi được Hồi sinh)**

![]()

**Node Functions (Chức năng Node)**

Sự kiện này được kích hoạt trên Node Graph của Thực thể Người chơi khi tất cả Nhân vật của Người chơi được Hồi sinh

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Player Entity | Entity |  |

## **6. When Player Is Abnormally Downed and Revives (Khi Người chơi bị Đánh bại Bất thường và Hồi sinh)**

![]()

**Node Functions (Chức năng Node)**

This event is triggered on the Player Entity when a Character is Downed and then Revived due to drowning, falling into an abyss, or similar reasons

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Player Entity | Entity |  |

## **7. When the Active Character Changes (Khi Nhân vật Hoạt động Thay đổi)**

![]()

**Node Functions (Chức năng Node)**

Available only in Classic Mode. This event is triggered on the player entity when the active character changes.

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Player Entity | Entity |  |
| Output Parameter | Player GUID | GUID |  |
| Output Parameter | Replaced Character Entity | Entity |  |
| Output Parameter | Current Active Character Entity | Entity |  |

# VI. Collision Trigger (Kích hoạt Va chạm)

## **1. When Entering Collision Trigger (Khi Bước Vào Vùng Va Chạm)**

![]()

**Node Functions (Chức năng Node)**

Khi phạm vi "Nguồn kích hoạt va chạm" (Collision Trigger Source) của một thực thể A (ví dụ: Người chơi) bước vào vùng "Kích hoạt va chạm" (Collision Trigger) của một thực thể B (ví dụ: Bức tượng).

Sự kiện Node Graph sẽ được gửi tới thực thể B - nơi được thiết lập "Kích hoạt va chạm".

**Node Parameters (Tham số Node)**

| | | | |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Output Parameter (Đầu ra) | Entering Entity (Thực thể vừa bước vào) | Entity (Thực thể) | Là Thực thể A (nhân vật của bạn) được nhắc đến ở trên |
| Output Parameter (Đầu ra) | Entering Entity GUID (GUID Thực thể bước vào) | GUID | |
| Output Parameter | Trigger Entity | Entity | Entity B (mentioned above) |
| Output Parameter | Trigger Entity GUID | GUID |  |
| Output Parameter | Trigger ID | Integer | The trigger with the corresponding ID in Entity B's Collision Trigger Component |

## **2. When Exiting Collision Trigger**

![]()

**Node Functions**

When the "Collision Trigger Source" range of active Entity A leaves the "Collision Trigger" range of active Entity B

Node graph events will be sent to the entity B configured with "Collision Trigger"

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Exiting Entity | Entity | Entity A (referenced above) |
| Output Parameter | Exiting Entity GUID | GUID |  |
| Output Parameter | Trigger Entity | Entity | Entity B (mentioned above) |
| Output Parameter | Trigger Entity GUID | GUID |  |
| Output Parameter | Trigger ID | Integer |  |

# VII. Combat

## **1. When HP Is Recovered**

![]()

**Node Functions**

This event is triggered when an Entity's HP is restored

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Healer Entity | Entity |  |
| Output Parameter | Recovery Amount | Floating Point Numbers | Actual healing amount. If the Entity had not lost any HP prior to healing, the amount is 0 |
| Output Parameter | Recover Tag List | String List |  |

## **2. When Initiating HP Recovery**

![]()

**Node Functions**

This event is triggered on the initiating Entity when an Entity restores HP to other Entities

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Recover Target Entity | Entity |  |
| Output Parameter | Recovery Amount | Floating Point Numbers | Actual healing amount. If the Target Entity had not lost any HP prior to healing, the amount is 0 |
| Output Parameter | Recover Tag List | String List |  |

## **3. When Attack Hits**

![]()

**Node Functions**

This event is triggered when an Entity's attack hits other Entities

(In Classic Mode, due to the Craftsperson's settings, the actual damage may differ from other scenarios.)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Hit Target Entity | Entity |  |
| Output Parameter | Damage | Floating Point Numbers | Actual damage dealt. If no damage is dealt due to Invincible or other reasons, the amount is 0 |
| Output Parameter | Attack Tag List | String List |  |
| Output Parameter | Elemental Type | Enumeration |  |
| Output Parameter | Elemental Attack Potency | Floating Point Numbers | Elemental Gauge in the Attack |

## **4. When Attacked**

![]()

**Node Functions**

This event is triggered when the Entity is attacked

(In Classic Mode, due to the Craftsperson's settings, the actual damage may differ from other scenarios.)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Attacker Entity | Entity |  |
| Output Parameter | Damage | Floating Point Numbers | Actual damage dealt. If no damage is dealt due to Invincible or other reasons, the amount is 0 |
| Output Parameter | Attack Tag List | String List |  |
| Output Parameter | Elemental Type | Enumeration |  |
| Output Parameter | Elemental Attack Potency | Floating Point Numbers | Elemental Gauge in the Attack |

## **5. When Entering an Interruptible State**

![]()

**Node Functions**

Available only in Beyond Mode.

This event is triggered when an Entity is attacked and enters the Vulnerable Status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Attacker | Entity |  |

# VIII. Motion Device

## **1. When Basic Motion Device Stops**

![]()

**Node Functions**

This event is sent to the Component Owner when a Basic Motion Device on the Basic Motion Device Component completes its movement or is disabled

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity | Component Owner |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Motion Device Name | String |  |

## **2. When Path Reaches Waypoint**

![]()

**Node Functions**

When the Pathing Motion Device reaches a Waypoint, it sends this event to the Owner of the Basic Motion Device Component. This event is triggered only if "Send Event on Waypoint Arrival" is enabled in the Waypoint settings

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity | Component Owner |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Motion Device Name | String |  |
| Output Parameter | Path Point ID | Integer |  |

# IX. Hit Detection

## **1. When On-Hit Detection Is Triggered**

![]()

**Node Functions**

This event is triggered when the On-Hit Detection Component's Owner hits other Entities or the Scene

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | On-Hit Hurtbox | Boolean | If set to False: The environment was hit  If set to True: An Entity was hit. Retrieve values from the Hit Entity output parameter |
| Output Parameter | On-Hit Entity | Entity | Hit Entity is only valid when a Hurtbox is hit |
| Output Parameter | On-Hit Location | 3D Vector |  |

# X. Timer

## **1. When Timer Is Triggered**

![]()

**Node Functions**

This event is triggered when the Timer reaches the specified time node

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Timer Name | String |  |
| Output Parameter | Timer Sequence ID | Integer |  |
| Output Parameter | Number of Loops | Integer |  |

# XI. Global Timer

## **1. When Global Timer Is Triggered**

![]()

**Node Functions**

This event is triggered when the Global Countdown Timer reaches zero

The Global Stopwatch Timer does not trigger this event

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Timer Name | String |  |

# XII. UI Control Groups

## **1. When UI Control Group Is Triggered**

![]()

**Node Functions**

This event is triggered only by UI controls of the following types: Interactive Button, Item Display, Custom Button, and Custom Switch

This event can only be received by the Player Node Graph that triggered the interaction

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | UI Control Group Composite Index | Integer | If the UI control that triggered this event forms a multi-control UI group with other controls, this output parameter returns the corresponding group value |
| Output Parameter | UI Control Group Index | Integer | If the triggering UI control is a single-control UI group, this value represents the ID of that UI control group  If the triggering UI control is part of a multi-control UI group, this value represents the ID of the control within that group |

# XIII. Unit Status

## **1. When Unit Status Changes (Khi Trạng thái Đơn vị Thay đổi)**

![]()

**Node Functions**

This event is triggered when the Stack Count of a Unit Status changes
Sự kiện này được kích hoạt khi Số lượng Stack của Trạng thái Đơn vị thay đổi

This event is triggered when Unit Status effects are applied or removed
Sự kiện này được kích hoạt khi hiệu ứng Trạng thái Đơn vị được áp dụng hoặc loại bỏ

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu)** | **Description (Mô tả)** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Unit Status Config ID | Config ID |  |
| Output Parameter | Applier Entity | Entity |  |
| Output Parameter | Infinite Duration | Boolean |  |
| Output Parameter | Remaining Status Duration | Floating Point Numbers |  |
| Output Parameter | Remaining Status Stacks | Integer | Edited Stack Count |
| Output Parameter | Original Status Stacks | Integer | Previous Stack Count |
| Output Parameter | Slot ID | Integer | ID of the Unit Status slot that changed |

## **2. When Unit Status Ends (Khi Trạng thái Đơn vị Kết thúc)**

![]()

**Node Functions**

This event is triggered when a Unit Status is removed for any reason or when its Runtime Duration expires

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Unit Status Config ID | Config ID |  |
| Output Parameter | Applier Entity | Entity |  |
| Output Parameter | Infinite Duration | Boolean |  |
| Output Parameter | Remaining Status Duration | Floating Point Numbers |  |
| Output Parameter | Remaining Status Stacks | Integer |  |
| Output Parameter | Remover Entity | Entity |  |
| Output Parameter | Removal Reason | Enumeration | Status Replacement: The Unit Status was removed because it was replaced by another status  Duration Exceeded: The Unit Status exceeded its runtime duration  Dispelled: The Unit Status was removed directly  Status Expired: The Unit Status became invalid due to other reasons  Class Changed: The Unit Status was removed due to a class change |
| Output Parameter | Slot ID | Integer | ID of the Unit Status slot that changed |

## **3. When Elemental Reaction Event Occurs**

![]()

**Node Functions**

Adds the Unit Status effect [Monitor Elemental Reaction] to the Entity. This event is triggered when the conditions are met

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Elemental Reaction Type | Enumeration |  |
| Output Parameter | Triggerer Entity | Entity |  |
| Output Parameter | Triggerer Entity GUID | GUID |  |

## **4. When Shield Is Attacked**

![]()

**Node Functions**

Adds the Unit Status effect [Add Shield] to the Entity. This event is triggered when the Shield takes damage

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Attacker Entity | Entity |  |
| Output Parameter | Attacker GUID | GUID |  |
| Output Parameter | Unit Status Config ID | Config ID |  |
| Output Parameter | Pre-Attack Layers | Integer |  |
| Output Parameter | Post-Attack Layers | Integer |  |
| Output Parameter | Shield Value of this Unit Status Before Attack | Floating Point Numbers |  |
| Output Parameter | Shield Value of this Unit Status After Attack | Floating Point Numbers |  |

# XIV. Tabs

## **1. When Tab Is Selected**

![]()

**Node Functions**

When the active tab is selected, it will send an event to the node graph

The Entity Node Graph configured by the Tab Component will receive this event

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity | Entity with the tab component mounted |
| Output Parameter | Event Source GUID | GUID | GUID of the Entity with the tab component mounted; outputs 0 if none exists |
| Output Parameter | Tab ID | Integer | ID of the tab |
| Output Parameter | Selector Entity | Entity | Character Entity that triggers the tab |

# XV. Creations

## **1. When Creation Enters Combat**

![]()

**Node Functions**

Only effective in Classic Aggro Mode

This event is triggered when a Creation enters battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |

## **2. When Creation Leaves Combat**

![]()

**Node Functions**

Only effective in Classic Aggro Mode

This event is triggered when a Creation leaves battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |

# XVI. Classes

## **1. When Player Class Level Changes**

![]()

**Node Functions**

This event is triggered when a Player's Class Level changes and is sent to the corresponding Player. It can be received in that Class's Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity | Active Player Entity |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Pre-Change Level | Integer |  |
| Output Parameter | Post-Change Level | Integer |  |

## **2. When Player Class Changes**

![]()

**Node Functions**

This event is triggered when a Player's Class changes and is sent to the corresponding Player. It can be received in the Node Graph of the new Class

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Pre-Modification Class Config ID | Config ID |  |
| Output Parameter | Post-Modification Config ID | Config ID |  |

## **3. When Player Class Is Removed**

![]()

**Node Functions**

This event is triggered when a Player's Class is removed and sent to the corresponding Player. It can be received in the Node Graph of the previous Class

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Pre-Modification Class Config ID | Config ID |  |
| Output Parameter | Post-Modification Config ID | Config ID |  |

# XVII. Skills

## **1. When Skill Node Is Called**

![]()

**Node Functions**

This event is triggered by the [Notify Server Node Graph] Node in the Skill Node Graph. Up to three strings can be passed in

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Caller Entity | Entity |  |
| Output Parameter | Caller GUID | GUID |  |
| Output Parameter | Parameter 1 | String |  |
| Output Parameter | Parameter 2 | String |  |
| Output Parameter | Parameter 3 | String |  |

# XVIII. Custom Aggro

## **1. When Aggro Target Changes**

![]()

**Node Functions**

Available only in Custom Aggro Mode

This event is triggered when the Aggro Target changes

This event can also be triggered when entering or leaving battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu)** | **Description (Mô tả)** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Pre-Change Aggro Target | Entity |  |
| Output Parameter | Post-Change Aggro Target | Entity |  |

## **2. When Self Enters Combat (Khi Thực thể Tự Nhập Trận)**

![]()

**Node Functions**

Available only in Custom Aggro Mode
Chỉ khả dụng trong Chế độ Aggro Tùy chỉnh

This event is triggered when the Entity itself enters battle
Sự kiện này được kích hoạt khi Thực thể tự nhập trận đấu

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu)** | **Description (Mô tả)** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |

## **3. When Self Leaves Combat (Khi Thực thể Tự Rời Trận)**

![]()

**Node Functions**

Available only in Custom Aggro Mode

This event is triggered when the Entity itself leaves battle
Sự kiện này được kích hoạt khi Thực thể tự rời trận đấu

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu)** | **Description (Mô tả)** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |

# XIX. Signals (Tín hiệu)

## **1. Monitor Signal (Giám sát Tín hiệu)**

![]()

**Node Functions**

Monitors Signal trigger events defined in the Signal Manager
Giám sát các sự kiện kích hoạt Tín hiệu được định nghĩa trong Trình quản lý Tín hiệu

The Signal name to monitor must be selected first
Tên Tín hiệu cần giám sát phải được chọn trước

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu)** | **Description (Mô tả)** |
| Output Parameter | Event Source Entity | Entity |  |
| Output Parameter | Event Source GUID | GUID |  |
| Output Parameter | Signal Source Entity | Entity | The Entity that sent this signal using the Send Signal node |

# XX. Deck Selector (Bộ chọn Bộ bài)

## **1. When Deck Selector Is Complete (Khi Bộ chọn Bộ bài Hoàn thành)

![]()

**Node Functions**

This event is triggered on the Player's Node Graph when the Player completes the Deck Selector, or when it is forcibly closed due to time constraints

The output parameters report the Deck Selector's result and the corresponding reason

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu)** | **Description (Mô tả)** |
| Output Parameter | Target Player | Entity | Active Player Entity |
| Output Parameter | Selection Result List | Integer List | When a selection interaction is triggered, valid **selection results** are returned as this output parameter, and the completion reason is **Completed by Player**  When a **Full Refresh** pop-up selection is triggered, the complete **selection result list** is returned as this output parameter, and the completion reason is **Refresh All**  When a **Fixed-Quantity Refresh** pop-up selection is triggered, valid **selection results** are returned as this output parameter, and the completion reason is **Fixed-Quantity Refresh**  When the Deck Selector times out with no interaction, **the default selection is returned** is returned as this output parameter, and the completion reason is **Timeout**  When **Allow Discard Selection is enabled** and the Deck Selector is closed by the player, **the default selection is returned** as this output parameter, and the completion reason is **Closed** **Manually**  When the Deck Selector is closed via the Node Graph, **the default selection is returned** as this output parameter, and the completion reason is **Closed by** **Node Graph** |
| Output Parameter | Completion Reason | Enumeration | Six reason enumerations  **Completed by Player**, **Refresh All**, **Fixed-Quantity Refresh**, Timeout, Closed Manually, Closed by Node Graph |
| Output Parameter | Deck Selector Index | Integer | Referenced Deck Selector ID |

# XXI. Text Bubbles (Bong bóng Văn bản)

## **1. When Text Bubble Is Completed (Khi Bong bóng Văn bản Hoàn thành)

![]()

**Node Functions**

This event can only be mounted by Text Bubble Components and is received by the Entity's Node Graph that completed the dialogue

Completion refers to when the final line of dialogue has finished playing

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Bubble Owner Entity | Entity | Runtime Entity with the Text Bubble component mounted |
| Output Parameter | Character Entity | Entity | Target Character of the current Bubble dialogue |
| Output Parameter | Text Bubble Configuration ID | Config ID | Currently active Text Bubble Config ID |
| Output Parameter | Text Bubble Completion Count | Integer | Number of times the currently active Text Bubble has been fully played for this dialogue Character |

# XXII. Shop (Cửa hàng)

## **1. When Selling Inventory Items in the Shop (Khi bán vật phẩm trong kho tại cửa hàng)

![]()

**Node Functions**

This event is triggered when Inventory items are sold in the Shop. The Owner of the Shop Component will receive it

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu)** | **Description (Mô tả)** |
| Output Parameter | Shop Owner | Entity |  |
| Output Parameter | Shop Owner GUID | GUID |  |
| Output Parameter | Buyer Entity | Entity |  |
| Output Parameter | Shop ID | Integer |  |
| Output Parameter | Item Config ID | Config ID |  |
| Output Parameter | Purchase Quantity | Integer |  |

## **2. When Custom Shop Item Is Sold (Khi vật phẩm tùy chỉnh được bán tại cửa hàng)

![]()

**Node Functions**

This event is triggered when Custom items are sold in the Shop. The Owner of the Shop Component will receive it

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu)** | **Description (Mô tả)** |
| Output Parameter | Shop Owner | Entity |  |
| Output Parameter | Shop Owner GUID | GUID |  |
| Output Parameter | Buyer Entity | Entity |  |
| Output Parameter | Shop ID | Integer |  |
| Output Parameter | Shop Item ID | Integer |  |
| Output Parameter | Purchase Quantity | Integer |  |

## **3. When selling items to the shop (Khi bán vật phẩm cho cửa hàng)

![]()

**Node Functions**

This event is triggered when items are purchased by the Shop. The Owner of the Shop Component will receive it

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu)** | **Description (Mô tả)** |
| Output Parameter | Shop Owner | Entity |  |
| Output Parameter | Shop Owner GUID | GUID |  |
| Output Parameter | Seller Entity | Entity |  |
| Output Parameter | Shop ID | Integer |  |
| Output Parameter | Purchase Item Dictionary | Dictionary |  |

# XXIII. Equipment (Trang bị)

## **1. When Equipment Is Equipped (Khi trang bị được gắn)

![]()

**Node Functions**

This event is triggered when Equipment is equipped. The Owner of the Equipment will receive it. Configure this in the Item Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu)** | **Description (Mô tả)** |
| Output Parameter | Equipment Holder Entity | Entity |  |
| Output Parameter | Equipment Holder GUID | GUID |  |
| Output Parameter | Equipment Index | Integer |  |

## **2. When Equipment Is Unequipped (Khi trang bị được tháo)

![]()

**Node Functions**

This event is triggered when Equipment is unequipped. The Owner of the Equipment will receive it. Configure this in the Item Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Equipment Owner Entity | Entity |  |
| Output Parameter | Equipment Owner GUID | GUID |  |
| Output Parameter | Equipment Index | Integer |  |

## **3. When Equipment Is Initialized**

![]()

**Node Functions**

When Equipment is first obtained and enters the Inventory, it is initialized. The event's output parameters return the unique ID of the Equipment instance. Use this ID to edit the Equipment dynamically. The Owner of the Equipment will receive this event. Configure this in the Item Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Equipment Owner | Entity |  |
| Output Parameter | Equipment Owner GUID | GUID |  |
| Output Parameter | Equipment Index | Integer |  |

## **4. When Equipment Affix Value Changes**

![]()

**Node Functions**

This event is triggered when Equipment Affix values change. The Owner of the Equipment will receive it. Configure this in the Item Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Equipment Owner | Entity |  |
| Output Parameter | Equipment Owner GUID | GUID |  |
| Output Parameter | Equipment Index | Integer |  |
| Output Parameter | Affix ID | Integer | The corresponding ID of this Entry within the Equipment Affixes |
| Output Parameter | Pre-Change Value | Floating Point Numbers |  |
| Output Parameter | Post-Change Value | Floating Point Numbers |  |

## **5. When Equipment is purchased**

![]()

**Node Functions**

The Inventory Owner Entity receives this event when it purchases equipment

This node is triggered only by item exchanges in the Inventory Shop. Custom shops do not trigger it. The Item Node Graph bound to the purchased equipment also receives this event

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Purchasing Inventory Owner Entity | Entity |  |
| Output Parameter | Purchasing Inventory Owner GUID | GUID |  |
| Output Parameter | Equipment Index List | Integer List | List of Indices of the Purchased Equipment |

## **6. When Equipment is sold**

![]()

**Node Functions**

The Inventory Owner Entity receives this event when it sells equipment

This node is triggered only by item exchanges in the Inventory Shop. Custom shops do not trigger it. The Item Node Graph bound to the purchased equipment also receives this event

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Purchasing Inventory Owner Entity | Entity |  |
| Output Parameter | Purchasing Inventory Owner GUID | GUID |  |
| Output Parameter | Equipment Index List | Integer List | List of Indices of the Sold Equipment |

# XXIV. Items

## **1. When Item Is Lost From Inventory**

![]()

**Node Functions**

This event is triggered when an Item is removed from the Inventory (its quantity becomes 0). The Owner of the Inventory Component will receive it

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Item Owner Entity | Entity |  |
| Output Parameter | Item Owner GUID | GUID |  |
| Output Parameter | Item Config ID | Config ID |  |
| Output Parameter | Quantity Lost | Integer |  |

## **2. When the Quantity of Inventory Item Changes**

![]()

**Node Functions**

This event is triggered when the quantity of Items in the Inventory changes. The Owner of the Inventory Component will receive it

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Item Owner Entity | Entity |  |
| Output Parameter | Item Owner GUID | GUID |  |
| Output Parameter | Item Config ID | Config ID |  |
| Output Parameter | Pre-Change Quantity | Integer |  |
| Output Parameter | Post-Change Quantity | Integer |  |
| Output Parameter | Reason for Change | Enumeration |  |

## **3. When Item Is Added to Inventory**

![]()

**Node Functions**

This event is triggered when a new Item is added to the Inventory. The Owner of the Inventory Component will receive it. This event is not triggered by quantity-only changes

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Item Owner Entity | Entity |  |
| Output Parameter | Item Owner GUID | GUID |  |
| Output Parameter | Item Config ID | Config ID |  |
| Output Parameter | Quantity Obtained | Integer |  |

## **4. When the Quantity of Inventory Currency Changes**

![]()

**Node Functions**

This event is triggered when the amount of Inventory Currency changes. The Owner of the Inventory Component will receive it

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Currency Owner Entity | Entity |  |
| Output Parameter | Currency Owner GUID | GUID |  |
| Output Parameter | Currency Config ID | Config ID |  |
| Output Parameter | Currency Change Value | Integer |  |

## **5. When Items in the Inventory Are Used**

![]()

**Node Functions**

This event is triggered when an Item in the Inventory is used. The Owner of the Inventory Component will receive it

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Item Owner Entity | Entity |  |
| Output Parameter | Item Owner GUID | GUID |  |
| Output Parameter | Item Config ID | Config ID |  |
| Output Parameter | Amount to Use | Integer |  |

# XXV. Creation Patrol

## **1. When Creation Reaches Patrol Waypoint**

![]()

**Node Functions**

When the **Send Node Graph Event on Arrival** option is enabled for a waypoint in the Patrol template, a Node Graph Event is triggered once the specified conditions are met

This Node Graph Event can only be received by the creation's node graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Creation Entity | Entity | Runtime Creation Entity |
| Output Parameter | Creation GUID | GUID | The GUID of the Creation. If it was not an initially placed Creation, the output is empty |
| Output Parameter | Current Patrol Template ID | Integer | The Patrol Template ID currently active on this Creation |
| Output Parameter | Current Path Index | Integer | The Path ID referenced by the Creation's currently active Patrol Template |
| Output Parameter | Current Reached Waypoint ID | Integer | The Waypoint ID the Creation has currently reached |
| Output Parameter | Next Waypoint ID | Integer | The Waypoint ID the Creation will move to next |

# XXVI. Creation Preset Status

1.

## When Complex Creation Preset Status Changes

![]()

**Node Functions**

This event is triggered when the preset state of a complex creation is changed using the "Set the preset status value of the complex creation" node (the modified and unmodified values ​​must be different for this event to trigger).

This node graph event can only be received by the node graph of the complex creation.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Event Source Entity | Entity | Complex Creation Entity |
| Output Parameter | Event Source Entity GUID | GUID | Complex Creation GUID |
| Output Parameter | Preset Status Index | Integer |  |
| Output Parameter | Pre-Change Value | Integer |  |
| Output Parameter | Post-Change Value | Integer |  |

# XXVII. Floating Interaction Page

## **1. When Floating Interaction Page is Triggered**

![]()

**Node Functions**  
When the [Return to Server Event] option is enabled for a tab or single-choice window, confirming the interaction will trigger this event on the corresponding Player Entity's Server Node Graph

If the interaction is with an Interaction Page Close Button, Interactive Button, Item Display, or Custom utton in the floating interaction page, confirming it will also trigger this event on the corresponding Player Entity's Server Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Player Entity | Entity | Active Player Entity |
| Output Parameter | Player GUID | GUID | GUID of the Active Player Entity |
| Output Parameter | Floating Interaction Page Index | Integer | Unique Identifier for the Floating Interaction Page |
| Output Parameter | Interactive Item Index | Integer | Index of the control that triggered this event |
| Output Parameter | List Index | Integer List | List of indices for the tabs or single-choice windows. Each List Index output parameter corresponds to a Selected List Item output parameter |
| Output Parameter | Selected List Item | Integer List | Each tab or single-choice window can have at most one selected item. Each Selected List Item output parameter corresponds to a List Index output parameter |

Execution Nodes

Flow Control Nodes
