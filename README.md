# Task API Mini Project

## 1. ภาพรวม (Overview)

โปรเจค Task API Mini Project เป็นระบบ RESTful API ที่พัฒนาด้วยภาษา Python และใช้ Flask Framework สำหรับจัดการรายการงาน (Task Management) โดยระบบนี้ออกแบบมาเพื่อให้ผู้ใช้งานสามารถเพิ่มและดูรายการงานของตนเองได้ผ่าน API

นอกจากนี้ ระบบยังมีการใช้ JWT (JSON Web Token) สำหรับการยืนยันตัวตน (Authentication) เพื่อควบคุมการเข้าถึงข้อมูล และเพิ่มความปลอดภัยในการใช้งาน อีกทั้งยังรองรับการเชื่อมต่อกับ API ของผู้ใช้งานอื่น (External API Integration) เพื่อดึงข้อมูล Task จากภายนอกมารวมแสดงผลได้ในระบบเดียว

ระบบนี้แสดงให้เห็นถึงแนวคิดสำคัญในการพัฒนา Web API ได้แก่ การออกแบบ Endpoint, การจัดการ Request และ Response, การทำการยืนยันตัวตนว่าเราเป็นใคร Authentication, การจัดการข้อผิดพลาด (Error Handling) และการเชื่อมต่อระหว่างระบบ (System Integration)

---

## 2. ฟีเจอร์หลัก (Features)

ระบบมีความสามารถหลักดังนี้:

* รองรับการ Login และยืนยันตัวตนด้วย JWT
* สามารถดูรายการ Task (ต้องใช้ Token)
* สามารถเพิ่ม Task ใหม่เข้าสู่ระบบ
* รองรับ Public API สำหรับดู Task โดยไม่ต้องใช้ Token
* สามารถเชื่อมต่อและดึงข้อมูลจาก API ของเพื่อน
* มีระบบจัดการ Error เช่น 400, 401 และ 500

---

## 3. เทคโนโลยีที่ใช้ (Technology Stack)

โปรเจคนี้พัฒนาด้วยเครื่องมือและเทคโนโลยีดังนี้:

* Python 3 — ภาษาหลักในการพัฒนา
* Flask — ใช้สร้าง RESTful API
* PyJWT — ใช้สำหรับสร้างและตรวจสอบ Token
* Requests — ใช้สำหรับเรียก External API
* JSON ผ่าน HTTP — ใช้สำหรับส่งข้อมูลระหว่างระบบ

---

## 4. วิธีใช้งาน (How to Run)

เริ่มต้นใช้งานระบบสามารถทำตามขั้นตอนดังนี้:

### 4.1 Clone โปรเจค

เปิด Command Prompt หรือ Terminal แล้วรันคำสั่ง:

```bash
git clone https://github.com/Bxnus2099/task-api.git
cd task-api
```

### 4.2 ติดตั้ง Dependencies

```bash
pip install -r requirements.txt
```

### 4.3 รันเซิร์ฟเวอร์

```bash
python app.py
```

หลังจากรันสำเร็จ ระบบจะสามารถเรียกใช้งานผ่าน:

```
http://localhost:5000
```

---

### 4.4 อัปโหลดขึ้น GitHub และ Deploy

หลังจากพัฒนาเสร็จ สามารถนำระบบขึ้นใช้งานจริงได้โดย:

1. push โค้ดขึ้น GitHub
2. ไปที่เว็บไซต์ Render (https://render.com)
3. เลือก New → Web Service
4. เชื่อมต่อกับ Repository ของเรา (task-api)
5. ตั้งค่า:

   * Build Command: `pip install -r requirements.txt`
   * Start Command: `python app.py`

เมื่อ Deploy สำเร็จ ระบบจะได้ URL เช่น:

```
https://your-api.onrender.com
```

ซึ่งสามารถนำไปใช้ใน Postman ได้ทันที

---

## 5. การยืนยันตัวตน (Authentication)

ผู้ใช้งานต้องทำการ Login เพื่อรับ Token ก่อนใช้งาน API

```http
POST /login
```

ตัวอย่าง Request:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

Response:

```json
{
  "token": "your_jwt_token"
}
```

จากนั้นให้นำ Token ไปใส่ใน Header:

```
Authorization: Bearer <token>
```

---

## 6. API Endpoints

ระบบประกอบด้วย Endpoint หลักดังนี้:

* `POST /login` → ใช้สำหรับ Login
* `GET /tasks` → ดู Task (ต้องใช้ Token)
* `POST /tasks` → เพิ่ม Task (ต้องใช้ Token)
* `GET /public-tasks` → ดู Task แบบ Public
* `GET /external-tasks` → ดึง Task จาก API ของเพื่อน

---

## 7.  ตัวอย่าง Request และ Response

### Login

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

---

### ดู Task

```json
{
  "tasks": [
    {
      "id": 1,
      "title": "ทำ Homework วิชา IE322",
      "status": "pending",
      "priority": "high",
      "due_date": "2026-04-30"
    }
  ]
}
```

---

### เพิ่ม Task

```json
{
  "title": "อ่านหนังสือสอบ",
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

### Error (400)

```json
{
  "error": {
    "code": 400,
    "message": "Title is required"
  }
}
```

---

### Error (401)

```json
{
  "error": {
    "code": 401,
    "message": "Invalid token"
  }
}
```

---

### Error (500)

```json
{
  "status": "error",
  "code": 500,
  "message": "Internal server error"
}
```

---

## 8. ขั้นตอนการทำงานของ Integration
การทำงานของ External API มีขั้นตอนดังนี้:

1. ระบบส่ง request ไปยัง API ของเพื่อน
2. รับข้อมูล JSON กลับมา
3. ตรวจสอบรูปแบบข้อมูล
4. รวมข้อมูลกับ Task ของตัวเอง
5. ส่งผลลัพธ์กลับไปยังผู้ใช้งาน

---

## 9. HTTP Status Codes ที่ใช้

* 200 OK
* 400 Bad Request
* 401 Unauthorized
* 500 Internal Server Error

---

## 10. การจัดการ Error
ระบบรองรับการจัดการ Error และส่งกลับในรูปแบบ JSON เพื่อให้ผู้ใช้งานเข้าใจได้ง่าย

---

## 11. ความปลอดภัย (Security)
* ใช้ JWT สำหรับ Authentication
* Token มีวันหมดอายุ
* ใช้ HTTPS เมื่อ Deploy จริง
* ห้ามใส่ข้อมูลส่วนตัวเช่นรหัส API หรือ Token ลง Github

---

## 12. สิ่งที่สามารถพัฒนาต่อได้

* เพิ่มฐานข้อมูล เช่น MySQL หรือ MongoDB
* เพิ่มฟีเจอร์ Update และ Delete Task
* เพิ่มระบบสมัครสมาชิก (Register)

---

## ผู้จัดทำ
- Name: BOONYANAT PUVICJITSUTIN
- Course: (ชื่อวิชา เช่น IE322)
- Project: Mini Task Management API
