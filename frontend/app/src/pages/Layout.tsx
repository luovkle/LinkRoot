import { Outlet } from "react-router-dom";
import { Auth0Provider } from "@auth0/auth0-react";
import { Navbar } from "../components";

export const Layout = () => {
  return (
    <>
      <Auth0Provider
        domain={import.meta.env.VITE_AUTH0_DOMAIN}
        clientId={import.meta.env.VITE_AUTH0_CLIENT_ID}
        authorizationParams={{
          redirect_uri: window.location.origin,
        }}
      >
        <Navbar />
      </Auth0Provider>
        <Outlet />
    </>
  )
}