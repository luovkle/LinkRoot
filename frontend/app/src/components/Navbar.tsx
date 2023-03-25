import { useState } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { Link } from "react-router-dom";
import { 
  AiOutlineMenu, 
  AiOutlineClose, 
  AiOutlineSearch, 
} from "react-icons/ai";
import { LoginButton } from "./auth/Login";
import { LogoutButton } from "./auth/Logout";
import { Search } from "./Search";

export const Navbar = () => {

  const { isAuthenticated } = useAuth0();
  const [ nav, setNav ] = useState(false);

  const handleNav = () => {
    setNav(!nav);
  };


  return (
    <>
      <div className="fixed my-2 w-full z-50">
        <div className="flex mx-1 px-2 top-1 bottom-1 rounded-3xl bg-white/50
          backdrop-blur-md items-center justify-between  max-w-[1240px] py-1 
          sm:duration-300 sm:mx-2 xl:mx-auto
          dark:bg-slate-800/70">
          <Link 
            to="/" 
            className="font-Lobster sm:text-xl md:text-2xl lg:text-3xl text-white py-2 px-1"
          >
            LinkRoot
          </Link>
          <div className="hidden relative sm:flex">
            <Search />
          </div>
          <ul className="hidden md:flex">
            <li>
              {
                isAuthenticated && <Link to="/profile">Profile</Link>
              }
            </li>
            <li>
              {
                isAuthenticated ? <LogoutButton /> : <LoginButton />
              }
            </li>
          </ul>
          <div onClick={ handleNav } className='block md:hidden'>
            { nav ? <AiOutlineClose size={20} /> : <AiOutlineMenu size={20} /> }
          </div>
        </div>
      </div>
      <ul 
        className={
          nav 
          ? "fixed pt-16 left-0 top-0 w-full h-full bg-white/50 backdrop-blur-md ease-in-out duration-500 sm:w-[30%] dark:bg-slate-900/50 z-40"
          : 'fixed pt-16 top-0 h-full ease-in-out duration-500  left-[-100%]'
        }
      >
        <li className="sm:hidden flex my-2 ">
          <Search />
        </li>
        <li className="my-2">
          {
            isAuthenticated && <Link to="/profile">Profile</Link>
          }
        </li>
        <li className="my-2">
          {
            isAuthenticated ? <LogoutButton /> : <LoginButton />
          }
        </li>
      </ul>

    </>
  )
}