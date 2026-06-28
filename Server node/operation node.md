# Operation Nodes (Node Phép Toán)

# I. General (Cài đặt chung)

## **1. Enumerations Equal (Bằng nhau kiểu Liệt kê)**

![](./operation node_files/10e51bd2-3efb-44e4-87a8-4c3013eb327d.png)

**Node Functions (Chức năng Node)**

Sau khi xác nhận kiểu Liệt kê (Enumeration), xác định xem hai giá trị đầu vào có bằng nhau hay không.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Enumeration 1 (Liệt kê 1) | Generic (Chung) |  |
| Input Parameter (Đầu vào) | Enumeration 2 (Liệt kê 2) | Generic (Chung) |  |
| Output Parameter (Đầu ra) | Result (Kết quả) | Boolean (Logic) | Trả về True nếu bằng nhau, False nếu không bằng nhau |

## **2. Assembly List (Lắp ráp danh sách)**

![](./operation node_files/a31c67bb-c8a9-443e-9fee-b4deaef799ae.png)

**Node Functions (Chức năng Node)**

Tập hợp nhiều Tham số Đầu vào (Input Parameters) cùng kiểu (lên đến 100) vào một Danh sách (List) duy nhất.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | 0~99 | Generic (Chung) | Tập hợp tối đa 100 tham số thành một danh sách |
| Output Parameter (Đầu ra) | List (Danh sách) | Generic (Chung) | Danh sách đã được lắp ráp |

## **3. Equal (Bằng nhau)**

![](./operation node_files/e64d3d4c-fb18-4611-bd8a-6090453b1e78.png)

**Node Functions (Chức năng Node)**

Xác định xem hai đầu vào có bằng nhau hay không.

Một số Loại tham số (Parameter Types) có quy tắc so sánh đặc biệt:

Số thực (Floating Point Numbers): Các số thực được so sánh bằng phương pháp bằng nhau gần đúng (approximate equality). Khi hiệu giữa hai số thực nhỏ hơn một giá trị cực kỳ nhỏ, hai số đó được coi là bằng nhau. Ví dụ: 2.0000001 và 2.0 được coi là bằng nhau.

Vecto 3D (3D Vector): Các thành phần x, y và z của một Vecto 3D được so sánh bằng phương pháp bằng nhau gần đúng của số thực.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Input 1 (Đầu vào 1) | Generic (Chung) |  |
| Input Parameter (Đầu vào) | Input 2 (Đầu vào 2) | Generic (Chung) |  |
| Output Parameter (Đầu ra) | Result (Kết quả) | Boolean (Logic) | Trả về True nếu bằng nhau, False nếu không bằng nhau |

## **4. Data Type Conversion (Chuyển đổi Kiểu dữ liệu)**

![](./operation node_files/baf41214-696f-4332-80d7-f94e2177f51a.png)

**Node Functions (Chức năng Node)**

Chuyển đổi các kiểu tham số đầu vào sang kiểu khác để làm đầu ra. Để biết các quy tắc cụ thể, hãy xem Basic Concepts - [Conversion Rules Between Basic Data Types] (Khái niệm Cơ bản - Quy tắc Chuyển đổi giữa Các kiểu Dữ liệu Cơ bản).

Số thực sẽ được làm tròn thành số nguyên khi chuyển đổi.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Input (Đầu vào) | Generic (Chung) |  |
| Output Parameter (Đầu ra) | Output (Đầu ra) | Generic (Chung) |  |

# II. Math (Toán học)

## **1. Split 3D Vector (Chia tách Vecto 3D)**

![](./operation node_files/8a4e18c5-9b47-4db9-b27a-d057e0edfc69.png)

**Node Functions (Chức năng Node)**

Xuất ra các thành phần x, y và z của một Vecto 3D dưới dạng ba Số thực.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | 3D Vector (Vecto 3D) | 3D Vector |  |
| Output Parameter (Đầu ra) | X-Component (Thành phần X) | Floating Point Numbers (Số thực) |  |
| Output Parameter (Đầu ra) | Y-Component (Thành phần Y) | Floating Point Numbers (Số thực) |  |
| Output Parameter (Đầu ra) | Z-Component (Thành phần Z) | Floating Point Numbers (Số thực) |  |

## **2. Multiplication (Phép nhân)**

![](./operation node_files/50365d5a-5959-471a-aad5-b0e11e7459ee.png)

