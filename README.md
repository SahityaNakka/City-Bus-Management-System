# CityTransit — Project 22: City Bus Management System (DEMO)

> **DEMO / NOT LIVE TRANSIT**: Fictional city bus routes, stops, buses, drivers, bookings, and mock payments. Inspired by RedBus & AbhiBus passenger search + seat selection, paired with a full transit operations portal.

---

## Clear Frontend vs. Backend Separation

### Backend (`backend/` — Python FastAPI + SQLAlchemy + Alembic)
| File / Folder | Responsibility |
| :--- | :--- |
| `backend/run.py` | Seeds demo data and launches FastAPI (`http://127.0.0.1:8000/`) |
| `backend/migrate_db.py` | Standalone Alembic schema upgrade + idempotent demo seeding |
| `backend/app/config.py` | Environment settings (`.env` loader, JWT, CORS, cutoff minutes) |
| `backend/app/database.py` | SQLAlchemy engine, SQLite/PostgreSQL/MySQL session setup |
| `backend/app/auth.py` | PBKDF2-SHA256 password hashing, JWT tokens, 7-role `require_roles` RBAC |
| `backend/app/models.py` | SQL ORM entities (`Role`, `User`, `Bus`, `Driver`, `Route`, `Stop`, `RouteStop`, `Schedule`, `FareRule`, `Trip`, `AssignmentHistory`, `TripEvent`, `Booking`, `AuditLog`, `Notification`) |
| `backend/app/schemas.py` | Pydantic v2 request/response validation schemas |
| `backend/app/services.py` | Business rules (route validation, bus/driver overlap locking, booking capacity locking, notifications, audit logs, dashboard stats) |
| `backend/app/routers/auth_users.py` | `/api/auth/*`, `/api/users/*`, `/api/notifications` |
| `backend/app/routers/master_data.py` | `/api/buses/*`, `/api/drivers/*`, `/api/stops/*`, `/api/routes/*` |
| `backend/app/routers/operations.py` | `/api/schedules/*`, `/api/fare-rules/*`, `/api/trips/*`, `/api/public/trips/search` |
| `backend/app/routers/bookings_reports.py` | `/api/bookings/*`, `/api/dashboard/summary`, `/api/reports/*`, `/api/audit-logs` |
| `backend/app/main.py` | FastAPI app, global error handlers, CORS, and React `dist/` hosting |
| `backend/tests/` | `test_api.py` & 4-stage `test_production_readiness.py` |

### Frontend (`City_Bus_Management_System_React_Frontend/City-Bus-Management-System-Frontend/src/` — React 18 + Vite)
| File / Folder | Responsibility |
| :--- | :--- |
| `src/api.js` | Axios HTTP client with JWT interceptor & readable error extraction |
| `src/utils/date.js` | Local timezone-safe ISO date, UTC time, and duration helpers |
| `src/context/AuthContext.jsx` | Session state, login/register/logout, and 7-role RBAC helpers |
| `src/components/` | Reusable UI (`Sidebar`, `Header`, `DataTable`, `FilterBar`, `FormField`, `ConfirmDialog`, `Pagination`, `Modal`, `PageTitle`, `StatCard`, `StatusBadge`) |
| `src/pages/Login.jsx` | Split-screen login, Passenger Sign-Up tabs, and 1-Click Demo Role cards |
| `src/pages/Dashboard.jsx` | Role-aware KPIs, route bookings chart, fleet readiness bars, and quick actions |
| `src/pages/SearchTrips.jsx` | RedBus/AbhiBus-inspired hero search bar, bus filters, stop timeline, and interactive 2+2 seat selector modal |
| `src/pages/BookingsPage.jsx` | Bookings table, printable demo E-Ticket / boarding pass modal, cancellations, and attendance controls |
| `src/pages/TripsPage.jsx` | Dispatch assignments, overlap validation, status transitions, and driver events |
| `src/pages/BusesPage.jsx`, `DriversPage.jsx`, `RoutesPage.jsx`, `StopsPage.jsx`, `SchedulesPage.jsx`, `UsersPage.jsx`, `Reports.jsx` | Master data, ordered stops, fare rules, filterable reports (with CSV export & print), and admin user control |
| `src/styles.css` | RedBus/AbhiBus-inspired responsive design system |

---

## 1. Quick Start (Single URL: `http://127.0.0.1:8000/`)

```powershell
cd backend
.\.venv\Scripts\Activate.ps1
python migrate_db.py
python run.py
```

- **CityTransit Web App:** `http://127.0.0.1:8000/`
- **Swagger API Docs:** `http://127.0.0.1:8000/docs`
- **Health Check:** `http://127.0.0.1:8000/api/health`
- **Tests:** `cd backend; pytest -v -s`

---

## 2. Optional Frontend Dev Mode (Hot Reload on `:5173`)

```powershell
cd "City_Bus_Management_System_React_Frontend\City-Bus-Management-System-Frontend"
npm.cmd install
npm.cmd run dev
```

- **Dev Frontend URL:** `http://localhost:5173` (proxies `/api` to `http://127.0.0.1:8000`)
- **Rebuild Production UI for Port `8000`:** `npm.cmd run build`

---

## 3. Seeded Demo Accounts (Password: `demo123`)

| Role | Email | Access Scope |
| :--- | :--- | :--- |
| Administrator | `admin@citytransit.demo` | Full system & user management |
| Transport Manager | `manager@citytransit.demo` | Routes, stops, buses, drivers, schedules, trips, reports |
| Dispatcher | `dispatcher@citytransit.demo` | Daily dispatch, assignments, trip status, follow-ups |
| Driver | `driver1@citytransit.demo` | Assigned trips, route stops, departure/arrival/passenger updates |
| Booking Clerk | `clerk@citytransit.demo` | Trip search, bookings, cancellations, attendance statuses |
| Passenger | `passenger@citytransit.demo` | Search published trips, select seats, manage demo E-tickets |
| Auditor/Viewer | `auditor@citytransit.demo` | Read-only operational reports & audit logs |
