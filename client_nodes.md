# Tổng số Client Nodes: 568

## I. General (Cài đặt chung)
### 1. Continue Executing Previous Frame Behavior (Tiếp tục hành vi của khung hình trước)
Nếu Chiến thuật (Tactic) được kích hoạt ở khung hình trước vẫn chưa hoàn thành, nó sẽ được tiếp tục thực thi cho đến khi kết thúc.

Nếu Kỹ năng (Skill) đã được thực thi ở khung hình trước, sẽ không có quá trình nào diễn ra thêm.

## II. Tactics
### 1. Tactic: Ground Confrontation (Chiến thuật: Đối đầu trên mặt đất)
The Creation executes a Paving Standoff. It uses four-direction Motion Tactics, with five directions: idle/forward/backward/left/right. Use this to simulate a sustained face-off with the Player.
Vật tạo ra (Creation) thực thi một hành vi Đối đầu di chuyển (Paving Standoff). Nó sử dụng Chiến thuật Di chuyển bốn hướng, với năm trạng thái: đứng im/tiến/lùi/trái/phải. Sử dụng điều này để mô phỏng một cuộc đối đầu giằng co liên tục với Người chơi.

You can use probability settings to create motion behaviors such as moving left and right around the Player, or preferring to move forward and avoiding moving backward. It also includes settings for adjusting distance to the Player and for obstacle avoidance.
Bạn có thể sử dụng các thiết lập xác suất để tạo các hành vi di chuyển như di chuyển qua trái/phải xung quanh Người chơi, hoặc ưu tiên tiến tới và tránh lùi lại. Nó cũng bao gồm các thiết lập để điều chỉnh khoảng cách tới Người chơi và để tránh chướng ngại vật.

Essentially, it just decides a direction; there is no specific Target Point.
Về cơ bản, nó chỉ quyết định một hướng đi; không có một Điểm Mục tiêu cụ thể nào.

Execution Conditions (Điều kiện Thực thi):



Requires the unit or the target to be within the Territory Range.
Yêu cầu đơn vị hoặc mục tiêu phải nằm trong Phạm vi Lãnh thổ.



If *Reachable via Pathfinding* is enabled and the unit is not airborne, Tactics will end when Pathfinding fails.
Nếu *Có thể tiếp cận thông qua Tìm đường* được bật và đơn vị không ở trên không, Chiến thuật sẽ kết thúc khi thao tác Tìm đường (Pathfinding) thất bại.

### 2. Tactic: Ground Escape (Chiến thuật: Bỏ trốn trên mặt đất)
The Creation executes a Paving Escape, a tactic for fleeing from the Target. It attempts to turn its back to the Target and move farther away.
Vật tạo ra thực thi hành vi Bỏ trốn di chuyển (Paving Escape), một chiến thuật dùng để chạy trốn khỏi Mục tiêu. Nó cố gắng quay lưng lại với Mục tiêu và di chuyển ra xa hơn.

Allows you to configure multiple segments of Escape Motion. Each segment/run calculates one escape point.
Cho phép bạn cấu hình nhiều phân đoạn của Hành động Bỏ trốn. Mỗi phân đoạn/đợt chạy sẽ tính toán một điểm trốn thoát.

Execution Conditions (Điều kiện Thực thi):



When the Creation is not in CD, and is inside its Territory, it will trigger fleeing behavior once their distance to the Target is less than *Flee Trigger Distance*.
Khi Vật tạo ra không trong thời gian Hồi chiêu (CD), và đang ở trong Lãnh thổ của nó, nó sẽ kích hoạt hành vi bỏ trốn một khi khoảng cách tới Mục tiêu nhỏ hơn *Khoảng cách Kích hoạt Bỏ trốn* (Flee Trigger Distance).

### 3. Tactic: Ground Idle Roaming (Chiến thuật: Đi lang thang trên mặt đất)
The Creation executes a Paving Roam, walking randomly within the AoE.
Vật tạo ra thực thi hành vi Đi lang thang (Paving Roam), bước đi ngẫu nhiên trong Khu vực Hiệu ứng (AoE).

Execution Conditions (Điều kiện Thực thi):



Affected by *Creation Underclock*, Creations that are too far from the Character will not enter this Tactic.
Chịu ảnh hưởng bởi *Creation Underclock* (Hạ xung Vật tạo ra), những Vật tạo ra ở quá xa Nhân vật sẽ không tiến vào Chiến thuật này.



Select a suitable Target Point.
Chọn một Điểm Mục tiêu phù hợp.

Point Selection Rules (Quy tắc Chọn Điểm):



Unlike most tactics, the point-selection logic for the *Paving Roam* tactic runs when it is **potentially** possible to execute *Paving Roam*, but before you Enter it.
Khác với hầu hết các chiến thuật, logic chọn điểm cho chiến thuật *Đi lang thang* sẽ chạy khi **có khả năng** thực thi *Đi lang thang*, nhưng xảy ra trước khi bạn Thực sự tiến vào (Enter) nó.

Because choosing the right Target Point is one of the requirements for entering this Tactic.
Bởi vì việc chọn đúng Điểm Mục tiêu là một trong những yêu cầu để tiến vào Chiến thuật này.



Upon entering a Tactic, execute the Motion quest immediately. Keep it running until the Motion stops (when you reach the destination or hit an obstacle). Then apply the CD and exit the Tactic.
Khi tiến vào một Chiến thuật, thực thi nhiệm vụ Di chuyển ngay lập tức. Giữ cho nó chạy cho đến khi Di chuyển dừng lại (khi bạn đến đích hoặc va phải chướng ngại vật). Sau đó áp dụng Hồi chiêu (CD) và thoát khỏi Chiến thuật.



If a Creation's current Location is already outside the *Roaming Radius* AoE, the *Paving Roam* Tactic selects a point in the direction from the current location toward the Spawn Point, at a distance equal to the *Roaming Radius*, as the Target Point.
Nếu Vị trí hiện tại của một Vật tạo ra đã nằm ngoài vùng AoE *Bán kính Lang thang* (Roaming Radius), chiến thuật *Đi lang thang* sẽ chọn một điểm theo hướng từ vị trí hiện tại đi tới Điểm Hồi sinh (Spawn Point), với khoảng cách bằng với *Bán kính Lang thang*, để làm Điểm Mục tiêu.



If Pathfinding is supported, it will be used to check whether the Target Point is valid.
Nếu tính năng Tìm đường được hỗ trợ, nó sẽ được dùng để kiểm tra xem Điểm Mục tiêu có hợp lệ hay không.

### 4. Tactic: Ground Pursuit (Chiến thuật: Truy đuổi trên mặt đất)
The Creation executes a Paving Pursuit.
Vật tạo ra thực thi hành vi Truy đuổi (Paving Pursuit).

Target Pursuit Tactic automatically selects a suitable location near the Target as the Target Point.
Chiến thuật Truy đuổi Mục tiêu tự động chọn một vị trí phù hợp gần Mục tiêu để làm Điểm Mục tiêu.

Execution Conditions (Điều kiện Thực thi):

[Required] (Bắt buộc)

1.

Has a Target.
Có một Mục tiêu.

2.

Not airborne.
Không ở trên không.

3.

This unit or the target is within the Territory Range.
Đơn vị này hoặc mục tiêu đang ở trong Phạm vi Lãnh thổ.

[Meet any one of the Conditions] (Thỏa mãn bất kỳ Điều kiện nào)

1.

If this unit is not currently in this Tactic and the distance between the unit and the Target is within [*Minimum Pursuit Trigger Distance*, *Maximum Pursuit Trigger Distance*], the unit will enter this Tactic.
Nếu đơn vị này hiện không ở trong Chiến thuật này và khoảng cách giữa đơn vị và Mục tiêu nằm trong khoảng [*Khoảng cách Kích hoạt Truy đuổi Tối thiểu*, *Khoảng cách Kích hoạt Truy đuổi Tối đa*], đơn vị sẽ tiến vào Chiến thuật này.

2.

When already in the Tactic, the unit will continue to execute the Tactic only if the distance between this unit and the Target is greater than the *Stop Pursuit Distance*.
Khi đã ở trong Chiến thuật, đơn vị sẽ tiếp tục thực thi Chiến thuật chỉ khi khoảng cách giữa đơn vị này và Mục tiêu lớn hơn *Khoảng cách Dừng Truy đuổi*.

### 5. Tactic: Stand Still (Chiến thuật: Đứng yên)
The Creation executes the Idle behavior.
Vật tạo ra thực thi hành vi Đứng im (Idle).

### 6. Tactic: Return to Spawn Point After Leaving Battle (Chiến thuật: Quay về Điểm Hồi sinh Sau Khi Rời Khỏi Trận Chiến)
The Creation returns to the Spawn Point after leaving battle.
Vật tạo ra quay trở về Điểm Hồi sinh sau khi rời khỏi trạng thái chiến đấu.

A tactic that makes a unit return to the initial point when leaving battle. While this tactic is running, the Aggro system is disabled and will not be re-enabled until the tactic ends.
Một chiến thuật làm cho đơn vị quay trở lại điểm khởi đầu khi rời khỏi trận chiến. Khi chiến thuật này đang chạy, hệ thống Aggro (Khiêu khích) bị vô hiệu hóa và sẽ không được kích hoạt lại cho đến khi chiến thuật kết thúc.

Execution Conditions (Điều kiện Thực thi):

3.

This is only available in the pre-battle and out-of-battle phases. Place it first in your pre-battle Tactics so the Aggro system switches to it as soon as the battle ends.
Chỉ khả dụng trong giai đoạn trước trận chiến và ngoài trận chiến. Hãy đặt nó lên đầu trong các Chiến thuật trước trận chiến để hệ thống Aggro chuyển sang nó ngay sau khi trận chiến kết thúc.

Select Target Points (Chọn Điểm Mục tiêu):

The Target Point is selected on the frame you enter the Tactic, and it will not be edited while the Tactic is being executed.
Điểm Mục tiêu được chọn tại khung hình bạn tiến vào Chiến thuật, và nó sẽ không bị thay đổi trong lúc Chiến thuật đang được thực thi.

Check the following conditions in order. When a condition is met, set the Target Point based on that item.
Kiểm tra các điều kiện sau theo thứ tự. Khi một điều kiện được thỏa mãn, hãy thiết lập Điểm Mục tiêu dựa trên mục đó.

a.

When the [Execute a Patrol] Tactic is performed and *Set End Point to Spawn Point* is enabled, the new Spawn Point will be used as the Target Point.
Khi Chiến thuật [Thực thi Tuần tra] (Execute a Patrol) được thực hiện và *Thiết lập Điểm Kết thúc thành Điểm Hồi sinh* được bật, Điểm Hồi sinh mới sẽ được sử dụng làm Điểm Mục tiêu.

b.

Set the Spawn Point as the Target Point.
Thiết lập Điểm Hồi sinh làm Điểm Mục tiêu.

### 7. Tactic: Rotate to the Target Entity (Chiến thuật: Xoay về phía Thực thể Mục tiêu)
The Creation rotates to face the Target Entity.
Vật tạo ra xoay người để hướng mặt về phía Thực thể Mục tiêu.