**Node Functions (Chức năng Node)**

Thực hiện phép nhân, hỗ trợ nhân Số thực và Số nguyên.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) |  | Generic (Chung) |  |
| Input Parameter (Đầu vào) |  | Generic (Chung) |  |
| Output Parameter (Đầu ra) | Result (Kết quả) | Generic (Chung) |  |

## **3. Division (Phép chia)**

![]()

**Node Functions (Chức năng Node)**
# **3. Division Operation (Phép chia)**

**Node Functions (Chức năng Node)**

Thực hiện phép chia, hỗ trợ chia số thực và chia số nguyên. Phép chia số nguyên trả về kết quả phần thương.

**Lưu ý**:
- Mẫu số (divisor) không nên bằng 0; nếu bằng 0 có thể trả về giá trị bất hợp pháp.
- Khi mẫu số bằng 0, kết quả sẽ trả về 0.
- Giá trị `-2147483648` chia cho `-1` sẽ trả về 0.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) |  | Generic (Chung) |  |
| Input Parameter (Đầu vào) |  | Generic (Chung) |  |
| Output Parameter (Đầu ra) | Result (Kết quả) | Generic (Chung) |  |

## **4. Create 3D Vector (Tạo Vector 3D)**

![]()

**Node Functions (Chức năng Node)**

Tạo một Vector 3D từ các thành phần x, y và z.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | X-Component (Thành phần X) | Floating Point Numbers (Số thực) |  |
| Input Parameter (Đầu vào) | Y-Component (Thành phần Y) | Floating Point Numbers (Số thực) |  |
| Input Parameter (Đầu vào) | Z-Component (Thành phần Z) | Floating Point Numbers (Số thực) |  |
| Output Parameter (Đầu ra) | 3D Vector (Vector 3D) | 3D Vector (Vector 3D) |  |
## **5. Logarithm Operation (Phép logarit)**

![]()

**Node Functions (Chức năng Node)**

Tính logarit của đối số với cơ số được chỉ định.

**Lưu ý**: Cơ số không được âm hoặc bằng 1, và đối số không được âm; nếu không sẽ sinh ra giá trị bất hợp pháp.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Real Number (Số thực) | Floating Point Numbers (Số thực) |  |
| Input Parameter (Đầu vào) | Base (Cơ số) | Floating Point Numbers (Số thực) |  |
| Output Parameter (Đầu ra) | Result (Kết quả) | Floating Point Numbers (Số thực) |  |
## **6. Arccosine Function (Hàm arccosine)**

![]()

**Node Functions (Chức năng Node)**

Tính arccosine của đầu vào và trả về giá trị theo radian.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Input (Đầu vào) | Floating Point Numbers (Số thực) |  |
| Output Parameter (Đầu ra) | Radian (Radian) | Floating Point Numbers (Số thực) |  |

## **7. Arctangent Function (Hàm arctangent)**

![]()

**Node Functions (Chức năng Node)**

Tính arctangent của đầu vào và trả về giá trị theo radian.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Input (Đầu vào) | Floating Point Numbers (Số thực) |  |
| Output Parameter (Đầu ra) | Radian (Radian) | Floating Point Numbers (Số thực) |  |

## **8. Arcsine Function (Hàm arcsine)**

![]()

**Node Functions (Chức năng Node)**

Tính arcsine của đầu vào và trả về giá trị theo radian.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Input (Đầu vào) | Floating Point Numbers (Số thực) |  |
| Output Parameter (Đầu ra) | Radian (Radian) | Floating Point Numbers (Số thực) |  |

## **9. Range Limiting Operation (Giới hạn phạm vi)**

![]()

**Node Functions (Chức năng Node)**

Giới hạn giá trị đầu vào vào khoảng `[lower limit, upper limit]` (cả hai giới hạn đều bao gồm). Nếu giá trị đầu vào nằm trong khoảng, trả về giá trị gốc; nếu thấp hơn giới hạn dưới, trả về giới hạn dưới; nếu cao hơn giới hạn trên, trả về giới hạn trên. Nếu giới hạn dưới lớn hơn giới hạn trên, coi đầu vào không hợp lệ và trả về giá trị bất hợp pháp.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Input (Đầu vào) | Generic (Chung) |  |
| Input Parameter (Đầu vào) | Lower Limit (Giới hạn dưới) | Generic (Chung) |  |
| Input Parameter (Đầu vào) | Upper Limit (Giới hạn trên) | Generic (Chung) |  |
| Output Parameter (Đầu ra) | Result (Kết quả) | Generic (Chung) |  |
| Input Parameter | Upper Limit | Generic |  |
| Output Parameter | Result | Generic |  |

