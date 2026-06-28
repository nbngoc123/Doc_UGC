# Tổng số Server Nodes: 464

## I. Custom Variables (Biến Tùy Chỉnh)
### 1. When Node Graph Variable Changes (Khi Biến của Node Graph thay đổi)
Sự kiện này được kích hoạt (triggered) khi một Biến (Node Graph Variable) trong Node Graph hiện tại bị thay đổi.

Giá trị trước (previous) và hiện tại (current) mang kiểu Chung (Generic). Cần xác định kiểu Generic để nhận đúng sự kiện cho các Biến có kiểu tương ứng.

Các Biến thuộc kiểu Vật chứa (Vessel-type) sẽ không cung cấp các tham số đầu ra chứa giá trị trước và sau khi thay đổi (before-value và after-value).

## II. Preset Status (Trạng thái Cài sẵn)
### 2. When Custom Variable Changes (Khi Biến Tùy chỉnh thay đổi)
Sự kiện này được kích hoạt khi Biến Tùy chỉnh (Custom Variable) của Thực thể (Entity) được liên kết với Node Graph hiện tại thay đổi.

Giá trị trước (previous) và hiện tại (current) mang kiểu Chung (Generic). Xác định kiểu Generic trước thì bạn mới có thể nhận đúng sự kiện cho các Biến Tùy chỉnh có kiểu tương ứng.

Các Biến Tùy chỉnh thuộc kiểu Vật chứa (Vessel-type) sẽ không cung cấp các tham số đầu ra chứa giá trị trước và sau khi thay đổi (before-value và after-value).

## III. Entity Related (Liên quan đến Thực thể)
### 1. When Preset Status Changes (Khi Trạng thái Cài sẵn thay đổi)
Sự kiện này được kích hoạt khi Trạng thái Cài sẵn (Preset Status) của Thực thể được liên kết với Node Graph thay đổi.

### 1. When Character Movement SPD Meets Condition (Khi Tốc độ di chuyển của Nhân vật đáp ứng Điều kiện)
Thêm hiệu ứng Trạng thái Đơn vị (Unit Status) [Monitor Movement Speed] (Theo dõi Tốc độ Di chuyển) vào Thực thể Nhân vật. Sự kiện này được kích hoạt khi các điều kiện được đáp ứng.

### 2. When Entity Is Created (Khi Thực thể được tạo ra)
Sự kiện này được kích hoạt khi một Thực thể (Entity) được tạo ra.

Tất cả các loại Thực thể đều có thể kích hoạt sự kiện này. Thực thể Màn chơi (Stage Entities), Thực thể Nhân vật (Character Entities) và Thực thể Người chơi (Player Entities) kích hoạt sự kiện này khi bước vào một Màn chơi (Stage).

### 3. When Entity Is Destroyed (Khi Thực thể bị phá hủy)
Sự kiện này kích hoạt khi các đối tượng và vật thể trong màn chơi bị phá hủy. Sự kiện này chỉ có thể kích hoạt trên các thực thể của màn chơi (stage entities).

## IV. Faction Related (Liên quan đến Phe phái)
### 4. When Entity Is Removed/Destroyed (Khi Thực thể bị Loại bỏ/Phá hủy)
This event is triggered when any Entity in the Stage is removed or destroyed, and it can only be triggered on Stage Entities
Sự kiện này được kích hoạt khi bất kỳ Thực thể nào trong Giai đoạn bị xóa hoặc bị tiêu diệt và nó chỉ có thể được kích hoạt trên Thực thể Giai đoạn

This event is triggered upon Entity destruction or removal. Therefore, when an Entity is destroyed, it triggers both the [On Entity Destroyed] and [On Entity Removed/Destroyed] events in sequence
Sự kiện này được kích hoạt khi Thực thể bị tiêu diệt hoặc loại bỏ. Do đó, khi một Thực thể bị tiêu diệt, nó sẽ kích hoạt cả hai sự kiện [Trên thực thể bị tiêu diệt] và [Trên thực thể bị xóa/hủy] theo trình tự

## V. Player and Character Related (Liên quan đến Người chơi và Nhân vật)
### 1. When Entity Faction Changes (Khi Phe phái Thực thể thay đổi)
This event is triggered when an Entity's Faction changes
Sự kiện này được kích hoạt khi Phe của Thực thể thay đổi

### 1. When the Character Is Down (Khi Nhân vật bị Đánh bại)
When a Character is Downed, the Node Graph on the Character Entity can trigger this event
Khi một Nhân vật bị hạ gục, Biểu đồ nút trên Thực thể Nhân vật có thể kích hoạt sự kiện này

### 2. When Character Revives (Khi Nhân vật Hồi sinh)
Khi một Nhân vật được Hồi sinh, Node Graph trên Thực thể Nhân vật có thể kích hoạt sự kiện này

### 3. When Player Teleport Completes (Khi Người chơi Hoàn thành Dịch chuyển)
Sự kiện này được kích hoạt trên Node Graph của Thực thể Người chơi khi Người chơi hoàn thành dịch chuyển

Sự kiện này cũng được kích hoạt khi Người chơi lần đầu tiên vào một Màn chơi

### 4. When All Player's Characters Are Down (Khi Tất cả Nhân vật của Người chơi bị Đánh bại)
Sự kiện này được kích hoạt trên Node Graph của Thực thể Người chơi khi tất cả Nhân vật của Người chơi bị Đánh bại

### 5. When All Player's Characters Are Revived (Khi Tất cả Nhân vật của Người chơi được Hồi sinh)
Sự kiện này được kích hoạt trên Node Graph của Thực thể Người chơi khi tất cả Nhân vật của Người chơi được Hồi sinh

### 6. When Player Is Abnormally Downed and Revives (Khi Người chơi bị Đánh bại Bất thường và Hồi sinh)
This event is triggered on the Player Entity when a Character is Downed and then Revived due to drowning, falling into an abyss, or similar reasons
Sự kiện này được kích hoạt trên Thực thể người chơi khi Nhân vật bị hạ gục và sau đó được hồi sinh do chết đuối, rơi xuống vực thẳm hoặc các lý do tương tự

## VI. Collision Trigger (Kích hoạt Va chạm)
### 7. When the Active Character Changes (Khi Nhân vật Hoạt động Thay đổi)
Available only in Classic Mode. This event is triggered on the player entity when the active character changes.
Chỉ khả dụng ở Chế độ cổ điển. Sự kiện này được kích hoạt trên thực thể người chơi khi nhân vật hoạt động thay đổi.

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Player Entity | Entity |  |
| Output Parameter | Player GUID | GUID |  |
| Output Parameter | Replaced Character Entity | Entity |  |
| Output Parameter | Current Active Character Entity | Entity |  |

### 1. When Entering Collision Trigger (Khi Bước Vào Vùng Va Chạm)
Khi phạm vi "Nguồn kích hoạt va chạm" (Collision Trigger Source) của một thực thể A (ví dụ: Người chơi) bước vào vùng "Kích hoạt va chạm" (Collision Trigger) của một thực thể B (ví dụ: Bức tượng).

Sự kiện Node Graph sẽ được gửi tới thực thể B - nơi được thiết lập "Kích hoạt va chạm".

## VII. Combat (Chiến đấu)
### 2. When Exiting Collision Trigger (Khi Thoát khỏi Vùng Va chạm)
This event is triggered when the "Collision Trigger Source" range of active Entity A leaves the "Collision Trigger" range of active Entity B.
Sự kiện này được kích hoạt khi phạm vi "Nguồn Kích hoạt Va chạm" của Thực thể A rời khỏi phạm vi "Kích hoạt Va chạm" của Thực thể B.

Node graph events will be sent to the entity B configured with "Collision Trigger".
Sự kiện Node Graph sẽ được gửi đến thực thể B được cấu hình "Kích hoạt Va chạm".

### 1. When HP Is Recovered (Khi HP được Phục hồi)
This event is triggered when an Entity's HP is restored.
Sự kiện này được kích hoạt khi HP của một Thực thể được phục hồi.

### 2. When Initiating HP Recovery (Khi Chủ động Phục hồi HP)
This event is triggered on the initiating Entity when an Entity restores HP to other Entities.
Sự kiện này được kích hoạt trên Thực thể chủ động khi nó phục hồi HP cho các Thực thể khác.

### 3. When Attack Hits (Khi Tấn công Trúng đích)
This event is triggered when an Entity's attack hits other Entities.
Sự kiện này được kích hoạt khi đòn tấn công của một Thực thể trúng các Thực thể khác.