### 8. Tactic: Rotate to the Specified Direction (Chiến thuật: Xoay về phía Hướng Chỉ định)
The Creation rotates to the Specified Orientation.
Vật tạo ra xoay về phía Hướng đã chỉ định.

### 9. Tactic: Rotate by Specified Angle (Chiến thuật: Xoay theo Góc Chỉ định)
The Creation rotates by the specified angle, and the Angular Velocity may have minor deviations during actual operation.
Vật tạo ra xoay theo một góc nhất định, và Vận tốc Góc (Angular Velocity) có thể có những sai lệch nhỏ trong quá trình vận hành thực tế.

### 10. Tactic: Move to the Target Position (Chiến thuật: Di chuyển đến Vị trí Mục tiêu)
The Creation moves to the Target Point.
Vật tạo ra di chuyển đến Điểm Mục tiêu.

### 11. Tactic: Move to the Target Entity (Chiến thuật: Di chuyển đến Thực thể Mục tiêu)
The Creation moves to the Target Entity.
Vật tạo ra di chuyển đến Thực thể Mục tiêu.

## I. General (Cài đặt chung)
### 12. Tactic: Execute Patrol (Chiến thuật: Thực thi Tuần tra)
A tactic setting where the Creation executes its patrol, using its configured Patrol Template to drive its motion.
Một thiết lập chiến thuật nơi Vật tạo ra thực thi việc tuần tra, sử dụng Mẫu Tuần tra (Patrol Template) đã được cấu hình để điều khiển di chuyển của nó.

Execution Conditions (Điều kiện Thực thi):

4.

The Creation is configured with a Patrol Template.
Vật tạo ra được cấu hình với một Mẫu Tuần tra.

5.

Patrol Template referenced by Tactics; the referenced path data is not empty.
Mẫu Tuần tra được tham chiếu bởi Chiến thuật; dữ liệu đường dẫn được tham chiếu không được bỏ trống.

### 1. Multiple Branches (Rẽ nhánh Đa luồng)
Accepts one input parameter as the control expression (supports Integer or String). Branches into multiple paths based on its value.
Chấp nhận một tham số đầu vào làm biểu thức điều khiển (hỗ trợ Số nguyên hoặc Chuỗi). Tách thành nhiều luồng rẽ nhánh dựa trên giá trị của nó.

When the value on an Output Pin equals the control expression, execution continues along that Output Pin. If no pin matches, the [Default] pin is taken.
Khi giá trị trên một Chốt Đầu ra (Output Pin) bằng với biểu thức điều khiển, quá trình thực thi tiếp tục theo Chốt Đầu ra đó. Nếu không có chốt nào khớp, chốt [Mặc định] (Default) sẽ được chọn.

### 2. Double Branch (Rẽ nhánh Đôi)
Branches into True or False based on the evaluated condition.
Rẽ nhánh thành Đúng (True) hoặc Sai (False) dựa trên điều kiện được đánh giá.

When the Boolean is True, the [True] execution flow runs; when it is False, the [False] execution flow runs.
Khi Boolean là Đúng, luồng thực thi [True] sẽ chạy; khi nó là Sai, luồng thực thi [False] sẽ chạy.

### 1. Multiple Branches (Rẽ nhánh Đa luồng)
Accepts one input parameter as the control expression (supports Integer or String). Branches into multiple paths based on its value.
Chấp nhận một tham số đầu vào làm biểu thức điều khiển (hỗ trợ Số nguyên hoặc Chuỗi). Tách thành nhiều luồng rẽ nhánh dựa trên giá trị của nó.

When the value on an Output Pin equals the control expression, execution continues along that Output Pin. If no pin matches, the [Default] pin is taken.
Khi giá trị trên một Chốt Đầu ra (Output Pin) bằng với biểu thức điều khiển, quá trình thực thi tiếp tục theo Chốt Đầu ra đó. Nếu không có chốt nào khớp, chốt [Mặc định] (Default) sẽ được chọn.

### 2. Double Branch (Rẽ nhánh Đôi)
Branches into True or False based on the evaluated condition.
Rẽ nhánh thành Đúng (True) hoặc Sai (False) dựa trên điều kiện được đánh giá.

When the Boolean is True, the [True] execution flow runs; when it is False, the [False] execution flow runs.
Khi Boolean là Đúng, luồng thực thi [True] sẽ chạy; khi nó là Sai, luồng thực thi [False] sẽ chạy.

### 1. Double Branch (Rẽ nhánh Đôi)
Branches into True or False based on the evaluated condition.
Rẽ nhánh thành Đúng (True) hoặc Sai (False) dựa trên điều kiện được đánh giá.

When the Boolean is True, the [True] execution flow runs; when it is False, the [False] execution flow runs.
Khi Boolean là Đúng, luồng thực thi [True] sẽ chạy; khi nó là Sai, luồng thực thi [False] sẽ chạy.

### 2.** **Multiple Branches (Rẽ nhánh Đa luồng)
Takes an input parameter as a control expression (supports integers or strings). Multiple branches can be defined based on the value of the control expression.
Lấy một tham số đầu vào làm biểu thức điều khiển (hỗ trợ số nguyên hoặc chuỗi). Có thể xác định nhiều rẽ nhánh dựa trên giá trị của biểu thức điều khiển.

Execution follows the output pin whose value matches the control expression. If no matching pin is found, it will proceed through the [Default] pin.
Quá trình thực thi chạy theo chốt đầu ra có giá trị khớp với biểu thức điều khiển. Nếu không có chốt nào khớp, nó sẽ xử lý thông qua chốt [Mặc định].

### 1. Double Branch (Rẽ nhánh Đôi)
Branches into True or False based on the evaluated condition.
Rẽ nhánh thành Đúng (True) hoặc Sai (False) dựa trên điều kiện được đánh giá.

When the Boolean is True, the [True] execution flow runs; when it is False, the [False] execution flow runs.
Khi Boolean là Đúng, luồng thực thi [True] sẽ chạy; khi nó là Sai, luồng thực thi [False] sẽ chạy.

### 2.** **Multiple Branches (Rẽ nhánh Đa luồng)
Takes an input parameter as a control expression (supports integers or strings). Multiple branches can be defined based on the value of the control expression.
Lấy một tham số đầu vào làm biểu thức điều khiển (hỗ trợ số nguyên hoặc chuỗi). Có thể xác định nhiều rẽ nhánh dựa trên giá trị của biểu thức điều khiển.

Execution follows the output pin whose value matches the control expression. If no matching pin is found, it will proceed through the [Default] pin.
Quá trình thực thi chạy theo chốt đầu ra có giá trị khớp với biểu thức điều khiển. Nếu không có chốt nào khớp, nó sẽ xử lý thông qua chốt [Mặc định].

### 1. Enumeration Match (Kiểm tra Khớp Kiểu Liệt kê)
After confirming the Enumeration type, determines whether the two input values are equal.
Sau khi xác nhận loại Liệt kê (Enumeration), quyết định xem hai giá trị đầu vào có bằng nhau hay không.

### 2. Equal (Bằng nhau)
Determines whether two inputs are equal.
Xác định xem hai đầu vào có bằng nhau hay không.

Some Parameter Types have special comparison rules:
Một số Loại Tham số có quy tắc so sánh đặc biệt:

Floating Point Numbers: Floating Point Numbers are compared using approximate equality. When the difference between two Floating Point Numbers is less than an extremely small value, the two numbers are considered equal. For example: 2.0000001 and 2.0 are considered equal.
Số Thực (Float): Các số thực được so sánh sử dụng giá trị bằng nhau gần đúng. Khi sự khác biệt giữa hai Số Thực nhỏ hơn một giá trị vô cùng nhỏ, hai số đó được coi là bằng nhau. Ví dụ: 2.0000001 và 2.0 được coi là bằng nhau.

3D Vector: The x, y, and z components of a 3D Vector are compared using Floating Point approximate equality.
Vector 3D: Các thành phần x, y và z của một Vector 3D được so sánh sử dụng giá trị bằng nhau gần đúng của số thực.

### 2. Assembly Dictionary (Lắp ráp Từ điển)
Combine up to 50 key-value pairs into a dictionary.
Kết hợp tối đa 50 cặp khóa-giá trị vào một từ điển (Dictionary).

### 1. Enumeration Match (Kiểm tra Khớp Kiểu Liệt kê)
After confirming the Enumeration type, determines whether the two input values are equal.
Sau khi xác nhận loại Liệt kê (Enumeration), quyết định xem hai giá trị đầu vào có bằng nhau hay không.

### 2. Equal (Bằng nhau)
Determines whether two inputs are equal.
Xác định xem hai đầu vào có bằng nhau hay không.

Some Parameter Types have special comparison rules:
Một số Loại Tham số có quy tắc so sánh đặc biệt:

Floating Point Numbers: Floating Point Numbers are compared using approximate equality. When the difference between two Floating Point Numbers is less than an extremely small value, the two numbers are considered equal. For example: 2.0000001 and 2.0 are considered equal.
Số Thực (Float): Các số thực được so sánh sử dụng giá trị bằng nhau gần đúng. Khi sự khác biệt giữa hai Số Thực nhỏ hơn một giá trị vô cùng nhỏ, hai số đó được coi là bằng nhau. Ví dụ: 2.0000001 và 2.0 được coi là bằng nhau.

3D Vector: The x, y, and z components of a 3D Vector are compared using Floating Point approximate equality.
Vector 3D: Các thành phần x, y và z của một Vector 3D được so sánh sử dụng giá trị bằng nhau gần đúng của số thực.

### 2. Assemble Structures (Lắp ráp Cấu trúc)
Combines multiple parameters into a single Structure-type value.
Kết hợp nhiều tham số vào một giá trị Kiểu cấu trúc (Structure) duy nhất.

### 1. Enumeration Match (Kiểm tra Khớp Kiểu Liệt kê)
After confirming the Enumeration type, determines whether the two input values are equal.
Sau khi xác nhận loại Liệt kê (Enumeration), quyết định xem hai giá trị đầu vào có bằng nhau hay không.

### 2. Equal (Bằng nhau)
Determines whether two inputs are equal.
Xác định xem hai đầu vào có bằng nhau hay không.

Some Parameter Types have special comparison rules:
Một số Loại Tham số có quy tắc so sánh đặc biệt:

Floating Point Numbers: Floating Point Numbers are compared using approximate equality. When the difference between two Floating Point Numbers is less than an extremely small value, the two numbers are considered equal. For example: 2.0000001 and 2.0 are considered equal.
Số Thực (Float): Các số thực được so sánh sử dụng giá trị bằng nhau gần đúng. Khi sự khác biệt giữa hai Số Thực nhỏ hơn một giá trị vô cùng nhỏ, hai số đó được coi là bằng nhau. Ví dụ: 2.0000001 và 2.0 được coi là bằng nhau.

3D Vector: The x, y, and z components of a 3D Vector are compared using Floating Point approximate equality.
Vector 3D: Các thành phần x, y và z của một Vector 3D được so sánh sử dụng giá trị bằng nhau gần đúng của số thực.