## **10. Direction Vector to Rotation**

![]()

**Chức năng Node**

Converts the Forward Vector and Upward Vector to Euler Angles

Example: For a Character, suppose it has an initial orientation in 3D space. To rotate the character to a desired orientation: The Forward Vector indicates the direction we want the Character's nose to face. The Upward Vector indicates the direction we want the Character's head to point. Output: A 3D Euler rotation vector representing the rotation the Character must undergo to move from its initial orientation to the specified target orientation.

Note: Ensure the Forward and Upward Vectors are normalized. Using non-normalized vectors can produce unintended scaling and inaccurate rotation results.

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Forward Vector | 3D Vector | Represents the desired Orientation of the Unit |
| Input Parameter | Upward Vector | 3D Vector | Defines the Unit's Up direction (used to determine the rotation angle). Default is the positive Y-axis of the World Coordinate System |
| Output Parameter | Rotate | 3D Vector | Returns Euler Angles, where each component represents:  X – Pitch: Rotation around the local X-axis (right). Controls looking up and down.  Y – Yaw: Rotation around the local Y-axis (up). Controls turning left and right.  Z – Roll: Rotation around the local Z-axis (forward). Controls tilting the object side to side. |

## **11. Chuyển đổi thời gian đã định dạng sang dấu thời gian**

![]()

**Chức năng Node**

Chuyển đổi thời gian đã định dạng sang dấu thời gian

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Year | Integer |  |
| Input Parameter | Month | Integer |  |
| Input Parameter | Day | Integer |  |
| Input Parameter | Hour | Integer |  |
| Input Parameter | Minute | Integer |  |
| Input Parameter | Second | Integer |  |
| Output Parameter | Timestamp | Integer |  |

## **12. Chuyển đổi dấu thời gian sang thời gian đã định dạng**

![]()

**Chức năng Node**

Chuyển đổi dấu thời gian sang thời gian đã định dạng

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Timestamp | Integer |  |
| Output Parameter | Year | Integer |  |
| Output Parameter | Month | Integer |  |
| Output Parameter | Day | Integer |  |
| Output Parameter | Hour | Integer |  |
| Output Parameter | Minute | Integer |  |
| Output Parameter | Second | Integer |  |

## **13. Tính ngày trong tuần từ dấu thời gian**

![]()

**Chức năng Node**

Chuyển đổi dấu thời gian sang ngày trong tuần

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Timestamp | Integer |  |
| Output Parameter | Weekday | Integer |  |

## **14. Radian sang Độ**

![]()

**Chức năng Node**

Chuyển đổi radian sang độ

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Radian Value | Floating Point Numbers |  |
| Output Parameter | Angle Value | Floating Point Numbers |  |

## **15. Phép cộng**

![]()

**Chức năng Node**

Cộng hai số thực hoặc số nguyên

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter |  | Generic |  |
| Input Parameter |  | Generic |  |
| Output Parameter | Result | Generic |  |

## **16. Phép trừ**

![]()

**Chức năng Node**

Trừ hai số thực hoặc số nguyên

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter |  | Generic |  |
| Input Parameter |  | Generic |  |
| Output Parameter | Result | Generic |  |

## **17. Độ sang Radian**

![]()

**Chức năng Node**

Chuyển đổi độ sang radian

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Angle Value | Floating Point Numbers |  |
| Output Parameter | Radian Value | Floating Point Numbers |  |

## **18. Lấy Giá trị Lớn hơn**

![]()

**Chức năng Node**

Trả về giá trị lớn hơn trong hai đầu vào

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input 1 | Generic |  |
| Input Parameter | Input 2 | Generic |  |
| Output Parameter | Larger Value | Generic |  |

## **19. Lấy Giá trị Nhỏ hơn**

![]()

**Chức năng Node**

Trả về giá trị nhỏ hơn trong hai đầu vào

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input 1 | Generic |  |
| Input Parameter | Input 2 | Generic |  |
| Output Parameter | Smaller Value | Generic |  |

