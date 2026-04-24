# Mini Task Management API

## 1. Overview (ระบบนี้คืออะไร)

Mini Task Management API เป็น RESTful API ที่พัฒนาด้วย Flask โดยมีวัตถุประสงค์เพื่อใช้ในการจัดการรายการงาน (Task Management) ภายในระบบ ผู้ใช้งานสามารถสร้าง, ดูและจัดการงานของตนเองได้ผ่าน API

ระบบนี้มีการใช้ JWT (JSON Web Token) สำหรับการยืนยันตัวตนว่าเราเป็นใคร เพื่อรักษาความปลอดภัยของข้อมูลและควบคุมการเข้าถึง Endpointต่างๆ นอกจากนี้ยังสามารถเชื่อมต่อกับ API ของผู้ใช้งานอื่น (External API Integration) เพื่อดึงข้อมูล Task จากระบบภายนอกมารวมแสดงผลได้ใน Endpoint เดียว

---

## Tools & Technologies

* Python 3
* Flask
* PyJWT
* Requests
* Postman
* Render

---

## 2. How to Run (วิธีติดตั้งและรัน)

### 1. Clone โปรเจค

```bash
git clone https://github.com/Bxnus2099/task-api.git
cd task-api
```

### 2. ติดตั้ง dependencies

```bash
pip install -r requirements.txt
```

### 3. Run server

```bash
python app.py
```

### 4. Server จะรันที่

http://localhost:5000

---

##  3. วิธีการใช้งาน (How to Use API)

### Step 1: Login เพื่อรับ Token

* Method: **POST**
* URL: `/login`
* Body (JSON):

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

 ผลลัพธ์:

```json
{
  "token": "your_jwt_token"
}
```

 **สำคัญ:** ต้อง copy token ไปใช้ในทุก API เพื่อต้องยืนยันตัวตน = Authorization

---

### Step 2: ใส่ Token ใน Header

ใน Postman ให้ไปที่ **Authorization → Bearer Token**

หรือใส่ใน Header:

```
Authorization: Bearer <token>
```

---

### Step 3: ดู Task ของตัวเอง

* Method: **GET**
* URL: `/tasks`

 Response:

```json
{
  "tasks": [...]
}
```

---

### Step 4: เพิ่ม Task

* Method: **POST**
* URL: `/tasks`
* Body (JSON):

```json
{
  "title": "อ่านหนังสือ",
  "status": "pending",
  "priority": "medium",
  "due_date": "2026-05-01"
}
```

 Response:

```json
{
  "message": "Task created"
}
```

---

### Step 5: ดู Task แบบ Public

* Method: **GET**
* URL: `/public-tasks`

 ใช้สำหรับให้เพื่อนเรียกข้อมูลของเรา

---

### Step 6: ดึง Task ของเพื่อน (External API)

* Method: **GET**
* URL: `/external-tasks`

 Response:

```json
{
  "Bonus_Tasks": [...],
  "external_tasks": {
    "Tangmo": [...],
    "Cream": [...]
  }
}
```

Endpoint นี้จะรวม:

* Task ของตัวเอง
* Task ของเพื่อน

---

## 4. Endpoints

| Method | Endpoint        | Description |
| ------ | --------------- | ----------- |
| POST   | /login          | Login       |
| GET    | /tasks          | ดู Task     |
| POST   | /tasks          | เพิ่ม Task  |
| GET    | /public-tasks   | Public Task |
| GET    | /external-tasks | รวม Task    |

---

## 5. Error Examples

### 401 Unauthorized

```json
{
  "error": {
    "code": 401,
    "message": "Invalid token"
  }
}
```

### 500 Internal Server Error

```json
{
  "status": "error",
  "code": 500,
  "message": "Internal server error"
}
```

---

## Notes

* ต้อง Login ก่อนใช้งาน API
* ต้องใช้ Token กับทุก endpoint (ยกเว้น public)
* External API ต้องมี `/public-tasks`
* ใช้ JSON เท่านั้น

---

## Author

* Name: BOONYANAT PUVICJITSUTIN
* Course: IE322 338B
* Project: Mini Task Management API