### 2. Assemble Structure (Lắp ráp Cấu trúc)
Combines multiple parameters into a single Structure-type value.
Kết hợp nhiều tham số vào một giá trị Kiểu cấu trúc (Structure) duy nhất.

### 1. Enumeration Match (Kiểm tra Khớp Kiểu Liệt kê)
After confirming the Enumeration type, determines whether the two input values are equal.
Sau khi xác nhận loại Liệt kê (Enumeration), quyết định xem hai giá trị đầu vào có bằng nhau hay không.

### 2. Equal (Bằng nhau)
Determines whether two inputs are equal.
Xác định xem hai đầu vào có bằng nhau hay không.

Some Parameter Types have special comparison rules:
Một số Loại Tham số có quy tắc so sánh đặc biệt:

Floating Point Numbers: Floating Point Numbers are compared using approximate equality. When the difference between two Floating Point Numbers is less than an extremely small value, the two numbers are considered equal. For example: 2.0000001 and 2.0 are considered equal.
Số Thực (Float): Các số thực được so sánh sử dụng giá trị bằng nhau gần đúng. Khi sự khác biệt giữa hai Số Thực nhỏ hơn một giá trị vô cùng nhỏ, hai số đó được coi là bằng nhau. Ví dụ: 2.0000001 và 2.0 được coi là bằng nhau.

3D Vector: The x, y, and z components of a 3D Vector are compared using Floating Point approximate equality.
Vector 3D: Các thành phần x, y và z của một Vector 3D được so sánh sử dụng giá trị bằng nhau gần đúng của số thực.

### 2. Assembly Dictionary (Lắp ráp Từ điển)
Combine up to 50 key-value pairs into a dictionary.
Kết hợp tối đa 50 cặp khóa-giá trị vào một từ điển (Dictionary).

### 1. Enumeration Match (Kiểm tra Khớp Kiểu Liệt kê)
After confirming the Enumeration type, determines whether the two input values are equal.
Sau khi xác nhận loại Liệt kê (Enumeration), quyết định xem hai giá trị đầu vào có bằng nhau hay không.

### 2. Equal (Bằng nhau)
Determines whether two inputs are equal.
Xác định xem hai đầu vào có bằng nhau hay không.

Some Parameter Types have special comparison rules:
Một số Loại Tham số có quy tắc so sánh đặc biệt:

Floating Point Numbers: Floating Point Numbers are compared using approximate equality. When the difference between two Floating Point Numbers is less than an extremely small value, the two numbers are considered equal. For example: 2.0000001 and 2.0 are considered equal.
Số Thực (Float): Các số thực được so sánh sử dụng giá trị bằng nhau gần đúng. Khi sự khác biệt giữa hai Số Thực nhỏ hơn một giá trị vô cùng nhỏ, hai số đó được coi là bằng nhau. Ví dụ: 2.0000001 và 2.0 được coi là bằng nhau.

3D Vector: The x, y, and z components of a 3D Vector are compared using Floating Point approximate equality.
Vector 3D: Các thành phần x, y và z của một Vector 3D được so sánh sử dụng giá trị bằng nhau gần đúng của số thực.

### 1. Whether the Entity Has the Specified Unit Status (Kiểm tra Thực thể Có Trạng thái Đơn vị Chỉ định Không)
Query whether the entity has the specified unit status.
Truy vấn xem thực thể có trạng thái đơn vị (Unit Status) được chỉ định hay không.

### 1. Check Target Position Pathfinding Availability (Kiểm tra Khả năng Tìm đường tới Vị trí Mục tiêu)
Check whether a Creation can reach the current Target Point using normal pathfinding.
Kiểm tra xem một Vật tạo ra có thể đến được Điểm Mục tiêu hiện tại thông qua chức năng tìm đường (pathfinding) thông thường hay không.

### 2. Check the Coordinates When Entering Battle (Kiểm tra Tọa độ Khi Bắt đầu Trận chiến)
Query the Coordinate Points when a Creation enters battle.
Truy vấn các Điểm Tọa độ (Coordinate Points) khi một Vật tạo ra bắt đầu tiến vào trạng thái chiến đấu.

### 3. Check If Entity Is on the Field (Kiểm tra Xem Thực thể Có trên Sân Không)
Check whether the Target Entity is present. Note: even if a Character Entity is in a Down state, it is still considered present.
Kiểm tra xem Thực thể Mục tiêu có đang tồn tại trên sân hay không. Lưu ý: ngay cả khi Thực thể Nhân vật đang trong trạng thái gục ngã (Down), nó vẫn được coi là đang có mặt.

### 4. Check the Vertical Angle From Self to Target (Kiểm tra Góc Dọc Từ Bản thân tới Mục tiêu)
Query the vertical angle between the Creation and the Target Entity. Valid only when the Creation has a Target.
Truy vấn góc dọc giữa Vật tạo ra và Thực thể Mục tiêu. Chỉ hợp lệ khi Vật tạo ra có một Mục tiêu.

### 5. Check the Vertical Distance From Self to Target (Kiểm tra Khoảng cách Dọc Từ Bản thân tới Mục tiêu)
Query the vertical distance from this Creation to its Target Entity. Valid only when the Creation has a Target.
Truy vấn khoảng cách dọc từ Vật tạo ra này tới Thực thể Mục tiêu của nó. Chỉ hợp lệ khi Vật tạo ra có một Mục tiêu.

### 6. Check the Distance From Self to Target (Kiểm tra Khoảng cách Từ Bản thân tới Mục tiêu)
Query the distance from this Creation to its Target Entity. Valid only when the Creation has a Target.
Truy vấn khoảng cách từ Vật tạo ra này tới Thực thể Mục tiêu của nó. Chỉ hợp lệ khi Vật tạo ra có một Mục tiêu.

### 7. Check the Horizontal Angle From Self to Target (Kiểm tra Góc Ngang Từ Bản thân tới Mục tiêu)
Query the horizontal angle between this Creation and the Target Entity. Valid only when the Creation has a Target.
Truy vấn góc ngang giữa Vật tạo ra này và Thực thể Mục tiêu. Chỉ hợp lệ khi Vật tạo ra có một Mục tiêu.

### 8. Check the Horizontal Distance From Self to Target (Kiểm tra Khoảng cách Ngang Từ Bản thân tới Mục tiêu)
Query the horizontal distance from this Creation to the Target Entity. Valid only when the Creation has a Target.
Truy vấn khoảng cách ngang từ Vật tạo ra này tới Thực thể Mục tiêu. Chỉ hợp lệ khi Vật tạo ra có một Mục tiêu.

### 9. Check Whether Self Is in Battle (Kiểm tra Xem Bản thân Có Trong Trận chiến Không)
Check whether the Creation is currently in battle.
Kiểm tra xem Vật tạo ra có đang trong trạng thái chiến đấu hay không.

### 10. Check if Self Is in the Territory (Kiểm tra Xem Bản thân Có Nằm trong Lãnh thổ Không)
Check whether this Creation's current location is within the Territory.

### 11. Check Whether Self Is Using a Skill (Kiểm tra Xem Bản thân Có Đang Dùng Kỹ năng Không)
Check whether a Creation is currently casting a Skill. If so, returns the index of the Skill being cast.
Kiểm tra xem một Vật tạo ra có đang thi triển Kỹ năng hay không. Nếu có, nó sẽ trả về chỉ mục của Kỹ năng đang được sử dụng.

### 12. Get Spawn Point Location Information (Nhận Thông tin Vị trí Điểm Hồi sinh)
Obtain the Creation's own Spawn Point information.
Lấy thông tin Điểm Hồi sinh (Spawn Point) của chính Vật tạo ra.

### 13. Get Stage Entity (Nhận Thực thể Màn chơi)
Obtain Stage Entities.
Lấy các Thực thể của Màn chơi (Stage Entities).

### 14. Get Target Level (Nhận Cấp độ Mục tiêu)
Obtain the Target Entity's current level.
Lấy cấp độ hiện tại của Thực thể Mục tiêu.

### 15. Get Target ATK (Nhận Sát thương Tấn công Mục tiêu)
Obtain the Target Entity's ATK parameters.
Lấy các thông số Tấn công (ATK) của Thực thể Mục tiêu.

### 16. Get Target HP
Obtain HP-related parameters for the Target Entity

### 17. Get Target Entity
Obtain the Creation's current Target Entity. Valid only when the Creation has a Target.

### 18. Get Previous Frame Execution Tactic
Obtain the Tactic executed by Creations in the previous frame

### 19. Get Previous Frame Execution Status
Obtain the Config ID of the [Creation Status Node Graph] executed in the previous frame

### 20. Get Entity's Type
Obtain the Target Entity's Type

### 21. Get Entity Location
Obtain the Target Entity's Location

### 22. Get Entity Rotation
Obtain the Target Entity's Rotation

### 23. Get Object Preset Status
Obtain the Preset Status Value at the specified Preset Status index from the Target Entity. If the Entity does not have the specified Preset Status, return 0

### 24. Get Custom Variable
Obtain the Variable Value of the specified Custom Variable from the Target Entity. If the variable does not exist, returns the default value for that type

### 25. Get Current Execution Status
Obtain the config ID of the [Creation Status Node Graph] currently being executed by this Creation

### 26. Get Self Entity
Returns the Entity associated with this Node Graph

### 6. Query Dictionary Value by Key
Query the corresponding Value in the Dictionary by Key. If the Key does not exist, returns the type's default value

### 1. Check Target Position Pathfinding Availability
Check whether a Creation can reach the current Target Point using normal pathfinding

### 2. Check the Coordinates When Entering Battle
Query the Coordinate Points when a Creation enters battle

### 3. Check If Entity Is on the Field
Check whether the Target Entity is present. Note: even if a Character Entity is in a Down state, it is still considered present

### 4. Check the Vertical Angle From Self to Target
Query the vertical angle between the Creation and the Target Entity. Valid only when the Creation has a Target

### 5. Check the Vertical Distance From Self to Target
Query the vertical distance from this Creation to its Target Entity. Valid only when the Creation has a Target

### 6. Check the Distance From Self to Target
Query the distance from this Creation to its Target Entity. Valid only when the Creation has a Target

### 7. Check the Horizontal Angle From Self to Target
Query the horizontal angle between this Creation and the Target Entity. Valid only when the Creation has a Target

### 8. Check the Horizontal Distance From Self to Target
Query the horizontal distance from this Creation to the Target Entity. Valid only when the Creation has a Target

### 9. Check Whether Self Is in Battle
Check whether the Creation is currently in battle

### 10. Check if Self Is in the Territory
Check whether this Creation's current location is within the Territory

### 11. Check Whether Self Is Using a Skill
Check whether a Creation is currently casting a Skill. If so, returns the index of the Skill being cast

### 12. Get Spawn Point Location Information
Obtain the Creation's own Spawn Point information


Obtain Stage Entities

### 14. Get Target Level
Obtain the Target Entity's current level

### 15. Get Target ATK
Obtain the Target Entity's ATK parameters

### 16. Get Target HP
Obtain HP-related parameters for the Target Entity

