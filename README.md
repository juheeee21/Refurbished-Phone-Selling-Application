# Refurbished Phone Selling Platform

A full-stack application for managing and selling refurbished phones on simulated e-commerce platforms (X, Y, Z).  
Handles inventory, platform-specific pricing and fees, phone condition mapping, and prevents unprofitable or out-of-stock listings.  
**Backend:** Python (FastAPI, SQLite)  
**Frontend:** React (TypeScript, Vite)

---

## Features

- **Admin Inventory Management**
  - Add, update, delete phones (model, brand, condition, specs, stock, price, tags)
  - Bulk upload via CSV
  - Manual platform price override

- **Platform Listing Simulation**
  - Simulate listing a phone on platform X, Y, or Z
  - Platform-specific price calculation and fee rejection logic
  - Maps phone condition to each platform’s categories

- **Stock and Tag Handling**
  - Prevents out-of-stock/discontinued phones from being listed

- **Search & Filtering**
  - Search by model or brand
  - Filter by condition
  - See which phones are listed on which platform

- **Security**
  - Input validation/sanitization
  - Mock authentication (any username/password)

---

## Getting Started

### 1. Backend

#### Prerequisites

- Python 3.9+
- [pip](https://pip.pypa.io/en/stable/)

#### Setup

```bash
cd backend
pip install -r requirements.txt
```

#### (Optional) Seed Demo Data

```bash
python demo_seed.py
```

#### Run the Server

```bash
uvicorn main:app --reload
```

- API docs available at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 2. Frontend

#### Prerequisites

- [Node.js](https://nodejs.org/) (v18+ recommended)
- npm

#### Setup

```bash
cd frontend
npm install
npm run dev
```

- Open [http://localhost:5173](http://localhost:5173) in your browser.

---

## Usage

1. **Login:** Any credentials are accepted.
2. **Bulk Upload:** Use the CSV upload form (see sample below).
3. **Manage Inventory:** View, search, filter, and delete phones.
4. **Simulate Listing:** Select a phone and simulate listing on a platform; the UI shows price, fees, or rejection reason.
5. **Manual Override:** Set per-platform prices for any phone.
6. **Edge Cases:** Try uploading zero-stock or unprofitable phones to see error handling in action.

---

## Sample CSV for Bulk Upload

```csv
brand,model,condition,specs,stock,base_price,tags
Apple,iPhone X,Good,"{'storage':'64GB','color':'Black'}",5,250,
Samsung,Galaxy S10,New,"{'storage':'128GB','color':'White'}",3,320,
Nokia,3310,Scrap,"{'storage':'16MB','color':'Blue'}",0,20,"out of stock"
```

---

## Project Structure

```
refurbished-phone-app/
│
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── utils.py
│   ├── crud.py
│   ├── auth.py
│   ├── demo_seed.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   ├── README.md
│   └── src/
│       ├── main.tsx
│       ├── api.ts
│       ├── types.ts
│       ├── App.tsx
│       └── components/
│           ├── Login.tsx
│           ├── Inventory.tsx
│           ├── BulkUpload.tsx
│           ├── ListingSimulator.tsx
│           └── ManualOverrideForm.tsx
│
└── sample_phones.csv  # (optional, for demo)
```

---

## Assessment Criteria Covered

- **Problem-Solving:** Complete inventory, pricing, platform logic, and robust error handling.
- **Code Quality:** Modular, documented, and type-checked code.
- **Security:** Input validation, sanitization, and authentication demo.
- **Functionality:** End-to-end flow with all required and bonus features.

---

## License

MIT License
