# Execution Nodes

# I. Common Nodes

## 1. Print String (In Chuỗi ra Nhật ký)

![](./execution node_files/1046b7d4-27e8-4799-959c-38979dd3fb4f.png)

**Node Functions (Chức năng Node)**

Xuất một chuỗi (string) ra màn hình nhật ký (log), thường được dùng để kiểm tra logic và gỡ lỗi (debugging).

Trong nhật ký, chuỗi này sẽ được in ra mỗi khi logic chạy thành công, bất kể Node Graph này có được kích hoạt hiển thị hay không.

**Node Parameters (Tham số Node)**

| | | | |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | String (Chuỗi) | String (Chuỗi) | Chuỗi văn bản cần in ra |

## **2. Set Local Variable (Cài đặt Biến Cục bộ)**

![](./execution node_files/403da859-e446-470e-becf-c4cedf6384aa.png)

**Node Functions (Chức năng Node)**

Khi được kết nối với Query Node (Node Truy vấn) có tên [Get Local Variable], node này sẽ ghi đè giá trị mới lên Biến Cục bộ đó.

**Node Parameters (Tham số Node)**

| | | | |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Local Variable (Biến cục bộ) | Local Variable (Biến cục bộ) | Vùng chứa để lưu trữ dữ liệu |
| Input Parameter (Đầu vào) | Value (Giá trị) | Generic (Chung) | Giá trị mới dùng để ghi đè lên biến cục bộ này |

## **3. Break Loop (Ngắt Vòng lặp)**

![]()

**Node Functions (Chức năng Node)**

Thoát khỏi Vòng lặp Hữu hạn (Finite Loop) hoặc Vòng lặp Duyệt Danh sách (List Iteration Loop). Chốt đầu ra (output pin) phải được kết nối với chốt đầu vào [Break Loop] của node [Finite Loop] hoặc [List Iteration Loop].

**Node Parameters (Tham số Node)**

| | | | |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| | | | |

## **4. Finite Loop (Vòng lặp Hữu hạn - For loop)**

![]()

**Node Functions (Chức năng Node)**

Bắt đầu từ [Loop Start Value] cho đến [Loop End Value], vòng lặp sẽ lặp lại liên tục, mỗi lần tăng thêm 1 đơn vị. Ở mỗi lần lặp, nó sẽ thực thi các Node được nối với chốt [Loop Body] (Thân vòng lặp). Sau khi lặp xong toàn bộ, nó sẽ thực thi các Node được nối với chốt [Loop Complete] (Hoàn thành vòng lặp).

Có thể dùng [Break Loop] để kết thúc quá trình lặp sớm. Sau khi thoát khỏi vòng lặp, logic được nối với chốt [Loop Complete] cũng sẽ được thực thi.

**Node Parameters (Tham số Node)**

| | | | |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Loop Start Value (Giá trị Bắt đầu) | Integer (Số nguyên) | Vòng lặp bao gồm cả giá trị này |
| Input Parameter (Đầu vào) | Loop End Value (Giá trị Kết thúc) | Integer (Số nguyên) | Vòng lặp bao gồm cả giá trị này |
| Output Parameter (Đầu ra) | Current Loop Value (Giá trị vòng lặp hiện tại) | Integer (Số nguyên) | Giá trị nguyên của vòng lặp hiện tại đang được thực thi |

## **5. Forwarding Event (Chuyển tiếp Sự kiện)**

![]()

**Node Functions (Chức năng Node)**

Chuyển tiếp sự kiện nguồn của Luồng Thực thi (Execution Flow) của Node này đến Thực thể Mục tiêu (Target Entity) được chỉ định. Sự kiện có cùng tên trên Node Graph của Thực thể Mục tiêu sẽ được kích hoạt.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể mục tiêu đang được chuyển tiếp |

# II. List Operations (Các thao tác với Danh sách)

## **1. Insert Value Into List (Chèn Giá trị vào Danh sách)**

![]()

**Node Functions (Chức năng Node)**

Chèn một giá trị tại Vị trí ID được chỉ định trong Danh sách đã chọn. Giá trị được chèn sẽ xuất hiện tại ID đó sau khi chèn.

Ví dụ: Chèn 5 tại ID 2 trong Danh sách [1, 2, 3, 4] sẽ tạo ra [1, 2, 5, 3, 4] (5 xuất hiện tại ID 2).

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | List (Danh sách) | Generic (Chung) | Tham chiếu đến danh sách đang được chèn |
| Input Parameter (Đầu vào) | Insert ID (ID Chèn) | Integer (Số nguyên) | ID của giá trị được chèn (sau khi chèn) |
| Input Parameter (Đầu vào) | Insert Value (Giá trị Chèn) | Generic (Chung) | Giá trị cần chèn |

## **2.** Set List Value (Cài đặt Giá trị Danh sách)

![]()

**Node Functions (Chức năng Node)**

Thiết lập giá trị tại một vị trí chỉ mục được chỉ định trong danh sách đã chọn.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | List (Danh sách) | Generic (Chung) | Tham chiếu danh sách đã chỉnh sửa |
| Input Parameter (Đầu vào) | ID | Integer (Số nguyên) | ID của giá trị được chỉnh sửa |
| Input Parameter (Đầu vào) | Value (Giá trị) | Generic (Chung) | Giá trị đã chỉnh sửa |

## **3. Remove Value From List (Xóa Giá trị khỏi Danh sách)**

![]()

**Node Functions (Chức năng Node)**

Xóa giá trị tại Vị trí ID được chỉ định khỏi Danh sách đã chọn. Tất cả các giá trị phía sau sẽ dịch chuyển lên trước một vị trí.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | List (Danh sách) | Generic (Chung) | Tham chiếu đến danh sách các giá trị cần xóa |
| Input Parameter (Đầu vào) | Remove ID (ID Xóa) | Integer (Số nguyên) | ID cần xóa |

## **4. List Iteration Loop (Vòng lặp Duyệt Danh sách)**

![]()

**Node Functions (Chức năng Node)**

Lặp qua Danh sách được chỉ định theo thứ tự tuần tự.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Iteration List (Danh sách Lặp) | Generic (Chung) | Danh sách để lặp qua |
| Output Parameter (Đầu ra) | Iteration Value (Giá trị Lặp) | Generic (Chung) | Mỗi giá trị trong danh sách |

## **5. List Sorting (Sắp xếp Danh sách)**

![]()

**Node Functions (Chức năng Node)**

Sắp xếp Danh sách được chỉ định theo phương pháp sắp xếp đã chọn.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | List (Danh sách) | Generic (Chung) | Danh sách Số nguyên hoặc Danh sách Số thực |
| Input Parameter (Đầu vào) | Sort By (Sắp xếp theo) | Enumeration (Liệt kê) | Tăng dần (Ascending) hoặc Giảm dần (Descending) |

## **6. Concatenate List (Nối Danh sách)**

![]()

**Node Functions (Chức năng Node)**

Nối Danh sách đầu vào vào cuối Danh sách Mục tiêu. Ví dụ: Danh sách Mục tiêu [1, 2, 3] với đầu vào [4, 5] trở thành [1, 2, 3, 4, 5] sau khi thực thi.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target List (Danh sách Mục tiêu) | Generic (Chung) | Danh sách đang được nhập vào |
| Input Parameter (Đầu vào) | Input List (Danh sách Đầu vào) | Generic (Chung) | Danh sách đầu vào sẽ được thêm vào cuối Danh sách Mục tiêu |

## **7. Clear List (Xóa sạch Danh sách)**

![]()

**Node Functions (Chức năng Node)**

Làm trống Danh sách được chỉ định.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | List (Danh sách) | Generic (Chung) | Danh sách cần làm trống |

# III. Custom Variables (Biến Tùy Chỉnh)

## **1. Set Node Graph Variable (Cài đặt Biến Node Graph)**

![]()

**Node Functions (Chức năng Node)**

Thiết lập giá trị của Biến Node Graph được chỉ định trong Node Graph hiện tại.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Variable Name (Tên Biến) | String (Chuỗi) | Tên của Biến Node Graph. Phải là duy nhất trong cùng một Node Graph |
| Input Parameter (Đầu vào) | Variable Value (Giá trị Biến) | Generic (Chung) | Giá trị được gán cho biến này |
| Input Parameter (Đầu vào) | Trigger Event (Kích hoạt Sự kiện) | Boolean (Logic) | Mặc định: True. Nếu đặt thành False, việc chỉnh sửa Biến Node Graph này sẽ không kích hoạt Sự kiện Thay đổi Biến |

## **2. Set Custom Variable (Cài đặt Biến Tùy Chỉnh)**

![]()

**Node Functions (Chức năng Node)**

Thiết lập giá trị của Biến Tùy chỉnh được chỉ định trên Thực thể Mục tiêu.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Biến được gắn vào thực thể này |
| Input Parameter (Đầu vào) | Variable Name (Tên Biến) | String (Chuỗi) | Tên biến tùy chỉnh. Phải là duy nhất |
| Input Parameter (Đầu vào) | Variable Value (Giá trị Biến) | Generic (Chung) | Giá trị được gán cho biến này |
| Input Parameter (Đầu vào) | Trigger Event (Kích hoạt Sự kiện) | Boolean (Logic) | Mặc định: True. Khi đặt thành False, việc chỉnh sửa biến tùy chỉnh này sẽ không kích hoạt sự kiện Khi Biến Tùy chỉnh Thay đổi (On Custom Variable Change) |

# IV. Preset Status (Trạng thái Được Lập trình Sẵn)

## **1. Set Preset Status (Cài đặt Trạng thái Được Lập trình Sẵn)**

![]()

**Node Functions (Chức năng Node)**

Thiết lập Trạng thái Được Lập trình Sẵn của Thực thể Mục tiêu được chỉ định.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Trạng thái Được Lập trình Sẵn được thiết lập cho thực thể |
| Input Parameter (Đầu vào) | Preset Status Index (Chỉ số Trạng thái) | Integer (Số nguyên) | Mã định danh duy nhất cho Trạng thái Được Lập trình Sẵn |
| Input Parameter (Đầu vào) | Preset Status Value (Giá trị Trạng thái) | Integer (Số nguyên) | Thường là "0" để tắt, "1" để bật |

# V. Entity Related (Liên quan đến Thực thể)

## **1. Create Entity (Tạo Thực thể)**

![]()

**Node Functions (Chức năng Node)**

Tạo một Thực thể bằng GUID. Thực thể phải được đặt trước trong Cảnh (Scene).

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target GUID (GUID Mục tiêu) | GUID | Mã định danh cho thực thể này |
| Input Parameter (Đầu vào) | Unit Tag Index List (Danh sách Chỉ số Thẻ Đơn vị) | Integer List (Danh sách Số nguyên) | Quyết định các Thẻ Đơn vị (Unit Tags) được mang theo khi thực thể này được tạo |

## **2. Create Prefab (Tạo Prefab)**

![]()

**Node Functions (Chức năng Node)**

Tạo một Thực thể bằng Prefab ID.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Prefab ID | Prefab ID | Mã định danh cho Prefab này |
| Input Parameter (Đầu vào) | Location (Vị trí) | 3D Vector | Vị trí tuyệt đối |
| Input Parameter (Đầu vào) | Rotate (Góc quay) | 3D Vector | Góc quay tuyệt đối |
| Input Parameter (Đầu vào) | Owner Entity (Thực thể Sở hữu) | Entity (Thực thể) | Quyết định xem thực thể được tạo ra có thuộc về một thực thể khác hay không |
| Input Parameter (Đầu vào) | Overwrite Level (Ghi đè Cấp độ) | Boolean (Logic) | Khi đặt thành False, tham số [Level] không có tác dụng |
| Input Parameter (Đầu vào) | Level (Cấp độ) | Integer (Số nguyên) | Quyết định Cấp độ khi thực thể được tạo |
| Input Parameter (Đầu vào) | Unit Tag Index List (Danh sách Chỉ số Thẻ Đơn vị) | Integer List (Danh sách Số nguyên) | Quyết định các Thẻ Đơn vị (Unit Tags) được mang theo khi thực thể này được tạo |
| Output Parameter (Đầu ra) | Created Entity (Thực thể được tạo) | Entity (Thực thể) | Các thực thể được tạo theo cách này không có GUID |

## 3. Create Prefab Group (Tạo Nhóm Prefab)

![]()

**Node Functions (Chức năng Node)**

Tạo các Thực thể có trong Nhóm Prefab bằng ID Nhóm Prefab.

**Node Parameters (Tham số Node)**

| Parameter Type (Loại) | Parameter Name (Tên tham số) | Type (Kiểu dữ liệu) | Description (Mô tả) |
| --- | --- | --- | --- |
| Input Parameter (Đầu vào) | Prefab Group ID (ID Nhóm Prefab) | Integer (Số nguyên) | Mã định danh cho Nhóm Prefab này |
| Input Parameter (Đầu vào) | Location (Vị trí) | 3D Vector | Vị trí tuyệt đối của trung tâm Nhóm Prefab |
| Input Parameter (Đầu vào) | Rotate (Góc quay) | 3D Vector | Góc quay tuyệt đối của trung tâm Nhóm Prefab |
| Input Parameter (Đầu vào) | Owner Entity (Thực thể Sở hữu) | Entity (Thực thể) | Quyết định xem thực thể có thuộc về một thực thể khác sau khi tạo hay không |
| Input Parameter (Đầu vào) | Level (Cấp độ) | Integer (Số nguyên) | Quyết định Cấp độ khi thực thể được tạo |
| Input Parameter (Đầu vào) | Unit Tag Index List (Danh sách Chỉ số Thẻ Đơn vị) | Integer List (Danh sách Số nguyên) | Quyết định các Thẻ Đơn vị (Unit Tags) được mang theo khi thực thể được tạo |
| Input Parameter (Đầu vào) | Overwrite Level (Ghi đè Cấp độ) | Boolean (Logic) | Khi đặt thành False, tham số [Level] không có tác dụng |
| Output Parameter (Đầu ra) | Created Entity List (Danh sách Thực thể được tạo) | Entity List (Danh sách Thực thể) | Các thực thể được tạo theo cách này không có GUID |