### 17. Get Target Entity
Obtain the Creation's current Target Entity. Valid only when the Creation has a Target.

### 18. Get Previous Frame Execution Tactic
Obtain the Tactic executed by Creations in the previous frame

### 19. Get Previous Frame Execution Status
Obtain the Config ID of the [Creation Status Node Graph] executed in the previous frame

### 20. Get Entity's Type
Obtain the Target Entity's Type

### 21. Get Entity Location
Obtain the Target Entity's Location

### 22. Get Entity Rotation
Obtain the Target Entity's Rotation

### 23. Get Object Preset Status
Obtain the Preset Status Value at the specified Preset Status index from the Target Entity. If the Entity does not have the specified Preset Status, return 0

### 24. Get Custom Variable
Obtain the Variable Value of the specified Custom Variable from the Target Entity. If the variable does not exist, returns the default value for that type

### 25. Get Current Execution Status
Obtain the config ID of the [Creation Status Node Graph] currently being executed by this Creation

### 26. Get Self Entity
Returns the Entity associated with this Node Graph

## I. Character Skills
### 1. Switch to self execution status
Once the execution conditions are met, run the Status Node Graph linked to this config ID

### 1. Traverse Entity List
Iterates through each Entity in the input Entity List

### 2. Play Timed Effects
Plays Timed Effects at the specified World Location

### 3. Fixed-Point Projectile Launch
Spawns a Local Projectile at the specified Location in the World Coordinate System

### 4. Fixed-Point Displacement
Moves from the current Location to the Target Location

Supports configuring movement duration and speed; if both are small, the movement may not reach the Target Location

### 5. Recover Character's HP
Initiates a one-time HP restoration for the Target Entity

### 6. Camera Orientation Detection Data
Casts a ray from the Camera to the emission Location and returns the Rotation and Location of valid Targets along the path

### 7. Force Exit Aiming State
When the character is in the aiming state, they will be forced to exit the aiming state.

### 8. Set Own Attack Target
Sets the Target Entity as its Attack Target

### 9. Trigger Hitbox at Specific Location
Initiates a Hitbox Attack at the specified Location in the World Coordinate System, with configurable attack parameters

### 10. Add Unit Status
Applies the Unit Status defined by the configuration ID to the Target

### 11. Notify Server Node Graph
Notifies the Server Node Graph; supports up to three String parameters

At runtime, forwards logic to the Server Node Graph and triggers the [On Skill Node Call] Event on the Server Node Graph

### 12. Player Turning
Turns the Player using the configured turning mode

### 13. Player Turns to Face Set Direction
Turns the Player toward the direction specified by the 3D Vector configuration

### 14. Set Attack Weight
You can set the weight of the current attack target

### 15. Remove Unit Status
Removes the Unit Status corresponding to the specified configuration ID from the Target Entity

### 16. Remove Specified Character Disruptor Device
Removes the specified type of Character Disruptor Device

### 17. Trigger Hitbox at Specific Location
Initiates a Hitbox Attack at the specified Attachment Point, with configurable attack parameters

### 18. Reset Skill Target
Resets the Skill Target and reruns the Skill selection logic to choose a new Target

### 19. Trigger Rectangular Hitbox at Specific Location
Initiate a rectangular hitbox at the specified position in the world coordinate system, and you can set various parameters for this attack.

### 20. Trigger Spherical Hitbox at Specific Location
Initiate a spherical hitbox at the specified position in the world coordinate system, and you can set various parameters for this attack.

### 21. Trigger Sector Hitbox at Specific Location
Initiate a sector hitbox at the specified position in the world coordinate system, and you can set various parameters for this attack.

### 22. Trigger Rectangular Hitbox at Specified Attachment Point
Initiate a rectangular hitbox at the specified attachment point, and you can set various parameters for this attack.

### 23. Trigger Spherical Hitbox at Specified Attachment Point
Initiate a spherical hitbox at the specified attachment point, and you can set various parameters for this attack.

### 24. Trigger Sector Hitbox at Specified Attachment Point
Initiate a sector hitbox at the specified attachment point, and you can set various parameters for this attack.

### 25. Interrupt Current Skil**l
Interrupts the skill currently being cast by the character

### 26. Set Skill Variable
Sets the value of the specified skill variable

### 27. Increase Skill Variable Value
Increases the value of the specified skill variable. The increment can be a negative value.

### 28. Character Blink
Makes the character blink to the target position, with the direction they are facing post-blink adjustable. The maximum blink distance is 200 meters.

### 29. Add Key Behavior
Adds a key behavior with the corresponding ID to the Key Behavior Log Panel, and records the current time along with it. The maximum number of key behaviors that can be recorded is 20.

### 30. Clear Key Behavior Log Panel
Clears all recorded key behaviors from the Key Behavior Log Panel.

### 31. Cast Skill From Specified Slot
Makes the character cast the skill corresponding to the specified Skill Instance ID.

For the button to be usable, the skill must be bound to a button and currently be in the foreground

## II. General
### 32. Cast Skill From Specified Slot
Makes the character cast the skill that is currently in the foreground for the corresponding skill slot.

For the button to be usable, the skill must be bound to a button and currently be in the foreground

### 1. Set Local Variable
Sets the value of a local variable

### 2. Break Loop
Break out of a Finite Loop. The output pin must connect to the [Break Loop] input parameter of the [Finite Loop] Node

### 26. Increase Skill Variable Value
Adds the given value to the specified Skill Variable. Value can be negative

### 1. Set Local Variable
Sets the value of a Local Variable

### 2. Break Loop
Break out of a Finite Loop. The output pin must connect to the [Break Loop] input parameter of the [Finite Loop] Node

### 3. Notify Server Node Graph
Notifies the Server Node Graph; supports up to three String parameters

At runtime, forwards logic to the Server Node Graph and triggers the [On Skill Node Call] Event on the Server Node Graph

## III. Custom Aggro
### 3. Finite Loop
From the [Loop Start Value] to the [Loop End Value], the loop iterates, incrementing the Integer by 1 each time. On each iteration, it executes the Nodes connected to [Loop Body]. After a full iteration, it executes the Nodes connected to [Loop Complete].

Use [Break Loop] to end the iteration early

### 1. Set the Aggro Value of the Specified Entity Proportionally
Available only in Custom Aggro Mode

Set the aggro value of the target entity for the specified aggro owner proportionally.

### 2. Transfer the Aggro Value of the Specified Entity Proportionally
Available only in Custom Aggro Mode

Transfers a percentage of Aggro on the Aggro Owner from the Source Entity to the Target Entity

### 3. Taunt Target
Available only in Custom Aggro Mode

The Taunter Entity taunts the specified Target Entity

### 4. Remove Target Entity From Aggro List
Available only in Custom Aggro Mode

Removes the Target Entity from the Aggro Owner Entity's Aggro List; this may cause the Target Entity to leave battle

### 5. Clear the Aggro List of the Specified Entity
Available only in Custom Aggro Mode

Clears the Aggro List of the specified Entity; this usually causes the Target to leave battle

### 6. Set the Aggro Value of the Specified Entity
Available only in Custom Aggro Mode

Sets the Aggro Value of the specified Entity on the Aggro Owner Entity

## IV. Signal
### 7. Increase the Aggro Value of the Specified Entity
Available only in Custom Aggro Mode

Modify the aggro value of the specified entity for the aggro owner entity; the increase value can be negative.

## I. Skills
### 1.** **Send Signal to Server Node Graph
Within the skill node graph, signals can be sent to the server node graph, and all server node graphs can listen for this signal.

### 1. Traverse Entity List
Iterates through each Entity in the input Entity List

### 2. Play Timed Effects
Plays Timed Effects at the specified World Location

### 3. Fixed-Point Projectile Launch
Spawns a Local Projectile at the specified Location in the World Coordinate System

### 4. Complex Creation Directed Movement
Moves from the current Location to the Target Location

You can configure the Maximum Distance. If this value is too small, the object may not be able to move to the Target Location

### 5. Complex Creation Teleport
Teleport from your current location to the Target Location

### 6. Recover Creation's HP
Initiates a one-time HP restoration for the Target Entity

### 7. Set the Global CD of the Creation
Permanently changes the Creation's Global CD for this stage run

### 8. Set the Current CD of the Creation Skill
Adjusts only the CD for this Creation Skill for this use. This is a one-time change and will not be saved

Note: When this Node runs, if the Target Skill is currently casting and is configured to trigger its CD when the Skill ends, the CD will be reset to the Skill's configured CD at End. Even if this Node successfully sets the Current CD, it will be overwritten by the CD triggered at Skill End.

### 9. Set the CD of the Creation Skill
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

### 10. Set the Current Time of the Creation Cooldown Group
Adjusts only this Creation's Skill Group CD for this session; changes are not saved

### 11. Set the Time of the Creation Cooldown Group
Permanently changes the Creation's Skill Group CD for this stage run

### 12. Trigger Hitbox at Specific Location
Initiates a Hitbox Attack at the specified Location in the World Coordinate System, with configurable attack parameters

### 13. Trigger Rectangular Hitbox at Specific Location
Initiates a Rectangular HitBox Attack at a specified location in the World Coordinate System, with configurable attack parameters

### 14. Trigger Spherical Hitbox at Specific Location
Initiates a Sphere Hitbox Attack at a specified location in the World Coordinate System, with configurable attack parameters

### 15. Trigger Sector Hitbox at Specific Location
Initiates a Sector Hitbox Attack at a specified location in the World Coordinate System, with configurable attack parameters

### 16. Add Unit Status
Applies the Unit Status defined by the configuration ID to the Target

### 17. Remove Unit Status
Removes the Unit Status corresponding to the specified configuration ID from the Target Entity

### 18. Remove Specified Character Disruptor Device
Removes the specified type of Character Disruptor Device

### 19. Resets the Creation's Skill CD
Resets the Skill CD to 0. If the conditions are met, the Skill can be cast immediately

### 20. Creation Turns to Face Set Direction
Rotates the Creation to face the orientation of the specified 3D Vector

### 21. Trigger Hitbox at Specified Attachment Point
Initiates a Hitbox Attack at a specified Attachment Point, with configurable attack parameters

### 22. Trigger Rectangular Hitbox at Specified Attachment Point
Initiates a Rectangular HitBox Attack from the Specified Attachment Point, with configurable attack parameters

### 23. Trigger Spherical Hitbox at Specified Attachment Point
Initiates a Sphere HitBox Attack from the Specified Attachment Point, with configurable attack parameters

### 24. Trigger Sector Hitbox at Specified Attachment Point
Initiates a Sector HitBox Attack from the Specified Attachment Point, with configurable attack parameters

### 25. Set Skill Variable
Assigns value to specified Skill Variable

### 1. Whether the Entity has the Specified Unit Status
Check whether the Target Entity has the specified Unit Status

### 1.** Get the Complex Creation's Current Using Skill
Return to the ID of the Skill currently being cast by the current Complex Creation

## III. Signals
### 4. Finite Loop
From the [Loop Start Value] to the [Loop Termination Value], the loop iterates, incrementing the Integer by 1 each time. On each iteration, it executes the Nodes connected to [Loop Body]. After a full iteration, it executes the Nodes connected to [Loop Complete].

