# DevNetwork 🚀
**Platformă web pentru developeri** - Comunicare, colaborare și gestionare proiecte

[![Django](https://img.shields.io/badge/Django-4.2-brightgreen)](https://djangoproject.com)
[![React](https://img.shields.io/badge/React-18-blue)](https://react.dev)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-purple)](https://postgresql.org)

---

## 🎯 Descriere Proiect
Platformă web dedicată **dezvoltatorilor** pentru:
- Comunicare în timp real (text chat, voice/video meetings)
- Colaborare la proiecte comune
- Gestionare eficientă a task-urilor și deadline-urilor
- Partajare de idei și portofolii

---

## ✨ Funcționalități

### **1. Comunicare & Networking**
- ✅ Text chat 1:1 și grupuri
- ✅ Voice/Video meetings (WebRTC)
- ✅ Sistem prieteni & request-uri
- ✅ Notificări real-time

### **2. Gestionare Proiecte**
- ✅ Creare proiecte cu descriere detaliată
- ✅ Invitare/Afiliere membri
- ✅ Deadline-uri și task management
- ✅ Căutare avansată (titlu, domeniu, skills)

### **3. Social Features**
- ✅ Postări & comentarii
- ✅ Reacții emoji
- ✅ Feed activitate proiecte

### **4. Profile Personalizate**
- ✅ Experiență profesională
- ✅ Proiecte personale
- ✅ Skills & interese
- ✅ Portofoliu GitHub

---

## 🛠️ Tech Stack

| Componentă | Tehnologie | Versiune |
|------------|------------|----------|
| **Backend** | Django + DRF | 5.0+ |
| **Frontend** | React + Vite | 18+ |
| **Database** | PostgreSQL | 16 |
| **Real-time** | Django Channels + Redis | Latest |
| **Video** | WebRTC Peer-to-Peer | Native |

---

## 🚀 Cum să rulezi local

```bash
# Clone repo
git clone https://github.com/hsky8689-sys/dev-network.git
cd dev-network

# Backend
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Frontend (tab nou)
cd ../frontend
npm install
npm run dev

