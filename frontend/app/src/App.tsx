import "./App.css";

import { LoginButton, LogoutButton, Profile } from "./components";

export const App = () => {
  return (
    <div className="App">
      <Profile />
      <LoginButton />
      <LogoutButton />
    </div>
  );
};