## **4. Activate/Disable Model Display (Kích hoạt/Vô hiệu hóa Hiển thị Mô hình)**

![]()

**Node Functions (Chức năng Node)**

Chỉnh sửa thuộc tính Hiển thị Mô hình của Thực thể để làm cho Mô hình của nó có thể nhìn thấy hoặc bị ẩn.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể sẽ được chỉnh sửa |
| Input Parameter (Đầu vào) | Activate (Kích hoạt) | Boolean (Logic) | Đặt thành True để làm cho mô hình hiển thị |

## **5. Destroy Entity**

![]()

**Node Functions (Chức năng Node)**

Phá hủy một thực thể được chỉ định sẽ dẫn đến hiệu ứng phá hủy và cũng có thể kích hoạt các logic chỉ xảy ra sau khi phá hủy, chẳng hạn như các hành vi khi kết thúc tuổi thọ của các vật thể bay cục bộ hoặc việc rớt ra các quả cầu năng lượng từ các tác phẩm tạo ra bị phá hủy.

Các sự kiện [Khi Thực thể Bị Phá hủy] (When Entity Is Destroyed) và [Khi Thực thể Bị Gỡ bỏ/Phá hủy] (When Entity Is Removed/Destroyed) có thể được giám sát trên Thực thể Màn chơi (Stage Entities).

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể sẽ bị phá hủy |

## **6. Remove Entity (Gỡ bỏ Thực thể)**

![]()

**Node Functions (Chức năng Node)**

Gỡ bỏ một thực thể được chỉ định thì khác với việc phá hủy nó; sẽ không có hiệu ứng phá hủy, và nó sẽ không kích hoạt bất kỳ logic nào xảy ra sau khi phá hủy, chẳng hạn như các hành vi khi kết thúc tuổi thọ trong các vật thể bay cục bộ hoặc việc rớt ra các quả cầu năng lượng từ các tác phẩm tạo ra bị gỡ bỏ.

Việc gỡ bỏ một Thực thể không kích hoạt sự kiện [Khi Thực thể Bị Phá hủy] (On Entity Destroyed), nhưng nó có thể kích hoạt sự kiện [Khi Thực thể Bị Gỡ bỏ/Phá hủy] (On Entity Removed/Destroyed).

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể sẽ bị gỡ bỏ |

# VI. Stage Related (Liên quan đến Màn chơi)

## **1. Settle Stage (Tổng kết Màn chơi)**

![]()

**Node Functions (Chức năng Node)**

Kích hoạt quá trình Tổng kết Màn chơi, quá trình này thực thi logic bên ngoài màn chơi như được định nghĩa trong mục Tổng kết Màn chơi.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
|  |  |  |  |

## **2. Set Current Environment Time (Cài đặt Thời gian Môi trường Hiện tại)**

![]()

**Node Functions (Chức năng Node)**

Ngay lập tức chuyển Thời gian Môi trường sang giờ được chỉ định. Tham số phải là một Số thực từ 0 đến 24.

Nếu giờ mục tiêu sớm hơn giờ hiện tại, nó được tính là ngày hôm sau (+1 ngày).

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Environment Time (Thời gian Môi trường) | Floating Point Numbers (Số thực) | Phải là một giá trị số thực từ 0–24; Node này sẽ không có hiệu lực nếu giá trị nằm ngoài phạm vi này |

## **3. Set Environment Time Passage Speed (Cài đặt Tốc độ Trôi qua của Thời gian Môi trường)**

![]()

**Node Functions (Chức năng Node)**

Số phút trôi qua mỗi giây, giới hạn từ 0 - 60 (Tốc độ ở Teyvat là 1).

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Environment Time Passage Speed (Tốc độ Trôi qua của Thời gian Môi trường) | Floating Point Numbers (Số thực) | Bị giới hạn trong phạm vi 0–60. Các giá trị ngoài phạm vi này được tự động đặt thành 0 hoặc 60 |

# VII. Faction Related (Liên quan đến Phe phái)

1.

## Set Entity Faction (Cài đặt Phe phái cho Thực thể)

![]()

**Node Functions (Chức năng Node)**

Thiết lập phe phái của thực thể mục tiêu được chỉ định.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể sẽ được chỉnh sửa phe phái |
| Input Parameter (Đầu vào) | Faction (Phe phái) | Faction (Phe phái) | Phe phái đã chỉnh sửa |

# VIII. Player and Character Related (Liên quan đến Người chơi và Nhân vật)

## **1. Teleport Player (Dịch chuyển Người chơi)**

![]()

**Node Functions (Chức năng Node)**

Dịch chuyển Thực thể Người chơi được chỉ định. Một giao diện tải có thể xuất hiện tùy thuộc vào khoảng cách dịch chuyển.

Nếu dịch chuyển lên trên một vật thể, hãy đảm bảo tọa độ Y mục tiêu cao hơn một chút so với vị trí tiếp đất.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Player Entity (Thực thể Người chơi) | Entity (Thực thể) | Người chơi Đang hoạt động (Active Player) |
| Input Parameter (Đầu vào) | Target Location (Vị trí Mục tiêu) | 3D Vector | Vị trí Tuyệt đối (Absolute Location) |
| Input Parameter (Đầu vào) | Target Rotation (Góc quay Mục tiêu) | 3D Vector | Góc quay Tuyệt đối (Absolute Rotation) |

## **2. Revive Character (Hồi sinh Nhân vật)**

![]()

**Node Functions (Chức năng Node)**

Chỉ khả dụng trong Chế độ Beyond (Beyond Mode), hồi sinh Thực thể Nhân vật được chỉ định.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Character Entity (Thực thể Nhân vật) | Entity (Thực thể) | Thực thể Nhân vật sẽ được hồi sinh |

## **3. Revive All Player's Characters (Hồi sinh Tất cả Nhân vật của Người chơi)**

![]()

**Node Functions (Chức năng Node)**

Hồi sinh tất cả thực thể nhân vật của người chơi được chỉ định, nhưng node này chỉ có hiệu lực khi người chơi ở trạng thái mà tất cả nhân vật của họ đã bị hạ gục.

Trong Chế độ Beyond, vì mỗi người chơi chỉ có một nhân vật, node này có tác dụng tương tự như node "Revive Character" (Hồi sinh Nhân vật).

Trong Chế độ Classic (Cổ điển), người chơi có thể có nhiều nhân vật. Nếu chỉ một số nhân vật bị hạ gục, node này sẽ không có hiệu lực, nghĩa là nó sẽ không hồi sinh các nhân vật đã bị hạ gục.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Player Entity (Thực thể Người chơi) | Entity (Thực thể) | Thực thể Người chơi sở hữu Nhân vật |
| Input Parameter (Đầu vào) | Deduct Revives (Trừ lượt Hồi sinh) | Boolean (Logic) | Nếu đặt thành False, Số lượt Hồi sinh sẽ không bị trừ |

## **4. Defeat All Player's Characters (Hạ gục Tất cả Nhân vật của Người chơi)**

![]()

**Node Functions (Chức năng Node)**

