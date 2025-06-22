# Alerto

Let’s go bhai 💪 Time to execute!
Here’s your complete **project flow**, broken into logical parts — so you don’t get overwhelmed.

---

## 🚧 Step-by-Step Build Flow for SafeWalk

---

### 🧱 **Phase 1: Core Setup (Day 0–1)**

#### 🔹 1.1 Setup Git & Folder Structure

Create main folders:

```
/safewalk
├── /mobile-app (React Native)
├── /web-dashboard (ReactJS)
├── /backend-api (Flask)
├── /hardware (Arduino/ESP32)
```

Set up Git repo locally or on GitHub.

---

#### 🔹 1.2 Start Backend API (Flask)

**Start here**: backend is the heart of coordination.

* `GET /api/alerts` → Send active SOS alerts (for dashboard)
* `POST /api/trigger-sos` → Trigger SOS alert
* `POST /api/voice-command` → Accept voice command input (optional)
* `POST /api/hardware-trigger` → BLE/GSM trigger endpoint

Use SQLite or Firebase RTDB for simple real-time storage.

---

### 📱 **Phase 2: Build Mobile App (React Native)**

Start basic screens:

1. **Home**: Start Trip / End Trip
2. **Tracking Screen**: Timer, live location
3. **SOS Trigger**: Auto via detection or manual
4. **Voice Command (optional)**
5. **Fake Call Button**
6. **Settings**: Add contacts, view reports

Use:

* `react-native-maps`
* `react-native-background-geolocation`
* `axios` for API
* `react-native-voice` (for voice commands)
* `react-native-fake-call` or similar (for fake call UI)

---

### 🌐 **Phase 3: Web Dashboard (ReactJS)**

Quick start from the dashboard I gave earlier.

Pages:

* Active Alerts (cards with map & call)
* Heatmap Viewer (Google Maps Heatmap Layer)
* Reports Table
* Admin Login (optional)

---

### 🔧 **Phase 4: Hardware Trigger (ESP32)**

Use:

* Triple button press detection
* BLE/GSM module
* Send HTTP request to `/api/hardware-trigger`
* Optional: attach buzzer or LED for siren effect

Test: Press button → sends SOS to API → triggers flow same as app.

---

### 🧠 **Phase 5: AI / Risk Features**

Start basic:

* Use sample data of trip histories + crime zones
* Detect:

  * If user stopped > X seconds
  * Deviated > Y meters from planned path
* If anomaly → auto POST to `/api/trigger-sos`

Bonus:

* Heatmap of risk zones using `Google Maps JavaScript Heatmap Layer`
* `Scikit-learn` model for route safety prediction

---

## 🧪 Final Demo Setup Flow

1. Start trip in mobile app
2. Simulate abnormal pause or press hardware button
3. Backend triggers:

   * WhatsApp Alert (Twilio)
   * Dashboard Alert
   * Optional: Fake call, recording start

---

## 🗂 Tools Recap (Use these)

| Part          | Tools                           |
| ------------- | ------------------------------- |
| Mobile App    | React Native, Expo              |
| Backend       | Python Flask, SQLite / Firebase |
| Messaging     | Twilio WhatsApp API             |
| Hardware      | ESP32 + Button + Buzzer         |
| Voice         | `react-native-voice`            |
| Map/Tracking  | Google Maps API                 |
| Web Dashboard | ReactJS + Tailwind + Axios      |

---

## 🟢 Start Here First:

```bash
cd backend-api
```

Make Flask API + `/api/trigger-sos` + `/api/alerts` working first.
Once that works, **plug into app and web**.

---

Tu bol next kis part pe kaam shuru karna hai (Flask backend? App setup? Dashboard?), I’ll give you exact starter code. Let’s build this 💻🔥
