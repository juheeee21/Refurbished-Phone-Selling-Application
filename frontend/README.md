# Refurbished Phone Seller Frontend

## Quickstart

1. Install dependencies:
   ```
   npm install
   ```

2. Start dev server (assumes backend is running on localhost:8000):
   ```
   npm run dev
   ```

3. Open [http://localhost:5173](http://localhost:5173)

## Features

- Login (any credentials)
- Inventory list, search, filter, delete
- Bulk upload CSV (see backend sample)
- Simulate listing on X, Y, Z (shows profit errors, stock errors, etc)
- Manual price override per platform

## Notes

- API endpoint is set to `http://localhost:8000` in `src/api.ts`.
- To change, edit `baseURL` in `src/api.ts`.
- Styling is minimal for clarity and demo.
