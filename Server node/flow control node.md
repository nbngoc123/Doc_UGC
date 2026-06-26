# Flow Control Nodes (Node Điều Hướng)

# I. Cài đặt chung (General)

## **1. Multiple Branches (Rẽ nhánh đa luồng)**

![](./flow control node_files/f737a2e0-028a-4724-9b39-077959f1e1a4.png)

**Chức năng của Node:**

Chấp nhận một tham số đầu vào làm biểu thức điều khiển (hỗ trợ kiểu Số nguyên hoặc Chuỗi). Từ đó phân nhánh thành nhiều luồng thực thi dựa trên giá trị của nó.

Khi giá trị trên một Output Pin (Chốt đầu ra) khớp với biểu thức điều khiển, luồng thực thi sẽ chạy tiếp theo Output Pin đó. Nếu không có pin nào khớp, nó sẽ chạy theo pin [Default] (Mặc định).

**Tham số của Node:**

| | | | |
| --- | --- | --- | --- |
| **Loại Tham số** | **Tên Tham số** | **Kiểu dữ liệu** | **Mô tả** |
| Đầu vào (Input) | Control Expression (Biểu thức điều khiển) | Generic (Chung) | Chỉ hỗ trợ Số nguyên (Integers) hoặc Chuỗi (Strings) |

## **2. Double Branch (Rẽ nhánh đôi - If/Else)**

![](./flow control node_files/f3debfdb-74c0-49d7-b08d-7168a73fa9f3.png)

**Chức năng của Node:**

Rẽ nhánh thành hai hướng True (Đúng) hoặc False (Sai) dựa trên kết quả kiểm tra của điều kiện.

Khi biểu thức Boolean trả về Đúng (True), luồng thực thi [True] sẽ được chạy; khi nó trả về Sai (False), luồng thực thi [False] sẽ được chạy.

**Tham số của Node:**

| | | | |
| --- | --- | --- | --- |
| **Loại Tham số** | **Tên Tham số** | **Kiểu dữ liệu** | **Mô tả** |
| Đầu vào (Input) | Condition (Điều kiện) | Boolean (Luận lý) | |