Use [Break Loop] to end the iteration early

## IV. Custom Aggro
### 1. Send Signal to Server Node Graph
In the Skill Node Graph, you can send a signal to the Server Node Graph, and all Server Node Graphs can monitor that signal

### 1. Set the Aggro Value of the Specified Entity Proportionally
Available only in Custom Aggro Mode

Set the Target Entity's Aggro Value toward the specified Aggro Owner proportionally

### 2. Transfer the Aggro Value of the Specified Entity Proportionally
Available only in Custom Aggro Mode

Transfers a percentage of Aggro on the Aggro Owner from the Source Entity to the Target Entity

### 3. Taunt Target
Available only in Custom Aggro Mode

The Taunter Entity taunts the specified Target Entity

### 4. Remove Target Entity From Aggro List
Available only in Custom Aggro Mode

Removes the Target Entity from the Aggro Owner Entity's Aggro List; this may cause the Target Entity to leave battle

### 5. Clear the Aggro List of the Specified Entity
Available only in Custom Aggro Mode

Clears the Aggro List of the specified Entity; this usually causes the Target to leave battle

### 6. Set the Aggro Value of the Specified Entity
Available only in Custom Aggro Mode

Sets the Aggro Value of the specified Entity on the Aggro Owner Entity

### 7. Increase the Aggro Value of the Specified Entity
Available only in Custom Aggro Mode

Edit the Aggro Value of the Specified Entity on the Aggro Owner, and the added value can be negative

## II. Math
### 3. Data Type Conversion
Converts input parameter types to another type for output. For specific rules, see Basic Concepts - [Conversion Rules Between Basic Data Types]

In the client node, when converting a floating-point number to an integer, the number will be truncated.

### 1. Split 3D Vector
Outputs the x, y, and z components of a 3D Vector as three Floating Point Numbers

### 2. Orientation to Rotation
Converts a Direction Vector to Euler Angles

### 3. Multiplication
Performs multiplication, supporting Floating Point and Integer multiplication

### 4. Division
Performs division, supporting Floating Point division and Integer division. Integer division returns the quotient result

The divisor should not be 0, otherwise it may return an illegal value

### 5. Arccosine Function
Calculates the arccosine of the input and returns the value in radians

### 6. Arctangent Function
Calculates the arctangent of the input and returns the value in radians

### 7. Arcsine Function
Calculates the arcsine of the input and returns the value in radians

### 8. Direction Vector to Rotation
Converts the Forward Vector and Upward Vector to Euler Angles

### 9. Radians to Degrees
Converts radians to degrees

### 10. Get Random Number
Returns a random number in [Lower Limit, Upper Limit] (inclusive)

### 11. Addition
Adds two Floating Point Numbers or Integers

### 12. Subtraction
Subtracts two Floating Point Numbers or Integers

### 13. Degrees to Radians
Converts degrees to radians

### 14. Absolute Value Operation
Returns the absolute value of the input

### 15. Logical NOT Operation
Performs a logical NOT operation on the input Boolean value and returns the result

### 16. Logical OR Operation
Performs a logical OR operation on the two input Boolean values and returns the result

### 17. Logical XOR Operation
Performs a logical XOR operation on the two input Boolean values and returns the result

### 18. Logical AND Operation
Performs a logical AND operation on the two input Boolean values and returns the result

### 19. 3D Vector Normalization
Normalizes the length of a 3D Vector and outputs the result

### 20. 3D Vector Addition
Calculates the sum of two 3D Vectors

### 21. 3D Vector Angle
Calculates the angle between two 3D Vectors and outputs the value in degrees

### 22. 3D Vector Subtraction
Calculates the difference of two 3D Vectors

### 23. 3D Vector Modulo Operation
Calculates the magnitude of the input 3D Vector

### 24. 3D Vector Dot Product
Calculates the dot product of two input 3D Vectors

### 25. 3D Vector Zoom
Scales the input 3D Vector (scalar multiplication) and outputs the result

### 26. 3D Vector Cross Product
Calculates the cross product of two 3D Vectors

### 27. 3D Vector Rotation
Rotates the input 3D Vector by the Euler Angles specified by the rotation and returns the result

### 28. Greater Than
Returns whether the left value is greater than the right value

### 29. Greater Than or Equal To
Returns whether the left value is greater than or equal to the right value

### 30. Less Than
Returns whether the left value is less than the right value

### 31. Less Than or Equal To
Returns whether the left value is less than or equal to the right value

### 32. Cosine Function
Calculates the cosine of the input in radians

### 33. Tangent Function
Calculates the tangent of the input in radians

### 34. Sine Function
Calculates the sine of the input in radians

### 3. Data Type Conversion
Converts input parameter types to another type for output. For specific rules, see Basic Concepts-[Conversion Rules Between Basic Data Types]

In the Local Node, converting Floating Point Numbers to an Integer truncates the decimal part

### 1. Split 3D Vector
Outputs the x, y, and z components of a 3D Vector as three Floating Point Numbers

### 2. Orientation to Rotation
Converts a Direction Vector to Euler Angles

### 3. Multiplication
Performs multiplication, supporting Floating Point and Integer multiplication

### 4. Division
Performs division, supporting Floating Point division and Integer division. Integer division returns the quotient result

The divisor should not be 0, otherwise it may return an illegal value

### 5. Create 3D Vector
Creates a 3D Vector from x, y, and z components

### 6.. Arccosine Function
Calculates the arccosine of the input and returns the value in radians

### 7.. Arctangent Function
Calculates the arctangent of the input and returns the value in radians

### 8.. Arcsine Function
Calculates the arcsine of the input and returns the value in radians

### 9. Direction Vector to Rotation
Converts the Forward Vector and Upward Vector to Euler Angles

### 10. Radians to Degrees
Converts radians to degrees

### 11. Get Random Number
Returns a random number in [Lower Limit, Upper Limit] (inclusive)

### 12. Addition
Adds two Floating Point Numbers or Integers

### 13. Subtraction
Subtracts two Floating Point Numbers or Integers

### 14. Degrees to Radians
Converts degrees to radians

### 15. Absolute Value Operation
Returns the absolute value of the input

### 16. Logical NOT Operation
Performs a logical NOT operation on the input Boolean value and returns the result

### 17. Logical OR Operation
Performs a logical OR operation on the two input Boolean values and returns the result

### 18. Logical XOR Operation
Performs a logical XOR operation on the two input Boolean values and returns the result

### 19. Logical AND Operation
Performs a logical AND operation on the two input Boolean values and returns the result

### 20. Assembly List
Assembles multiple Input Parameters of the same type (up to 10) into a single List

### 21. 3D Vector Normalization
Normalizes the length of a 3D Vector and outputs the result

### 22. 3D Vector Addition
Calculates the sum of two 3D Vectors

### 23. 3D Vector Angle
Calculates the angle between two 3D Vectors and outputs the value in degrees

### 24. 3D Vector Subtraction
Calculates the difference of two 3D Vectors

### 25. 3D Vector Modulo Operation
Calculates the magnitude of the input 3D Vector

### 26. 3D Vector Dot Product
Calculates the dot product of two input 3D Vectors

### 27. 3D Vector Zoom
Scales the input 3D Vector (scalar multiplication) and outputs the result

### 28. 3D Vector Cross Product
Calculates the cross product of two 3D Vectors

### 29. 3D Vector Rotation
Rotates the input 3D Vector by the Euler Angles specified by the rotation and returns the result

### 30. Greater Than
Returns whether the left value is greater than the right value

### 31. Greater Than or Equal To
Returns whether the left value is greater than or equal to the right value

### 32. Less Than
Returns whether the left value is less than the right value

### 33. Less Than or Equal To
Returns whether the left value is less than or equal to the right value

### 34. Cosine Function
Calculates the cosine of the input in radians

### 35. Tangent Function
Calculates the tangent of the input in radians

### 3. Data Type Conversion
Converts input parameter types to another type for output. For specific rules, see Basic Concepts-[Conversion Rules Between Basic Data Types]

In the Local Node, converting Floating Point Numbers to an Integer truncates the decimal part

### 1. Split 3D Vector
Outputs the x, y, and z components of a 3D Vector as three Floating Point Numbers

### 2. Orientation to Rotation
Converts a Direction Vector to Euler Angles

### 3. Multiplication
Performs multiplication, supporting Floating Point and Integer multiplication

### 4. Division
Performs division, supporting Floating Point division and Integer division. Integer division returns the quotient result

The divisor should not be 0, otherwise it may return an illegal value

### 5. Create 3D Vector
Creates a 3D Vector from x, y, and z components

### 6.. Arccosine Function
Calculates the arccosine of the input and returns the value in Radian

### 7.. Arctangent Function
Calculates the arctangent of the input and returns the value in Radian

### 8.. Arcsine Function
Calculates the arcsine of the input and returns the value in Radian

### 9. Direction Vector to Rotation
Converts the Forward Vector and Upward Vector to Euler Angles

### 10. Radians to Degrees
Converts Radian to degrees

### 11. Get Random Number
Returns a random number in [Lower Limit, Upper Limit] (inclusive)

### 12. Addition
Adds two Floating Point Numbers or Integers

### 13. Subtraction
Subtracts two Floating Point Numbers or Integers

### 14. Degrees to Radians
Converts degrees to Radian

### 15. Absolute Value Operation
Returns the absolute value of the input

### 16. Logical NOT Operation
Performs a logical NOT operation on the input Boolean value and returns the result

### 17. Logical OR Operation
Performs a logical OR operation on the two input Boolean values and returns the result

### 18. Logical XOR Operation
Performs a logical XOR operation on the two input Boolean values and returns the result

### 19. Logical AND Operation
Performs a logical AND operation on the two input Boolean values and returns the result

### 20. Assembly List
Assembles multiple Input Parameters of the same type (up to 10) into a single List

### 21. 3D Vector Normalization
Normalizes the length of a 3D Vector and outputs the result

### 22. 3D Vector Addition
Calculates the sum of two 3D Vectors

### 23. 3D Vector Angle
Calculates the angle between two 3D Vectors and outputs the value in degrees

### 24. 3D Vector Subtraction
Calculates the difference of two 3D Vectors

### 25. 3D Vector Modulo Operation
Calculates the magnitude of the input 3D Vector

### 26. 3D Vector Dot Product
Calculates the dot product of two input 3D Vectors

### 27. 3D Vector Zoom
Scales the input 3D Vector (scalar multiplication) and outputs the result

### 28.. 3D Vector Cross Product
Calculates the cross product of two 3D Vectors

### 29. 3D Vector Rotation
Rotates the input 3D Vector by the Euler Angles specified by the rotation and returns the result

### 30. Greater Than
Returns whether the left value is greater than the right value

### 31. Greater Than or Equal To
Returns whether the left value is greater than or equal to the right value

### 32. Less Than
Returns whether the left value is less than the right value

### 33. Less Than or Equal To
Returns whether the left value is less than or equal to the right value

### 34. Cosine Function
Calculates the cosine of the input in Radian

