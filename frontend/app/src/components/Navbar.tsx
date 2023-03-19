import { Link } from "react-router-dom";
import { LoginButton } from "./auth/Login";

export const Navbar = () => {
  return (
    <header className="sticky top-0 z-10">
      <nav className="flex backdrop-blur-sm bg-white/50 w-full
        justify-between">
        <Link to="/" className="font-logo text-4xl text-white py-2 px-1">LinkRoot</Link>
        <ul className="flex items-center gap-4">
          <li>
            <Link to="/profile">Profile</Link>
          </li>
          <li>
            <LoginButton />
          </li>
        </ul>
      </nav>
    </header>
  )
}