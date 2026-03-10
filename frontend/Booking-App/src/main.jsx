import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.jsx";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import deluxe1 from "./assets/images/deluxe1.jpg";
import deluxe2 from "./assets/images/deluxe2.jpg";
import deluxe3 from "./assets/images/deluxe3.jpg";
import family_suite1 from "./assets/images/family_suite1.jpg";
import family_suite2 from "./assets/images/family_suite2.webp";
import standard1 from "./assets/images/standard1.jpg";
import standard2 from "./assets/images/standard2.webp";
import standard3 from "./assets/images/standard3.webp";

import AllRooms from "./components/AllRooms.jsx";
import BookingComponent from "./components/BookingComponent.jsx";
import AuthForm from "./components/AuthForm.jsx";
import { UserProvider } from "./components/UserContext.jsx";
import GuestRoute from "./components/GuestRoute.jsx";
import OccupiedDateDisplay from "./components/OccupiedDateDisplay.jsx";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App></App>,
    children: [
      {
        path: "/",
        element: <BookingComponent></BookingComponent>,
      },
      {
        path: "/all-rooms",
        element: <AllRooms></AllRooms>,
      },
      {
        path: "/auth",
        element: (
          <GuestRoute>
            <AuthForm></AuthForm>
          </GuestRoute>
        ),
      },
      {
        path: "/my-bookings",
        element: <OccupiedDateDisplay></OccupiedDateDisplay>,
      },
    ],
  },
]);

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <UserProvider>
      <RouterProvider router={router} />
    </UserProvider>
  </StrictMode>,
);