### 35. Tangent Function
Calculates the tangent of the input in Radian

### 3. Data Type Conversion
Converts input parameter types to another type for output. For specific rules, see Basic Concepts - [Conversion Rules Between Basic Data Types]

In the client node, when converting a floating-point number to an integer, the number will be truncated.

### 1. Split 3D Vector
Outputs the x, y, and z components of a 3D Vector as three Floating Point Numbers

### 2. Orientation to Rotation
Converts a Direction Vector to Euler Angles

### 3. Multiplication
Performs multiplication, supporting Floating Point and Integer multiplication

### 4. Division
Performs division, supporting Floating Point division and Integer division. Integer division returns the quotient result

The divisor should not be 0, otherwise it may return an illegal value

### 5. Arccosine Function
Calculates the arccosine of the input and returns the value in Radian

### 6. Arctangent Function
Calculates the arctangent of the input and returns the value in Radian

### 7. Arcsine Function
Calculates the arcsine of the input and returns the value in Radian

### 8. Direction Vector to Rotation
Converts the Forward Vector and Upward Vector to Euler Angles

### 9. Radians to Degrees
Converts Radian to degrees

### 10. Get Random Number
Returns a random number in [Lower Limit, Upper Limit] (inclusive)

### 11. Addition
Adds two Floating Point Numbers or Integers

### 12. Subtraction
Subtracts two Floating Point Numbers or Integers

### 13. Degrees to Radians
Converts degrees to Radian

### 14. Absolute Value Operation
Returns the absolute value of the input

### 15. Logical NOT Operation
Performs a logical NOT operation on the input Boolean value and returns the result

### 16. Logical OR Operation
Performs a logical OR operation on the two input Boolean values and returns the result

### 17. Logical XOR Operation
Performs a logical XOR operation on the two input Boolean values and returns the result

### 18. Logical AND Operation
Performs a logical AND operation on the two input Boolean values and returns the result

### 19. 3D Vector Normalization
Normalizes the length of a 3D Vector and outputs the result

### 20. 3D Vector Addition
Calculates the sum of two 3D Vectors

### 21. 3D Vector Angle
Calculates the angle between two 3D Vectors and outputs the value in degrees

### 22. 3D Vector Subtraction
Calculates the difference of two 3D Vectors

### 23. 3D Vector Modulo Operation
Calculates the magnitude of the input 3D Vector

### 24. 3D Vector Dot Product
Calculates the dot product of two input 3D Vectors

### 25. 3D Vector Zoom
Scales the input 3D Vector (scalar multiplication) and outputs the result

### 26. 3D Vector Cross Product
Calculates the cross product of two 3D Vectors

### 27. 3D Vector Rotation
Rotates the input 3D Vector by the Euler Angles specified by the rotation and returns the result

### 28. Greater Than
Returns whether the left value is greater than the right value

### 29. Greater Than or Equal To
Returns whether the left value is greater than or equal to the right value

### 30. Less Than
Returns whether the left value is less than the right value

### 31. Less Than or Equal To
Returns whether the left value is less than or equal to the right value

### 32. Cosine Function
Calculates the cosine of the input in Radian

### 33. Tangent Function
Calculates the tangent of the input in Radian

### 34. Sine Function
Calculates the sine of the input in Radian

### 3. Data Type Conversion
Converts input parameter types to another type for output. For specific rules, see Basic Concepts - [Conversion Rules Between Basic Data Types]

In the client node, when converting a floating-point number to an integer, the number will be truncated.

### 1. Split 3D Vector
Outputs the x, y, and z components of a 3D Vector as three Floating Point Numbers

### 2. Orientation to Rotation
Converts a Direction Vector to Euler Angles

### 3. Multiplication
Performs multiplication, supporting Floating Point and Integer multiplication

### 4. Division
Performs division, supporting Floating Point division and Integer division. Integer division returns the quotient result

The divisor should not be 0, otherwise it may return an illegal value

### 5. Arccosine Function
Calculates the arccosine of the input and returns the value in radians

### 6. Arctangent Function
Calculates the arctangent of the input and returns the value in radians

### 7. Arcsine Function
Calculates the arcsine of the input and returns the value in radians

### 8. Direction Vector to Rotation
Converts the Forward Vector and Upward Vector to Euler Angles

### 9. Radians to Degrees
Converts radians to degrees

### 10. Get Random Number
Returns a random number in [Lower Limit, Upper Limit] (inclusive)

### 11. Addition
Adds two Floating Point Numbers or Integers

### 12. Subtraction
Subtracts two Floating Point Numbers or Integers

### 13. Degrees to Radians
Converts degrees to radians

### 14. Absolute Value Operation
Returns the absolute value of the input

### 15. Logical NOT Operation
Performs a logical NOT operation on the input Boolean value and returns the result

### 16. Logical OR Operation
Performs a logical OR operation on the two input Boolean values and returns the result

### 17. Logical XOR Operation
Performs a logical XOR operation on the two input Boolean values and returns the result

### 18. Logical AND Operation
Performs a logical AND operation on the two input Boolean values and returns the result

### 19. 3D Vector Normalization
Normalizes the length of a 3D Vector and outputs the result

### 20. 3D Vector Addition
Calculates the sum of two 3D Vectors

### 21. 3D Vector Angle
Calculates the angle between two 3D Vectors and outputs the value in degrees

### 22. 3D Vector Subtraction
Calculates the difference of two 3D Vectors

### 23. 3D Vector Modulo Operation
Calculates the magnitude of the input 3D Vector

### 24. 3D Vector Dot Product
Calculates the dot product of two input 3D Vectors

### 25. 3D Vector Zoom
Scales the input 3D Vector (scalar multiplication) and outputs the result

### 26. 3D Vector Cross Product
Calculates the cross product of two 3D Vectors

### 27. 3D Vector Rotation
Rotates the input 3D Vector by the Euler Angles specified by the rotation and returns the result

### 28. Greater Than
Returns whether the left value is greater than the right value

### 29. Greater Than or Equal To
Returns whether the left value is greater than or equal to the right value

### 30. Less Than
Returns whether the left value is less than the right value

### 31. Less Than or Equal To
Returns whether the left value is less than or equal to the right value

### 32. Cosine Function
Calculates the cosine of the input in radians

### 33. Tangent Function
Calculates the tangent of the input in radians

### 34. Sine Function
Calculates the sine of the input in radians

## III. Lists
### 35. Create 3D Vector
Creates a 3D Vector from x, y, and z components

### 35. Create 3D Vector
Creates a 3D Vector from x, y, and z components

### 35. Create 3D Vector
Creates a 3D Vector from x, y, and z components

### 2. Query If Faction Is Hostile
Check whether Faction 1 and Faction 2 are hostile

### 1. Get Corresponding Value From List
Return the value at the specified index in the Data List. Indexes start at 0

### 2. Get List Length
Returns the length of the list (number of elements)

### 3. Get Maximum Value From List
Applies only to Floating Point Number or Integer lists; returns the maximum value

### 4. Get Minimum Value From List
Applies only to Floating Point Number or Integer lists; returns the minimum value

### 2. Query If Faction Is Hostile
Check whether Faction 1 and Faction 2 are hostile

### 1. Get Corresponding Value From List
Return the value at the specified index in the Data List. Indexes start at 0

### 2. Get List Length
Returns the length of the list (number of elements)

### 3. Get Maximum Value From List
Applies only to Floating Point Number or Integer lists; returns the maximum value

### 4. Get Minimum Value From List
Applies only to Floating Point Number or Integer lists; returns the minimum value

## IV. Structure
### 1. Assembly List
Assembles multiple Input Parameters of the same type (up to 10) into a single List

### 1. Split Structure
Get all parameters of the specified structure.

### 1. Assembly List
Assembles multiple Input Parameters of the same type (up to 10) into a single List

### 1. Split Structure
Get all parameters of the specified structure.

### 1. Assembly List
Assembles multiple Input Parameters of the same type (up to 10) into a single List

### 1. Split Structure
Get all parameters of the specified structure.

## V. Dictionary
### 2. Assemble Structure
Combine multiple parameters into a value of the structure type.

### 1. Create Dictionary
Create key-value pairs according to the order of the input keys and values list.

This node will create a dictionary based on the shorter of the two lists, and any excess elements will be truncated.

If there are duplicate values in the keys list, the creation will fail, and an empty dictionary will be returned.

### 2. Assemble Structure
Combine multiple parameters into a value of the structure type.

### 1. Create Dictionary
Create key-value pairs according to the order of the input keys and values list.

This node will create a dictionary based on the shorter of the two lists, and any excess elements will be truncated.

If there are duplicate values in the keys list, the creation will fail, and an empty dictionary will be returned.

### 2. Assemble Structure
Combine multiple parameters into a value of the structure type.

### 1. Create Dictionary
Create key-value pairs according to the order of the input keys and values list.

This node will create a dictionary based on the shorter of the two lists, and any excess elements will be truncated.

If there are duplicate values in the keys list, the creation will fail, and an empty dictionary will be returned.

### 2. Assembly Dictionary
Combine up to 50 key-value pairs into a dictionary.

## III. Dictionary
### 36. Sine Function
Calculates the sine of the input in radians

### 1. Create Dictionary
Creates Key-Value Pairs sequentially from the input key and value lists.

This node builds the Dictionary using the shorter of the key and value lists; extra items are truncated

If duplicate keys are found in the key list, creation fails and returns an empty Dictionary

### 36. Sine Function
Calculates the sine of the input in Radian

### 1. Create Dictionary
Creates Key-Value Pairs sequentially from the input key and value lists.

This node builds the Dictionary using the shorter of the key and value lists; extra items are truncated

If duplicate keys are found in the key list, creation fails and returns an empty Dictionary

## IV. Structures
### 2. Assembly Dictionary
Combines up to 50 Key-Value Pairs into one Dictionary

### 1. Split Structure
Returns all parameters of the specified Structure

### 2. Assembly Dictionary
Combines up to 50 Key-Value Pairs into one Dictionary

### 1. Split Structure
Returns all parameters of the specified Structure

## Other
### 1. Node Graph Starts
Start event of the Skill Node Graph

Used to customize the Skill logic after this Node; subsequent Nodes execute in the order defined by the Node Graph

### 1. Execute Only by Sequence
Start Event of the Creation Status Node Graph

The Creation Status Node Graph starts with an [**Execute Only by Sequence]** node. Each output pin connects to an Execution Node, allowing different actions to run as needed. If the entry conditions for the previous action are not met, the graph will enter the *Failed Execution* first. If the conditions are still not met, it will try the action on the next pin

The Creation Status Node Graph runs continuously. If a higher-priority behavior meets its conditions, the Complex Creation immediately switches to execute that behavior

If the conditions are not met, the Complex Creation may not execute any actions

Example: At runtime, Branch 1 checks Node A first. If Node A meets its conditions and executes successfully, Nodes B and C will not execute. If Node A does not meet its conditions, Branch 1 continues by checking Node B. If neither Node A nor Node B meets its conditions, Branch 2 then checks whether Node C meets its conditions