## **20. Phép lấy Giá trị Tuyệt đối**

![]()

**Chức năng Node**

Trả về giá trị tuyệt đối của đầu vào

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input | Generic |  |
| Output Parameter | Result | Generic |  |

## **21. Khoảng cách giữa Hai Điểm Tọa độ**

![]()

**Chức năng Node**

Tính khoảng cách Euclid giữa hai tọa độ

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Coordinate Point 1 | 3D Vector |  |
| Input Parameter | Coordinate Point 2 | 3D Vector |  |
| Output Parameter | Distance | Floating Point Numbers |  |

## **22. Phép NOT Logic**

![]()

**Chức năng Node**

Thực hiện phép NOT logic trên giá trị Boolean đầu vào và trả về kết quả

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input | Boolean |  |
| Output Parameter | Result | Boolean |  |

## **23. Phép OR Logic**

![]()

**Chức năng Node**

Thực hiện phép OR logic trên hai giá trị Boolean đầu vào và trả về kết quả

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input 1 | Boolean |  |
| Input Parameter | Input 2 | Boolean |  |
| Output Parameter | Result | Boolean |  |

## **24. Phép XOR Logic**

![]()

**Chức năng Node**

Thực hiện phép XOR logic trên hai giá trị Boolean đầu vào và trả về kết quả

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input 1 | Boolean |  |
| Input Parameter | Input 2 | Boolean |  |
| Output Parameter | Result | Boolean |  |

## **25. Phép AND Logic**

![]()

**Chức năng Node**

Thực hiện phép AND logic trên hai giá trị Boolean đầu vào và trả về kết quả

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input 1 | Boolean |  |
| Input Parameter | Input 2 | Boolean |  |
| Output Parameter | Result | Boolean |  |

## **26. Lũy thừa**

![]()

**Chức năng Node**

Nâng cơ số lên mức lũy thừa cho trước và trả về kết quả

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Base | Generic |  |
| Input Parameter | Exponent | Generic |  |
| Output Parameter | Result | Generic |  |

## **27. Phép modulo**

![]()

**Chức năng Node**

Trả về kết quả của input 1 modulo input 2, với input 1 là số chia

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter |  | Integer |  |
| Input Parameter |  | Integer |  |
| Output Parameter | Result | Integer |  |

## **28. Phép căn bậc hai**

![]()

**Chức năng Node**

Trả về căn bậc hai của giá trị đầu vào

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input | Floating Point Numbers |  |
| Output Parameter | Result | Floating Point Numbers |  |

## **29. Phép xác định dấu**

![]()

**Chức năng Node**

Khi đầu vào dương, trả về 1

Khi đầu vào âm, trả về -1

Khi đầu vào bằng 0, trả về 0

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input | Generic |  |
| Output Parameter | Result | Generic |  |

## **30. Phép làm tròn tới số nguyên**

![]()

**Chức năng Node**

Thực hiện phép làm tròn dựa trên phương pháp làm tròn và trả về số nguyên đã làm tròn

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Input | Floating Point Numbers |  |
| Input Parameter | Rounding Mode | Enumeration | Round: Rounds to the nearest integer according to standard rules  Round Up: Returns the smallest integer greater than the input value. For example: input 1.2 → 2; input −2.3 → −2  Round Down: Returns the largest integer smaller than the input value. For example: input 1.2 → 1; input −2.3 → −3  Truncate: Removes the decimal part of the floating point number (rounds toward zero). For example: input 1.2 → 1; input −2.3 → −2 |
| Output Parameter | Result | Integer |  |

## **31. Chuẩn hoá Vector 3D**

![]()

**Chức năng Node**

Chuẩn hoá độ dài của Vector 3D và xuất ra kết quả

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector | 3D Vector |  |
| Output Parameter | Result | 3D Vector |  |

## **32. Cộng Vector 3D**

![]()

**Chức năng Node**

Tính tổng của hai Vector 3D

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector 1 | 3D Vector |  |
| Input Parameter | 3D Vector 2 | 3D Vector |  |
| Output Parameter | Result | 3D Vector |  |

## **33. Góc Vector 3D**

![]()

**Chức năng Node**

Tính góc giữa hai Vector 3D và xuất ra dưới dạng radian

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector 1 | 3D Vector |  |
| Input Parameter | 3D Vector 2 | 3D Vector |  |
| Output Parameter | Angle (Radians) | Floating Point Numbers |  |