(In Classic Mode, due to the Craftsperson's settings, the actual damage may differ from other scenarios.)
(Trong Chế độ Cổ điển, do cài đặt của Nhà sáng tạo (Craftsperson), sát thương thực tế có thể khác so với các tình huống khác.)

### 4. When Attacked (Khi Bị Tấn công)
This event is triggered when the Entity is attacked.
Sự kiện này được kích hoạt khi Thực thể bị tấn công.

(In Classic Mode, due to the Craftsperson's settings, the actual damage may differ from other scenarios.)
(Trong Chế độ Cổ điển, do cài đặt của Nhà sáng tạo, sát thương thực tế có thể khác so với các tình huống khác.)

## VIII. Motion Device (Thiết bị Chuyển động)
### 5. When Entering an Interruptible State (Khi Bước vào Trạng thái Có thể Bị ngắt quãng)
Available only in Beyond Mode.
Chỉ khả dụng trong Chế độ Beyond.

This event is triggered when an Entity is attacked and enters the Vulnerable Status.
Sự kiện này được kích hoạt khi một Thực thể bị tấn công và rơi vào Trạng thái Sơ hở (Vulnerable Status).

### 1. When Basic Motion Device Stops (Khi Thiết bị Chuyển động Cơ bản Dừng lại)
This event is sent to the Component Owner when a Basic Motion Device on the Basic Motion Device Component completes its movement or is disabled.
Sự kiện này được gửi đến Chủ sở hữu Thành phần khi một Thiết bị Chuyển động Cơ bản hoàn thành việc di chuyển hoặc bị vô hiệu hóa.

## IX. Hit Detection (Phát hiện Va chạm/Đánh trúng)
### 2. When Path Reaches Waypoint (Khi Đường dẫn Đi tới Điểm tham chiếu)
When the Pathing Motion Device reaches a Waypoint, it sends this event to the Owner of the Basic Motion Device Component. This event is triggered only if "Send Event on Waypoint Arrival" is enabled in the Waypoint settings.
Khi Thiết bị Chuyển động Theo đường dẫn (Pathing Motion Device) đi tới một Điểm tham chiếu (Waypoint), nó sẽ gửi sự kiện này đến Chủ sở hữu. Sự kiện này chỉ kích hoạt nếu tùy chọn "Gửi Sự kiện khi tới Điểm tham chiếu" được bật.

## X. Timer (Đồng hồ Hẹn giờ)
### 1. When On-Hit Detection Is Triggered (Khi Phát hiện Đánh trúng được Kích hoạt)
This event is triggered when the On-Hit Detection Component's Owner hits other Entities or the Scene.
Sự kiện này được kích hoạt khi Chủ sở hữu của Thành phần Phát hiện Đánh trúng (On-Hit Detection Component) va chạm với Thực thể khác hoặc Cảnh.

## XI. Global Timer (Đồng hồ Hẹn giờ Toàn cục)
### 1. When Timer Is Triggered (Khi Đồng hồ Hẹn giờ Kích hoạt)
This event is triggered when the Timer reaches the specified time node.
Sự kiện này được kích hoạt khi Đồng hồ Hẹn giờ đạt đến mốc thời gian được chỉ định.

### 1. Get Follow Motion Device Target (Lấy Mục tiêu của Thiết bị Chuyển động Bám theo)
Returns the Target of the Follow Motion Device, including the Target Entity and its GUID.
Trả về Mục tiêu của Thiết bị Chuyển động Bám theo (Follow Motion Device), bao gồm Thực thể Mục tiêu và GUID của nó.

## XII. UI Control Groups (Nhóm Điều khiển UI)
### 1. When Global Timer Is Triggered (Khi Đồng hồ Hẹn giờ Toàn cục Kích hoạt)
This event is triggered when the Global Countdown Timer reaches zero.
Sự kiện này được kích hoạt khi Đồng hồ Đếm ngược Toàn cục đếm ngược về 0.

The Global Stopwatch Timer does not trigger this event.
Đồng hồ Bấm giờ Toàn cục (Global Stopwatch Timer) sẽ không kích hoạt sự kiện này.

### 1. Get Current Global Timer Time (Lấy Thời gian Đồng hồ Hẹn giờ Toàn cục Hiện tại)
Returns the current time of the specified Global Timer on the Target Entity.
Trả về thời gian hiện tại của Đồng hồ Hẹn giờ Toàn cục được chỉ định trên Thực thể Mục tiêu.

## XIII. Unit Status (Trạng thái Đơn vị)
### 1. When UI Control Group Is Triggered (Khi Nhóm Điều khiển UI Kích hoạt)
This event is triggered only by UI controls of the following types: Interactive Button, Item Display, Custom Button, and Custom Switch.
Sự kiện này chỉ được kích hoạt bởi các điều khiển UI thuộc các loại sau: Nút Tương tác, Hiển thị Vật phẩm, Nút Tùy chỉnh và Công tắc Tùy chỉnh.

This event can only be received by the Player Node Graph that triggered the interaction.
Sự kiện này chỉ có thể được nhận bởi Node Graph của Người chơi đã kích hoạt tương tác.

### 1. When Unit Status Changes (Khi Trạng thái Đơn vị Thay đổi)
This event is triggered when the Stack Count of a Unit Status changes.
Sự kiện này được kích hoạt khi Số cộng dồn (Stack Count) của Trạng thái Đơn vị thay đổi.

This event is triggered when Unit Status effects are applied or removed.
Sự kiện này được kích hoạt khi hiệu ứng Trạng thái Đơn vị được áp dụng hoặc bị loại bỏ.

### 2. When Unit Status Ends (Khi Trạng thái Đơn vị Kết thúc)
This event is triggered when a Unit Status is removed for any reason or when its Runtime Duration expires.
Sự kiện này được kích hoạt khi Trạng thái Đơn vị bị gỡ bỏ vì bất kỳ lý do gì hoặc khi thời gian hiệu lực của nó kết thúc.

### 3. When Elemental Reaction Event Occurs (Khi Sự kiện Phản ứng Nguyên tố Xảy ra)
Adds the Unit Status effect [Monitor Elemental Reaction] to the Entity. This event is triggered when the conditions are met.
Thêm hiệu ứng Trạng thái Đơn vị [Theo dõi Phản ứng Nguyên tố] vào Thực thể. Sự kiện này được kích hoạt khi các điều kiện được đáp ứng.

## XIV. Tabs (Thẻ/Tab)
### 4. When Shield Is Attacked (Khi Khiên Bị Tấn công)
Adds the Unit Status effect [Add Shield] to the Entity. This event is triggered when the Shield takes damage.
Thêm hiệu ứng Trạng thái Đơn vị [Thêm Khiên] vào Thực thể. Sự kiện này được kích hoạt khi Khiên chịu sát thương.

## XV. Creations (Vật Tạo ra)
### 1. When Tab Is Selected (Khi Tab Được Chọn)
When the active tab is selected, it will send an event to the node graph.
Khi tab hoạt động được chọn, nó sẽ gửi một sự kiện đến Node Graph.

The Entity Node Graph configured by the Tab Component will receive this event.
Node Graph Thực thể được định cấu hình bởi Thành phần Tab sẽ nhận sự kiện này.

### 1. When Creation Enters Combat (Khi Vật Tạo ra Nhập Trận)
Only effective in Classic Aggro Mode.
Chỉ có hiệu lực trong Chế độ Aggro Cổ điển.

This event is triggered when a Creation enters battle.
Sự kiện này được kích hoạt khi một Vật Tạo ra (Creation) bước vào trạng thái chiến đấu.

## XVI. Classes (Lớp Nhân vật/Môn phái)
### 2. When Creation Leaves Combat (Khi Vật Tạo ra Rời Trận)
Only effective in Classic Aggro Mode.
Chỉ có hiệu lực trong Chế độ Aggro Cổ điển.

This event is triggered when a Creation leaves battle.
Sự kiện này được kích hoạt khi một Vật Tạo ra thoát khỏi trạng thái chiến đấu.

### 1. When Player Class Level Changes (Khi Cấp độ Lớp Người chơi Thay đổi)
This event is triggered when a Player's Class Level changes and is sent to the corresponding Player. It can be received in that Class's Node Graph.
Sự kiện này được kích hoạt khi Cấp độ Lớp (Class Level) của Người chơi thay đổi và được gửi đến Người chơi tương ứng. Sự kiện này có thể được nhận trong Node Graph của Lớp đó.

### 2. When Player Class Changes (Khi Lớp Người chơi Thay đổi)
This event is triggered when a Player's Class changes and is sent to the corresponding Player. It can be received in the Node Graph of the new Class.
Sự kiện này được kích hoạt khi Lớp của Người chơi thay đổi và được gửi đến Người chơi tương ứng. Có thể nhận sự kiện này trong Node Graph của Lớp mới.

## XVII. Skills (Kỹ năng)
### 3. When Player Class Is Removed (Khi Lớp Người chơi Bị Gỡ bỏ)
This event is triggered when a Player's Class is removed and sent to the corresponding Player. It can be received in the Node Graph of the previous Class.
Sự kiện này được kích hoạt khi Lớp của Người chơi bị gỡ bỏ và gửi đến Người chơi tương ứng. Có thể nhận sự kiện này trong Node Graph của Lớp trước đó.

## XVIII. Custom Aggro (Aggro Tùy chỉnh)
### 1. When Skill Node Is Called (Khi Node Kỹ năng Được Gọi)
This event is triggered by the [Notify Server Node Graph] Node in the Skill Node Graph. Up to three strings can be passed in.
Sự kiện này được kích hoạt bởi Node [Thông báo Server Node Graph] trong Skill Node Graph. Có thể truyền tối đa 3 chuỗi ký tự.

### 1. When Aggro Target Changes (Khi Mục tiêu Aggro Thay đổi)
Available only in Custom Aggro Mode.
Chỉ khả dụng trong Chế độ Aggro Tùy chỉnh.

This event is triggered when the Aggro Target changes.
Sự kiện này được kích hoạt khi Mục tiêu Aggro thay đổi.

This event can also be triggered when entering or leaving battle.
Sự kiện này cũng có thể được kích hoạt khi vào hoặc rời trạng thái chiến đấu.

### 2. When Self Enters Combat (Khi Bản thân Nhập Trận)
Available only in Custom Aggro Mode.
Chỉ khả dụng trong Chế độ Aggro Tùy chỉnh.

This event is triggered when the Entity itself enters battle.
Sự kiện này được kích hoạt khi chính Thực thể đó bước vào trạng thái chiến đấu.

### 2. Get Entity Unit Tag List (Lấy Danh sách Thẻ Đơn vị của Thực thể)
Returns a list of all Unit Tags carried by the Target Entity.
Trả về danh sách tất cả các Thẻ Đơn vị (Unit Tags) mà Thực thể Mục tiêu đang mang.

### 1. Query Global Aggro Transfer Multiplier (Truy vấn Hệ số Chuyển giao Aggro Toàn cục)
Searches the Global Aggro Transfer Multiplier; it can be configured in [Stage Settings].
Truy vấn Hệ số Chuyển giao Aggro Toàn cục; có thể được định cấu hình trong [Cài đặt Màn chơi].

### 2. Query the Aggro Multiplier of the Specified Entity (Truy vấn Hệ số Aggro của Thực thể được Chỉ định)
Query Aggro Multiplier of Specific Entity.
Truy vấn Hệ số Aggro của một Thực thể cụ thể.

### 3. Query the Aggro Value of the Specified Entity (Truy vấn Giá trị Aggro của Thực thể được Chỉ định)
Searches the Aggro Value of the Target Entity on its Aggro Owners.
Truy vấn Giá trị Aggro của Thực thể Mục tiêu đối với các Chủ sở hữu Aggro của nó.

### 4. Query if Specified Entity Is in Combat (Truy vấn xem Thực thể Chỉ định có Đang trong Trận chiến hay không)
Searches whether the specified Entity has entered battle.
Truy vấn xem Thực thể được chỉ định đã bước vào chiến đấu hay chưa.

### 5. Get List of Owners Who Have the Target in Their Aggro List (Lấy Danh sách Chủ sở hữu Có Mục tiêu trong Danh sách Aggro của Họ)
Searches which Entities' Aggro Lists include the specified Target Entity.
Truy vấn Danh sách Aggro của các Thực thể nào có bao gồm Thực thể Mục tiêu được chỉ định.

### 6. Get List of Owners That Have the Target As Their Aggro Target (Lấy Danh sách Chủ sở hữu Có Mục tiêu là Mục tiêu Aggro của Họ)
Searches which Entities have the Target Entity as their Aggro Target.
Truy vấn xem Thực thể nào lấy Thực thể Mục tiêu làm Mục tiêu Aggro của họ.

### 7. Get the Aggro List of the Specified Entity (Lấy Danh sách Aggro của Thực thể được Chỉ định)
Get Specific Entity's Aggro List.
Lấy Danh sách Aggro của Thực thể Cụ thể.

## XIX. Signals (Tín hiệu)
### 3. When Self Leaves Combat (Khi Bản thân Rời Trận)
Available only in Custom Aggro Mode.
Chỉ khả dụng trong Chế độ Aggro Tùy chỉnh.

This event is triggered when the Entity itself leaves battle.
Sự kiện này được kích hoạt khi chính Thực thể đó thoát khỏi trạng thái chiến đấu.

## XX. Deck Selector (Bộ chọn Thẻ bài/Deck)
### 1. Monitor Signal (Giám sát Tín hiệu)
Monitors Signal trigger events defined in the Signal Manager.
Giám sát các sự kiện kích hoạt Tín hiệu được định nghĩa trong Trình quản lý Tín hiệu.

The Signal name to monitor must be selected first.
Phải chọn trước tên Tín hiệu cần giám sát.

## XXI. Text Bubbles (Bong bóng Văn bản)
### 1. When Deck Selector Is Complete (Khi Bộ chọn Thẻ bài Hoàn thành)
This event is triggered on the Player's Node Graph when the Player completes the Deck Selector, or when it is forcibly closed due to time constraints.
Sự kiện này được kích hoạt trên Node Graph của Người chơi khi Người chơi hoàn thành Bộ chọn Thẻ bài, hoặc khi nó bị buộc đóng do hết thời gian.

The output parameters report the Deck Selector's result and the corresponding reason.
Các tham số đầu ra sẽ báo cáo kết quả của Bộ chọn Thẻ bài và lý do tương ứng.

## XXII. Shop (Cửa hàng)
### 1. When Text Bubble Is Completed (Khi Bong bóng Văn bản Hoàn thành)
This event can only be mounted by Text Bubble Components and is received by the Entity's Node Graph that completed the dialogue.
Sự kiện này chỉ có thể được liên kết bởi Thành phần Bong bóng Văn bản và được nhận bởi Node Graph của Thực thể đã hoàn thành hội thoại.

Completion refers to when the final line of dialogue has finished playing.
Sự hoàn thành ở đây nghĩa là khi câu thoại cuối cùng đã được phát xong.

### 1. When Selling Inventory Items in the Shop (Khi Bán Vật phẩm trong Kho cho Cửa hàng)
This event is triggered when Inventory items are sold in the Shop. The Owner of the Shop Component will receive it.
Sự kiện này được kích hoạt khi vật phẩm trong Kho được bán cho Cửa hàng. Chủ sở hữu của Thành phần Cửa hàng sẽ nhận được sự kiện này.

### 2. When Custom Shop Item Is Sold (Khi Vật phẩm Cửa hàng Tùy chỉnh được Bán)
This event is triggered when Custom items are sold in the Shop. The Owner of the Shop Component will receive it.
Sự kiện này được kích hoạt khi các Vật phẩm Tùy chỉnh được bán trong Cửa hàng. Chủ sở hữu của Thành phần Cửa hàng sẽ nhận được sự kiện này.

## XXIII. Equipment (Trang bị)
### 3. When selling items to the shop (Khi bán vật phẩm cho cửa hàng)
This event is triggered when items are purchased by the Shop. The Owner of the Shop Component will receive it.
Sự kiện này được kích hoạt khi các vật phẩm được Cửa hàng thu mua. Chủ sở hữu của Thành phần Cửa hàng sẽ nhận được sự kiện này.

### 1. When Equipment Is Equipped (Khi Trang bị được Mặc/Trang bị)
This event is triggered when Equipment is equipped. The Owner of the Equipment will receive it. Configure this in the Item Node Graph.
Sự kiện này được kích hoạt khi Trang bị được mặc lên người. Chủ sở hữu của Trang bị sẽ nhận sự kiện này. Cấu hình điều này trong Node Graph Vật phẩm.

### 2. When Equipment Is Unequipped (Khi Trang bị được Tháo ra)
This event is triggered when Equipment is unequipped. The Owner of the Equipment will receive it. Configure this in the Item Node Graph.
Sự kiện này được kích hoạt khi Trang bị bị tháo ra. Chủ sở hữu của Trang bị sẽ nhận sự kiện này. Cấu hình điều này trong Node Graph Vật phẩm.

### 3. When Equipment Is Initialized (Khi Trang bị được Khởi tạo)
When Equipment is first obtained and enters the Inventory, it is initialized. The event's output parameters return the unique ID of the Equipment instance. Use this ID to edit the Equipment dynamically. The Owner of the Equipment will receive this event. Configure this in the Item Node Graph.
Khi Trang bị lần đầu tiên thu thập được và đưa vào Kho, nó sẽ được khởi tạo. Tham số đầu ra của sự kiện trả về ID duy nhất của phiên bản Trang bị đó. Sử dụng ID này để chỉnh sửa Trang bị một cách linh hoạt. Chủ sở hữu của Trang bị sẽ nhận được sự kiện này. Cấu hình trong Node Graph Vật phẩm.

### 4. When Equipment Affix Value Changes (Khi Giá trị Phụ kiện/Từ tố Trang bị Thay đổi)
This event is triggered when Equipment Affix values change. The Owner of the Equipment will receive it. Configure this in the Item Node Graph.
Sự kiện này được kích hoạt khi giá trị Phụ kiện (Affix) của Trang bị thay đổi. Chủ sở hữu của Trang bị sẽ nhận được sự kiện này. Cấu hình trong Node Graph Vật phẩm.

### 5. When Equipment is purchased (Khi Trang bị được Mua)
The Inventory Owner Entity receives this event when it purchases equipment.
Thực thể Chủ sở hữu Kho nhận được sự kiện này khi mua trang bị.

This node is triggered only by item exchanges in the Inventory Shop. Custom shops do not trigger it. The Item Node Graph bound to the purchased equipment also receives this event.
Node này chỉ được kích hoạt bởi các giao dịch hoán đổi vật phẩm trong Cửa hàng Kho. Các cửa hàng tùy chỉnh sẽ không kích hoạt nó. Node Graph Vật phẩm liên kết với trang bị được mua cũng nhận được sự kiện này.

## XXIV. Items (Vật phẩm)
### 6. When Equipment is sold (Khi Trang bị được Bán)
The Inventory Owner Entity receives this event when it sells equipment.
Thực thể Chủ sở hữu Kho nhận được sự kiện này khi bán trang bị.

This node is triggered only by item exchanges in the Inventory Shop. Custom shops do not trigger it. The Item Node Graph bound to the purchased equipment also receives this event.
Node này chỉ được kích hoạt bởi các giao dịch hoán đổi vật phẩm trong Cửa hàng Kho. Các cửa hàng tùy chỉnh sẽ không kích hoạt nó. Node Graph Vật phẩm liên kết với trang bị được mua (bán) cũng nhận được sự kiện này.

### 1. When Item Is Lost From Inventory (Khi Vật phẩm Bị Mất khỏi Kho)
This event is triggered when an Item is removed from the Inventory (its quantity becomes 0). The Owner of the Inventory Component will receive it.
Sự kiện này được kích hoạt khi một Vật phẩm bị xóa khỏi Kho (số lượng bằng 0). Chủ sở hữu của Thành phần Kho sẽ nhận được nó.

### 2. When the Quantity of Inventory Item Changes (Khi Số lượng Vật phẩm trong Kho Thay đổi)
This event is triggered when the quantity of Items in the Inventory changes. The Owner of the Inventory Component will receive it.
Sự kiện này được kích hoạt khi số lượng Vật phẩm trong Kho bị thay đổi. Chủ sở hữu của Thành phần Kho sẽ nhận được nó.

### 3. When Item Is Added to Inventory (Khi Vật phẩm Được Thêm vào Kho)
This event is triggered when a new Item is added to the Inventory. The Owner of the Inventory Component will receive it. This event is not triggered by quantity-only changes.
Sự kiện này được kích hoạt khi một Vật phẩm mới được thêm vào Kho. Chủ sở hữu của Thành phần Kho sẽ nhận được nó. Sự kiện này không được kích hoạt nếu chỉ thay đổi số lượng của vật phẩm hiện có.

### 4. When the Quantity of Inventory Currency Changes (Khi Số lượng Tiền tệ trong Kho Thay đổi)
This event is triggered when the amount of Inventory Currency changes. The Owner of the Inventory Component will receive it.
Sự kiện này được kích hoạt khi số lượng Tiền tệ trong Kho thay đổi. Chủ sở hữu của Thành phần Kho sẽ nhận được nó.

## XXV. Creation Patrol (Vật Tạo ra Tuần tra)
### 5. When Items in the Inventory Are Used (Khi Vật phẩm trong Kho Được Sử dụng)
This event is triggered when an Item in the Inventory is used. The Owner of the Inventory Component will receive it.
Sự kiện này được kích hoạt khi một Vật phẩm trong Kho được sử dụng. Chủ sở hữu của Thành phần Kho sẽ nhận được nó.

## XXVII. Floating Interaction Page (Trang Tương tác Nổi)
### 1. When Creation Reaches Patrol Waypoint (Khi Vật Tạo ra Tới Điểm Tuần tra)
When the **Send Node Graph Event on Arrival** option is enabled for a waypoint in the Patrol template, a Node Graph Event is triggered once the specified conditions are met.
Khi tùy chọn **Gửi Sự kiện Node Graph Khi Tới nơi** được bật cho một điểm tham chiếu trong mẫu Tuần tra, một Sự kiện Node Graph sẽ được kích hoạt khi các điều kiện chỉ định được đáp ứng.

This Node Graph Event can only be received by the creation's node graph.
Sự kiện Node Graph này chỉ có thể được nhận bởi Node Graph của vật tạo ra đó.


This event is triggered when the preset state of a complex creation is changed using the "Set the preset status value of the complex creation" node (the modified and unmodified values ​​must be different for this event to trigger).
Sự kiện này được kích hoạt khi trạng thái cài sẵn của một vật tạo ra phức tạp (complex creation) bị thay đổi thông qua node "Cài đặt giá trị trạng thái cài sẵn của vật tạo ra phức tạp" (giá trị trước và sau khi sửa đổi phải khác nhau thì mới kích hoạt).

This node graph event can only be received by the node graph of the complex creation.
Sự kiện Node Graph này chỉ có thể được nhận bởi Node Graph của vật tạo ra phức tạp.

### 1. When Floating Interaction Page is Triggered (Khi Trang Tương tác Nổi Kích hoạt)
When the [Return to Server Event] option is enabled for a tab or single-choice window, confirming the interaction will trigger this event on the corresponding Player Entity's Server Node Graph.
Khi tùy chọn [Trả về Sự kiện Server] được bật cho một tab hoặc một cửa sổ lựa chọn đơn, việc xác nhận tương tác sẽ kích hoạt sự kiện này trên Server Node Graph của Thực thể Người chơi tương ứng.

If the interaction is with an Interaction Page Close Button, Interactive Button, Item Display, or Custom utton in the floating interaction page, confirming it will also trigger this event on the corresponding Player Entity's Server Node Graph
Nếu tương tác được thực hiện với Nút đóng trang tương tác, Nút tương tác, Hiển thị vật phẩm hoặc Utton tùy chỉnh trong trang tương tác nổi, việc xác nhận nó cũng sẽ kích hoạt sự kiện này trên Biểu đồ nút máy chủ của Thực thể người chơi tương ứng

## I. Common Nodes (Các Node Chung)
### 1. Print String (In Chuỗi ra Nhật ký)
Outputs a string to the log screen, typically used for logic testing and debugging.
Xuất một chuỗi (string) ra màn hình nhật ký (log), thường được dùng để kiểm tra logic và gỡ lỗi (debugging).

In the log, this string will be printed each time the logic runs successfully, regardless of whether this Node Graph is activated for display.
Trong nhật ký, chuỗi này sẽ được in ra mỗi khi logic chạy thành công, bất kể Node Graph này có được thiết lập hiển thị hay không.

### 2. Set Local Variable (Cài đặt Biến Cục bộ)
When connected with a Query Node named [Get Local Variable], this node will overwrite the Local Variable with a new value.
Khi được kết nối với Query Node (Node Truy vấn) có tên [Get Local Variable], node này sẽ ghi đè giá trị mới lên Biến Cục bộ đó.

### 3. Break Loop (Ngắt Vòng lặp)
Exits a Finite Loop or List Iteration Loop. The output pin must be connected to the [Break Loop] input pin of the [Finite Loop] or [List Iteration Loop] node.
Thoát khỏi Vòng lặp Hữu hạn (Finite Loop) hoặc Vòng lặp Duyệt Danh sách (List Iteration Loop). Chốt đầu ra (output pin) phải được kết nối với chốt đầu vào [Break Loop] của node [Finite Loop] hoặc [List Iteration Loop].

### 4. Finite Loop (Vòng lặp Hữu hạn - For loop)
Starting from the [Loop Start Value] to the [Loop End Value], the loop repeats continuously, increasing by 1 each time. In each iteration, it executes the Nodes connected to the [Loop Body] pin. After the full loop finishes, it executes the Nodes connected to the [Loop Complete] pin.
Bắt đầu từ [Loop Start Value] cho đến [Loop End Value], vòng lặp sẽ lặp lại liên tục, mỗi lần tăng thêm 1 đơn vị. Ở mỗi lần lặp, nó sẽ thực thi các Node được nối với chốt [Loop Body] (Thân vòng lặp). Sau khi lặp xong toàn bộ, nó sẽ thực thi các Node được nối với chốt [Loop Complete] (Hoàn thành vòng lặp).

[Break Loop] can be used to end the iteration early. After exiting the loop, the logic connected to the [Loop Complete] pin will also be executed.
Có thể dùng [Break Loop] để kết thúc quá trình lặp sớm. Sau khi thoát khỏi vòng lặp, logic được nối với chốt [Loop Complete] cũng sẽ được thực thi.

## II. List Operations (Các Thao tác với Danh sách)
### 5. Forwarding Event (Chuyển tiếp Sự kiện)
Forwards the Execution Flow's source event of this Node to the specified Target Entity. The event with the same name on the Target Entity's Node Graph will be triggered.
Chuyển tiếp sự kiện nguồn của Luồng Thực thi (Execution Flow) của Node này đến Thực thể Mục tiêu (Target Entity) được chỉ định. Sự kiện có cùng tên trên Node Graph của Thực thể Mục tiêu sẽ được kích hoạt.

### 1. Insert Value Into List (Chèn Giá trị vào Danh sách)
Inserts a value at the specified ID position in the selected List. The inserted value will appear at that ID after insertion.
Chèn một giá trị tại Vị trí ID (Chỉ mục) được chỉ định trong Danh sách đã chọn. Giá trị được chèn sẽ xuất hiện tại vị trí ID đó sau khi chèn.

For example: Inserting 5 at ID 2 in the List [1, 2, 3, 4] will produce [1, 2, 5, 3, 4] (5 appears at ID 2).
Ví dụ: Chèn 5 vào vị trí ID 2 trong Danh sách [1, 2, 3, 4] sẽ tạo ra [1, 2, 5, 3, 4] (số 5 xuất hiện tại ID 2).

### 2. Set List Value (Cài đặt Giá trị Danh sách)
Sets the value at a specified index position in the selected List.
Thiết lập giá trị tại một vị trí chỉ mục (index) được chỉ định trong Danh sách đã chọn.

### 3. Remove Value From List (Xóa Giá trị khỏi Danh sách)
Removes the value at the specified ID position from the selected List. All subsequent values will shift forward by one position.
Xóa giá trị tại Vị trí ID được chỉ định khỏi Danh sách đã chọn. Tất cả các giá trị ở phía sau sẽ dịch chuyển lên trước một vị trí.

### 4. List Iteration Loop (Vòng lặp Duyệt Danh sách)
Iterates through the specified List in sequential order.
Lặp qua Danh sách được chỉ định theo thứ tự tuần tự.

### 5. List Sorting (Sắp xếp Danh sách)
Sorts the specified List according to the chosen sorting method.
Sắp xếp Danh sách được chỉ định theo phương pháp sắp xếp đã chọn.

### 6. Concatenate List (Nối Danh sách)
Appends the input List to the end of the Target List. For example: Target List [1, 2, 3] with input [4, 5] becomes [1, 2, 3, 4, 5] after execution.
Nối Danh sách đầu vào vào cuối Danh sách Mục tiêu. Ví dụ: Danh sách Mục tiêu [1, 2, 3] với đầu vào [4, 5] trở thành [1, 2, 3, 4, 5] sau khi thực thi.

## III. Custom Variables (Biến Tùy Chỉnh)
### 7. Clear List (Xóa sạch Danh sách)
Empties the specified List.
Làm rỗng Danh sách được chỉ định.

### 1. Set Node Graph Variable (Cài đặt Biến Node Graph)
Sets the value of the specified Node Graph Variable in the current Node Graph.
Thiết lập giá trị của Biến Node Graph được chỉ định trong Node Graph hiện tại.

## IV. Preset Status (Trạng thái Được Lập trình Sẵn)
### 2. Set Custom Variable (Cài đặt Biến Tùy Chỉnh)
Sets the value of the specified Custom Variable on the Target Entity.
Thiết lập giá trị của Biến Tùy chỉnh được chỉ định trên Thực thể Mục tiêu.

## V. Entity Related (Liên quan đến Thực thể)
### 1. Set Preset Status (Cài đặt Trạng thái Được Lập trình Sẵn)
Sets the Preset Status of the specified Target Entity.
Thiết lập Trạng thái Cài sẵn (Preset Status) của Thực thể Mục tiêu được chỉ định.

### 1. Create Entity (Tạo Thực thể)
Creates an Entity by GUID. The Entity must be pre-placed in the Scene.
Tạo một Thực thể bằng GUID. Thực thể này phải được đặt sẵn từ trước trong Cảnh (Scene).

### 2. Create Prefab (Tạo Prefab)
Creates an Entity by Prefab ID.
Tạo một Thực thể bằng Prefab ID.

### 3. Create Prefab Group (Tạo Nhóm Prefab)
Creates the Entities included in the Prefab Group by Prefab Group ID.
Tạo các Thực thể có trong Nhóm Prefab bằng ID Nhóm Prefab.

### 4. Activate/Disable Model Display (Kích hoạt/Vô hiệu hóa Hiển thị Mô hình)
Edits the Entity's Model Display property to make its Model visible or hidden.
Chỉnh sửa thuộc tính Hiển thị Mô hình của Thực thể để làm cho Mô hình của nó được hiển thị hoặc bị ẩn đi.

### 5. Destroy Entity (Phá hủy Thực thể)
Destroying a specified Entity will result in a destruction effect and may also trigger post-destruction logic, such as end-of-life behaviors for local flying objects or dropping energy orbs from destroyed creations.
Phá hủy một Thực thể được chỉ định sẽ tạo ra hiệu ứng phá hủy và cũng có thể kích hoạt các logic sau khi phá hủy, chẳng hạn như hành vi khi kết thúc vòng đời của các vật thể bay cục bộ hoặc hiệu ứng rơi ra các quả cầu năng lượng từ các vật tạo ra (creations) bị phá hủy.

The [When Entity Is Destroyed] and [When Entity Is Removed/Destroyed] events can be monitored on Stage Entities.
Các sự kiện [Khi Thực thể Bị Phá hủy] và [Khi Thực thể Bị Gỡ bỏ/Phá hủy] có thể được giám sát trên Thực thể Màn chơi (Stage Entities).

## VI. Stage Related (Liên quan đến Màn chơi)
### 6. Remove Entity (Gỡ bỏ Thực thể)
Removing a specified Entity differs from destroying it; there is no destruction effect, and it does not trigger post-destruction logic, such as end-of-life behaviors in local flying objects or dropping energy orbs from removed creations.
Việc gỡ bỏ một Thực thể được chỉ định sẽ khác với việc phá hủy nó; sẽ không có hiệu ứng phá hủy, và nó sẽ không kích hoạt logic sau khi bị gỡ, chẳng hạn như hành vi kết thúc vòng đời ở các vật thể bay cục bộ hoặc hiệu ứng rơi ra quả cầu năng lượng.

Removing an Entity does not trigger the [On Entity Destroyed] event, but it may trigger the [On Entity Removed/Destroyed] event.
Việc gỡ bỏ một Thực thể không kích hoạt sự kiện [Khi Thực thể Bị Phá hủy], nhưng nó có thể kích hoạt sự kiện [Khi Thực thể Bị Gỡ bỏ/Phá hủy].

### 1. Settle Stage (Tổng kết Màn chơi)
Triggers the Stage Settlement process, which executes out-of-stage logic as defined in Stage Settlement.
Kích hoạt quá trình Tổng kết Màn chơi (Stage Settlement), quá trình này sẽ thực thi các logic ngoài màn chơi như được định nghĩa trong mục Tổng kết Màn chơi.

### 2. Set Current Environment Time (Cài đặt Thời gian Môi trường Hiện tại)
Immediately switches the Environment Time to the specified hour. The parameter must be a Floating Point Number between 0 and 24.
Ngay lập tức chuyển Thời gian Môi trường sang giờ được chỉ định. Tham số phải là một Số thực (Float) từ 0 đến 24.

If the target hour is earlier than the current hour, it is counted as the next day (+1 day).
Nếu giờ mục tiêu sớm hơn giờ hiện tại, nó sẽ được tính là sang ngày hôm sau (+1 ngày).

### 3. Set Environment Time Passage Speed (Cài đặt Tốc độ Trôi qua của Thời gian Môi trường)
The number of minutes that pass per second, limited from 0 to 60 (The speed in Teyvat is 1).
Số phút trong game trôi qua trên mỗi giây thực tế, giới hạn từ 0 - 60 (Tốc độ chuẩn ở Teyvat là 1).

## VIII. Faction Related (Liên quan đến Phe phái)
### 1. Set Entity Faction (Cài đặt Phe phái của Thực thể)
Sets the Faction of the specified Target Entity.
Thiết lập phe phái của Thực thể Mục tiêu được chỉ định.

## IX. Player and Character Related (Liên quan đến Người chơi và Nhân vật)
### 1. Teleport Player (Dịch chuyển Người chơi)
Teleports the specified Player Entity. A loading screen may appear depending on the movement distance.
Dịch chuyển Thực thể Người chơi được chỉ định. Màn hình chờ (loading) có thể xuất hiện tùy thuộc vào khoảng cách dịch chuyển.

If teleporting on top of an object, ensure the target Y coordinate is slightly higher than the landing position.
Nếu dịch chuyển lên trên một vật thể, hãy đảm bảo tọa độ Y mục tiêu cao hơn một chút so với vị trí tiếp đất.

### 2. Revive Character (Hồi sinh Nhân vật)
Available only in Beyond Mode, revives the specified Character Entity.
Chỉ khả dụng trong Chế độ Beyond, hồi sinh Thực thể Nhân vật được chỉ định.

### 3. Revive All Player's Characters (Hồi sinh Tất cả Nhân vật của Người chơi)
Revives all Character Entities of the specified Player, but this node only takes effect when the Player is in a state where all their characters have been downed.
Hồi sinh tất cả Thực thể Nhân vật của Người chơi được chỉ định, nhưng node này chỉ có hiệu lực khi Người chơi ở trạng thái mà tất cả nhân vật của họ đã bị hạ gục.

In Beyond Mode, since each player only has one character, this node has the same effect as the "Revive Character" node.
Trong Chế độ Beyond, vì mỗi người chơi chỉ có một nhân vật, node này có tác dụng hoàn toàn tương tự như node "Hồi sinh Nhân vật" (Revive Character).

In Classic Mode, a player can have multiple characters. If only some characters are downed, this node will have no effect, meaning it will not revive the downed characters.
Trong Chế độ Cổ điển (Classic), người chơi có thể có nhiều nhân vật. Nếu chỉ một số nhân vật bị hạ gục, node này sẽ không có hiệu lực, nghĩa là nó sẽ không hồi sinh các nhân vật đã bị hạ gục đó.

### 4. Defeat All Player's Characters (Hạ gục Tất cả Nhân vật của Người chơi)
Downs all characters of the specified player, causing the player to enter the *When All Player's Characters Are Down* state.
Đánh gục tất cả nhân vật của người chơi được chỉ định, khiến người chơi bước vào trạng thái *Khi Tất cả Nhân vật của Người chơi Bị Hạ gục*.

### 5. Activate Revive Point (Kích hoạt Điểm Hồi sinh)
Activates the specified Revive Point ID for the player. The next time the player triggers the Revive logic, they can revive at this Revive Point.
Kích hoạt ID Điểm Hồi sinh được chỉ định cho người chơi. Lần tới khi người chơi kích hoạt logic Hồi sinh, họ có thể hồi sinh tại Điểm Hồi sinh này.

### 6. Set Player Revive Time (Cài đặt Thời gian Hồi sinh của Người chơi)
Sets the duration for the Player's next revive. If the Player is currently reviving, this does not affect the ongoing revive process.
Cài đặt thời gian đếm ngược cho lần hồi sinh tiếp theo của Người chơi. Nếu Người chơi hiện đang trong quá trình hồi sinh, điều này không ảnh hưởng đến tiến trình hồi sinh đang diễn ra.

### 7. Set Player Remaining Revives (Cài đặt Số lượt Hồi sinh Còn lại của Người chơi)
Sets the number of remaining revives for the specified Player. When set to 0, the Player cannot revive.
Cài đặt số lượt hồi sinh còn lại cho Người chơi được chỉ định. Khi giá trị được đặt thành 0, Người chơi không thể hồi sinh.

### 8. Set Environment Configuration (Cài đặt Cấu hình Môi trường)
Applies the specified Environment Configuration to the target player. Takes effect immediately upon execution.
Áp dụng Cấu hình Môi trường được chỉ định cho người chơi mục tiêu. Sẽ có hiệu lực ngay khi thực thi.

### 9. Allow/Forbid Player to Revive (Cho phép/Cấm Người chơi Hồi sinh)
Sets whether the specified player is allowed to revive.
Cài đặt xem người chơi được chỉ định có được phép hồi sinh hay không.

### 10. Deactivate Revive Point (Hủy kích hoạt Điểm Hồi sinh)
Unregisters the specified Revive Point ID for the player. The next time, the player will not revive at this Revive Point.
Hủy đăng ký ID Điểm Hồi sinh được chỉ định cho người chơi. Lần tới, người chơi sẽ không thể hồi sinh tại Điểm Hồi sinh này.

### 11. Set Character's Elemental Energy (Cài đặt Năng lượng Nguyên tố của Nhân vật)
Available only in Classic Mode, sets the elemental energy for a specific character.
Chỉ khả dụng trong Chế độ Cổ điển, cài đặt mức năng lượng nguyên tố cho một nhân vật cụ thể.

### 12. Increase Character's Elemental Energy (Tăng Năng lượng Nguyên tố của Nhân vật)
Available only in Classic Mode, increases the elemental energy for a specific character.
Chỉ khả dụng trong Chế độ Cổ điển, tăng mức năng lượng nguyên tố cho một nhân vật cụ thể.

### 13. Revive the active character (Hồi sinh nhân vật đang hoạt động)
Available only in Classic Mode, revives the downed active character entity of the specified player.
Chỉ khả dụng trong Chế độ Cổ điển, hồi sinh thực thể nhân vật đang hoạt động (đã bị hạ gục) của người chơi được chỉ định.

### 14. Teleport Player (Classic Mode) (Dịch chuyển Người chơi (Chế độ Cổ điển))
Teleports the specified Player Entity. A loading screen may appear depending on the movement distance.
Dịch chuyển Thực thể Người chơi được chỉ định. Màn hình chờ (loading) có thể xuất hiện tùy thuộc vào khoảng cách dịch chuyển.

If teleporting on top of an object, the target Y coordinate should be slightly higher than the landing point.
Nếu dịch chuyển lên trên một vật thể, tọa độ Y của vị trí mục tiêu phải cao hơn một chút so với điểm tiếp đất.

## X. Collision (Va chạm)
### 1. Activate/Disable Extra Collision (Kích hoạt/Vô hiệu hóa Va chạm Phụ)
Edits the data in the Entity's Extra Collision Component to enable/disable Extra Collision.
Chỉnh sửa dữ liệu trong Thành phần Va chạm Phụ (Extra Collision Component) của Thực thể để bật/tắt Va chạm Phụ.

### 2. Activate/Disable Extra Collision Climbability (Kích hoạt/Vô hiệu hóa Khả năng Leo trèo của Va chạm Phụ)
Edits the Climbability of the Entity's Extra Collision Component.
Chỉnh sửa Khả năng Leo trèo (Climbability) của Thành phần Va chạm Phụ của Thực thể.

### 3. Activate/Disable Native Collision (Kích hoạt/Vô hiệu hóa Va chạm Gốc)
Edits the Entity's Native Collision.
Chỉnh sửa Va chạm Gốc (Native Collision) của Thực thể.

### 4. Activate/Disable Native Collision Climbability (Kích hoạt/Vô hiệu hóa Khả năng Leo trèo của Va chạm Gốc)
Edits the Climbability of the Entity's Native Collision.
Chỉnh sửa Khả năng Leo trèo của Va chạm Gốc của Thực thể.

## XI. Collision Triggers (Kích hoạt Va chạm)
### 1. Activate/Disable Collision Trigger (Kích hoạt/Vô hiệu hóa Kích hoạt Va chạm)
Edits the Collision Trigger Component's data to Activate/Disable the Trigger at the specified ID.
Chỉnh sửa dữ liệu của Thành phần Kích hoạt Va chạm (Collision Trigger Component) để Kích hoạt/Vô hiệu hóa Kích hoạt tại ID được chỉ định.

## XII. Combat (Chiến đấu)
### 1. Initiate Attack (Bắt đầu Tấn công)
Causes the specified Entity to initiate an attack. The Entity using this node must be configured with a corresponding Ability Unit.
Làm cho Thực thể được chỉ định bắt đầu một cuộc tấn công. Thực thể sử dụng node này phải được cấu hình Đơn vị Kỹ năng (Ability Unit) tương ứng.

There are two usage modes:
Có hai chế độ sử dụng:
When the Ability Unit is a [Hitbox Attack], it performs a hitbox attack centered on the Target Entity's Position.
Khi Đơn vị Kỹ năng là [Tấn công Hitbox] (Hitbox Attack), nó sẽ thực hiện một đòn tấn công hitbox lấy Vị trí của Thực thể Mục tiêu làm trung tâm.
When the Ability Unit is a [Direct Attack], it directly attacks the Target Entity.
Khi Đơn vị Kỹ năng là [Tấn công Trực tiếp] (Direct Attack), nó sẽ trực tiếp tấn công Thực thể Mục tiêu.

### 2. Recover HP (Phục hồi HP)
Restores HP to the specified Target Entity via an Ability Unit.
Phục hồi HP cho Thực thể Mục tiêu được chỉ định thông qua một Đơn vị Kỹ năng.

### 3. HP Loss (Mất HP)
Directly causes the specified target to lose HP. HP loss is not an attack, so it does not trigger attack-related events.
Trực tiếp làm cho mục tiêu được chỉ định bị mất HP. Mất HP không phải là một đòn tấn công, vì vậy nó không kích hoạt các sự kiện liên quan đến tấn công.

### 4. Recover HP Directly (Phục hồi HP Trực tiếp)
Directly restores HP to the specified Target Entity. Unlike [Recover HP], this node does not require an Ability Unit.
Trực tiếp phục hồi HP cho Thực thể Mục tiêu được chỉ định. Khác với [Phục hồi HP], node này không yêu cầu một Đơn vị Kỹ năng.

## XIII. Motion Devices (Thiết bị Chuyển động)
### 1. Recover Basic Motion Device (Tiếp tục Thiết bị Chuyển động Cơ bản)
Resumes a paused Basic Motion Device on the Target Entity. The Target Entity must have a Basic Motion Device Component.
Tiếp tục (Resume) một Thiết bị Chuyển động Cơ bản đang bị tạm dừng trên Thực thể Mục tiêu. Thực thể Mục tiêu phải có Thành phần Thiết bị Chuyển động Cơ bản.

### 2. Activate Fixed-Point Motion Device (Kích hoạt Thiết bị Chuyển động Điểm Cố định)
Dynamically adds a Fixed-Point Basic Motion Device to the Target Entity during Stage runtime.
Thêm động (dynamically add) một Thiết bị Chuyển động Cơ bản Điểm Cố định (Fixed-Point) vào Thực thể Mục tiêu trong thời gian chạy của Màn chơi.

### 3. Activate Basic Motion Device (Kích hoạt Thiết bị Chuyển động Cơ bản)
Activates the Basic Motion Device configured in the Target Entity's Basic Motion Device Component.
Kích hoạt Thiết bị Chuyển động Cơ bản được cấu hình trong Thành phần Thiết bị Chuyển động Cơ bản của Thực thể Mục tiêu.

### 4. Add Target-Oriented Rotation-Based Motion Device (Thêm Thiết bị Chuyển động Xoay Hướng tới Mục tiêu)
Dynamically adds a Basic Motion Device with Target-Oriented Rotation to the Target Entity during Stage runtime.
Thêm động một Thiết bị Chuyển động Cơ bản với khả năng Xoay Hướng tới Mục tiêu vào Thực thể Mục tiêu trong thời gian chạy của Màn chơi.

### 5. Add Uniform Basic Linear Motion Device (Thêm Thiết bị Chuyển động Tuyến tính Cơ bản Đều)
Dynamically adds a Basic Motion Device with Uniform Linear Motion during runtime.
Thêm động một Thiết bị Chuyển động Cơ bản với Chuyển động Tuyến tính Đều (Uniform Linear Motion) vào thời gian chạy.

### 6. Add Uniform Basic Rotation-Based Motion Device (Thêm Thiết bị Chuyển động Cơ bản Xoay Đều)
Dynamically adds a Basic Motion Device with Uniform Rotation during runtime.
Thêm động một Thiết bị Chuyển động Cơ bản với Chuyển động Xoay Đều (Uniform Rotation) vào thời gian chạy.

### 7. Stop and Delete Basic Motion Device (Dừng và Xóa Thiết bị Chuyển động Cơ bản)
Stops and deletes a running Motion Device.
Dừng và xóa một Thiết bị Chuyển động đang chạy.

### 8. Pause Basic Motion Device (Tạm dừng Thiết bị Chuyển động Cơ bản)
Pauses a running Motion Device. The Resume Motion Device node can then be used to resume it.
Tạm dừng một Thiết bị Chuyển động đang chạy. Node [Tiếp tục Thiết bị Chuyển động Cơ bản] sau đó có thể được sử dụng để tiếp tục.

## XIV. Follow Motion Device (Thiết bị Chuyển động Theo dõi)
### 1. Activate/Disable Follow Motion Device (Kích hoạt/Vô hiệu hóa Thiết bị Chuyển động Theo dõi)
Enables/Disables the Follow Motion Device logic on the Target Entity.
Bật/Tắt logic của Thiết bị Chuyển động Theo dõi trên Thực thể Mục tiêu.

### 2. Switch Follow Motion Device Target by GUID (Chuyển đổi Mục tiêu Theo dõi theo GUID)
Switches the Follow Motion Device's Tracking Target using a GUID.
Chuyển đổi Mục tiêu Theo dõi của Thiết bị Chuyển động Theo dõi bằng GUID.

### 3. Switch Follow Motion Device Target by Entity (Chuyển đổi Mục tiêu Theo dõi theo Thực thể)
Switches the Follow Motion Device's Tracking Target using an Entity.
Chuyển đổi Mục tiêu Theo dõi của Thiết bị Chuyển động Theo dõi bằng Thực thể.

## XV. Special Effects (Hiệu ứng Đặc biệt/VFX)
### 1. Play Timed Effects (Phát Hiệu ứng Có Thời hạn)
Plays a Timed Effect associated with the Target Entity. A valid Target Entity and Attachment Point are required.
Phát một Hiệu ứng Có Thời hạn (Timed Effect) liên quan đến Thực thể Mục tiêu. Bắt buộc phải có một Thực thể Mục tiêu và Điểm đính kèm (Attachment Point) hợp lệ.

### 2. Clear Special Effects Based on Special Effect Assets (Xóa các Hiệu ứng Dựa trên Tài nguyên Hiệu ứng)
Clears all Effects on the specified Target Entity that use the given Effect Asset. Applies only to Looping Effects.
Xóa tất cả các Hiệu ứng trên Thực thể Mục tiêu được chỉ định có sử dụng Tài nguyên Hiệu ứng (Effect Asset) đã cho. Chỉ áp dụng cho Hiệu ứng Lặp lại (Looping Effects).

### 3. Mount Looping Special Effect (Gắn Hiệu ứng Lặp lại)
Mounts a Looping Effect associated with the Target Entity. A valid Target Entity and Attachment Point are required.
Gắn một Hiệu ứng Lặp lại liên quan đến Thực thể Mục tiêu. Bắt buộc phải có Thực thể Mục tiêu và Điểm Đính kèm hợp lệ.

This node returns an Effect Instance ID that can be stored. Later, when using the [Clear Looping Effects] node, use this Effect Instance ID to clear the specified Looping Effect.
Node này trả về một ID Phiên bản Hiệu ứng (Effect Instance ID) có thể được lưu trữ. Sau này, khi sử dụng node [Xóa Hiệu ứng Lặp lại], hãy sử dụng ID Phiên bản Hiệu ứng này để xóa đúng Hiệu ứng đã chỉ định.

### 4. Clear Looping Special Effect (Xóa Hiệu ứng Lặp lại)
Clears the specified Looping Effect on the Target Entity using the Effect Instance ID. Upon successful mounting, the [Mount Looping Effect] node generates an Effect Instance ID.
Xóa Hiệu ứng Lặp lại đã chỉ định trên Thực thể Mục tiêu bằng ID Phiên bản Hiệu ứng. Sau khi gắn thành công, node [Gắn Hiệu ứng Lặp lại] sẽ tạo ra một ID Phiên bản Hiệu ứng.

## XVI. Timer (Đồng hồ Hẹn giờ)
### 1. Resume Timer (Tiếp tục Đồng hồ Hẹn giờ)
Resumes a paused Timer on the Target Entity.
Tiếp tục một Đồng hồ Hẹn giờ (Timer) đang tạm dừng trên Thực thể Mục tiêu.

### 2. Start Timer (Khởi động Đồng hồ Hẹn giờ)
Starts a Timer on the Target Entity.
Khởi động một Đồng hồ Hẹn giờ trên Thực thể Mục tiêu.

The Timer includes a Timer Sequence with or without looping. A Timer Sequence is a collection of time points in seconds sorted in ascending order; when the Timer reaches these points, it triggers the [On Timer Triggered] event.
Đồng hồ Hẹn giờ bao gồm một Chuỗi Thời gian (Timer Sequence) có lặp lại hoặc không lặp lại. Chuỗi Thời gian là một tập hợp các mốc thời gian tính bằng giây được sắp xếp theo thứ tự tăng dần; khi Đồng hồ Hẹn giờ đạt đến các mốc này, nó sẽ kích hoạt sự kiện [Khi Đồng hồ Hẹn giờ Kích hoạt].

When the Loop feature is set to "Yes", the Timer restarts from 0s after reaching the last time point.
Khi tính năng Vòng lặp (Loop) được đặt thành "Có", Đồng hồ Hẹn giờ sẽ tự động khởi động lại từ 0s sau khi đạt đến mốc thời gian cuối cùng.

### 3. Pause Timer (Tạm dừng Đồng hồ Hẹn giờ)
Pauses the specified Timer on the Target Entity. The [Resume Timer] node can then be used to continue the countdown.
Tạm dừng Đồng hồ Hẹn giờ được chỉ định trên Thực thể Mục tiêu. Node [Tiếp tục Đồng hồ Hẹn giờ] sau đó có thể được sử dụng để tiếp tục quá trình đếm.

### 4. Stop Timer (Dừng Đồng hồ Hẹn giờ)
Completely terminates the specified Timer on the Target Entity; it cannot be resumed.
Kết thúc hoàn toàn Đồng hồ Hẹn giờ được chỉ định trên Thực thể Mục tiêu; không thể tiếp tục được nữa.

## XVII. Global Timer (Đồng hồ Hẹn giờ Toàn cục)
### 1. Recover Global Timer (Khôi phục Đồng hồ Hẹn giờ Toàn cục)
Resumes a paused Global Timer on the Target Entity.
Tiếp tục Đồng hồ Hẹn giờ Toàn cục đang bị tạm dừng trên Thực thể Mục tiêu.

### 2. Start Global Timer (Khởi động Đồng hồ Hẹn giờ Toàn cục)
Starts a Global Timer on the Target Entity.
Khởi động một Đồng hồ Hẹn giờ Toàn cục trên Thực thể Mục tiêu.

### 3. Increase Global Timer Value (Tăng Giá trị Đồng hồ Hẹn giờ Toàn cục)
Adjusts the time of a running Global Timer via the Node Graph.
Điều chỉnh thời gian của Đồng hồ Hẹn giờ Toàn cục đang chạy thông qua Node Graph.

If the timer is paused first, then modified to 0s, followed by modifying the time to increase it, and finally resumed, the [When the Global Timer Is Triggered] event will not be triggered.
Nếu bộ hẹn giờ bị tạm dừng trước, sửa đổi thành 0, sau đó sửa đổi để tăng thời gian và cuối cùng tiếp tục lại, sự kiện [Khi Đồng hồ Hẹn giờ Toàn cục Kích hoạt] sẽ KHÔNG được kích hoạt.

### 4. Pause Global Timer (Tạm dừng Đồng hồ Hẹn giờ Toàn cục)
Pauses a running Global Timer via the Node Graph.
Tạm dừng Đồng hồ Hẹn giờ Toàn cục đang chạy thông qua Node Graph.

When paused, the UI controls linked to the timer will also pause their display.
Khi bị tạm dừng, các điều khiển UI được liên kết với bộ hẹn giờ cũng sẽ tạm dừng hiển thị.

### 5. Stop Global Timer (Dừng Đồng hồ Hẹn giờ Toàn cục)
Uses the node graph to stop running a global timer early.
Sử dụng Node Graph để kết thúc sớm một Đồng hồ hẹn giờ toàn cục.

## XVIII. Camera (Máy ảnh/Góc nhìn)
### 1. Switch Main Camera Template (Chuyển Mẫu Camera Chính)
Switches the Main Camera Template for the target Player List to the specified Template.
Chuyển Mẫu Camera Chính (Main Camera Template) cho Danh sách Người chơi mục tiêu sang Mẫu được chỉ định.

### 2. Set Player Camera to Follow Entity (Cài đặt Camera Người chơi Bám theo Thực thể)
Sets the specified Player Entity's camera to follow the target entity.
Cài đặt camera của Thực thể Người chơi được chỉ định để bám theo một thực thể mục tiêu.

### 3. Reset Player Camera to Follow Entity (Đặt lại Camera Bám theo Nhân vật)
Resets the player camera to follow the Player Entity.
Đặt lại camera của người chơi để trở lại bám theo Thực thể Người chơi (nhân vật của họ).

## XIX. Character Disruptor Device (Thiết bị Cản trở Nhân vật)
### 1. Set Character Disruptor Device (Cài đặt Thiết bị Cản trở Nhân vật)
Edits the Character Disruptor Device active on the Target Entity by ID; if the ID does not exist, the Character Disruptor Device will no longer function after the modification.
Chỉnh sửa Thiết bị Cản trở Nhân vật (Character Disruptor Device) đang hoạt động trên Thực thể Mục tiêu bằng ID; nếu ID không tồn tại, Thiết bị Cản trở Nhân vật sẽ không còn hoạt động sau khi sửa đổi.

## XX. Unit Status (Trạng thái Đơn vị)
### 1. Add Unit Status (Thêm Trạng thái Đơn vị)
Adds a specified Stack Count of Unit Status to the Target Entity.
Thêm một Số lượng Cộng dồn (Stack Count) Trạng thái Đơn vị nhất định vào Thực thể Mục tiêu.

### 2. Remove Unit Status (Gỡ bỏ Trạng thái Đơn vị)
Removes a specified Unit Status from the Target Entity. Either all stacks or a single stack can be removed.
Xóa một Trạng thái Đơn vị được chỉ định khỏi Thực thể Mục tiêu. Có thể xóa tất cả các cộng dồn hoặc chỉ xóa một cộng dồn.

## XXI. Tabs (Thẻ/Tab)
### 1. Activate/Disable Tab (Kích hoạt/Vô hiệu hóa Tab)
Edits the Tab state by ID in the Target Entity's Tab Component.
Chỉnh sửa trạng thái của Tab bằng ID trong Thành phần Tab của Thực thể Mục tiêu.

## XXII. Collision Trigger Source (Nguồn Kích hoạt Va chạm)
### 1. Activate/Disable Collision Trigger Source (Kích hoạt/Vô hiệu hóa Nguồn Kích hoạt Va chạm)
Edits the state of the Collision Trigger Source Component on the Target Entity.
Chỉnh sửa trạng thái của Thành phần Nguồn Kích hoạt Va chạm trên Thực thể Mục tiêu.

## XXIII. Class (Lớp/Môn phái)
### 1. Change Player's Current Class Level (Thay đổi Cấp độ Lớp Hiện tại của Người chơi)
Sets the Player's current Class Level. If it exceeds the defined range, the change will not take effect.
Cài đặt Cấp độ Lớp hiện tại của Người chơi. Nếu vượt quá phạm vi giới hạn, thay đổi sẽ không có hiệu lực.

### 2. Change Player Class (Thay đổi Lớp của Người chơi)
Sets the Player's current Class to the Class referenced by the Config ID and processes the Player's existing skills.
Chuyển Lớp hiện tại của Người chơi thành Lớp được tham chiếu bởi ID Cấu hình và xử lý các kỹ năng hiện có của Người chơi.

### 3. Increase Player's Current Class EXP (Tăng EXP Lớp Hiện tại của Người chơi)
Increases the Player's current Class EXP. Any excess beyond the maximum Level will not take effect.
Tăng EXP Lớp hiện tại của Người chơi. Số EXP vượt quá Cấp độ tối đa sẽ không được tính.

## XXIV. UI Control Groups (Nhóm Điều khiển UI)
### 1. Activate UI Control Group in Control Group Library (Kích hoạt Nhóm Điều khiển UI trong Thư viện)
Activates the UI Control Groups stored as Custom Templates in the UI Control Group Library within the Target Player's Interface Layout.
Kích hoạt các Nhóm Điều khiển UI được lưu trữ dưới dạng Mẫu Tùy chỉnh trong Thư viện Nhóm Điều khiển UI thuộc Bố cục Giao diện của Người chơi mục tiêu.

### 2. Switch Current Interface Layout (Chuyển đổi Bố cục Giao diện Hiện tại)
Switches the Target Player's current Interface Layout via Layout ID.
Chuyển đổi Bố cục Giao diện hiện tại của Người chơi Mục tiêu thông qua ID Bố cục.

### 3. Set UI Control (Group) Status (Cài đặt Trạng thái Điều khiển UI)
Edits the state of the UI Control in the Target Player's Interface Layout by its UI Control ID.
Chỉnh sửa trạng thái của Điều khiển UI trong Bố cục Giao diện của Người chơi Mục tiêu thông qua ID Điều khiển UI của nó.

### 4. Remove Interface Control Group From Control Group Library (Gỡ bỏ Nhóm Điều khiển Giao diện khỏi Thư viện)
Removes the UI Control Groups activated via [Activate UI Control Group in Control Group Library] from the Target Player's Interface Layout.
Gỡ bỏ Nhóm Điều khiển UI (đã được kích hoạt thông qua node Kích hoạt Nhóm Điều khiển UI) khỏi Bố cục Giao diện của Người chơi mục tiêu.

### 5. Play UI Animation on Control (Phát Hoạt ảnh UI trên Điều khiển)
Plays the VFX asset mounted to this UI animation control in the Player Entity's Interface Layout. To hide or disable the VFX, use the [Set UI Control (Group) Status] node. If this node is executed multiple times, the VFX can be played multiple times as well.
Phát tài nguyên hiệu ứng hình ảnh (VFX) được gắn vào điều khiển hoạt ảnh UI này trong Bố cục Giao diện của Thực thể Người chơi. Để ẩn hoặc vô hiệu hóa VFX, hãy sử dụng node [Cài đặt Trạng thái Điều khiển UI]. Nếu node này được thực thi nhiều lần, VFX cũng có thể được phát lại nhiều lần.

### 6. Refresh Notification Queue (Làm mới Hàng đợi Thông báo)
The Notification Queue UI Control allows for the transmission of a given set of data to be displayed via a node graph. Once transmitted, the data will be displayed in the specified Notification Queue UI Control according to the graphic-text group template entered.
Điều khiển UI Hàng đợi Thông báo (Notification Queue UI Control) cho phép truyền một tập hợp dữ liệu nhất định để hiển thị thông qua Node Graph. Sau khi truyền, dữ liệu sẽ được hiển thị trong Điều khiển UI Hàng đợi Thông báo được chỉ định theo mẫu nhóm văn bản/hình ảnh đã nhập.

## XXV. Skills (Kỹ năng)
### 1. Set Skill CD Based on Maximum CD Percentage (Cài đặt Hồi chiêu Dựa trên Phần trăm Kỹ năng Tối đa)
Modifies the skill in a character's skill slot by adjusting the percentage of the skill's maximum cooldown time.
Sửa đổi kỹ năng trong ô kỹ năng của nhân vật bằng cách điều chỉnh phần trăm thời gian hồi chiêu tối đa của kỹ năng.

### 2. Initialize Character Skill (Khởi tạo Kỹ năng Nhân vật)
Resets the Target Character's skills to those defined in the Class Template.
Đặt lại các kỹ năng của Nhân vật Mục tiêu về trạng thái nguyên bản được định nghĩa trong Mẫu Lớp (Class Template).

### 3. Set Skill Resource Amount (Cài đặt Lượng Tài nguyên Kỹ năng)
Edits the Character's skill resource amount.
Chỉnh sửa lượng tài nguyên kỹ năng của Nhân vật.

### 4. Set Character Skill CD (Cài đặt Thời gian Hồi chiêu Kỹ năng Nhân vật)
Directly sets the cooldown time of a specific skill slot on the target character to a specified value.
Trực tiếp thiết lập thời gian hồi chiêu của một ô kỹ năng cụ thể trên nhân vật mục tiêu thành một giá trị cụ thể.

### 5. Add Character Skill (Thêm Kỹ năng Nhân vật)
Adds a skill to the specified Target Character's Skill Slot.
Thêm một kỹ năng vào Ô kỹ năng của Nhân vật Mục tiêu được chỉ định.

### 6.** Increase Skill Resource Amount
Modifying the resource amount of a skill will add an increase to the current value; this increase can be a negative number.
Việc sửa đổi lượng tài nguyên của một kỹ năng sẽ tăng thêm giá trị hiện tại; mức tăng này có thể là một số âm.

### 7.** Increase Character Skill CD
Modifying the cooldown of a target character's skill slot will add an increase to the current cooldown time; this increase can be a negative number.
Việc sửa đổi thời gian hồi chiêu của ô kỹ năng của nhân vật mục tiêu sẽ tăng thêm thời gian hồi chiêu hiện tại; mức tăng này có thể là một số âm.

### 8. Delete Character Skill by Slot (Xóa Kỹ năng Nhân vật theo Ô)
Deletes the skill in the specified slot of the Target Character.
Xóa kỹ năng trong ô kỹ năng được chỉ định của Nhân vật Mục tiêu.

### 9. Delete Character Skill by ID (Xóa Kỹ năng Nhân vật theo ID)
Iterates through and deletes all skills with the specified Config ID across all of the Character's slots.
Lặp qua và xóa tất cả các kỹ năng có ID Cấu hình được chỉ định trên tất cả các ô kỹ năng của Nhân vật.

### 10. Bind Custom Skill Instance to Specified Slot (Liên kết Phiên bản Kỹ năng Tùy chỉnh với Ô Chỉ định)
Binds the specified skill instance to the specified skill slot.
Liên kết một phiên bản (instance) kỹ năng được chỉ định vào ô kỹ năng cụ thể.

### 11. Unbind Skill Instance (Hủy liên kết Phiên bản Kỹ năng)
Unbinds the specified skill instance from the Character Entity.
Hủy liên kết phiên bản kỹ năng được chỉ định khỏi Thực thể Nhân vật.

### 12. Unbind all Skill Instances on the Slot (Hủy liên kết Tất cả Phiên bản Kỹ năng trên Ô)
Unbinds all skill instances on the specified slot of the Character Entity.
Hủy liên kết tất cả các phiên bản kỹ năng trên ô được chỉ định của Thực thể Nhân vật.

### 13. Create Custom Skill Instance (Tạo Phiên bản Kỹ năng Tùy chỉnh)
Creates a skill instance from the specified config ID for the Character Entity.
Tạo một phiên bản kỹ năng từ ID Cấu hình được chỉ định cho Thực thể Nhân vật.

### 14. Destroy Custom Skill Instance (Phá hủy Phiên bản Kỹ năng Tùy chỉnh)
Destroys the specified skill instance on the Character Entity.
Phá hủy phiên bản kỹ năng được chỉ định trên Thực thể Nhân vật.

### 15. Cast Skill From Specified Panel Slot (Thi triển Kỹ năng Từ Ô Bảng Điều khiển)
Casts the skill currently active in the specified skill slot on the Character Entity.
Thi triển kỹ năng hiện đang hoạt động trong ô kỹ năng được chỉ định trên Thực thể Nhân vật.

This input works only if the skill is bound to a button and is currently active.
Đầu vào này chỉ hoạt động nếu kỹ năng đã được liên kết với một nút bấm và hiện đang ở trạng thái hoạt động.

## XXVI. Sound Effects (Hiệu ứng Âm thanh/SFX)
### 16. Cast Specified Skill Instance (Thi triển Phiên bản Kỹ năng Chỉ định)
Casts the skill corresponding to the specified skill instance ID on the Character Entity.
Thi triển kỹ năng tương ứng với ID Phiên bản Kỹ năng được chỉ định trên Thực thể Nhân vật.

This input works only if the skill is bound to a button and is currently active.
Đầu vào này chỉ hoạt động nếu kỹ năng đã được liên kết với một nút bấm và hiện đang ở trạng thái hoạt động.

### 1. Adjust Player Background Music Volume (Điều chỉnh Âm lượng Nhạc nền Người chơi)
Adjusts Player Background Music Volume.
Điều chỉnh Âm lượng Nhạc nền của Người chơi.

### 2. Adjust Specified Sound Effect Player (Điều chỉnh Trình phát Hiệu ứng Âm thanh Cụ thể)
Adjusts the volume and playback speed of the Sound Effect Player with the specified ID in the Sound Effect Player Component on the Target Entity.
Điều chỉnh âm lượng và tốc độ phát lại của Trình phát Hiệu ứng Âm thanh có ID được chỉ định trong Thành phần Trình phát SFX trên Thực thể Mục tiêu.

### 3. Close Specified Sound Effect Player (Đóng Trình phát Hiệu ứng Âm thanh Cụ thể)
Disables the Sound Effect Player with the specified ID in the Sound Effect Player Component on the specified Target Entity.
Vô hiệu hóa Trình phát Hiệu ứng Âm thanh có ID được chỉ định trong Thành phần Trình phát SFX trên Thực thể Mục tiêu.

### 4. Start/Pause Player Background Music (Bắt đầu/Tạm dừng Nhạc nền Người chơi)
Edits the background music state for the specified Player.
Chỉnh sửa trạng thái nhạc nền cho Người chơi được chỉ định.

### 5. Start/Pause Specified Sound Effect Player (Bắt đầu/Tạm dừng Trình phát Hiệu ứng Âm thanh Cụ thể)
Edits the state of the Sound Effect Player with the specified ID in the Sound Effect Player Component on the Target Entity. This node is only active when the sound effect is set to loop playback. It does not take effect for sound effects configured for single-playback.
Chỉnh sửa trạng thái của Trình phát SFX bằng ID được chỉ định trên Thực thể Mục tiêu. Node này chỉ có hiệu lực khi hiệu ứng âm thanh được đặt chế độ phát lặp lại (loop). Nó sẽ không hoạt động với các hiệu ứng âm thanh chỉ phát một lần.

### 6. Add Sound Effect Player (Thêm Trình phát Hiệu ứng Âm thanh)
Dynamically adds a Sound Effect Player. The Unit must have a Sound Effect Player Component.
Thêm động một Trình phát Hiệu ứng Âm thanh. Đơn vị này bắt buộc phải có Thành phần Trình phát SFX.

### 7. Player Plays One-Shot 2D Sound Effect (Người chơi Phát Hiệu ứng Âm thanh 2D Một lần)
Player plays a one-shot 2D Sound Effect.
Người chơi phát một Hiệu ứng Âm thanh 2D chỉ một lần duy nhất.

## XXVII. Unit Tags (Thẻ Đơn vị)
### 8. Set Player Background Music (Cài đặt Nhạc nền Người chơi)
Sets player background music parameters.
Cài đặt các thông số nhạc nền cho người chơi.

### 1. Clear Unit Tags from Entity (Xóa Thẻ Đơn vị khỏi Thực thể)
Clears Unit Tags for the specified Entity.
Xóa sạch Thẻ Đơn vị (Unit Tags) cho Thực thể được chỉ định.

### 2. Add Unit Tag to Entity (Thêm Thẻ Đơn vị vào Thực thể)
Adds Unit Tags to the specified Entity.
Thêm Thẻ Đơn vị vào Thực thể được chỉ định.

## XXVIII. Custom Aggro (Mục tiêu Kẻ thù Tùy chỉnh/Aggro)
### 3. Remove Unit Tag from Entity (Gỡ bỏ Thẻ Đơn vị khỏi Thực thể)
Removes Unit Tags from the specified Entity.
Gỡ bỏ Thẻ Đơn vị khỏi Thực thể được chỉ định.

### 1. Taunt Target (Khiêu khích Mục tiêu)
Available only in Custom Aggro Mode.
Chỉ khả dụng ở Chế độ Aggro (Khiêu khích/Mục tiêu Kẻ thù) Tùy chỉnh.

Makes the Taunter Entity taunt the specified Target Entity.
Làm cho Thực thể Khiêu khích (Taunter Entity) khiêu khích Thực thể Mục tiêu được chỉ định.

### 2. Remove Target Entity From Aggro List (Gỡ bỏ Thực thể Mục tiêu khỏi Danh sách Aggro)
Available only in Custom Aggro Mode.
Chỉ khả dụng ở Chế độ Aggro Tùy chỉnh.

Removes the Target Entity from the Aggro Owner's Aggro List; this may cause the target to leave battle.
Gỡ bỏ Thực thể Mục tiêu khỏi Danh sách Aggro của Chủ sở hữu Aggro; điều này có thể khiến mục tiêu thoát khỏi trạng thái chiến đấu.

### 3. Clear Specified Target's Aggro List (Xóa Danh sách Aggro của Mục tiêu Cụ thể)
Available only in Custom Aggro Mode.
Chỉ khả dụng ở Chế độ Aggro Tùy chỉnh.

Clears the Aggro Owner's Aggro List. This may cause them to leave battle.
Xóa sạch Danh sách Aggro của Chủ sở hữu. Điều này có thể khiến họ rời khỏi trạng thái chiến đấu.

## XXIX. Signals (Tín hiệu)
### 4. Set the Aggro Value of Specified Entity (Cài đặt Giá trị Aggro của Thực thể Cụ thể)
Available only in Custom Aggro Mode.
Chỉ khả dụng ở Chế độ Aggro Tùy chỉnh.

Sets the Aggro Value of the specified Target Entity on the specified Aggro Owner.
Cài đặt Giá trị Aggro của Thực thể Mục tiêu được chỉ định trên Chủ sở hữu Aggro.

## XXX. Nameplate (Biển tên)
### 1. Send Signal (Gửi Tín hiệu)
Sends a custom Signal to the global Stage. Before use, select the corresponding Signal name to ensure correct parameter usage.
Gửi một Tín hiệu (Signal) tùy chỉnh đến Màn chơi toàn cục. Trước khi sử dụng, hãy chọn tên Tín hiệu tương ứng để đảm bảo thông số truyền vào là chính xác.

## XXXI. Text Bubbles (Bong bóng Chat)
### 1. Set Entity Active Nameplate (Cài đặt Biển tên Hoạt động của Thực thể)
Sets the active Nameplate list for the specified target. Nameplates included in the input list are enabled, while those not included are disabled.
Cài đặt danh sách Biển tên hoạt động cho mục tiêu được chỉ định. Các biển tên có trong danh sách đầu vào sẽ được bật, trong khi những biển tên không có trong danh sách sẽ bị tắt.

## XXXII. Deck Selector (Trình chọn Bộ bài)
### 1. Switch Active Text Bubble (Chuyển đổi Bong bóng Chat Hoạt động)
In the Target Entity's Text Bubble Component, replaces the current active Text Bubble with the one corresponding to the Config ID.
Trong Thành phần Bong bóng Chat của Thực thể Mục tiêu, thay thế Bong bóng Chat hiện tại bằng bong bóng chat tương ứng với ID Cấu hình.

### 1. Close Deck Selector (Đóng Trình chọn Bộ bài)
Closes the currently active Deck Selector for the specified Player.
Đóng Trình chọn Bộ bài (Deck Selector) hiện đang mở của Người chơi được chỉ định.

### 2. Invoke Deck Selector (Gọi Trình chọn Bộ bài)
Opens the pre-made Deck Selector for the Target Player.
Mở Trình chọn Bộ bài đã được tạo sẵn cho Người chơi Mục tiêu.

## XXXIII. Stage Settlement (Tổng kết Màn chơi)
### 3. Random Deck Selector Selection List (Danh sách Chọn Lọc Ngẫu nhiên Trình chọn Bộ bài)
Randomly sorts the input List.
Sắp xếp ngẫu nhiên Danh sách đầu vào.

### 1. Set Player Settlement Success Status (Cài đặt Trạng thái Tổng kết Thành công của Người chơi)
Sets Player Settlement Success Status.
Cài đặt Trạng thái Thành công/Thất bại khi Tổng kết của Người chơi.

### 2. Set Player Settlement Scoreboard Data Display (Cài đặt Hiển thị Dữ liệu Bảng điểm Tổng kết Người chơi)
Sets the Player's Scoreboard display data, which is shown on the Scoreboard after Stage Settlement. Since this node involves the display of external functions, [Data Value] and [Data Name] currently support multilingual translation only when manually entering text. If entered via connection input, multilingual translation is not supported.
Cài đặt dữ liệu hiển thị Bảng điểm của Người chơi sau khi Tổng kết Màn chơi. Vì node này liên quan đến việc hiển thị giao diện bên ngoài, [Giá trị Dữ liệu] và [Tên Dữ liệu] hiện tại chỉ hỗ trợ dịch đa ngôn ngữ khi bạn nhập văn bản thủ công. Nếu dữ liệu được truyền vào thông qua chốt kết nối, nó sẽ không hỗ trợ đa ngôn ngữ.

### 3. Set Player Settlement Ranking Value (Cài đặt Giá trị Xếp hạng Tổng kết Người chơi)
Sets the Player's ranking value after Settlement, then determines the final ranking order according to [Ranking Value Comparison Order] in [Stage Settings] – [Settlement].
Cài đặt giá trị xếp hạng của Người chơi sau khi Tổng kết, sau đó xác định thứ tự xếp hạng cuối cùng theo [Thứ tự So sánh Giá trị Xếp hạng] trong [Cài đặt Màn chơi] – [Tổng kết].

### 4. Set Faction Settlement Success Status (Cài đặt Trạng thái Tổng kết Thành công của Phe phái)
Sets Faction Settlement Success Status.
Cài đặt Trạng thái Thành công/Thất bại khi Tổng kết của một Phe phái.

## XXXIV. Light Source Components (Thành phần Nguồn sáng)
### 5. Set Faction Settlement Ranking Value (Cài đặt Giá trị Xếp hạng Tổng kết Phe phái)
Sets the faction's ranking value after Settlement, then determines the final ranking order according to [Ranking Value Comparison Order] in [Stage Settings] – [Settlement].
Cài đặt giá trị xếp hạng của phe phái sau khi Tổng kết, sau đó xác định thứ tự xếp hạng cuối cùng theo [Thứ tự So sánh Giá trị Xếp hạng] trong [Cài đặt Màn chơi] – [Tổng kết].

## XXXV. Dictionary (Từ điển/Cấu trúc Dữ liệu Key-Value)
### 1. Toggle Entity Light Source (Bật/Tắt Nguồn sáng Thực thể)
Adjusts the Light Source state at the specified ID in the Light Source Component on the Target Entity.
Điều chỉnh trạng thái Nguồn sáng tại ID được chỉ định trong Thành phần Nguồn sáng trên Thực thể Mục tiêu.

### 1. Sort Dictionary by Key (Sắp xếp Từ điển theo Khóa)
Sorts and outputs the specified Dictionary by keys in ascending or descending order.
Sắp xếp và xuất Từ điển được chỉ định dựa trên các khóa (Key) theo thứ tự tăng dần hoặc giảm dần.

### 2. Sort Dictionary by Value (Sắp xếp Từ điển theo Giá trị)
Sorts and outputs the specified Dictionary by values in ascending or descending order.
Sắp xếp và xuất Từ điển được chỉ định dựa trên các giá trị (Value) theo thứ tự tăng dần hoặc giảm dần.

### 3. Set or Add Key Value Pairs to Dictionary (Cài đặt hoặc Thêm Cặp Khóa-Giá trị vào Từ điển)
Adds a Key-Value Pair to the specified Dictionary.
Thêm một cặp Khóa-Giá trị (Key-Value Pair) vào Từ điển được chỉ định.

### 4. Clear Dictionary (Xóa sạch Từ điển)
Clears all Key-Value Pairs from the specified Dictionary.
Xóa tất cả các cặp Khóa-Giá trị khỏi Từ điển được chỉ định.

## XXXVI. Structures (Cấu trúc Data/Struct)
### 5. Remove Key Value Pairs from Dictionary by Key (Xóa Cặp Khóa-Giá trị khỏi Từ điển theo Khóa)
Removes Key-Value Pairs from the specified Dictionary by key.
Xóa cặp Khóa-Giá trị khỏi Từ điển được chỉ định bằng cách tìm Khóa tương ứng.

## XXXVII. Shop (Cửa hàng)
### 1. Modify Structure (Chỉnh sửa Cấu trúc)
After selecting a Structure, you can edit each parameter of that Structure.
Sau khi chọn một Cấu trúc (Struct), bạn có thể chỉnh sửa từng thông số bên trong Cấu trúc đó.

### 1. Remove Item From Inventory Shop Sales List (Gỡ Vật phẩm khỏi Danh sách Bán Cửa hàng Túi đồ)
Removes items from the inventory shop's sales list.
Gỡ bỏ các vật phẩm khỏi danh sách bày bán của Cửa hàng Túi đồ (Inventory Shop).

### 2. Remove Item From Purchase List (Gỡ Vật phẩm khỏi Danh sách Thu mua)
Removes items from the purchase list.
Gỡ bỏ các vật phẩm khỏi Danh sách Thu mua (Purchase List).

### 3. Remove Item From Custom Shop Sales List (Gỡ Vật phẩm khỏi Danh sách Bán Cửa hàng Tùy chỉnh)
Removes items from the custom shop's sales list.
Gỡ bỏ các vật phẩm khỏi danh sách bày bán của Cửa hàng Tùy chỉnh (Custom Shop).

### 4. Open Shop (Mở Cửa hàng)
Opens the Shop from the Player Entity's perspective during gameplay.
Mở Cửa hàng dưới góc nhìn của Thực thể Người chơi trong quá trình chơi game.

### 5. Close Shop (Đóng Cửa hàng)
Closes all open Shops from the Player Entity's perspective during gameplay.
Đóng tất cả các Cửa hàng đang mở trên màn hình của Thực thể Người chơi trong quá trình chơi game.

### 6. Add New Item to Inventory Shop Sales List (Thêm Vật phẩm Mới vào Danh sách Bán Cửa hàng Túi đồ)
Adds new items to the inventory shop's sales list.
Thêm mặt hàng mới vào danh sách bày bán của Cửa hàng Túi đồ.

### 7. Add Items to the Purchase List (Thêm Vật phẩm vào Danh sách Thu mua)
Adds New Items to the Item Purchase List.
Thêm mặt hàng mới vào danh sách Thu mua Vật phẩm.

### 8. Add New Item to Custom Shop Sales List (Thêm Vật phẩm Mới vào Danh sách Bán Cửa hàng Tùy chỉnh)
Adds items to the Custom Shop Sales List. Upon success, an Integer ID is generated in the Output Parameter as the item identifier.
Thêm mặt hàng vào Danh sách Bán của Cửa hàng Tùy chỉnh. Sau khi thành công, một ID Số nguyên sẽ được tạo ra ở Tham số Đầu ra để làm định danh cho vật phẩm đó.

### 9. Set Inventory Shop Item Sales Info (Cài đặt Thông tin Bán Vật phẩm Cửa hàng Túi đồ)
Sets up information on items for sale in the inventory shop.
Thiết lập thông tin bán hàng cho các vật phẩm trong Cửa hàng Túi đồ.

### 10. Set Item Purchase Info in the Purchase List (Cài đặt Thông tin Thu mua Vật phẩm trong Danh sách)
Sets up item acquisition table.
Thiết lập bảng thu thập vật phẩm (Mua lại từ người chơi).

## XXXVIII. Equipment
### 11. Set Custom Shop Item Sales Info (Cài đặt Thông tin Bán Vật phẩm Cửa hàng Tùy chỉnh)
Sets custom store product sales information.
Thiết lập thông tin bán sản phẩm trong Cửa hàng Tùy chỉnh.

### 1. Set Equipment Affix Value (Cài đặt Giá trị Phụ gia Trang bị)
Sets the value on the corresponding entry for a specified equipment instance.
Cài đặt giá trị trên mục nhập tương ứng cho một phiên bản (instance) trang bị cụ thể.

### 2. Remove Equipment Affix (Gỡ bỏ Phụ gia Trang bị)
Removes the specified Affix from the Equipment instance.
Gỡ bỏ Phụ gia (Affix) được chỉ định khỏi phiên bản Trang bị.

### 3. Add Affix to Equipment (Thêm Phụ gia vào Trang bị)
Adds a preconfigured Affix to the specified Equipment instance, with the option to overwrite the Affix value.
Thêm một Phụ gia đã được cấu hình sẵn vào phiên bản Trang bị được chỉ định, kèm theo tùy chọn ghi đè giá trị Phụ gia.

### 4. Add Affix to Equipment at Specified ID (Thêm Phụ gia vào Trang bị tại ID Cụ thể)
Adds a preconfigured Affix at the specified Affix ID on the Equipment instance, with the option to overwrite the Affix value.
Thêm một Phụ gia đã được cấu hình sẵn tại ID Phụ gia được chỉ định trên phiên bản Trang bị, kèm theo tùy chọn ghi đè giá trị Phụ gia.

### 5. Replace Equipment to the Specified Slot (Thay thế Trang bị vào Ô Cụ thể)
Replaces the specified equipment in the corresponding equipment slot of the target entity.
Thay thế trang bị được chỉ định vào ô trang bị tương ứng của thực thể mục tiêu.

If the equipment is already equipped in the equipment slot, the replacement will not take effect.  
Nếu trang bị đó đã được lắp sẵn trong ô trang bị, việc thay thế sẽ không có tác dụng.
  
If the target slot already contains an equipped item, that item will be replaced.
Nếu ô mục tiêu đã chứa một vật phẩm được trang bị, vật phẩm đó sẽ bị thay thế.

## XXXIX. Items and Inventory (Vật phẩm và Túi đồ)
### 6. Remove Equipment from Specified Slot (Tháo Trang bị khỏi Ô Cụ thể)
Removes the equipment from the specified slot (by row and column).
Tháo trang bị khỏi ô được chỉ định (theo hàng và cột).

### 1. Set Inventory Item Drop Contents (Cài đặt Nội dung Rơi Vật phẩm Túi đồ)
Configures the Inventory Item drop data in Dictionary format, and specifies the Drop Type.
Định cấu hình dữ liệu vật phẩm rơi (drop) dưới định dạng Từ điển (Dictionary) và chỉ định Loại Rơi (Drop Type).

### 2. Set Inventory Drop Items/Currency Amount (Cài đặt Số lượng Vật phẩm/Tiền Rơi của Túi đồ)
Sets the type and quantity of Items or Currency for the Inventory drop.
Cài đặt loại và số lượng Vật phẩm hoặc Tiền tệ sẽ rơi ra từ Túi đồ.

### 3. Trigger Loot Drop (Kích hoạt Rơi Chiến lợi phẩm)
Triggers a loot drop for the dropper entity, with configurable loot type.
Kích hoạt việc rơi chiến lợi phẩm (loot drop) cho thực thể tạo rơi rớt (dropper entity), với loại chiến lợi phẩm có thể tùy chỉnh.

### 4. Set Loot Drop Content (Cài đặt Nội dung Rơi Chiến lợi phẩm)
Configures the Loot drop data in the Loot Component on the Dropper Entity in Dictionary format.
Định cấu hình dữ liệu rơi Chiến lợi phẩm trong Thành phần Chiến lợi phẩm (Loot Component) trên Thực thể Tạo Rơi rớt dưới định dạng Từ điển.

### 5. Increase Inventory Item Quantity (Tăng Số lượng Vật phẩm Túi đồ)
Modifying the quantity of a specified item in your inventory will add an increase to the current value; the increase can be a negative number.
Việc sửa đổi số lượng của một vật phẩm được chỉ định trong túi đồ của bạn sẽ cộng thêm một mức tăng vào giá trị hiện tại; mức tăng này có thể là số âm (nghĩa là giảm đi).

### 6. Increase Inventory Currency Quantity (Tăng Số lượng Tiền tệ Túi đồ)
Modifies the amount of a specified currency in the player's inventory. This will add the specified increase value to the current amount, and the increase value can be negative.
Sửa đổi số lượng của một loại tiền tệ cụ thể trong túi đồ của người chơi. Điều này sẽ cộng thêm một mức tăng chỉ định vào số tiền hiện tại, và mức tăng có thể là số âm.

### 7. Increase Loot Component Item Quantity (Tăng Số lượng Vật phẩm trong Thành phần Chiến lợi phẩm)
Modifies the quantity of a specified item in the drop component of a loot prefab. This will add the specified increase value to the current quantity, and the increase value can be negative.
Sửa đổi số lượng của một vật phẩm cụ thể trong thành phần rơi rớt của prefab chiến lợi phẩm. Điều này sẽ cộng thêm giá trị tăng vào số lượng hiện tại, và giá trị tăng có thể là âm.

### 8. Increase Loot Component Currency Quantity (Tăng Số lượng Tiền tệ trong Thành phần Chiến lợi phẩm)
Modifies the amount of a specified currency in the drop component of a loot prefab. This will add the specified increase value to the current amount, and the increase value can be negative.
Sửa đổi số lượng của một loại tiền cụ thể trong thành phần rơi rớt của prefab chiến lợi phẩm. Điều này sẽ cộng thêm giá trị tăng vào lượng tiền hiện tại, và giá trị tăng có thể là âm.

### 9. Increase Maximum Inventory Capacity (Tăng Sức chứa Tối đa của Túi đồ)
Increases the maximum Inventory capacity of the specified Inventory Owner.
Tăng giới hạn sức chứa (capacity) tối đa của túi đồ đối với Chủ sở hữu Túi đồ (Inventory Owner) được chỉ định.

## XL. Mini-Map Marker Component (Thành phần Điểm đánh dấu Bản đồ nhỏ)
### 1. Set Player List for Visible Mini-Map Markers (Cài đặt Danh sách Người chơi được Thấy Điểm đánh dấu)
The mini-map marker at the specified ID in the Target Entity's Mini-map Marker Component is visible to all Players in the Player List.
Điểm đánh dấu bản đồ nhỏ (mini-map marker) tại ID được chỉ định trong Thành phần Đánh dấu Bản đồ nhỏ của Thực thể Mục tiêu sẽ hiển thị cho tất cả Người chơi có trong Danh sách.

### 2. Set Player Markers on the Mini-Map (Cài đặt Điểm đánh dấu Người chơi trên Bản đồ nhỏ)
When the Player Marker option is selected and a corresponding Player Entity is linked in the Node Graph, the Target Entity's display on the mini-map changes to that Player's avatar.
Khi tùy chọn Đánh dấu Người chơi được chọn và một Thực thể Người chơi tương ứng được liên kết trong Node Graph, hiển thị của Thực thể Mục tiêu trên bản đồ nhỏ sẽ thay đổi thành ảnh đại diện (avatar) của Người chơi đó.

### 3. Set Mini-Map Marker Activation Status (Cài đặt Trạng thái Kích hoạt Điểm đánh dấu Bản đồ nhỏ)
Edits the active state of mini-map markers on the Target Entity in batches using the input list of Mini-map Marker IDs.
Chỉnh sửa hàng loạt trạng thái hoạt động của các điểm đánh dấu bản đồ nhỏ trên Thực thể Mục tiêu bằng cách sử dụng danh sách ID Điểm đánh dấu đầu vào.

### 4. Set Mini-Map Zoom (Cài đặt Phóng to Bản đồ nhỏ)
Sets the map scale of the mini-map interface control for the target player.
Cài đặt tỷ lệ bản đồ của điều khiển giao diện bản đồ nhỏ cho người chơi mục tiêu.

### 5. Set Player List for Tracking Mini-Map Markers (Cài đặt Danh sách Người chơi để Theo dõi Điểm đánh dấu)
Sets the mini-map marker of the target entity with the corresponding index to a tracking appearance for the specified player.
Cài đặt điểm đánh dấu bản đồ nhỏ của thực thể mục tiêu (với chỉ mục tương ứng) thành giao diện theo dõi dành cho người chơi được chỉ định.

### 6. Switch Custom Maps (Chuyển đổi Bản đồ Tùy chỉnh)
Allows switching the Target Player's currently active minimap configuration.
Cho phép chuyển đổi cấu hình bản đồ nhỏ hiện đang hoạt động của Người chơi Mục tiêu.

## XLI. Creation Patrol (Tuần tra của Vật tạo ra)
### 1. Switch Creation Patrol Template (Chuyển đổi Mẫu Tuần tra của Vật tạo ra)
Immediately switches the patrol template for the Creation and moves according to the new template.
Lập tức chuyển đổi mẫu tuần tra (patrol template) cho Vật tạo ra (Creation) và di chuyển theo mẫu mới.

## XLII. Leaderboard (Bảng xếp hạng)
### 1. Set Player Leaderboard Score as a Float (Cài đặt Điểm Xếp hạng Người chơi dạng Số thực)
Sets Player Leaderboard Score (Float).
Cài đặt Điểm trên Bảng xếp hạng Người chơi (Kiểu Số thực - Float).

### 2. Set Player Leaderboard Score as an Integer (Cài đặt Điểm Xếp hạng Người chơi dạng Số nguyên)
Sets Player Leaderboard Score (Integer).
Cài đặt Điểm trên Bảng xếp hạng Người chơi (Kiểu Số nguyên - Integer).

## XLIII. Achievements (Thành tựu)
### 1. Increase Achievement Progress Tally (Tăng Số đếm Tiến trình Thành tựu)
Changes the progress counter for the specified Achievement ID on the Target Entity.
Thay đổi bộ đếm tiến trình cho ID Thành tựu được chỉ định trên Thực thể Mục tiêu.

### 2. Set Achievement Progress Tally (Cài đặt Số đếm Tiến trình Thành tựu)
Sets the progress counter for the specified Achievement ID on the Target Entity.
Cài đặt bộ đếm tiến trình cho ID Thành tựu được chỉ định trên Thực thể Mục tiêu.

## XLIV. Scan Tags (Thẻ Quét)
### 1. Set Scan Tag Rules (Cài đặt Quy tắc Thẻ Quét)
Configures rules for Scan Tags. The scanning logic is executed based on the configured rules.
Định cấu hình các quy tắc cho Thẻ Quét (Scan Tags). Logic quét sẽ được thực thi dựa trên các quy tắc đã cấu hình.

### 2. Set Scan Component's Active Scan Tag ID (Cài đặt ID Thẻ Quét Hoạt động của Thành phần Quét)
Sets the Scan Tag with the specified ID in the Target Entity's Scan Tag Component to the active state.
Cài đặt Thẻ Quét có ID cụ thể trong Thành phần Thẻ Quét của Thực thể Mục tiêu sang trạng thái hoạt động.

## XLV. Rank (Hạng cạnh tranh)
### 1. Switch the Scoring Group that Affects Player's Competitive Rank (Chuyển đổi Nhóm tính điểm Ảnh hưởng đến Hạng cạnh tranh của Người chơi)
Switches the active Scoring Group of the specified Player's Ranking by Scoring Group ID.
Chuyển đổi Nhóm tính điểm đang hoạt động cho Xếp hạng của Người chơi cụ thể bằng ID Nhóm tính điểm.

### 2. Set Player Rank Score Change (Cài đặt Thay đổi Điểm Hạng Người chơi)
Sets the Player's rank score change based on the settlement status.
Cài đặt mức thay đổi điểm hạng của Người chơi dựa trên trạng thái tổng kết.

## XLVI. Entity Deployment Group (Nhóm Triển khai Thực thể)
### 1. Activate/Disable Entity Deployment Group (Kích hoạt/Vô hiệu hóa Nhóm Triển khai Thực thể)
Edits the Initial Creation Switch state of the Entity Layout Group.
Chỉnh sửa trạng thái Công tắc Tạo Ban đầu (Initial Creation Switch) của Nhóm Bố cục Thực thể.

## XLVII. Chat Channel (Kênh Chat)
### 1. Set Chat Channel Switch (Cài đặt Công tắc Kênh Chat)
Configures the voice and text toggles for the chat channel.
Định cấu hình công tắc bật/tắt tính năng chat thoại (voice) và chat chữ (text) cho kênh trò chuyện.

### 2. Set Player's Current Channel (Cài đặt Kênh Hiện tại của Người chơi)
Sets the Player's currently available channels. Channels in the list are available to the Player, and channels not in the list are unavailable.
Cài đặt các kênh hiện đang khả dụng của Người chơi. Các kênh có trong danh sách sẽ khả dụng đối với Người chơi, và các kênh không có trong danh sách sẽ không khả dụng.

### 3. Set Text Chat Permissions (Cài đặt Quyền Chat Chữ)
Sets the target player's permission to use text chat in the channel list.
Cài đặt quyền cho người chơi mục tiêu sử dụng tính năng chat chữ (text chat) trong danh sách kênh.

### 4. Set Voice Chat Scope (Cài đặt Phạm vi Chat Thoại)
Sets the voice chat range of the target player within the channel list.
Cài đặt phạm vi chat thoại (voice chat) của người chơi mục tiêu trong danh sách kênh.

### 5. Set Voice Chat Permissions (Cài đặt Quyền Chat Thoại)
Sets the target player's permissions to use voice chat in the channel list.
Cài đặt quyền sử dụng tính năng chat thoại của người chơi mục tiêu trong danh sách kênh.

### 6. Set Player Channel Permissions (Cài đặt Quyền Kênh Người chơi)
Sets player channel permissions.
Cài đặt quyền đối với kênh của người chơi.

## XLVIII. Wonderland Gift Boxes (Hộp Quà Xứ Sở Thần Tiên)
### 1. Consume Gift Box (Tiêu thụ Hộp Quà)
Consumes the specified Player's Wonderland Gift Box.
Tiêu thụ (sử dụng) Hộp Quà Xứ Sở Thần Tiên (Wonderland Gift Box) của Người chơi được chỉ định.

## XLIX. Pathfinding Obstacle (Vật cản Tìm đường)
### 1. Enable/Disable Pathfinding Obstacle (Bật/Tắt Vật cản Tìm đường)
You can modify whether the pathfinding obstacle component of the target entity, corresponding to the specified index, is active.
Bạn có thể sửa đổi xem thành phần vật cản tìm đường (pathfinding obstacle) của thực thể mục tiêu, tương ứng với chỉ mục đã cho, có đang hoạt động hay không.

### 2. Enable/Disable Pathfinding Obstacle Feature (Bật/Tắt Tính năng Vật cản Tìm đường)
You can modify whether the pathfinding obstacle function of the target entity is activated.
Bạn có thể thiết lập xem chức năng tạo vật cản tìm đường của thực thể mục tiêu có được kích hoạt hay không.

## L. Creation Preset Status (Trạng thái Cài sẵn của Vật tạo ra)
### 1. Set the Preset Status Value of the Complex Creation (Cài đặt Giá trị Trạng thái Cài sẵn của Vật tạo phức hợp)
You can set the preset state value for a specified preset state index of a complex creation.
Bạn có thể đặt giá trị trạng thái cài sẵn cho một chỉ mục trạng thái cụ thể của một vật tạo phức hợp (complex creation).

## LI. Floating Interaction Page (Trang Tương tác Nổi)
### 1. Close Floating Interaction Page (Đóng Trang Tương tác Nổi)
Closes the floating interaction page at the specified index for the Player Entity.
Đóng trang tương tác nổi (floating interaction page) tại chỉ mục được chỉ định cho Thực thể Người chơi.

### 2. Update Floating Interaction Page List Data (Cập nhật Dữ liệu Danh sách Trang Tương tác Nổi)
Replaces the current displayed items of the tab or single-choice window at the specified list index with the visible list items corresponding to the input integer list.
Thay thế các mục đang hiển thị của tab hoặc cửa sổ một lựa chọn tại chỉ mục danh sách được chỉ định bằng các mục hiển thị tương ứng với danh sách số nguyên đầu vào.

### 3. Show Floating Interaction Page (Hiển thị Trang Tương tác Nổi)
Opens the floating interaction page at the specified index for the Player, with optional initialization of tab or single-choice window data.
Mở trang tương tác nổi tại chỉ mục được chỉ định cho Người chơi, với tùy chọn khởi tạo dữ liệu cho tab hoặc cửa sổ một lựa chọn.

## LII. Tasks (Nhiệm vụ)
### 1. No. of Tasks Configured (Số lượng Nhiệm vụ đã Cấu hình)
Available only for Beyond Mode.
Chỉ khả dụng cho Chế độ Beyond.

Allows the setting of player's current corresponding task count to a specified value.
Cho phép đặt số lượng nhiệm vụ tương ứng hiện tại của người chơi thành một giá trị được chỉ định.

### 2. Increase Task Count (Tăng Số lượng Nhiệm vụ)
Available only for Beyond Mode.
Chỉ khả dụng cho Chế độ Beyond.

Use this to increase the current count of the corresponding player tasks (value entered may be negative).
Sử dụng node này để tăng số đếm hiện tại của các nhiệm vụ người chơi tương ứng (giá trị nhập vào có thể là số âm).

## LIII. Player Actions (Hành động Người chơi)
### 3. Set Player Escape Validity (Cài đặt Hiệu lực Chạy trốn của Người chơi)
Sets whether escaping is permitted for the specified Player.
Cài đặt xem việc chạy trốn (escape) có được phép đối với Người chơi được chỉ định hay không.

## LIV. General (Cài đặt Chung)
### 1. Multiple Branches (Rẽ nhánh Đa luồng - Switch)
Executes different branches based on matching conditions.
Thực thi các nhánh (branch) khác nhau dựa trên việc khớp các điều kiện.

### 2. Double Branch (Rẽ nhánh Đôi - If/Else)
Executes a branch based on whether a boolean condition is true or false.
Thực thi một nhánh dựa trên điều kiện boolean (đúng hoặc sai).

### 3. Enumerations Equal (Kiểm tra Bằng nhau kiểu Liệt kê)
After confirming the Enumeration type, determines whether two input values are equal.
Sau khi xác nhận kiểu Liệt kê (Enumeration), xác định xem hai giá trị đầu vào có bằng nhau hay không.

### 4. Assembly List (Lắp ráp Danh sách)
Gathers multiple Input Parameters of the same type (up to 100) into a single List.
Tập hợp nhiều Tham số Đầu vào (Input Parameters) có cùng kiểu (hỗ trợ lên đến 100) thành một Danh sách (List) duy nhất.

### 5. Equal (Bằng nhau)
Determines whether two inputs are equal.
Xác định xem hai đầu vào có bằng nhau hay không.

Some Parameter Types have special comparison rules:
Một số Loại Tham số (Parameter Types) có quy tắc so sánh đặc biệt:

Floating Point Numbers: Floating point numbers are compared using approximate equality. When the difference between two floating point numbers is extremely small, they are considered equal. For example, 2.0000001 and 2.0 are considered equal.
Số thực (Float): Các số thực được so sánh bằng phương pháp bằng nhau gần đúng. Khi độ chênh lệch giữa hai số thực là cực kỳ nhỏ, chúng được coi là bằng nhau. Ví dụ: 2.0000001 và 2.0 được coi là bằng nhau.

3D Vector: The x, y, and z components of a 3D Vector are compared using the approximate equality method for floating point numbers.
Vector 3D: Các thành phần x, y và z của một Vector 3D cũng được so sánh bằng phương pháp bằng nhau gần đúng của số thực.

### 6. Data Type Conversion (Chuyển đổi Kiểu dữ liệu)
Converts input parameter types to another type for output. For specific rules, see Basic Concepts - [Conversion Rules Between Basic Data Types].
Chuyển đổi kiểu tham số đầu vào sang một kiểu dữ liệu khác để xuất ra. Để biết các quy tắc cụ thể, vui lòng xem phần Khái niệm Cơ bản - [Quy tắc Chuyển đổi giữa Các Kiểu Dữ liệu Cơ bản].

Floating point numbers will be rounded to integers during conversion.
Lưu ý: Số thực sẽ được làm tròn thành số nguyên trong quá trình chuyển đổi.

## LV. Math (Toán học)
### 1. Split 3D Vector (Chia tách Vector 3D)
Outputs the x, y, and z components of a 3D Vector as three Float values.
Xuất ra các thành phần x, y và z của một Vector 3D dưới dạng ba giá trị Số thực (Float).

### 2. Multiplication (Phép nhân)
Performs multiplication, supporting Floats and Integers.
Thực hiện phép nhân, hỗ trợ nhân Số thực và Số nguyên.

### 3. Division (Phép chia)
Performs division, supporting Floats and Integers. Integer division returns the quotient.
Thực hiện phép chia, hỗ trợ chia Số thực và Số nguyên. Phép chia số nguyên sẽ trả về kết quả là phần thương (không lấy dư).

### 4. Create 3D Vector (Tạo Vector 3D)
Creates a 3D Vector from x, y, and z components.
Tạo một Vector 3D từ các thành phần x, y và z.

### 5. Logarithm Operation (Phép logarit)
Calculates the logarithm of the argument with the specified base.
Tính logarit của đối số (argument) với cơ số được chỉ định.

### 6. Arccosine Function (Hàm arccosine)
Calculates the arccosine of the input and returns the value in radians.
Tính hàm arccosine của đầu vào và trả về giá trị theo đơn vị radian.

### 7. Arctangent Function (Hàm arctangent)
Calculates the arctangent of the input and returns the value in radians.
Tính hàm arctangent của đầu vào và trả về giá trị theo đơn vị radian.

### 8. Arcsine Function (Hàm arcsine)
Calculates the arcsine of the input and returns the value in radians.
Tính hàm arcsine của đầu vào và trả về giá trị theo đơn vị radian.

### 9. Range Limiting Operation (Giới hạn Phạm vi)
Limits the input value to the range `[lower limit, upper limit]` (both inclusive). If the input value is within the range, it returns the original value; if it's lower than the lower limit, it returns the lower limit; if it's higher than the upper limit, it returns the upper limit. If the lower limit is greater than the upper limit, the input is considered invalid and returns an illegal value.
Giới hạn giá trị đầu vào vào khoảng `[giới hạn dưới, giới hạn trên]` (bao gồm cả hai). Nếu giá trị đầu vào nằm trong khoảng, nó trả về giá trị gốc; nếu thấp hơn giới hạn dưới, nó trả về giới hạn dưới; nếu cao hơn giới hạn trên, nó trả về giới hạn trên. Nếu giới hạn dưới lớn hơn giới hạn trên, hệ thống sẽ coi đầu vào không hợp lệ và trả về giá trị bất hợp pháp.

### 10. Direction Vector to Rotation (Chuyển Vector Hướng sang Góc Quay)
Converts a direction vector to a rotation value.
Chuyển đổi một vector hướng thành giá trị góc quay.

### 11. Convert Formatted Time to Timestamp (Chuyển đổi Thời gian đã Định dạng sang Timestamp)
Converts formatted time strings into Unix timestamps.
Chuyển đổi các chuỗi thời gian đã được định dạng sang dấu thời gian (Unix timestamp).

### 12. Convert Timestamp to Formatted Time (Chuyển đổi Timestamp sang Thời gian Định dạng)
Converts Unix timestamps back into human-readable formatted time strings.
Chuyển đổi dấu thời gian (Timestamp) thành chuỗi thời gian đã định dạng để dễ đọc.

### 13. Calculate Day of Week from Timestamp (Tính Ngày trong Tuần từ Timestamp)
Determines the day of the week based on a given timestamp.
Tính toán và xác định ngày trong tuần dựa trên một dấu thời gian cụ thể.

### 14. Radians to Degrees (Đổi Radian sang Độ)
Converts angle values from radians to degrees.
Chuyển đổi giá trị góc từ radian sang độ.

### 15. Addition (Phép cộng)
Performs mathematical addition.
Thực hiện phép tính cộng toán học.

### 16. Subtraction (Phép trừ)
Performs mathematical subtraction.
Thực hiện phép tính trừ toán học.

### 17. Degrees to Radians (Đổi Độ sang Radian)
Converts angle values from degrees to radians.
Chuyển đổi giá trị góc từ độ sang radian.

### 18. Get Larger Value (Lấy Giá trị Lớn hơn)
Returns the greater of two given values.
Trả về giá trị lớn hơn trong hai giá trị được cho (Hàm Max).

### 19. Get Smaller Value (Lấy Giá trị Nhỏ hơn)
Returns the lesser of two given values.
Trả về giá trị nhỏ hơn trong hai giá trị được cho (Hàm Min).

### 20. Absolute Value Operation (Phép lấy Giá trị Tuyệt đối)
Returns the absolute (positive) value of a number.
Trả về giá trị tuyệt đối (luôn dương) của một số.

### 21. Distance Between Two Coordinate Points (Khoảng cách giữa Hai Điểm Tọa độ)
Calculates the spatial distance between two coordinate points.
Tính toán khoảng cách không gian giữa hai điểm tọa độ.

### 22. Logical NOT Operation (Phép NOT Logic)
Reverses a boolean value (True becomes False, False becomes True).
Đảo ngược giá trị boolean (Đúng thành Sai, Sai thành Đúng).

### 23. Logical OR Operation (Phép OR Logic)
Returns True if at least one of the inputs is True.
Trả về Đúng (True) nếu ít nhất một trong các đầu vào là Đúng.

### 24. Logical XOR Operation (Phép XOR Logic)
Returns True only if exactly one of the inputs is True.
Trả về Đúng (True) chỉ khi có đúng một đầu vào là Đúng (Loại trừ).

### 25. Logical AND Operation (Phép AND Logic)
Returns True only if all inputs are True.
Trả về Đúng (True) chỉ khi tất cả các đầu vào đều là Đúng.

### 26. Exponentiation (Lũy thừa)
Raises a number to a specified power.
Tính lũy thừa của một số theo số mũ được chỉ định.

### 27. Modulo Operation (Phép chia lấy dư - Modulo)
Returns the remainder of a division operation.
Trả về phần dư của một phép chia.

### 28. Square Root Operation (Phép căn bậc hai)
Calculates the square root of a given number.
Tính căn bậc hai của một số đã cho.

### 29. Sign Determination Operation (Phép xác định Dấu)
Determines whether a number is positive, negative, or zero.
Xác định xem một số là số dương, số âm hay số không (0).

### 30. Round to Integer Operation (Phép làm tròn tới số nguyên)
Rounds a floating-point number to the nearest integer.
Làm tròn một số thực tới số nguyên gần nhất.

### 31. Normalize 3D Vector (Chuẩn hóa Vector 3D)
Adjusts a 3D vector so its length is exactly 1 while maintaining its direction.
Điều chỉnh một vector 3D sao cho độ dài của nó chính xác bằng 1 trong khi vẫn giữ nguyên hướng (Vector đơn vị).

### 32. 3D Vector Addition (Cộng Vector 3D)
Adds two 3D vectors together.
Cộng hai vector 3D lại với nhau.

### 33. 3D Vector Angle (Góc Vector 3D)
Calculates the angle between two 3D vectors.
Tính góc giữa hai vector 3D.

### 34. 3D Vector Subtraction (Trừ Vector 3D)
Subtracts one 3D vector from another.
Trừ vector 3D này cho một vector 3D khác.

### 35. 3D Vector Length (Độ dài Vector 3D)
Calculates the magnitude or length of a 3D vector.
Tính độ lớn hoặc chiều dài của một vector 3D.

### 36. 3D Vector Dot Product (Tích vô hướng Vector 3D)
Calculates the dot product of two 3D vectors.
Tính tích vô hướng (Dot Product) của hai vector 3D.

### 37. 3D Vector Scalar Multiplication (Phép nhân vô hướng Vector 3D)
Multiplies a 3D vector by a scalar (single number) to scale its length.
Nhân một vector 3D với một đại lượng vô hướng (một số duy nhất) để chia tỷ lệ độ dài của nó.

### 38. 3D Vector Cross Product (Tích có hướng Vector 3D)
Calculates the cross product of two 3D vectors.
Tính tích có hướng (Cross Product) của hai vector 3D.

### 39. Rotate 3D Vector (Quay Vector 3D)
Rotates a 3D vector by a specified angle.
Xoay một vector 3D theo một góc được chỉ định.

### 40. Greater Than (Lớn hơn)
Checks if the first value is greater than the second.
Kiểm tra xem giá trị đầu tiên có lớn hơn giá trị thứ hai hay không.

### 41. Greater Than or Equal (Lớn hơn hoặc Bằng)
Checks if the first value is greater than or equal to the second.
Kiểm tra xem giá trị đầu tiên có lớn hơn hoặc bằng giá trị thứ hai hay không.

### 42. Less Than (Nhỏ hơn)
Checks if the first value is less than the second.
Kiểm tra xem giá trị đầu tiên có nhỏ hơn giá trị thứ hai hay không.

### 43. Less Than or Equal (Nhỏ hơn hoặc Bằng)
Checks if the first value is less than or equal to the second.
Kiểm tra xem giá trị đầu tiên có nhỏ hơn hoặc bằng giá trị thứ hai hay không.

### 44. Cosine Function (Hàm cosin)
Calculates the cosine of a given angle.
Tính hàm cosin của một góc đã cho.

### 45. Tangent Function (Hàm tang)
Calculates the tangent of a given angle.
Tính hàm tang của một góc đã cho.

### 46. Sine Function (Hàm sin)
Calculates the sine of a given angle.
Tính hàm sin của một góc đã cho.

### 47. Bitwise Left Shift (Phép dịch trái Bitwise)
Shifts the bits of a number to the left.
Dịch chuyển các bit của một số sang bên trái.

### 48. Bitwise Right Shift (Phép dịch phải Bitwise)
Shifts the bits of a number to the right.
Dịch chuyển các bit của một số sang bên phải.

### 49. Bitwise AND (Phép AND Bitwise)
Performs a bitwise AND operation on two integers.
Thực hiện phép toán AND mức bit (bitwise) trên hai số nguyên.

### 50. Bitwise OR (Phép OR Bitwise)
Performs a bitwise OR operation on two integers.
Thực hiện phép toán OR mức bit trên hai số nguyên.

### 51. Phép XOR (Exclusive OR)

### 52. Phủ định bitwise

### 53. Ghi bằng bit

### 2. Get Local Variable (Lấy Biến Cục bộ)
Truy xuất một Biến Cục bộ (Local Variable) và tùy ý đặt [Initial Value] (Giá trị Ban đầu) cho nó.

Sau khi đặt [Initial Value], tham số đầu ra [Value] (Giá trị) sẽ bằng với [Initial Value] được truyền vào.

Khi [Local Variable] (Biến Cục bộ) đầu ra được kết nối với đầu vào [Local Variable] của Node Thực thi [Set Local Variable] (Đặt Biến Cục bộ), tham số đầu vào [Value] của node [Set Local Variable] sẽ ghi đè lên tham số đầu ra [Value] của Node Truy vấn này. Lần tiếp theo bạn sử dụng [Get Local Variable], đầu ra [Value] sẽ là giá trị đã được ghi đè.

### 1. Query Server Time Zone (Truy vấn Múi giờ Máy chủ)
Truy tìm Múi giờ của Máy chủ.

### 2. Query Timestamp (UTC+0) (Truy vấn Dấu thời gian (UTC+0))
Truy tìm Dấu thời gian hiện tại.

### 3. Get Random Floating Point Number (Lấy Số thực Ngẫu nhiên)
Trả về một Số thực Ngẫu nhiên lớn hơn hoặc bằng (≥) giới hạn dưới và nhỏ hơn hoặc bằng (≤) giới hạn trên. Phạm vi này bao gồm cả hai giới hạn.

### 4. Get Random Integer (Lấy Số nguyên Ngẫu nhiên)
Trả về một Số nguyên Ngẫu nhiên lớn hơn hoặc bằng (≥) giới hạn dưới và nhỏ hơn hoặc bằng (≤) giới hạn trên. Phạm vi này bao gồm cả hai giới hạn.

### 5. Weighted Random (Ngẫu nhiên có Trọng số)
Nhận một danh sách trọng số và chọn ngẫu nhiên một ID dựa trên phân bố trọng số.

Ví dụ, với danh sách trọng số {10, 20, 66, 4}, node này sẽ xuất ra 0, 1, 2, hoặc 3 với xác suất tương ứng là 10%, 20%, 66%, và 4%.

### 6. 3D Vector: Backward (Vector 3D: Lùi)
Return (0,0,-1)
Trả về (0,0,-1)

### 7. 3D Vector: Zero Vector (Vector 3D: Không)
Return (0,0,0)
Trả về (0,0,0)

### 8. 3D Vector: Forward (Vector 3D: Tiến)
Return (0,0,1)
Trả về (0,0,1)

### 9. 3D Vector: Up (Vector 3D: Lên)
Return (0,1,0)
Trả về (0,1,0)

### 10. 3D Vector: Down (Vector 3D: Xuống)
Return (0,-1,0)
Trả về (0,-1,0)

### 11. 3D Vector: Right (Vector 3D: Phải)
Return (1,0,0)
Trả về (1,0,0)

### 12. 3D Vector: Left (Vector 3D: Trái)
Return (-1,0,0)
Trả về (-1,0,0)

## III. Dictionary
### 54. Đọc bằng bit

### 1. Create Dictionary

## IV. Structures
### 2. Assembly Dictionary

### 1. Split Structure

### 2. Assemble Structure

## III. List Related
### 13. Pi (π) (Pi - Số π)
Returns the approximate value of π (≈ 3.142)
Trả về giá trị gần đúng của π (≈ 3,142)

### 1. Search List and Return Value ID
Find the specified value in the list and return a list of IDs where it appears
Tìm giá trị được chỉ định trong danh sách và trả về danh sách ID nơi nó xuất hiện

For example, if the target list is {1,2,3,2,1} and the value is 1, the returned ID list is {0,4}, meaning 1 appears at IDs 0 and 4 in the target list
Ví dụ: nếu danh sách mục tiêu là {1,2,3,2,1} và giá trị là 1 thì danh sách ID trả về là {0,4}, nghĩa là 1 xuất hiện tại ID 0 và 4 trong danh sách mục tiêu

### 2. Get Corresponding Value From List
Returns the value at the specified ID in the list (0-based)
Trả về giá trị tại ID được chỉ định trong danh sách (dựa trên 0)

### 3. Get List Length
Returns the length of the list (number of elements)
Trả về độ dài của danh sách (số phần tử)

### 4. Get Maximum Value from List
Applies only to Floating Point Number or Integer lists; returns the maximum value
Chỉ áp dụng cho danh sách Số dấu phẩy động hoặc Số nguyên; trả về giá trị tối đa

### 5. Get Minimum Value From List
Applies only to Floating Point Number or Integer lists; returns the minimum value
Chỉ áp dụng cho danh sách Số dấu phẩy động hoặc Số nguyên; trả về giá trị tối thiểu

## IV. Custom Variables
### 6. List Includes This Value
Returns whether the list contains the specified value
Trả về xem danh sách có chứa giá trị được chỉ định hay không

### 1. Query Custom Variable Snapshot
Searches the value of the specified Variable Name from the Custom Variable Component snapshot
Tìm kiếm giá trị của Tên biến được chỉ định từ ảnh chụp nhanh Thành phần biến tùy chỉnh

Only available for the [On Entity Destroyed] event
Chỉ áp dụng cho sự kiện [On Entity Destroyed]

### 2. Get Node Graph Variable
Returns the value of the specified Node Graph Variable from the current Node Graph
Trả về giá trị của Biến biểu đồ nút được chỉ định từ Biểu đồ nút hiện tại

If the variable does not exist, returns the type's default value
Nếu biến không tồn tại, trả về giá trị mặc định của loại

## V. Preset Status
### 3. Get Custom Variable
Returns the value of the specified Custom Variable from the Target Entity
Trả về giá trị của Biến tùy chỉnh được chỉ định từ Thực thể mục tiêu

If the variable does not exist, returns the type's default value
Nếu biến không tồn tại, trả về giá trị mặc định của loại

## VI. Entity Related
### 1. Get Preset Status
Returns the value of the specified Preset Status for the Target Entity. Returns 0 if the Entity does not have that Preset Status
Trả về giá trị của Trạng thái đặt trước đã chỉ định cho Thực thể đích. Trả về 0 nếu Thực thể không có Trạng thái đặt trước đó

### 1. Query Character's Current Movement SPD
Can only be searched when the Character has the [Monitor Movement Speed] Unit Status effect
Chỉ có thể tìm kiếm khi Nhân vật có hiệu ứng Trạng thái Đơn vị [Theo dõi tốc độ di chuyển]

### 2. Query If Entity Is on the Field
Searches whether the specified Entity is present
Tìm kiếm xem Thực thể được chỉ định có hiện diện hay không

Note that Character Entities are still considered present even when Downed
Lưu ý rằng các Thực thể Nhân vật vẫn được coi là hiện diện ngay cả khi Bị Hạ gục

### 3. Get All Entities on the Field
Returns all Entities currently present in the scene. The number of Entities in this List may be large
Trả về tất cả các Thực thể hiện có trong cảnh. Số lượng Thực thể trong Danh sách này có thể lớn

### 4. Get Specified Type of Entities on the Field
Returns all Entities of the specified type currently in the scene. The number of Entities in this list may be large
Trả về tất cả các Thực thể thuộc loại được chỉ định hiện có trong cảnh. Số lượng Thực thể trong danh sách này có thể lớn

### 5. Get Entities With Specified Prefab on the Field
Returns all Entities currently in the scene that were created by the specified Prefab ID
Trả về tất cả các Thực thể hiện có trong cảnh được tạo bởi ID Prefab đã chỉ định

### 6. Get Character Attribute
Returns the Base Attributes of the Character Entity
Trả về các thuộc tính cơ bản của thực thể ký tự

### 7. Get Entity Advanced Attribute
Returns the Advanced Attributes of the Entity
Trả về các thuộc tính nâng cao của thực thể

### 8. Get Entity Type
Returns the Entity Type of the Target Entity
Trả về Loại thực thể của Thực thể đích

### 9. Get Entity Location and Rotation (Lấy Vị trí và Góc quay của Thực thể)
Trả về thông tin Vị trí (Location) và Góc quay (Rotation) của Thực thể Mục tiêu (Target Entity).

Không áp dụng cho Thực thể Người chơi (Player Entities) hoặc Thực thể Màn chơi (Stage Entities).

### 10. Get Entity Forward Vector
Returns the Forward Vector of the specified Entity (the positive Z-axis direction in the Entity's relative coordinate system)
Trả về Vector chuyển tiếp của Thực thể được chỉ định (hướng trục Z dương trong hệ tọa độ tương đối của Thực thể)

### 11. Get Entity Upward Vector
Returns the Upward Vector of the specified Entity (the positive Y-axis direction in the Entity's relative coordinate system)
Trả về Vector hướng lên của Thực thể được chỉ định (hướng trục Y dương trong hệ tọa độ tương đối của Thực thể)

### 12. Get Entity Right Vector
Returns the Right Vector of the specified Entity (the positive X-axis direction in the Entity's relative coordinate system)
Trả về Vector bên phải của Thực thể được chỉ định (hướng trục X dương trong hệ tọa độ tương đối của Thực thể)

### 13. Get List of Entities Owned by the Entity
Returns a list of all Entities owned by the Target Entity
Trả về danh sách tất cả các Thực thể thuộc sở hữu của Thực thể Đích

### 14. Get Entity Elemental Attribute
Returns the Element Attributes of the Target Entity
Trả về các thuộc tính phần tử của thực thể đích

### 15. Get Object Attribute
Returns the Base Attributes of the Object
Trả về các thuộc tính cơ bản của đối tượng

### 16. Get Owner Entity
Returns the Owner Entity of the specified Target Entity
Trả về Thực thể chủ sở hữu của Thực thể mục tiêu đã chỉ định

### 17. Get Entity List by Specified Range
Returns a list of Entities within a specified spherical range from the Target Entity List
Trả về danh sách các Thực thể trong phạm vi hình cầu được chỉ định từ Danh sách Thực thể Đích

### 18. Get Entity List by Specified Type
Returns a list of specified Entity types from the Target Entity List
Trả về danh sách các loại Thực thể được chỉ định từ Danh sách Thực thể Đích

### 19. Get Entity List by Specified Prefab ID
Returns a list of Entities created with the specified Prefab ID from the Target Entity List
Trả về danh sách Thực thể được tạo bằng ID Prefab được chỉ định từ Danh sách thực thể đích

### 20. Get Entity List by Specified Faction
Returns the list of Entities belonging to a specific Faction from the Target Entity List
Trả về danh sách các Thực thể thuộc một Phe cụ thể từ Danh sách Thực thể Đích

### 21. Get Self Entity
Returns the Entity associated with this Node Graph
Trả về Thực thể được liên kết với Biểu đồ nút này

### 22. Query GUID by Entity
Searches for the GUID of the specified Entity
Tìm kiếm GUID của Thực thể được chỉ định

### 23. Query Entity by GUID
Searches for an Entity by GUID
Tìm kiếm một thực thể bằng GUID

## VII. Stage Related
### 24. Check Entity's Elemental Effect Status
Check entity's elemental effect status
Kiểm tra trạng thái hiệu ứng nguyên tố của thực thể

### 1. Query Current Environment Time
Searches the current Environment Time, in the range [0, 24)
Tìm kiếm Thời gian môi trường hiện tại, trong phạm vi [0, 24)

## VIII. Faction Related
### 2. Query Game Time Elapsed
Searches how long the game has been running, in seconds
Tìm kiếm trò chơi đã chạy được bao lâu, tính bằng giây

### 1. Query Entity Faction
Searches the Faction of the specified Entity
Tìm kiếm Phe của Thực thể được chỉ định

## IX. Player and Character Related
### 2. Query If Faction Is Hostile
Searches whether two Factions are hostile to each other
Tìm kiếm xem hai phe có thù địch với nhau không

### 1. Query If All Player Characters Are Down
Check if all of the player's characters are downed
Kiểm tra xem tất cả nhân vật của người chơi có bị hạ gục không

### 2. Get Player GUID by Player ID
Returns the Player GUID based on Player ID, where the ID indicates which Player they are
Trả về GUID người chơi dựa trên ID người chơi, trong đó ID cho biết họ là Người chơi nào

### 3. Get Player ID by Player GUID
Returns the Player ID based on Player GUID, where the ID indicates which Player they are
Trả về ID người chơi dựa trên GUID của người chơi, trong đó ID cho biết họ là Người chơi nào

### 4. Get Player Client Input Device Type
Returns the Player's local input device type, as determined by the Interface mapping method
Trả về loại thiết bị đầu vào cục bộ của Trình phát, như được xác định bằng phương pháp ánh xạ Giao diện

### 5.** Get Player Entity to Which the Character Belongs
Returns the Player Entity that owns the Character Entity
Trả về Thực thể người chơi sở hữu Thực thể nhân vật

### 6. Get Player Revive Time
Returns the revive duration of the specified Player Entity, in seconds
Trả về thời gian hồi sinh của Thực thể người chơi được chỉ định, tính bằng giây

### 7. Get Player Nickname
Returns the Player's nickname
Trả về biệt danh của người chơi

### 8. Get Player Remaining Revives
Returns the remaining number of revives for the specified Player Entity
Trả về số lần hồi sinh còn lại cho Thực thể người chơi được chỉ định

### 9. Get List of Player Entities on the Field
Returns a list of all Player Entities present in the scene
Trả về danh sách tất cả các Thực thể người chơi có trong cảnh

### 10. Get All Character Entities of Specified Player
Returns a list of all Character Entities for the specified Player Entity
Trả về danh sách tất cả các Thực thể Nhân vật cho Thực thể Người chơi được chỉ định

### 11. Get Active Character of Specified Player
Available only in Classic Mode, get the active character in the player's party.
Chỉ khả dụng ở Chế độ cổ điển, nhận nhân vật hoạt động trong nhóm của người chơi.

## X. Follow Motion Device
### 12. Check Classic Mode Character ID
Available only in Classic Mode. You can search for the character ID of the target character to see the appendix for the specific character in Classic Mode Character ID List
Chỉ khả dụng ở Chế độ cổ điển. Bạn có thể tìm kiếm ID ký tự của ký tự đích để xem phụ lục cho ký tự cụ thể trong Danh sách ID ký tự ở Chế độ Cổ điển

## XIII. Creation
### 1. Get Player's Current UI Layout
Returns the ID of the currently active Interface Layout on the specified Player Entity
Trả về ID của Bố cục giao diện hiện đang hoạt động trên Thực thể người chơi được chỉ định

### 1. Get Creation's Current Target
The Target Entity varies with the Creation's current behavior
Thực thể Mục tiêu thay đổi theo hành vi hiện tại của Sáng tạo

For example, when a Creation is attacking, its Target is the specified enemy Entity
Ví dụ: khi một Sáng tạo đang tấn công, Mục tiêu của nó là Thực thể kẻ thù được chỉ định

For example, when a Creation is healing allies, its Target is the specified allied Entity
Ví dụ: khi một Sáng tạo đang chữa lành vết thương cho đồng minh, Mục tiêu của nó là Thực thể đồng minh được chỉ định

### 2. Get Aggro List of Creation in Default Mode
Returns the Aggro List in Default Mode. This Node only outputs a valid list when the Aggro Configuration is set to [Default Type]
Trả về Danh sách Aggro ở Chế độ mặc định. Nút này chỉ xuất ra danh sách hợp lệ khi Cấu hình Aggro được đặt thành [Loại mặc định]

## XIV. Class
### 3. Get Creation Attribute
Returns the Attributes of the specified Creation
Trả về các thuộc tính của Sáng tạo được chỉ định

### 1. Query Player Class Level
Searches the Player's Level of the specified Class
Tìm kiếm Cấp độ của Người chơi trong Lớp được chỉ định

## XV. Skills
### 2. Query Player Class
Searches the Player's current Class; outputs the Config ID of that Class
Tìm kiếm Lớp hiện tại của Người chơi; xuất ra ID cấu hình của Lớp đó

### 1. Query Character Skill
Searches the Skill in the specified slot of a Character; outputs that Skill's Config ID
Tìm kiếm Kỹ năng trong vị trí được chỉ định của Nhân vật; xuất ra ID cấu hình của Skill đó

### 2. Query Skill Config ID by Skill Instance ID
Retrieve the Skill Config ID that corresponds to the specified Character Entity and Skill Instance ID
Truy xuất ID cấu hình kỹ năng tương ứng với Thực thể nhân vật và ID phiên bản kỹ năng được chỉ định

### 3. Query All Skill Instance IDs by Skill Config ID
Retrieve the Skill Instance ID List that corresponds to the specified Character Entity and Skill Config ID
Truy xuất Danh sách ID phiên bản kỹ năng tương ứng với Thực thể nhân vật và ID cấu hình kỹ năng được chỉ định

### 4. Query All Skill Instance IDs by Skill Slot
Retrieve all Skill Instance IDs present in a specified Skill Slot for the given Character Entity
Truy xuất tất cả ID phiên bản kỹ năng có trong Khe kỹ năng được chỉ định cho Thực thể ký tự nhất định

### 5. Query Skill Instance ID by Skill Slot and Skill Config ID
Retrieve the Skill Instance ID in a specified Skill Slot that corresponds to a given Skill Config ID for the Character Entity
Truy xuất ID phiên bản kỹ năng trong Khe kỹ năng được chỉ định tương ứng với ID cấu hình kỹ năng nhất định cho Thực thể nhân vật

## XVI. Unit Status
### 6. Query Skill Attribute Group Value
Retrieve the value of a Skill Group for a Character Entity, based on the specified Skill Group Config ID
Truy xuất giá trị của Nhóm kỹ năng cho Thực thể nhân vật, dựa trên ID cấu hình nhóm kỹ năng được chỉ định

### 1. List of Slot IDs Querying Unit Status
Searches the list of all Slot IDs for the Unit Status with the specified Config ID on the Target Entity
Tìm kiếm danh sách tất cả ID vị trí cho Trạng thái đơn vị với ID cấu hình được chỉ định trên Thực thể mục tiêu

### 2. Query If Entity Has Unit Status
Searches whether the specified Entity has a Unit Status with the given Config ID
Tìm kiếm xem Thực thể được chỉ định có Trạng thái Đơn vị với ID Cấu hình đã cho hay không

### 3. Query Unit Status Stacks by Slot ID
Searches the Stack Count of the specified Unit Status on the Target Entity's designated Slot
Tìm kiếm Số lượng ngăn xếp của Trạng thái đơn vị được chỉ định trên Vị trí được chỉ định của Thực thể mục tiêu

## XVII. Unit Tags
### 4. Query Unit Status Applier by Slot ID
Searches the Applier of the specified Unit Status on the Target Entity's designated Slot
Tìm kiếm Ứng dụng của Trạng thái Đơn vị được chỉ định trên Vị trí được chỉ định của Thực thể Mục tiêu

### 1. Get Entity List by Unit Tag
Returns a list of all Entities in the scene that carry this Unit Tag
Trả về danh sách tất cả các Thực thể trong cảnh mang Thẻ Đơn vị này

## XIX. Global Path
### 8. Get the Aggro Target of the Specified Entity
Get Aggro Target of Specific Entity
Nhận mục tiêu Aggro của thực thể cụ thể

### 1. Get the Number of Waypoints in the Global Path
Get the number of Waypoints in the Global Path
Lấy số điểm tham chiếu trong Đường dẫn toàn cầu

## XX. Preset Points
### 2. Get Specified Waypoint Info
Searches the specified Waypoint information for the given Path
Tìm kiếm thông tin Điểm tham chiếu đã chỉ định cho Đường dẫn đã cho

### 1. Get Preset Point List by Unit Tag
Searches all Preset Points that carry the Unit Tag by its ID; outputs each Preset Point's ID
Tìm kiếm tất cả các Điểm đặt trước mang Thẻ Đơn vị theo ID của nó; xuất ra mỗi ID của Điểm đặt trước

## XXI. Stage Settlement
### 2. Query Preset Point Position Rotation
Searches the Location and Rotation of the specified Preset Point
Tìm kiếm Vị trí và Góc quay của Điểm đặt trước được chỉ định

### 1. Get Player Settlement Success Status
Get Player Settlement Success Status
Nhận trạng thái thành công thanh toán của người chơi

### 2. Get Player Settlement Ranking Valu**e
Returns the Settlement ranking value for the specified Player Entity
Trả về giá trị xếp hạng Dàn xếp cho Thực thể Người chơi được chỉ định

### 3. Get Faction Settlement Success Status
Get Faction Settlement Success Status
Nhận trạng thái thành công giải quyết phe phái

## XXII. Dictionary
### 4. Get Faction Settlement** Ranking Value
Returns the Settlement ranking value for the specified Faction
Trả về giá trị xếp hạng Dàn xếp cho Phe được chỉ định

### 1. Query If Dictionary Contains Specific Key
Searches whether the specified Dictionary contains the specified Key
Tìm kiếm xem Từ điển đã chỉ định có chứa Khóa được chỉ định hay không

### 2. Query If Dictionary Contains Specific Value
Searches whether the specified Dictionary contains the specified Value
Tìm kiếm xem Từ điển đã chỉ định có chứa Giá trị đã chỉ định hay không

### 3. Query Dictionary's Length
Searches the number of Key-Value Pairs in the Dictionary
Tìm kiếm số cặp khóa-giá trị trong từ điển

### 4. Query Dictionary Value by Key
Searches the corresponding Value in the Dictionary by Key. If the Key does not exist, returns the type's default value
Tìm kiếm Giá trị tương ứng trong Từ điển theo Khóa. Nếu Khóa không tồn tại, trả về giá trị mặc định của loại

### 5. Get List of Keys from Dictionary
Returns a list of all Keys in the Dictionary. Because Key-Value Pairs are unordered, the Keys may not be returned in insertion order
Trả về danh sách tất cả các Khóa trong Từ điển. Vì Cặp khóa-giá trị không có thứ tự nên Khóa có thể không được trả về theo thứ tự chèn

## XXIII. Shop
### 6. Get List of Values from Dictionary
Returns a list of all Values in the Dictionary. Because Key-Value Pairs are unordered, the Values may not be returned in insertion order
Trả về danh sách tất cả các Giá trị trong Từ điển. Vì Cặp khóa-giá trị không có thứ tự nên các Giá trị có thể không được trả về theo thứ tự chèn

### 1. Query Inventory Shop Item Sales Info
Searches sale information for a specified Item in the Inventory Shop
Tìm kiếm thông tin bán hàng cho một Mặt hàng được chỉ định trong Cửa hàng Hàng tồn kho

### 2. Query Inventory Shop Item Sales List
Search the inventory shop's sales list
Tìm kiếm danh sách bán hàng của cửa hàng tồn kho

### 3. Query Shop Purchase Item List
Search the shop's purchase list
Tìm kiếm danh sách mua hàng của cửa hàng

### 4. Query Shop Item Purchase Info
Searches purchase information for a specified Item in the Shop
Tìm kiếm thông tin mua hàng cho một Mặt hàng được chỉ định trong Cửa hàng

### 5. Query Custom Shop Item Sales List
Searches the Custom Shop sale list; the output parameter is a list of Item IDs
Tìm kiếm danh sách bán hàng của Custom Shop; tham số đầu ra là danh sách ID mặt hàng

## XXIV. Equipment
### 6. Query Custom Shop Item Sales Info
Searches sale information for a specified Item in the Custom Shop
Tìm kiếm thông tin bán hàng cho một Mặt hàng được chỉ định trong Cửa hàng tùy chỉnh

### 1. Query Equipment Tag List
Searches the list of all Tags on this Equipment instance
Tìm kiếm danh sách tất cả các Thẻ trên phiên bản Thiết bị này

### 2. Query Equipment Config ID by Equipment ID
Searches the Equipment Config ID by Equipment ID. The Equipment Instance ID can be obtained in the [Equipment Initialization] event
Tìm kiếm ID cấu hình thiết bị theo ID thiết bị. ID phiên bản thiết bị có thể nhận được trong sự kiện [Khởi tạo thiết bị]

### 3. Get Equipment Affix List
Returns a list of all Affixes on this Equipment instance
Trả về danh sách tất cả các Phụ kiện trên phiên bản Thiết bị này

When Equipment is initialized, Affix values are randomized, so the Equipment Affixes on the Equipment instance also generate corresponding instances. Therefore, the data type is Integer rather than Config ID
Khi Thiết bị được khởi tạo, các giá trị Phụ kiện được chọn ngẫu nhiên, do đó, Phụ kiện Thiết bị trên phiên bản Thiết bị cũng tạo ra các phiên bản tương ứng. Do đó, kiểu dữ liệu là Số nguyên thay vì ID cấu hình

### 4. Get Equipment Affix Config ID
Returns the Config ID of an Equipment Affix by its ID on the Equipment instance
Trả về ID cấu hình của Phụ kiện thiết bị theo ID của nó trên phiên bản Thiết bị

### 5. Get Equipment Affix Value
Returns the value of the Affix at the specified ID on the Equipment instance
Trả về giá trị của Affix tại ID được chỉ định trên phiên bản Thiết bị

## XXV. Items
### 6. Get the Equipment Index of the Specified Equipment Slot
Get the equipment index of the specified equipment slot
Lấy chỉ số trang bị của ô trang bị được chỉ định

### 1. Get Inventory Item Quantity
Returns the quantity of the Item with the specified Config ID in the Inventory
Trả về số lượng Mặt hàng có ID cấu hình được chỉ định trong Kho

### 2. Get Inventory Currency Quantity
Returns the amount of Currency with the specified Config ID in the Inventory
Trả về số lượng Tiền tệ với ID cấu hình được chỉ định trong Kho

### 3. Get Inventory Capacity
Get Inventory Capacity
Nhận dung lượng tồn kho

### 4. Get All Currency From Inventory
Returns all Currencies in the Inventory, including types and corresponding amounts
Trả về tất cả các loại tiền tệ trong kho, bao gồm loại và số lượng tương ứng

### 5. Get all basic items from Inventory
Returns all Basic Items in the Inventory, including Item types and their quantities
Trả về tất cả Vật phẩm cơ bản trong Kho, bao gồm loại Vật phẩm và số lượng của chúng

### 6. Get all equipment from Inventory
Returns all Equipment in the Inventory; the output parameter is a list of all Equipment IDs
Trả lại tất cả Thiết bị trong Kho; tham số đầu ra là danh sách tất cả ID thiết bị

### 7. Get Loot Component Item Quantity
Returns the quantity of Items with the specified Config ID from the Loot Component on the Loot Prefab
Trả về số lượng Vật phẩm có ID cấu hình được chỉ định từ Thành phần chiến lợi phẩm trên Loot Prefab

### 8. Get Loot Component Currency Quantity
Returns the amount of Currency with the specified Config ID from the Loot Component on the Loot Prefab
Trả về số lượng Tiền tệ với ID cấu hình được chỉ định từ Thành phần chiến lợi phẩm trên Loot Prefab

### 9. Get All Equipment from Loot Component
Returns all Equipment from the Loot Component on the Loot Prefab
Trả về tất cả thiết bị từ Thành phần chiến lợi phẩm trên Loot Prefab

### 10.** Get All Items from Loot Component
Returns all Items from the Loot Component on the Loot Prefab
Trả về tất cả các mục từ Thành phần chiến lợi phẩm trên Loot Prefab

## XXVI. Collision Trigger
### 11.** Get All Currency from Loot Component
Returns all Currencies from the Loot Component on the Loot Prefab
Trả về tất cả các loại tiền tệ từ Thành phần chiến lợi phẩm trên Loot Prefab

## XXVII. Mini-Map Marker Component
### 1. Get All Entities Within the Collision Trigger
Returns all Entities within the Collision Trigger corresponding to a specific ID in the Collision Trigger Component on the Target Entity
Trả về tất cả các Thực thể trong Trình kích hoạt va chạm tương ứng với một ID cụ thể trong Thành phần kích hoạt va chạm trên Thực thể đích

### 1. Query Specified Mini-Map Marker Information
Searches the information of the Mini-map Marker with the specified ID in the Mini-map Marker Component on the Target Entity
Tìm kiếm thông tin của Điểm đánh dấu bản đồ thu nhỏ với ID được chỉ định trong Thành phần điểm đánh dấu bản đồ thu nhỏ trên Thực thể mục tiêu

## XXVIII. Creature Patrol
### 2. Get Entity's Mini-Map Marker Status
Searches the configuration and activation status of the Entity's current Mini-map Marker
Tìm kiếm cấu hình và trạng thái kích hoạt của Điểm đánh dấu bản đồ thu nhỏ hiện tại của Thực thể

## XXIX. Achievements
### 1. Get Current Creation's Patrol Template
Returns the Patrol Template information of the specified Creation Entity
Trả về thông tin Mẫu tuần tra của Thực thể tạo được chỉ định

## XXX. Scan Tags
### 1. Query If Achievement Is Completed
Searches whether the Achievement corresponding to a specific ID on the Target Entity is complete
Tìm kiếm xem Thành tích tương ứng với một ID cụ thể trên Thực thể mục tiêu đã hoàn thành hay chưa

## XXXI. Rank Tier
### 1. Get the Currently Active Scan Tag Config ID
Returns the Configuration ID of the currently active Scan Tags on the Target Entity
Trả về ID cấu hình của Thẻ quét hiện đang hoạt động trên Thực thể đích

### 1. Get Player Rank Score Change
Returns the Rank change score for the Player Entity under different Settlement states
Trả về điểm thay đổi Thứ hạng cho Thực thể Người chơi ở các trạng thái Dàn xếp khác nhau

### 2. Get Player Ranking Info
Returns the Player's Rank-related information
Trả về thông tin liên quan đến Xếp hạng của Người chơi

## XXXII. Entity Layout Group
### 3. Get Player Escape Validity
Get Player Escape Permission
Nhận quyền thoát khỏi người chơi

## XXXIII. Wonderland Gift Box Related
### 1. Get Currently Active Entity Deployment Groups
Searches the list of Entity Layout Groups currently active in the Stage
Tìm kiếm danh sách Nhóm bố cục thực thể hiện đang hoạt động trong Giai đoạn

### 1. Query Corresponding Gift Box Quantity
Searches the quantity of the specified Gift Box on the Player Entity
Tìm kiếm số lượng Hộp quà được chỉ định trên Thực thể người chơi

## XXXIV. Creation Preset Status
### 2. Query Corresponding Gift Box Consumption
Searches the consumed quantity of the specified Gift Box on the Player Entity
Tìm kiếm số lượng tiêu thụ của Hộp quà được chỉ định trên Thực thể người chơi

### 1. Get the Preset Status Value of the Complex Creation
Get the preset status value of the complex creation
Nhận giá trị trạng thái đặt trước của quá trình tạo phức tạp

### 1. Query Specified Task Count
Available only in Beyond Mode
Chỉ khả dụng ở Chế độ ngoài

Returns the corresponding player's current task count for specified tasks
Trả về số lượng nhiệm vụ hiện tại của người chơi tương ứng cho các nhiệm vụ được chỉ định

### 2. Query If Specified Task is Completed
Available only in Beyond Mode
Chỉ khả dụng ở Chế độ ngoài

Use this to check if a specified task has been completed by the corresponding player
Sử dụng tính năng này để kiểm tra xem người chơi tương ứng đã hoàn thành một nhiệm vụ cụ thể chưa