If the Creation is executing the behavior in Node C, but Node A's execution condition is met, the Complex Creation will immediately switch to executing the behavior in Node A

### 1. Execute Only by Sequence
Start Event for the Creation Status Decision Node Graph

The Creation Status Decision Node Graph starts with an [**Execute Only by Sequence)]** node. Each output pin connects to a **[Switch to self execution status]** node, so you can execute different behaviors as needed. If the entry conditions for the previous state are not met, it will enter the *Failed Execution* first. If the conditions are still not met, it will try the state on the next pin

The Creation Status Decision Node Graph runs continuously. When a state earlier in the sequence meets its conditions, the Complex Creation immediately switches execution state and executes the Status Node Graphs in that preceding order

If no conditions are met, the Complex Creation may not execute any Status Node Graph

Example: At runtime, Branch 1 checks Node A first. If Node A meets its conditions and executes successfully, Nodes B and C will not execute. If Node A does not meet its conditions, Branch 1 continues by checking Node B. If neither Node A nor Node B meets its conditions, Branch 2 then checks whether Node C meets its conditions

If the Creation Status Node Graph in Node C is currently running, but Node A's execution conditions are met, the Complex Creation will immediately switch to the Creation Status Node Graph in Node A

### 1. Node Graph Begins
Start event of the Skill Node Graph

Used to customize the Skill logic after this Node; subsequent Nodes execute in the order defined by the Node Graph

### 2. Node Graph End (Boolean)

### 3. Node Graph End (Integer)

## I. List Related
### 1. Get Corresponding Value From List
Returns the value at the specified ID in the List. IDs start at 0

### 2. Get List Length
Returns the length of the list (number of elements)

### 3. Get Maximum Value From List
Applies only to Floating Point Number or Integer lists; returns the maximum value

### 4. Get Minimum Value From List
Applies only to Floating Point Number or Integer lists; returns the minimum value

### 5. Get Ray Filter Type List
Assembles the required Ray Filter types into a List. Available filters include Hurtbox, Scene, and Object Self-Collision

### 6. Get Entity Type List
Assembles the required Entity types into a List. Types include Stages, Objects, Players, Characters, and Creations

### 6. Query Dictionary Value by Key
Query the corresponding Value in the Dictionary by Key. If the Key does not exist, returns the type's default value

### 1. Get Corresponding Value From List
Returns the value at the specified ID in the List. IDs start at 0

### 2. Get List Length
Returns the length of the list (number of elements)

### 3. Get Maximum Value From List
Applies only to Floating Point Number or Integer lists; returns the maximum value

### 4. Get Minimum Value From List
Applies only to Floating Point Number or Integer lists; returns the minimum value

### 5. Get Ray Filter Type List
Assembles the required Ray Filter types into a List. Available filters include Hurtbox, Scene, and Object Self-Collision

### 6. Get Entity Type List
Assembles the required Entity types into a List. Types include Stages, Objects, Players, Characters, and Creations

## II. Custom Variables
### 7. List Includes This Value
Returns whether the list contains the specified value

### 7. List Includes This Value
Returns whether the list contains the specified value

## III. Preset Status
### 1. Get Custom Variable
Returns the value of the specified Custom Variable from the Target Entity

If the variable does not exist, returns the type's default value

### 1. Get Custom Variable
Returns the value of the specified Custom Variable from the Target Entity

If the variable does not exist, returns the type's default value

## IV. Entity Related
### 1. Get Preset Status
Returns the Preset Status value of the specified Entity. Returns 0 if the Entity does not have the specified Preset Status

### 1. Query If Entity Is on the Field
Searches whether the specified Entity is present

Note that Character Entities are still considered present even when Downed

### 2. Get Unit Attack Target
Returns the Target Entity that the Unit Entity is currently attacking

### 3. Get Target Attachment Point Location
Returns the Attachment Point Location corresponding to the specified Attachment Point Name on the Target Entity

### 4. Get Target Attachment Point Rotation
Returns the Attachment Point Rotation corresponding to the specified Attachment Point Name on the Target Entity

### 5. Get Target Entity
Returns the Target Entity. The meaning of this output varies depending on the functional module that references the Filter Node Graph

### 6. Get Entity‘s Type
Returns the type of the specified Entity

### 7. Get Entity Location
Returns the Location of the specified Entity

### 8. Get Entity Rotation
Returns the Rotation of the specified Entity in Euler Angles

### 9. Get Self Entity
Returns the Entity associated with this Node Graph

### 10. Filter Entity List Within Square Range
Filters Entities within a square range according to specified rules and a maximum count, and returns a list of Entities that meet the conditions

### 11. Filter Entity List Within Spherical Range
Filters Entities within a spherical range according to specific rules and a maximum count, and returns a list of Entities that meet the conditions

### 12. Query Entity by GUID
Searches for an Entity by GUID

### 1. Get Preset Status
Returns the Preset Status value of the specified Entity. Returns 0 if the Entity does not have the specified Preset Status

### 1. Check the Preset Status Value of the Complex Creation
Query the Preset Status Value of the Target Creation under the corresponding Preset Status index

### 2. Query If Entity Is on the Field
Check whether the specified Entity is present

Note that Character Entities are still considered present even when Downed

### 3. Get Unit Attack Target
Returns the Target Entity that the Unit Entity is currently attacking

### 4. Get Target Attachment Point Location
Returns the Location of the specified Attachment Point on the Target Entity.

### 5. Get Target Entity
Returns the Target Entity. The meaning of this output varies depending on the functional module that references the Filter Node Graph

### 6. Get Entity's Type
Returns the type of the specified Entity

### 7. Get Entity Location
Returns the Location of the specified Entity

### 8. Get Entity Rotation
Returns the Rotation of the specified Entity in Euler Angles

### 9. Get Self Entity
Returns the Entity associated with this Node Graph

### 10. Filter Entity List Within Square Range
Filters Entities within a square range according to specified rules and a maximum count, and returns a list of Entities that meet the conditions

### 11. Filter Entity List Within Spherical Range
Filters Entities within a spherical range according to specific rules and a maximum count, and returns a list of Entities that meet the conditions

## V. Faction Related
### 13. Check the Preset Status Value of the Complex Creation
Query the preset state value of the target creation corresponding to the preset state index.

### 1. Query Entity Faction
Searches Target Entity's Faction

### 12. Query Entity by GUID
Search for an Entity by GUID

### 1. Query Entity Faction
Search for Target Entity's Faction

## VI. Player and Character Related
### 2. Query If Faction Is Hostile
Searches whether Faction 1 and Faction 2 are hostile

### 1. Query If Self Is in Combat
Searches whether the Entity associated with this Node Graph has entered battle

### 2. Get Current Character
Returns the Character Entity currently controlled by this Player's client

### 3. Get Player Entity to Which the Character Belongs
Returns the Player Entity that owns the Character Entity

### 4. Get List of Player Entities on the Field
Returns a list of all Player Entities present in the scene

### 5. Get Character Entity of Specified Player
Returns the Character Entity of the specified Player Entity

### 6. Query GUID by Entity
Searches for the GUID of the specified Entity

### 7. Get Player Client Input Device Type
Returns the Player's local input device type, as determined by the Interface mapping method

### 8. Get Player Movement Input
Returns the Input Direction and Input Strength of the current client player's movement.

### 9. Query Skill Variable Value
Searches for the corresponding variable value based on the Skill Variable Config ID.

### 10. Get Current Key Behavior
Returns all Key Behavior IDs and their corresponding entry times from the current Key Behavior Log Panel.

### 11. Get Current Key Behavior (High Precision)
Returns all Key Behavior IDs and their corresponding entry times from the current Key Behavior Log Panel. Due to floating-point precision issues, use this node if you require greater granularity for the entry times.

### 12. Get Current Client Time
Returns the current client time.

### 13. Get Current Client Time (High Precision)
Returns the current client time. Due to floating-point precision issues, use this node if you requite greater granularity for the client time.

### 14. Query Whether Player Is Currently in Voice Chat
Returns "Yes" when microphone input is detected from this player's client.

Note: This node only takes effect during multiplayer games (multiplayer test play, actual multiplayer play). It will not work in single-player games (single-player test play, actual single-player play).

### 15. Get Skill Config ID by Skill Instance ID
Returns the corresponding Skill Config ID based on the Skill Instance ID provided.

### 16. Query Skill Instance List by Specified Slot
Searches for all skill instances in the slot specified.

### 17. Query Active Skill Instance List of Specified Slot
Returns the skill instance(s) currently in the foreground for the slot specified.

### 2. Query If Faction Is Hostile
Check whether Faction 1 and Faction 2 are hostile

### 1. Query If Self Is in Combat
Check whether the Entity associated with this Node Graph has entered battle

### 2. Get Player Client Input Device Type
Returns the Player's local input device type, as determined by the Interface mapping method

### 3. Get Current Character
Returns the Character Entity currently controlled by this Player's client

### 4. Get Player Entity to Which the Character Belongs
Returns the Player Entity that owns the Character Entity

### 5. Get List of Player Entities on the Field
Returns a list of all Player Entities present in the scene

### 6. Get Character Entity of Specified Player
Returns the Character Entity of the specified Player Entity

### 7. Query GUID by Entity
Search for the GUID of the specified Entity

### 8. Get Active Character of Specified Player
Available only in Classic Mode. Returns the on-field character in the player's team

### 9. Check Classic Mode Character IDs
Only available in the Classic Mode. Query the character ID of the Target Character. Check the appendix to see which Character it corresponds toClassic Mode Character ID List

### 10.** **Get Player's Character List
Returns a list of characters in the player's team. Available only in Classic Mode.

### 11. Get Player Movement Input
Returns the Input Direction and Input Strength of the player's movement on the current client.

### 12. Query Skill Variable Value
Queries the corresponding Variable Value based on the Skill Variable Config ID.

### 13. Get Current Key Behavior
Returns all Key Behavior IDs on the current Key Behavior Log Panel and their corresponding entry times.

### 14. Get Current Key Behavior (High Precision)
Returns all Key Behavior IDs on the current Key Behavior Log Panel and their corresponding entry times. Due to floating-point precision issues, use this node if you require greater granularity for the entry times.

### 15. Get Current Client Time
Returns the current client time.

### 16. Get Current Client Time (High Precision)
Returns the current client time. Due to floating-point precision issues, use this node if you need greater granularity for the client time.

### 17. Query Whether Player Is Currently in Voice Chat
Returns "Yes" when microphone input is detected from this player's client.

Note: This node only takes effect in multiplayer games (multiplayer test play, actual multiplayer play). It will not work in single-player games (single-player test play, actual single-player play).

### 18. Get Skill Config ID by Skill Instance ID
Returns the corresponding Skill Config ID based on the Skill Instance ID provided

### 19. Query Skill Instance List by Specified Slot
Returns a list of all skill instances in the slot specified.

### 20. Query Active Skill Instance List of Specified Slot
Gets the skill instance currently in the foreground for the slot specified.

## VII. Unit Tags
### 18. Query Skill Instance ID by Skill Slot and Skill Config ID
Returns the corresponding skill instance based on the skill slot and Skill Config ID provided.