## **34. Trừ Vector 3D**

![]()

**Chức năng Node**

Tính hiệu của hai Vector 3D

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector 1 | 3D Vector |  |
| Input Parameter | 3D Vector 2 | 3D Vector |  |
| Output Parameter | Result | 3D Vector |  |

## **35. Độ dài Vector 3D**

![]()

**Chức năng Node**

Tính độ lớn (magnitude) của Vector 3D đầu vào

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector | 3D Vector |  |
| Output Parameter | Result | Floating Point Numbers |  |

## **36. Tích vô hướng Vector 3D**

![]()

**Chức năng Node**

Tính tích vô hướng của hai Vector 3D đầu vào

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector 1 | 3D Vector |  |
| Input Parameter | 3D Vector 2 | 3D Vector |  |
| Output Parameter | Result | Floating Point Numbers |  |

## **37. Phép nhân vô hướng Vector 3D**

![]()

**Chức năng Node**

Phóng đại Vector 3D đầu vào (phép nhân vô hướng) và xuất ra kết quả

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector | 3D Vector |  |
| Input Parameter | Zoom Multiplier | Floating Point Numbers |  |
| Output Parameter | Result | 3D Vector |  |

## **38. Tích có hướng Vector 3D**

![]()

**Chức năng Node**

Tính tích có hướng của hai Vector 3D

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | 3D Vector 1 | 3D Vector |  |
| Input Parameter | 3D Vector 2 | 3D Vector |  |
| Output Parameter | Result | 3D Vector |  |

## **39. Quay Vector 3D**

![]()

**Chức năng Node**

Xoay Vector 3D đầu vào theo các góc Euler được chỉ định và trả về kết quả

Note: The Rotated 3D Vector is the one you want to rotate. The Rotated Euler Angles define how the vector should be rotated. The resulting output vector shows the position of the original 3D Vector after applying the rotation.

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Rotate | 3D Vector | This 3D input vector represents a specific rotation in Euler angles, where each component represents:  X – Pitch: Rotation around the local X-axis (right). Controls looking up and down.  Y – Yaw: Rotation around the local Y-axis (up). Controls turning left and right.  Z – Roll: Rotation around the local Z-axis (forward). Controls tilting the object side to side. |
| Input Parameter | Rotated 3D Vector | 3D Vector |  |
| Output Parameter | Result | 3D Vector |  |

## **40. Lớn hơn**

![]()

**Chức năng Node**

Trả về liệu giá trị bên trái có lớn hơn giá trị bên phải hay không

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Left Value | Generic |  |
| Input Parameter | Right Value | Generic |  |
| Output Parameter | Result | Boolean |  |

## **41. Lớn hơn hoặc bằng**

![]()

**Chức năng Node**

Trả về liệu giá trị bên trái có lớn hơn hoặc bằng giá trị bên phải hay không

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Left Value | Generic |  |
| Input Parameter | Right Value | Generic |  |
| Output Parameter | Result | Boolean |  |

## **42. Nhỏ hơn**

![]()

**Chức năng Node**

Trả về liệu giá trị bên trái có nhỏ hơn giá trị bên phải hay không

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Left Value | Generic |  |
| Input Parameter | Right Value | Generic |  |
| Output Parameter | Result | Boolean |  |

## **43. Nhỏ hơn hoặc bằng**

![]()

**Chức năng Node**

Trả về liệu giá trị bên trái có nhỏ hơn hoặc bằng giá trị bên phải hay không

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Left Value | Generic |  |
| Input Parameter | Right Value | Generic |  |
| Output Parameter | Result | Boolean |  |

## **44. Hàm cosin**

![]()

**Chức năng Node**

Tính giá trị cosin của đầu vào tính bằng radian

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Radian | Floating Point Numbers |  |
| Output Parameter | Result | Floating Point Numbers |  |

## **45. Hàm tang**

![]()

**Chức năng Node**

Tính giá trị tang của đầu vào tính bằng radian

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Radian | Floating Point Numbers |  |
| Output Parameter | Result | Floating Point Numbers |  |

## **46. Hàm sin**

![]()

**Chức năng Node**

Tính giá trị sin của đầu vào tính bằng radian

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Radian | Floating Point Numbers |  |
| Output Parameter | Result | Floating Point Numbers |  |