Đánh gục tất cả nhân vật của người chơi được chỉ định, khiến người chơi bước vào trạng thái *Khi Tất cả Nhân vật của Người chơi Bị Hạ gục* (When All Player's Characters Are Down).

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Player Entity (Thực thể Người chơi) | Entity (Thực thể) | Thực thể Người chơi sở hữu Nhân vật |

## **5. Activate Revive Point (Kích hoạt Điểm Hồi sinh)**

![]()

**Node Functions (Chức năng Node)**

Kích hoạt ID Điểm Hồi sinh được chỉ định cho người chơi. Lần sau, khi người chơi kích hoạt logic Hồi sinh, họ có thể hồi sinh tại Điểm Hồi sinh này.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Player Entity (Thực thể Người chơi) | Entity (Thực thể) | Người chơi Đang hoạt động (Active Player) |
| Input Parameter (Đầu vào) | Revive Point ID (ID Điểm Hồi sinh) | Integer (Số nguyên) | Mã định danh cho Điểm Hồi sinh này |

## **6. Set Player Revive Time (Cài đặt Thời gian Hồi sinh của Người chơi)**

![]()

**Node Functions (Chức năng Node)**

Cài đặt thời lượng cho lần hồi sinh tiếp theo của Người chơi. Nếu Người chơi hiện đang hồi sinh, điều này không ảnh hưởng đến quá trình hồi sinh đang diễn ra.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Player Entity (Thực thể Người chơi) | Entity (Thực thể) | Người chơi Đang hoạt động |
| Input Parameter (Đầu vào) | Duration (Thời lượng) | Integer (Số nguyên) | Đơn vị là giây |

## **7. Set Player Remaining Revives (Cài đặt Số lượt Hồi sinh Còn lại của Người chơi)**

![]()

**Node Functions (Chức năng Node)**

Cài đặt số lượt hồi sinh còn lại cho Người chơi được chỉ định. Khi đặt thành 0, Người chơi không thể hồi sinh.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Player Entity (Thực thể Người chơi) | Entity (Thực thể) | Người chơi Đang hoạt động |
| Input Parameter (Đầu vào) | Remaining Times (Số lần Còn lại) | Integer (Số nguyên) | Khi đặt thành 0, người chơi sẽ không được hồi sinh |

## **8. Set Environment Configuration (Cài đặt Cấu hình Môi trường)**

![]()

**Node Functions (Chức năng Node)**

Áp dụng Cấu hình Môi trường được chỉ định cho người chơi được chọn. Có hiệu lực ngay khi thực thi.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Environment Config Index (Chỉ số Cấu hình Môi trường) | Integer (Số nguyên) | Mã định danh cho Cấu hình Môi trường này |
| Input Parameter (Đầu vào) | Target Player List (Danh sách Người chơi Mục tiêu) | Entity List (Danh sách Thực thể) | Chỉ áp dụng cho Người chơi trong danh sách được chỉ định |
| Input Parameter (Đầu vào) | Enable Weather Config (Bật Cấu hình Thời tiết) | Boolean (Logic) | Đặt thành True để bật |
| Input Parameter (Đầu vào) | Weather Config Index (Chỉ số Cấu hình Thời tiết) | Integer (Số nguyên) | Cấu hình Thời tiết khớp với ID này sẽ có hiệu lực. Nếu ID không tồn tại, sẽ không có gì xảy ra |

## **9. Allow/Forbid Player to Revive (Cho phép/Cấm Người chơi Hồi sinh)**

![]()

**Node Functions (Chức năng Node)**

Cài đặt xem người chơi được chỉ định có được phép hồi sinh hay không.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Player Entity (Thực thể Người chơi) | Entity (Thực thể) | Người chơi Đang hoạt động |
| Input Parameter (Đầu vào) | Allow (Cho phép) | Boolean (Logic) | Nếu đặt thành True, người chơi được phép hồi sinh |

## **10. Deactivate Revive Point (Hủy kích hoạt Điểm Hồi sinh)**

![]()

**Node Functions (Chức năng Node)**

Hủy đăng ký ID Điểm Hồi sinh được chỉ định cho người chơi. Lần tới, người chơi sẽ không hồi sinh tại Điểm Hồi sinh này.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Player Entity (Thực thể Người chơi) | Entity (Thực thể) | Người chơi Đang hoạt động |
| Input Parameter (Đầu vào) | Revive Point ID (ID Điểm Hồi sinh) | Integer (Số nguyên) | Mã định danh cho Điểm Hồi sinh này |

## **11.** Set Character's Elemental Energy (Cài đặt Năng lượng Nguyên tố của Nhân vật)

![]()

**Node Functions (Chức năng Node)**

Chỉ khả dụng trong Chế độ Classic (Cổ điển), cài đặt năng lượng nguyên tố cho một nhân vật cụ thể.

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Character Entity (Thực thể Nhân vật) | Entity (Thực thể) |  |
| Input Parameter (Đầu vào) | Elemental Energy (Năng lượng Nguyên tố) | Floating Point Numbers (Số thực) |  |

## **12.** Increases Character's Elemental Energy (Tăng Năng lượng Nguyên tố của Nhân vật)

![]()

**Node Functions (Chức năng Node)**

Chỉ khả dụng trong Chế độ Classic (Cổ điển), tăng năng lượng nguyên tố cho một nhân vật cụ thể.

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Character Entity (Thực thể Nhân vật) | Entity (Thực thể) |  |
| Input Parameter (Đầu vào) | Elemental Energy Increase Value (Giá trị Tăng Năng lượng Nguyên tố) | Floating Point Numbers (Số thực) |  |

## **13. Revive the active character (Hồi sinh nhân vật đang hoạt động)**

![]()

**Node Functions (Chức năng Node)**

Chỉ khả dụng trong Chế độ Classic (Cổ điển), hồi sinh thực thể nhân vật đang hoạt động đã bị hạ gục của người chơi được chỉ định.

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Player Entity (Thực thể Người chơi) | Entity (Thực thể) |  |

## **14. Teleport Player (Classic Mode) (Dịch chuyển Người chơi (Chế độ Cổ điển))**

![]()

**Node Functions (Chức năng Node)**

Dịch chuyển Thực thể Người chơi được chỉ định. Một màn hình tải có thể xuất hiện tùy thuộc vào khoảng cách di chuyển.

Nếu dịch chuyển lên trên một vật thể, tọa độ Y của vị trí mục tiêu phải cao hơn một chút so với điểm tiếp đất.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Player Entity (Thực thể Người chơi) | Entity (Thực thể) | Người chơi Đang hoạt động |
| Input Parameter (Đầu vào) | Target Location (Vị trí Mục tiêu) | 3D Vector | Vị trí tuyệt đối |
| Input Parameter (Đầu vào) | Target Rotation (Góc quay Mục tiêu) | 3D Vector | Góc quay tuyệt đối |

# IX. Collision (Va chạm)

## **1. Activate/Disable Extra Collision (Kích hoạt/Vô hiệu hóa Va chạm Phụ)**

![]()

**Node Functions (Chức năng Node)**

Chỉnh sửa dữ liệu trong Thành phần Va chạm Phụ (Extra Collision Component) của Thực thể để bật/tắt Va chạm Phụ.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể Đang hoạt động (Active Entity) |
| Input Parameter (Đầu vào) | Extra Collision ID (ID Va chạm Phụ) | Integer (Số nguyên) | Mã định danh cho Va chạm Phụ này |
| Input Parameter (Đầu vào) | Activate (Kích hoạt) | Boolean (Logic) | Đặt thành True để kích hoạt |

## **2. Activate/Disable Extra Collision Climbability (Kích hoạt/Vô hiệu hóa Khả năng Leo trèo của Va chạm Phụ)**

![]()

**Node Functions (Chức năng Node)**

Chỉnh sửa Khả năng Leo trèo (Climbability) của Thành phần Va chạm Phụ của Thực thể.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể Đang hoạt động |
| Input Parameter (Đầu vào) | Extra Collision ID (ID Va chạm Phụ) | Integer (Số nguyên) | Mã định danh cho Va chạm Phụ này |
| Input Parameter (Đầu vào) | Activate (Kích hoạt) | Boolean (Logic) | Đặt thành True để kích hoạt |

## **3. Activate/Disable Native Collision (Kích hoạt/Vô hiệu hóa Va chạm Gốc)**

![]()

**Node Functions (Chức năng Node)**

Chỉnh sửa Va chạm Gốc (Native Collision) của Thực thể.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể Đang hoạt động |
| Input Parameter (Đầu vào) | Activate (Kích hoạt) | Boolean (Logic) | Đặt thành True để kích hoạt |

## **4. Activate/Disable Native Collision Climbability (Kích hoạt/Vô hiệu hóa Khả năng Leo trèo của Va chạm Gốc)**

![]()

**Node Functions (Chức năng Node)**

Chỉnh sửa Khả năng Leo trèo của Va chạm Gốc của Thực thể.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể Đang hoạt động |
| Input Parameter (Đầu vào) | Activate (Kích hoạt) | Boolean (Logic) | Đặt thành True để kích hoạt |

# X. Collision Triggers (Kích hoạt Va chạm)

## **1. Activate/Disable Collision Trigger (Kích hoạt/Vô hiệu hóa Kích hoạt Va chạm)**

![]()

**Node Functions (Chức năng Node)**

Chỉnh sửa dữ liệu của Thành phần Kích hoạt Va chạm (Collision Trigger Component) để Kích hoạt/Vô hiệu hóa Kích hoạt tại ID được chỉ định.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể Đang hoạt động |
| Input Parameter (Đầu vào) | Trigger ID (ID Kích hoạt) | Integer (Số nguyên) | Mã định danh cho Kích hoạt Va chạm này |
| Input Parameter (Đầu vào) | Activate (Kích hoạt) | Boolean (Logic) | Đặt thành True để kích hoạt |

# XI. Combat (Chiến đấu)

## **1. Initiate Attack (Bắt đầu Tấn công)**

![]()

![]()

**Node Functions (Chức năng Node)**

Làm cho Thực thể được chỉ định bắt đầu một cuộc tấn công. Thực thể sử dụng node này phải được cấu hình Đơn vị Kỹ năng (Ability Unit) tương ứng.

Có hai chế độ sử dụng:

Khi Đơn vị Kỹ năng là [Tấn công Hitbox] (Hitbox Attack), nó thực hiện một đòn tấn công hitbox tập trung vào Vị trí của Thực thể Mục tiêu.

Khi Đơn vị Kỹ năng là [Tấn công Trực tiếp] (Direct Attack), nó trực tiếp tấn công Thực thể Mục tiêu.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Tùy thuộc vào Đơn vị Kỹ năng, phần này có thể được xem là mục tiêu tham chiếu cho Vị trí Hitbox hoặc làm mục tiêu tấn công |
| Input Parameter (Đầu vào) | Damage Coefficient (Hệ số Sát thương) | Floating Point Numbers (Số thực) | Hệ số áp dụng cho lượng sát thương gây ra bởi đòn tấn công này |
| Input Parameter (Đầu vào) | Damage Increment (Gia tăng Sát thương) | Floating Point Numbers (Số thực) | Lượng sát thương cộng thêm áp dụng cho đòn tấn công này |
| Input Parameter (Đầu vào) | Location Offset (Độ lệch Vị trí) | 3D Vector | Khi sử dụng Tấn công Hitbox, sẽ xác định độ lệch Hitbox. Khi sử dụng Tấn công Trực tiếp, sẽ xác định vị trí phát hiện đòn đánh cho cuộc tấn công và do đó quyết định nơi các hiệu ứng đặc biệt khi trúng đòn được tạo ra |
| Input Parameter (Đầu vào) | Rotation Offset (Độ lệch Góc quay) | 3D Vector | Khi sử dụng Tấn công Hitbox, sẽ xác định góc quay Hitbox. Khi sử dụng Tấn công Trực tiếp, sẽ xác định vị trí phát hiện đòn đánh cho cuộc tấn công và do đó quyết định góc quay được sử dụng cho các hiệu ứng khi trúng đòn |
| Input Parameter (Đầu vào) | Ability Unit (Đơn vị Kỹ năng) | String (Chuỗi) | Đơn vị Kỹ năng được tham chiếu. Phải được cấu hình trên thực thể được liên kết với Node Graph này |
| Input Parameter (Đầu vào) | Overwrite Ability Unit Config (Ghi đè Cấu hình Đơn vị Kỹ năng) | Boolean (Logic) | Khi đặt thành True, bốn tham số — Hệ số Sát thương, Gia tăng Sát thương, Độ lệch Vị trí và Độ lệch Góc quay — sẽ ghi đè các tham số có cùng tên trong Đơn vị Kỹ năng. Khi đặt thành False, cấu hình ban đầu của Đơn vị Kỹ năng sẽ được sử dụng |
| Input Parameter (Đầu vào) | Initiator Entity (Thực thể Khởi xướng) | Entity (Thực thể) | Xác định Thực thể Khởi xướng cho cuộc tấn công này. Mặc định là Thực thể được liên kết với Node Graph này. Ảnh hưởng đến việc kẻ tấn công nào được xác định trong các sự kiện như Trúng đòn (On Hit) và Khi Bị Tấn công (When Attacked) |

## **2. Recover HP (Phục hồi HP)**

![]()

**Node Functions (Chức năng Node)**

Phục hồi HP cho Thực thể Mục tiêu được chỉ định thông qua một Đơn vị Kỹ năng.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Mục tiêu phục hồi HP |
| Input Parameter (Đầu vào) | Recovery Amount (Lượng Phục hồi) | Floating Point Numbers (Số thực) | Lượng HP được phục hồi trong lần hồi máu này |
| Input Parameter (Đầu vào) | Ability Unit (Đơn vị Kỹ năng) | String (Chuỗi) | Đơn vị Kỹ năng được tham chiếu. Phải được cấu hình trên thực thể liên kết với Node Graph này |
| Input Parameter (Đầu vào) | Overwrite Ability Unit Config (Ghi đè Cấu hình Đơn vị Kỹ năng) | Boolean (Logic) | Khi đặt thành True, Lượng Phục hồi ghi đè tham số có cùng tên trong Đơn vị Kỹ năng. Khi đặt thành False, cấu hình ban đầu của Đơn vị Kỹ năng sẽ được sử dụng |
| Input Parameter (Đầu vào) | Recover Initiator Entity (Thực thể Khởi xướng Phục hồi) | Entity (Thực thể) | Xác định Thực thể Khởi xướng của hành động hồi máu này. Mặc định là Thực thể liên kết với Node Graph này. Ảnh hưởng đến việc xác định người hồi máu trong các sự kiện như Khi HP Được Phục hồi (When HP Is Recovered) và Khi Bắt đầu Phục hồi HP (When Initiating HP Recovery) |

## **3. HP Loss (Mất HP)**

![]()

**Node Functions (Chức năng Node)**

Trực tiếp làm cho mục tiêu được chỉ định bị mất HP. Mất HP không phải là một cuộc tấn công, vì vậy nó không kích hoạt các sự kiện liên quan đến tấn công.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Mục tiêu bị mất HP |
| Input Parameter (Đầu vào) | HP Loss (Lượng HP Mất) | Floating Point Numbers (Số thực) | Lượng HP bị mất trong trường hợp này |
| Input Parameter (Đầu vào) | Lethal (Chí mạng) | Boolean (Logic) | Nếu đặt thành False, lần mất HP này sẽ để lại cho Mục tiêu ít nhất 1 HP |
| Input Parameter (Đầu vào) | Can be blocked by invincibility (Có thể bị chặn bởi trạng thái bất khả chiến bại) | Boolean (Logic) | Nếu đặt thành True, và Mục tiêu được đặt là Bất khả chiến bại (Invincible) thông qua Trạng thái Đơn vị (Unit Status), thì việc mất HP sẽ không có tác dụng |
| Input Parameter (Đầu vào) | Can be Blocked by Locked HP? (Có thể bị Chặn bởi HP Bị Khóa không?) | Boolean (Logic) | Nếu đặt thành True, và HP của Mục tiêu bị khóa thông qua Trạng thái Đơn vị, thì việc mất HP sẽ không có tác dụng |
| Input Parameter (Đầu vào) | Damage Pop-Up Type (Loại Hiển thị Sát thương) | Enumeration (Liệt kê) | Không Hiển thị (No Pop-Up) / Hiển thị Bình thường (Normal Pop-Up) / Hiển thị Đòn Chí mạng (CRIT Hit Pop-Up) |

## **4. Recover HP Directly (Phục hồi HP Trực tiếp)**

![]()

**Node Functions (Chức năng Node)**

Trực tiếp phục hồi HP cho Thực thể Mục tiêu được chỉ định. Khác với [Recover HP], node này không yêu cầu một Đơn vị Kỹ năng.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Recover Initiator Entity (Thực thể Khởi xướng Phục hồi) | Entity (Thực thể) | Thực thể khởi xướng việc hồi máu |
| Input Parameter (Đầu vào) | Recover Target Entity (Thực thể Mục tiêu Phục hồi) | Entity (Thực thể) | Thực thể Mục tiêu sẽ được hồi máu |
| Input Parameter (Đầu vào) | Recovery Amount (Lượng Phục hồi) | Floating Point Numbers (Số thực) | Lượng HP được phục hồi trong lần hồi máu này |
| Input Parameter (Đầu vào) | Ignore Recovery Amount Adjustment (Bỏ qua Điều chỉnh Lượng Phục hồi) | Boolean (Logic) | Nếu đặt thành True, lượng hồi máu này sẽ không bị ảnh hưởng bởi các hiệu ứng Trạng thái Đơn vị của Mục tiêu có điều chỉnh lượng hồi máu |
| Input Parameter (Đầu vào) | Aggro Generation Multiplier (Hệ số Tạo Aggro) | Floating Point Numbers (Số thực) | Điểm Thu hút (Aggro) được tạo ra bởi lần hồi máu này, thể hiện dưới dạng hệ số nhân. Chỉ áp dụng khi sử dụng Chế độ Aggro Tùy chỉnh (Custom Aggro Mode) |
| Input Parameter (Đầu vào) | Aggro Generation Increment (Gia tăng Tạo Aggro) | Floating Point Numbers (Số thực) | Điểm Thu hút được tạo ra bởi lần hồi máu này, thể hiện dưới dạng giá trị gia tăng. Chỉ áp dụng khi sử dụng Chế độ Aggro Tùy chỉnh |
| Input Parameter (Đầu vào) | Healing Tag List (Danh sách Thẻ Hồi máu) | String List (Danh sách Chuỗi) | Danh sách các thẻ được liên kết với hành động hồi máu này. Có thể truy cập chúng trong các sự kiện Khi HP Được Phục hồi và Khi Bắt đầu Phục hồi HP để xác định một hành động hồi máu cụ thể |

# XII. Motion Devices (Thiết bị Chuyển động)

## **1. Recover Basic Motion Device (Khôi phục Thiết bị Chuyển động Cơ bản)**

![]()

**Node Functions (Chức năng Node)**

Tiếp tục một Thiết bị Chuyển động Cơ bản (Basic Motion Device) đang bị tạm dừng trên Thực thể Mục tiêu. Thực thể Mục tiêu phải có Thành phần Thiết bị Chuyển động Cơ bản.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể Đang hoạt động |
| Input Parameter (Đầu vào) | Motion Device Name (Tên Thiết bị Chuyển động) | String (Chuỗi) | Mã định danh cho thiết bị chuyển động này |

## **2. Activate Fixed-Point Motion Device (Kích hoạt Thiết bị Chuyển động Điểm Cố định)**

![]()

![]()

**Node Functions (Chức năng Node)**

Động lực thêm Thiết bị Chuyển động Cơ bản Điểm Cố định (Fixed-Point Basic Motion Device) vào Thực thể Mục tiêu trong thời gian chạy của Màn chơi.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể Đang hoạt động |
| Input Parameter (Đầu vào) | Motion Device Name (Tên Thiết bị Chuyển động) | String (Chuỗi) | Mã định danh cho thiết bị chuyển động này |
| Input Parameter (Đầu vào) | Movement Mode (Chế độ Di chuyển) | Enumeration (Liệt kê) |  |
| Input Parameter (Đầu vào) | Movement SPD (Tốc độ Di chuyển) | Floating Point Numbers (Số thực) |  |
| Input Parameter (Đầu vào) | Target Location (Vị trí Mục tiêu) | 3D Vector | Vị trí tuyệt đối |
| Input Parameter (Đầu vào) | Target Rotation (Góc quay Mục tiêu) | 3D Vector | Góc quay tuyệt đối |
| Input Parameter (Đầu vào) | Lock Rotation (Khóa Góc quay) | Boolean (Logic) |  |
| Input Parameter (Đầu vào) | Parameter Type (Loại tham số) | Enumeration (Liệt kê) | Tùy chọn: Tốc độ Cố định (Fixed Speed) hoặc Thời gian Cố định (Fixed Time) |
| Input Parameter (Đầu vào) | Movement Time (Thời gian Di chuyển) | Floating Point Numbers (Số thực) |  |

## **3. Activate Basic Motion Device (Kích hoạt Thiết bị Chuyển động Cơ bản)**

![]()

**Node Functions (Chức năng Node)**

Kích hoạt Thiết bị Chuyển động Cơ bản (Basic Motion Device) được cấu hình trong Thành phần Thiết bị Chuyển động Cơ bản của Thực thể Mục tiêu.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể Đang hoạt động |
| Input Parameter (Đầu vào) | Motion Device Name (Tên Thiết bị Chuyển động) | String (Chuỗi) | Mã định danh cho thiết bị chuyển động này |

## **4. Add Target-Oriented Rotation-Based Motion Device (Thêm Thiết bị Chuyển động Dựa trên Góc quay Hướng tới Mục tiêu)**

![]()

**Node Functions (Chức năng Node)**

Động lực thêm Thiết bị Chuyển động Cơ bản với khả năng Xoay Hướng tới Mục tiêu (Target-Oriented Rotation) vào Thực thể Mục tiêu trong thời gian chạy của Màn chơi.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể Đang hoạt động |
| Input Parameter (Đầu vào) | Motion Device Name (Tên Thiết bị Chuyển động) | String (Chuỗi) | Mã định danh cho thiết bị chuyển động này |
| Input Parameter (Đầu vào) | Motion Device Duration (Thời lượng Thiết bị Chuyển động) | Floating Point Numbers (Số thực) | Thời lượng mà thiết bị chuyển động này duy trì trạng thái hoạt động |
| Input Parameter (Đầu vào) | Target Angle (Góc Mục tiêu) | 3D Vector | Góc tuyệt đối |

## **5. Add Uniform Basic Linear Motion Device (Thêm Thiết bị Chuyển động Tuyến tính Cơ bản Đều)**

![]()

**Node Functions (Chức năng Node)**

Động lực thêm Thiết bị Chuyển động Cơ bản với Chuyển động Tuyến tính Đều (Uniform Linear Motion) vào thời gian chạy.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể Đang hoạt động |
| Input Parameter (Đầu vào) | Motion Device Name (Tên Thiết bị Chuyển động) | String (Chuỗi) | Mã định danh cho thiết bị chuyển động này |
| Input Parameter (Đầu vào) | Motion Device Duration (Thời lượng Thiết bị Chuyển động) | Floating Point Numbers (Số thực) | Thời lượng mà thiết bị chuyển động này duy trì trạng thái hoạt động |
| Input Parameter (Đầu vào) | Velocity Vector (Vecto Vận tốc) | 3D Vector | Xác định độ lớn và hướng của vận tốc |

## **6. Add Uniform Basic Rotation-Based Motion Device (Thêm Thiết bị Chuyển động Cơ bản Dựa trên Góc quay Đều)**

![]()

**Node Functions (Chức năng Node)**

Động lực thêm Thiết bị Chuyển động Cơ bản với Chuyển động Xoay Đều (Uniform Rotation) vào thời gian chạy.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể Đang hoạt động |
| Input Parameter (Đầu vào) | Motion Device Name (Tên Thiết bị Chuyển động) | String (Chuỗi) | Mã định danh cho thiết bị chuyển động này |
| Input Parameter (Đầu vào) | Motion Device Duration (Thời lượng Thiết bị Chuyển động) | Floating Point Numbers (Số thực) | Thời lượng mà thiết bị chuyển động này duy trì trạng thái hoạt động |
| Input Parameter (Đầu vào) | Angular Velocity (°/s) (Vận tốc Góc) | Floating Point Numbers (Số thực) | Độ lớn của Vận tốc Góc |
| Input Parameter (Đầu vào) | Rotation Axis Orientation (Hướng của Trục Quay) | 3D Vector | Hướng tương đối |

## **7. Stop and Delete Basic Motion Device (Dừng và Xóa Thiết bị Chuyển động Cơ bản)**

![]()

**Node Functions (Chức năng Node)**

Dừng và xóa một Thiết bị Chuyển động đang chạy.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể Đang hoạt động |
| Input Parameter (Đầu vào) | Motion Device Name (Tên Thiết bị Chuyển động) | String (Chuỗi) | Mã định danh cho thiết bị chuyển động này |
| Input Parameter (Đầu vào) | Stop All Basic Motion Devices (Dừng Tất cả Thiết bị Chuyển động Cơ bản) | Boolean (Logic) | Nếu đặt thành True, sẽ dừng tất cả Thiết bị Chuyển động Cơ bản trên Thực thể này. Nếu đặt thành False, chỉ dừng Thiết bị Chuyển động có tên khớp với thiết bị được chỉ định |

## **8. Pause Basic Motion Device (Tạm dừng Thiết bị Chuyển động Cơ bản)**

![]()

**Node Functions (Chức năng Node)**

Tạm dừng một Thiết bị Chuyển động đang chạy. Node Resume Motion Device (Tiếp tục Thiết bị Chuyển động) sau đó có thể được sử dụng để tiếp tục.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể Đang hoạt động |
| Input Parameter (Đầu vào) | Motion Device Name (Tên Thiết bị Chuyển động) | String (Chuỗi) | Mã định danh cho thiết bị chuyển động này |

# XIII. Follow Motion Device (Thiết bị Chuyển động Theo dõi)

## **1. Activate/Disable Follow Motion Device (Kích hoạt/Vô hiệu hóa Thiết bị Chuyển động Theo dõi)**

![]()

**Node Functions (Chức năng Node)**

Bật/Tắt logic của Thiết bị Chuyển động Theo dõi trên Thực thể Mục tiêu.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể mà Thiết bị Chuyển động Theo dõi được gắn vào |
| Input Parameter (Đầu vào) | Activate (Kích hoạt) | Boolean (Logic) | Đặt thành True để kích hoạt |

## **2. Switch Follow Motion Device Target by GUID (Chuyển đổi Mục tiêu của Thiết bị Chuyển động Theo dõi theo GUID)**

![]()

![]()

**Node Functions (Chức năng Node)**

Chuyển đổi Mục tiêu Theo dõi của Thiết bị Chuyển động Theo dõi bằng GUID.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể mà Thiết bị Chuyển động Theo dõi được gắn vào |
| Input Parameter (Đầu vào) | Follow Target GUID (GUID của Mục tiêu Theo dõi) | GUID | Mã định danh cho Mục tiêu Theo dõi |
| Input Parameter (Đầu vào) | Follow Target Attachment Point Name (Tên Điểm đính kèm của Mục tiêu Theo dõi) | String (Chuỗi) | Tên của Điểm Đính kèm cần theo dõi |
| Input Parameter (Đầu vào) | Location Offset (Độ lệch Vị trí) | 3D Vector | Độ lệch vị trí dựa trên Hệ tọa độ Theo dõi |
| Input Parameter (Đầu vào) | Rotation Offset (Độ lệch Góc quay) | 3D Vector | Độ lệch góc quay dựa trên Hệ tọa độ Theo dõi |
| Input Parameter (Đầu vào) | Follow Coordinate System (Hệ tọa độ Theo dõi) | Enumeration (Liệt kê) | Tùy chọn: Hệ tọa độ Tương đối (Relative Coordinate System) hoặc Hệ tọa độ Thế giới (World Coordinate System) |
| Input Parameter (Đầu vào) | Follow Type (Kiểu Theo dõi) | Enumeration (Liệt kê) | Tùy chọn: Theo dõi Hoàn toàn (Completely Follow), Theo dõi Vị trí (Follow Location), Theo dõi Góc quay (Follow Rotation) |

## **3. Switch Follow Motion Device Target by Entity (Chuyển đổi Mục tiêu của Thiết bị Chuyển động Theo dõi theo Thực thể)**

![]()

**Node Functions (Chức năng Node)**

Chuyển đổi Mục tiêu Theo dõi của Thiết bị Chuyển động Theo dõi bằng Thực thể.

**Node Parameters (Tham số Node)**

| Input Parameter (Đầu vào) | Overwrite Level (Ghi đè Cấp độ) | Boolean (Logic) | Khi đặt thành False, tham số [Level] (Cấp độ) không có tác dụng |
| Input Parameter (Đầu vào) | Level (Cấp độ) | Integer (Số nguyên) | Xác định Cấp độ khi thực thể được tạo ra |
| Input Parameter (Đầu vào) | Unit Tag Index List (Danh sách Chỉ mục Thẻ Đơn vị) | Integer List (Danh sách Số nguyên) | Xác định các Thẻ Đơn vị được mang theo khi thực thể này được tạo |
| Output Parameter (Đầu ra) | Created Entity (Thực thể Được tạo) | Entity (Thực thể) | Thực thể này kế thừa các thuộc tính của Cấu hình mẫu Vật thể bay (Projectile Prefab) |

# XV. Special Effects (Hiệu ứng Đặc biệt)

## **1. Play Timed Effects (Phát Hiệu ứng Định giờ)**

![]()

![]()

**Node Functions (Chức năng Node)**

Phát một Hiệu ứng Định giờ (Timed Effect) liên quan đến Thực thể Mục tiêu. Bắt buộc phải có một Thực thể Mục tiêu và Điểm đính kèm (Attachment Point) hợp lệ.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Special Effects Asset (Tài sản Hiệu ứng Đặc biệt) | Config ID (ID Cấu hình) | Mã định danh cho Hiệu ứng này |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Nếu Thực thể không tồn tại, Hiệu ứng sẽ không phát |
| Input Parameter (Đầu vào) | Attachment Point Name (Tên Điểm Đính kèm) | String (Chuỗi) | Nếu Tên Điểm Đính kèm không tồn tại, Hiệu ứng Đặc biệt sẽ không phát |
| Input Parameter (Đầu vào) | Move With the Target (Di chuyển Cùng Mục tiêu) | Boolean (Logic) | Nếu đặt thành True, sẽ đi theo Chuyển động của Thực thể Mục tiêu |
| Input Parameter (Đầu vào) | Rotate With the Target (Xoay Cùng Mục tiêu) | Boolean (Logic) | Nếu đặt thành True, sẽ đi theo Góc quay của Thực thể Mục tiêu |
| Input Parameter (Đầu vào) | Location Offset (Độ lệch Vị trí) | 3D Vector | Độ lệch Vị trí so với Điểm Đính kèm được chỉ định của Thực thể Mục tiêu |
| Input Parameter (Đầu vào) | Rotation Offset (Độ lệch Góc quay) | 3D Vector | Độ lệch góc quay so với Điểm Đính kèm được chỉ định của Thực thể Mục tiêu |
| Input Parameter (Đầu vào) | Zoom Multiplier (Hệ số Thu phóng) | Floating Point Numbers (Số thực) | Hệ số Thu phóng của Hiệu ứng này |
| Input Parameter (Đầu vào) | Play Built-In Sound Effect (Phát Hiệu ứng Âm thanh Tích hợp) | Boolean (Logic) | Nếu đặt thành True, cũng sẽ phát Hiệu ứng Âm thanh Tích hợp |

## **2. Clear Special Effects Based on Special Effect Assets (Xóa các Hiệu ứng Đặc biệt Dựa trên Tài sản Hiệu ứng Đặc biệt)**

![]()

**Node Functions (Chức năng Node)**

Xóa tất cả các Hiệu ứng trên Thực thể Mục tiêu được chỉ định có sử dụng Tài sản Hiệu ứng đã cho. Chỉ áp dụng cho Hiệu ứng Vòng lặp (Looping Effects).

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể Đang hoạt động |
| Input Parameter (Đầu vào) | Special Effects Asset (Tài sản Hiệu ứng Đặc biệt) | Config ID (ID Cấu hình) | Mã định danh cho Hiệu ứng này |

## **3. Mount Looping Special Effect (Gắn Hiệu ứng Đặc biệt Vòng lặp)**

![]()

**Node Functions (Chức năng Node)**

Gắn một Hiệu ứng Vòng lặp liên quan đến Thực thể Mục tiêu. Bắt buộc phải có Thực thể Mục tiêu và Điểm Đính kèm hợp lệ.

Node này trả về một ID Phiên bản Hiệu ứng (Effect Instance ID) có thể được lưu trữ. Sau này, khi sử dụng node [Clear Looping Effects] (Xóa Hiệu ứng Vòng lặp), hãy sử dụng ID Phiên bản Hiệu ứng này để xóa Hiệu ứng Vòng lặp đã chỉ định.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Special Effects Asset (Tài sản Hiệu ứng Đặc biệt) | Config ID (ID Cấu hình) | Mã định danh cho Hiệu ứng này |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Nếu Thực thể không tồn tại, Hiệu ứng sẽ không phát |
| Input Parameter (Đầu vào) | Attachment Point Name (Tên Điểm Đính kèm) | String (Chuỗi) | Nếu Tên Điểm Đính kèm không tồn tại, Hiệu ứng Đặc biệt sẽ không phát |
| Input Parameter (Đầu vào) | Move With the Target (Di chuyển Cùng Mục tiêu) | Boolean (Logic) | Nếu đặt thành True, sẽ đi theo Chuyển động của Thực thể Mục tiêu |
| Input Parameter (Đầu vào) | Rotate With the Target (Xoay Cùng Mục tiêu) | Boolean (Logic) | Nếu đặt thành True, sẽ đi theo Góc quay của Thực thể Mục tiêu |
| Input Parameter (Đầu vào) | Location Offset (Độ lệch Vị trí) | 3D Vector | Độ lệch Vị trí so với Điểm Đính kèm được chỉ định của Thực thể Mục tiêu |
| Input Parameter (Đầu vào) | Rotation Offset (Độ lệch Góc quay) | 3D Vector | Độ lệch góc quay so với Điểm Đính kèm được chỉ định của Thực thể Mục tiêu |
| Input Parameter (Đầu vào) | Zoom Multiplier (Hệ số Thu phóng) | Floating Point Numbers (Số thực) | Hệ số Thu phóng của Hiệu ứng này |
| Input Parameter (Đầu vào) | Play Built-In Sound Effect (Phát Hiệu ứng Âm thanh Tích hợp) | Boolean (Logic) | Chuyển sang Yes để phát hiệu ứng âm thanh tích hợp |
| Output Parameter (Đầu ra) | Special Effect Instance ID (ID Phiên bản Hiệu ứng Đặc biệt) | Integer (Số nguyên) | ID Phiên bản tự động được tạo ra khi gắn Hiệu ứng này |

## **4. Clear Looping Special Effect (Xóa Hiệu ứng Đặc biệt Vòng lặp)**

![]()

**Node Functions (Chức năng Node)**

Xóa Hiệu ứng Vòng lặp đã chỉ định trên Thực thể Mục tiêu bằng ID Phiên bản Hiệu ứng. Sau khi gắn thành công, node [Mount Looping Effect] sẽ tạo ra một ID Phiên bản Hiệu ứng.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Special Effect Instance ID (ID Phiên bản Hiệu ứng Đặc biệt) | Integer (Số nguyên) | ID Phiên bản tự động được tạo bởi node Mount Looping Special Effect (Gắn Hiệu ứng Đặc biệt Vòng lặp) |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể Đang hoạt động |

# XVI. Timer (Đồng hồ hẹn giờ / Bộ định thời gian)

## **1. Resume Timer (Tiếp tục Bộ định thời gian)**

![]()

**Node Functions (Chức năng Node)**

Tiếp tục một Bộ định thời gian (Timer) đang tạm dừng trên Thực thể Mục tiêu.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể Đang hoạt động |
| Input Parameter (Đầu vào) | Timer Name (Tên Bộ định thời gian) | String (Chuỗi) | Mã định danh Bộ định thời gian |

## **2. Start Timer (Khởi động Bộ định thời gian)**

![]()

**Node Functions (Chức năng Node)**

Khởi động một Bộ định thời gian trên Thực thể Mục tiêu.

Bộ định thời gian được xác định duy nhất bằng tên của nó.

Bộ định thời gian bao gồm một Chuỗi Thời gian (Timer Sequence) có lặp lại hoặc không lặp lại. Chuỗi Thời gian là một tập hợp các mốc thời gian tính bằng giây được sắp xếp theo thứ tự tăng dần; khi Bộ định thời gian đạt đến các mốc này, nó sẽ kích hoạt sự kiện [On Timer Triggered] (Khi Bộ định thời gian Kích hoạt). Chiều dài tối đa của một Chuỗi Thời gian là 100.

Ví dụ: nếu bạn nhập Chuỗi Thời gian [1, 3, 5, 7], sự kiện [On Timer Triggered] sẽ kích hoạt ở các giây 1s, 3s, 5s và 7s.

Khi tính năng Vòng lặp (Loop) được đặt thành "Yes", Bộ định thời gian sẽ khởi động lại từ 0s sau khi đạt đến mốc thời gian cuối cùng. Đối với [1, 3, 5, 7], nó sẽ khởi động lại từ 0s sau khi đạt đến 7s.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể Đang hoạt động |
| Input Parameter (Đầu vào) | Timer Name (Tên Bộ định thời gian) | String (Chuỗi) | Mã định danh Bộ định thời gian |
| Input Parameter (Đầu vào) | Loop (Vòng lặp) | Boolean (Logic) | Nếu đặt thành True, Chuỗi Thời gian sẽ thực thi theo vòng lặp |
| Input Parameter (Đầu vào) | Timer Sequence (Chuỗi Thời gian) | Floating Point Number List (Danh sách Số thực) | Cung cấp danh sách được sắp xếp theo thứ tự tăng dần. Nếu danh sách không hợp lệ (không tăng dần một cách nghiêm ngặt, chứa số âm, v.v.), Bộ định thời gian sẽ không chạy |

## **3. Pause Timer (Tạm dừng Bộ định thời gian)**

![]()

**Node Functions (Chức năng Node)**

Tạm dừng Bộ định thời gian được chỉ định trên Thực thể Mục tiêu. Node [Resume Timer] (Tiếp tục Bộ định thời gian) sau đó có thể được sử dụng để tiếp tục quá trình đếm ngược.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể Đang hoạt động |
| Input Parameter (Đầu vào) | Timer Name (Tên Bộ định thời gian) | String (Chuỗi) | Mã định danh Bộ định thời gian |

## **4. Stop Timer (Dừng Bộ định thời gian)**

![]()

**Node Functions (Chức năng Node)**

Kết thúc hoàn toàn Bộ định thời gian được chỉ định trên Thực thể Mục tiêu; không thể tiếp tục được nữa.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể Đang hoạt động |
| Input Parameter (Đầu vào) | Timer Name (Tên Bộ định thời gian) | String (Chuỗi) | Mã định danh Bộ định thời gian |

# XVII. Global Timer (Bộ định thời gian Toàn cục)

## **1. Recover Global Timer (Khôi phục Bộ định thời gian Toàn cục)**

![]()

**Node Functions (Chức năng Node)**

Tiếp tục Bộ định thời gian Toàn cục đang tạm dừng trên Thực thể Mục tiêu.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể Đang hoạt động |
| Input Parameter (Đầu vào) | Timer Name (Tên Bộ định thời gian) | String (Chuỗi) | Mã định danh của Bộ định thời gian. Chỉ những Tên Bộ định thời gian được cấu hình trong Quản lý Bộ định thời gian (Timer Management) mới có thể được tham chiếu |

## **2. Start Global Timer (Khởi động Bộ định thời gian Toàn cục)**

![]()

**Node Functions (Chức năng Node)**

Khởi động một Bộ định thời gian Toàn cục trên Thực thể Mục tiêu.

Bộ định thời gian trên Thực thể Mục tiêu được xác định duy nhất bằng tên của nó.

Dựa trên cài đặt Quản lý Bộ định thời gian, Bộ định thời gian Đếm ngược (Countdown Timer) và Bấm giờ (Stopwatch Timer) sẽ được tạo tương ứng.

**Node Parameters (Tham số Node)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type (Loại)** | **Parameter Name (Tên tham số)** | **Type (Kiểu dữ liệu)** | **Description (Mô tả)** |
| Input Parameter (Đầu vào) | Target Entity (Thực thể Mục tiêu) | Entity (Thực thể) | Thực thể Đang hoạt động |
| Input Parameter (Đầu vào) | Timer Name (Tên Bộ định thời gian) | String (Chuỗi) | Mã định danh của Bộ định thời gian. Chỉ những Tên Bộ định thời gian được cấu hình trong Quản lý Bộ định thời gian mới có thể được tham chiếu |

## **3.** **Increase Global Timer Value (Tăng Giá trị Bộ định thời gian Toàn cục)**

![]()

**Node Functions (Chức năng Node)**

Điều chỉnh thời gian của Bộ định thời gian Toàn cục đang chạy thông qua Node Graph.

Nếu bộ định thời gian bị tạm dừng trước và sau đó được sửa đổi để giảm thời gian, thời gian đã sửa đổi sẽ ít nhất là 0 giây.

Đối với bộ đếm ngược (countdown timer), việc tạm dừng rồi chỉnh sửa thời gian thành 0s sẽ kích hoạt sự kiện [Khi Bộ định thời gian Toàn cục được Kích hoạt] (When the Global Timer Is Triggered) ngay sau khi tiếp tục bộ đếm ngược.

If the timer is paused first, then modified to 0s, followed by modifying the time to increase it, and finally resumed, the [When the Global Timer Is Triggered] event will not be triggered.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity | Active Entity |
| Input Parameter | Timer Name | String | Identifier for the Timer. Only Timer Names configured in Timer Management can be referenced |
| Input Parameter | Increase Value | Floating Point Numbers | For a Countdown Timer, a positive value increases the remaining time; a negative value decreases the remaining time  If the timer is set to Stopwatch, a positive value increases the accumulated time, while a negative value decreases it |

## **4. Pause Global Timer**

![]()

**Node Functions**

Pause a running Global Timer via the Node Graph

When paused, the UI controls linked to the timer will also pause their display

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity | Active Entity |
| Input Parameter | Timer Name | String | Identifier for the Timer. Only Timer Names configured in Timer Management can be referenced |

## **5. Stop Global Timer**

![]()

**Node Functions**

Use the node graph to stop running a global timer early

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity | Active Entity |
| Input Parameter | Timer Name | String | Identifier for the Timer. Only Timer Names configured in Timer Management can be referenced |

# XVIII. Camera

## **1. Switch Main Camera Template**

![]()

**Node Functions**

Switch the Main Camera Template for the target Player List to the specified Template

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Player List | Entity List | Active Player List |
| Input Parameter | Camera Template Name | String | Camera Template Identifier |

## **2. Set Player Camera to Follow Entity**

![]()

**Node Functions**

Set the specified Player Entity's camera to follow the target entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity | Active Player Entity |
| Input Parameter | Follow Entity | Entity | Camera Target Entity |
| Input Parameter | Camera Template Name | String | Camera Template Identifier |

## **3. Reset Player Camera to Follow Entity**

![]()

**Node Functions**

Reset the player camera to follow the Player Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity | Active Player Entity |

# XIX. Character Disruptor Device

## **1.** **Set Character Disruptor Device**

![]()

**Node Functions**

Edit the Character Disruptor Device active on the Target Entity by ID; if the ID does not exist, the Character Disruptor Device will no longer function after the modification

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity | Active Entity |
| Input Parameter | Device ID | Integer | Identifier for the Character Disruptor Device |

# XX. Unit Status

## **1. Add Unit Status**

![]()

**Node Functions**

Add a specified Stack Count of Unit Status to the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Applier Entity | Entity | Determines the Applier Entity for this action. Defaults to the Entity associated with this Node Graph |
| Input Parameter | Application Target Entity | Entity | The Entity that actually receives this Unit Status |
| Input Parameter | Unit Status Config ID | Config ID | Identifier for this Unit Status |
| Input Parameter | Applied Stacks | Integer | The Stack Count for this Unit Status |
| Input Parameter | Unit Status Parameter Dictionary | Dictionary | You can carry a set of parameters to override the configuration values in the unit's state. |
| Output Parameter | Application Result | Enumeration | Failed, other exceptions  Failed: Yielded to another status. A yielding relationship exists between the Target's current Unit Status and the one being applied  Failed: Maximum coexistence limit reached. The specified Unit Status on the Target Entity has reached its Coexistence Limit  Failed: Unable to add additional stack. Stack addition failed  Success: New status applied. Successfully applied new Unit Status  Success: Slot stacking. Target already has this Unit Status, stacking applied |
| Output Parameter | Slot ID | Integer | If application succeeds, returns the Unit Status Slot ID containing the instance |

## **2. Remove Unit Status**

![]()

**Node Functions**

Remove a specified Unit Status from the Target Entity. Either all stacks or a single stack can be removed

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Remove Target Entity | Entity | The Entity from which the Unit Status will be removed |
| Input Parameter | Unit Status Config ID | Config ID | Identifier for this Unit Status |
| Input Parameter | Removal Method | Enumeration | All Coexisting Statuses with the Same Name: Removes all statuses applied with this Config ID that share the same name  Status With Fastest Stack Loss: Removes one stack from the status that loses stacks the fastest |
| Input Parameter | Remover Entity | Entity | Determines the Remover Entity for this action. Defaults to the Entity associated with this Node Graph |

# XXI. Tabs

## **1. Activate/Disable Tab**

![]()

**Node Functions**

Edit the Tab state by ID in the Target Entity's Tab Component

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity | Active Entity |
| Input Parameter | Tab ID | Integer | Identifier for the Tab |
| Input Parameter | Activate | Boolean | If set to True, it is active and can be selected |

# XXII. Collision Trigger Source

## **1. Activate/Disable Collision Trigger Source**

![]()

**Node Functions**

Edit the state of the Collision Trigger Source Component on the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity | Active Entity |
| Input Parameter | Activate | Boolean | If set to True, activates collision with Entities that carry Collision Trigger Components |

# XXIII. Class

## **1. Change Player's Current Class Level**

![]()

**Node Functions**

Set the Player's current Class Level. If it exceeds the defined range, the change will not take effect

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Player | Entity | Active Player Entity |
| Input Parameter | Level | Integer | Edited Level |

## **2. Change Player Class**

![]()

**Node Functions**

Set the Player's current Class to the Class referenced by the Config ID and process the Player's existing skills

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Player | Entity | Active Player Entity |
| Input Parameter | Class Config ID | Config ID | Class Identifier |
| Input Parameter | Existing Skill Handling | Enumeration | Clear All: Clear all existing skills  Preserve Unrelated Skills: Retain skills that are not defined in the default skill sets of either the previous or the new class |

## **3. Increase Player's Current Class EXP**

![]()

**Node Functions**

Increase the Player's current Class EXP. Any excess beyond the maximum Level will not take effect

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Player | Entity | Active Player Entity |
| Input Parameter | EXP | Integer | Amount of EXP to be increased |

# XXIV. UI Control Groups

## **1. Activate UI Control Group in Control Group Library**

![]()

**Node Functions**

Activate the UI Control Groups stored as Custom Templates in the UI Control Group Library within the Target Player's Interface Layout

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Player | Entity | Active Player Entity |
| Input Parameter | UI Control Group Index | Integer | Identifier for the UI Control Group |

## **2. Switch Current Interface Layout**

![]()

**Node Functions**

Switch the Target Player's current Interface Layout via Layout ID

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Player | Entity | Active Player Entity |
| Input Parameter | Layout Index | Integer | Identifier for the UI Layout |

## **3.** Set UI Control (Group) Status

![]()

**Node Functions**

Edit the state of the UI Control in the Target Player's Interface Layout by its UI Control ID

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Player | Entity | Active Player Entity |
| Input Parameter | UI Control Group Index | Integer | Identifier for the UI Control |
| Input Parameter | Display Status | Enumeration | Off: Invisible and logic not running  On: Visible and logic running normally  Hidden: Invisible and logic running normally |

## **4.** Remove Interface Control Group From Control Group Library

![]()

**Node Functions**

Remove the UI Control Groups activated via [Activate UI Control Group in Control Group Library] from the Target Player's Interface Layout

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Player | Entity | Active Player Entity |
| Input Parameter | UI Control Group Index | Integer | Identifier for the UI Control Group |

## **5.** Play UI Animation on Control

![]()

**Node Functions**

Plays the VFX asset mounted to this UI animation control in the Player Entity's Interface Layout. To hide or disable the VFX, use the [Set UI Control (Group) Status] node. If this node is executed multiple times, the VFX can be played multiple times as well.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity | Active Player Entity |
| Input Parameter | Special Effect Control Index | Integer | Identifier for the UI Control/Fullscreen UI Control to Play the Animation on |

## **6. Refresh Notification Queue**

![]()

**Node Functions**

The Notification Queue UI Control allows for the transmission of a given set of data to be displayed via a node graph. Once transmitted, the data will be displayed in the specified Notification Queue UI Control according to the graphic-text group template entered

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Emtity |  |
| Input Parameter | Notification Queue Index | Integer |  |
| Input Parameter | Notification Item ID | Integer |  |
| Input Paraneter | Notification Queue Data | Generic |  |

# XXV. Skills

## **1.** Set Skill CD Based on Maximum CD Percentage

![]()

**Node Functions**

Modify the skill in a character's skill slot by adjusting the percentage of the skill's maximum cooldown time.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity | Active Character Entity |
| Input Parameter | Character Skill Slot | Enumeration | The Skill Slot to edited: Normal Attack, Skill 1-E, Skill 2-Q, Skill 3-R, Skill 4-T, or Custom Skill |
| Input Parameter | Ratio Value | Floating Point Numbers | The revised actual cooldown time is: original cooldown time \* ratio value |
| Input Parameter | Limit Maximum CD Time | Boolean | If set to True, the edited Cooldown cannot be less than the specified minimum value |

## **2. Initialize Character Skill**

![]()

**Node Functions**

Reset the Target Character's skills to those defined in the Class Template

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity | Active Character Entity |
| Input Parameter | Character Skill Slot | Enumeration | The Skill Slot to initialize: Normal Attack, Skill 1-E, Skill 2-Q, Skill 3-R, Skill 4-T, or Custom Skill |

## **3. Set Skill Resource Amount**

![]()

**Node Functions**

Edit the Character's skill resource amount

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity | Active Character Entity |
| Input Parameter | Skill Resource Config ID | Config ID | Skill Resource Identifier |
| Input Parameter | Target Value | Floating Point Numbers | Edited value will be set to this input value |

## **4.** Set Character Skill CD

![]()

**Node Functions**

Directly set the cooldown time of a specific skill slot on the target character to a specified value.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity | Active Character Entity |
| Input Parameter | Character Skill Slot | Enumeration | The Skill Slot to edited: Normal Attack, Skill 1-E, Skill 2-Q, Skill 3-R, Skill 4-T, or Custom Skill |
| Input Parameter | CD Time | Floating Point Numbers | Edited Cooldown will be set to this input value |
| Input Parameter | Limit Maximum CD Time | Boolean | If set to True, the edited Cooldown cannot be less than the specified minimum value |

## **5. Add Character Skill**

![]()

**Node Functions**

Add a skill to the specified Target Character's Skill Slot

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity | Active Character Entity |
| Input Parameter | Skill Config ID | Config ID | Skill Identifier |
| Input Parameter | Skill Slot | Enumeration | The Skill Slot to be added: Normal Attack, Skill 1-E, Skill 2-Q, Skill 3-R, Skill 4-T, or Custom Skill |
| Input Parameter | Original Slot Skill Handling | Enumeration | Destroy: Remove the original skill  Preserve Slot Binding: Retain the current slot binding. When the newly bound skill instance is removed, it is automatically displayed in that slot  Remove Slot Binding: The skill must be reassigned to the specified slot in order to be displayed in that slot |
| Output Parameter | Switched Skill Instance ID | Integer |  |

## **6.** Increase Skill Resource Amount

![]()

**Node Functions**

Modifying the resource amount of a skill will add an increase to the current value; this increase can be a negative number.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity | Active Character Entity |
| Input Parameter | Skill Resource Config ID | Config ID | Skill Resource Identifier |
| Input Parameter | Increase Value | Floating Point Numbers | The modified value is: original value + increase value. |

## **7.** Increase Character Skill CD

![]()

**Node Functions**

Modifying the cooldown of a target character's skill slot will add an increase to the current cooldown time; this increase can be a negative number.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity | Active Character Entity |
| Input Parameter | Character Skill Slot | Enumeration | The Skill Slot to be edited: Normal Attack, Skill 1-E, Skill 2-Q, Skill 3-R, Skill 4-T, or Custom Skill |
| Input Parameter | CD Time Increase Value | Floating Point Numbers | The modified value is: original value + increase value. |
| Input Parameter | Limit Maximum CD Time | Boolean | If set to True, the edited Cooldown cannot be less than the specified minimum value |

## **8. Delete Character Skill by Slot**

![]()

**Node Functions**

Delete the skill in the specified slot of the Target Character

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity | Active Character Entity |
| Input Parameter | Character Skill Slot | Enumeration | The Skill Slot to be deleted: Normal Attack, Skill 1-E, Skill 2-Q, Skill 3-R, Skill 4-T, or Custom Skill |

## **9. Delete Character Skill by ID**

![]()

**Node Functions**

Iterate through and delete all skills with the specified Config ID across all of the Character's slots

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity | Active Character Entity |
| Input Parameter | Skill Config ID | Config ID | Skill Identifier |

## **10. Bind Custom Skill Instance to Specified Slo**t

![]()

**Node Functions**

Bind the specified skill instance to the specified skill slot

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity | Active Character Entity |
| Input Parameter | Skill Instance ID | Integer | Identifier for the Skill Instance |
| Input Parameter | Skill Slot | Enumeration |  |
| Input Parameter | Original Slot Skill Handling | Enumeration | Destroy: Remove the original skill  Preserve Slot Binding: Retain the current slot binding. When the newly bound skill instance is removed, it is automatically displayed in that slot  Remove Slot Binding: The skill must be reassigned to the specified slot in order to be displayed in that slot |
| Output Parameter | Original Slot Skill Instance ID | Integer |  |

## **11. Unbind Skill Instance**

![]()

**Node Functions**

Unbind the specified skill instance from the Character Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Character Entity | Entity | Active Character Entity |
| Input Parameter | Skill Instance ID | Integer | Identifier for the Skill Instance |

## **12. Unbind all Skill Instances on the Slot**

![]()

**Node Functions**

Unbind all skill instances on the specified slot of the Character Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Character Entity | Entity | Active Character Entity |
| Input Parameter | Specified Slot | Enumeration |  |
| Output Parameter | Unbound Skill Instance ID List | Integer List | List of skill instance IDs unbound from the slot |

## **13. Create Custom Skill Instance**

![]()

**Node Functions**

Create a skill instance from the specified config ID for the Character Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Character Entity | Entity | Active Character Entity |
| Input Parameter | Skill Config ID | Config ID | Skill Identifier |
| Output Parameter | Skill Instance ID | Integer | Identifier for the Skill Instance |

## **14. Destroy Custom Skill Instance**

![]()

**Node Functions**

Destroy the specified skill instance on the Character Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Character Entity | Entity | Active Character Entity |
| Input Parameter | Skill Instance ID | Integer | Identifier for the Skill Instance |

## **15. Cast Skill From Specified Panel Slot**

![]()

**Node Functions**

Cast the skill currently active in the specified skill slot on the Character Entity

This input works only if the skill is bound to a button and is currently active

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Character Entity | Entity | Active Character Entity |
| Input Parameter | Skill Slot | Enumeration |  |
| Input Parameter | Check Key Availability | Boolean | Yes: Cast only when the key is available  No: Cast even if the key is not available |

## **16. Cast Specified Skill Instance**

![]()

**Node Functions**

Cast the skill corresponding to the specified skill instance ID on the Character Entity

This input works only if the skill is bound to a button and is currently active

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Character Entity | Entity | Active Character Entity |
| Input Parameter | Skill Instance ID | Integer | Identifier for the Skill Instance |
| Input Parameter | Check Key Availability | Boolean | Yes: Cast only when the key is available  No: Cast even if the key is not available |

# XXVI. Sound Effects

## **1. Adjust Player Background Music Volume**

![]()

**Node Functions**

Adjust Player Background Music Volume

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity | Active Player Entity |
| Input Parameter | Volume | Integer |  |

## **2. Adjust Specified Sound Effect Player**

![]()

**Node Functions**

Adjust the volume and playback speed of the Sound Effect Player with the specified ID in the Sound Effect Player Component on the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | SFX Player ID | Integer |  |
| Input Parameter | Volume | Integer |  |
| Input Parameter | Playback Speed | Floating Point Numbers |  |

## **3. Close Specified Sound Effect Player**

![]()

**Node Functions**

Disable the Sound Effect Player with the specified ID in the Sound Effect Player Component on the specified Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | SFX Player ID | Integer |  |

## **4. Start/Pause Player Background Music**

![]()

**Node Functions**

Edit the background music state for the specified Player

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity | Active Player Entity |
| Input Parameter | Recover | Boolean |  |

## **5. Start/Pause Specified Sound Effect Player**

![]()

**Node Functions**

Edit the state of the Sound Effect Player with the specified ID in the Sound Effect Player Component on the Target Entity. This node is only active when the sound effect is set to loop playback. It does not take effect for sound effects configured for single-playback.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | SFX Player ID | Integer |  |
| Input Parameter | Recover | Boolean |  |

## **6. Add Sound Effect Player**

![]()

![]()

**Node Functions**

Dynamically add a Sound Effect Player. The Unit must have a Sound Effect Player Component

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Sound Effect Asset Index | Integer |  |
| Input Parameter | Volume | Integer |  |
| Input Parameter | Playback Speed | Floating Point Numbers |  |
| Input Parameter | Loop Playback | Boolean |  |
| Input Parameter | Loop Interval Time | Floating Point Numbers |  |
| Input Parameter | 3D Sound Effect | Boolean |  |
| Input Parameter | Range Radius | Floating Point Numbers |  |
| Input Parameter | Attenuation Mode | Enumeration |  |
| Input Parameter | Attachment Point Name | String |  |
| Input Parameter | Attachment Point Offset | 3D Vector |  |
| Output Parameter | SFX Player ID | Integer |  |

## **7. Player Plays One-Shot 2D Sound Effect**

![]()

**Node Functions**

Player plays a one-shot 2D Sound Effect

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity | Active Player Entity |
| Input Parameter | Sound Effect Asset Index | Integer |  |
| Input Parameter | Volume | Integer |  |
| Input Parameter | Playback Speed | Floating Point Numbers |  |

## **8.** Set Player Background Music

![]()

![]()

**Node Functions**

Set player background music parameters

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity | Active Player Entity |
| Input Parameter | Background Music Index | Integer |  |
| Input Parameter | Start Time | Floating Point Numbers |  |
| Input Parameter | End Time | Floating Point Numbers |  |
| Input Parameter | Volume | Integer |  |
| Input Parameter | Loop Playback | Boolean |  |
| Input Parameter | Loop Interval | Floating Point Numbers |  |
| Input Parameter | Playback Speed | Floating Point Numbers |  |
| Input Parameter | Enable Fade In/Out | Boolean |  |

# XXVII. Unit Tags

## **1. Clear Unit Tags from Entity**

![]()

**Node Functions**

Clear Unit Tags for the specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |

## **2. Add Unit Tag to Entity**

![]()

**Node Functions**

Add Unit Tags to the specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Unit Tag Index | Integer |  |

## **3. Remove Unit Tag from Entity**

![]()

**Node Functions**

Remove Unit Tags from the specified Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Unit Tag Index | Integer |  |

# XXVIII. Custom Aggro

## **1. Taunt Target**

![]()

**Node Functions**

Available only in Custom Aggro Mode

Make the Taunter Entity taunt the specified Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Taunter Entity | Entity |  |
| Input Parameter | Target Entity | Entity |  |

## **2. Remove Target Entity From Aggro List**

![]()

**Node Functions**

Available only in Custom Aggro Mode

Remove the Target Entity from the Aggro Owner's Aggro List; this may cause the target to leave battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Aggro Owner Entity | Entity |  |

## **3. Clear Specified Target's Aggro List**

![]()

**Node Functions**

Available only in Custom Aggro Mode

Clear the Aggro Owner's Aggro List. This may cause them to leave battle

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Aggro Owner | Entity |  |

## **4. Set the Aggro Value of Specified Entity**

![]()

**Node Functions**

Available only in Custom Aggro Mode

Set the Aggro Value of the specified Target Entity on the specified Aggro Owner

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Aggro Owner Entity | Entity |  |
| Input Parameter | Aggro Value | Integer |  |

# XXIX. Signals

## **1. Send Signal**

![]()

**Node Functions**

Send a custom Signal to the global Stage. Before use, select the corresponding Signal name to ensure correct parameter usage

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
|  |  |  |  |

# XXX. Nameplate

## **1. Set Entity Active Nameplate**

![]()

**Node Functions**

Set the active Nameplate list for the specified target. Nameplates included in the input list are enabled, while those not included are disabled

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Nameplate Config ID List | Config ID List |  |

# XXXI. Text Bubbles

## **1. Switch Active Text Bubble**

![]()

**Node Functions**

In the Target Entity's Text Bubble Component, replace the current active Text Bubble with the one corresponding to the Config ID

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Text Bubble Configuration ID | Config ID |  |

# XXXII. Deck Selector

## **1. Close Deck Selector**

![]()

**Node Functions**

Close the currently active Deck Selector for the specified Player

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Player | Entity | Active Player Entity |
| Input Parameter | Deck Selector Index | Integer |  |

## **2. Invoke Deck Selector**

![]()

**Node Functions**

Open the pre-made Deck Selector for the Target Player

**Node Parameters**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** | |
| Input Parameter | Target Player | Entity | Specify the runtime Player to invoke the Deck Selector | |
| Input Parameter | Deck Selector ID | Integer | Referenced UI Control Group ID | |
| Input Parameter | Select Duration | Floating Point Numbers | If empty, uses the Deck Selector's default configuration; otherwise, this time value is used as the effective duration  Unit in seconds. If the duration exceeds 2,000,000 seconds, it can no longer be invoked | |
| Input Parameter | Select Result Corresponding List | Integer List | One-to-one with display items: the Deck Selector returns the result value corresponding to each display item  Recommended configuration: 1 to X | |
| Input Parameter | Select Display Corresponding List | Integer List | Deck Library Configuration Reference | |
| Input Parameter | Select Minimum Quantity | Integer | The minimum number of cards that must be selected for a valid interaction | |
| Input Parameter | Select Maximum Quantity | Integer | The maximum number of cards that can be selected for a valid interaction | |
| Input Parameter | Refresh Mode | Enumeration | Cannot Refresh: Both input parameters (Refresh Maximum Quantity and Refresh Maximum Quantity) are ignored, and the selection screen has no refresh button  Partial Refresh: Both input parameters (Refresh Maximum Quantity and Refresh Maximum Quantity) take effect, and the selection screen includes a refresh button  Refresh All: Both input parameters (Refresh Maximum Quantity and Refresh Maximum Quantity) are ignored. All results are returned by default, and the selection screen includes a refresh button | |
| Input Parameter | Refresh Minimum Quantity | Integer | The minimum number of cards that must be selected for a valid refresh interaction. | |
| Input Parameter | Refresh Maximum Quantity | Integer | The maximum number of cards that can be selected for a valid refresh interaction | |
| Input Parameter | Default Return Selection | Integer List | If the Deck Selector times out, has no interaction, or closes abnormally, force-assign this configured result  The length of this Result List must match the valid card selection count | |

## **3. Random Deck Selector Selection List**

![]()

**Node Functions**

Randomly sort the input List

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Select List | Integer List |  |

# XXXIII. Stage Settlement

## **1. Set Player Settlement Success Status**

![]()

**Node Functions**

Set Player Settlement Success Status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |
| Input Parameter | Settlement Status | Enumeration | Three types: Undefined, Victory, Defeat |

## **2. Set Player Settlement Scoreboard Data Display**

![]()

**Node Functions**

Set the Player's Scoreboard display data, which is shown on the Scoreboard after Stage Settlement. Since this node involves the display of external functions, [Data Value] and [Data Name] currently support multilingual translation only when manually entering text. If entered via connection input, multilingual translation is not supported.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Set Entity | Entity | Active Player Entity |
| Input Parameter | Data Order | Integer | The sort order of this data |
| Input Parameter | Data Name | String | The name of this data |
| Input Parameter | Data Value | Generic | The value of this data. Supports Integer, Floating Point Number, and String |

## **3. Set Player Settlement Ranking Value**

![]()

**Node Functions**

Set the Player's ranking value after Settlement, then determine the final ranking order according to [Ranking Value Comparison Order] in [Stage Settings] – [Settlement]

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |
| Input Parameter | Ranking Value | Integer |  |

## **4. Set Faction Settlement Success Status**

![]()

**Node Functions**

Set Faction Settlement Success Status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Faction | Faction | Active Faction Entity |
| Input Parameter | Settlement Status | Enumeration | Three types: Undefined, Victory, Defeat |

## **5. Set Faction Settlement Ranking Value**

![]()

**Node Functions**

Set the faction's ranking value after Settlement, then determine the final ranking order according to [Ranking Value Comparison Order] in [Stage Settings] – [Settlement]

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Faction | Faction | Active Faction Entity |
| Input Parameter | Ranking Value | Integer |  |

# XXXIV. Light Source Components

## **1. Toggle Entity Light Source**

![]()

**Node Functions**

Adjust the Light Source state at the specified ID in the Light Source Component on the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Light Source ID | Integer |  |
| Input Parameter | Enable or Disable | Boolean | If set to True, turns On |

# XXXV. Dictionary

## **1. Sort Dictionary by Key**

![]()

**Node Functions**

Sort and output the specified Dictionary by keys in ascending or descending order

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Sort By | Enumeration |  |
| Output Parameter | Key List | Generic |  |
| Output Parameter | Value List | Generic |  |

## **2. Sort Dictionary by Value**

![]()

**Node Functions**

Sort and output the specified Dictionary by values in ascending or descending order

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Sort By | Enumeration |  |
| Output Parameter | Key List | Generic |  |
| Output Parameter | Value List | Generic |  |

## **3. Set or Add Key Value Pairs to Dictionary**

![]()

**Node Functions**

Add a Key-Value Pair to the specified Dictionary

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Key | Generic |  |
| Input Parameter | Value | Generic |  |

## **4. Clear Dictionary**

![]()

**Node Functions**

Clear all Key-Value Pairs from the specified Dictionary

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |

## **5. Remove Key Value Pairs from Dictionary by Key**

![]()

**Node Functions**

Remove Key-Value Pairs from the specified Dictionary by key

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dictionary | Generic |  |
| Input Parameter | Key | Generic |  |

# XXXVI. Structures

## **1. Modify Structure**

![]()

**Node Functions**

After selecting a Structure, you can edit each parameter of that Structure

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Structure |  |  |

# XXXVII. Shop

## **1.** Remove Item From Inventory Shop Sales List

![]()

**Node Functions**

Remove items from the inventory shop's sales list

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Shop Owner Entity | Entity |  |
| Input Parameter | Shop ID | Integer | The Shop ID corresponding to the Shop component on the Shop Owner Entity |
| Input Parameter | Item Config ID | Config ID |  |

## **2. Remove Item From Purchase List**

![]()

**Node Functions**

Remove items from the purchase list

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Shop Owner Entity | Entity |  |
| Input Parameter | Shop ID | Integer | The Shop ID corresponding to the Shop component on the Shop Owner Entity |
| Input Parameter | Shop Item Config ID | Config ID |  |

## **3.** Remove Item From Custom Shop Sales List

![]()

**Node Functions**

Remove items from the custom shop's sales list

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Shop Owner Entity | Entity |  |
| Input Parameter | Shop ID | Integer | The Shop ID corresponding to the Shop component on the Shop Owner Entity |
| Input Parameter | Shop Item ID | Integer |  |

## **4. Open Shop**

![]()

**Node Functions**

Open the Shop from the Player Entity's perspective during gameplay

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |
| Input Parameter | Shop Owner Entity | Entity | The Shop ID corresponding to the Shop component on the Shop Owner Entity |
| Input Parameter | Shop ID | Integer |  |

## **5. Close Shop**

![]()

**Node Functions**

Close all open Shops from the Player Entity's perspective during gameplay

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |

## **6.** Add New Item to Inventory Shop Sales List

![]()

**Node Functions**

Add new items to the inventory shop's sales list

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Shop Owner Entity | Entity |  |
| Input Parameter | Shop ID | Integer | The Shop ID corresponding to the Shop component on the Shop Owner Entity |
| Input Parameter | Shop Item Config ID | Config ID |  |
| Input Parameter | Sell Currency Dictionary | Dictionary |  |
| Input Parameter | Affiliated Tab ID | Integer | 1 Equipment, 2 Consumables, 3 Materials, 4 Valuables |
| Input Parameter | Sort Priority | Integer |  |
| Input Parameter | Can Be Sold | Boolean |  |

## **7. Add Items to the Purchase List**

![]()

**Node Functions**

Add New Items to the Item Purchase List

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Shop Owner Entity | Entity |  |
| Input Parameter | Shop ID | Integer | The Shop ID corresponding to the Shop component on the Shop Owner Entity |
| Input Parameter | Shop Item Config ID | Config ID |  |
| Input Parameter | Purchase Currency Dictionary | Dictionary |  |
| Input Parameter | Purchasable | Boolean |  |

## **8.** Add New Item to Custom Shop Sales List

![]()

**Node Functions**

Add items to the Custom Shop Sales List. Upon success, an Integer ID is generated in the Output Parameter as the item identifier

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Shop Owner Entity | Entity |  |
| Input Parameter | Shop ID | Integer | The Shop ID corresponding to the Shop component on the Shop Owner Entity |
| Input Parameter | Shop Item Config ID | Config ID |  |
| Input Parameter | Sell Currency Dictionary | Dictionary |  |
| Input Parameter | Affiliated Tab ID | Integer | 1 Equipment, 2 Consumables, 3 Materials, 4 Valuables |
| Input Parameter | Limit Purchase | Boolean |  |
| Input Parameter | Purchase Limit | Integer |  |
| Input Parameter | Sort Priority | Integer |  |
| Input Parameter | Can Be Sold | Boolean |  |
| Output Parameter | Item Index | Integer |  |

## **9.** Set Inventory Shop Item Sales Info

![]()

**Node Functions**

Set up information on items for sale in the inventory shop.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Shop Owner Entity | Entity |  |
| Input Parameter | Shop ID | Integer | The Shop ID corresponding to the Shop component on the Shop Owner Entity |
| Input Parameter | Item Config ID | Config ID |  |
| Input Parameter | Sell Currency Dictionary | Dictionary |  |
| Input Parameter | Affiliated Tab ID | Integer |  |
| Input Parameter | Sort Priority | Integer |  |
| Input Parameter | Can Be Sold | Boolean |  |

## **10.** Set Item Purchase Info in the Purchase List

![]()

**Node Functions**

Set up item acquisition table

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Shop Owner Entity | Entity |  |
| Input Parameter | Shop ID | Integer | The Shop ID corresponding to the Shop component on the Shop Owner Entity |
| Input Parameter | Shop Item Config ID | Config ID |  |
| Input Parameter | Purchase Currency Dictionary | Dictionary |  |
| Input Parameter | Purchasable | Boolean |  |

## **11.** Set Custom Shop Item Sales Info

![]()

![]()

**Node Functions**

Set custom store product sales information

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Shop Owner Entity | Entity |  |
| Input Parameter | Shop ID | Integer | The Shop ID corresponding to the Shop component on the Shop Owner Entity |
| Input Parameter | Shop Item ID | Integer |  |
| Input Parameter | Item Config ID | Config ID |  |
| Input Parameter | Sell Currency Dictionary | Dictionary |  |
| Input Parameter | Affiliated Tab ID | Integer | 1 Equipment, 2 Consumables, 3 Materials, 4 Valuables |
| Input Parameter | Limit Purchase | Boolean |  |
| Input Parameter | Purchase Limit | Integer |  |
| Input Parameter | Sort Priority | Integer |  |
| Input Parameter | Can Be Sold | Boolean |  |

# XXXVIII. Equipment

## **1.** Set Equipment Affix Value

![]()

**Node Functions**

Sets the value on the corresponding entry for a specified equipment instance.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Equipment Index | Integer | Integer ID generated during Equipment Initialization to identify the equipment instance |
| Input Parameter | Affix ID | Integer | Each ID corresponds to one single Affix |
| Input Parameter | Affix Value | Floating Point Numbers |  |

## **2. Remove Equipment Affix**

![]()

**Node Functions**

Remove the specified Affix from the Equipment instance

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Equipment ID | Integer | Integer ID generated during Equipment Initialization to identify the equipment instance |
| Input Parameter | Affix ID | Integer |  |

## **3. Add Affix to Equipment**

![]()

**Node Functions**

Add a preconfigured Affix to the specified Equipment instance, with the option to overwrite the Affix value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Equipment ID | Integer | Integer ID generated during Equipment Initialization to identify the equipment instance |
| Input Parameter | Affix Config ID | Config ID | The Config ID of the preconfigured Affix defined in Equipment Data Management |
| Input Parameter | Overwrite Affix Value | Boolean |  |
| Input Parameter | Affix Value | Floating Point Numbers | Can overwrite the value on a pre-configured Affix |

## **4. Add Affix to Equipment at Specified ID**

![]()

**Node Functions**

Add a preconfigured Affix at the specified Affix ID on the Equipment instance, with the option to overwrite the Affix value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Equipment ID | Integer | Integer ID generated during Equipment Initialization to identify the equipment instance |
| Input Parameter | Affix Config ID | Config ID | The Config ID of the preconfigured Affix defined in Equipment Data Management |
| Input Parameter | Insert ID | Integer |  |
| Input Parameter | Overwrite Affix Value | Boolean |  |
| Input Parameter | Affix Value | Floating Point Numbers | Can overwrite the value on a pre-configured Affix |

## **5. Replace Equipment to the Specified Slot**

![]()

**Node Functions**

Replaces the specified equipment in the corresponding equipment slot of the target entity.

If the equipment is already equipped in the equipment slot, the replacement will not take effect.  
  
If the target slot already contains an equipped item, that item will be replaced.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Equipment Row | Integer |  |
| Input Parameter | Equipment Column | Integer |  |
| Input Parameter | Equipment Index | Integer | The equipment instance is identified by an integer index generated during equipment initialization. |

## **6. Remove Equipment from Specified Slot**

![]()

**Node Functions**

Remove the equipment from the specified slot (by row and column)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Equipment Slot Owner Entity | Entity |  |
| Input Parameter | Equipment Slot Row Count | Integer |  |
| Input Parameter | Equipment Slot Column Count | Integer |  |

# XXXIX. Items and Inventory

## **1. Set Inventory** Item Drop Contents

![]()

**Node Functions**

Configure the Inventory Item drop data in Dictionary format, and specify the Drop Type

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Inventory Owner Entity | Entity |  |
| Input Parameter | Item Drop Dictionary | Dictionary |  |
| Input Parameter | Loot Type | Enumeration | Types: Shared Reward (one share for all), Individualized Reward (one share per person) |

## **2.** Set Inventory Drop Items/Currency Amount

![]()

**Node Functions**

Set the type and quantity of Items or Currency for the Inventory drop

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Inventory Owner Entity | Entity |  |
| Input Parameter | Item/Currency Config ID | Config ID |  |
| Input Parameter | Quantity Dropped | Integer |  |
| Input Parameter | Loot Type | Enumeration | Types: Shared Reward (one share for all), Individualized Reward (one share per person) |

## **3. Trigger Loot Drop**

![]()

**Node Functions**

Triggers a loot drop for the dropper entity, with configurable loot type.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dropper Entity | Entity |  |
| Input Parameter | Loot Type | Enumeration | Types: Shared Reward (one share for all), Individualized Reward (one share per person) |

## **4. Set Loot Drop Content**

![]()

**Node Functions**

Configure the Loot drop data in the Loot Component on the Dropper Entity in Dictionary format

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Dropper Entity | Entity |  |
| Input Parameter | Loot Drop Dictionary | Dictionary |  |

## **5.** Increase Inventory Item Quantity

![]()

**Node Functions**

Modifying the quantity of a specified item in your inventory will add an increase to the current value; the increase can be a negative number.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Inventory Owner Entity | Entity |  |
| Input Parameter | Item Config ID | Config ID |  |
| Input Parameter | Increase Value | Integer | The changed value = original value + increase value |

## **6. Increase Inventory Currency Quantity**

![]()

**Node Functions**

Modify the amount of a specified currency in the player's inventory. This will add the specified increase value to the current amount, and the increase value can be negative.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Inventory Owner Entity | Entity |  |
| Input Parameter | Currency Config ID | Config ID |  |
| Input Parameter | Increase Value | Integer | The changed value = original value + increase value |

## **7. Increase Loot Component Item Quantity**

![]()

**Node Functions**

Modify the quantity of a specified item in the drop component of a loot prefab. This will add the specified increase value to the current quantity, and the increase value can be negative.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Loot Entity | Entity |  |
| Input Parameter | Item Config ID | Config ID |  |
| Input Parameter | Increase Value | Integer | The changed value = original value + increase value |

## **8. Increase Loot Component Currency Quantity**

![]()

**Node Functions**

Modify the amount of a specified currency in the drop component of a loot prefab. This will add the specified increase value to the current amount, and the increase value can be negative.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Loot Entity | Entity |  |
| Input Parameter | Currency Config ID | Config ID |  |
| Input Parameter | Increase Value | Integer | The changed value = original value + increase value |

## **9. Increase Maximum Inventory Capacity**

![]()

**Node Functions**

Increase the maximum Inventory capacity of the specified Inventory Owner

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Inventory Owner Entity | Entity |  |
| Input Parameter | Increase Capacity | Integer |  |

# XL. Mini-Map Marker Component

## **1. Set Player List for Visible Mini-Map Markers**

![]()

**Node Functions**

The mini-map marker at the specified ID in the Target Entity's Mini-map Marker Component is visible to all Players in the Player List

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity | Entity that owns the Mini-map Marker component to be edited |
| Input Parameter | Mini-Map Marker ID | Integer | ID of the specified Mini-map Marker to be edited |
| Input Parameter | Player List | Entity List | The specified Mini-map ID on the Target Entity, visible only to the Player providing input |

## **2. Set Player Markers on the Mini-Map**

![]()

**Node Functions**

When the Player Marker option is selected and a corresponding Player Entity is linked in the Node Graph, the Target Entity's display on the mini-map changes to that Player's avatar

![]()

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity | Entity that owns the Mini-map Marker component to be edited |
| Input Parameter | Mini-Map Marker ID | Integer | ID of the specified Mini-map Marker to be edited |
| Input Parameter | Corresponding Player Entity | Entity | Changes the avatar of the corresponding Player Entity |

## **3. Set Mini-Map Marker Activation Status**

![]()

**Node Functions**

Edit the active state of mini-map markers on the Target Entity in batches using the input list of Mini-map Marker IDs

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity | Entity that owns the Mini-map Marker component to be edited |
| Input Parameter | Mini-Map Marker ID List | Integer List | List of Mini-map Marker IDs to be set to the specified status  Unconfigured Mini-map Markers will be set to the opposite status |
| Input Parameter | Active | Boolean | If input is True,  the Mini-map Markers corresponding to the specified ID numbers in the input list will be set to Enabled  For IDs not in the input list, the corresponding Mini-map Markers will be set to Disabled |

## **4. Set Mini-Map Zoom**

![]()

**Node Functions**

Set the map scale of the mini-map interface control for the target player.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Player | Entity |  |
| Input Parameter | Zoom Dimensions | Floating Point Numbers |  |

## **5. Set Player List for Tracking Mini-Map Markers**

![]()

**Node Functions**

Set the mini-map marker of the target entity with the corresponding index to a tracking appearance for the specified player.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Mini-Map Marker ID | Integer |  |
| Input Parameter | Player List | Entity List |  |

## **6. Switch Custom Maps**

![]()

**Node Functions**

Allows switching the Target Player's currently active minimap configuration

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Player | Entity |  |
| Input Parameter | Map Config ID | Config ID |  |
| Input Parameter | Display Map? | Boolean | Toggle Yes to display map |

# XLI. Creation Patrol

## **1. Switch Creation Patrol Template**

![]()

**Node Functions**

Immediately switch the patrol template for the Creation and move according to the new template

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Creation Entity | Entity |  |
| Input Parameter | Patrol Template ID | Integer |  |

# XLII. Leaderboard

## **1. Set Player Leaderboard Score as a Float**

![]()

**Node Functions**

Set Player Leaderboard Score (Float)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player ID List | Integer List |  |
| Input Parameter | Leaderboard Score | Floating Point Numbers |  |
| Input Parameter | Leaderboard ID | Integer | The ID corresponding to the specified Leaderboard in Peripheral System management |

## **2. Set Player Leaderboard Score as an Integer**

![]()

**Node Functions**

Set Player Leaderboard Score (Integer)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player ID List | Integer List |  |
| Input Parameter | Leaderboard Score | Integer |  |
| Input Parameter | Leaderboard ID | Integer | The ID corresponding to the specified Leaderboard in Peripheral System management |

# XLIII. Achievements

## **1. Increase Achievement Progress Tally**

![]()

**Node Functions**

Change the progress counter for the specified Achievement ID on the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Change Entity | Entity |  |
| Input Parameter | Achievement ID | Integer |  |
| Input Parameter | Progress Tally Increase Value | Integer | New Value = Previous Value + Change Value |

## **2. Set Achievement Progress Tally**

![]()

**Node Functions**

Set the progress counter for the specified Achievement ID on the Target Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Set Entity | Entity |  |
| Input Parameter | Achievement ID | Integer |  |
| Input Parameter | Progress Tally | Integer | Sets the Progress Count to the input value |

# XLIV. Scan Tags

## **1. Set Scan Tag Rules**

![]()

**Node Functions**

Configure rules for Scan Tags. The scanning logic is executed based on the configured rules

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Rule Type | Enumeration | Options: Prioritize View or Prioritize Distance |

## **2.** Set Scan Component's Active Scan Tag ID

![]()

**Node Functions**

Set the Scan Tag with the specified ID in the Target Entity's Scan Tag Component to the active state

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity |  |
| Input Parameter | Scan Tag ID | Integer |  |

# XLV. Rank

## **1.** Switch the Scoring Group that Affects Player's Competitive Rank

![]()

**Node Functions**

Switch the active Scoring Group of the specified Player's Ranking by Scoring Group ID

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |
| Input Parameter | Score Group ID | Integer | The ID corresponding to the specified Score Group in Peripheral System management |

## **2. Set Player Rank Score Change**

![]()

**Node Functions**

Set the Player's rank score change based on the settlement status

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |
| Input Parameter | Settlement Status | Enumeration | Includes: Undefined, Victory, Defeat, Escape |
| Input Parameter | Score Change | Integer |  |

## **3. Set Player Escape Validity**

![]()

**Node Functions**

Set whether escaping is permitted for the specified Player

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |
| Input Parameter | Valid | Boolean |  |

# XLVI. Entity Deployment Group

## **1. Activate/Disable Entity Deployment Group**

![]()

**Node Functions**

Edit the Initial Creation Switch state of the Entity Layout Group

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Entity Deployment Group Index | Integer |  |
| Input Parameter | Activate | Boolean | If set to True, the Entity Layout Group's Initial Creation switch is enabled |

# XLVII. Chat Channel

## **1. Set Chat Channel Switch**

![]()

**Node Functions**

Configure the voice and text toggles for the chat channel

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Channel Index | Integer |  |
| Input Parameter | Voice-Over Switch | Boolean |  |
| Input Parameter | Text Switch | Boolean |  |

## **2. Set Player's Current Channel**

![]()

**Node Functions**

Set the Player's currently available channels. Channels in the list are available to the Player, and channels not in the list are unavailable

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player GUID | GUID |  |
| Input Parameter | Channel Index List | Integer List |  |

## **3. Set Text Chat Permissions**

![]()

**Node Functions**

Set the target player's permission to use text chat in the channel list

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Player | Entity |  |
| Input Parameter | Channel List | Integer List |  |
| Input Parameter | Limit Permissions | Boolean | When enabled, the corresponding functionality of the player in the designated channel list will be restricted |

## **4. Set Voice Chat Scope**

![]()

**Node Functions**

Set the voice chat range of the target player within the channel list

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Player | Entity |  |
| Input Parameter | Channel List | Integer List |  |
| Input Parameter | Effective Range | Integer | This determines the distance within which the target player can hear voice chat from other players in the same channel, and does not affect the range at which other players can hear the target player  Range: 1–100 m |
| Input Parameter | Limit Scope | Boolean | The range takes effect only when this option is enabled; When disabled, the configured range value is ignored |

## **5. Set Voice Chat Permissions**

![]()

**Node Functions**

Set the target player's permissions to use voice chat in the channel list

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Player | Entity |  |
| Input Parameter | Channel List | Integer List |  |
| Input Parameter | Restrict Voice Chat (Speak) | Boolean | When enabled, other players cannot hear the target player's voice |
| Input Parameter | Restrict Voice Chat (Listen) | Boolean | When enabled, the target player cannot hear other players' voices |

## **6. Set Player Channel Permissions**

![]()

**Node Functions**

Set player channel permissions

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player GUID | GUID |  |
| Input Parameter | Channel Index | Integer |  |
| Input Parameter | Join | Boolean | When enabled, the channel is only available to the specified player(s) |

# XLVIII. Wonderland Gift Boxes

## **1. Consume Gift Box**

![]()

**Node Functions**

Consume the specified Player's Wonderland Gift Box

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |
| Input Parameter | Gift Box Index | Integer |  |
| Input Parameter | Consumption Quantity | Integer |  |
| Output Parameter | Consumer? | Boolean | Output Paramter reads Yes when Gift Box is successfully consumed |

# XLIX. Pathfinding Obstacle

## **1. Enable/Disable Pathfinding Obstacle**

![]()

**Node Functions**

You can modify whether the pathfinding obstacke component of the target entity, corresponding to the specified index, is active.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity | Only applies to objects |
| Input Parameter | Pathfinding Obstacle ID | Integer |  |
| Input Parameter | Activate | Boolean |  |

## **2. Enable/Disable Pathfinding Obstacle Feature**

![]()

**Node Functions**

You can modify whether the pathfinding obstacle function of the target entity is activated.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity | Only applies to objects |
| Input Parameter | Activate | Boolean |  |

# L. Creation Preset Status

## **1. Set the Preset Status Value of the Complex Creation**

![]()

**Node Functions**

You can set the preset state value for a specified preset state index of a complex creation.

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Target Entity | Entity | Only applies to complex creations |
| Input Parameter | Preset Status Index | Integer |  |
| Input Parameter | Preset Status Value | Integer |  |

# LI. Floating Interaction Page

## **1. Close Floating Interaction Page**

![]()

**Node Functions**

Close the floating interaction page at the specified index for the Player Entity

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity | Active Player Entity |
| Input Parameter | Floating Interaction Page Index | Integer | Unique Identifier of the Floating Interaction Page |

## **2. Update Floating Interaction Page List Data**

![]()

**Node Functions**

Replace the current displayed items of the tab or single-choice window at the specified list index with the visible list items corresponding to the input integer list

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity | Active Player Entity |
| Input Parameter | List Index | Integer | Unique Identifier for a Tab or Single-Choice Window |
| Input Parameter | Visible List Item | Integer List | List of items for the tab or single-choice window. The input will update the visible list items of the specified tab or single-choice window |
| Input Parameter | Select First Item by Default | Boolean | Yes: Select the first item by default  No: Keeps the last selected item (if any) |

## **3. Show Floating Interaction Page**

![]()

**Node Functions**

Open the floating interaction page at the specified index for the Player, with optional initialization of tab or single-choice window data

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity | Active Player Entity |
| Input Parameter | Floating Interaction Page Index | Integer | Unique Identifier of the Floating Interaction Page |
| Input Parameter | Initialize List Data | Dictionary | Key (int): Index corresponding to the tab or single-choice window  Value (List): Integer list corresponding to the tab items (for tabs) or item list (for single-choice windows) |

# **LII. Stage Quests**

## **1. No. of Tasks Configured**

![]()

**Node Functions**

Available only for Beyond Mode

Allows the setting of player's current corresponding task count to a specified value

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |
| Input Parameter | Quest Index | Integer |  |
| Input Parameter | Task Count | Integer |  |

## **2. Increase Task Count**

![]()

**Node Functions**

Available only for Beyond Mode

Use this to increase the current count of the corresponding player tasks (value entered may be negative)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Player Entity | Entity |  |
| Input Parameter | Quest Index | Integer |  |
| Input Parameter | Task Count Increased by | Integer | New Value = Previous Value + Increase Value |

## 

##

Event Nodes