### 1. Get Entity List by Unit Tag
Returns a list of all Entities in the scene that carry this Unit Tag

## VIII. General
### 2. Get Entity's Unit Tag List
Returns a list of all Unit Tags carried by the Target Entity

### 2. Get Entity's Unit Tag List
Returns a list of all Unit Tags carried by the Target Entity

## IX. Custom Aggro
### 1. Get Local Variable
Returns the value of a specific local variable

### 1. Query if Specified Entity is in Combat
Available only for Custom Aggro Mode

Searches whether the specified Entity has entered battle

### 2. Get the Aggro List of the Specified Entity
Available only for Custom Aggro Mode

Gets Specific Entity's Aggro List

### 1. Get Local Variable
Returns the value of a specific local variable

### 1. Query If Specified Entity Is in Combat
Available only in Custom Aggro Mode

Check whether the specified Entity has entered battle

### 2. Get the Aggro List of the Specified Entity
Available only in Custom Aggro Mode

Get Specified Entity's Aggro List

## X. Triggers
### 3. Get the Aggro Target of the Specified Entity
Available only for Custom Aggro Mode

Gets Aggro Target of Specific Entity

### 3. Get the Aggro Target of the Specified Entity
Available only in Custom Aggro Mode

Get Aggro Target of Specified Entity

## XI. Ray
### 1. Get All Entities Within the Collision Trigger
Returns all Entities within the Collision Trigger corresponding to a specific ID in the Collision Trigger Component on the Target Entity

### 1. Get All Entities Within the Collision Trigger
Returns all Entities within the Collision Trigger corresponding to a specific ID in the Collision Trigger Component on the Target Entity

## XII. Scanning
### 1. Get Ray Detection Result
Returns the first Target or On-Hit Location that meets the Filter criteria, ordered from nearest to farthest along the ray

### 1.** Get All Valid Entities That Are Scannable by Scan Component
Returns all Units carrying a Scan Component whose Filter returns True, regardless of the Unit's scannable status

### 2.** Get Entity Currently Scanned by Scan Component
Returns Entities currently detected by the Scan Component; these are Entities in the Active State

### 3.** Get Entity's Current Active Scan Tags
Returns the Target Entity's Current Active Scan Tags

## XIII. Dictionary
### 4. Get Entity's Scan Status
Get Entity Scan Status

### 1. Query If Dictionary Contains Specific Key
Query if the specified dictionary contains a specific key

### 2. Query If Dictionary Contains Specific Value
Query if the specified dictionary contains a specific value

### 3. Check Dictionary Length
Query the number of key-value pairs in a dictionary

### 4. Get List of Keys From Dictionary
Get a list of all keys in the dictionary. Since the key-value pairs in the dictionary are unordered, the list of keys retrieved may not be in the order they were inserted.

### 5. Get List of Values From Dictionary
Get a list of all values in the dictionary. Since the key-value pairs in the dictionary are unordered, the list of values retrieved may not be in the order they were inserted.

## XIV. Unit Status
### 6. Query Dictionary Value by Key
Query the value corresponding to a key in the dictionary, and return the default value of the type if the key does not exist.

## II. Faction
### 27. Get Self Preset Status Value
Obtain the Preset Status Value at the specified Preset Status index for this Entity. If the Entity does not have the specified Preset Status index, return 0

### 1. Check Entity Faction
Search for Target Entity's Faction

### 27. Get Self Preset Status Value
Obtain the Preset Status Value at the specified Preset Status index for this Entity. If the Entity does not have the specified Preset Status index, return 0

### 1. Check Entity Faction
Search for Target Entity's Faction

## IV. Dictionary
### 5. List Includes This Value
Check whether the specified list contains a specific value

### 1. Query If Dictionary Contains Specific Key
Check whether the specified Dictionary contains the specified Key

### 2. Query If Dictionary Contains Specific Value
Check whether the specified Dictionary contains the specified Value

### 3. Query Dictionary Length
Query the number of Key-Value Pairs in the Dictionary

### 4. Get List of Keys From Dictionary
Returns a list of all Keys in the Dictionary. Because Key-Value Pairs are unordered, the Keys may not be returned in insertion order

### 5. Query List of Values From Dictionary
Returns a list of all Values in the Dictionary. Because Key-Value Pairs are unordered, the Values may not be returned in insertion order

### 5. List Includes This Value
Check whether the specified list contains a specific value

### 1. Query If Dictionary Contains Specific Key
Check whether the specified Dictionary contains the specified Key

### 2. Query If Dictionary Contains Specific Value
Check whether the specified Dictionary contains the specified Value

### 3. Query Dictionary Length
Query the number of Key-Value Pairs in the Dictionary

### 4. Get List of Keys From Dictionary
Returns a list of all Keys in the Dictionary. Because Key-Value Pairs are unordered, the Keys may not be returned in insertion order

### 5. Query List of Values From Dictionary
Returns a list of all Values in the Dictionary. Because Key-Value Pairs are unordered, the Values may not be returned in insertion order

## VII. Attachment Points
### 21. Query Skill Instance ID by Skill Slot and Skill Config ID
Returns the corresponding skill instance based on the skill slot and Skill Config ID provided.

## VIII. Triggers
### 1. Get Target Attachment Point Rotation
Returns the Rotation of the specified Attachment Point on the Target Entity.

## IX. Rays
### 1. Get All Entities Within the Collision Trigger
Returns all Entities within the Collision Trigger corresponding to a specific ID in the Collision Trigger Component on the Target Entity

## X. Scanning
### 1. Get Ray Detection Result
Returns the first Target or On-Hit Location that meets the Filter criteria, ordered from nearest to farthest along the ray


Returns all Units carrying a Scan Component whose Filter returns True, regardless of the Unit's scannable status


Returns Entities currently detected by the Scan Component; these are Entities in the Active State


Returns the Target Entity's Current Active Scan Tags

### 4. Get Entity's Scan Status
Get Entity Scan Status

### 1. Query If Dictionary Contains Specific Key
Check whether the specified Dictionary contains the specified Key

### 2. Query If Dictionary Contains Specific Value
Check whether the specified Dictionary contains the specified Value

### 3. Check Dictionary Length
Query the number of Key-Value Pairs in the Dictionary

### 4. Get List of Keys From Dictionary
Returns a list of all Keys in the Dictionary. Because Key-Value Pairs are unordered, the Keys may not be returned in insertion order

### 5. Get List of Values From Dictionary
Returns a list of all Values in the Dictionary. Because Key-Value Pairs are unordered, the Values may not be returned in insertion order

### 6. Query Dictionary Value by Key
Query the corresponding Value in the Dictionary by Key. If the Key does not exist, returns the type's default value

## II. List Operations
### 2. Query Skill Variable Value
Returns the corresponding variable value based on Skill Variable Config ID

### 1. Get Corresponding Value From List
Returns the value at the specified ID in the List. IDs start at 0

### 2. Get List Length
Returns the length of the list (number of elements)

### 3. Get Maximum Value From List
Applies only to Floating Point Number or Integer lists; returns the maximum value

### 4. Get Minimum Value From List
Applies only to Floating Point Number or Integer lists; returns the minimum value

### 5. Get Ray Filter Type List
Assembles the required Ray Filter types into a List. Available filters include Hurtbox, Scene, and Object Self-Collision

### 6. Get Entity Type List
Assembles the required Entity types into a List. Types include Stages, Objects, Players, Characters, and Creations

## III. Custom Variables
### 7. List Includes This Value
Returns whether the list contains the specified value

## IV. Preset Status
### 1. Get Custom Variable
Returns the value of the specified Custom Variable from the Target Entity

If the variable does not exist, returns the type's default value

## V. Entity-Related
### 1. Get Preset Status
Returns the Preset Status value of the specified Entity. Returns 0 if the Entity does not have the specified Preset Status

### 1. Check the preset status value of the complex creation
Query the Preset Status Value of the Target Creation under the corresponding Preset Status index

### 2. Query if Entity Is on the Field
Check whether the specified Entity is present

Note that Character Entities are still considered present even when Downed

### 3. Get Unit Attack Target
Returns the Target Entity that the Unit Entity is currently attacking

### 4. Get Target Attachment Point Location
Returns the Location of the specified Attachment Point on the Target Entity.

### 5. Get Target Attachment Point Rotation
Returns the Rotation of the specified Attachment Point on the Target Entity.

### 6. Get Entity's Type
Returns the type of the specified Entity

### 7. Get Entity Location
Returns the Location of the specified Entity

### 8. Get Entity Rotation
Returns the Rotation of the specified Entity in Euler Angles

### 9. Get Creation's Current Target
Return to the specified Creation's current target

### 10. Get Self Entity
Returns the Entity associated with this Node Graph

### 11. Get Sub-Entity List
Return to the Target Entity's Sub-Entity List

### 12. Filter Entity List Within Square Range
Filters Entities within a square range according to specified rules and a maximum count, and returns a list of Entities that meet the conditions

### 13. Filter Entity List Within Spherical Range
Filters Entities within a spherical range according to specific rules and a maximum count, and returns a list of Entities that meet the conditions

### 14. Query Entity by GUID
Search for an Entity by GUID

### 15. Get Player Entity to Which the Character Belongs
Returns the Player Entity that owns the Character Entity

### 16. Get List of Player Entities on the Field
Returns a list of all Player Entities present in the scene

### 17. Get Active Character of Specified Player
Available only in the Classic Mode. Obtains the on-field character in the player's team

### 18. Get Player's Character List
Available in the Classic Mode only. Returns a list of all characters in the Player's team

### 19. Query GUID by Entity
Returns the GUID of the specified Entity

## VI. Faction-Related
### 20. Check Class Mode Character ID
Available in Classic Mode only. Returns the Character ID of the Target Character, and can be used to look up the corresponding character in the Appendix Classic Mode Character IDs

### 1. Query Entity Faction
Search for Target Entity's Faction

## VII. Tags
### 2. Query If Faction Is Hostile
Check whether Faction 1 and Faction 2 are hostile

### 1. Get Entity List by Unit Tag
Returns a list of all Entities in the scene that carry this Unit Tag

## XII. Dictionary
### 1. Get Ray Detection Result
Returns the first Target or On-Hit Location that meets the Filter criteria, ordered from nearest to farthest along the ray

### 1. Query If Dictionary Contains Specific Key
Check whether the specified Dictionary contains the specified Key

### 2. Query If Dictionary Contains Specific Value
Check whether the specified Dictionary contains the specified Value

### 3. Check Dictionary Length
Query the number of Key-Value Pairs in the Dictionary

### 4. Get List of Keys From Dictionary
Returns a list of all Keys in the Dictionary. Because Key-Value Pairs are unordered, the Keys may not be returned in insertion order

### 5. Get List of Values From Dictionary
Returns a list of all Values in the Dictionary. Because Key-Value Pairs are unordered, the Values may not be returned in insertion order

### 6. Query Dictionary Value by Key
Query the corresponding Value in the Dictionary by Key. If the Key does not exist, returns the type's default value

### 1. Whether the Entity Has the Specified Unit Status
Check whether the Target Entity has the specified Unit Status