## **47. Phép dịch trái**

![]()

**Chức năng Node**

Thực hiện phép dịch trái logic trên đầu vào với số bit được chỉ định và xuất ra kết quả

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Value | Integer |  |
| Input Parameter | Left Shift Count | Integer |  |
| Output Parameter | Result | Integer |  |

## **48. Phép dịch phải**

![]()

**Chức năng Node**

Thực hiện phép dịch phải logic trên đầu vào với số bit được chỉ định và xuất ra kết quả

Thực hiện phép dịch phải số học, giữ nguyên bit dấu

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Value | Integer |  |
| Input Parameter | Right Shift Count | Integer |  |
| Output Parameter | Result | Integer |  |

## **49. Phép AND bitwise**

![]()

**Chức năng Node**

Thực hiện phép AND bitwise trên hai đầu vào và trả về kết quả

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Value 1 | Integer |  |
| Input Parameter | Value 2 | Integer |  |
| Output Parameter | Result | Integer |  |

## **50. Phép OR bitwise**

![]()

**Chức năng Node**

Thực hiện phép OR bitwise trên hai đầu vào và trả về kết quả

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Value 1 | Integer |  |
| Input Parameter | Value 2 | Integer |  |
| Output Parameter | Result | Integer |  |

## **51. Phép XOR (Exclusive OR)**

![]()

**Chức năng Node**

Thực hiện phép XOR bitwise trên hai đầu vào và trả về kết quả

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Value 1 | Integer |  |
| Input Parameter | Value 2 | Integer |  |
| Output Parameter | Result | Integer |  |

## **52. Phủ định bitwise**

![]()

**Chức năng Node**

Thực hiện phép phủ định bitwise trên đầu vào và trả về kết quả

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Value | Integer |  |
| Output Parameter | Result | Integer |  |

## **53. Ghi bằng bit**

![]()

**Chức năng Node**

Ghi giá trị cần ghi dưới dạng nhị phân vào các bit [bắt đầu, kết thúc] của giá trị mục tiêu (cũng là số nhị phân). Bit bắt đầu được đánh chỉ số từ 0, và độ dài ghi bao gồm cả bit bắt đầu và kết thúc

Nếu độ dài nhị phân có ý nghĩa của giá trị ghi (đếm từ 1 đầu tiên bên trái) vượt quá độ dài ghi, thao tác ghi sẽ thất bại và trả về giá trị gốc

Nếu giá trị ghi là số âm, cũng sẽ thất bại do vượt quá độ dài ghi (bit đầu tiên của biểu diễn nhị phân số âm là bit dấu 1)

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Written value | Integer |  |
| Input Parameter | Write value | Integer |  |
| Input Parameter | Write starting position | Integer |  |
| Input Parameter | Write end position | Integer |  |
| Output Parameter | Result | Integer |  |

## **54. Đọc bằng bit**

![]()

**Chức năng Node**

Đọc giá trị từ các bit [bắt đầu, kết thúc] của giá trị (trong dạng biểu diễn nhị phân)

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Value | Integer |  |
| Input Parameter | Read starting position | Integer |  |
| Input Parameter | Read end position | Integer |  |
| Output Parameter | Result | Integer |  |

# III. Dictionary

## **1. Create Dictionary**

![]()

**Chức năng Node**

Creates Key-Value Pairs sequentially from the input key and value lists

This node builds the Dictionary using the shorter of the key and value lists; extra items are truncated

If duplicate keys are found in the key list, creation fails and returns an empty Dictionary

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Key List | Generic |  |
| Input Parameter | Value List | Generic |  |
| Output Parameter | Dictionary | Generic |  |

## **2. Assembly Dictionary**

![]()

**Chức năng Node**

Combines up to 50 Key-Value Pairs into one Dictionary

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Key 0~49 | Generic |  |
| Input Parameter | Value 0~49 | Generic |  |
| Output Parameter | Dictionary | Generic |  |

# IV. Structures

## **1. Split Structure**

![]()

**Chức năng Node**

Returns all parameters of the specified Structure

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Structure |  |  |

## **2. Assemble Structure**

![]()

**Chức năng Node**

Combines multiple parameters into a single Structure-type value

**Tham số Node**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Output Parameter | Structure |  |  |

# 

#

Query Nodes
